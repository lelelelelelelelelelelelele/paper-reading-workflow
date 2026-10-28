import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    "check_published", Path(__file__).resolve().parents[1] / "scripts/check_published.py"
)
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class PublicationTests(unittest.TestCase):
    def test_published_main_can_install(self):
        CHECK.require_published("refs/heads/main", "a" * 40, "a" * 40 + "\trefs/heads/main\n")

    def test_unpublished_or_different_main_cannot_install(self):
        for rows in ("", "b" * 40 + "\trefs/heads/main", "a" * 40 + "\trefs/heads/other"):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                CHECK.require_published("refs/heads/main", "a" * 40, rows)

    def test_unlanded_branch_cannot_install_even_with_matching_commit(self):
        with self.assertRaises(ValueError):
            CHECK.require_published("refs/heads/codex/candidate", "a" * 40, "a" * 40 + "\trefs/heads/main")
