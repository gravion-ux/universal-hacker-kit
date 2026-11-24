"""Integrity tests for the Universal Hacker Kit plugin package.

The kit ships configuration and prose, not application code — so the
suite validates the package the way a user experiences it: every JSON
manifest parses and agrees with the others, every skill carries valid
frontmatter, the SessionStart hook points at a file that exists, and
the documentation's own claims (skill count, relative links) are true.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_JSON = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE_JSON = ROOT / ".claude-plugin" / "marketplace.json"
HOOKS_JSON = ROOT / "hooks" / "hooks.json"
README = ROOT / "README.md"
SKILLS_DIR = ROOT / "skills"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---"), f"{path} has no YAML frontmatter"
    block = text.split("---", 2)[1]
    fields = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def skill_dirs():
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())


# --- Manifests -----------------------------------------------------------

def test_all_json_files_parse():
    for path in (PLUGIN_JSON, MARKETPLACE_JSON, HOOKS_JSON):
        load_json(path)


def test_plugin_manifest_required_fields():
    plugin = load_json(PLUGIN_JSON)
    for field in ("name", "version", "description", "license"):
        assert plugin.get(field), f"plugin.json is missing '{field}'"


def test_plugin_version_is_semver_shaped():
    version = load_json(PLUGIN_JSON)["version"]
    assert re.fullmatch(r"\d+\.\d+\.\d+", version), version


def test_marketplace_lists_the_plugin():
    plugin = load_json(PLUGIN_JSON)
    marketplace = load_json(MARKETPLACE_JSON)
    entries = marketplace.get("plugins", [])
    assert entries, "marketplace.json lists no plugins"
    assert entries[0]["name"] == plugin["name"]
    assert entries[0]["source"] == "."


def test_license_file_matches_manifest():
    plugin = load_json(PLUGIN_JSON)
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if plugin["license"].startswith("GPL"):
        assert "GNU GENERAL PUBLIC LICENSE" in license_text
    elif plugin["license"].startswith("MIT"):
        assert "MIT License" in license_text


# --- Skills --------------------------------------------------------------

def test_every_skill_has_a_skill_file():
    dirs = skill_dirs()
    assert dirs, "no skill directories found"
    for d in dirs:
        assert (d / "SKILL.md").is_file(), f"{d.name} has no SKILL.md"


def test_skill_frontmatter_is_valid_and_matches_directory():
    for d in skill_dirs():
        fields = frontmatter(d / "SKILL.md")
        assert fields.get("name") == d.name, (
            f"frontmatter name '{fields.get('name')}' != directory '{d.name}'"
        )
        assert len(fields.get("description", "")) > 40, (
            f"{d.name} description is missing or too short to trigger on"
        )


def test_skill_bodies_are_substantive():
    for d in skill_dirs():
        body = (d / "SKILL.md").read_text(encoding="utf-8")
        assert len(body) > 800, f"{d.name}/SKILL.md looks like a stub"


def test_skill_count_matches_documented_claims():
    count = len(skill_dirs())
    words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
    heading = f"**{words[count]} skills:**"
    assert heading in README.read_text(encoding="utf-8"), (
        "README skill-count heading is stale"
    )


def test_manifest_descriptions_agree():
    plugin = load_json(PLUGIN_JSON)
    marketplace = load_json(MARKETPLACE_JSON)
    assert plugin["description"] == marketplace["plugins"][0]["description"]


def test_skill_reference_files_exist_and_are_nonempty():
    for ref in SKILLS_DIR.rglob("references/*"):
        if ref.is_file():
            assert ref.stat().st_size > 200, f"{ref} looks empty"


# --- Hooks ---------------------------------------------------------------

def test_session_start_hook_points_at_a_real_file():
    hooks = load_json(HOOKS_JSON)
    groups = hooks["hooks"]["SessionStart"]
    assert groups, "no SessionStart hook configured"
    commands = [
        h["command"]
        for g in groups
        for h in g["hooks"]
        if h.get("type") == "command"
    ]
    assert commands, "SessionStart hook has no command"
    joined = " ".join(commands)
    assert "always-on-rules.md" in joined
    assert (ROOT / "always-on-rules.md").is_file()


# --- Documentation ---------------------------------------------------------

def test_readme_relative_links_resolve():
    text = README.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path = (ROOT / target.split("#")[0]).resolve()
        assert path.exists(), f"README links to missing file: {target}"
