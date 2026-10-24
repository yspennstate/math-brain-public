SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-24T06:02:10Z.

# Early calculation: a full physical 2x2 crossing with one untwisted bank

Target remains full QFORM-DENSITY-3EIG-20260922. This run attacks `QFORM-FIXEDSCALE-V1-PIVOT-OR-STRONGHUB-L1-v1` after consuming account03/B02 r47.

Let `U=(U1,U2)` and `V=(V1,V2)` be four literal independent original coordinates, each with density at most one. After conditioning every other original coordinate `W=w`, suppose

`Q_w = F_w(U) + 2 U^T C V + ell_w^T V + d_w`,

where `C` is an invertible physical `2x2` cross block and `F_w` is arbitrary. No quadratic term in the `V` bank is allowed in this local receiver.

For `L=C^T U+ell_w/2`,

`phi_w(t)=E_U exp(it(F_w(U)+d_w)) psi_1(2tL_1) psi_2(2tL_2)`.

Plancherel and `f_{V_j}<=1` give

`int |psi_1(2tL_1) psi_2(2tL_2)| dt <= pi |L_1L_2|^{-1/2}`.

Now `L_1L_2` is a rank-two quadratic polynomial in the two physical source variables `U`: its quadratic matrix is

`S=C [[0,1/2],[1/2,0]] C^T`, hence `|det S|=|det C|^2/4`.

The completed in-range rank-two affine half-Riesz theorem therefore gives

`E_U |L_1L_2|^{-1/2} <= 16 sqrt(30) |det S|^{-1/4} = 16 sqrt(60)|det C|^{-1/2}`.

Consequently

`int_R |phi_Q(t)|dt <= 16 pi sqrt(60)|det C|^{-1/2}`,

uniformly in every conditioned outside coefficient and arbitrary `F_w`. Thus this branch has a continuous `C0` density.

A sharper direct height bound follows by conditioning on `U`. The conditional `V`-density has height at most `1/[2 max(|L_1|,|L_2|)]`. The transformed vector `L=C^T U+ell_w/2` has a joint probability density bounded by `K=|det C|^{-1}`. Bathtub against the `l_infinity` radial kernel gives

`E [1/(2||L||_infinity)] <= 2 sqrt(K)=2|det C|^{-1/2}`.

So the same branch satisfies `||p_Q||_infinity <=2|det C|^{-1/2}`.

This extends the preceding B02 diagonal two-pair receiver to a fully entangled invertible physical `2x2` cross block, while retaining arbitrary same-bank curvature on the opposite (`U`) side. The unpaid interface is genuinely two-sided curvature: arbitrary quadratic terms in the `V` bank cannot be inserted into the per-variable Plancherel step.
