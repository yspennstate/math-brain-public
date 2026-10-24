# Source refresh addendum — newest designated partner

Before publication, a newer completed `account03/B01` result appeared at brain commit `00703d7b1378fd37c26de163532b2790acbdb7c4`, canonical mathematics `yspennstate/math-open-problems@e8c8cc633f1fe33ec6b568f80c5c7f68a105a159`. It supersedes the earlier partner result for compatible source-disjoint-square configurations but does not subsume the overlapping receiver-square theorem in `REPORT.md`.

## New partner theorem actually applied

For disjoint original banks `I,J,D,W`, exact rank-two `K=A_IJ` with nonzero singular values `kappa_1,kappa_2`, a nonzero vector `a` on the source-disjoint bank `D` with `sigma=|a|_2`, and arbitrary same-bank phases `F_W(X_I),G_W(X_J)`, the partner proves

`||p_Q||_infinity <= (16/3) 12^(1/4) (kappa_1 kappa_2)^(-3/8) (|lambda| sigma^2)^(-1/4)`

for

`Q=F_W(X_I)+G_W(X_J)+2X_I^T K X_J+lambda(a^T X_D+h(W))^2+c(W)`.

This is an integrated-frequency theorem: the rank-two cross packet supplies only a borderline `1/|t|` estimate and the disjoint square is used through a translation-uniform `L^3` quadratic-phase estimate. It explicitly preserves the phase-aligned-density refutation of scalar pointwise decay.

Apply it to a source-disjoint variant of the strict-N3 stress architecture from `REPORT.md`. Let `m=2^q`, `0<eta<=1/4`, `c=1+eta`; on disjoint size-`m` banks choose diffuse Walsh vectors `u_1,u_2`, `v_1,v_2`, and `w`, and let `H_m` be the normalized symmetric Sylvester-Hadamard matrix. Set

`K=c(u_1v_1^T+u_2v_2^T)`

and, on the three disjoint banks `I,J,D`,

`A_disj = [[eta H_m, K, 0], [K^T, 0, 0], [0,0, w w^T]]`.

The cross block has `kappa_1=kappa_2=c`, while the disjoint square has `lambda=1`, `sigma=1`. The same singular-value perturbation argument as in `REPORT.md` gives at least four absolute eigenvalues `>=c-eta=1`, plus the disjoint eigenvalue `1`; hence this is a full-target family. Its physical diagonals and pair determinants tend to zero with `m`, so it is strict N3 for every fixed threshold at large `m`.

The newest partner theorem therefore gives the actual target-level inequality

`||p_{X^T A_disj X}||_infinity <= (16/3)12^(1/4)c^(-3/4)`

`< 9.927 c^(-3/4) <= 9.927`.

At `eta=1/4`, `c=5/4`, this is `< 8.400`.

## Complementarity with the present run

The new theorem in `REPORT.md` instead treats an **overlapping** third curvature direction on the receiver bank itself:

`A_JJ=D+lambda w w^T`, with `w` transverse to `range(K^T)`.

That square is not source-disjoint from the `J` variables used in the rank-two cross packet, so the newest partner theorem does not directly apply. The grouped Fresnel/Brascamp--Lieb argument here pays this overlap and yields the stronger stress-family estimate `<=4.2263818466` at `eta=1/4`, under its augmented leverage/transversality hypotheses.

Thus the source refresh sharpens the proof map: the source-disjoint-square route is paid by the newest designated partner, while the genuinely overlapping receiver-square route is the new contribution of this run. The remaining structural debt is to route arbitrary strict-N3 two-sided curvature to one of these two receivers or another already-paid packet.
