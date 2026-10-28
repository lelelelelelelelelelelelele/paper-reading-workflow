#!/usr/bin/env python3
"""Read-only install precondition: local main must equal published origin/main."""
import argparse
import json
from pathlib import Path
import subprocess
from urllib.parse import urlparse


def require_published(local_ref, local_head, remote_rows):
    rows = [row.split() for row in remote_rows.splitlines() if row.strip()]
    if local_ref != "refs/heads/main":
        raise ValueError("Install only from the landed main branch")
    if rows != [[local_head, "refs/heads/main"]]:
        raise ValueError("GitHub main differs from local main; synchronize before installing")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git", default="git")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]

    def git(*command):
        return subprocess.check_output(
            [args.git, "-C", str(root), *command], text=True, timeout=45
        ).strip()

    # Restrict the network operation to the registered public GitHub host.
    url = git("remote", "get-url", "origin")
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != "github.com" or parsed.username:
        raise ValueError("Expected an HTTPS GitHub origin without embedded credentials")
    local_ref = git("symbolic-ref", "HEAD")
    head = git("rev-parse", "HEAD")
    published = git("ls-remote", "--exit-code", "origin", "refs/heads/main")
    require_published(local_ref, head, published)
    print(json.dumps({"status": "published", "origin": url, "ref": local_ref, "commit": head}))


if __name__ == "__main__":
    main()
