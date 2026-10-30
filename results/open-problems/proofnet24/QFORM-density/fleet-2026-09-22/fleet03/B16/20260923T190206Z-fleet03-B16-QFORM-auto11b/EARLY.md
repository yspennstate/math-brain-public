SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-23T19:02:06Z.
attacking: close the zero-Rayleigh endpoint and remove the Schur-sign restriction in the true near-coloop projection-product reduction, while keeping the original physical hub as the genuine smoothing source.

# Early substantive calculation

Programme: `QFORM-DENSITY-3EIG-20260922`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Full QFORM remains OPEN; global continuity remains OPEN.

Work in the inherited exact-rank-three B16 hard chamber

`A=R Lambda R^T`, `R^T R=I_3`, `D=|det Lambda|>=1`,

with physical hub row `r_0=sqrt(c)e`, `c>63/64`, and every leaf transverse leverage `<1/64`. Rotate only the deterministic transverse spectral plane so

`Lambda=[[a,b,0],[b,u,v],[0,v,w]]`.

Write leaf rows as `(s_j,p_j,q_j)` and the leaf projections

`S=sum s_j X_j`, `U=sum p_j X_j`, `V=sum q_j X_j`.

Then the physical quadratic is exactly

`Q=a(sqrt(c)X_0+S)^2+2b(sqrt(c)X_0+S)U+uU^2+2vUV+wV^2`.      (E1)

The leaf coefficient vectors for `(U,V)` are orthonormal, and each physical leaf row has leverage `p_j^2+q_j^2<1/64`.

## 1. A dependence-safe scalar replacement

Put

`Y=X_0+S/sqrt(c)`.

Although `Y` need not be independent of `(U,V)`, its conditional law given `(U,V)` has density at most one. Indeed, conditional on `(U,V)=z`, let `mu_z` be any regular conditional law of `S`. Since the original physical coordinate `X_0` is independent of every leaf,

`p_(Y|U,V=z)(y)=int f_0(y-s/sqrt(c)) mu_z(ds)<=1`.              (E2)

This is a genuine convolution/translation cap inherited from one untouched physical source. It is not a conditional projection-density claim.

Equation (E1) becomes

`Q=acY^2+2b sqrt(c) YU+uU^2+2vUV+wV^2`.                        (E3)

## 2. The exact zero-Rayleigh endpoint is paid

If `a=0`, (E3) is a zero-pivot quadratic in `(Y,U,V)` with coefficient matrix

`G_0=[[0,b sqrt(c),0],[b sqrt(c),u,v],[0,v,w]]`.

Its determinant is

`det G_0=-c b^2 w=c det Lambda`,                                (E4)

so `|det G_0|=cD`. The two-dimensional orthogonal product projection `(U,V)` has joint density at most `2` by the Livshyts--Paouris--Pivovarov projection theorem, while (E2) supplies conditional scalar cap `K=1`.

Applying the completed `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1` theorem therefore gives

`||p_Q||_infinity <=3*2^(4/3) (cD)^(-1/3)
                   <3*2^(4/3)(64/63)^(1/3)
                   <7.6`.                                      (E5)

Thus the true near-coloop endpoint `a=0` is closed for arbitrary rough cap-one inputs without declaring `(Y,U,V)` independent. Essential boundedness is proved; continuity is not claimed by this route.

## 3. Direct application of designated partner fleet04/B16 when a!=0

For `a!=0`, complete the square in the same untouched physical hub:

`Q=ac[X_0+S/sqrt(c)+bU/(a sqrt(c))]^2 + (U,V)^T B (U,V)`,      (E6)

where

`B=[[u-b^2/a,v],[v,w]]`,
`det B=det Lambda/a`.                                           (E7)

This is exactly the scope of fleet04/B16 theorem `QFORM-HEAVY-FRESH-TRANSVERSE-CROSS-LIFT-v1`: take the fresh bank `J={0}`, so its reserved direction has physical coefficient one; take the leaf bank as `I`, `P=(U,V)`, and `det(MM^T)=1`; take `gamma=ac` and the shift in (E6) as the allowed `a^T X_I` term. The partner theorem yields the actual inequality

`||p_Q||_infinity <=128 c^(-1/2)(|a|D)^(-1/4)`.                 (E8)

No transformed random coordinates are asserted independent.

## 4. Diffuse-leaf sharpening removes the sign restriction

Treat (E1) as a quadratic polynomial in the genuine physical scalar `X_0`. Its root discriminant divided by four is

`c K_t`, where

`K_t=(b^2-au)U^2-2avUV-awV^2+a t
    =(U,V)^T H_a(U,V)+a t`,

`H_a=[[b^2-au,-av],[-av,-aw]]`.                                 (E9)

The exact determinant identity is

`det H_a=a det Lambda`.                                         (E10)

For fixed leaves, the cap-one density of `X_0` and the two-root formula give

`p_(Q|leaves)(t) <=c^(-1/2) (K_t)_+^(-1/2)
                  <=c^(-1/2)|K_t|^(-1/2)`                      (E11)

on the set where roots exist. Since every `(U,V)` projection row has leverage `<1/64<1/2`, the diffuse case of the completed rank-two affine half-Riesz theorem gives, for either signature of `H_a`,

`sup_s E |(U,V)^T H_a(U,V)-s|^(-1/2)
 <=4 sqrt(2e) |det H_a|^(-1/4)`.                               (E12)

Combining (E10)--(E12),

`||p_Q||_infinity
 <=4 sqrt(2e)c^(-1/2)(|a|D)^(-1/4)`.                           (E13)

This is sign-free. In particular,

`|a|D>=2^(-12)  =>  ||p_Q||_infinity<76`,                       (E14)

because `c>63/64`. The previous general nonzero-pivot payment on this threshold was `<1033`; the same branch is now paid by a factor over thirteen smaller using the actual projection-product geometry.

The only exact-rank-three true-near-coloop Rayleigh collar left by this calculation is therefore

`0<|a|D<2^(-12)`,                                               (E15)

together with the already-recorded B16 ultra-collar structural survivors. The endpoint `a=0` is no longer part of that debt.

Sources actually used: fleet04/B16 `yspennstate/math-open-problems@48d2f4234b05dfa527f1119c2c3dfc4a4b941f5d`; rank-two affine half-Riesz `@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`; zero-pivot conditional trace `@1bbe7c7c194bc92e10fc9c3cb3eb548d65e7043d`; current B16 ultra-collar compiler `@f6f7e407aea4977e9b061d90eefd8e692d3191ed`.
