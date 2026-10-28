# account03/B05 — scalar-conditioned rank-three core supremum is not uniformly bounded

**Run:** `20260922T181101Z-account03-B05-QFORM-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_ROUTE_CORRECTION / EXPLICIT PRODUCT-LAW COUNTEREXAMPLE TO SCALAR-WORST-FIBER BRIDGE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and the implication tested

The full owner target remains open: for every dimension, every independent real input family with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal bound for the essential density of `Q=X^TAX`, or give a valid target counterexample. Continuity is a separate desired conclusion.


`Q=Q_3+Q'`

in spectral coordinates, where `Q_3` uses three large eigen-directions and `Q'` is the remaining quadratic part. The proposed worst-fiber quantity is

`M = sup_b || p_{Q_3 | Q'=b} ||_infinity`.

If `M` were universally bounded, then mixing would immediately bound the density of `Q`. This report tests that first missing implication before using it.

The result is negative: **`M` is not universally bounded**, even in dimension four, even when all four eigenvalues have modulus exactly one, and even on a determinant-rich rank-three spectral frame. This refutes the scalar **worst-conditioned-fiber** bridge, not the full QFORM conjecture.

The live corrections against pointwise van der Corput, post-rotation independence, naive vector-fiber suprema, conditional-cap substitution, and fixed-good-minor extraction are all respected. No moment, support-connectivity, log-concavity, or Gaussian assumption is used.

The designated partner `account04/B05` was checked at its canonical QFORM math and handoff roots immediately before this derivation; no completed current-QFORM artifact was present, so no result is fabricated for that slot. A completed compatible account04 theorem is applied quantitatively in Section 7: account04/B16 `QFORM-NESTED-HEAVY-ZERODIAG-ATOM-v1` / its fixed-pair determinant identity, canonical source

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

## 2. A four-dimensional cap-one product source

Fix an integer `m>=2` and set

`E_m = union_{k=0}^{m-1} [10k, 10k+1/m]`.

Let the original physical coordinates be independent with densities

`f_1 = 1_{E_m}`,

`f_2=f_3=f_4=1_[0,1]`.

Each density is between zero and one and has total mass one.

Introduce the orthonormal basis of `R^4`

`v=(1,1,1,1)/2`,

`t=(3,-1,-1,-1)/sqrt(12)`,

`u=(0,1,-1,0)/sqrt(2)`,

`w=(0,1,1,-2)/sqrt(6)`.

Let

`Z=v dot X`,

`T=t dot X`, `U=u dot X`, `W=w dot X`,

and define

`Q_3 = T^2+U^2-W^2`,

`Q' = Z^2`.

Thus the full form is

`Q=Q_3+Q' = X^T A X`,

where

`A=tt^T+uu^T-ww^T+vv^T = I_4-2ww^T`.

Consequently the spectrum of `A` is exactly `{1,1,1,-1}`. This is a legitimate target matrix with four eigenvalues of modulus one. The rank-three core has spectrum `{1,1,-1}`.

## 3. Exact conditional coordinates

Write

`s=X_2+X_3+X_4`.

For the last three coordinates use the orthogonal planar coordinates

`u=(X_2-X_3)/sqrt(2)`,

`w=(X_2+X_3-2X_4)/sqrt(6)`.

The inverse formulas are

`X_2=s/3+u/sqrt(2)+w/sqrt(6)`,

`X_3=s/3-u/sqrt(2)+w/sqrt(6)`,

`X_4=s/3-2w/sqrt(6)`,

and

`dX_2 dX_3 dX_4 = (1/sqrt(3)) ds du dw`.

Since

`Z=(X_1+s)/2`,

at fixed `z` one has `s=2z-X_1`, and the joint density in coordinates `(X_1,u,w,z)` is

`(2/sqrt(3)) 1_{X_1 in E_m} 1_{(u,w) in D_{2z-X_1}}`,

where `D_s` is the image of the cube section

`{(X_2,X_3,X_4) in [0,1]^3 : X_2+X_3+X_4=s}`.

