# Security Policy

Universal Hacker Kit is a discipline kit for **authorised** bug
bounty hunting: plain-markdown skills and an always-on rules file.
This policy covers problems **in this repository** — the kit's own
content, manifest, and hook.

## Reporting a vulnerability

Please **do not open a public issue** for a security problem in the
kit itself. Report it privately, either way:

- GitHub's private vulnerability reporting:
  <https://github.com/gravion-ux/universal-hacker-kit/security/advisories/new>
- Email: priyanshukumarthakur937@gmail.com

Please include:

- A one- or two-sentence description of the issue.
- The version or commit SHA it affects.
- The smallest reproduction you have — the skill file and the input
  that triggers the behaviour.
- The impact you believe it has.

You can expect an acknowledgement within a few days.

## Disclosure timing

Please allow **90 days** for a fix to be released before any public
disclosure. If a fix ships earlier, coordinated disclosure can happen
as soon as the fixed version is available.

## Scope

In scope — the kit itself, for example:

- The bundled `SessionStart` hook doing anything other than printing
  `always-on-rules.md` into context — no network, no writes, nothing
  else, by design. Any deviation is a vulnerability.
- Skill or rules content that instructs the assistant to bypass a
  programme's scope, skip dedupe, fabricate evidence, or submit
  unverified claims. The kit's whole point is the opposite; content
  that undermines it is a defect with security impact.
- A crafted finding/report input that makes a skill produce a report
  claiming impact the evidence does not show.

Out of scope:

- Vulnerabilities in the platforms or programmes you hunt on — those
  go to the programme itself, through its own disclosure channel.
  Never report a target's vulnerability in this repository.
- Disagreement with the method itself (the 7-Question Gate, dedupe
  order, severity discipline). That is a discussion — open a normal
  issue.

## Supported versions

Only the current `main` branch and the latest release are supported.
Older commits are kept for history, not for backports.
