# fleet03/B14 — exact smooth-compact reduction and select-before-localize principle

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T133524Z-fleet03-B14-qform-r11`  
**Assignment:** translations and localization  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_LOCALIZATION_EQUIVALENCE / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source corrections

The owner target is unchanged: for every `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove

`P{X^T A X in I} <= C |I|`

for every bounded interval `I`, with one finite universal `C`, or give a valid counterexample. This is equivalent to an essentially bounded output density. Continuity is a separate requested regularity conclusion.

This report does not rotate the input and retain false independence, does not use the refuted law-uniform pointwise quadratic-phase decay, and does not impose a uniform support diameter, moment bound, fragment count, or connectedness. In particular it respects the live correction `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE` from fleet03/B13: compactness below is per approximant, with no uniform diameter.

The assigned partner result actually consumed is fleet04/B14:

`yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`.

It proves exact equality of the optimal small-ball constant between arbitrary admissible product densities and products of indicators `1_{E_i}` with `|E_i|=1`, and then compact finite unions of intervals, with arbitrary locations and separations. The present report strengthens the localization interface in two directions: an exact cap-preserving `C_c^infinity` reduction, and a selective localization rule that leaves the coordinates responsible for smoothing completely unfragmented.

## 2. Quantitative cap-preserving compact smooth approximation

Let

`D = { f in L^1(R): f>=0, integral f = 1, ||f||_infinity <= 1 }`.

### Lemma 2.1

For every `f in D` and every `epsilon>0`, there is `g in C_c^infinity(R)` such that

`g>=0`, `integral g=1`, `||g||_infinity<=1`, and `||f-g||_1<epsilon`.

### Proof

Choose `R` so that

`d_R := integral_{|x|>R} f(x) dx < epsilon/8`.

Define a bounded probability density by truncating and replacing the missing mass with a unit-height filler interval:

`h_R(x)=f(x) 1_{[-R,R]}(x) + 1_{[R+1,R+1+d_R]}(x)`.

The two displayed pieces have disjoint supports, so `0<=h_R<=1` and `integral h_R=1`. On the tail, the original removed mass is `d_R` and the added filler mass is also `d_R`; hence

`||h_R-f||_1 <= 2 d_R < epsilon/4`.                           (2.1)

Let `rho_eta` be a nonnegative `C_c^infinity` probability mollifier. Then

`g_eta=h_R*rho_eta`

is nonnegative, compactly supported, smooth, and has integral one. Because convolution with a probability kernel is an average,

`||g_eta||_infinity <= ||h_R||_infinity <=1`.                 (2.2)

The approximate-identity theorem in `L^1` gives `||g_eta-h_R||_1 ->0`; choose `eta` so it is below `3 epsilon/4`. Combining with (2.1) gives the claim. QED.

Nothing in this construction bounds `R`, moments, support diameter, or derivatives uniformly in `f`. Translation is harmless: translating both `f` and `g_eta` preserves every displayed norm and cap.

## 3. Product and pushforward total-variation control

### Lemma 3.1

For probability measures `mu_i,nu_i`,

`d_TV( tensor_i mu_i, tensor_i nu_i ) <= sum_i d_TV(mu_i,nu_i)`. (3.1)

For any measurable map `F`,

`d_TV(F_# mu,F_# nu) <= d_TV(mu,nu)`.                         (3.2)

If the measures have densities `f_i,g_i`, then

`d_TV(mu_i,nu_i)=(1/2)||f_i-g_i||_1`.                        (3.3)

### Proof

(3.1) follows by telescoping the product measure one marginal at a time and using that tensoring with a probability measure preserves the total-variation norm of a signed measure. (3.2) is immediate by taking the supremum only over inverse images `F^{-1}(B)`. Equation (3.3) is the standard density formula. QED.

Therefore, for the quadratic map `Q_A(x)=x^T A x`, if `X_i` and `Y_i` have marginal densities `f_i,g_i`, then

`sup_B |P{Q_A(X) in B}-P{Q_A(Y) in B}|`

`    <= (1/2) sum_i ||f_i-g_i||_1`.                           (3.4)

This is a dimension-explicit approximation inequality, valid for every symmetric `A`, every sign pattern, and every Borel set `B`.

## 4. Exact equality of the optimal bounded-density constant on smooth compact inputs

Let `C_all` be the best constant in the owner's small-ball inequality over the full class `D` in every coordinate, over all dimensions and all target matrices. Let `C_frag` be the same best constant when every marginal is the indicator of a compact finite union of intervals of total length one. Let `C_sm` be the same best constant when every marginal lies in `D cap C_c^infinity`.

### Theorem 4.1

`C_all = C_frag = C_sm`                                            (4.1)

with the convention that all may be `+infinity`.

### Proof

The partner theorem fleet04/B14 gives

`C_all=C_frag`.                                                   (4.2)

Fix one finite-fragment product law and one interval `I`. Mollify each indicator marginal as in Lemma 2.1; because each fragment set is already compact, no filler is needed, and the mollified marginals remain in `D cap C_c^infinity`. By (3.4), the output laws converge in total variation. Hence, if `C_sm<infinity`,

