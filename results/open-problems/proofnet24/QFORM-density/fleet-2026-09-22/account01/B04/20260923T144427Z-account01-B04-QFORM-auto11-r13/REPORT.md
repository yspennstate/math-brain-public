SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T14:44:27Z.
attacking: entropy-optimal third-volume reweighting via an exact Gibbs dual, then convert poor Fourier currency into a bounded physical compound-hub certificate and test it on a fully dense rotated indefinite form.

# account01/B04 r13 — Gibbs dual for third-volume Fourier weights and a quantitative soft-hub exit

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Outcome: `SUPPORTING_THEOREM_PROVED / ESSENTIAL_MISSING_IMPLICATION_ADVANCED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Continuity in the new Fourier branch: **proved (`C_0`)**.  
Full unrestricted QFORM theorem: **OPEN**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The proof stays entirely in original-coordinate product space. It uses no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint coarea estimate, no conditional projection-cap moment, no bounded-support assumption, and no moment assumption.

## 1. Fresh sources actually used


The newest required Claude/e5 source was read at the immutable source

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,
- `.../FOURIER_ROUTE_REPORT.md`,
- `.../COUNTEREXAMPLE_SEARCH.md`.

The equation-level input from e5 is Theorem D and its arbitrary-weight/KL remark: a physical third-minor law may replace canonical volume sampling, with determinant volume replaced by the entropy-adjusted determinant currency. The D' extension raises the row-marginal gate from `1/2` to every strict `h<3/4`. This run solves the exact finite-dimensional entropy optimization behind that arbitrary-weight step.

For the final constant I use this slot's completed sharper compiler

- `QFORM-ENTROPY-WEIGHTED-THREE-VOLUME-v1`,
- `yspennstate/math-open-problems@1d2dd52680ec729f28b7289e74a6f3752a379127`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T021315Z-account01-B04-QFORM-auto11/REPORT.md`.

If a probability law `w` on supported physical `3 x 3` minors has constrained-side row marginals `alpha_i<=q/2`, `1<=q<3/2`, and

`G(w)=exp(sum_(S,T) w_(S,T) log(det(M[S,T])^2/w_(S,T)))`,

then the full ambient quadratic form, with arbitrary same-bank curvature, outside couplings and induced affine terms, satisfies

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6)`,          (1.1)

and has a representative in `C_0(R)`.

The designated partner theorem actually applied below is account02/B04

- `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`,
- `yspennstate/math-open-problems@febf0c97f0f85e802b6bc2ab4a475c15109de013`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260923T111930Z-qform/REPORT.md`.

It completely pays the exact strict-`3/4` support-defect geometries. In particular an exact-rank-three four-row tetrahedral packet with third volume `E3` has a `C_0` density bounded by `6 E3^(-1/6)`.

## 2. Compress full minors to a row-volume entropy problem

Let `M=A[I,J]` be an original-coordinate physical cross block. For every physical row triple `S subset I`, put

`a_S = det(M_S M_S^T)
     = sum_(|T|=3) det(M[S,T])^2`.                              (2.1)

Let `B={S:a_S>0}` and

`Z=sum_(S in B) a_S=E3(M)`.

Given any probability law `mu` on `B`, lift it to full physical minors by retaining the canonical conditional column-volume law:

`w_(S,T)=mu_S det(M[S,T])^2/a_S`.                              (2.2)

Then the constrained-side row marginals are exactly

`alpha_i(mu)=sum_(S contains i) mu_S`,                          (2.3)

and the full determinant/entropy currency collapses exactly to

`boxed: G(mu)=exp(sum_S mu_S log(a_S/mu_S)).`                   (2.4)

Indeed `det(M[S,T])^2/w_(S,T)=a_S/mu_S` on every supported minor. Thus the column complexity disappears from the entropy optimization without rotating any random coordinate.

Let

`p_S=a_S/Z`                                                     (2.5)

be the canonical row-volume law. Then there is also the exact KL identity

`boxed: log[Z/G(mu)] = D_KL(mu||p).`                            (2.6)

So the best admissible Fourier weight is precisely the information projection of canonical physical volume onto a marginal polytope.

## 3. New theorem — `QFORM-THIRDVOLUME-GIBBS-DUAL-AND-SOFT-HUB-v1`

Fix `0<h<1`. Define

`F_h={mu on B: alpha_i(mu)<=h for every physical row i}`,

and define the optimal admissible currency

`G_h(M)=sup_(mu in F_h) G(mu)`,                                 (3.1)

with `G_h=0` if `F_h` is empty.

