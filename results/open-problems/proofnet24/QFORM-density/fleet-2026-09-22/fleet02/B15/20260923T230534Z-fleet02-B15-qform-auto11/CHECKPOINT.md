SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T23:05:34Z.
attacking: whether the grouped determinant receiver survives a nonzero leaf-leaf block, and if not how a collective Schur remainder restores the third smoothing resource before any worst-fibre supremum.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full unrestricted target remains OPEN.

Let, in original coordinates `(P1,P2,L1,L2,W_1,...,W_m)`,

`Y=m^(-1/2) sum_j W_j`,

`Q_m=(P1+L1)^2-(P2-L2)^2+Y^2`.

The matrix has spectrum `{2,-2,1,0,...,0}`, hence is literally in the owner target. On the grouped four-coordinate core, with `P=(P1,P2)` and `L=(L1,L2)`,

`C=D=diag(1,-1),   M=I_2`,

so `det M=1` although the leaf-leaf block is nonzero.

Take `P1,P2,L1,L2` iid uniform on `[-1/2,1/2]`. Then `U=P1+L1` and `V=P2-L2` are independent with triangular density `g(u)=(1-|u|)_+`. For `H=U^2`,

`h(s)=(1-sqrt(s))/sqrt(s), 0<s<1`.

Hence the four-coordinate conditional core `R=U^2-V^2` has

`p_R(t)=int_0^(1-t) h(s+t)h(s) ds` for `0<t<1`, and for `0<t<1/8`, integrating over `s in [t,1/4]` gives

`p_R(t) >= (8 sqrt(2))^(-1) log(1/(4t)) -> infinity`.

Thus **no finite density bound depending only on `det M` can extend the previous `[[C,M],[M^T,0]]` grouped receiver to arbitrary leaf curvature `D`**. Worse, conditioning on the whole `W` bank leaves only a translate of `R`, so every such worst fibre is unbounded.

The obstruction is route-level, not a QFORM counterexample. The third resource is the collective bank `Y^2`. The physical indefinite pair `(P1,P2)` has Schur complement `S=0_2 direct-sum (J_m/m)`, whose nonzero eigenvalue is one while its largest physical entry is only `1/m`. The latest fleet03/B15 physical-entry theorem therefore gives the valid but nonuniform bound `2^(13/4)m^(1/4)`. This exhibits exactly why aggregation must precede reciprocal payment.

A dimension-free repair is available when the Schur remainder is rank one. For a homogeneous form with an invertible indefinite physical pair `D_0`, Schur complement `S=sigma r r^T`, `||r||_2=1`, and `Delta=|det D_0|`, `kappa=sigma_min(D_0)`, the scalar product `T=<r,Z>` has density at most `sqrt(2)` by the one-dimensional Ball/Rogozin projection bound. Therefore

`P(|sigma T^2-a|<rho) <= 4 sqrt(rho/|sigma|)`.

Putting this `H=4|sigma|^(-1/2)` into the completed logarithmic physical-pair envelope from fleet03/B15 gives

`||p_Q||_infinity <= 8 sqrt(2) (Delta*kappa*|sigma|)^(-1/4)`.

For the displayed `Q_m`, `Delta=kappa=|sigma|=1`, so the Schur payment is uniform in `m`, despite every physical coefficient of the Schur bank being `1/m`.

The required `e5f71d79...` source will be applied in the completed report after the rough ruled bridge is rechecked. No continuity assertion is used in any height estimate above.
