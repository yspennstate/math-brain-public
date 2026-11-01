SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-22T20:10:15Z.
attacking: a physical-row integrated Fourier estimate stable through zero/near-zero diagonal pivots, then applying the named fleet03/B02 overlap-one/localized results to the first unpaid near-isotropic branch.

# QFORM-PHYSICAL-ROW-LP-FOURIER-v1

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260922T201015Z-fleet02-B02-qform-r12`.
Fresh owner control applied: revision `2026-09-22.15`.
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Exact target and live corrections

The target is unchanged: for independent real coordinates with one-dimensional densities bounded by one and an arbitrary real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `Q=X^T A X`, or give a valid counterexample. No moments, compact support, log-concavity, diagonal-coordinate assumption, or independence after a spectral rotation is used.

The current corrections are respected. In particular, this report does not use law-uniform pointwise Fresnel decay; the refuted arbitrary-joint rank-three coarea lemma; the refuted positive conditional-projection-density moments; a fixed good physical minor; the false scalar-conditioning supremum; or post-rotation independence. The current owner-side source still proposes an unweighted `L^1` characteristic-function route, but no exact-target counterexample to that criterion is known to me in this run. The newest named-partner report also records only a logarithmically divergent *normalized conditional-L3 majorant*, not a counterexample to `phi_Q in L^1`; I therefore do not upgrade that failure into a false claim about the target-wide Fourier criterion.

## 2. Source-pinned partner inputs actually consumed

### 2.1 Latest named partner fleet03/B02, r14

Completed report:

`yspennstate/math-open-problems@54c9b45ccd6dd4dd686e91ff04e39e2cc5ebbbcf`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T200207Z-fleet03-B02-qform-r14/REPORT.md`.

Its correction-safe theorem says that if an ORIGINAL-coordinate principal `3 x 3` block `B` satisfies `sigma_min(B)>=c>0`, then the full ambient form has an essentially bounded density with

`||p_Q||_infinity <= 128*2^(1/4)/c`.                                      (2.1)

This result is used below as the localized branch of the conditional end-to-end reduction. It avoids the now-refuted arbitrary-joint coarea argument.

### 2.2 Named partner fleet03/B02, overlap-one theorem from r13

Completed report:

`yspennstate/math-open-problems@1b8f72a4e25ef55ca4fd974007146d3971f49bf8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T190121Z-fleet03-B02-qform-r13/REPORT.md`.

For an exact-rank-three form `A=R Lambda R^T`, `R^T R=I_3`, with triple weights `w_I=det(R_I)^2`, overlap-one mass `D_1`, row leverage `c_i=||r_i||^2`, residual disjoint-pair mass `d_i`, and `z_i=c_i^2 d_i`, it proves

`D_1=sum_i z_i`,                                                         (2.2)

and, for

`E_1(tau)=sum_{i:|A_ii|>=tau} z_i`,

if `E_1(tau)>0`,

`||p_Q||_infinity <= 4 sqrt(3 pi) |det Lambda|^(-1/4)
                      tau^(-1/4) E_1(tau)^(-1/4)`.                      (2.3)

It also proves the square-root selection estimate

`max_{i in L} z_i >= (sum_{i in L}z_i)^2/9`.                            (2.4)

The unpaid branch isolated there is overlap-one mass concentrated on small `|A_ii|`. The theorem below attacks exactly that branch without dividing by `A_ii`.

### 2.3 One-dimensional product-projection source

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, prove that a one-dimensional orthogonal marginal of a product density with one-dimensional factors bounded by one has density at most `sqrt(2)`. Consequently, for independent cap-one variables and a nonzero coefficient vector `b`, the linear form `sum b_j X_j` has density at most

`sqrt(2)/||b||_2`.                                                       (2.5)

Only this one-dimensional consequence is used.

## 3. Main theorem: a diagonal-uniform physical-row `L^p` estimate

### Theorem 3.1 — `QFORM-PHYSICAL-ROW-LP-SHEAR-v1`

Let `X` be independent of a random element `W`, with density `f_X<=1`. Let `U=U(W)` have a marginal density bounded by `M<infinity`, and let `R=R(W)` be arbitrary and allowed to depend completely on `U`. For any real `a`, put

`T = a X^2 + 2 X U + R`.                                                (3.1)

Then for every `1<p<2`, `T` has a density and

`boxed:
 ||p_T||_p
 <= [ 2^(p-1)/(2-p) ]^(1/p) M^((p-1)/p).
`                                                                           (3.2)

The bound is **uniform in `a`**, including `a=0`. At the convenient exponent `p=3/2`,

`boxed: ||p_T||_(3/2) <= 2 M^(1/3).`                                    (3.3)

With the Fourier convention

`phi_T(t)=int exp(i t s) p_T(s) ds`,

Hausdorff--Young therefore gives the genuine integrated characteristic-function estimate

`boxed: ||phi_T||_3 <= 2 (2 pi)^(1/3) M^(1/3).`                         (3.4)

This is not a pointwise oscillatory estimate.

### Proof

