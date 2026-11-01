# II.B bulk overlap moment (D >= eps*m): precise statement, roadmap, honest difficulty

Lead, 2026-06-28. This is the LONE remaining gap for the non-Gaussian universality upper bound
(II.B). The small/intermediate-D range is proved distribution-free (notes/IIB_overlap_smallD.md,
integrated as prop:small-D-negligible); the per-pair 2D anti-concentration is proved
(notes/IIB_lemma_2D.md, lem:two-proj). What remains:

## Statement
Work in F^D (F in {R,C}), D >= eps*m. Let g_1,...,g_{D-1} be iid, mean 0, isotropic
(E g g^* = I_D), sub-Gaussian, independent of a fixed unit e. W = span{g_i}, u_T the unit normal
to W, rho = <e,u_T>. Then
   E[(1-|rho|^2)^{-d_F/2}] = E[||P_W e||^{-d_F}] <= 1 + C/D,
matching the Gaussian/Haar value (Beta law). [It suffices to get 1+o(1) for D=Theta(m).]

## Key identities (clean, verified)
- 1 - |rho|^2 = ||P_W e||^2 = e^* P_W e   (since W^perp = span u_T is 1-dimensional).
- ||P_W e||^2 = b^*(G^*G)^{-1} b, where b_i = <g_i, e>, G = [g_1 ... g_{D-1}] (D x (D-1)).
- Equivalently 1-|rho|^2 = dist(e, W)^2 = det Gram(g_1,...,g_{D-1},e) / det Gram(g_1,...,g_{D-1}).

## Why the typical value is right (heuristic, makes 1+C/D plausible)
||P_W e||^2 ~ 1 - 1/D in mean: E||P_{W^perp} e||^2 = E|rho|^2. With nearly-orthonormal frame
ĝ_i, ||P_W e||^2 ~ sum_i |<e,ĝ_i>|^2, and E|<e,ĝ_i>|^2 = E[|<e,g_i>|^2/||g_i||^2] ~ 1/D, summed
over D-1 terms ~ 1 - 1/D. So (1-|rho|^2)^{-d_F/2} ~ (1-1/D)^{-d_F/2} ~ 1 + d_F/(2D) typically.

## Why it is HARD (the real obstruction; do not fake)
The negative moment is governed by the LOWER tail P{||P_W e||^2 <= y} = P{|<e,u_T>|^2 >= 1-y},
i.e. the event that the fixed e is nearly aligned with the random NULL direction u_T of the
(D-1)-column matrix G. Two genuine difficulties at D=Theta(m):
1. Aspect ratio -> 1: G is D x (D-1), so G^*G is hard-edge ill-conditioned (smallest eigenvalue
   -> 0 like (1-sqrt((D-1)/D))^2). So (G^*G)^{-1} is large; ||P_W e||^2 = b^*(G^*G)^{-1}b is a
   ratio that can be small when b aligns with the bottom eigenvector of G^*G.
2. The crude per-vector bound ||P_W e||^2 >= max_i |<e,ĝ_i>|^2 gives the right tail EXPONENT
   ((D-1)/2) but a constant (C sqrt(D))^{D-1} that blows up (the sqrt(D) threshold from ||g_i||~sqrt D
   compounds). This is exactly the poly(m)-not-1 failure noted in IIB_assembly.md. The bound must
   use the JOINT geometry (e nearly perpendicular to the WHOLE span), not the product over single
   vectors.

## Correct route (the right tools; a genuine sub-project, ~a lemma's worth of RMT)
- The needed input is anti-concentration of <e,u_T> for the null vector u_T of a sub-Gaussian
  matrix in a FIXED direction e: P{|<e,u_T>|^2 >= 1-y} <= (C y)^{c D}. This is "no-gaps
  delocalization" / null-vector anti-concentration (Rudelson--Vershynin invertibility +
  Rudelson "no-gaps delocalization for general random matrices", 2016). Delocalization alone
  (||u_T||_inf small) is NOT enough; one needs the small-ball of a single fixed linear functional
  of u_T near its extreme, which the no-gaps machinery supplies.
- Combined with Gram concentration (matrix Bernstein for sum g_i g_i^* on the (D-1)-frame) to
  pin the typical value, and the 1+c*E|rho|^2 expansion on {||P_W e||^2 > 1/2}, this should give
  E[(1-|rho|^2)^{-d_F/2}] <= 1+C/D. Each piece is standard; assembling the sharp constant is the work.
- Cleanest hypothesis to target first: sub-Gaussian isotropic g_i (covers iid sub-Gaussian rows).
  Bounded-density-only may need an extra anti-concentration input; state hypotheses explicitly.

## Status
- prob:pc (as reframed by the user) is now EXACTLY this bulk estimate. Two of three ingredients
  proved; this third is a well-defined hard-edge RMT lemma, not yet closed. Do NOT claim II.B
  proved until this is done. It is the right target for a dedicated future round (or a short
  standalone companion lemma) using the no-gaps delocalization tools above.
