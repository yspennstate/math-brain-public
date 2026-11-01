# fleet02/B14 — acyclic fragment packing and the cyclic-anchor obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T140126Z-b14-qform-localization-r13`  
**Assignment:** Translations and localization  
**Status:** `SUPPORTING_LOCALIZATION_LEMMA / SCOPE_CORRECTION / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid localization implication

The target remains: for every dimension `n`, every independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove

`P{X^T A X in J} <= C |J|`

for all bounded intervals `J`, with one finite universal `C`, or give a valid counterexample.

The current exact localization state already removes arbitrary tails and absolute translations without moments. In particular, fleet03/B14, canonical proof

`yspennstate/math-open-problems@2208c3f666582999f1fbc7e55921a4530cbe2789`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T133524Z-fleet03-B14-qform-r11/REPORT.md`

proves cap-preserving compact-smooth reduction and, using fleet04/B14's finite-fragment extremal reduction, a **select-before-localize** theorem: an original-coordinate active set can be kept completely unfragmented while only the complement is localized; any deterministic-outside active estimate uniform in the outside-induced affine terms transfers with exactly the same constant.

The first unpaid implication for the more aggressive fragment/coarea route is therefore precise:

> If a local shell estimate is proved after fragmenting several coordinates, under what hypotheses can the fragment singularities be summed without a support, moment, separation, or fragment-count loss?

The previous B14 run proved the one-coordinate subcritical packing bound for a fixed anchor. The present run gives the correct multi-coordinate compiler and shows that **individual subcriticality is not enough when the anchors depend cyclically on other fragment labels**.

The live corrections are respected throughout: no law-uniform pointwise Fresnel decay, no independence after rotation, no naive fiber supremum, no bounded-diameter localization, no conditional-cap surrogate for genuine independence, and no absolute phase-Wiener interface.

## 2. One-coordinate packing, reproved

Let

`E = disjoint_union_alpha I_alpha`, `|E|=sum_alpha ell_alpha=1`,

where the `I_alpha` are bounded intervals and `ell_alpha=|I_alpha|`. For an anchor `a in R`, define

`r_alpha(a)=dist(a,I_alpha)+ell_alpha`.

For `0<=theta<1`,

`sum_alpha ell_alpha r_alpha(a)^(-theta) <= 2^theta/(1-theta)`.      (2.1)

Indeed, for every `x in I_alpha`,

`|x-a| <= dist(a,I_alpha)+ell_alpha = r_alpha(a)`,

so

`ell_alpha r_alpha(a)^(-theta) <= integral_{I_alpha}|x-a|^(-theta) dx`.

Summing over `alpha`,

`sum_alpha ell_alpha r_alpha(a)^(-theta) <= integral_E |x-a|^(-theta) dx`.

Among measurable sets of measure one, the integral of the symmetric decreasing kernel `|x-a|^(-theta)` is maximized by the unit interval centered at `a`. Hence

`integral_E |x-a|^(-theta) dx <= integral_{-1/2}^{1/2}|u|^(-theta)du = 2^theta/(1-theta)`.

The constant is uniform in `a`; therefore arbitrary absolute translation of both the fragments and the anchor costs nothing.

## 3. New theorem: acyclic/triangular fragment-packing compiler

For `i=1,...,m`, let

`E_i = disjoint_union_{alpha_i} I_{i,alpha_i}`, `sum_{alpha_i} ell_{i,alpha_i}=1`,

and put

`r_{i,alpha_i}(a)=dist(a,I_{i,alpha_i})+ell_{i,alpha_i}`.

Choose exponents `0<=theta_i<1`. Let `W(alpha_1,...,alpha_m)>=0` be any array satisfying

`W(alpha_1,...,alpha_m)`

` <= K prod_{i=1}^m [ ell_{i,alpha_i} r_{i,alpha_i}( a_i(alpha_{i+1},...,alpha_m) )^(-theta_i) ]`,   (3.1)

where the anchor in coordinate `i` may depend arbitrarily on **later** component labels but not on `alpha_i` or any earlier label.

Then

`sum_{alpha_1,...,alpha_m} W(alpha_1,...,alpha_m)`

` <= K prod_{i=1}^m 2^(theta_i)/(1-theta_i)`.                    (3.2)

### Proof

Fix all labels `alpha_2,...,alpha_m`. Every factor with index `j>=2` is independent of `alpha_1`, while `a_1` is just a fixed real number during the `alpha_1` sum. By (2.1),

`sum_{alpha_1} ell_{1,alpha_1} r_{1,alpha_1}(a_1)^(-theta_1)`

` <= 2^(theta_1)/(1-theta_1)`.

Remove that coordinate and repeat with `alpha_2`, then `alpha_3`, and so on. This gives (3.2). QED.

The proof is pointwise in every later parameter. Consequently each `a_i` may also be an arbitrary measurable function of later **continuous variables**, not only of later component labels. No size, derivative, moment, or support bound on the anchors is needed. This is exactly the dependence produced by a sequential completion-of-squares or a sequential coarea elimination when the current stationary center is allowed to depend on variables that have not yet been eliminated.

### Explicit square-root corollary

If at most three localized coordinates carry square-root singularities, `theta_i=1/2`, and their centers are triangular in the sense above, then the entire fragmentation cost is at most

`(2^(1/2)/(1-1/2))^3 = (2 sqrt(2))^3 = 16 sqrt(2) < 22.63`.       (3.3)

For two such coordinates the multiplier is exactly `8`. The constants are independent of fragment count, positions, separation, and support diameter.

Thus a future source-valid local shell estimate of the form (3.1) with at most three square-root losses and an acyclic elimination order transfers to arbitrary finite-fragment extreme laws with a universal explicit multiplier. By the already-proved exact extremal/compactification reductions, that then transfers to the original arbitrary-density target.

