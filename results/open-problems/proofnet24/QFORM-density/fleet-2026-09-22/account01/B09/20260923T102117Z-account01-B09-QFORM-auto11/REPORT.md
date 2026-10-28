SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T10:21:17Z.
attacking: quotient-frame degeneration by puncturing literal physical rows and using the raw half-leverage Brascamp--Lieb gate before any Pluecker entropy loss; then localizing failure of that gate to a bounded physical collar in the partner's exact low-disjoint-rank leaf reduction.

# account01/B09 — half-leverage puncture routing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains open. This report proves a stronger puncture certificate than the preceding `theta+dq<1` Pluecker-union-bound gate. The new condition is dimension-free in the coefficient-frame rank:

`q <= (1-theta)/2`.

It is obtained by preserving the exact Brascamp--Lieb half-leverage hypothesis under conditioning. The result gives a continuous density and a direct `O(interval length)` bound. It uses only literal original-coordinate conditioning; no rotated random coordinates are introduced.

## 1. Source-pinned inputs


### 1.1 Raw mixed-hub theorem

I use the completed interactive theorem `Theorem H` from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For literal physical hubs `H`, a surviving leaf bank `I`, and

`A_II = D + sum_(a=1)^r lambda_a v_a v_a^T`,

with `D` diagonal, form the augmented physical coefficient rows

`w_i=((v_a)_i,a<=r ; A_{ih},h in H)`

and Gram matrix `G_I=sum_i w_i w_i^T`. If all normalized row leverages satisfy

`w_i^T G_I^{-1} w_i <= 1/2`,

then, with `h=|H|`,

`|phi_Q(t)| <= (2|t|)^(-h) prod_a(4pi|t lambda_a|)^(-1/2)
                (4pi)^(r+h) det(G_I)^(-1/2)`.

The blocks on the hubs, conditioned coordinates and outside coordinates are arbitrary. When `r+2h>2`, this envelope is integrable.

### 1.2 Designated partner

The newest completed designated-partner report actually used below is account02/B09

`QFORM-ONEHUB-PLUCKER-SMOOTHING-v1`,

read at

`yspennstate/math-open-problems@0029401037d9e0bb0f18c030c959bbc5afd57d52`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T074200Z-account02-B09-QFORM-r13/REPORT.md`.

For one literal hub and

`A_II=D+sum_(a=1)^r lambda_a v_av_a^T`, `r>=1`,

put `W=[v_1,...,v_r,c]`, `G=W^TW`, where `c` is the hub-to-leaf coupling. If `rho` is the probability that two iid Pluecker bases of the whitened frame are disjoint and `rho>0`, then

`||p_Q||_infinity
 <= ((r+2)/r) exp((r+1)/(r+2))
    [rho det(G) prod_a |lambda_a|]^(-1/(r+2)).`                 (1.1)

The density is continuous and the identical coefficient multiplies interval length. The same partner report also proves the exact arbitrary-leaf-curvature reduction: if the leaf disjoint five-volume vanishes, conditioning at most eight literal leaf coordinates leaves `diagonal + symmetric rank <=4`.

## 2. Exact puncture identities

Let a full-rank deterministic coefficient frame on a literal leaf bank `L` be

`W=(w_i)_(i in L)`, `G=W^T W>0`, `d=rank W`.

For each physical row define its original normalized leverage

`p_i = w_i^T G^{-1}w_i`.

Condition a literal physical set `K subset L`, and write `I=L\K`. Put

`theta = sum_(i in K) p_i`,
`q = max_(i in I) p_i`.

Let `u_i=G^(-1/2)w_i` and

`R_K=sum_(i in K) u_i u_i^T`.

Then

`tr R_K=theta`,                                                   (2.1)

and the surviving Gram matrix is exactly

`G_I = W_I^T W_I
     = G^(1/2)(I-R_K)G^(1/2)`.                                  (2.2)

Assume `theta<1`. Since `R_K>=0` and `||R_K||op<=tr R_K=theta`,

`I-R_K >= (1-theta)I`.                                          (2.3)

Consequently

`det G_I = det G det(I-R_K) >= (1-theta) det G`.                (2.4)

For completeness, if `r_1,...,r_d` are the eigenvalues of `R_K`, then

`prod_j(1-r_j) >= 1-sum_j r_j=1-theta`;                         (2.5)

this proves (2.4) without replacing `(1-theta)` by `(1-theta)^d`.

The normalized leverage of a surviving row with respect to the **surviving** frame is

`ell_i = w_i^T G_I^{-1}w_i
       = u_i^T(I-R_K)^(-1)u_i
       <= p_i/(1-theta).`                                       (2.6)

This is the essential implication.

## 3. `QFORM-HALFLEVERAGE-PUNCTURE-v1`

Split the independent original coordinates into literal physical hubs `H`, leaves `L`, and an arbitrary outside bank. Let `h=|H|`. Choose a literal leaf set `K` to condition and put `I=L\K`. Suppose, after this conditioning, the surviving principal leaf block is exactly

`A_II=D+sum_(a=1)^r lambda_a v_av_a^T`,                          (3.1)

where `D` is diagonal and every displayed `lambda_a` is nonzero. Extend the `v_a` by zero on `K`, and form on all of `L` the augmented coefficient frame

`W=[v_1,...,v_r,C]`,                                             (3.2)

where the columns of `C` are the actual physical hub-to-leaf couplings. Let `G=W^TW>0`, and let `p_i,theta,q` be as in Section 2. Assume

`theta<1`,
`q <= (1-theta)/2`,                                              (3.3)

and

`r+2h>2`.                                                        (3.4)

### Theorem

The full quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= C_H(h,r)
    [(1-theta) det(G) prod_(a=1)^r |lambda_a|]^(-1/(r+2h)),`     (3.5)