Let `p_S` be the Irwin--Hall density of `S=X_2+X_3+X_4`. Then

`p_Z(z)=2 integral_{E_m} p_S(2z-x) dx`.                                  (3.1)

The global maximum of `p_S` is `3/4`.

## 4. Select one packet and keep a common two-dimensional square

Let

`I_m=[10,10+1/m]`,

`c_m=10+1/(2m)`,

`z_m=(c_m+3/2)/2`,

and consider the positive-length interval

`J_m=[z_m-1/(8m), z_m+1/(8m)]`.

For every `z in J_m`, the condition `0<=s=2z-X_1<=3` selects **only** the packet `I_m` from `E_m`. Indeed the packet near zero would require `s>3`, while every packet beginning at `20` or later gives `s<0`.

For `x in I_m`, write `x=c_m+d`, so `|d|<=1/(2m)`. Then, uniformly for `z in J_m`,

`9/8 <= s=2z-x <=15/8`.                                                (4.1)

Equation (3.1) and `p_S<=3/4` therefore give

`p_Z(z) <= 3/(2m)`.                                                     (4.2)

Hence the conditional density of `(X_1,u,w)` given `Z=z` satisfies, everywhere on its support,

`rho_{X_1,u,w | Z=z} >= 4m/(3sqrt(3))`.                                (4.3)

Now put `r=1/8`. The square

`R=[-r,r]^2`

is contained in every `D_s` for the range (4.1). This follows directly from the inverse formulas: with `s/3 in [3/8,5/8]`, the maximum `u,w` displacement in `X_2,X_3` is

`r(1/sqrt(2)+1/sqrt(6))<0.14`,

and the maximum displacement in `X_4` is `2r/sqrt(6)<0.103`.

Thus every scalar-conditioned fiber contains the same fixed hyperbolic rectangle `R` with conditional mass density at least the quantity in (4.3).

## 5. Hyperbolic coarea on the common square

For `h in R`, define the raw coarea density

`K(h)= integral_R delta(h-(u^2-w^2)) du dw`.

Use the linear change

`a=u-w`, `b=u+w`,

whose Jacobian is `du dw=(1/2) da db`. The image of `R` is the diamond `|a|+|b|<=2r`, which contains the square `[-r,r]^2`. Therefore, for `0<|h|<r^2`,

`K(h) >= (1/2) integral_{[-r,r]^2} delta(h-ab) da db`

`       = log(r^2/|h|)`.                                               (5.1)

This is exactly the rank-two logarithmic cone singularity, but here it occurs inside a scalar-conditioned rank-three fiber.

## 6. The conditional rank-three density grows like log m

At fixed `z in J_m`, the remaining core coordinate is

`T=(3X_1-s)/sqrt(12)=(2X_1-z)/sqrt(3)`.

Set

`T_0(z)=(2c_m-z)/sqrt(3)`,

`q_0(z)=T_0(z)^2`.

For `X_1=c_m+d`,

`T=T_0+(2/sqrt(3))d`.

For every `m>=2`, every `z in J_m`, and every `|d|<=1/(2m)`, one has the uniform elementary bound

`|T^2-T_0^2| <=22 |d| <=11/m`.                                        (6.1)

Now take any

`q in [q_0(z)-1/(4m), q_0(z)+1/(4m)]`.

Then

`|q-T^2| <= 45/(4m)=11.25/m`.                                         (6.2)

Since `r^2=1/64`, for every `m>720` the right side is strictly below `r^2`. Combining (4.3), the common-square restriction, and (5.1), the conditional density satisfies for almost every such `q`

`p_{Q_3 | Z=z}(q)`

` >= (4m/(3sqrt(3))) integral_{I_m} K(q-T(x)^2) dx`

` >= (4m/(3sqrt(3))) (1/m) log( (1/64)/(45/(4m)) )`

` = (4/(3sqrt(3))) log(m/720)`.                                      (6.3)

Therefore, for every `z in J_m` and `m>720`,

`boxed( ||p_{Q_3 | Z=z}||_infinity >= (4/(3sqrt(3))) log(m/720). )`    (6.4)

