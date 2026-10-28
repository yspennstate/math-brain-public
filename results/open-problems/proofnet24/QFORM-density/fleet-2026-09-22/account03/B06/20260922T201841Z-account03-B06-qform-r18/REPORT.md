SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B06, 2026-09-22T20:18:41Z.
attacking: aggregate the post-pivot curved cross bank before reciprocal minor selection, using one physical row plus the second exterior energy of all remaining rows.

# account03/B06 QFORM r18 — one-row / aggregate-E2 hybrid smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T201841Z-account03-B06-qform-r18`  
**Assignment:** Curved fiber integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** not proved by the new theorem. The conclusions below are `L^3` regularity of a residual law and essential `L^infinity` boundedness after a genuine physical square.

## 1. Exact scope and source-valid inputs

The target remains the full arbitrary-dimensional theorem for independent original coordinates with one-dimensional probability densities at most one and a real symmetric matrix having at least three eigenvalues of modulus at least one. No moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence hypothesis is added.

This run explicitly avoids the live refuted interfaces: law-uniform pointwise quadratic-phase decay; arbitrary-joint rank-three coarea; positive moments of worst conditional projection densities; unrestricted spectral-fiber suprema; generic X-ray control of an indefinite trace; a universally good single physical minor; and direct reciprocal averaging of Pluecker/minor certificates.

The mechanism is new relative to B06 r17. Instead of selecting one physical pair and paying a negative power of its determinant, it keeps **all** two-row exterior curvature of a deleted-row cross bank through its second elementary singular-value energy before any reciprocal power is taken.

Source-valid completed inputs actually used:

1. **Regularized determinant / graph Brascamp--Lieb estimate**, interactive canonical report `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`. In the unconditional `q=2` form it bounds the decoupled product attached to any original-coordinate cross block, with arbitrary same-side phases and outside couplings.