### Theorem 3.1: exact Gibbs dual

One has the exact finite-dimensional dual formula

`boxed:
 G_h(M)=inf_(lambda_i>=0)
 exp(h sum_i lambda_i)
 sum_(S in B) a_S exp(-sum_(i in S)lambda_i).`                  (3.2)

Equivalently,

`G_h(M)=Z exp[- inf_(mu in F_h) D_KL(mu||p)].`                  (3.3)

When the dual infimum is attained at a finite vector `lambda`, the corresponding primal optimizer is the Gibbs tilt

`boxed:
 mu_lambda(S)=
 a_S exp(-lambda(S)) /
 sum_R a_R exp(-lambda(R)),
 lambda(S)=sum_(i in S)lambda_i,`                               (3.4)

and complementary slackness gives

`lambda_i>0  =>  alpha_i(mu_lambda)=h`.                         (3.5)

Boundary cases are obtained by limits; no existence of a finite threshold on the infinite line is assumed.

#### Proof

For `mu` in the full probability simplex on `B` and `lambda_i>=0`, set

`L(mu,lambda)
 = sum_S mu_S log(a_S/mu_S)
   + sum_i lambda_i[h-alpha_i(mu)].`                            (3.6)

If `mu in F_h`, then `inf_lambda L=log G(mu)`. If some marginal exceeds `h`, sending its multiplier to infinity gives `inf_lambda L=-infinity`. Hence

`sup_mu inf_lambda L = log G_h`.                               (3.7)

The probability simplex is compact convex, the multiplier cone is convex, and `L` is concave upper-semicontinuous in `mu` and affine in `lambda`; the finite-dimensional minimax theorem gives

`sup_mu inf_lambda L = inf_lambda sup_mu L`.                   (3.8)

For fixed `lambda`, the Gibbs variational identity gives

`sup_mu L
 = h sum_i lambda_i
   + log sum_S a_S exp[-lambda(S)].`                            (3.9)

Exponentiating proves (3.2). The maximizing law in (3.9) is (3.4); the usual KKT complementary slackness gives (3.5). Identity (3.3) is just (2.6). QED.

### Theorem 3.2: poor entropy currency forces a bounded compound hub

Let

`eta=G_h(M)/E3(M)` in `[0,1]`.                                  (3.10)

Then there exists a set of physical rows `H` satisfying

`boxed: |H| < 3/h`                                              (3.11)

such that

`boxed:
 E3(M[I\H,J]) <= G_h(M) = eta E3(M).`                           (3.12)

Equivalently,

`boxed:
 G_h(M) >= min_(|H|<3/h) E3(M[I\H,J]).`                         (3.13)

In particular, at the useful fixed gate `h=3/5`, either the admissible third-volume Fourier currency is target-scale, or deleting at most **four** physical row hubs makes the residual third volume comparably small.

#### Proof

Suppose first `eta<1`; the endpoint `eta=1` is trivial. For every `eps>0`, the dual supplies `lambda>=0` with

`exp(h Lambda) E_(S~p) exp[-lambda(S)] <= eta+eps`,
`Lambda=sum_i lambda_i`.                                       (3.14)

For `eps<1-eta`, necessarily `Lambda>0`. Normalize

`omega_i=lambda_i/Lambda`, `sum_i omega_i=1`,                  (3.15)

and define

`H={i: omega_i>h/3}`.                                           (3.16)

Since the `omega_i` sum to one, `|H|<3/h`. Every triple avoiding `H` satisfies `omega(S)<=h`, hence `lambda(S)<=h Lambda`; on that event the integrand in (3.14), after multiplication by `exp(h Lambda)`, is at least one. Therefore

`p{S cap H = empty} <= eta+eps`.                                (3.17)

But by row Cauchy-Binet,

`p{S cap H=empty}
 = E3(M[I\H,J])/E3(M)`.                                        (3.18)

Only finitely many row sets of cardinality `<3/h` occur, so letting `eps` decrease to zero and passing to a repeated set proves (3.12). If `eta=0`, the same limiting argument applies. QED.

This is the first essential missing implication attacked this run: the fleet's phrase "poor determinant/entropy currency" is no longer qualitative. It produces a concrete bounded original-coordinate compound hub. No reciprocal individual minor is selected.

### Corollary 3.3: a usable Fourier/hub dichotomy

For `1/2<=h<3/4`, set `q=2h`. Given any `g>0`, either

`G_h(M)>=g`,

in which case (1.1) gives