The lower bound holds on a positive-length interval of output `q`, so it is an **essential-supremum** statement, not a point-version artifact.

All original variables remain independent and all physical densities remain capped by one.

## 7. Passing from Z to the scalar quadratic remainder Q'=Z^2

All four physical variables in this construction are nonnegative, hence `Z>=0`. On the positive interval `J_m`, the map

`z -> b=z^2`

is one-to-one. Consequently the regular conditional law given `Q'=b` is exactly the regular conditional law given `Z=sqrt(b)` for almost every

`b in B_m := {z^2 : z in J_m}`.

Equation (6.4) therefore gives

`boxed(
  ess sup_{b in B_m} ||p_{Q_3 | Q'=b}||_infinity
  >= (4/(3sqrt(3))) log(m/720).
)`                                                                    (7.1)

As `m -> infinity`, this tends to infinity. Hence there is no universal finite bound on

`sup_b ||p_{Q_3 | Q'=b}||_infinity`

under the hypotheses of the full QFORM target.

### Actual application of completed account04 mathematics

The failure is not caused by a weak rank-three frame. The projection onto the core subspace `E=v^perp` is

`P=I-vv^T`,

so every physical spectral row has leverage

`P_ii=3/4`,

and every pair of distinct rows has inner product

`P_ij=-1/4`.

Apply the completed account04/B16 fixed-pair identity. After choosing any first row `i`, every second row has residual leverage

`h=3/4-(1/16)/(3/4)=2/3`.

Thus its exact Gram area is

`G_ij=(3/4)(2/3)=1/2`,                                                (7.2)

and since the core has `|det Lambda|=1`, account04/B16 gives the actual determinant-bank inequality

`boxed(
 sum_{k != i,j} |det (A_core)_{ {i,j,k} }| = 1/2.
)`                                                                      (7.3)

So the scalar-conditioned blowup occurs on a uniformly nested-heavy, determinant-rich rank-three core. It cannot be repaired merely by demanding a fixed positive amount of rank-three determinant bank mass.

The exact assigned slot `account04/B05` still had no completed current-QFORM source at the source check, so (7.2)--(7.3) use the completed compatible account04/B16 result rather than inventing a B05 result.

## 8. What is refuted and the missing factor

### Refuted intermediate implication

`QFORM-SCALAR-CONDITIONED-CORE-SUP-v1` is false:

> A three-large-eigenvalue core plus an arbitrary scalar quadratic remainder does **not** have a universally bounded worst conditional core density `sup_b ||p_{Q_3|Q'=b}||_infinity`, even for a four-dimensional cap-one product law and a full matrix with spectrum `{1,1,1,-1}`.


### Precise missing factor

The lost quantity is the **unnormalized scalar-fiber mass**. In this construction each selected `Z` packet has density only of order `1/m`, while normalizing the conditional fiber multiplies its three-dimensional density by order `m`; the hyperbolic trace then retains a logarithmic cost. Taking `sup_b` discards the compensating packet weight before curvature is paid.

Therefore a viable scalar-coarea bridge must retain the factor `p_{Q'}(b)` (or an equivalent unnormalized coarea measure) together with the conditional curved trace. A representative target is an estimate directly on

`p_Q(y)= integral p_{Q'}(b) p_{Q_3|Q'=b}(y-b) db`,

using product provenance **before** taking any worst conditioned-fiber supremum. The present construction shows that no proof may replace this weighted integral by the universal bound of its normalized conditional factor.

## 9. Status

Proved here:

1. the exact four-dimensional cap-one product construction;
2. the positive-measure conditional lower bound (7.1), diverging like `log m`;
3. the failure of the scalar worst-conditioned-core bridge;
4. by direct application of account04/B16, determinant-bank mass `1/2` on the same core.

Not proved here:

- any unboundedness of the full density of `Q`;
- the full QFORM theorem;
- the desired continuous-density conclusion;
- a replacement weighted scalar-coarea theorem.

**Full QFORM conjecture: OPEN / NOT PROVED.**
