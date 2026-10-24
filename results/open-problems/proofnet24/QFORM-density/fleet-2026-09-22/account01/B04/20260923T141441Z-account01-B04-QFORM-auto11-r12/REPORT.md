SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T14:14:41Z.
attacking: regularize third-volume Fourier weights by mixing canonical E3 volume with fourth-volume face deletion; prove an exact entropy-currency interpolation and exhibit a dense rotated indefinite matrix where both endpoint marginals nearly hit the q=3/2 Fourier barrier but the interior mixture gives a constant-size certificate.

# account01/B04 — regularized E3/E4 volume interpolation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Outcome: `SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATES / FULL_TARGET_OPEN`  
Continuity in the new theorem: **proved (`C_0`)**.  
Full unrestricted QFORM theorem: **OPEN**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The argument stays in original-coordinate product space. It uses no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint coarea estimate, no moment assumptions, and no bounded-support assumption.

## 1. Sources actually used

Fresh owner control at run start was QFORM-only, OWNER CONTROL revision `2026-09-22.15`.

The Fourier compiler used here is this slot's completed theorem

- `QFORM-ENTROPY-WEIGHTED-THREE-VOLUME-v1`,
- `yspennstate/math-open-problems@1d2dd52680ec729f28b7289e74a6f3752a379127`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T021315Z-account01-B04-QFORM-auto11/REPORT.md`.

For any probability law `w` on supported physical `3 x 3` minors, with constrained-side row marginals `alpha_i`, determinant/entropy currency

`G(w)=exp(sum_w log(det(M[S,T])^2/w_(S,T)))`,

and `max_i alpha_i <= q/2`, `1<=q<3/2`, it gives

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6)`,      (1.1)

and `p_Q` has a continuous representative in `C_0(R)`. Arbitrary same-bank quadratic curvature, outside couplings and induced affine terms are retained.

The designated partner result actually applied below is the newest compatible account02/B04 theorem

