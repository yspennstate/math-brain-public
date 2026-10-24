SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-23T17:51:00Z.
attacking: the true-near-coloop two-bank survivor by a sign-specific saddle-plus-square canonicalization that keeps the original product coordinates and isolates the single longitudinal leak.

# Early mathematical checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

Let the exact-rank-three spectral matrix satisfy `min |eig M| >= s`, and let `e` be the near-coloop hub direction. Write

`M = [[q,b^T],[b,C]]` on `e direct_sum e^perp`, with `|q|<s`, `beta=||b||`, `u=b/beta`, and let `z` be the unit vector in `e^perp` perpendicular to `u`. Put

`alpha=u^T C u`, `gamma=u^T C z`, `delta=z^T C z`.

The first unpaid implication is now sharpened by the following exact algebra.

**Lemma (`QFORM-NEARCOLOOP-ROBUST-SADDLE-SQUARE`, preliminary).**

1. `beta^2 >= s^2-q^2`.
2. `delta^2 >= s^2 + (s^2-q^2) gamma^2/beta^2`, hence `|delta|>=s`.
3. With `a=alpha-gamma^2/delta`,

`M` is congruent to `delta direct_sum B`, `B=[[q,beta],[beta,a]]`,

and `det B = det M/delta`; consequently `|det B|>=s^2` because `|delta|<=||M||op` and the product of the other two eigenvalue magnitudes is at least `s^2`.
4. In signature `(2,1)`, if `q<0` is the minority sign then `delta>0` and `B` is indefinite. Reflection gives: in signature `(1,2)`, minority `q>0` forces `delta<0` and `B` indefinite. Thus the rank-two opposite-sign saddle remains uniformly nondegenerate, and the third direction is a uniformly nondegenerate square; the logarithmic rank-two endpoint has not been hidden.

Proof of (2): `Mz=gamma u+delta z` and `Me=q e+beta u`. For `x=z-(gamma/beta)e`, `Mx=delta z-(q gamma/beta)e`. Since `s_min(M)>=s`,

`delta^2+q^2 gamma^2/beta^2 >= s^2(1+gamma^2/beta^2)`,

which is exactly (2).

For the true-near-coloop frame `r_0=sqrt(c)e`, `r_j=s_j e+w_j`, with `sum s_j^2=rho=1-c`, `sum s_jw_j=0`, `sum w_jw_j^T=I_2`, define `S=sum s_jX_j`, `U=sum <u,w_j>X_j`, `V=sum <z,w_j>X_j`, `Y=sqrt(c)X_0+S`. Then, without rotating the random variables,

`Q = delta (V+(gamma/delta)U)^2 + qY^2 + 2 beta YU + a U^2`.

This is a deterministic coefficient identity only; `(Y,U,V)` are generally dependent.

Partner account03/B11 r36 supplies disjoint original-coordinate banks `Sbank,Tbank` with transverse Grams `G_B >= I_2/32` (indeed its construction gives `det G_B>1/32`) and fixed hub-star energy on both. The shear `z -> z+(gamma/delta)u` has determinant one, so on either bank the Gram determinant of the pair `(U_B,V_B+(gamma/delta)U_B)` is exactly `det G_B`. Hence each bank retains the full third-direction area after the canonicalization; no `gamma/delta` loss occurs.

For the required pinned Claude result, Theorem C of `math-open-problems@e5f71d79.../COUNTEREXAMPLE_SEARCH.md` applies to the actual exact-rank-three form: in signature `(2,1)`, `p_Q(t)<=pi sqrt(2)` on the one-sheet side `t>=0`; after negation, signature `(1,2)` has the same bound on `t<=0`. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction prevents extending this by X-ray control alone to the opposite side.

Next: orthogonalize the leaf hub-partner against the small longitudinal direction and compute the exact one-leak normal form; the goal is to show that every coefficient except one longitudinal projection is already uniformly paid by the robust square/saddle and partner banks.