where

`C_H(h,r)
 = 4 (r+2h)/(r+2h-2) 2^(-2h/(r+2h)).`                           (3.6)

Therefore every interval `B` satisfies

`boxed:
 P{Q in B}
 <= C_H(h,r)
    [(1-theta) det(G) prod_a |lambda_a|]^(-1/(r+2h)) |B|.`      (3.7)

All hub self-curvature, hub/outside couplings, curvature touching the conditioned coordinates, the outside quadratic block, signs and conditioning-generated affine terms are arbitrary.

### Proof

By (2.6) and (3.3), every surviving augmented row satisfies

`ell_i<=1/2`.                                                    (3.8)

Thus the completed raw Theorem H applies to the original-coordinate survivor. Put

`alpha=h+r/2=(r+2h)/2>1`,
`R=det(G_I) prod_a |lambda_a|`.

Theorem H gives

`|phi_Q(t)|
 <= min{1,
         2^(-h)(4pi)^alpha R^(-1/2)|t|^(-alpha)}.`              (3.9)

For `K0>0`,

`int_R min(1,K0|t|^(-alpha))dt
 =2 alpha/(alpha-1) K0^(1/alpha).`                              (3.10)

Fourier inversion and (3.9) therefore give

`||p_Q||infinity
 <= 4 alpha/(alpha-1) 2^(-h/alpha)
    R^(-1/(2alpha))
 = C_H(h,r) R^(-1/(r+2h)).`                                    (3.11)

Finally (2.4) gives

`R >= (1-theta)det(G)prod_a|lambda_a|`,                         (3.12)

which proves (3.5). The uniform `L^1` characteristic-function envelope gives continuity. The interval bound follows by integrating the density. QED.

## 4. Why this strictly strengthens the preceding B09 puncture gate

The preceding Pluecker-union-bound puncture argument required

`theta+dq<1`,                                                    (4.1)

with `d=r+h`, because it lower-bounded disjoint-basis probability by a collision union bound.

The new theorem only requires

`theta+2q<=1`,                                                   (4.2)

regardless of `d`.

For every `d>2`, (4.2) is strictly weaker than (4.1). The improvement comes from stopping before the determinant-weighted Pluecker entropy step and using the original half-leverage Brascamp--Lieb gate directly.

A briefly tested alternative was to use a two-way MSS paving to manufacture explicit disjoint Pluecker mass. That route only gives a leverage threshold below `(1-1/sqrt(2))^2`, so it is strictly dominated here by the exact half-leverage theorem and is not used positively.

## 5. Target-valid stress test where the old gate fails and the new gate pays

Take `r=31`, `h=2`. Split a physical leaf bank into `33` mutually disjoint groups of size `32`. Let

`v_1,...,v_31,c_1,c_2`

be the unit-flat vectors on those groups. They are mutually orthonormal. Define

`Q = sum_(a=1)^31 <v_a,Y>^2
     +2X_1<c_1,Y>+2X_2<c_2,Y>.`                                 (5.1)

The matrix spectrum on the active compression is

`1` with multiplicity `31`, together with two copies of `{1,-1}`. Thus it has `35` eigenvalues of absolute value one and is a literal full-target example.

Here

`G=I_33`, `theta=0`, `q=1/32`, `d=33`.                          (5.2)

The previous gate fails:

`theta+dq=33/32>1`.                                             (5.3)

The new gate is strongly satisfied: `q<1/2`. Formula (3.5) gives

`||p_Q||infinity
 <= 4*(35/33)*2^(-4/35)
 =3.9193194949... <3.920.`                                      (5.4)

Hence, for every admissible independent cap-one product law,

