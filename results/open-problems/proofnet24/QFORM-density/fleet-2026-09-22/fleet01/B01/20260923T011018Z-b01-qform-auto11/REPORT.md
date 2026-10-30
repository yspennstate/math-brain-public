# QFORM fleet01/B01 — pair-wedge averaged Fourier gate and scalar-square lift

Status: **ESSENTIAL_STEP_APPLIED / SUPPORTING ANALYTIC THEOREM / FULL TARGET OPEN**.

Programme: `QFORM-DENSITY-3EIG-20260922`. Fresh owner control at the start of this run was revision `2026-09-22.15`; QFORM remained the sole research target and no fleet01/B01 stop was observed. The full conjecture and the full continuity conclusion remain open.

The required correction remains in force: for arbitrary densities bounded by one there is no law-uniform pointwise decay `|E exp(i t X^2)| <= C |t|^{-gamma}` with any `gamma>0`. The theorem below does not use such a bound. It obtains an `L^{3/2}` frequency budget from a two-dimensional **random linear slope** while retaining arbitrary quadratic phase in the selected physical pair.

## Source premises

1. Livshyts--Paouris--Pivovarov: every two-dimensional orthogonal marginal of a product probability density whose one-dimensional factors are bounded by one has density at most `2`. Equivalently, if `G` is a rank-two real matrix with row Gram determinant `D>0`, then the density of `G X` is at most `2/sqrt(D)`.

   This is the same source-valid projection theorem used in fleet01/B01 run `20260922T143759Z-b01-qform-auto11b`, canonical report `yspennstate/math-open-problems@a441556830cbcb4e9a2aad95835dc86d7ffcac99:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260922T143759Z-b01-qform-auto11b/REPORT_FINAL.md`.

2. Completed designated partner fleet02/B01 r31, canonical source `yspennstate/math-open-problems@3280d9fab56fe4878189ae89176887e3da29f569:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T233020Z-fleet02-B01-qform-r31/REPORT.md`. For a physical cross block `M`, with

   `Z=e_3(M^T M)`

   and natural squared-3-volume row law, if row `h` has marginal `alpha`, and `N` denotes `M` with row `h` deleted, then

   `e_2(N^T N) >= alpha Z / ||r_h||_2^2`.                                  (P)

I apply (P) quantitatively in Section 5.

## 1. Arbitrary-self-phase pair-wedge theorem

Let `Y=(Y_1,...,Y_m)` have independent densities bounded by one and let

`R(Y)=Y^T S Y`

for an arbitrary real symmetric `S`. Choose two distinct original coordinates `i,k` and a disjoint original-coordinate bank `J`. Put

`u=S[i,J]`, `v=S[k,J]`,

`D = ||u||_2^2 ||v||_2^2 - <u,v>^2 = ||u wedge v||_2^2`.                  (1.1)

Assume `D>0`. Then, with `phi_R(t)=E exp(i t R)`,

`|phi_R(t)| <= min(1, pi sqrt(2) D^(-1/4) |t|^(-1))`.                     (1.2)

Consequently

`int_R |phi_R(t)|^(3/2) dt <= 6 pi sqrt(2) D^(-1/4)`,                    (1.3)

and the law of `R` has an `L^3` density satisfying

`||p_R||_3 <= 3^(2/3) 2^(1/3) D^(-1/6)`                                 (1.4)

(the numerical constant is `2.6207413942...`).

There is **no restriction** on `S_ii,S_kk,S_ik`, on the quadratic block `S[J,J]`, on coefficients outside the selected coordinates, or on their couplings. Thus (1.2) is not the fleet02/B01 exact-zero two-slope theorem: the selected pair may have arbitrary self curvature and an arbitrary mutual edge.

### Proof

Condition on all original coordinates outside `{i,k} union J`. All terms depending only on the conditioned variables have modulus-one phase and may be suppressed. Terms coupling the conditioned variables to `Y_i,Y_k` become arbitrary affine phases in those two variables; terms coupling them to the bank `J` become an arbitrary affine phase in the bank.

Let

`Z=(u.X_J, v.X_J) in R^2`.

By the two-dimensional product-marginal theorem, `Z` has a density `p_Z` with

`||p_Z||_infinity <= 2/sqrt(D)`.                                         (1.5)

Push the complex measure

`exp(i t [X_J^T S[J,J] X_J + affine(X_J)]) prod_{j in J} f_j(X_j) dX_J`

through the map `X_J -> Z`, and call its complex density `g_t(z)`. Pointwise domination of pushforward variation gives

`|g_t(z)| <= p_Z(z)`, `||g_t||_1 <= 1`,

hence

`||g_t||_2 <= ||p_Z||_infinity^(1/2) <= sqrt(2) D^(-1/4)`.               (1.6)

