---
name: c0134_positive_cookie_ballisticity_resolved_two_audits_2026_11_13
description: "C0134 positive excited walk ballisticity (KZ13 Problem 5.3): second independent audit MINOR, no math error; counts as resolved; funding lines unverified (the author's call)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T02:28:27+02:00
  status: verified
  evidence: "C0134R REPORT.md first line MINOR, brain commit 6e4186bb, ledger e8a87262"
---

C0134 (Kosygina-Zerner 2013, Problem 5.3: can (BD) be replaced by (POS1) in the 1-d ballisticity criterion?) now counts as RESOLVED under the ledger rule: two independent audits kept the answer YES (speed 0 for delta <= 2, positive for delta > 2, delta = infinity included; iid stacks, nonnegative drifts, weak ellipticity, no stack-tail condition).
- Paper: https://github.com/yspennstate/positive-cookie-ballisticity (13 Oct 2026).
- Audit 1: an agent, 13 Oct. Audit 2: Codex gpt-6.1-sol high run C0134R on Mac mini 1, 13 Nov, verdict MINOR, no mathematical correction; it read the survey's exact definitions (arXiv 1204.1895v2 pp. 3-4, 20) and found no silent use of bounded stacks or finite moments in the critical proof. Report: brain 06_math_research/referee_reports/2026-11-13/C0134R/REPORT.md (commit 6e4186bb); ledger row e8a87262.
- The positive-speed half follows from truncation plus monotonicity; the new content is the zero-speed argument at delta = 2 for unrestricted stacks.
- Open minor revisions: add a revision date (the paper cites things dated after 13 Oct); give Chakhtoun's 2019 CUNY dissertation theorem and tail condition precisely; the referee could not verify the funding lines (ISF 4101/25, the Simons collaboration name, cloud credit, corporate support) - those are the author's to confirm, not an agent's to edit.
How to apply: count C0134 as solved in totals; do not re-audit it; route the wording fixes to the paper agent and the funding question to the author.

