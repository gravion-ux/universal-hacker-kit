# Contributing to Universal Hacker Kit

Thanks for helping! Universal Hacker Kit is a discipline kit for bug
bounty hunters — **dedupe first, evidence only, lab-verified,
scope-bound** — built from a working hunter's own method. It is plain
markdown throughout: four skills, an always-on rules file, and a
`SessionStart` hook that does nothing but print those rules into
context.

The most valuable contributions are sharper skill instructions backed
by real triage experience, per-platform field corrections, and tests
that pin the package's integrity rules down.

## Ground rules

- **Authorised testing only — the kit's whole premise.** Content must
  never instruct a hunter (or an assistant) to test outside a
  programme's scope, skip dedupe, inflate impact beyond what a PoC
  demonstrates, or submit an unverified claim. Contributions that
  weaken the discipline layer will not be merged.
- **No invented platform rules.** Claims about a platform's fields,
  severity caps, or policies must be verifiable against that
  platform's own programme pages or documentation. If you cannot
  point to the source, mark it as field experience, not as a rule.
- **Plain markdown, no tooling lock-in.** Skills must stay readable
  and usable by any assistant that can read a rules file — no
  Claude-Code-only machinery inside `skills/` beyond the documented
  invocation names.
- **The hook stays trivial.** `hooks/hooks.json` may only print
  `always-on-rules.md`. No network, no writes, nothing else — ever.

## Repository layout

- `skills/<name>/SKILL.md` — one skill per folder (`dedupe`,
  `gotchas`, `triage`, `write`). Each `SKILL.md` starts with YAML
  front matter: `name` (matching the folder) and a `description`
  that states what the skill does and the phrases that should
  trigger it.
- `always-on-rules.md` — the discipline layer loaded every session.
- `.claude-plugin/plugin.json` + `marketplace.json` — the plugin
  manifest. The manifest, the README's "**Four skills:**" section,
  and the folders under `skills/` must always agree — the test suite
  checks this.
- `tests/test_plugin_integrity.py` — the integrity suite (13 tests):
  manifest validity, skill presence, front-matter shape, and
  README/manifest agreement.

## Development setup

There is nothing to build and no runtime dependency. You need
Python 3.10+ and pytest to run the tests:

```bash
git clone https://github.com/gravion-ux/universal-hacker-kit.git
cd universal-hacker-kit
pip install pytest
```

## Running the tests

```bash
python -m pytest tests/ -q
```

That is exactly what CI runs (Python 3.12). All 13 integrity tests
must pass before a change can be merged.