Condition first on `W=w`, so `u=U(w)` and `r=R(w)` are constants. Translation by `r` does not change any `L^p` norm. For fixed `u`, consider

`F_u(x)=a x^2+2ux`.                                                       (3.5)

For almost every output value, `F_u` has at most two inverse branches. Its conditional pushforward density is

`g_u(y)=sum_{x:F_u(x)=y} f_X(x)/|2(ax+u)|`.                              (3.6)

For `p>1`, using `(s+t)^p<=2^(p-1)(s^p+t^p)` and then the one-dimensional change-of-variables formula on the monotone branches,

`||g_u||_p^p
 <= 2^(p-1) int f_X(x)^p |2(ax+u)|^(1-p) dx
 = int f_X(x)^p |ax+u|^(-(p-1)) dx.`                                    (3.7)

For `a=0` there is only one branch and the same displayed inequality remains valid (indeed it is then nonsharp by a harmless factor).

Now mix over `W`. Minkowski and Jensen give

`||p_T||_p
 <= E ||g_U||_p
 <= [ E ||g_U||_p^p ]^(1/p).`                                            (3.8)

Set `beta=p-1 in (0,1)`. For every real shift `v`, among all probability densities bounded by `M`, the integral against the symmetric decreasing kernel `|u-v|^(-beta)` is maximized by the cap-saturated centered interval of length `1/M`. Hence

`sup_v E |U-v|^(-beta)
 <= M * 2 int_0^(1/(2M)) s^(-beta) ds
 = 2^beta M^beta/(1-beta).`                                             (3.9)

Because `f_X<=1` and `int f_X=1`, one has `int f_X^p<=1`. Averaging (3.7), using (3.9) with `v=-ax`, gives

`E ||g_U||_p^p
 <= 2^(p-1) M^(p-1)/(2-p).`                                             (3.10)

Taking the `p`th root proves (3.2). At `p=3/2`, the constant simplifies exactly to `2`, proving (3.3). Standard Hausdorff--Young interpolation for the present Fourier normalization gives

`||phi_T||_3 <= (2pi)^(1/3)||p_T||_(3/2)`,                              (3.11)

which is (3.4). QED.

### Why the dependence statement matters

`R(W)` may be an arbitrary function of the same variables that determine `U`. Thus (3.2) survives precisely the dependence pattern that invalidates several conditional-cap shortcuts in the correction inbox. The only independence used is the original-coordinate independence of `X` from the remaining coordinates. The estimate is also stable through `a=0` and `a` arbitrarily close to zero, so it does not pay a reciprocal physical scalar pivot.

## 4. Direct full-matrix corollary

Fix any original coordinate `i` in an arbitrary symmetric matrix `A` and write

`a=A_ii`,

`U_i=sum_{j!=i} A_ij X_j`,

`R_i=X_{-i}^T A_{-i,-i} X_{-i}`.                                       (4.1)

Then

`Q=a X_i^2+2X_i U_i+R_i`.                                                (4.2)

Let

`sigma_i=(sum_{j!=i}A_ij^2)^(1/2)`.                                     (4.3)

If `sigma_i>0`, (2.5) gives `||p_(U_i)||_infinity<=sqrt(2)/sigma_i`. Therefore Theorem 3.1 yields, for every `1<p<2`,

`boxed:
 ||p_Q||_p
 <= [2^(p-1)/(2-p)]^(1/p)
    (sqrt(2)/sigma_i)^((p-1)/p).
`                                                                           (4.4)

In particular,

`boxed: ||p_Q||_(3/2) <= 2^(7/6) sigma_i^(-1/3),`                       (4.5)

and

`boxed: ||phi_Q||_3 <= 2^(7/6)(2pi)^(1/3) sigma_i^(-1/3).`              (4.6)

No hypothesis is placed on `A_ii`, the residual spectrum, or the dependence between `U_i` and `R_i`.

This is a target-compatible integrated-Fourier resource for a physical row: substantial off-diagonal row energy alone gives a quantitative global `L^3_t` budget for the full quadratic-form characteristic function.

## 5. Applying the named partner overlap-one result to the near-isotropic branch

Assume now the exact-rank-three setting of source 2.2 and the target normalization `|lambda_j|>=1`. Suppose

`D_1>=eta>0`.                                                           (5.1)

Choose

`tau=sqrt(eta/12)`.                                                      (5.2)

There are two cases.

### Case A: non-isotropic overlap-one mass

If

`E_1(tau)>=D_1/2>=eta/2`,                                                (5.3)

then the named partner inequality (2.3) directly gives

`||p_Q||_infinity
 <=4 sqrt(3pi) (2/(tau eta))^(1/4)
 =4 sqrt(3pi)(2 sqrt(12))^(1/4) eta^(-3/8).`                            (5.4)

Thus this half of the overlap-one channel is already paid at `L^infinity`.

### Case B: near-isotropic overlap-one mass

Otherwise, with

`N={i:|A_ii|<tau}`,

(2.2) gives

`sum_{i in N} z_i > D_1/2 >= eta/2`.                                    (5.5)

