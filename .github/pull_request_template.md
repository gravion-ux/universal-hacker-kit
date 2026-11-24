## What changed

<!-- One or two sentences. What is different after this pull request? -->

## Why

<!-- Link the issue it closes, or describe the hunting situation
     behind it: platform, report stage, what went wrong. -->

## How it was tested

<!-- The exact command you ran and what it printed:
     `python -m pytest tests/ -q` (13 integrity tests, all passing).
     If you changed a skill's behaviour, also say how you exercised
     the skill itself (which assistant, what input, what verdict). -->

## Checklist

- [ ] Full integrity suite passes locally and CI is green
- [ ] If a skill was added/removed: `skills/`, `.claude-plugin/plugin.json`, and the README "**Four skills:**" section (including the count) all agree
- [ ] Skill front matter is valid YAML with `name` (matching the folder) and `description`
- [ ] The discipline layer is not weakened: no instruction to test out of scope, skip dedupe, inflate impact, or submit unverified claims
- [ ] No invented platform rules — platform claims cite the platform's own pages or are marked as field experience
- [ ] The hook still only prints `always-on-rules.md` (no network, no writes)
- [ ] No secrets or non-public programme details anywhere in the diff
- [ ] One logical change in this PR — one skill per PR is ideal