`boxed: P{Q in B}<3.920 |B|.`                                  (5.5)

The density is continuous. No coefficient in a rotated random basis is used.

## 6. Latest designated partner applied to an actual high-leverage inequality

The new half-leverage theorem intentionally does not cover every frame. The newest account02/B09 Pluecker theorem supplies a complementary route beyond the raw leverage gate.

Use one physical hub `X_h` and three mutually disjoint leaf banks. On the first bank take a unit vector `v_1` whose squared coordinates are

`0.7, 0.01, ..., 0.01`                                          (6.1)

with thirty copies of `0.01`. On the second and third banks take unit-flat vectors `v_2` and `c`, each on `100` coordinates. Thus `v_1,v_2,c` are orthonormal. Set

`Q_* = <v_1,Y>^2 + <v_2,Y>^2 + 2X_h<c,Y>.`                      (6.2)

The active spectrum is exactly

`{1,1,1,-1}`,                                                   (6.3)

so `Q_*` satisfies the full three-large-eigenvalue target. The augmented frame has `G=I_3`, but its largest leverage is `0.7>1/2`; raw Theorem H does not apply.

Because the three column supports are disjoint, a Pluecker basis chooses one physical coordinate from each support. For two iid bases, disjointness occurs independently across the three supports. Hence

`rho
 =(1-(0.7^2+30*0.01^2))
  (1-100*0.01^2)^2
 =0.507*(0.99)^2
 =0.4969107.`                                                    (6.4)

Apply account02/B09 `QFORM-ONEHUB-PLUCKER-SMOOTHING-v1` with `r=2`, `lambda_1=lambda_2=1`, `det G=1`. It gives

`boxed:
 ||p_(Q_*)||infinity
 <= 2 e^(3/4) rho^(-1/4)
 =5.0429106098... <5.043,`                                      (6.5)

and therefore

`boxed: P{Q_* in B}<5.043 |B|.`                                (6.6)

This is an actual designated-partner application on a target-valid frame lying outside the new half-leverage branch.

## 7. Consequence for the partner's exact arbitrary-leaf reduction

The newest account02/B09 report proves that if the leaf disjoint five-volume is exactly zero, then after conditioning a pivot set `K` of at most eight literal leaf coordinates, the surviving leaf matrix is

`D+C`, `rank C=r<=4`.                                           (7.1)

In the one-hub case diagonalize the deterministic low-rank matrix only at the coefficient level,

`C=sum_(a=1)^r lambda_a v_av_a^T`,                              (7.2)

without rotating the random variables, and augment with the physical star `c`. Then `d=r+1<=5`.

For every `r>=1`, the zero-disjoint-five-volume branch now has the following source-valid dichotomy.

**Paid half-leverage branch.** If

`theta<1` and `q<=(1-theta)/2`,                                 (7.3)

the full quadratic form is paid by (3.5), retaining the arbitrary physical hub core and every conditioned coupling.

**Localized collar branch.** If (7.3) fails, then either

`theta>=1/2`,                                                    (7.4)

so the at-most-eight pivot rows already carry at least half a unit of augmented-frame leverage, or `theta<1/2` and there is a surviving row with

`p_i>(1-theta)/2>1/4`.                                         (7.5)

Since `sum_i p_i=d<=5`, fewer than `4d<=20` physical rows can have leverage above `1/4`. Thus every failure of the new analytic gate is witnessed by the at-most-eight pivot rows together with fewer than twenty high-leverage physical rows: a collar of at most `27` leaf coordinates (plus the literal hub).

This does **not** yet prove the full target: conditioning that collar can destroy the very determinant resource one is trying to keep. It does, however, replace a diffuse high-dimensional degeneration by a bounded physical localization problem in the exact zero-disjoint-five-volume one-hub branch.

## 8. First unpaid B09 implication

`QFORM-LOCALIZED-COLLAR-ELEVATION-v1`:

In the exact zero-disjoint-five-volume one-hub survivor above, use the at-most-27-coordinate localized collar without conditioning away the third spectral resource. Either extract an already-paid physical pair / definite pair / rank-two cross / grouped square from the collar, or prove that the complement retains a quantitative quotient-frame determinant to which (3.5) applies. The near-coloop stress families remain mandatory regression tests; a small leftover quadratic term may not be deleted on arbitrary unbounded product laws.

## 9. Corrections respected

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, fixed-good-minor implication, positive moment of worst conditional projection caps, small-random-error deletion, or probability squaring is used. The only spectral rotations above diagonalize deterministic coefficient matrices inside exact identities; all random conditioning and factorization remain in the original independent coordinates.

Full QFORM remains open. Full-target continuity remains open. Continuity is proved on the new theorem branch and on the designated-partner example.