`boxed:
 ||p_Q||_infinity
 <= [3e/((3-4h)sqrt(2h))] g^(-1/6),
 p_Q in C_0(R),`                                                (3.19)

or there is a physical hub set `H`, `|H|<3/h`, with

`E3(M[I\H,J])<g`.                                               (3.20)

This is not yet the global three-eigenvalue theorem: one still has to pay the bounded hub branch from the bare spectral hypothesis without multiplying by a tiny extra singular direction.

## 4. Exact one-hub information projection

The Gibbs dual has a closed form when one physical row is the only active marginal obstruction. Let row `0` be the hub and write

`Z1=sum_(S contains0) a_S`,
`Z0=sum_(S not contains0) a_S`,
`Z=Z1+Z0`, `p=Z1/Z`.                                           (4.1)

Assume `p>h` and that the one-coordinate tilt below satisfies all other row constraints. Then the KL projection fixes total incident mass to `h` and preserves canonical relative proportions inside the incident and nonincident classes:

`mu(S)=h a_S/Z1` for `0 in S`,
`mu(S)=(1-h)a_S/Z0` for `0 notin S`.                            (4.2)

The optimal currency is exactly

`boxed:
 G_h=(Z1/h)^h (Z0/(1-h))^(1-h)
    = Z exp[-D_Ber(h||p)].`                                    (4.3)

The dual multiplier is determined by

`exp(-lambda_0)=h Z0/[(1-h)Z1].`                               (4.4)

Thus a near-coloop does not require an arbitrary reciprocal local-minor penalty; it pays the exact Bernoulli information cost needed to lower its inclusion frequency.

## 5. Fully dense genuinely rotated indefinite target family

Let

`V=I_4-(1/2)J_4`,                                               (5.1)

which is orthogonal. Let the four tetrahedral sign vectors be

`s1=(1,1,1), s2=(1,-1,-1), s3=(-1,1,-1), s4=(-1,-1,1)`.       (5.2)

For `L>0`, form the `5 x 4` matrix `R_L` whose first row is `L e1` and whose remaining four rows are

`(0,s1),...,(0,s4)`.                                           (5.3)

Put

`M_L=R_L V`.                                                    (5.4)

Then

`R_L^T R_L=diag(L^2,4,4,4)`,                                   (5.5)

so the singular values of `M_L` are exactly

`L,2,2,2`.                                                      (5.6)

For `L=32`,

`M = [[16,-16,-16,-16],
      [-3/2,-1/2,-1/2,-1/2],
      [ 1/2, 3/2,-1/2,-1/2],
      [ 1/2,-1/2, 3/2,-1/2],
      [ 1/2,-1/2,-1/2, 3/2]].`                                 (5.7)

Every physical cross coefficient is nonzero. To make the **entire** ambient symmetric matrix dense, define

`A_L=[[J_5/100, M_L],
      [M_L^T,    J_4/100]].`                                   (5.8)

Every entry of `A_L` is nonzero. If the same-bank blocks in (5.8) are set to zero, the exact spectrum is

`{+L,-L,+2,+2,+2,-2,-2,-2,0}`.                                (5.9)

The perturbation in (5.8) has operator norm `1/20`. Thus at `L=32`, Weyl's inequality leaves four negative eigenvalues at most `-39/20` and four positive eigenvalues at least `39/20`. In particular this is a genuinely rotated, fully dense, indefinite instance of the owner's exact target, with **eight** eigenvalues of modulus at least one.

The new theorem permits the arbitrary same-bank curvature in (5.8), so the perturbation is not discarded in the density argument.

## 6. Exact row-volume geometry and the new explicit bound

The row-triple volumes of `M_L` have only two values:

- each of the six triples containing the hub row has `a_S=8L^2`;
- each of the four triples avoiding the hub has `a_S=16`.

Hence

`Z1=48L^2`, `Z0=64`, `E3(M_L)=48L^2+64`.                       (6.1)

At `L=32`,

`E3=49216`,
`p_hub=Z1/E3=768/769`.                                         (6.2)

So canonical volume sampling is essentially a coloop: its hub marginal is about `0.9987`, far outside every strict `3/4` Fourier gate.

Now take

`h=3/5`, `q=6/5`.                                               (6.3)

The one-hub Gibbs tilt has

`exp(-lambda_hub)=2/L^2`;                                      (6.4)

at `L=32` this is `1/512`. It equalizes all ten row-triple Gibbs weights. Thus the optimal row law is simply **uniform on all `C(5,3)=10` row triples**, and every one of the five row marginals is exactly

`alpha_i=6/10=3/5`.                                            (6.5)

