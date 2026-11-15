---
name: it01_mds_even_characteristic_preprint_last_section_checked_2026_11_12
description: "MDS conjecture for even q claimed proved (arXiv 2610.28208)? Section 5 holds by hand and on computed arcs; Sections 3-4 unread; open part is odd non-prime q"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:04:28+02:00
  status: provisional
  evidence: "it01_check.out: 90 cases over F_8, F_16, F_32, 0 failures, kappa at the bound in 38; Section 5 read line by line; Sections 3-4 unread"
---

Row IT01 (linear MDS conjecture), 12 Nov 2026.

arXiv 2610.28208v1 (Bocong Chen, Jing Huang, 20 Oct 2026) claims the conjecture for every even q: n <= q + 1, except q + 2 for k = 3 and k = q - 1. Its introduction names a second independent report (P. Kumar, Palomar record PALOMAR-2026-10-15-000014, with a Lean formalization; not on arXiv, not read). With Ball's theorem for prime q the open part is odd non-prime q.

Shape of the proof: no [q + 2, k] code for 4 <= k <= q - 2. Put m = q/2, h = k - 3 <= m - 2. Local subcodes D_a of the dual, all inside the dual shortened at h coordinates (dimension q - 2h - 1); their sum has dimension at least q - 2h because its complement is at most 3 + kappa and kappa <= h - 1, where kappa = dim of (X1^m, X2^m, X3^m) : J in degree h - 2 and J is the product of the q + 2 - h lines of the projected planar arc. The margin is one dimension.

Checked here: Section 5 by hand (degrees, the Frobenius derivation identity, socle degree, the count). By computation over F_8, F_16, F_32 on real planar arcs (sub-families of the conic with nucleus, the translation hyperoval t^4, arcs grown at random), h = 1..m-1, 90 cases: the colon ideal is zero up to degree h - 3 (Lemma 5.1) and kappa <= h - 1 (Proposition 5.2) in all of them; kappa = h - 1 in 38, so the bound is sharp. Hilbert functions for q = 8, 16 symmetric and unimodal. A pencil of lines breaks Lemma 5.1 as it should; one concurrent triple does not.

Not checked: Sections 3 and 4 (the construction, inclusion (9), Proposition 4.6), Lemma 2.1 from Ball-Lavrauw Theorem 13.1, whether the cited unimodality theorem (Stanley 1978, Zanello 2006) is stated for characteristic two, Kumar's report. Since kappa = h - 1 occurs, the proof has no slack: Proposition 4.6 must hold exactly as stated.

Method worth keeping: a proof by contradiction can still be tested where its lemmas speak about objects that exist. Here the code does not exist but the planar arcs of size q + 2 - h do, so the two algebraic lemmas were testable. Look for the sub-statements about existing objects before saying a nonexistence proof cannot be checked numerically.

Two arXiv searches on 12 Nov (phrase "MDS conjecture"; "maximum distance separable" with "even characteristic") show no comment or follow-up.

Files: 06_math_research/it01_mds_agent_2026_11_12/ (IT01_CHECK.md, it01_check.py, it01_arcs_side.py, outputs). Row proposal: restate to odd non-prime q. Related: [[al04_kaplansky_zero_divisor_positive_char_finite_parts_recomputed_2026_11_12]], [[an09_fuglede_dim2_finite_sets_in_z60xz12_check_out_2026_11_12]].

