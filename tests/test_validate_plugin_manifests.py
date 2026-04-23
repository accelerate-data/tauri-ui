from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_plugin_manifests import validate


def write_manifest(root: Path, relative_path: str, **overrides: object) -> None:
    manifest = {
        "name": "backend-skills",
        "description": "Backend coding standards for Rust, Tauri, and Node sidecar architecture.",
        "version": "1.0.1",
        "author": {"name": "Accelerate Data"},
        "repository": "https://github.com/accelerate-data/backend-skills",
        "license": "MIT",
        "skills": "./skills",
    }
    manifest.update(overrides)
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest), encoding="utf-8")


def write_valid_pair(root: Path) -> None:
    write_manifest(root, ".claude-plugin/plugin.json")
    write_manifest(root, ".codex-plugin/plugin.json")


class ManifestValidationTests(unittest.TestCase):
    def test_valid_manifest_pair_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            write_valid_pair(root)

            self.assertEqual(validate(root), [])

    def test_codex_name_must_match_plugin_identity(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            write_valid_pair(root)
            write_manifest(root, ".codex-plugin/plugin.json", name="ad-backend")

            errors = validate(root)

        self.assertIn(".codex-plugin/plugin.json: expected name 'backend-skills', found 'ad-backend'", errors)
        self.assertIn("manifest mismatch: 'name' differs between Claude and Codex", errors)

    def test_codex_version_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            write_valid_pair(root)
            codex_path = root / ".codex-plugin/plugin.json"
            codex = json.loads(codex_path.read_text(encoding="utf-8"))
            del codex["version"]
            codex_path.write_text(json.dumps(codex), encoding="utf-8")

            errors = validate(root)

        self.assertIn(".codex-plugin/plugin.json: missing required field 'version'", errors)
        self.assertIn(".codex-plugin/plugin.json: version must be a semver string like 1.2.3", errors)


if __name__ == "__main__":
    unittest.main()
