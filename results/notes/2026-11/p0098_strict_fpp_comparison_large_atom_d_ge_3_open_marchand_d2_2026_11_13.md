---
name: p0098_strict_fpp_comparison_large_atom_d_ge_3_open_marchand_d2_2026_11_13
description: "[PROVISIONAL] P0098 strict FPP time-constant comparison when F(r) >= oriented p_c: Marchand AAP 2002 did d=2; d>=3 open, no paper found"
metadata:
  type: project
status: provisional
---

P0098 on the 200 list (Auffinger-Damron-Hanson, 50 years of FPP): if G is strictly more variable than F (increasing
concave order) and the minimum support point r > 0 has F(r) >= p_c of oriented percolation, is the axial time constant
of G strictly smaller in d > 2?

Literature checked 13 Nov 2026 (web search plus arXiv abstracts; no full text read):
- van den Berg-Kesten (Ann. Appl. Probab. 1993): strict inequality in all d >= 2, but only when F(r) < oriented p_c
  (r > 0), or F(0) < bond p_c (r = 0).
- Marchand, "Strict inequalities for the time constant in first passage percolation", Ann. Appl. Probab. 12 (2002)
  1001-1038: Z^2, removes that condition for the axial direction in the supercritical oriented case, and gives an
  upper bound there. The proof is two-dimensional.
- Gorski, arXiv 2208.13922: the van den Berg-Kesten theorem on graphs of polynomial growth and quasi-trees, still
  under a subcriticality hypothesis.
- Jacquet, arXiv 2412.20779: strict FPP < directed-FPP time constants on Z^d; a different comparison.
- Jahnel-Koppl-Luchtrath-Vu, arXiv 2605.28766: convex order alone fails for first contact percolation; not FPP on Z^d.
- No d >= 3 extension of Marchand found.

Status: OPEN for d >= 3. Why it is hard: with F(r) above oriented p_c, the r-edges percolate in an oriented cone, so
mu(x) = r|x|_1 in the cone (Durrett-Liggett flat edge) and the comparison is equality there. The axial direction sits
outside the cone in d = 2. In d >= 3 one must show e_1 stays outside the cone and that local modifications still pay
on axial geodesics. Possible paper target, but the d = 2 argument has to be read first to see what is planar.
