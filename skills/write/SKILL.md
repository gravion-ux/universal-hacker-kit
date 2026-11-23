---
name: write
description: Report structure and per-section rules for writing up a confirmed bug bounty finding, for any platform (HackerOne, Bugcrowd, Intigriti, YesWeHack, Patchstack). Use when the hunter is drafting — "help me write this up", "what sections do I need", "structure this finding", "here are my notes".
---

# Write the Report

Your job: turn the hunter's verified notes into a report a triager can
validate in one pass. You propose wording from their facts; the hunter
stays the author and must be able to defend every sentence.

Before anything else: the draft header records the program, the asset,
and the **dedupe verdict** (from the `dedupe` skill). No verdict, no
drafting.

## Body sections, in order

1. **Summary** — two or three sentences: what the bug is, where it
   lives, what it lets an attacker do *that was demonstrated*. No
   class definitions, no CWE lecture.
2. **Background / discovery notes** *(short, optional)* — how it was
   found, in lab-notes voice. Dead ends are credibility; keep them.
   One paragraph at most.
3. **Steps to reproduce** — numbered, atomic, one observable action
   per step. State preconditions first: account role, auth state,
   victim interaction, browser/app version. At the step where the bug
   shows itself, write expected vs actual.
4. **Proof of concept** — the minimal raw HTTP request/response pairs
   that prove it (curl is acceptable; a script only when the bug
   genuinely needs one — races, long chains). Redact session tokens
   and real user data with `[REDACTED]`; never redact the parts that
   prove the bug. Screenshots/video support visual or multi-step
   proof, always paired with the request behind them.
5. **Impact** — only demonstrated outcomes, stated bottom-up: "the
   request in step 3 returned user B's email and phone for account A".
   If the chain stops at reflection, the impact stops at reflection.
6. **Remediation** *(optional)* — include only when it is specific to
   this code ("encode `q` before it is reflected in `search.php`").
   Generic advice ("validate input") is deleted, not written.
7. **References** *(optional)* — only a pointer a triager would
   otherwise have to hunt for: the exact vendor advisory, the precise
   technique write-up. One line each. Never a CWE restatement — the
   platform form already carries the CWE/CVE fields.

## Platform fields (form, not body) — check them anyway

- **Title** — `<class> in <location> via <parameter/route>`, under 100
  characters, zero marketing words. "Stored XSS in profile bio via
  POST /settings" beats "Critical vulnerability in your platform".
- **Asset** — copied from the program's scope list, not from memory.
- **Severity / CVSS** — score Base metrics only, each metric justified
  by a verified precondition (if self-registration is open, PR is
  None, not Low; if the ID is a random UUID the hunter happened to
  know, AC is High). Leave Temporal/Environmental to the program.
- **Platform notes** — HackerOne: keep the body self-contained, the
  form's fields don't render your markdown attachments inline.
  Bugcrowd: map the claim to their VRT category in the summary line.
  Intigriti: their form separates "endpoint" and "proof" — keep the
  PoC complete in the body anyway. Patchstack/WordPress: name the
  plugin, the exact version, and the required role in the first lines.

## Anti-patterns to refuse

- A section that exists but is empty, "TBD", or "see PoC".
- Steps written as narration ("then I exploited the flaw").
- An Impact section longer than the PoC that supposedly proves it.
- A severity vector that contradicts the stated preconditions.
- Filling a missing fact with a confident guess. Ask instead.
