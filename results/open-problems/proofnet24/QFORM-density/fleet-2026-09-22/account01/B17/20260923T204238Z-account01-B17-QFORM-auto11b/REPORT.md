SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T20:42:38Z.
attacking: exact finite-period arithmetic optimization of the sharp periodic cube-frame witness, including Pell-optimal periods and a dense rotated realization; then apply the completed account02/B17 global barrier to a concrete exact-spectrum comparator.

# QFORM B17 — Pell-optimal periodic witnesses and exact dense rotations

Run: `20260923T204238Z-account01-B17-QFORM-auto11b`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN**  
Continuity: no unrestricted continuity claim.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted arbitrary-product-law theorem remains OPEN. This report strengthens only the sharp-witness side. It uses no arbitrary-joint coarea cap, no post-rotation independence, and no law-uniform pointwise oscillatory decay.

## 1. Source-valid inputs

The preceding B17 periodic Edgeworth theorem is consumed from

`yspennstate/math-open-problems@a1ba664bb0eb87aa086402b959e2503a734c633d:proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T123638Z-account01-B17-qform-diffuse-edgeworth-v1/REPORT.md`.

For `J=diag(1,1,-1)`, a fixed Parseval row pattern `v_1,...,v_r in R^3`, repeated `m` times with row scale `m^{-1/2}`, and independent physical `Unif[-1/2,1/2]` variables, it proves

`p_{Q_m}(0)=3sqrt(2)[1-(20m)^{-1} sum_j E_J(v_j)+O(m^{-2})]`,

where, with `s(v)=v_1^2+v_2^2` and `t(v)=v_3^2`,

`E_J(v)=(57/32)s(v)^2+(15/4)s(v)t(v)+(3/4)t(v)^2`.

Every finite physical matrix has exact nonzero spectrum `{1,1,-1}`.