After the bank integration, the remaining conditional characteristic function is

`int f_i(x) f_k(y) exp(i t q(x,y)) \hat g_t(2 t x,2 t y) dx dy`,          (1.7)

where `q` is an arbitrary real quadratic-affine polynomial and

`\hat g_t(xi)=int exp(i xi.z) g_t(z) dz`.

Cauchy--Schwarz in `(x,y)` uses `||f_i f_k||_2<=1`. With the Fourier convention above, two-dimensional Plancherel gives

`int |\hat g_t(2tx,2ty)|^2 dxdy`
` = pi^2 |t|^(-2) ||g_t||_2^2`.                                         (1.8)

Therefore the conditional characteristic function is bounded by

`pi |t|^(-1) ||g_t||_2 <= pi sqrt(2) D^(-1/4)|t|^(-1)`.                 (1.9)

The bound is uniform in the conditioned variables, so averaging proves (1.2).

Let `A=pi sqrt(2)D^(-1/4)`. Since `|phi_R|<=min(1,A/|t|)`,

`int |phi_R|^(3/2) <= 2[A + A^(3/2) int_A^infinity t^(-3/2)dt] = 6A`,

which is (1.3).

For `\hat f(t)=int exp(i t x)f(x)dx`, Hausdorff--Young gives

`||p_R||_3 <= (2pi)^(-2/3)||phi_R||_(3/2)`.

Using (1.3),

`||p_R||_3 <= (2pi)^(-2/3)(6pi sqrt(2)D^(-1/4))^(2/3)`
`            =3^(2/3)2^(1/3)D^(-1/6)`,

proving (1.4). In particular the law of `R` is absolutely continuous. This theorem does not assert continuity of `p_R`.

## 2. Scalar-square lift

Now let `X=(X_0,X_K)` have independent densities bounded by one and let `A` be arbitrary symmetric with one nonzero **physical** pivot

`a=A_00 !=0`.

Completing the square only in the original coordinate `X_0` gives

`Q=X^TAX = a (X_0 + a^(-1)A[0,K]X_K)^2 + R(X_K)`,                       (2.1)

where

`R(X_K)=X_K^T S X_K`,
`S=A[K,K]-a^(-1)A[K,0]A[0,K]`.                                        (2.2)

Suppose the Schur residual `S` has a pair and bank as in Section 1, with aggregate wedge `D>0`. Then `Q` has a density and

**`||p_Q||_infinity <= C_* |a|^(-1/2) D^(-1/8)`,**                     (2.3)

where

`C_* = 2^(15/4) 3^(-1/4) = 10.223089667940359...`.                     (2.4)

No sign assumption is made. All other Schur coefficients and couplings remain arbitrary.

### Proof

Conditional on `X_K=y`, the law of the first term in (2.1) has density bounded by

`|a|^(-1/2)|x|^(-1/2)`                                                  (2.5)

at displacement `x` from the residual value, uniformly in the shift `a^(-1)A[0,K]y`. Hence

`p_Q(q) <= |a|^(-1/2) int |q-r|^(-1/2) p_R(r) dr`.                     (2.6)

Let `N=||p_R||_3`. For any `rho>0`, Hölder on `|q-r|<=rho` and probability normalization outside give

`int |q-r|^(-1/2)p_R(r)dr`
` <=4 N rho^(1/6)+rho^(-1/2)`.                                         (2.7)

The minimum occurs at `rho^(1/6)=(3/(4N))^(1/4)`, and equals

`2^(7/2)3^(-3/4) N^(3/4)`.                                              (2.8)

Insert (1.4):

`N^(3/4) <= 3^(1/2)2^(1/4)D^(-1/8)`.

Equations (2.6)--(2.8) give exactly (2.3)--(2.4). QED.

**Regularity statement.** Section 2 proves existence of an essentially bounded density in its stated scope. It does **not** prove continuity for arbitrary cap-one input densities, because the square shift in (2.1) may depend on the same residual variables and the argument is a fractional-potential bound rather than `L^1` Fourier inversion.

## 3. Exact clustered-coheavy 3-volume identity

Let `M` be any physical cross block with row vectors `r_1,...,r_m` and

`Z=e_3(M^T M)>0`.

Let `w_0` be the natural squared-3-volume distribution on pairs `(S,T)` of three rows and three columns:

`w_0(S,T)=det(M_ST)^2/Z`.

For two distinct rows `i,k`, define

`p_ik=P_w0({i,k} subset S)`,
`D_ik=||r_i wedge r_k||_2^2`,                                           (3.1)

and, when `D_ik>0`, let `P_ik` be orthogonal projection in column space onto `span(r_i,r_k)^perp` and set

`R_ik=sum_{ell != i,k} ||P_ik r_ell||_2^2`.                             (3.2)

Then the following identity is exact:

