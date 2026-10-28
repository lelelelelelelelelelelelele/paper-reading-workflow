import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("install_skill", Path(__file__).resolve().parents[1] / "scripts/install_skill.py")
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.source, self.a, self.b = (base / n for n in ("producer", "a", "b"))
        for root in (self.source, self.a, self.b):
            root.mkdir()
            (root / "SKILL.md").write_text("old")
        (self.source / "SKILL.md").write_text("new")
        (self.source / "assets").mkdir()
        (self.source / "assets/figure.html").write_text("new figure")

    def test_install_preserves_consumer_metadata_and_exports_only_runtime(self):
        for root in (self.a, self.b):
            (root / ".git").mkdir()
            (root / ".git/HEAD").write_text("consumer history")
            (root / ".workblock").mkdir()
            (root / ".workblock/WORKITEM.md").write_text("frozen record")
            (root / "unrelated.txt").write_text("keep")
            (root / "assets").mkdir()
            (root / "assets/stale.html").write_text("obsolete runtime")
        (self.source / "tests").mkdir()
        (self.source / "tests/private.txt").write_text("not runtime")
        INSTALLER.install(self.source, [self.a, self.b])
        INSTALLER.verify(self.source, [self.a, self.b])
        for root in (self.a, self.b):
            self.assertEqual((root / "SKILL.md").read_text(), "new")
            self.assertEqual((root / ".git/HEAD").read_text(), "consumer history")
            self.assertEqual((root / ".workblock/WORKITEM.md").read_text(), "frozen record")
            self.assertEqual((root / "unrelated.txt").read_text(), "keep")
            self.assertFalse((root / "tests").exists())
            self.assertFalse((root / "assets/stale.html").exists())

    def test_second_target_symlink_stops_before_first_target_changes(self):
        (self.b / "assets").symlink_to(self.source / "assets", target_is_directory=True)
        with self.assertRaises(ValueError):
            INSTALLER.install(self.source, [self.a, self.b])
        self.assertEqual((self.a / "SKILL.md").read_text(), "old")

    def test_source_or_consumer_overlap_is_rejected(self):
        for targets in ([self.source], [self.a, self.a], [self.a, self.a / "nested"]):
            with self.subTest(targets=targets), self.assertRaises(ValueError):
                INSTALLER.inspect(self.source, targets)

    def test_plan_does_not_write_and_verify_detects_drift(self):
        _, plans = INSTALLER.inspect(self.source, [self.a, self.b])
        self.assertIn("SKILL.md", plans[0]["changed"])
        self.assertEqual((self.a / "SKILL.md").read_text(), "old")
        with self.assertRaises(ValueError):
            INSTALLER.verify(self.source, [self.a, self.b])


if __name__ == "__main__":
    unittest.main()
