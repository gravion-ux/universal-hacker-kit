# AI-slop patterns in bug bounty reports

A practical checklist of what LLM-drafted reports get wrong, and how a
triager spots it. Apply every pattern to the draft under review.

## Fabricated specifics

- CVE IDs that don't resolve, or resolve to a different product.
- Endpoints, parameters or features that don't exist in the hunter's
  own evidence.
- Version numbers and stack details asserted without a fingerprint.
- "Common in this framework" reasoning standing in for observation.

Fix: every concrete noun in the report must trace to a request, a
response, a screenshot or the hunter's notes. Untraceable = delete.

## Theoretical impact chains

- "An attacker could then…" repeated past the demonstrated step.
- Impact nouns (account takeover, data breach, RCE) attached to a PoC
  that shows reflection, a redirect, or an error message.
- Severity vectors that assume preconditions the steps contradict.

Fix: the impact section may only restate, in outcome language, what
the PoC visibly did.

## Boilerplate mass

- Class-definition paragraphs ("XSS is a vulnerability that…").
- Generic remediation lists unrelated to the vulnerable code.
- Severity essays arguing with the platform's published caps.

Fix: cut anything that would read identically in a report about a
different product.

## Confidence without evidence

- "Confirmed", "verified", "successfully exploited" for tests that
  were reasoned about rather than run.
- Scanner output presented as manual verification.

Fix: verbs must match what was actually executed. A scanner hit is a
lead; a replayed request is a finding.