- `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`,
- `yspennstate/math-open-problems@febf0c97f0f85e802b6bc2ab4a475c15109de013`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260923T111930Z-qform/REPORT.md`.

If `E3(N)>0` and no probability law on the supported physical `3 x 3` minors has every constrained-side row marginal strictly below `3/4`, that theorem gives the ambient form a `C_0` density with

`||p_Q||_infinity <= 6*4^(1/6) E3(N)^(-1/6)`.              (1.2)

Current corrections consumed: the law-uniform pointwise van-der-Corput bound is false; arbitrary bounded joint projection density does not by itself control an indefinite quadratic pushforward; worst-fiber supremum can lose dimension; and a spectral rotation cannot be used to preserve independence.

## 2. Exact regularized face-volume identity

Let `M=A[I,J]` be any original-coordinate cross block and write

`E_k(M)=e_k(M^T M)`.

Assume `E3(M)>0`. For each physical three-row set `S`, put

`a_S = det(M_S M_S^T)
     = sum_(|T|=3) det(M[S,T])^2`.                              (2.1)

For `a_S>0`, define the total squared height of all other physical rows over `span(M_S)` by

`tau_S = sum_(j notin S) dist(m_j, span(M_S))^2`.               (2.2)

When `a_S=0` its value is irrelevant below. The Gram-height identity gives

`sum_(j notin S) det(M_(S union {j}) M_(S union {j})^T)
   = a_S tau_S`.                                                (2.3)

Summing over all triples counts every four-row determinant four times, so

`boxed:  sum_S a_S tau_S = 4 E4(M).`                            (2.4)

Fix `gamma>0` and define

`Z_gamma = 4E4(M)+gamma^2 E3(M)
         = sum_S a_S(tau_S+gamma^2)`,                           (2.5)

`mu_gamma(S)=a_S(tau_S+gamma^2)/Z_gamma`.                       (2.6)

This is an exact interpolation between two product-space volume laws. If

`p_3(S)=a_S/E3(M)`                                              (2.7)

is canonical third-volume sampling and `mu_0` is the uniformly deleted fourth-volume face law, then

`mu_gamma = (1-theta) mu_0 + theta p_3`,                        (2.8)

with

`theta = gamma^2 E3 /(4E4+gamma^2 E3)`.                         (2.9)

Hence its row inclusion marginals satisfy the exact affine interpolation

`alpha_i(gamma)
 = (1-theta) alpha_i^(4->3) + theta alpha_i^(3)`,               (2.10)

where `alpha_i^(4->3)=(3/4)rho_i` and `rho_i` is the canonical fourth-volume row inclusion marginal.

The important point is that different physical rows can be the bad endpoint at the two ends of (2.10), so an interior regularization can cross the Fourier admissibility gate even when both endpoints nearly saturate it.

## 3. Exact entropy currency

Lift `mu_gamma` to full physical `3 x 3` minors by choosing, conditional on `S`, a column triple `T` with probability

`P(T|S)=det(M[S,T])^2/a_S`.                                    (3.1)

Thus

`w_(S,T)=mu_gamma(S) det(M[S,T])^2/a_S`.                        (3.2)

For every supported `(S,T)`,

`det(M[S,T])^2/w_(S,T)=a_S/mu_gamma(S)
                     =Z_gamma/(tau_S+gamma^2)`.                 (3.3)

Therefore the determinant/entropy currency is **exactly**

`boxed:
G_gamma
 = Z_gamma exp[- E_(mu_gamma) log(tau_S+gamma^2)].`             (3.4)

Equivalently, with

`tau_geo,gamma
 = exp(E_(mu_gamma) log(tau_S+gamma^2))`,                       (3.5)

`boxed: G_gamma=Z_gamma/tau_geo,gamma.`                         (3.6)

No reciprocal individual minor is selected.

Since

`tau_S <= sum_j ||m_j||^2 = ||M||_F^2`,                         (3.7)

we have the explicit coarse lower bound

`boxed:
G_gamma >= [4E4(M)+gamma^2 E3(M)]/[||M||_F^2+gamma^2].`         (3.8)

This is the new regularized volume currency.

## 4. New theorem

### Theorem 4.1 — `QFORM-REGULARIZED-E3-E4-VOLUME-INTERPOLATION-v1`

Let `M=A[I,J]` be an original-coordinate cross block with `E3(M)>0`. For `gamma>0`, define `mu_gamma`, `alpha_i(gamma)` and `G_gamma` by (2.6), (2.10), and (3.4). Put

`alpha_*(gamma)=max_i alpha_i(gamma)`,

`q_gamma=max{1, 2 alpha_*(gamma)}`.                              (4.1)

If `alpha_*(gamma)<3/4`, then `q_gamma<3/2`, the full ambient quadratic form has a density in `C_0(R)`, and

`boxed:
||p_Q||_infinity
 <= [3e/((3-2q_gamma)sqrt(q_gamma))]
    G_gamma^(-1/6)`                                            (4.2)

and, in particular,

`boxed:
||p_Q||_infinity
 <= [3e/((3-2q_gamma)sqrt(q_gamma))]
    [(4E4+gamma^2 E3)/(||M||_F^2+gamma^2)]^(-1/6).`            (4.3)

### Proof

The row marginals of the full minor law (3.2) are exactly those of `mu_gamma`, so the hypothesis gives the admissible Fourier exponent `q_gamma<3/2`. Equation (3.4) computes its exact entropy currency. Apply (1.1). The lower bound (3.8) gives (4.3). Integrability of the resulting characteristic-function envelope is inherited from the compiler, so the density representative is continuous and vanishes at infinity. QED.

This theorem genuinely interpolates **marginal geometry**, not merely the scalar currency. The scalar ratio in (3.8) is fractional-linear in `gamma^2`, but the row vector (2.10) can improve strictly in the interior because the heavy row can change between the two endpoint laws.

## 5. Partner endpoint actually paid

The regularized theorem is not a replacement for exact support obstructions. If the physical third-volume support does not admit **any** probability law with all constrained-side row marginals strictly below `3/4`, then the newest account02/B04 theorem (1.2) supplies the actual inequality

`boxed:
||p_Q||_infinity <= 6*4^(1/6) E3(M)^(-1/6),
qquad p_Q in C_0(R).`                                           (5.1)

For a concrete target-valid application, use the first four rows of the explicit matrix in Section 6 below, call the resulting `4 x 4` cross block `N`. Then

`E3(N)=2130`.                                                   (5.2)

Every supported row triple has size three on a four-row ground set, so every probability law on supported triples has

`sum_(i=1)^4 alpha_i=3`.

Hence strict `alpha_i<3/4` for all four rows is impossible. The partner theorem gives

`boxed:
||p_Q||_infinity
 <= 6*4^(1/6)*2130^(-1/6)
 = 2.107485757711179... .`                                     (5.3)

This is an actual use of the designated partner result, not only a citation.

The same four-row block is target-valid: the upper-left `3 x 3` principal block of `N^T N-I` has Sylvester minors

`1, 23, 387`,                                                   (5.4)

so that principal block is positive definite. Cauchy interlacing gives at least three eigenvalues of `N^T N` larger than one, hence the symmetric cross form `[[0,N],[N^T,0]]` has at least six eigenvalues of modulus greater than one.

## 6. Dense rotated indefinite example where the interior mixture opens the gate

Take

`R = [[-1, 1, 0, 0],
      [ 0, 3, 3,-1],
      [ 1, 3,-2,-1],
      [ 0,-3, 3,-1],
      [ 3, 3, 1, 0],
      [-3, 1,-1, 0]]`.                                        (6.1)

Let `v=(1,2,4,8)^T`, `v^T v=85`, and let

`V=I-(2/85)vv^T`.                                               (6.2)

Then `V` is orthogonal. Put

`M=RV`,

`A=[[0,M],[M^T,0]]`.                                            (6.3)

For transparency,

`85 M =
[[-87,  81,  -8, -16],
 [-20, 215, 175,-245],
 [103, 291, -98,  59],
 [  4,-247, 271, -53],
 [229, 203, -19,-208],
 [-245,105, -45,  80]].`                                      (6.4)

Thus **every physical cross coefficient is nonzero**. The form is genuinely non-diagonal and indefinite.

Right orthogonal multiplication preserves singular values and all row Gram determinants. Directly,

`R^T R-I =
[[19,  8,  4,-1],
 [ 8, 37, -4,-3],
 [ 4, -4, 23,-4],
 [-1, -3, -4, 2]]`,                                            (6.5)

whose leading principal minors are

`19, 639, 13545, 12290`.                                       (6.6)

By Sylvester's criterion, `R^T R-I` is positive definite. Hence **all four** singular values of `M` exceed one, and `A` has eight nonzero eigenvalues `+/- sigma_j`, all of modulus greater than one. In particular it satisfies the owner's three-large-eigenvalue hypothesis with room to spare.

The exact volume data are

`E3(M)=20286`,

`E4(M)=30384`,

`||M||_F^2=85`.                                                 (6.7)

The canonical third-volume row marginals are

`alpha^(3)=
(349/3381,
 15175/20286,
 4801/10143,
 11959/20286,
 5563/10143,
 79/147).`                                                      (6.8)

Its largest entry is

`15175/20286 = 0.7480528443...`,                                (6.9)

so the canonical Fourier exponent is already almost at the forbidden endpoint:

`q_3=15175/10143=1.4961056887...`.                              (6.10)

The uniformly deleted fourth-volume face law has row marginals

`alpha^(4->3)=
(235/2532,
 12299/20256,
 3785/5064,
 12587/20256,
 9911/20256,
 8951/20256).`                                                  (6.11)

Now the bad row is different: the third row has

`3785/5064=0.7474328594...`,                                    (6.12)

so this endpoint also sits near `3/4`, with

`q_4=3785/2532=1.4948657188...`.                                (6.13)

Thus **both natural endpoint weights nearly close the Fourier integrability gate, on different rows**.

Choose the interior mixing weight

`theta=1/3`.                                                    (6.14)

By (2.9), this is achieved exactly by

`gamma^2=2E4/E3=3376/1127`.                                    (6.15)

The regularized row marginals are then

`alpha(gamma)=
(412123/4280346,
 67198319/102728304,
 16849129/25682076,
 62743439/102728304,
 52289779/102728304,
 78367/165424).`                                                (6.16)

Their maximum is

`alpha_* = 16849129/25682076
         = 0.6560656934... < 2/3`.                              (6.17)

Therefore

`q_gamma=16849129/12841038
        =1.3121313869... <4/3`.                                 (6.18)

The regularized partition function is

`Z_gamma=4E4+gamma^2E3=182304`,                                 (6.19)

while

`||M||_F^2+gamma^2=99171/1127`.                                (6.20)

Hence the explicit entropy-currency lower bound is

`G_gamma >= 182304/(99171/1127)
          =7609504/3673
          =2071.7408113258916...`.                              (6.21)

Applying Theorem 4.1 gives, for **every** independent cap-one product input law,

`boxed:
||p_(X^T A X)||_infinity
 <= [3e/((3-2q_gamma)sqrt(q_gamma))]
    (7609504/3673)^(-1/6)
 = 5.3066479794034... ,`                                      (6.22)

and

`boxed: p_(X^T A X) in C_0(R).`                                (6.23)

This is the requested explicit estimate for a genuinely rotated indefinite quadratic form.

For scale, applying the same sharp compiler directly to the canonical endpoint (6.8) gives about `163.91`; using the pure fourth-face endpoint with the simple currency lower bound `4E4/||M||_F^2` gives about `193.52`. The point is not those nonoptimal endpoint numerics themselves; it is the structural fact that the interior mixture moves the row-marginal exponent from almost `3/2` down below `4/3` without selecting a tiny minor.

All exact values used above are recorded in `CHECKS.json` in this run directory.

## 7. What this changes structurally

The previous fourth-volume downshift treated `E4` and canonical `E3` as separate mechanisms. The new identity shows that there is a one-parameter **product-space interpolation** whose determinant/entropy currency is explicit and whose row marginals move affinely.

Thus a future global routing argument does not need to decide prematurely between a pure third-volume certificate and a pure fourth-volume face certificate. It can choose `gamma` so that the heavy-coordinate patterns cancel at the marginal level while paying only the regularized scalar currency

`(4E4+gamma^2 E3)/(||M||_F^2+gamma^2)`.                        (7.1)

The exact support-infeasible endpoint is already paid by account02/B04 through (5.1).

## 8. First remaining implication

`QFORM-REGULARIZED-VOLUME-OR-COMPOUND-HUB-ROUTING-v1`:

Starting only from the full symmetric matrix hypothesis `A` has at least three eigenvalues of modulus at least one, prove that some original-coordinate cut `M=A[I,J]` admits either

1. a scale `gamma>0` with `alpha_*(gamma)<=3/4-c` and target-scale regularized currency

   `(4E4(M)+gamma^2E3(M))/(||M||_F^2+gamma^2) >= c0`,

or

2. the exact/quantitative failure is forced into one of the already-paid support-defect, compound-hub, ridge, pair-log, aggregate-square, grouped-bank, or exact-rank branches.

The present theorem solves the **analytic interpolation step** once such a cut and scale are available. It does not prove that the bare three-large-eigenvalue hypothesis always supplies them. Therefore the full conjecture remains open.

## 9. Scope audit

- Inputs: arbitrary independent real coordinates with densities bounded by one.
- No Gaussianity, log-concavity, moments, compact support, connected support, or identical-law hypothesis.
- No independence asserted after an orthogonal spectral rotation.
- Pointwise law-uniform quadratic-phase decay is not used.
- Arbitrary same-bank quadratic curvature and outside couplings are allowed through the imported entropy-weighted Fourier theorem.
- New theorem conclusion: bounded **continuous** density in its stated branch.
- Full owner target: **not proved**.
- Independent review of this new theorem: **pending**.
