# account01/B14 — exact localization plus an SCC/cyclic fragment-packing compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T150938Z-account01-B14-qform-r12`  
**Assignment:** translations and localization  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_THEOREM / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target

For every dimension `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, the full target is to prove one finite universal `C` such that

`P{X^T A X in J} <= C |J|`

for every bounded interval `J`, or give a valid counterexample. No moment, centering, support-diameter, connected-support, sign, or post-rotation independence hypothesis is allowed.

This report proves a localization theorem and a sharp fragment-packing compiler. It does **not** prove the full QFORM conjecture.

## 2. Dependencies actually consumed

The named partner result consumed here is account02/B14:

`yspennstate/math-open-problems@d358b89ba78735cee238c01e83c2c3ca9ec66352`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T140126Z-b14-qform-localization-r13/REPORT.md`.

Its source-exact one-coordinate packing theorem is the following. If

`E = disjoint_union_alpha I_alpha`, `sum_alpha ell_alpha=1`,

`r_alpha(a)=dist(a,I_alpha)+ell_alpha`,

then for every `0<=theta<1` and every real anchor `a`,

`sum_alpha ell_alpha r_alpha(a)^(-theta) <= 2^theta/(1-theta)`.    (2.1)

The same partner report proves an acyclic/triangular multi-coordinate compiler and gives an exact two-coordinate cyclic construction that diverges logarithmically at `theta_1+theta_2=1` and by a power when `theta_1+theta_2>1`.

For compatibility with the existing localization state, I also checked account03/B14:

