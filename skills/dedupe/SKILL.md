---
name: dedupe
description: Dedupe verifier for bug bounty findings. Run BEFORE drafting any report. Searches the platform's own disclosures, vendor changelogs and patch diffs, CVE/advisory databases, public write-ups and the hunter's own history, then returns a verdict — CLEAR, LIKELY DUPLICATE or CONFIRMED DUPLICATE — with the evidence for it. Triggers on "is this a duplicate", "dedupe this", "check if this is known", "has this been reported", or before any report drafting starts.
---

# Dedupe Verifier

A duplicate report earns nothing and costs reputation. This check runs
before drafting, every time. A finding is not "new" because the hunter
found it independently — it is new only if nobody has reported or
disclosed it before.

## Inputs needed

- The exact asset (domain, app, plugin + version, endpoint).
- The vulnerability class and the precise mechanism (parameter, route,
  required role/state).
- The platform the report would go to.

If any of these is vague, pin it down first. Dedupe on a fuzzy
description produces false confidence.

## The five checks (run all five, in this order)

1. **The platform's own search.** Search the target platform's
   disclosed reports / hacktivity for the asset + class. This is the
   authoritative source — public mirrors and search engines miss
   reports. If the platform requires sign-in to search, say so and use
   the signed-in session; never conclude "clear" from a public mirror
   alone.
2. **The vendor's own paper trail.** Changelog, release notes and the
   patch diff between the last two versions. If the newest release
   "fixes a security issue" anywhere near this mechanism, diff it —
   the bug may already be fixed and disclosed.
3. **CVE / advisory databases.** Patchstack's vulnerability database,
   Wordfence Intelligence, NVD, GitHub Advisory Database, CVE.org —
   search asset + version + class. A CVE assigned to the same mechanism
   in the same or an earlier version ends the hunt for this finding.
4. **Public write-ups and search.** Blogs, X/Twitter posts, YouTube
   walkthroughs, other hunters' portfolios. An undisclosed-but-public
   write-up means the race is already lost or will be.
5. **The hunter's own history.** Their submitted, closed and duplicate
   reports on every platform. Self-duplicates happen — check before
   the platform does.

## Verdicts

Return exactly one, with the evidence listed under it:

```
VERDICT: CLEAR | LIKELY DUPLICATE | CONFIRMED DUPLICATE

Evidence:
- Platform search: [what was searched, what was found]
- Vendor trail: [changelog/diff result]
- CVE/advisory: [result]
- Public write-ups: [result]
- Own history: [result]
```

- **CONFIRMED DUPLICATE** — a prior report, CVE or vendor fix covers
  the same asset + mechanism. Stop. Do not draft. If the prior
  disclosure is partial (different parameter, different role, a bypass
  of the fix), say exactly what differs — a genuine variant is a new
  finding, but the burden of difference is on the hunter.
- **LIKELY DUPLICATE** — strong signals (a fix release, a similar
  disclosed report on a sibling asset) but not a proven match. Draft
  only with the risk stated at the top, or park it.
- **CLEAR** — all five checks ran and found nothing. Note which
  sources were actually reachable; an unreachable source is a hole in
  the check, not a pass.

## Hard rules

- Never declare CLEAR from fewer than the five checks.
- A search that returned nothing because it could not run (sign-in
  wall, broken page, rate limit) is reported as NOT RUN, not as empty.
- Record the verdict in the draft's header so triage can see it.
