---
name: gotchas
description: Per-vulnerability-class minimum proof, automatic N/A traps and classic overclaims. Apply the relevant section before any severity is claimed — "what do triagers need to see for XSS", "is this IDOR submittable", "SSRF gotchas", or when a draft's claimed class doesn't match its PoC.
---

# Class Gotchas

For the claimed class: state the minimum proof, whether the PoC clears
it, and any overclaim to cut. Each class also lists what is routinely
closed as N/A on major platforms.

## Reflected XSS
- **Minimum:** unencoded reflection of a working payload in an HTML/JS
  context, executed in a real browser, on the in-scope domain.
- **N/A traps:** self-XSS (only the attacker is affected), reflection
  inside JSON that never renders, `javascript:` links needing the
  victim to paste, payload firing only in the hunter's own session.
- **Overclaim:** "session hijacking" without a session actually being
  affected — HttpOnly and modern token storage usually end the chain
  at the alert.

## Stored XSS
- **Minimum:** payload persists and fires for a *different* user (or
  an admin view) without that user doing anything unusual.
- **N/A traps:** stored only in the attacker's own private view;
  requires a privileged victim to hunt down an obscure page nobody
  visits (state the realistic viewer, or expect downgrade).
- **Overclaim:** worm/ATO language for a payload that fires in one
  low-traffic field.

## DOM XSS
- **Minimum:** source→sink trace (location/hash/postMessage → innerHTML
  etc.) plus the payload firing from a deliverable URL.
- **N/A traps:** sink reachable only with DevTools manipulation.

## IDOR / BOLA
- **Minimum:** two accounts (A and B). A's session reads or changes
  B's object by swapping the identifier. Show both objects' ownership
  and the cross-access response.
- **N/A traps:** public objects by design; sequential IDs with no
  sensitive data behind them; "access" to the attacker's own data
  under a second ID they control end-to-end (use genuinely separate
  accounts and state how they were obtained — program test accounts
  where provided).
- **Overclaim:** "full database dump" from one swapped ID; write-IDOR
  severity for a read of a non-sensitive field.

## Broken access control / privilege escalation
- **Minimum:** a lower-role session performing a named higher-role
  action, with the action's effect shown (not just a 200).
- **N/A traps:** UI-hidden but documented API behaviour; role
  differences the program defines as intended.

## SQL injection
- **Minimum:** demonstrated data extraction or a reliable boolean/time
  differential across multiple controlled trials — not a lone error.
- **N/A traps:** WAF error pages, framework stack traces, a single
  slow response. Blind claims need the differential table.

## SSRF
- **Minimum:** the server making a request the attacker controls —
  proven by a callback to an attacker listener, or a readable internal
  response. State which of the two.
- **N/A traps:** the server fetching a public URL is the feature
  working; DNS-only pings prove resolution, not request forgery
  impact; cloud metadata claims without the metadata response.

## CSRF
- **Minimum:** a cross-site request that changes state on a sensitive
  action, with the victim's session, absent/ineffective token checks,
  and SameSite reality addressed.
- **N/A traps:** CSRF on logout, preferences, or any non-state-changing
  endpoint; self-CSRF.

## Authentication flaws
- **Minimum:** the bypass completed — logged in, reset, or 2FA passed
  — on an account the hunter controls as the "victim".
- **N/A traps:** rate-limit absence alone (no successful brute force),
  verbose login errors without an enumeration payoff, password-policy
  complaints.

## Race conditions
- **Minimum:** the invariant broken and the benefit captured (double
  credit spent, limit exceeded) with parallel-request evidence.
- **N/A traps:** duplicate cosmetic records; races needing unrealistic
  timing windows.

## CORS misconfiguration
- **Minimum:** a cross-origin page actually reading a sensitive
  response with the victim's credentials — PoC page included.
- **N/A traps:** reflected Origin without credentialed data access;
  wildcard on public endpoints.

## Information disclosure
- **Minimum:** the disclosed data is non-public and sensitive, shown
  in the response itself.
- **N/A traps:** version banners, public emails, directory listings of
  public files, stack traces alone (usually informational at best).

## Open redirect
- **Minimum:** attacker-controlled redirect on a trusted domain, plus
  the program must accept the class — many cap or exclude it.
- **N/A traps:** redirects requiring the victim to already be on a
  phishing page with no trust gain; chains into OAuth theft claimed
  but not demonstrated.

## SSTI / XXE / file inclusion / RCE
- **Minimum:** engine/file/command evidence — arithmetic evaluated by
  the template engine, the file's contents returned, command output in
  the response. An error message is a lead, not proof.
- **N/A traps:** self-XSS-style self-injection; sandbox escapes claimed
  from a version banner.
