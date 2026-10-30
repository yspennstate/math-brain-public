SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-22T23:17:17Z.
attacking: exact rough-input/affine transfer for the ruled rank-three side, plus a no-tax outside-conditioning lift of the partner's top-two-cross theorem.

# fleet01/B14 r23 — rough ruled-side localization and outside-lifted cross compilers

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T231717Z-fleet01-B14-QFORM-r23`  
**Assignment:** Translations and localization  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `SUPPORTING TARGET-LEVEL THEOREMS PROVED / FULL QFORM OPEN`.

## 1. Exact target and correction boundary

The target remains: for independent real original coordinates with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite `C` such that

`P(X^T A X in J) <= C |J|`

for every interval `J`, or produce a valid counterexample.

No moment, centering, compact-support, connected-support, log-concavity, identical-law, or post-rotation-independence assumption is made below. I do not use the false law-uniform pointwise quadratic Fourier decay, the false arbitrary-joint rank-three coarea lemma, the false positive conditional-fibre moment gate, a bounded-diameter/fixed-fragment reduction, or a universal well-conditioned physical minor.

This run changes mechanism from the preceding B14 reciprocal/log-star work: it makes the newest ruled-hyperboloid result rigorous for rough cap-one product inputs and then lifts the assigned partner's cross theorem through completely arbitrary outside couplings.

## 2. Source-pinned inputs actually applied

### 2.1 Newest owner-required mathematical source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

contains Theorem C. If

`q(Y)=lambda_1 Y_1^2 + lambda_2 Y_2^2 - mu Y_3^2`,

where `Y=(<r_1,X>,<r_2,X>,<r_3,X>)`, `r_1,r_2,r_3` are orthonormal, and `lambda_1,lambda_2,mu>=1`, then on the one-sheet side `s>=0`

`p_q(s) <= (lambda_1 lambda_2 mu)^(-1/2)
             integral_0^{2pi} [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta
          <= pi sqrt(2).`                                                (2.1)

The current owner continuation explicitly asks B14 to retain rough laws, arbitrary translations, unbounded/fragmented supports, and conditioning-generated affine terms. The source also warns that the ruled result does **not** cover the two-sheet side.

The same source directory's `FOURIER_ROUTE_REPORT.md` proves the unrestricted fifth-volume cross estimate

`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10),
 Z_5=e_5(C^T C),`                                                        (2.2)

for any original-coordinate cross block `C=A_IJ`, with no volume-marginal condition and arbitrary self blocks/affine terms.

### 2.2 Assigned partner fleet02/B14

The latest completed assigned-partner result used here is

`yspennstate/math-open-problems@2ca523ac73b814a97e846de8d37a932c127eecfb`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T220604Z-fleet02-B14-QFORM-r21/REPORT.md`.

Its theorem `QFORM-TOP-d-CROSS-AVERAGING-v1` says that, for genuinely independent original-coordinate blocks `U,V`,

`Q=2 U^T C V + R(V) + ell_U^T U + ell_V^T V + c`,                       (2.3)

with **no U-self quadratic term**, arbitrary measurable `R(V)`, arbitrary affine shifts, and cross singular values `s_1>=s_2>=...`,

`||p_Q||_infinity <= e sqrt(pi) / sqrt(s_1(C)s_2(C))`                    (2.4)

whenever `s_2(C)>0`. The theorem is uniform over arbitrary translations, distant fragments and unbounded supports. Its proof averages the reciprocal linear coefficient using a translation-uniform rank-two linear-image negative moment; it does not assume independence after rotation.

## 3. Exact rough-input transfer lemma

### Theorem 3.1 — `QFORM-SMOOTH-PRODUCT-TRANSFER-v1`

Let `F:R^n->R` be any Borel map. Suppose that for **every** independent input with smooth probability densities `g_i<=1`,

`P(F(X) in J) <= C |J|`                                                  (3.1)

for all intervals `J` in a prescribed Borel output region `Omega`, with one constant `C` independent of the smooth laws. Then exactly the same interval inequality holds for every independent input with arbitrary probability densities `f_i<=1`. There is no loss in `C` and no support or moment hypothesis.

#### Proof

Fix a nonnegative smooth probability mollifier `eta_epsilon`. Put