`P_frag{Q in I} = lim_m P_sm,m{Q in I} <= C_sm |I|`.

Thus `C_frag<=C_sm`. Conversely `D cap C_c^infinity` is a subclass of `D`, so `C_sm<=C_all`. Together with (4.2), this proves (4.1). QED.

### Corollary 4.2 — counterexample transfer

If a proposed finite constant `C` fails for some admissible product law, matrix `A`, and interval `I`, then it fails for a product of compactly supported smooth densities still satisfying the exact cap `<=1`, with the same `A` and `I`.

Indeed, if

`P{Q in I} - C|I| = gamma >0`,

choose smooth approximants whose product/output total-variation error is below `gamma/2`; then the smooth law still has probability greater than `C|I|`. Therefore any genuine failure of the universal conjecture can be witnessed on smooth compact product laws. Unbounded support and roughness are not essential to a counterexample, although the required support radii and derivative norms may diverge along a counterexample sequence.

This is an exact reduction, not permission to use estimates with constants depending on support diameter, moments, derivative norms, or smoothness seminorms.

## 5. Select-before-localize: do not fragment the coordinates that provide smoothing

The full component-box decomposition from the preceding B14 run scaled every coordinate and exposed a `D A D` weighted-congruence debt. That debt is real for that decomposition, but it is **not intrinsic** when a proof uses a fixed original-coordinate active block.

Let `S subset {1,...,n}` be an active coordinate set, chosen from `A` before any localization of the input laws. Keep the active densities `f_i`, `i in S`, fixed.

### Theorem 5.1 — selective extreme-product localization

For fixed `A`, interval `I`, and active marginal densities `(f_i)_{i in S}`,

`sup_{(f_j)_{j notin S} in D} P{Q_A(X) in I}`

is unchanged if every outside marginal `j notin S` is restricted to an indicator `1_{E_j}` of a measurable set of measure one; it is also unchanged if those outside sets are further restricted to compact finite unions of intervals of measure one.

### Proof

Use exactly the one-coordinate bathtub argument proved by fleet04/B14, but iterate it only over `j notin S`. At the step for coordinate `j`, every other marginal, including every active marginal, is held fixed, and the conditional success function still takes values in `[0,1]`; therefore replacing `f_j` by `1_{E_j}` cannot reduce the small-ball probability. Iterating only outside `S` proves the measurable-set reduction. Approximate only those outside sets by compact finite unions and use (3.1)-(3.2) to pass to the limit while leaving the active marginals untouched. QED.

### Theorem 5.2 — deterministic-outside kernel criterion

Suppose that for some `K` and every deterministic outside vector `z in R^{S^c}`, every product law on the active coordinates with marginal densities bounded by one, and every bounded interval `I`,

`P{ Q_A(X_S,z) in I | X_{S^c}=z } <= K |I|`.                 (5.1)

Then the full product law satisfies

`P{Q_A(X) in I} <= K |I|`                                     (5.2)

for arbitrary admissible outside laws, with no moment/support assumptions.

### Proof

Integrate (5.1) against the outside product probability measure. QED.

The point is structural: under (5.1), there is no reason to condition on fragment labels in the active coordinates. Their Hessian remains the original physical block `A_{S,S}`; no diagonal scaling `D_S A_{S,S} D_S` appears. Distant fragments and arbitrary translations in the active marginals are handled directly by the density cap in (5.1).

## 6. Exact partial-fragment formula and removal of the artificial scale debt

On the partner's finite-fragment class, decompose only outside coordinates `j notin S`:

`E_j = disjoint_union_alpha I_{j,alpha}`,

with component lengths `ell_{j,alpha}` summing to one. Let `k` select one outside component in each such coordinate and let

`w_k = product_{j notin S} ell_{j,k_j}`.

Conditioning on the outside component labels gives

`P{Q in I} = sum_k w_k P{ q_k(X_S,Z_k) in I }`,              (6.1)

where the active variables keep their original full densities `1_{E_i}`, `i in S`, and **the active quadratic block remains exactly `A_{S,S}`**. The centers and lengths of the outside fragments can change affine/self terms and the outside conditional law, but they do not scale the active block.

If every term in (6.1) is bounded by `K|I|` using a bound uniform in the induced affine/outside parameters, then

`P{Q in I} <= sum_k w_k K|I| = K|I|`.                         (6.2)

Thus the earlier weighted-congruence problem is avoidable whenever the smoothing block is selected from `A` before localization and its estimate is uniform under arbitrary outside-induced affine terms.

This is the exact localization mechanism needed for original-coordinate block proofs.

## 7. Application 1: the definite physical-pair branch

Take `S={i,j}` and suppose the physical principal block `B=A_{S,S}` has `det B=Delta>0`. The previous B14 run proved, uniformly in every outside vector and every induced linear term,

`P{Q_A(X_S,z) in I | z} <= pi |I|/sqrt(Delta)`.              (7.1)