## 4. New obstruction: cyclic anchor dependence has a sharp critical threshold

The triangular hypothesis above is not a proof artifact. Individual inequalities `theta_i<1` do **not** suffice for arbitrary component-dependent anchors.

For `N>=2`, define the measure-one finite-fragment set

`E_N = union_{k=1}^N I_k`,

`I_k=[2(k-1)/N,(2k-1)/N]`,

so every fragment has length `ell_k=1/N`. Let `c_k` be the midpoint of `I_k`:

`c_k=(4k-3)/(2N)`.

Create a two-coordinate cyclic anchor rule

`a_1(l)=c_l`, `a_2(k)=c_k`.

For `d=|k-l|`, direct geometry gives

`r_k(c_l)=r_l(c_k)=1/N` if `d=0`,

and

`r_k(c_l)=r_l(c_k)=(4d+1)/(2N)` if `d>=1`.                    (4.1)

Let `Theta=theta_1+theta_2`. The cyclic packing sum is therefore exactly

`S_N(Theta)`

` = sum_{k,l} N^(-2) r_k(c_l)^(-theta_1) r_l(c_k)^(-theta_2)`

` = N^(Theta-1)`

`   + 2^(Theta+1) N^(Theta-2) sum_{d=1}^{N-1}(N-d)(4d+1)^(-Theta)`.   (4.2)

Three regimes follow.

### 4.1 Supercritical cycle: `Theta>1`

The diagonal terms alone give

`S_N(Theta) >= N^(Theta-1) -> infinity`.                        (4.3)

Thus two individually subcritical exponents can still produce a power divergence when their sum around a two-cycle exceeds one.

### 4.2 Critical cycle: `Theta=1`

For `1<=d<=N/2`, `(N-d)/N>=1/2` and `4d+1<=5d`. From (4.2),

`S_N(1) >= 1 + sum_{d=1}^{floor(N/2)} 2/(4d+1)`

`        >= 1 + (2/5) sum_{d=1}^{floor(N/2)} 1/d`.              (4.4)

Hence

`S_N(1) >= (2/5) log(N/2)+1`,

up to the standard positive harmonic-number remainder. The loss is genuinely logarithmic at the cycle threshold.

### 4.3 Subcritical cycle: `Theta<1`

Using `4d+1>=4d` and `sum_{d<=N}d^(-Theta) <= 1+N^(1-Theta)/(1-Theta)`, (4.2) gives a bound independent of `N`:

`S_N(Theta)`

` <= 1 + 2^(1-Theta) [1 + 1/(1-Theta)]`.                       (4.5)

So this explicit family has the sharp threshold `Theta=1`.

## 5. Correction to the scope of the previous B14 packing statement

The previous run's one-coordinate estimate is correct. Its product-factorization consequence is correct for fixed anchors and, more generally, for the acyclic/triangular dependence of Theorem 3. The present construction shows that it must **not** be read as allowing arbitrary mutually component-dependent anchors merely because every individual exponent is below one.

Accordingly the safe localization interface is:

- fixed anchors: product factorization is valid;
- triangular/acyclic anchors: Theorem 3 is valid with the same product constants;
- cyclic anchors: one must inspect the sum of exponents around the cycle or prove additional cancellation/aggregation; individual subcriticality alone is insufficient.

This is a mechanism-level correction, not a QFORM counterexample.

## 6. Application of the completed partner result

The fleet03/B14 select-before-localize theorem is now seen to do more than avoid the earlier diagonal-congruence scale debt. It also avoids cyclic fragment-center debts in the active smoothing block entirely.

For its live applications — the definite physical pair and the regularized original-coordinate cross-block theorem — the active coordinates remain unfragmented. Outside component labels only generate self/affine parameters in an estimate already uniform in those parameters. In the language of Theorem 3, all outside localization exponents are `theta=0`, so the multiplier is exactly one. Therefore arbitrary outside translations, distant fragments, and unbounded supports are transferred **with no localization loss**, exactly as the partner report claims.

For the localized-triple/heavy branch, the present theorem gives a concrete acceptance condition for any attempt that does fragment active coordinates: arrange the local shell proof in a genuine elimination order so that each current center depends only on later variables and keep every resulting exponent strictly below one. If two or more fragment centers depend cyclically, the new example shows that a nominally subcritical coordinatewise ledger can still acquire a logarithmic or power loss.

## 7. What remains

The full conjecture is not proved. The first B14-localization implication is now narrower:

> Produce a source-valid local shell/coarea estimate for the heavy/localized active block whose fragment singularities admit an acyclic elimination order of the form (3.1), or keep that active block unfragmented via the partner's select-before-localize theorem. A proof that assigns mutually dependent fragment centers must pay the cycle threshold explicitly; `theta_i<1` coordinatewise is not enough.

This is a genuine restriction on admissible localization arguments and an explicit dimension-free compiler when the restriction is met. It does not impose moments, bounded support, connected support, rotation-independence, or a fixed fragment count.

## 8. Source pins

- owner programme/control: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`;
- source-control snapshot used before scientific write: `yspennstate/math-research-brain@f131875d619a0186efc7e7aa942257f5247ac01a`;
- completed partner applied: fleet03/B14, `yspennstate/math-open-problems@2208c3f666582999f1fbc7e55921a4530cbe2789`, path above;
- prior B14 one-coordinate packing result: `yspennstate/math-open-problems@2e0f363a166b694e6b91a8eb6dc59f1488c5cba8`;
- corrections consumed before write include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`.

No novelty or priority claim is made. Full QFORM remains OPEN.