`f_i^(epsilon)=f_i * eta_epsilon`.

Then

`0<=f_i^(epsilon)<=||f_i||_infinity ||eta_epsilon||_1<=1`,
`int f_i^(epsilon)=1`, and `||f_i^(epsilon)-f_i||_1 ->0`.                 (3.2)

For the product densities, telescoping gives

`|| product_i f_i^(epsilon) - product_i f_i ||_1
 <= sum_i ||f_i^(epsilon)-f_i||_1 ->0`,                                  (3.3)

because every untouched marginal has `L^1` norm one. Pushforward by the measurable map `F` contracts total variation, hence for every interval `J`

`|P_epsilon(F in J)-P(F in J)| ->0`.                                     (3.4)

Apply (3.1) and pass to the limit. QED.

This is deliberately not a compactness or coefficient-perturbation argument. The quadratic map is kept fixed and only the product law is approximated in total variation. Arbitrarily remote support fragments and tails remain allowed.

## 4. Direct audit of the ruled Jacobian for smooth product laws

I record the geometric calculation because it is the exact place where an a.e. marginal-density statement must not be evaluated on a curve without a regularization step.

First take the isotropic signature

`q(y)=y_1^2+y_2^2-y_3^2`.

For `s>0`, write

`e_theta=(cos theta,sin theta,0)`,
`e_theta^perp=(-sin theta,cos theta,0)`,
`e_3=(0,0,1)`

and parametrize the one-sheet level set by

`y(s,theta,t)=sqrt(s)e_theta+t(e_theta^perp+e_3)`.                        (4.1)

Indeed `q(y)=s`. In the moving orthonormal basis `(e_theta,e_theta^perp,e_3)`,

`partial_s y=(1/(2sqrt(s)),0,0)`,
`partial_theta y=(-t,sqrt(s),0)`,
`partial_t y=(0,1,1)`,

so

`|det(partial_s y,partial_theta y,partial_t y)|=1/2`.                     (4.2)

If `rho` is the smooth density of `Y=(<r_1,X>,<r_2,X>,<r_3,X>)`, then for `0<a<b`

`P(a<=q(Y)<=b)
 = int_a^b (1/2) int_0^{2pi} int_R rho(y(s,theta,t)) dt dtheta ds`.       (4.3)

The ruling vector `w_theta=e_theta^perp+e_3` has length `sqrt(2)`. The arclength integral of `rho` along that line is the density of the orthogonal two-dimensional projection onto `w_theta^perp`. For a product source, the two-dimensional projection density is bounded by `2` (the product-projection theorem used in Theorem C). Therefore

`int_R rho(y_0+t w_theta) dt <= 2/|w_theta|=sqrt(2)`,                     (4.4)

and (4.3) gives

`P(a<=q(Y)<=b) <= pi sqrt(2) (b-a)`.                                     (4.5)

Why is the pointwise use in (4.4) legitimate after smoothing? For any rank-two linear projection `T X`, choose two original coordinates whose coefficient columns form an invertible `2x2` matrix. Conditional on all other original coordinates, the projected density is an affine translate of a product of two continuous densities divided by the determinant; averaging and dominated convergence make that projected density continuous. Its essential cap `<=2` therefore holds pointwise. The same argument gives a continuous three-dimensional projection density for the rank-three map used in (4.3).

For anisotropic coefficients, scale the same ruling. The line direction becomes

`w_theta=(-sin(theta)/sqrt(lambda_1),
          cos(theta)/sqrt(lambda_2),
          1/sqrt(mu))`,                                                  (4.6)

and the Jacobian gains `(lambda_1 lambda_2 mu)^(-1/2)`. This reproduces the exact first bound in (2.1). If `lambda_1,lambda_2,mu>=sigma`, write them as `sigma a,sigma b,sigma c` with `a,b,c>=1`; then the integrand after simplification is

`1/[sigma sqrt(bc sin^2(theta)+ac cos^2(theta)+ab)] <= 1/(sigma sqrt(2))`.

Hence

`P(q(Y) in J) <= (pi sqrt(2)/sigma)|J|`                                   (4.7)

