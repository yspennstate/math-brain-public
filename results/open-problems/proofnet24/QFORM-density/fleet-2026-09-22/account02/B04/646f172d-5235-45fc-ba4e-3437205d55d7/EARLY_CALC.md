SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T08:20:12Z.
attacking: the surviving one-anchor exact-rank-two Schur collar by combining an independent physical square's uniform L^3 Fourier budget with the full rank-two projected-crossing envelope, before any local minor inversion.

# Early calculation: square L3 x critical rank-two crossing

Programme: `QFORM-DENSITY-3EIG-20260922`.

The newest designated partner account03/B04 r53 pays the whole overlap-two `J_2` packet and leaves the localized overlap-one class `J_1^*` as the first distinct debt. The account02/B20 rank-two compiler exhibits a genuine pure-Schur stress state with a small physical square and a large exact-rank-two crossing. The calculation below pays the exact starless endpoint of that stress by a different integrated-Fourier mechanism.

Let `X_0` be one original coordinate, independent of two disjoint product banks `X_R,X_C`. Let `b!=0`, let `N=A[R,C]` have exact rank two with nonzero singular values `s_1,s_2`, put `p=s_1s_2`, and allow arbitrary measurable same-bank real functions `F_R,F_C`. Assume the physical anchor has no quadratic edges to `R union C`; edges to already-conditioned outside coordinates may remain and only translate its square. After conditioning outside coordinates the law has the form

`Q=b(X_0-a)^2+F_R(X_R)+2 X_R^T N X_C+F_C(X_C)+const.`

For a cap-one variable `Z`, the density `h` of `Z^2` satisfies `h(y)<=y^(-1/2)` and

`int h^(3/2) <= E|Z|^(-1/2) <=4+1=5`.

With Fourier convention `hat h(t)=int e^(ity)h(y)dy`, Hausdorff--Young gives

`|| E exp(it b Z^2) ||_3 <= (2 pi)^(1/3) 5^(2/3) |b|^(-1/3).`  (E1)

The checked arbitrary-internal-function exact-rank crossing theorem at `math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `NEW_PROJECTED_CROSSING.md`, gives for the remaining two-bank scalar output `S`

`|phi_S(t)| <= min(1,K/|t|),`
`K=pi (M_R M_C)^(1/2) p^(-1/2) <=2 pi p^(-1/2)`,                 (E2)

because the two-dimensional orthonormal projections of cap-one product banks have density caps `M_R,M_C<=2`.

The anchor is genuinely independent of both banks, hence `phi_Q=phi_(bZ^2) phi_S` up to a constant phase. If `m_K(t)=min(1,K/|t|)`, then

`int m_K(t)^(3/2) dt=6K`, so `||m_K||_(3/2)=(6K)^(2/3)`.          (E3)

Holder, (E1)--(E3), and Fourier inversion therefore give

`||p_Q||_infinity
 <=(2pi)^(-1)(2pi)^(1/3)5^(2/3)|b|^(-1/3)(12pi p^(-1/2))^(2/3)
 =30^(2/3)(|b|p)^(-1/3).`                                       (E4)

The same calculation proves `phi_Q in L^1`, hence this branch has a continuous `C_0` density. This is an integrated product-space estimate, not a pointwise one-dimensional stationary-phase bound.

Concrete stress for the final report: take `L=2`, `m=64`, `delta=1/4`, `b=1/192`, and the `2 x 64` matrix `N` with first row all `1/4` and second row thirty-two `+1/4` followed by thirty-two `-1/4`. Then `NN^T=4 I_2`, so `p=4`, `|b|p=1/48`, and (E4) gives

`||p_Q||_infinity <=30^(2/3)48^(1/3)=35.088212858554385...`.

Put diagonal `delta` on both source banks and no other same-bank off-diagonal coefficients. The nonzero large spectrum is exactly `delta+L=9/4` twice and `delta-L=-7/4` twice, so this is an indefinite target-valid physical matrix with four eigenvalues of modulus >1. The tiny nonzero C-bank quadratic curvature is retained exactly; it is not deleted as a perturbation.

Next: prove the exact all-cut rank-two obstruction for pinned D/D'/D5 and ridge, globally enumerate the partner r53 `J_2(H)` currency on the same matrix, and save a deterministic check.