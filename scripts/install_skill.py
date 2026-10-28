#!/usr/bin/env python3
"""Install this producer's runtime files through its local WorkBlock envelope."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

MANAGED_FILE = "SKILL.md"
MANAGED_DIRS = ("agents", "assets", "references")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(root: Path) -> dict[str, Path]:
    result = {}
    main = root / MANAGED_FILE
    if main.is_symlink() or not main.is_file():
        raise ValueError(f"Missing or linked Skill entry: {main}")
    result[MANAGED_FILE] = main
    for name in MANAGED_DIRS:
        folder = root / name
        if folder.is_symlink() or (folder.exists() and not folder.is_dir()):
            raise ValueError(f"Invalid managed directory: {folder}")
        if not folder.exists():
            continue
        for base, dirs, files in os.walk(folder, followlinks=False):
            for child in dirs + files:
                path = Path(base) / child
                if path.is_symlink():
                    raise ValueError(f"Linked payload path: {path}")
            for child in files:
                path = Path(base) / child
                if child == ".DS_Store" or "__pycache__" in path.parts or path.suffix == ".pyc":
                    continue
                result[path.relative_to(root).as_posix()] = path
    return result


def inspect(source: Path, targets: list[Path]) -> tuple[dict[str, Path], list[dict]]:
    source = source.resolve()
    resolved = [p.resolve() for p in targets]
    for index, root in enumerate(resolved):
        if root == source or root.is_relative_to(source) or source.is_relative_to(root):
            raise ValueError("Consumer and producer overlap")
        for other in resolved[:index]:
            if root == other or root.is_relative_to(other) or other.is_relative_to(root):
                raise ValueError("Consumers overlap")
    source_files = payload(source)
    plans = []
    for target in targets:
        if not target.exists() or not target.is_dir():
            raise ValueError(f"Consumer root must already exist: {target}")
        installed = payload(target)
        changed = [r for r, p in source_files.items() if r not in installed or digest(p) != digest(installed[r])]
        stale = sorted(set(installed) - set(source_files))
        plans.append({"target": str(target), "changed": sorted(changed), "stale": stale})
    return source_files, plans


def install(source: Path, targets: list[Path]) -> list[dict]:
    # Inspect all targets before the first write, including every managed symlink.
    files, plans = inspect(source, targets)
    for target, plan in zip(targets, plans):
        for rel in plan["changed"]:
            dest = target / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(dir=dest.parent, delete=False) as handle:
                    temporary = Path(handle.name)
                    handle.write(files[rel].read_bytes())
                os.chmod(temporary, files[rel].stat().st_mode & 0o777)
                os.replace(temporary, dest)
                temporary = None
            finally:
                if temporary is not None:
                    temporary.unlink(missing_ok=True)
        for rel in plan["stale"]:
            (target / rel).unlink()
    verify(source, targets)
    return plans


def verify(source: Path, targets: list[Path]) -> list[dict]:
    _, plans = inspect(source, targets)
    if any(p["changed"] or p["stale"] for p in plans):
        raise ValueError("Consumer runtime payload does not match producer")
    return plans


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("plan", "apply", "verify"))
    args = parser.parse_args()
    project = Path(__file__).resolve().parents[1]
    source = project / "skills/paper-reading-intake"
    action = json.loads((project / ".workblock/actions/install.json").read_text())
    if action.get("action") != "install" or action.get("onFailure") != "stop":
        raise ValueError("Invalid install action identity")
    targets = [Path(value) for value in action["targets"]]
    if not targets or any(not p.is_absolute() for p in targets):
        raise ValueError("Install targets must be absolute local directories")
    if set(action["targets"]) != set(action["permissions"]["write"]):
        raise ValueError("Install targets differ from write permissions")
    if set(action["targets"]) != set(action["permissions"]["delete"]):
        raise ValueError("Stale managed-file cleanup is not registered")
    if action["permissions"]["network"]:
        raise ValueError("This installer does not use network authority")
    if args.mode == "apply":
        plans = install(source, targets)
    elif args.mode == "verify":
        plans = verify(source, targets)
    else:
        _, plans = inspect(source, targets)
    print(json.dumps({"mode": args.mode, "writes": args.mode == "apply", "targets": plans}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