2. **Weighted affine-fiber projection theorem**, account02/B06 canonical report `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. Its `k=1` case says that a unit linear projection of independent cap-one coordinates has density at most `sqrt(e)`; this remains true for independent difference coordinates, whose densities are also at most one.

3. **Compatible account04 result actually applied:** account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical report `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`. I apply its exact one-sided Abel/square-kernel domination to the `L^3` residual density below. The designated `account04/B06` current-QFORM artifact was still absent at the source check; no result or PASS is fabricated for it.

4. **Near-coloop state applied below:** account03/B08 r19, canonical mathematics `yspennstate/math-open-problems@86cbf124545c3457b0037b49151f4f641391fc76:proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T194215Z-account03-B08-qform-diffuse-r19/REPORT.md`. In its surviving nonzero-pivot branch, at `g=gamma/16`, the normalized cross matrix `Z=H(g^2 I+H^T H)^(-1/2)` has `theta=||Z||_F^2>=256/129`; if the already-paid ridge branches fail, a physical row `j` has squared normalized leverage `q_j=||z_j||^2>99/100`, while `theta<201/100`.

## 2. The aggregate curvature quantity

Let `I,J` be disjoint sets of ORIGINAL coordinates and condition on all coordinates outside `I union J`. The remaining quadratic form has the form

`R=F(U)+2 U^T H V+G(V)+c`,                                      (2.1)

where `U=X_I`, `V=X_J` are independent product vectors with coordinate density caps one, while `F,G` may contain arbitrary quadratic and affine terms induced by the conditioning.

Fix a physical row `j in I`, write

`h=h_j in R^J`, `r=||h||_2>0`,                                  (2.2)

and let `H_0` be the matrix obtained from `H` by deleting row `j`. Define

`E_2(H_0)=sum_(p<q) s_p(H_0)^2 s_q(H_0)^2`.                      (2.3)

By Cauchy--Binet this is exactly

`E_2(H_0)=sum_{k<l, u<v} det H_0[{k,l},{u,v}]^2`,                (2.4)

the sum of the squares of **all physical 2 x 2 cross minors** of the deleted-row bank. Thus (2.3) is an aggregate-before-inversion currency; it never selects the largest pair.

## 3. Main theorem: one physical row plus aggregate exterior curvature gives L3

### Theorem 3.1 — `QFORM-ONE-ROW-E2-HYBRID-L3-v1`

In (2.1), suppose `E:=E_2(H_0)>0`. Let `phi(t)=E exp(itR)`. Then for every `t!=0`,

`|phi(t)| <= min{ 1,
 (pi sqrt(e)/(r|t|))^(1/4)
 [1+16 E t^4/(pi^4 e^4)]^(-1/8) }`.                            (3.1)

Consequently

`J:=int_R |phi(t)|^(3/2) dt`

satisfies the explicit aggregate bound

`boxed(
 J <= pi e E^(-1/4)
      +2^(27/8) pi e^(13/16) r^(-3/8) E^(-5/32).
)`                                                               (3.2)

Hence `R` has an `L^3` density and

`boxed(
 ||p_R||_3 <= (2pi)^(-2/3) J^(2/3).
)`                                                               (3.3)

No leverage hypothesis is imposed on `H_0`, and arbitrarily many extra singular directions are retained.

### Proof

The regularized-determinant source begins from the exact original-coordinate one-sided decoupling inequality. If `V'` is an independent copy of `V` and `D=V-V'`, then

`|phi(t)|^2
 <= E_D product_(i in I) |hat f_i(2t (H D)_i)|`.             (3.4)

The self phases `F,G` and outside-conditioned affine terms have already been handled in that source; (3.4) does not declare any rotated coordinates independent.

Put

`A(t)=E_D |hat f_j(2t h dot D)|^2`,
`B(t)=E_D product_(i!=j)|hat f_i(2t h_i dot D)|^2`.              (3.5)

Cauchy--Schwarz in the genuine product difference variable gives

`|phi(t)|^2 <= A(t)^(1/2) B(t)^(1/2)`.                           (3.6)

Each coordinate of `D` has density `f*tilde f` of mass one and sup norm at most one. Normalize `h=r u`, `||u||=1`. The account02/B06 weighted affine-fiber theorem with `k=1` therefore gives the scalar projection `u dot D` a density at most `sqrt(e)`, and `h dot D` a density at most `sqrt(e)/r`. Plancherel for the original physical density `f_j`, with `int f_j^2<=1`, yields

`A(t)
 <= (sqrt(e)/r) int_R |hat f_j(2ts)|^2 ds
 <= pi sqrt(e)/(r|t|)`.                                         (3.7)

For `B(t)` use the unconditional `q=2` regularized graph determinant on the entire deleted-row bank `H_0`. With the same Fourier convention,

`B(t)
 <= det(I+4t^2 H_0^T H_0/(pi^2 e^2))^(-1/2)`.                  (3.8)

Taking the required roots in (3.6) gives

`|phi(t)|
 <=(pi sqrt(e)/(r|t|))^(1/4)
   det(I+4t^2 H_0^T H_0/(pi^2e^2))^(-1/8)`.                    (3.9)

If `lambda_p=s_p(H_0)^2`, the determinant expansion has nonnegative coefficients, so

`det(I+c t^2 H_0^T H_0)
 >=1+c^2 t^4 sum_(p<q)lambda_p lambda_q
 =1+c^2 E t^4`,                                                 (3.10)

where `c=4/(pi^2e^2)`. This proves (3.1).

Set

`b=c^2E=16E/(pi^4e^4)`, `T=b^(-1/4)`.                           (3.11)

On `|t|<=T`, use `|phi|<=1`; the contribution to `J` is at most

`2T=pi e E^(-1/4)`.                                             (3.12)

For `|t|>=T`, use `(1+bt^4)^(-3/16)<=b^(-3/16)|t|^(-3/4)` in the `3/2` power of (3.1). Therefore

`|phi(t)|^(3/2)
 <=(pi sqrt(e)/r)^(3/8)b^(-3/16)|t|^(-9/8)`.                    (3.13)

Since `2 int_T^infinity t^(-9/8)dt=16 T^(-1/8)`, the tail is at most

`16 (pi sqrt(e)/r)^(3/8)b^(-5/32)
 =2^(27/8) pi e^(13/16) r^(-3/8)E^(-5/32)`.                    (3.14)

Equations (3.12)--(3.14) give (3.2). Since `phi in L^(3/2)`, inverse Hausdorff--Young constructs an `L^3` density and gives (3.3). QED.

### Why this is genuinely aggregate

The first term in (3.2) depends on `E_2(H_0)^(-1/4)` and the second on `E_2(H_0)^(-5/32)`. Neither term contains the number of rows or columns, nor a maximum/minimum over physical pairs. By (2.4), all 2 x 2 physical cross curvature is summed **before** these negative powers appear. This is precisely the operation that the live single-minor and Pluecker-support corrections demand.

## 4. Spending the L3 bank through a genuine original-coordinate square

Suppose now that the residual (2.1) arose by completing a nonzero ORIGINAL-coordinate scalar pivot,

`Q=R+a V_R^2`, `a!=0`,                                         (4.1)

where, conditional on `R`, `V_R` is a mixture of translations of one untouched original coordinate density and therefore has conditional density at most one.

The completed account04/B18 proof gives the exact dependence-safe kernel inequality

`p_Q(t)
 <= |a|^(-1/2) int_0^infinity
      p_R(t-sgn(a)u) u^(-1/2)du`.                              (4.2)

This is the partner result used at an actual inequality. If `||p_R||_3<=M`, split the integral at `U`. Holder on `[0,U]` and mass one on `[U,infinity)` give

`int_0^infinity p_R(t-u)u^(-1/2)du
 <=2^(4/3) M U^(1/6)+U^(-1/2)`.                                (4.3)

Optimizing, rather than merely equating the two terms, gives

`U=[3/(2^(4/3)M)]^(3/2)` and

`sup_t int_0^infinity p_R(t-u)u^(-1/2)du
 <= C_A M^(3/4),
 C_A=8/3^(3/4)<3.510`.                                         (4.4)

Combining (3.3) and (4.4) yields

`boxed(
 ||p_Q||_infinity
 <= C_A / sqrt(2pi |a|) * sqrt(J),
)`                                                               (4.5)

with `J` bounded by the aggregate expression (3.2). The same proof applies for `a<0` after reflection.

## 5. Application to the live B08 near-coloop branch

Take the B08 r19 surviving branch. At

`g=gamma/16`,
`Z=H(g^2I+H^T H)^(-1/2)`,                                     (5.1)

there is a physical row `j` with

`q_j:=||z_j||^2>99/100`,                                       (5.2)

and

`256/129 <= theta:=||Z||_F^2 <201/100`.                         (5.3)

Let `Z_0` and `H_0` be obtained by deleting row `j`, and define the dimensionless aggregate residual curvature

`eta:=E_2(Z_0)=sum_(p<q)s_p(Z_0)^2 s_q(Z_0)^2`.                 (5.4)

Because `Z_0=H_0(g^2I+H^TH)^(-1/2)`, equivalently

`H_0=Z_0(g^2I+H^TH)^(1/2)`,                                    (5.5)

and the second factor has smallest singular value at least `g`. Hence

`s_k(H_0)>=g s_k(Z_0)` for every `k`,
`E_2(H_0)>=g^4 eta`.                                            (5.6)

Also (5.2) and `||(g^2I+H^TH)^(-1/2)||<=1/g` imply

`r=||h_j||>=g sqrt(q_j)`.                                       (5.7)

Substitute (5.6)--(5.7) into (3.2):

`J <= (pi/g) [
 e eta^(-1/4)
 +2^(27/8)e^(13/16)q_j^(-3/16)eta^(-5/32)
 ].`                                                            (5.8)

### Corollary 5.1 — `QFORM-NEAR-COLOOP-AGGREGATE-E2-CLOSURE-v1`

If, in the B08 surviving branch,

`eta=E_2(Z_0)>=1/64`,                                           (5.9)

then the full post-pivot quadratic form obeys

`boxed(
 ||p_Q||_infinity <72 / sqrt(|a| gamma).
)`                                                               (5.10)

Indeed the bracket in (5.8), using `q_j>0.99`, is less than

`52.551`,                                                        (5.11)

and `g=gamma/16` in (4.5) gives the numerical prefactor

`2 sqrt(2) C_A sqrt(52.551)<72`.                                (5.12)

Thus a universal amount of **aggregate deleted-row second exterior curvature** closes this near-coloop branch without selecting any one physical pair and without a range-leverage assumption on `H_0`.

The scale product `|a| gamma` is still visible; this result does not claim that the bare three-eigenvalue hypothesis has already paid that separate structural scale.

## 6. Failure of the new payment forces a quantitative rank-two tube

The complementary case is much more structured. Assume

`eta<1/64`.                                                      (6.1)

Let the eigenvalues of `Z_0 Z_0^T` be

`lambda_1>=lambda_2>=...>=0`,
`s=sum_p lambda_p=||Z_0||_F^2`.                                (6.2)

From (5.2)--(5.3) and the fact that every diagonal of `ZZ^T` is at most one,

`127/129 <= s <1.02`.                                           (6.3)

Moreover

`eta=sum_(p<q)lambda_p lambda_q
    =(s^2-sum_p lambda_p^2)/2`.                                 (6.4)

If `lambda_1<s/2`, then `sum lambda_p^2<=lambda_1 s<s^2/2`, so

`eta>s^2/4 >= (127/129)^2/4 >1/64`,                             (6.5)

contrary to (6.1). Hence `lambda_1>=s/2`. If

`delta=s-lambda_1=sum_(p>=2)lambda_p`,                           (6.6)

then the terms involving `lambda_1` in (6.4) give

`eta>=lambda_1 delta >=(s/2)delta`.                              (6.7)

Therefore

`boxed(
 delta < 2/(64s) <=129/4064 <0.031743.
)`                                                               (6.8)

By Eckart--Young, `delta` is exactly the squared Frobenius error of the best rank-one approximation to `Z_0`. Keep the physical row `z_j` unchanged and replace only `Z_0` by that best rank-one approximation. The resulting matrix has rank at most two, and

`boxed(
 inf_{rank(W)<=2, W_{j,*}=Z_{j,*}} ||Z-W||_F^2
 <129/4064.
)`                                                               (6.9)

So the branch not closed by (5.10) is not an arbitrary high-rank cross geometry: it lies in an explicit normalized Frobenius tube of squared radius `<0.031743` around a rank-two matrix while preserving the near-coloop row exactly.

The live B08 r19 theorem supplies, in addition, a right near-coloop column and a normalized intersection-minor reserve `>2349/5000`; this report does not spend that extra currency. It is available for the next stability step.

## 7. What is now paid and what remains

**Proved here:**

- `QFORM-ONE-ROW-E2-HYBRID-L3-v1`: a dimension-free `L^3` bound obtained from one physical row plus the sum of **all** deleted-row `2 x 2` cross-minor squares.
- `QFORM-OUTER-SQUARE-ONE-ROW-E2-v1`: the preceding aggregate bank becomes an essential `L^infinity` bound after a genuine original-coordinate square, using the completed account04/B18 dependence-safe kernel.
- `QFORM-NEAR-COLOOP-AGGREGATE-E2-CLOSURE-v1`: in the live B08 normalized branch, `E_2(Z_0)>=1/64` gives `<72/sqrt(|a|gamma)`.
- If that aggregate payment fails, the normalized cross bank lies within squared Frobenius distance `<129/4064` of rank two while keeping the heavy physical row exact.

**Not proved:** the full QFORM conjecture. In particular, this report does not prove a universal lower bound on `|a|gamma`, does not prove that a small normalized Frobenius perturbation of the exact-rank-two r17 mechanism is harmless for arbitrary fragmented product laws, and does not establish continuity from the final Abel step.

### Next exact obligation

`QFORM-NEAR-RANK2-STABILITY-OR-SECOND-CURVATURE-v1`: in the surviving B08 two-sided near-coloop branch, combine the right near-coloop column and intersection-minor reserve with the rank-two tube (6.9) to obtain either

1. a dependence-safe stability theorem for the exact-rank-two cross-bank `L^3` mechanism under the quantified normalized perturbation, or
2. a second aggregate curvature payment that forces `eta>=1/64`, or
3. an already-paid physical-pair / ridge / grouped-bank branch.

Any such argument must keep arbitrary self blocks and original-coordinate product provenance; simply discarding the `<0.032` normalized remainder is not authorized.

## 8. Computation status

A deterministic checker accompanying this report verifies the Cauchy--Binet identity for `E_2`, the singular-value transfer `E_2(H_0)>=g^4 E_2(Z_0)` on random matrices, and all displayed numerical constants. The computation is a sanity check only; the inequalities above are proved symbolically.
