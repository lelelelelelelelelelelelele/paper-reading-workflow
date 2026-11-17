# CLI usage

The helper dispatches to the installed DeepTutor CLI. Use the Python interpreter from that installation's environment, with `DEEPTUTOR_HOME` pointing to its runtime. On the Mac where this entry point was verified, the known installation is:

```sh
dt_deployment="$HOME/Documents/Codex/2026-10-25/note-skill-knowledge-design/work/deeptutor-deployment"
dt_python="$dt_deployment/.venv/bin/python"
export DEEPTUTOR_HOME="$dt_deployment/runtime"
```

Use a different already-configured runtime when appropriate. Check that its CLI and runtime exist. If running on a different machine, resolve that machine's paths. The helper does not set up DeepTutor or provider accounts.

Set `dt_skill` to the directory containing this Skill. List registered workspaces and inspect the chosen session or Notebook in its own scope. General has an empty scope ID, so pass `--workspace ""` when using it.

```sh
"$dt_python" "$dt_skill/scripts/learning.py" workspaces
"$dt_python" "$dt_skill/scripts/learning.py" --workspace "$dt_workspace" session list
"$dt_python" "$dt_skill/scripts/learning.py" --workspace "$dt_workspace" session show "$dt_session" --format json
"$dt_python" "$dt_skill/scripts/learning.py" --workspace "$dt_workspace" session rename "$dt_session" --title "$dt_title"
"$dt_python" "$dt_skill/scripts/learning.py" --workspace "$dt_workspace" notebook list
"$dt_python" "$dt_skill/scripts/learning.py" --workspace "$dt_workspace" notebook show "$dt_notebook" --format json
```

For a new session, omit `--session "$dt_session"`. Write the task and only the relevant source excerpts to a UTF-8 prompt file. Use manageable page ranges rather than passing whole long PDFs as one message.

```sh
umask 077
"$dt_python" -u "$dt_skill/scripts/learning.py" --workspace "$dt_workspace" \
    --prompt-file "$dt_prompt" run chat --session "$dt_session" --language zh --format json \
    > "$dt_events" 2> "$dt_errors"
```

Use the learner's language. Put the prompt, event log and stderr in a private working directory. Run the CLI as a background tool session if necessary and poll that same process through completion. Track `session_id` and `turn_id` from the events as soon as they appear. The CLI can exit successfully after a model failure. For the same turn, verify a `done` event with `metadata.status == "completed"` and a nonempty `result.metadata.response`. Use that response when saving the draft. If a run stops early, check the events and `session show` (or scoped history for a first turn). Resume with the same ID once the prior turn has ended. Avoid starting another session or saving a partial response.

On 1.6.15 the helper sets the visible-output idle timeout to 300 seconds inside the CLI process. It also sets connection and read timeouts for the `cl100k_base` tokenizer download so a cold cache can fall back to DeepTutor's approximate token counting if the download fails. These settings affect only the CLI process. Wait for an active command in the chosen workspace to exit before sending another command there. The helper rejects overlapping calls in that workspace.

For organizing notes or revising them, add `--draft` before `run chat`. The 1.6.15 drafting turn uses the prompt and conversation without model tool calls. This keeps DeepTutor's built-in Notebook tool from saving before Codex has checked the draft.

If there is no suitable Notebook, create one in the chosen workspace and retain its ID. Use a single Notebook for the session's draft.

```sh
"$dt_python" "$dt_skill/scripts/learning.py" --workspace "$dt_workspace" notebook create "$dt_title"
"$dt_python" "$dt_skill/scripts/learning.py" --workspace "$dt_workspace" save-md \
    "$dt_notebook" "$dt_session" "$dt_markdown" --title "$dt_title"
```

`save-md` uses the same DeepTutor Notebook service as `add-md` and `replace-md`. It resolves its record within the Notebook by the DeepTutor session ID stored in native record metadata. Replaying the same draft returns the same record. On revision, pass `--record "$dt_record"` and save the full revised Markdown. A mismatched ID stops the write. For a pre-existing note created outside this entry point, verify its Notebook and record IDs and use the native `notebook replace-md NOTEBOOK RECORD FILE` when the user means to update that record.

Upstream command reference: [DeepTutor CLI](https://github.com/HKUDS/DeepTutor/blob/a31d82624c27d75f4e771d4fcb78dce16470b383/SKILL.md).