The immediately preceding account01/B17 report

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260923T200944Z-account01-B17-QFORM-auto11/REPORT.md`

proved the universal pattern inequality

`sum_j E_J(v_j) >= D/r`,

`D=(63+2sqrt(342))/8`,

hence the first relative finite-size coefficient is at least

`c_* = D/20 = (63+2sqrt(342))/160 = 0.6249155251113366...`.

It also established that this lower coefficient is asymptotically sharp over Parseval row patterns.

The newest completed designated-partner theorem is consumed from

`yspennstate/math-open-problems@994cf283d0c9b51cd43328c69d68c8fc17a7d481:proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T195641Z-account02-B17-QFORM-auto11/REPORT.md`.

Its exact scope is used in Section 6 below.

## 2. Exact finite-period optimization inside the sign-segregated sharp class

Fix a period `r`. Put `k` rows wholly in the positive spectral plane and `q=r-k` rows wholly on the negative axis, with `2<=k<=r-1`. Parseval gives

`sum_(positive) s_j=2`, `sum_(negative) t_j=1`.

Since mixed terms vanish in this class, Cauchy gives

`sum_j E_J(v_j) >= (57/32)*(4/k)+(3/4)*(1/q)`

`= F_r(k):=57/(8k)+3/[4(r-k)].`

Equality is attainable for every such `(r,k)`: use an equal-norm Parseval frame of `k` vectors in the positive plane (for `k>=3`, the regular `k`-gon scaled by `sqrt(2/k)`; for `k=2`, use the two coordinate vectors), and use `q` copies of `e_3/sqrt(q)` on the negative axis.

The continuous minimizer of `F_r` is at

`alpha r`,  `alpha=sqrt(38)/(sqrt(38)+2)=(19-sqrt(38))/17=0.7550344704135896...`.

Therefore the exact integer minimizer in this sign-segregated class is one of `floor(alpha r)` and `ceil(alpha r)` (subject only to `2<=k<=r-1`).

There is an exact gap identity. For every admissible integer `k`,

`F_r(k)-D/r = D (k-alpha r)^2/[r k(r-k)]`.

Equivalently, in total physical dimension `n=rm`, the Edgeworth expansion for the equality frame is

`p_{Q_m}(0)=3sqrt(2)[1-c_r(k)/n+O_r(n^{-2})]`,

where

`c_r(k)=rF_r(k)/20`

and

`boxed(c_r(k)-c_* = D (k-alpha r)^2/[20 k(r-k)]).`

Thus ordinary nearest-integer periods approach `c_*` at rate `O(r^{-2})` in the first coefficient. The next section produces an explicit arithmetic subsequence with the much faster rate `O(r^{-4})`.

## 3. Pell-optimal periods: an explicit O(r^-4) saturation sequence

Let `(p_j,r_j)` be defined by

`(p_0,r_0)=(25,4)`,

`p_(j+1)=37p_j+228r_j`,
`r_(j+1)=6p_j+37r_j`.

This is multiplication by the Pell unit `37+6sqrt(38)`. Consequently

`p_j^2-38r_j^2=17`

for every `j`. The congruence `p_j == 2r_j (mod 17)` is also preserved. Define

`k_j=(19r_j-p_j)/17`,  `q_j=r_j-k_j`.

These are integers, and the first values are

`(r,k,q,p)=(4,3,1,25)`,
`(298,225,73,1837)`,
`(22048,16647,5401,135913)`,
`(1631254,1231653,399601,10055725)`.

Since `alpha=(19-sqrt(38))/17`, the Pell equation gives the exact Diophantine error

`k_j-alpha r_j=(r_j sqrt(38)-p_j)/17`

`=-1/(p_j+r_j sqrt(38)).`

Substitution into the finite-period gap identity yields

`boxed(c_(r_j)(k_j)-c_* = D/[20 k_j q_j (p_j+r_j sqrt(38))^2]).`

Because `k_j` and `q_j` are both proportional to `r_j` and `p_j+r_j sqrt(38)` is proportional to `r_j`, this is `O(r_j^{-4})`.

The first coefficient gaps are already

- `r=4`: `8.4474888663383e-5`;
- `r=298`: `2.8186342571703e-12`;
- `r=22048`: `9.4065240194274e-20`;
- `r=1631254`: `3.1392045244435e-27`.

Hence there is an explicit sequence of exact finite Parseval cube-frame periods for which

`p_{Q_m}(0)=3sqrt(2)[1-(c_*+epsilon_j)/n+O_j(n^{-2})]`,

with the displayed exact positive `epsilon_j=O(r_j^{-4})`.

**Scope warning.** The source Edgeworth remainder is for each fixed period `r`; no uniformity in `r` is asserted. This is a two-scale statement: first fix a Pell period and let `m->infinity`, then let the Pell period grow. No simultaneous one-parameter `r,m->infinity` expansion is claimed.

## 4. Exact entrywise-dense rotated versions

The Pell equality frames are sign-segregated and therefore have structural zeros before rotation. Those zeros are not essential.

For rational parameters `x,y` put `d=1+x^2+y^2` and define the rational orthogonal matrix

`O(x,y)=d^{-1} [[1+y^2-x^2,-2xy,2x],[-2xy,1-y^2+x^2,2y],[-2x,-2y,1-x^2-y^2]].`

It satisfies `O(x,y)->I` as `(x,y)->(0,0)`. Its third column is the rational unit vector

`n(x,y)=(2x,2y,1-x^2-y^2)/d`,

and

`G(x,y)=O(x,y) J O(x,y)^T = I-2 n(x,y)n(x,y)^T`.

Fix any Pell equality pattern with nonzero rows `v_i`, and let `V` be the row matrix. The physical base matrix is

`A(x,y)=V G(x,y) V^T`.

For every pair of nonzero rows `u,v`,

`u^T G(x,y)v = u.v - 2(u.n(x,y))(v.n(x,y))`.

This rational/analytic function is not identically zero on the two-parameter sphere chart: if `u.v !=0`, choose `n` orthogonal to `u`; if `u.v=0`, choose a unit `n` with nonzero projections on both `u` and `v`. Thus each zero condition is a proper algebraic set. There are only finitely many row pairs. Rational `(x,y)` are dense, so arbitrarily close to `(0,0)` one can choose rational `(x,y)` outside their finite union. For such a choice **every physical entry of `A(x,y)` is nonzero**.

At the same time, writing the rotated Parseval pattern as `w_i=v_i O(x,y)`, the Edgeworth coefficient `sum_i E_J(w_i)` depends continuously on `(x,y)` and tends to the Pell coefficient as `(x,y)->0`. Repeating the rotated pattern `m` times therefore gives exact entrywise-dense finite physical matrices with nonzero spectrum exactly `{1,1,-1}` and first Edgeworth coefficients arbitrarily close to the Pell-optimal values.

Consequently `c_*` is not merely an infimum of sparse/sign-separated witness geometries. In the two-limit sense above it is also the infimum approached by **exact entrywise-dense rotated periodic product-cube families**.

## 5. Sharp-constant consequence

The strongest source-valid universal lower obstruction remains

`boxed(C_univ >= 3sqrt(2)=4.242640687119...)`.

This report does not raise that obstruction and does not prove `C_univ=3sqrt(2)`. It strengthens the rigidity information around it: even after demanding exact finite spectra and entrywise-dense physical coupling, one can approach `3sqrt(2)` from below with the first `1/n` coefficient arbitrarily close to the universal periodic value `c_*`; moreover an explicit Pell sequence makes the coefficient error decay as `r^{-4}`.

Therefore any proposed sharp upper proof cannot rely on a dimension-free stability gap separating dense finite frames from the diffuse Gaussian obstruction. Conversely, a counterexample above `3sqrt(2)` cannot be produced by the first Edgeworth correction of these fixed-period cube frames, whose first correction is strictly negative.

## 6. Actual application of the completed account02/B17 theorem

Let `X` be arbitrary with density `0<=f<=1`, independent of centered unit intervals `U_1,U_2,U_3,V_1,V_2,V_3,V_4`. Set

`S=(U_1+2U_2+2U_3)/3`,
`T=(V_1+V_2+V_3+V_4)/2`.

The leverage vectors

`a=(1,2,2)/3`,  `b=(1,1,1,1)/2`

are unit vectors. Hence the physical matrix

`A_sep=diag(1,aa^T,-bb^T)`

has exact nonzero spectrum `{1,1,-1}`. Applying the completed partner theorem at its actual hypotheses gives

`boxed(||p_{X^2+S^2-T^2}||_infinity <= K_(4/5))`,

where

`K_(4/5)=2sqrt(2) asin(4/5)+sqrt(5)(pi/2-asin(4/5))`

`=4.061699170101463... < 3sqrt(2)`.

The gap is about `0.180941517017822`. This is a genuine global inequality for an exact target matrix and an arbitrary cap-one singleton law, not a cone-tip estimate.

For every fixed Pell period above, the periodic shared-sign-geometry cube witness tends to `3sqrt(2)` as its repetition count grows, and therefore eventually exceeds this entire separated-architecture global ceiling. Thus the partner result and the Pell witness together certify a structural constraint: a sharp proof cannot uniformly compress all near-extremizers into one arbitrary heavy coordinate plus two disjoint opposite rank-one centered-cube banks. Shared diffuse sign geometry carries concentration that this separated architecture provably cannot reach.

## 7. Verification and remaining witness frontier

The deterministic symbolic checker verifies the coefficient identities, the Pell norm and congruence recurrences, the exact `k_j`, the exact error identity, and the partner constant comparison. It returns

`QFORM_B17_PELL_PERIODIC_CHECK_PASS`.

The remaining witness frontier is outside this fixed-period Edgeworth neighborhood: nonperiodic/mesoscopic changing frames, arbitrary rough cap-one laws on the diffuse coordinates, several shared intermediate-leverage rows, off-zero modes, or additional active spectrum. Full QFORM and unrestricted continuity remain OPEN.
