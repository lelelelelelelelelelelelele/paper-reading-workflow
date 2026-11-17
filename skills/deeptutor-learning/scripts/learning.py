"""Run the installed DeepTutor CLI with the reading workspace pinned."""

import argparse
import asyncio
from functools import partial
import json
from importlib.metadata import version
from pathlib import Path
import sys


def configure_chat():
    """Keep DeepTutor 1.6.15 compatibility changes local to a chat process."""
    from deeptutor.agents.loop import agent_loop
    from tiktoken import load
    import requests

    agent_loop._STREAM_IDLE_TIMEOUT_SECONDS = 300.0
    read_file = load.read_file
    encoding_url = "https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken"
    unavailable = False

    def read_encoding(path):
        # tiktoken still owns cache lookup and verifies the encoding hash.
        if path != encoding_url:
            return read_file(path)
        nonlocal unavailable
        if unavailable:
            raise OSError("cl100k_base download unavailable in this process")
        try:
            response = requests.get(path, timeout=(5, 15))
            response.raise_for_status()
            return response.content
        except requests.RequestException:
            unavailable = True
            print("Tokenizer download failed. DeepTutor will estimate token counts.", file=sys.stderr)
            raise

    load.read_file = read_encoding


def save_markdown(workspace, arguments):
    """Upsert a session's Markdown record using the same backend as notebook CLI."""
    parser = argparse.ArgumentParser(prog="learning.py save-md")
    parser.add_argument("notebook")
    parser.add_argument("session")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--record", help="Expected existing record ID when revising")
    args = parser.parse_args(arguments)
    body = args.markdown.read_text(encoding="utf-8")
    if not body.strip():
        parser.error("Markdown is empty")

    from deeptutor.app import DeepTutorApp
    client = DeepTutorApp(workspace_id=workspace)
    if asyncio.run(client.get_session(args.session)) is None:
        parser.error("session was not found in this workspace")

    notebook = client.get_notebook(args.notebook)
    if notebook is None:
        parser.error("notebook was not found in this workspace")
    matches = [
        record for record in notebook["records"]
        if (record.get("metadata") or {}).get("codex_learning_session") == args.session
    ]
    if len(matches) > 1:
        parser.error("multiple records match the session; resolve them before saving")
    current = matches[0] if matches else None
    if args.record and (current is None or current["id"] != args.record):
        parser.error("expected record does not match in this workspace and notebook")
    if current is None:
        result = client.add_record(
            notebook_ids=[args.notebook],
            record_type="chat",
            title=args.title,
            user_query="",
            output=body,
            metadata={"codex_learning_session": args.session},
        )
        record_id = result["record"]["id"]
        action = "created"
    else:
        record_id = current["id"]
        action = "unchanged"
        if current["output"] != body:
            client.update_record(args.notebook, record_id, output=body)
            action = "updated"
    notebook = client.get_notebook(args.notebook)
    saved = next(
        (record for record in (notebook or {}).get("records", []) if record["id"] == record_id),
        None,
    )
    if saved is None or saved["output"] != body:
        raise SystemExit("Notebook read-back failed; check the same notebook before retrying")

    print(json.dumps({
        "workspace_id": workspace,
        "session_id": args.session,
        "notebook_id": args.notebook,
        "record_id": record_id,
        "markdown": str(args.markdown.resolve()),
        "action": action,
    }, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", help="DeepTutor workspace ID (empty string selects General)")
    parser.add_argument("--prompt-file", type=Path, help="UTF-8 prompt for run chat")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="DeepTutor CLI command")
    args = parser.parse_args()

    from deeptutor.services.workspace import get_content_workspace_service
    from deeptutor.services.workspace.context import workspace_context

    if args.command == ["workspaces"]:
        print(json.dumps(get_content_workspace_service().list_workspaces(), ensure_ascii=False))
        return

    if args.workspace is None:
        parser.error("--workspace is required for a learning command")
    from deeptutor_cli.main import app
    from deeptutor_cli.common import console
    from filelock import FileLock, Timeout

    command = args.command
    if command[:2] == ["run", "chat"] and version("deeptutor") == "1.6.15":
        configure_chat()
    if command[:2] in (["session", "show"], ["notebook", "show"]):
        # The CLI's JSON read-back uses Rich and can wrap within a JSON string.
        if ("--format", "json") in zip(command, command[1:]) or "--format=json" in command:
            console.print = partial(console.print, soft_wrap=True, markup=False, emoji=False)
    if args.prompt_file:
        if command[:2] != ["run", "chat"]:
            parser.error("--prompt-file requires run chat")
        # Use the end-of-options marker so prompt text cannot be parsed as flags.
        command = command + ["--", args.prompt_file.read_text(encoding="utf-8")]

    # The CLI's Session and Notebook subcommands lack --workspace in 1.6.15.
    with workspace_context(args.workspace) as scope:
        lock = FileLock(str(scope.content_root / ".codex-learning.lock"), timeout=0)
        try:
            with lock:
                if command[:1] == ["save-md"]:
                    save_markdown(scope.workspace_id, command[1:])
                else:
                    app(args=command, prog_name="deeptutor")
        except Timeout as exc:
            if exc.lock_file != lock.lock_file:
                raise
            raise SystemExit("A Codex DeepTutor command is running in this workspace. Wait for it.") from None


if __name__ == "__main__":
    main()
