"""Tests for the platform scope-rules dataset.

The dataset is the machine-readable scope gate: every platform entry
must carry accepted classes, exclusions, dedupe policy and
consequences, and the pre-submission checklist must stay complete.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "platform-scope-rules.json"

EXPECTED_PLATFORMS = {
    "patchstack",
    "hackerone",
    "bugcrowd",
    "yeswehack",
    "intigriti",
    "wordfence",
    "open_bug_bounty",
}

REQUIRED_FIELDS = {"scope", "accepted_classes", "out_of_scope", "dedupe", "consequences"}


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))


def test_dataset_parses_and_covers_all_platforms():
    data = load()
    assert set(data["platforms"]) == EXPECTED_PLATFORMS


def test_every_platform_has_required_fields():
    for name, entry in load()["platforms"].items():
        missing = REQUIRED_FIELDS - set(entry)
        assert not missing, f"{name} missing fields: {missing}"
        assert entry["accepted_classes"], f"{name} has no accepted classes"
        assert entry["out_of_scope"], f"{name} has no exclusions"


def test_patchstack_exclusions_carry_rule_references():
    joined = " ".join(load()["platforms"]["patchstack"]["out_of_scope"])
    for rule in ("4.2", "4.4", "4.6", "3.9"):
        assert rule in joined, f"Patchstack rule {rule} not recorded"


def test_checklist_is_complete():
    checklist = load()["pre_submission_checklist"]
    assert len(checklist) >= 10
    joined = " ".join(checklist).lower()
    for keyword in ("scope", "accepted", "exclusion", "dedupe", "poc", "cvss"):
        assert keyword in joined, f"checklist missing {keyword}"


def test_target_states_below_two_percent():
    assert "below 2%" in load()["target"]
