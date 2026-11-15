---
name: ge07_moving_sofa_baek_proof_parts_checked_2026_11_12
description: "Moving sofa claimed solved (Baek, arXiv 2411.19826): Gerver's sofa rebuilt, area 2.219531669 two ways; arm-length inequality, Lemma 6.5.3 and the upper bound Q (Q(G)=|G|, concave, no tested cap above) hold numerically; Chapters 2-5 and 7 unread; do not work the row as open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:41:33+02:00
  status: provisional
  evidence: "06_math_research/ge07_sofa_agent_2026_11_12/GE07_CHECK.md, ge07_check.out, ge07_q_800.out, ge07_q_1600.out; push 87f7bada3488c7d20db9e06b262cb444699f7e1e"
---

Row GE07 (moving sofa) of the general-math top-200 list has a complete claimed solution: J. Baek, "Optimality of Gerver's Sofa", arXiv 2411.19826v1 (29 Nov 2024, 119 pages). On 12 Nov 2026 the arXiv record had one version and no journal reference; acceptance and formalization were not established. D. Trela, arXiv 2610.13955 (Aug 2026), states an exact-rational certification of the Gerver-specific hypotheses (abstract only read).

What I did (12 Nov 2026): read Sections 1.1, 1.7, 1.8, 6.5, the definitions of 8.1-8.2, Section 8.3 in full, 8.4 to Theorem 8.4.3 and the statements of 8.4.4-8.5.8. By hand: (1.9) implies (1.10); m0 piecewise and increasing; both cases of Lemma 6.5.3 with exact minima 0.12782 and 0.00564; Lemma 8.3.4; the steps of Section 8.3 given Theorems 7.1.2 and 7.4.2. By computer (ge07_check.py): Gerver's sofa from Romik's Table 1, gluing and balance equations to 1e-14, area 2.219531669 by Green's theorem and 2.21953 by a column method with no shape assumption; (1.9)-(1.11) hold on Gerver's sofa with equality on the second and fourth intervals; the iteration of Section 6.5 as stated. By computer (ge07_q.py, polygons with normals on a fixed grid, Q an exact quadratic form): Q at Gerver's triple converges to the area (2.219533645, 2.219532163, extrapolated 2.219531669); area <= Q on 19 other caps up to grid error; Q below Q(Gerver) on all 19; concave on 253 segments; directional derivative at Gerver's triple at most +8e-8 (grid error) and clearly negative in several directions.

Not read: Chapters 2-5 (monotone, balanced, rotation angle pi/2), Chapter 6 apart from 6.5, Chapter 7, the proof of Theorem 8.2.4 (area <= Q) and the proofs of Section 8.5. So this is a partial check, not a verification.

Two small points in the text: the Figure 1.10 caption says three iterations give f_3 > 1 numerically, the iteration as defined first passes 1 at n = 6 (the proof uses eleven steps, unaffected); Lemma 6.5.5 is stated on (0, 1] where its proof gives (0, pi/2].

How to use: do not work on GE07 as open. Reusable tools: a rotating-hallway sofa is the cap minus the niche, its area is computable column by column from the rotation path alone; on polygons with a common normal grid, Minkowski combinations are linear in the support vector and Mamikon-type area functionals become exact quadratic forms, which makes concavity and first-order optimality testable by three evaluations per segment. Open neighbours: the ambidextrous sofa (Romik, 1.64495..., optimality open), three-dimensional corridors.

What would change this: a later version or erratum of 2411.19826, a published referee outcome, or a formalization.