The exact optimal currency is

`G_(3/5)(M_L)
 = (80L^2)^(3/5) 160^(2/5)
 = 80*2^(2/5)*L^(6/5).`                                        (6.6)

At `L=32`,

`G = 5120*2^(2/5)
  = 6755.880503157218... .`                                    (6.7)

Applying (1.1) with `q=6/5` gives, for **every** independent cap-one product input law,

`boxed:
 ||p_(X^T A_32 X)||_infinity
 <= 2.853602893356842...,
 p_(X^T A_32 X) in C_0(R).`                                    (6.8)

More generally this family obeys

`||p_(X^T A_L X)||_infinity
 <= 5.707205786713684... * L^(-1/5).`                           (6.9)

The decreasing power in `L` is not obtained by a pointwise scalar stationary-phase estimate; it is entirely the entropy-balanced physical minor product-Fourier certificate.

## 7. Designated partner applied to the same actual matrix

Condition only on the original hub-row coordinate of the left bank. This is legitimate original-coordinate conditioning. The residual physical cross block consists of the four tetrahedral rows and has exact singular values

`2,2,2`,                                                      (7.1)

so

`E3=64`.                                                        (7.2)

It has four active physical rows. Any law on row triples has marginal sum three over those four rows, hence some marginal is at least `3/4`; the strict support gate is impossible. This is exactly the support-defect scope of the completed designated-partner account02/B04 theorem. Because this residual block has exact rank three, the partner's sharper branch gives the actual all-input-law inequality

`boxed: ||p_(X^T A_32 X)||_infinity <= 6*64^(-1/6)=3.`          (7.3)

The fixed hub value only induces affine terms, and the same-bank `J/100` curvature is allowed by the partner theorem. Averaging the uniform conditional bound preserves it.

The new full-volume Gibbs weight therefore improves the completed partner certificate on the **same fully dense rotated indefinite matrix** from `3` to

`2.853602893356842...`,                                        (7.4)

a factor `1.0513035587...`, while using the very large hub volume instead of conditioning it away.

This comparison is intentionally modest: the point is not the numerical 5% but the mechanism. An almost-coloop canonical volume law can still contain strong global entropy currency after the correct product-space reweighting.

## 8. What changed in the full proof map

The exact support question and the quantitative currency question are now separated cleanly:

1. **Support geometry.** The threshold

`h_*(B)=min_mu max_i alpha_i(mu)`                               (8.1)

has the minimax representation

`h_*(B)=max_(omega_i>=0,sum omega_i=1) min_(S in B) omega(S)`.   (8.2)

This follows by finite minimax from `max_i alpha_i=max_omega E_mu omega(S)`. Account02/B04's completed strict-`3/4` support-defect theorem pays the relevant exact boundary geometries at its stated scope.

2. **Quantitative volume geometry.** Once support is feasible, the optimal determinant currency is not mysterious: it is the Gibbs/I-projection value (3.2)-(3.3).

3. **Soft failure.** If this optimal currency is small, Theorem 3.2 converts it to a bounded physical compound hub with small residual `E3`; for `h=3/5` at most four hubs suffice.

Thus the next exact implication is

`QFORM-GIBBS-SOFT-HUB-TO-COMPOUND-ROUTING-v1`:

> starting from the bounded hub set produced by Theorem 3.2, pay the incident third-volume mass by a mixed-hub / lower-compound / ridge / grouped-coordinate mechanism while preserving arbitrary leaf-bank curvature and without multiplying by an arbitrarily small extra singular direction.

The newest fleet lower-compound work shows this is possible in important symmetric three-hub families, but an exhaustive arbitrary-matrix routing theorem is still missing.

## 9. Scope, corrections, and status

The theorem applies to arbitrary independent one-dimensional input densities `0<=f_i<=1`, arbitrary dimension, arbitrary fragmented/unbounded supports, and arbitrary same-bank curvature/outside couplings within the source compiler's scope. It does not assume Gaussianity, log-concavity, moments, compact support, connected support, or independence of eigen-coordinates.

The source corrections remain active: no law-uniform pointwise van-der-Corput decay is used; bounded projection density alone is not used to control an indefinite quadratic pushforward; no worst fiber-supremum or positive conditional-cap moment is taken; repeated eigenvalues are not treated as Hessian degeneracy; no numerical histogram is used as proof.

The full universal QFORM conjecture and its full-target continuity strengthening are still **OPEN**. The present branch proves a continuous bounded density only under the explicit Gibbs-currency certificate above. Independent end-to-end review of this new theorem is still pending.