`yspennstate/math-open-problems@2208c3f666582999f1fbc7e55921a4530cbe2789`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T133524Z-account03-B14-qform-r11/REPORT.md`.

It proves exact cap-preserving compactification and the select-before-localize principle. I reprove below the exact extreme-product localization step needed for this report so the new compiler is self-contained.

Live corrections rechecked before this scientific write include: law-uniform pointwise quadratic Fourier decay is false; naive fiber suprema lose dimension; independence is not preserved after rotation; bounded-diameter localization is false; a conditional density cap is not a surrogate for independence; absolute phase-Wiener control is false; and there is no universal fixed fragment-count bathtub reduction. None of those refuted mechanisms is used below.

## 3. Exact constant-preserving localization to arbitrary finite fragments

Let

`D={f:R->[0,1] measurable : integral f=1}`.

For a bounded measurable `Phi:R^n->[0,1]`, define

`T(f_1,...,f_n)=integral Phi(x) prod_i f_i(x_i) dx`.

For QFORM we use `Phi(x)=1_{x^T A x in J}`.

### Lemma 3.1 — one-coordinate bathtub with exact cap

For every measurable `g:R->[0,1]`,

`sup_{f in D} integral g f = sup_{E measurable, |E|=1} integral_E g`.   (3.1)

#### Proof

The `>=` direction is immediate because `1_E in D` whenever `|E|=1`.

For the reverse direction, choose a threshold `c` and a measurable set `E` of measure one such that `g>=c` on `E` and `g<=c` on `E^c`, modifying only a subset of the level set `{g=c}` if necessary. Such a quantile set exists; if a superlevel set already has measure at least one, take a unit-measure subset at the threshold, while if all superlevel sets have measure below one, fill from the threshold level. For any `f in D`, since `integral f=|E|=1`,

`integral g(f-1_E)=integral (g-c)(f-1_E)`.

On `E`, `g-c>=0` and `f-1<=0`; on `E^c`, `g-c<=0` and `f>=0`. Hence the integrand has nonpositive sign everywhere and

`integral g f <= integral_E g`.

This proves (3.1). QED.

### Theorem 3.2 — exact product localization

For every bounded measurable `Phi:R^n->[0,1]`,

`sup_{f_1,...,f_n in D} T(f_1,...,f_n)`

` = sup_{|E_1|=...=|E_n|=1} integral_{E_1 x ... x E_n} Phi(x) dx`.   (3.2)

#### Proof

Fix all marginals except the first. The conditional success function

`g_1(x_1)=integral Phi(x) prod_{j>=2} f_j(x_j) dx_2...dx_n`

lies in `[0,1]`. By Lemma 3.1, replace `f_1` by `1_{E_1}` without decreasing `T`. Holding this replacement fixed, do the same to `f_2`, then `f_3`, and so on. After `n` steps every marginal is an indicator of a measure-one set and the objective has not decreased. The reverse inequality is again immediate because every such indicator is admissible. QED.

### Theorem 3.3 — bounded finite unions suffice, with no uniform diameter or fragment-count bound

The right-hand side of (3.2) is unchanged if every `E_i` is required to be a bounded finite union of intervals of total length one.

#### Proof

Every measurable finite-measure set `E` can be approximated in symmetric-difference measure by a bounded finite union of intervals. The approximant can be adjusted to have measure exactly one by adding a disjoint interval of the missing length or trimming excess length from finitely many components. Thus for every `epsilon>0` there is a bounded finite union `F` with `|F|=1` and `|E triangle F|<epsilon`.

If all sets have measure one, then

`|(E_1 x ... x E_n) triangle (F_1 x ... x F_n)| <= sum_i |E_i triangle F_i|`.   (3.3)

Since `0<=Phi<=1`, the corresponding objective values differ by at most the right-hand side of (3.3). Letting all approximation errors tend to zero proves the claim. QED.

**Important scope.** The support radius and number of components may depend arbitrarily on the approximant and on the input law. No uniform bound on either quantity follows or is used. This is exactly compatible with the live bounded-diameter and fixed-fragment-count corrections.

### QFORM consequence

For fixed `A` and interval `J`, the optimal small-ball probability over all admissible product densities is exactly the supremum over products of unit-height bounded finite-fragment sets. Therefore any inequality

`P{X^T A X in J} <= C |J|`                                      (3.4)

proved uniformly for all such finite-fragment product laws transfers to arbitrary independent densities `<=1` with **the same constant `C`**. Conversely, a failure of (3.4) in the full class can be approximated arbitrarily closely by finite-fragment witnesses. Arbitrary translations, distant fragments, and unbounded supports are therefore localization issues only if an intermediate estimate itself introduces location-dependent losses.

## 4. New theorem: arbitrary cyclic anchor dependence below the total critical exponent

The partner report proves the triangular case and shows that coordinatewise `theta_i<1` alone does not control cycles. The missing positive statement is that a genuinely cyclic block is still summable when its **total singular exponent** is below one.

For `i=1,...,m`, let

`E_i = disjoint_union_{alpha_i} I_{i,alpha_i}`,  `sum_{alpha_i} ell_{i,alpha_i}=1`,

and

`r_{i,alpha_i}(a)=dist(a,I_{i,alpha_i})+ell_{i,alpha_i}`.

Let `0<=theta_i<1`, set

`Theta=sum_i theta_i`,

and allow the anchor `a_i` to depend arbitrarily on every **other** component label `alpha_j`, `j!=i`, and on arbitrary additional continuous parameters, but not on its own label `alpha_i`.

Assume a nonnegative fragment ledger obeys

`W(alpha_1,...,alpha_m)`

` <= K prod_i [ell_{i,alpha_i} r_{i,alpha_i}(a_i(alpha_{-i}))^(-theta_i)]`.   (4.1)

### Theorem 4.1 — full cyclic Holder compiler

If `Theta<1`, then

`sum_{alpha_1,...,alpha_m} W(alpha_1,...,alpha_m)`

` <= K 2^Theta/(1-Theta)`.                                      (4.2)

#### Proof

Equip the label space with the product probability measure

`mu(alpha_1,...,alpha_m)=prod_i ell_{i,alpha_i}`.

Discard indices with `theta_i=0`, since their singular factor is one. If `Theta=0`, (4.2) is immediate. Otherwise, for every positive `theta_i` define

`p_i=Theta/theta_i`, so `p_i>=1` and `sum_i 1/p_i=1`.

Write

`F_i(alpha)=r_{i,alpha_i}(a_i(alpha_{-i}))^(-theta_i)`.

Generalized Holder gives

`E_mu prod_i F_i <= prod_i ||F_i||_{p_i}`.                       (4.3)

Because `p_i theta_i=Theta`,

`||F_i||_{p_i}^{p_i}`

` = E_{alpha_{-i}} [ sum_{alpha_i} ell_{i,alpha_i}`

`       r_{i,alpha_i}(a_i(alpha_{-i}))^(-Theta) ]`.

For every fixed choice of the other labels, the anchor is a fixed real number during the `alpha_i` sum. Apply the partner's one-coordinate theorem (2.1) with exponent `Theta<1`:

`sum_{alpha_i} ell_{i,alpha_i} r_{i,alpha_i}(a_i)^(-Theta)`

` <= 2^Theta/(1-Theta) =: C_Theta`.                              (4.4)

Hence `||F_i||_{p_i}<=C_Theta^(1/p_i)`. Multiplying and using `sum_i1/p_i=1` in (4.3),

`E_mu prod_i F_i <= C_Theta`.

Multiplying by `K` proves (4.2). QED.

### Sharp two-cycle threshold

For `m=2`, account02/B14's explicit cyclic construction proves divergence at and above `theta_1+theta_2=1`: logarithmic at equality and power-law above. Combined with Theorem 4.1, this gives the exact arbitrary-anchor two-cycle criterion:

`uniform fragment packing for all two-cycle anchors <=> theta_1+theta_2<1`.   (4.5)

Thus the partner obstruction is not merely negative; together with the Holder compiler it identifies the exact critical exponent for the complete two-coordinate cyclic class.

## 5. New theorem: strongly-connected-component localization compiler

The previous theorem can be combined with the partner's acyclic idea to handle much larger dependency graphs.

Create a directed graph `G` on `{1,...,m}` by putting an edge

`i -> j`

whenever the anchor `a_i` depends on the component label `alpha_j`. There are no self-edges because an anchor is assumed independent of its own component label. Let `C` run over the strongly connected components (SCCs) of `G`, and define

`Theta_C=sum_{i in C} theta_i`.

### Theorem 5.1 — SCC compiler

If

`Theta_C<1` for every strongly connected component `C`,             (5.1)

then every ledger satisfying (4.1) obeys

`sum_alpha W(alpha)`

` <= K prod_{C in SCC(G)} [2^(Theta_C)/(1-Theta_C)]`.             (5.2)

#### Proof

The condensation graph of SCCs is a finite DAG. Choose a source component `C`, meaning no edge enters `C` from another component. By the orientation convention, no factor belonging to a vertex outside `C` can depend on any label `alpha_i`, `i in C`; otherwise there would be an incoming edge to `C`. Therefore all factors outside `C` are constant while the labels in `C` are summed.

Fix every label outside `C`. Inside `C`, anchors may depend arbitrarily on all other labels of the same component, and also on the fixed outside labels. Apply Theorem 4.1 with total exponent `Theta_C` to sum over the labels in `C`. This costs at most

`2^(Theta_C)/(1-Theta_C)`.

Delete `C` from the graph. The remaining condensation graph is still a DAG. Repeat with a new source component. Multiplying the losses proves (5.2). QED.

### Relation to the partner theorem

If the dependency graph is acyclic, every SCC is a singleton, and (5.2) becomes exactly the partner's product constant

`prod_i 2^(theta_i)/(1-theta_i)`.

If the whole graph is strongly connected, (5.2) becomes Theorem 4.1. Thus Theorem 5.1 interpolates between the fully triangular and fully cyclic regimes and gives the correct unit of subcriticality: **total exponent per strongly connected dependency block**, not per coordinate.

## 6. Actual QFORM small-ball inequality produced by the compiler

Combine Theorem 3.3 with Theorem 5.1. Suppose a finite-fragment local shell/coarea analysis for the quadratic form produces, for every component tuple `alpha`, a nonnegative contribution `W_alpha(J)` satisfying

`W_alpha(J) <= K |J| prod_i [ell_{i,alpha_i}`

`  r_{i,alpha_i}(a_i(alpha_{-i}))^(-theta_i)]`,                 (6.1)

and the anchor-dependence graph has SCC totals below one. Then for every finite-fragment product law,

`P{X^T A X in J}`

` <= K |J| prod_C 2^(Theta_C)/(1-Theta_C)`.                    (6.2)

By the exact localization theorem of Section 3, the **same inequality (6.2)** holds for arbitrary independent input densities bounded by one, with no support, moment, translation, separation, or fragment-count hypothesis.

This is an actual target-level localization transfer: once a source-valid local shell estimate has the form (6.1), all arbitrary-law localization debt is discharged by the explicit SCC constant in (6.2).

### Concrete cyclic example not covered by the triangular theorem

Suppose three localized coordinates yield

`W_{alpha,beta,gamma}(J)`

` <= K|J| ell_alpha m_beta n_gamma`

`    r_alpha(a_{beta,gamma})^(-1/4)`

`    s_beta(b_{alpha,gamma})^(-1/4)`

`    t_gamma(c)^(-1/2)`.                                       (6.3)

The first two centers depend on one another, so the partner's triangular theorem does not apply directly. The dependency graph has SCCs `{1,2}` and `{3}` with totals `1/2` and `1/2`. Theorem 5.1 gives

`sum_{alpha,beta,gamma} W_{alpha,beta,gamma}(J)`

` <= K|J| (2^(1/2)/(1-1/2))^2`

` = 8 K |J|`.                                                   (6.4)

This is strictly stronger than the global-total criterion of Theorem 4.1, because the total exponent in (6.3) equals one. The graph structure, not a false coordinatewise independence assumption, is what saves the estimate.

The pattern is directly relevant to quadratic completion/coarea arguments: two mutually coupled stationary centers may form a genuine two-cycle, while a third center can lie in a downstream acyclic component. Quarter-power losses on the cyclic pair plus one square-root loss downstream are therefore summable with an explicit constant even though naive total-exponent counting is critical.

## 7. Translation, distant-fragment, and unbounded-support consequences

The new compiler has three invariances required by the assignment.

1. **Absolute translations cost nothing.** Every one-coordinate factor uses only `dist(a,I)+|I|`; translating both a fragment and its induced anchor leaves this unchanged. The packing constants depend only on exponents.
2. **Distant fragments cost nothing beyond the same formula.** No bound uses the diameter of the union, the number of gaps, or the largest center. In fact distance only increases `r` and therefore decreases the singular weight.
3. **Unbounded supports require no moments.** The exact bathtub/finite-fragment reduction is an approximation in product measure and small-ball probability, not in moments or support radii. The finite approximants may have arbitrarily large radii and fragment counts; (6.2) is uniform in both.

Thus the correct localization principle is not 'reduce to a bounded interval'. It is: reduce exactly to arbitrary finite fragments, prove a local fragment ledger, then sum that ledger by its dependency graph without inserting any support-scale parameter.

## 8. What remains unpaid

The full conjecture remains OPEN. This report does not itself produce the missing local shell estimate (6.1) for every matrix with three eigenvalues of modulus at least one.

The first B14-localization implication is now sharper than in the partner report:

> For a heavy/localized active block, derive a source-valid local shell/coarea estimate and record its fragment-center dependency graph. The localization step is automatically safe if every SCC has total singular exponent below one. A two-cycle at total exponent at least one needs genuine extra cancellation/aggregation, because the partner's explicit construction shows that fragment packing alone then diverges.

This removes the need to insist on a globally triangular elimination order. Mild cyclic stationary-center dependence is now admissible whenever the cyclic singularity budget is subcritical.

## 9. Source pins and correction closure

- source control immediately before scientific write: `yspennstate/math-research-brain@143158f9cac70bca95f553d1abd9da0bfa496eb1`;
- programme/control: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`;
- named partner actually applied: account02/B14, `yspennstate/math-open-problems@d358b89ba78735cee238c01e83c2c3ca9ec66352`, exact report path in Section 2;
- exact localization compatibility source checked: account03/B14, `yspennstate/math-open-problems@2208c3f666582999f1fbc7e55921a4530cbe2789`;
- fresh correction inbox re-read at control commit `143158f9cac70bca95f553d1abd9da0bfa496eb1`, including the newer `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`; no challenged premise above depends on that refuted structural implication.

No novelty/priority claim is made. Repository transport is not native memory ingestion. Full QFORM remains open.
