SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T15:44:25Z.
attacking: exact marginal factors in the entropy-weighted third-volume product-Fourier compiler, then stress them on a dense permutation-symmetric rotated indefinite block and compare with the newest projection-tail and account02/B04 exits.

# account01/B04 — exact marginal-factor third-volume Fourier bound

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T154425Z-account01-B04-QFORM-auto11-r14`  
Status: `SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not** proved here. The theorem below gives a continuous `C_0` density in its stated product-Fourier scope.

## 1. Source-pinned inputs and corrections

The current control remains revision `2026-09-22.15`, QFORM-only. I used the volume-stability proof at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

and its `PEER_TAIL_EXTENSION.md`. I also applied the designated partner account02/B04 theorem

`QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`

from

`yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec:proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260923T111930Z-qform/REPORT.md`.

The current correction set was refreshed before publication. In particular I do not use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, conditional projection-cap moments, fiber suprema, or pre-Schur rank-two stability. The newest quadratic-hub square-root-slice correction is also immaterial because no slice-only hub reduction occurs below.

## 2. New theorem: retain the exact marginal factors

Let `I,J` be disjoint original-coordinate product banks and let `M=A[I,J]`. Let `w_(S,T)` be any probability law supported on positive physical `3x3` minors, with

`d_(S,T)=det(M[S,T])^2>0`.

Define row and column inclusion marginals

`alpha_i = sum_(S contains i,T) w_(S,T)`,

`beta_j = sum_(S,T contains j) w_(S,T)`,

and the determinant/entropy currency

`G(w)=exp(sum_(S,T) w_(S,T) log(d_(S,T)/w_(S,T))).`

Set

`R(w)=prod_i (1-alpha_i)^(-(1-alpha_i)/2)
      *prod_j (1-beta_j)^(-(1-beta_j)/2)`,

with the continuous endpoint value `1` when an exponent is zero.

### Theorem `QFORM-Q1-EXACT-MARGINAL-FACTOR-v1`

If every row marginal satisfies `alpha_i<=1/2`, then for the full ambient quadratic form, allowing arbitrary within-bank measurable phases/quadratic curvature, arbitrary outside couplings and induced affine terms,

`boxed: ||p_Q||_infinity <= 3 R(w)^(1/3) G(w)^(-1/6).`            (2.1)

Moreover the characteristic function obeys

`boxed: integral_R |phi_Q(t)| dt <= 6 pi R(w)^(1/3) G(w)^(-1/6),` (2.2)

so `p_Q` has a continuous representative vanishing at infinity.

### Proof

The decoupling step in the cited volume-stability report gives

`|phi_Q(t)|^2 <= E_D prod_i |psi_i(2t(MD)_i)|`.               (2.3)

Apply the same Brascamp--Lieb datum as in that proof. The determinant expansion followed by weighted AM--GM with the arbitrary minor weights gives

`det(D_J+M^T D_I M)
 >= G(w) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j).`          (2.4)

Hence the Gaussian BL constant is at most

`G(w)^(-1/2)
 prod_i alpha_i^(-alpha_i/2)
 prod_j (1-beta_j)^(-(1-beta_j)/2).`                           (2.5)

Now use the sharp Hausdorff--Young estimate from the source proof at `q=1`. For each active row,

`|| |psi_i(2t .)| ||_(1/alpha_i)
 <= (pi/|t|)^alpha_i
    alpha_i^(alpha_i/2)
    (1-alpha_i)^(-(1-alpha_i)/2).`                             (2.6)

The powers of `alpha_i` in (2.5) and (2.6) cancel exactly; the column density norms are at most one. Therefore

`|phi_Q(t)|^2
 <= R(w) pi^3 G(w)^(-1/2) |t|^(-3).`                         (2.7)

Together with `|phi_Q|<=1`,

`|phi_Q(t)| <= min(1,K |t|^(-3/2)),
 K=R(w)^(1/2) pi^(3/2) G(w)^(-1/4).`                           (2.8)

The transition point is `K^(2/3)`. Exact integration yields

`integral_R min(1,K|t|^(-3/2))dt = 6 K^(2/3)`,                (2.9)

which is (2.2), and Fourier inversion gives (2.1). Integrability of the characteristic function gives the `C_0` representative. QED.

The generic source bound replaces the two products in `R` by `e^(3/2)` each, hence `R<=e^3` and recovers `3e G^(-1/6)`. Equation (2.1) keeps the actual product geometry instead.

## 3. Doubly balanced six-coordinate corollary

If there are six physical rows and six physical columns and the chosen weight has

`alpha_i=beta_j=1/2`

for every row and column, then

`R=(2^(1/4))^12=8`.

Thus

`boxed: ||p_Q||_infinity <= 6 G(w)^(-1/6),`                   (3.1)

and

`boxed: integral |phi_Q| <= 12 pi G(w)^(-1/6).`              (3.2)

For the canonical squared-minor law `p_(S,T)=d_(S,T)/Z`, `Z=E3(M)`, one has the exact entropy identity

`G(w)=Z exp(-D_KL(w||p))<=Z`.                                 (3.3)

Therefore the canonical law globally maximizes determinant/entropy currency. This does **not** claim it globally minimizes the full quantity `R(w)^(1/3)G(w)^(-1/6)` among all feasible weights; (3.3) is the precise optimization statement used below.

## 4. Dense permutation-symmetric spiked block

Let

`u=6^(-1/2)(1,...,1)^T`,

`M_(L,s)=s I_6 +(L-s)u u^T`, with `L>s>0`.                   (4.1)

Its singular values are

`L,s,s,s,s,s`.

