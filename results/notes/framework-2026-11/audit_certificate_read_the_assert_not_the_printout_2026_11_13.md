---
name: audit_certificate_read_the_assert_not_the_printout_2026_11_13
description: "[VERIFIED] Auditing an exact certificate script (Codex STRAT runs): judge it by what its assert covers and what it reads, not by the lines it prints - non-PSD rows at a diagnostic point can be harmless, a fast run can be honest; check both before flagging or trusting"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T12:51:19+02:00
  status: provisional
  evidence: ""
---

Seen 13 Nov 2026 on T104 STRAT16 (2+5 split carrier, Mac mini 1). rank_two_certificate.py printed 'g 1 ... not PSD 5/9' for 12 subcones and then PROVED. Reading the code: the assert covers only g=0 and g=gmax; g=1 is a diagnostic. That is sound because J/5+g vv^T is a segment inside the convex set K_u, and the separately certified concavity on K_u makes T* concave in g, so the endpoints suffice. Codex's LOG said the same ('certificate insufficiency, not a counterexample'). tree_certificate.py ran in 0.35 s for ~2,100 coefficients; suspicious, but it recomputes in sympy's sparse QQ ring and writes tree_checks.json without ever reading it.

**Why:** a printed failure line looks like a gap and a fast run looks like a cache replay; either misread wastes a tick or, worse, waves through a certificate that never checked anything.

**How to apply:** for each certificate script, (1) grep the assert/exit conditions and list exactly which cases they cover, (2) for every printed failure, say which proved fact makes it irrelevant, or flag it, (3) grep for json/read_text/open/load to confirm results are recomputed, not read back, (4) replay from a frozen copy with hashes recorded, and diff against the live scripts before the write-up. Related: [[t104_5plus1_class_all_n_proved_strat15_2026_11_13]], [[agents_audit_check_scars_smell_test_2026_07_31]].

Second instance, same day: disconnected_certificate.py argued in a comment that the projection rank is 2, 3 or 4. I flagged rank 5 (edge + scaled K5), where the bracket 2k(k-5) vanishes at N=7, as an unexplained exclusion. One tick later it was my misreading: the script's scope is DISCONNECTED five-parts, whose rank is at most 3, so the total is at most 4; and the h >= 1 claim follows because every component of a projection Laplacian is I - J/n_c. So add (5): before flagging an excluded case, read the script's docstring and final PROVED line for its scope, and test the excluded case against that scope. Flag only what is in scope and still unexplained.