for every interval `J subset [0,infinity)` and every **smooth** cap-one product law. Theorem 3.1 now transfers (4.7) with the identical constant to arbitrary cap-one product laws. This supplies the rough-input bridge requested by the newest owner continuation without evaluating an a.e. density representative on a prescribed ruling.

## 5. Affine translation theorem on the ruled side

### Theorem 5.1 — `QFORM-RULED-RANGE-AFFINE-ROUGH-v1`

Let `A` be symmetric of exact rank three with signature `(2,1)`, its three nonzero eigenvalue magnitudes at least `sigma>0`, and let `b in Range(A)`. For arbitrary independent cap-one inputs and

`Q=X^T A X+b^T X+c`,                                                     (5.1)

set

`h=(1/2)A^dagger b`,
`tau=c-(1/4)b^T A^dagger b`.                                             (5.2)

Then for every interval `J subset [tau,infinity)`,

`boxed: P(Q in J) <= (pi sqrt(2)/sigma)|J|.`                              (5.3)

Equivalently, the restriction of the output law to its one-sheet side has density cap `pi sqrt(2)/sigma`. For signature `(1,2)`, the reflected statement holds on `(-infinity,tau]`.

#### Proof

Since `b in Range(A)`, `Ah=b/2`, and

`Q=(X+h)^T A(X+h)+tau`.                                                   (5.4)

The coordinatewise deterministic translation `X -> X+h` preserves independence and every density cap `<=1`, regardless of how far the supports move. Apply (4.7) to the translated product source and shift the output by `tau`. QED.

The hypothesis `b in Range(A)` is essential to this completion identity. A kernel component of `b` is not silently discarded.

### Conditional physical-triple corollary

Let `I` be three **original** coordinates and suppose the physical principal block `B=A_II` is invertible of signature `(2,1)` with all eigenvalue magnitudes at least `sigma`. Let `W=X_{I^c}`. Conditioning on `W=w` gives

`Q=U^T B U + ell(w)^T U+c(w)`,                                           (5.5)

where `U=X_I` remains a product of three cap-one laws. Since `B` is invertible, every `ell(w)` lies in its range. Define

`tau(w)=c(w)-(1/4)ell(w)^T B^{-1}ell(w)`.                                 (5.6)

Then for every fixed interval `J`,

`boxed:
 P(Q in J, Q>=tau(W)) <= (pi sqrt(2)/sigma)|J|.`                           (5.7)

This remains true with arbitrary outside couplings and arbitrarily large conditioning-generated translations. It is intentionally only the one-sheet contribution: the two-sheet event `Q<tau(W)` is the surviving geometric obstruction and is not bounded by this theorem.

## 6. Applying the assigned partner: outside-lifted top-two cross theorem

### Theorem 6.1 — `QFORM-OUTSIDE-LIFTED-TOP2-CROSS-v1`

Partition the original coordinates into disjoint sets `I,J,K`; write `U=X_I`, `V=X_J`, `W=X_K`. Suppose

`A_II=0`,
`C=A_IJ`,
`s_2(C)>0`.                                                              (6.1)

There is **no assumption** on `A_JJ,A_IK,A_JK,A_KK`, and arbitrary deterministic affine terms are allowed. Then

`boxed:
 ||p_(X^T A X+b^T X+c)||_infinity
 <= e sqrt(pi) / sqrt(s_1(C)s_2(C)).`                                    (6.2)

#### Proof — actual partner application

Condition on `W=w`. Original-coordinate independence gives independent cap-one blocks `U,V`. The conditional polynomial is exactly

`Q_w(U,V)
 =2U^T C V + R_w(V)+ell_U(w)^T U+ell_V(w)^T V+c(w)`,                     (6.3)

with

`R_w(V)=V^T A_JJ V`

and with the arbitrary outside couplings absorbed only into the affine shifts

`ell_U(w)=b_I+2A_IK w`,
`ell_V(w)=b_J+2A_JK w`.                                                   (6.4)

Equation (6.3) is precisely the hypothesis of fleet02/B14's theorem (2.3)-(2.4), with the **same** cross matrix `C` for every `w`. Therefore for every interval `J_0`,

`P(Q in J_0 | W=w)
 <= [e sqrt(pi)/sqrt(s_1(C)s_2(C))] |J_0|`                               (6.5)

