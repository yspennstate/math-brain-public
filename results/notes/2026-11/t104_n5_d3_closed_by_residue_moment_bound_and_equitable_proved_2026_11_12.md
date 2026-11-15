---
name: t104_n5_d3_closed_by_residue_moment_bound_and_equitable_proved_2026_11_12
description: "[VERIFIED] T104 n=5 D=3 closed (residue moment bound m4<=p+(3+5p)m3^2/4 + weight bound); equitable q=3,4 proved; X1+X2>=2S5 false at 1,2,2"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T23:28:57+02:00
  status: provisional
  evidence: ""
---

T104 (Alon) stratum claim T = X1 + X2 + X3 - 2S5 >= 0, 12 Nov 2026, push 131 (979a81c, c4ee712) in 06_math_research/t104_alon_agent_2026_11_11.

n = 5, D = 3 is closed: T >= g/9 with G = g vv'. The step that worked is a moment bound from nonnegative residues: with a = max v_i, b = -min v_i, p = ab, r_i = (a - v_i)(b + v_i) >= 0 sum to 5p - 1, and weighted Cauchy-Schwarz on sum v_i r_i and sum v_i^2 r_i gives m4 <= p + (3+5p) m3^2/4. The edge-weight constraint enters only as p <= (2+g)/(20g). Without the weights the bracket goes negative (-14 in my scan), so any proof of a rank-one stratum that ignores w_ij >= 0 is doomed. Try the same residue trick on n = 5, D = 2 (rank-two G) next.

Equitable partitions into 3 or 4 blocks are proved (block contrasts on top). For q = 4, and q = 3 with no singleton, X1 >= 2S5 alone, since tau = 1/a + 1/b <= D/2 across blocks. Block sizes 1,a,b need X3. X1 + X2 >= 2S5 is false there: an exact 1,2,2 graph has margin -143/10000. My earlier equitable test (43 q = 3 instances) never hit it; 371 instances restricted to 1,a,b found -2.0e-2. Lesson: a random test over mixed block sizes undersampled the one shape where the stronger inequality fails. Sample each structural case separately before conjecturing.

Audit: Codex STRAT3 wrote the proofs; t104_strat3_audit.py checked every identity in sympy (all 0), the moment bound, min bracket 9.75 over 1313 feasible pairs, bound (12) tight to 3e-16 on 371 graphs, and the 1,2,2 example exactly. D = 2 worst ratios with 60 starts: 0.937, 0.835, 0.794 at n = 5, 6, 7. Still open: D = 2, 3 with a top space not spanned by block contrasts.