Simultaneous coordinate-permutation symmetry makes the canonical row and column inclusion marginals uniform. Their sums are three, so

`alpha_i=beta_j=1/2`.                                         (4.2)

The third squared singular volume is

`Z=E3(M)=10 s^4(L^2+s^2).`                                   (4.3)

Therefore (3.1) gives the dimension-free all-product-law estimate

`boxed: ||p_Q||_infinity
 <= 6 [10 s^4(L^2+s^2)]^(-1/6),`                             (4.4)

with a continuous `C_0` density, while retaining arbitrary same-bank curvature and outside terms.

## 5. The newest projection-tail sufficient gate fails on the same block

The current tail theorem uses

`T2=sum_(j>=3) sigma_j(M)^2=4s^2`

and asks for a projection `P` with

`max_i P_ii<=1/2`,
`epsilon=||(I-P)M||op <= sqrt(T2)/15 =2s/15`.                 (5.1)

Any such `P` is proper because `tr P<=3<6`. Choose a unit vector `y` in `ran(I-P)`. Since the least singular value of `M` is `s`,

`epsilon=||M^T(I-P)||op >= ||M^T y|| >=s`.                   (5.2)

Thus

`epsilon/sqrt(T2)>=1/2>1/15`,                                (5.3)

so the cited projection-tail **sufficient certificate cannot apply at any admissible projection** on this family. The exact volume law nonetheless sits at the sharp `q=1` gate by (4.2). This is a complementary certificate, not a contradiction to the tail theorem.

## 6. Fully dense target-valid indefinite matrix and explicit constant

Take `s=2`, `L=8`. Then

`M=2I_6+J_6`,                                                 (6.1)

so every physical cross entry is nonzero. Its row Gram matrix is

`MM^T=4I_6+10J_6`.

For every three-row set the `3x3` Gram matrix has eigenvalues `34,4,4`; hence its determinant is

`544`.

There are twenty row triples, giving

`Z=20*544=10880`.                                             (6.2)

Put `C=J_6/100` and

`A_*=[[C,M],[M,C]].`                                          (6.3)

Every entry of `A_*` is nonzero. Since `C` and `M` are simultaneously diagonal on `span{u}` and `u^perp`, the spectrum is exactly

`boxed: {8.06,-7.94,+2 (multiplicity 5),-2 (multiplicity 5)}.` (6.4)

Thus this is a genuinely non-diagonal indefinite instance satisfying the owner hypothesis with all twelve eigenvalues of modulus at least one.

For every admissible independent cap-one input law, (3.1) gives

`boxed: ||p_(X^T A_* X)||_infinity
 <= 6*10880^(-1/6)
 =1.2746171799329793... ,`                                    (6.5)

with `p in C_0(R)`. Also

`boxed: integral |phi_Q(t)|dt
 <=12 pi*10880^(-1/6)
 =8.008655937233575... .`                                     (6.6)

The generic `3e Z^(-1/6)` relaxation on this same block is

`1.7323843592267656...`,

so retaining the exact marginal products improves that certificate by the exact factor `e/2`.

## 7. Designated partner theorem applied to the same actual matrix

Condition any two original coordinates in the left bank. The retained four-by-six cross block `B` has four physical row triples, each with squared row volume `544`, hence

`E3(B)=4*544=2176=Z/5`.                                       (7.1)

For any probability law on triples of four active rows, the row inclusion marginals sum to three. Therefore at least one marginal is at least `3/4`; no supported minor law can have every row marginal strictly below `3/4`.

The completed account02/B04 theorem `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1` applies to each conditional form, including all induced affine and same-bank terms, and gives the uniform Fourier estimate

`||p_Q||_infinity
 <=6*4^(1/6)*2176^(-1/6)
 =2.0999942250555836... .`                                    (7.2)

Its characteristic-function proof is uniform under the conditioning, so averaging preserves the continuous `C_0` conclusion. This is an equation-level application of the designated partner result to the same matrix, not a bibliography-only citation.

The new full six-row exact-marginal certificate (6.5) improves (7.2) by

`boxed: 20^(1/6)=1.6475489724420658... .`                     (7.3)

The gain comes from using all twenty balanced physical row triples simultaneously instead of conditioning down to the four-row support-defect endpoint.

## 8. What changed and the next missing implication

This run changed mechanism from the preceding Gibbs/soft-hub and E3/E4 interpolation work to **exact scalar factors inside the already-proved joint Fourier compiler**. It proves that the generic `e^3` entropy relaxation can hide a substantial constant and that a dense rank-six cross block may have a perfect q=1 volume certificate even when the newest projection-tail sufficient gate fails for every admissible projection.

The next structural obligation is

`QFORM-EXACT-MARGINAL-VOLUME-OR-COMPOUND-HUB-ROUTING-v1`:

> Starting only from the full three-large-eigenvalue hypothesis, either produce an original-coordinate cross block and minor weight with `alpha_*<=1/2` and target-scale `R(w)^(-2)G(w)` currency, or route quantitative failure into the already-paid fractional-support-defect, compound-hub, ridge, pair-log, aggregate-square, or exact-rank mechanisms without multiplying by arbitrarily small extra singular directions.

The bare three-eigenvalue assumption is not shown here to force such a block. Hence the full conjecture and the full continuity claim remain **OPEN**.

## 9. Integrity/status

No Gaussianity, moments, log-concavity, compactness, connected support, spectral-coordinate independence, or pointwise oscillatory decay was assumed. Numerical decimals above only evaluate exact closed-form expressions; the proof does not rely on Monte Carlo evidence. No scheduler/task state, email/push notification, public-release, paid-model/API, cross-account authentication, or permission mutation was made. Repository transport is not verified learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