The partner selection (2.4) supplies `i in N` with

`z_i=c_i^2d_i >= eta^2/36`.                                             (5.6)

Because `0<c_i<=1` and `0<=d_i<=1`, this single selected row simultaneously satisfies

`c_i>=eta/6`,   `d_i>=eta^2/36`.                                        (5.7)

For exact rank three,

`sum_{j!=i}A_ij^2
 = ||Lambda r_i||_2^2-A_ii^2
 >= c_i-A_ii^2
 > eta/6-eta/12
 = eta/12.`                                                              (5.8)

Hence

`sigma_i>sqrt(eta/12)`.                                                  (5.9)

The one-dimensional projection theorem gives

`||p_(U_i)||_infinity <= sqrt(24/eta)`.                                 (5.10)

Substituting this actual inequality into Theorem 3.1 at `p=3/2` yields

`boxed:
 ||p_Q||_(3/2) <= 2 (24/eta)^(1/6),
`                                                                           (5.11)

and therefore

`boxed:
 ||phi_Q||_3 <= 2(2pi)^(1/3)(24/eta)^(1/6).
`                                                                           (5.12)

The same selected row retains the independent residual disjoint-pair currency `d_i>=eta^2/36`; it was not discarded to obtain (5.12).

### Corollary 5.1 — `QFORM-RANK3-OVERLAP1-LINF-OR-L3-v1`

For every exact-rank-three target form with `D_1>=eta`, either the density is already bounded by (5.4), or the full characteristic function has the global `L^3` bound (5.12) at a row whose residual disjoint-pair mass also satisfies `d_i>=eta^2/36`.

This is the requested application of the named partner's actual exterior-mass identity and estimate. It converts the partner's first unpaid **near-isotropic physical-pivot** branch into a diagonal-uniform integrated-Fourier resource without post-rotation independence.

## 6. Applying the latest named partner r14 localized theorem

The newest fleet03/B02 theorem (2.1) supplies the complementary localized branch exactly: for every chosen fixed `c>0`,

`exists an original-coordinate principal 3x3 B with sigma_min(B)>=c`

implies

`boxed: ||p_Q||_infinity <=128*2^(1/4)c^(-1).`                          (6.1)

Thus the live conditional proof skeleton may now discard this branch rigorously, without the false arbitrary-joint coarea lemma. Outside (6.1), all physical triples have `sigma_min<c`, and the remaining Fourier/geometric work must aggregate coordinates before reciprocal local-minor payment. Corollary 5.1 is one such aggregate payment on the exact-rank-three overlap-one channel.

This is an actual inequality application of the latest named partner result, not a citation-only dependency.

## 7. Relation to the unweighted `L^1` Fourier criterion

Theorem 3.1 proves a uniform **integrated** characteristic-function estimate, but at `L^3_t`, not `L^1_t`. It therefore does not by itself close bounded density by Fourier inversion. It is nonetheless stronger than a pointwise-decay surrogate in the relevant near-isotropic branch because it is law-uniform under the exact product hypotheses and stable under arbitrary residual dependence.

The newest partner r14 reports that a straightforward normalized conditional-`L^3` implementation of the revision-15 decoupling template has a logarithmically divergent majorant on a valid diagonal product family. That is a counterexample to that intermediate *majorant*, not to the unweighted target-wide assertion `phi_Q in L^1`. I found no exact-product target counterexample to the latter and do not claim one.

## 8. First unpaid implication

The first unpaid implication exposed by this run is now:

> In Case B of Corollary 5.1, combine the diagonal-uniform global `L^3_t` credit (5.12) with the simultaneously retained residual disjoint-pair mass `d_i>=eta^2/36` to obtain either a global `L^1_t` estimate for `phi_Q` or a direct `L^infinity` density estimate, **without** dividing by the small scalar pivot `A_ii` and without factorizing dependent spectral coordinates.

Equivalently, derive a product-preserving vector-valued/grouped-coordinate estimate that spends the residual two-bank resource before absolute values destroy its interaction with the physical-row shear. A formal multiplication of separate characteristic functions is not allowed because the pieces share original coordinates.

At the full-matrix level, the conditional proof remains: partner r14 closes any quantitatively localized physical `3x3` block; completed ridge/cross/grouped-hyperbolic branches close their stated scopes; the surviving aggregate geometry must be converted to enough row/bank integrated Fourier credit to close `L^1`, or bounded density must be obtained directly. The unrestricted theorem remains open.

## 9. Status and provenance

Classification: `ESSENTIAL_STEP_APPLIED`.

New results:

1. `QFORM-PHYSICAL-ROW-LP-SHEAR-v1`, equations (3.2)--(3.4).
2. Full-matrix row corollary, equations (4.4)--(4.6).
3. `QFORM-RANK3-OVERLAP1-LINF-OR-L3-v1`, equations (5.4), (5.11), (5.12).

Named partner actually applied: fleet03/B02 r14 localized theorem and r13 overlap-one theorem, source commits stated above.

No full-target proof, target counterexample, or novelty/priority claim is made. No numerical experiment is used as proof.