**`p_ik Z = D_ik R_ik`.**                                               (3.3)

Indeed, Cauchy--Binet for each fixed row triple gives

`sum_{|T|=3} det M[{i,k,ell},T]^2`
` = det Gram(r_i,r_k,r_ell)`
` = D_ik ||P_ik r_ell||^2`.                                             (3.4)

Summing over `ell` proves (3.3).

If row `i` has natural 3-volume marginal `alpha_i>1/2` and a conditional co-heavy partner satisfies

`P(k in S | i in S)>1/2`,                                                (3.5)

then

`p_ik>1/4`, hence

**`D_ik R_ik > Z/4`.**                                                   (3.6)

Thus the previously unpaid clustered-coheavy branch carries a concrete product of two aggregate currencies: physical pair area `D_ik` times the entire transverse residual energy `R_ik`. No individual `3x3` minor is selected.

A useful threshold form is: for every `eta>0`, either

`D_ik>=eta`,                                                            (3.7)

or

`R_ik>Z/(4 eta)`.                                                       (3.8)

When the cross block occurs inside a scalar-pivot Schur residual, branch (3.7) is paid by (2.3); branch (3.8) isolates the remaining diffuse transverse-energy debt.

## 4. Why this is a replacement for the false scalar pointwise bound

The phase-aligned fragmented-support counterexample remains untouched. For any prescribed scalar frequency `s>0` and sufficiently small `delta>0`, the set

`{x: dist(s x^2,2pi Z)<=delta}`

has infinite Lebesgue measure. A finite union of its components of total length one gives a cap-one probability density with

`Re E exp(i s X^2)>=cos(delta)`.

So no scalar law-uniform positive power pointwise decay is available.

By contrast, (1.2) is produced by a **two-dimensional random linear slope** after retaining arbitrary quadratic phase, and its genuinely useful output is the integrated estimate (1.3). The scalar-square lift spends that `L^{3/2}` frequency budget through an `L^3` density/fractional-potential estimate. No scalar Fresnel pointwise estimate is used.

## 5. Designated partner r31 applied to an actual new inequality

Use the notation of partner fleet02/B01 r31. Let a Schur-residual physical cross block `M` have

`Z=e_3(M^T M)>0`.

Let row `h` have natural 3-volume marginal `alpha>1/2`, let `r_h` be that row, and let `N` be `M` with `h` deleted. Partner r31 proves

`E_2:=e_2(N^T N) >= alpha Z/||r_h||_2^2`.                              (5.1)

Suppose an actual physical row pair `(j,k)` of `N` carries a fraction `theta>0` of this aggregate two-volume:

`D_jk=||r_j wedge r_k||_2^2 >= theta E_2`.                              (5.2)

Then (5.1) gives the concrete lower bound

`D_jk >= theta alpha Z/||r_h||_2^2`.                                   (5.3)

If `M` is a cross block of the Schur residual after a physical scalar pivot `a!=0`, applying Theorem (2.3) to this actual pair yields

**`||p_Q||_infinity <= C_* |a|^(-1/2)`**
**`   * [theta alpha Z/||r_h||_2^2]^(-1/8)`.**                          (5.4)

This is a direct application of the completed partner result to a new density inequality. It closes the branch where the partner's residual two-volume has a dimension-free concentration fraction `theta`; no reciprocal `2x2` **column** minor is paid. The unresolved complementary case is precisely when the partner's guaranteed `e_2` currency is itself spread over many physical row pairs, requiring another aggregate-before-selection step.

## 6. What remains unpaid

The full three-large-eigenvalue conjecture is still open. The new analytic gate says that after a usable physical scalar pivot, **one aggregate two-row wedge in the Schur residual is enough**; unlike earlier rank-two-bank theorems, the residual cross block may have arbitrary rank and the selected pair may have arbitrary self/mutual quadratic terms.

The structural debt is now:

`QFORM-DIFFUSE-E2-AFTER-COHEAVY-v1` — in a branch where natural 3-volume is clustered on co-heavy rows but every individual residual pair wedge is small, spend the guaranteed aggregate `e_2` and the exact transverse-energy identity (3.3) without selecting a vanishing physical pair. Candidate mechanisms are a fractional/mixed-order row-pair Brascamp--Lieb average or a grouped transverse bank recursion. The exact identity (3.3) should be retained as the normalization check.

No full-solution claim is made and the two independent end-to-end reviews required for a full candidate do not exist.

## Finite checker

A seeded checker verifies (3.3) on 200 random rectangular matrices by comparing the Cauchy--Binet sum over all `3x3` minors containing a selected row pair against `D_ik R_ik`; maximum normalized discrepancy was below `1.3e-15`. It also verifies the constants in (1.4) and (2.4). These computations are regression evidence only; all substantive statements above are proved analytically.