Applying Theorem 5.2 gives

`||p_Q||_infinity <= pi/sqrt(Delta)`                          (7.2)

for the complete arbitrary-law problem in this matrix branch. Formula (6.1) explains exactly why no fragment-size factors ever need to be paid: the two smoothing coordinates are never fragmented in the proof.

## 8. Application 2: the live regularized original-coordinate cross-block theorem

The completed interactive report

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`

proves the following source-exact conditional estimate. For disjoint original-coordinate sets `I,J`, let `B=A[I,J]`, put `S=I union J`, and let `1<=q<2`. If the coordinate leverage of `range(B)` on the chosen side is at most `q/2`, then after conditioning on **all coordinates outside `S`**, the induced self phases and linear terms are arbitrary but the same bound holds uniformly in the outside value `z`:

`|phi_z(t)| <= det(I + 2q t^2 B B^T/(pi^2 e^2))^(-1/(4q)).`  (8.1)

For `q=2` the leverage assumption is unnecessary and the corresponding exponent is `-1/8` with coefficient `4/(pi^2 e^2)`.

This is precisely the hypothesis of the select-before-localize principle: the active cross block `B` is chosen from the original `A`, and outside fragment locations enter only through self/linear phases that the source theorem already treats uniformly. Therefore arbitrary outside translations, distant fragments, and unbounded supports do not alter `B` or its singular values.

If `B` has `r>2q` singular values at least `sigma`, the source theorem gives, and selective localization preserves without any extra factor,

`||p_Q||_infinity <= e r / (sqrt(2q) sigma (r-2q)).`          (8.2)

The analytic estimate (8.1)-(8.2) is the cited peer result, not newly re-proved here. The new inference is that full finite-fragment conditioning is unnecessary: **the active block can remain unscaled throughout localization**, so the `DAD` scale loss from the all-coordinate box decomposition is not a barrier for this whole original-coordinate cross-block pathway.

## 9. Application to the determinant-weighted localized branch

Fleet02/B07 proved a determinant-weighted dichotomy: either a disjoint-basis smoothing parameter is large enough to bound the density directly, or one large spectral direction has more than half its energy on one physical coordinate triple. Its first unpaid implication is to combine that localized triple with the remaining two large directions.

For that branch, Theorem 5.1 says the selected physical triple may be kept entirely active and unfragmented while only its complement is reduced to finite fragments. Therefore the next hybrid proof does **not** need to survive diagonal rescaling of the three localized coordinates. The remaining difficulty is genuinely spectral/coupling geometry, not support location or fragment scale on that active triple.

This does not solve the B07 hybrid implication; it removes one localization debt from it.

## 10. Continuity is not transferred by this reduction alone

Theorem 4.1 exactly transfers the `L^infinity` small-ball target, but it does not by itself transfer continuity of the output density. Continuous bounded densities can converge in `L^1` to a bounded discontinuous density. Therefore the owner's continuous-density request remains separate.

A sufficient transfer principle would be a universal modulus of continuity on the smooth compact subclass: if every smooth-input output density obeyed

`|p(y)-p(y')| <= omega(|y-y'|)` with `omega(r)->0`

using the same `omega` for the full target family, then local Arzela-Ascoli plus the total-variation convergence above would yield a continuous density for every rough input. No such universal modulus is proved here.

## 11. What is paid and what remains

**Proved in this run:**

1. every admissible marginal can be approximated in `L^1` by `C_c^infinity` probability densities with the exact same density cap `<=1`, with no moments or bounded-diameter assumption;
2. product/output total variation is controlled by one half of the sum of marginal `L^1` errors;
3. the optimal full QFORM small-ball constant is exactly unchanged when one restricts to compactly supported smooth marginals;
4. any genuine target counterexample transfers to smooth compact product laws with the same matrix and violating interval;
5. the partner fleet04/B14 bathtub/localization theorem admits an exact **selective** version: only inactive coordinates need be extremized/localized;
6. for any fixed active block with a deterministic-outside affine bound, arbitrary shifts/fragments/tails on all coordinates incur zero additional constant;
7. consequently the all-coordinate `DAD` weighted-congruence debt is not intrinsic to definite-pair or original-coordinate cross-block mechanisms.

**Not proved:** the unrestricted three-large-eigenvalue density theorem. In particular no argument here proves that every target matrix contains a physical definite pair or a cross block satisfying the regularized determinant hypotheses.

**Next target-relevant implication:** combine the select-before-localize principle with the heavy/localized matrix branch: select an original-coordinate active set from `A` whose conditional affine quadratic admits a dimension-free bound, without fragmenting that set. Fleet02/B07's localized triple is a concrete current test case. The support/translation problem is now separated from the remaining spectral/coupling problem.

**Suggested recipients:** assigned partner `fleet04/B14` (localization integration), `fleet02/B07` (localized-triple hybrid), and a B19 proof-assembly worker.

No numerical histogram or unsupported extremality claim is used in this report.