for almost every `w`. Integrating (6.5) proves (6.2). QED.

This is the required application of the named partner result to an actual new inequality. The conclusion is uniform over arbitrary outside dimension, arbitrary outside quadratic curvature, arbitrary outside couplings, arbitrary support translations and fragments, and unbounded laws; no conditional density cap is assumed.

### Genuine target-class family

Take any cross matrix `C` with `s_1(C),s_2(C)>=1` and the physical principal block

`B=[[0,C],[C^T,0]]`.                                                      (6.6)

Its eigenvalues include `+s_1,+s_2,-s_1,-s_2`, so it already has four eigenvalues of modulus at least one. Adjoin arbitrarily many outside coordinates with **arbitrary** symmetric outside block and **arbitrary** cross couplings to this principal block. Cauchy interlacing preserves at least two eigenvalues `>=1` and two `<=-1` in the full matrix. Thus every such extension lies in the original QFORM target class, while (6.2) gives

`boxed: ||p_Q||_infinity <= e sqrt(pi) <4.819.`                           (6.7)

This demonstrates that arbitrary outside couplings and conditioning-generated affine translations cost exactly zero once a legitimate two-direction zero-self cross smoother is exposed.

## 7. Applying the newest Claude D5 theorem through outside conditioning

For completeness, the same no-tax localization principle gives a second branch that does **not** require `A_II=0`. For any disjoint original-coordinate `I,J,K`, put `C=A_IJ` and

`Z_5=e_5(C^T C)`.                                                        (7.1)

If `Z_5>0`, condition on `X_K`. All outside couplings become affine terms while `C`, `A_II`, and `A_JJ` stay fixed. Apply the newest-source D5 theorem (2.2) conditionally and average:

`boxed:
 ||p_(X^TAX+b^TX+c)||_infinity
 <=5 sqrt(2e) Z_5^(-1/10).`                                             (7.2)

No row-marginal hypothesis, support condition, or moment condition appears. Combining (6.2) and (7.2) on their common scope gives the explicit translation/localization compiler

`||p_Q||_infinity <= min{
 e sqrt(pi)[s_1(C)s_2(C)]^(-1/2),
 5 sqrt(2e) e_5(C^TC)^(-1/10)
}`                                                                       (7.3)

whenever `A_II=0` and `rank C>=5`; each branch separately remains valid on its own stated hypotheses.

## 8. What this pays and what remains unpaid

The run establishes three exact interfaces:

1. rough arbitrary cap-one product laws may be replaced by smooth cap-one product laws for a **uniform interval inequality** with zero loss, by total-variation product approximation;
2. the newest ruled one-sheet theorem therefore survives arbitrary rough/fragmented/unbounded laws and all range-affine translations with the same `pi sqrt(2)/sigma` constant;
3. the partner top-two cross theorem and the newest D5 theorem survive arbitrary outside couplings by conditioning on outside **original coordinates**, with exactly the same constants.

These remove localization and conditioning-generated translations from the stated branches. They do **not** prove the full conjecture.

The first unpaid implication is structural/geometric: under only `s_3(A)>=1`, route every remaining matrix either to a paid cross/ridge/diffuse/grouped branch or control the **two-sheet** contribution of an indefinite localized triple (and the convex side in the exact-rank-three geometry) while retaining product provenance. The correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` shows that a bare arbitrary-joint X-ray bound is insufficient; any repair must use the product source more deeply or combine the two-sheet term with another independent smoothing mechanism.

## 9. Integrity/status

- Full QFORM: `OPEN`.
- New theorem: `QFORM-SMOOTH-PRODUCT-TRANSFER-v1`.
- New theorem: `QFORM-RULED-RANGE-AFFINE-ROUGH-v1` and moving-critical-value physical-triple corollary.
- New theorem: `QFORM-OUTSIDE-LIFTED-TOP2-CROSS-v1`, directly applying fleet02/B14.
- New conditional lift: D5 with arbitrary outside variables, applying the newest Claude source.
- No claim of universal `C=pi`; no claim that one-sheet control pays the two-sheet side; no claim that the bare spectral hypothesis exposes the required cross block.
- Repository transport is not native memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.
