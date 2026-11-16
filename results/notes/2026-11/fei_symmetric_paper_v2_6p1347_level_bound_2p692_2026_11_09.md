---
name: fei_symmetric_paper_v2_6p1347_level_bound_2p692_2026_11_09
description: "Yes, 6.1347 (9 Nov): symmetric FEI H <= (673/250+2+1/ln2) I; level bound L <= 2.692 I for all Boolean f by interval certificate; v2 a76da72 public + emailed"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T07:29:13+04:00
  status: verified
  evidence: "github.com/yspennstate/fourier-entropy-influence-symmetric a76da72; check_all 22 PASS; certificate 7058 cells max 2.6919998948"
superseded_by: symmetric_fei_best_constant_4p650431_v4_1_repo_23b66aa_2026_11_09
---

Yes, 6.1347 (9 Nov 07:3x, an agent): every symmetric Boolean f has H <= (673/250 + 2 + 1/ln 2) I = 6.1346950409 I.

Public: github.com/yspennstate/fourier-entropy-influence-symmetric, v1 commit 99b82ee (6.1908, ~07:05), v2 commit a76da72 (6.1347, 11 pages).

What moved the constant: FSYM07 (Codex, gpt-6.1-sol) sharpened the level-entropy bound L <= log2(4+e) I (Lemma 2.1 of arXiv:2610.16069) to L <= 2.692 I for EVERY Boolean f. It is the same Gibbs-against-geometric argument with r = 147/100, keeping exact h(eps) and dividing by the exact edge-isoperimetric bound 2p log2(1/p). This leaves F(p) < 2.692 on 0 < p <= 1/2. The end cases q = log2(1/p) in [1,2] (< 2.646) and q >= 32 (< 2.590) are done by hand. The middle range is an mpmath.iv certificate, 45 digits, 7,058 dyadic cells, max upper 2.6919998948. Rerun in a copy: same. My own grid gives sup F = 2.69173 at r = 1.47 (r = 1.48 the same), so this method is at its floor; any further gain in L needs a new idea. Symmetric L/I max seen is 2.51755 (AND/OR n = 6).

FSYM30's audit of v1 found no gap in either theorem and flagged 10 items; 8 went into v2 after numeric checks:
- non-strict abstract;
- parent bound h(t) <= 3 + ln(t + 1/6) via the triangular density, max excess -3.3e-9 on [1e-8, 1e8];
- the E1 lower bounds in an appendix;
- certificate JSON rounded outward (bound 4.636423665923149);
- majority B/I -> 2/ln 2 via arcsine, integral = 2, B/I 2.8747 at m = 1e5;
- the OD14 cite;
- "principal constants" wording;
- h'' at t != 1.
Rejected: removing the Math Brain acknowledgement paragraph and the MathBrainPaper cite (the author's standing format; the path papers/math-brain-2026-10-24 exists).

check_all.py: 22 PASS. Theorem D (limsup Delta_1/I_1 <= 4.6364) is unchanged.

Open: an explicit cutoff for the restriction step (FSYM04 n0 = 1e4, FSYM18 n0 = 3e4, neither closes it); whether the symmetric constant is 4.

See also [[fei27_fixed_left_origin_bound_large_z_and_cofactor_zero_single_or_open_2026_11_09]], [[fei_paper_duplicate_two_machines_same_theorem_2026_11_09]].

