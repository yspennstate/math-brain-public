# fleet02/B14 — tail-free compactification and bang-bang localization

Status: **TARGET-LEVEL REDUCTION PROVED / FULL QFORM TARGET OPEN**

Programme: `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`.
Run: `20260922T120110Z-b14-qform-localization-r13`.
Execution context: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

## 1. Assignment and exact target

Current B14 assignment: control arbitrary shifts, distant fragments and unbounded supports with no moment assumptions, and prove a localization lemma preserving the full quadratic-density target and its constant.

Target: for every finite `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^T A X` has a density bounded by one universal constant `C`.

I use the equivalent measure form: a probability law `mu` on `R` has density bounded by `C` iff

`mu(I) <= C |I|`

for every bounded interval `I`. The reverse implication follows first for open sets (countable unions of disjoint intervals), then for Borel sets by outer regularity, giving `mu <= C Leb` and hence a Radon--Nikodym density at most `C`.

Mandatory corrections are preserved. Nothing below uses the refuted law-uniform pointwise Fresnel decay, independence after rotation, or a fiberwise spectral supremum.

## 2. Exact tail-free compactification, with no constant loss

### Theorem 2.1 (compact-support reduction)

Fix `n`, a measurable map `T:R^n->R` (in particular `T(x)=x^T A x`), and `C<infinity`. Suppose that for every product probability density

`F(x)=prod_i h_i(x_i)`,

with `0<=h_i<=1` and each `h_i` compactly supported, the pushforward `T_#(F dx)` satisfies

`T_#(F dx) <= C Leb`.

Then the same conclusion holds for arbitrary probability densities `0<=f_i<=1`, with **the identical constant `C`**.

### Proof

For `R>0`, put

`g_{i,R}(x)=f_i(x) 1_{[-R,R]}(x)`,
`m_{i,R}=int g_{i,R}`, and `tau_{i,R}=1-m_{i,R}`.

Choose a bounded interval `J_{i,R}` disjoint from `[-R,R]` of length exactly `tau_{i,R}` and set

`h_{i,R}=g_{i,R}+1_{J_{i,R}}`.

Then `h_{i,R}` is a compactly supported probability density and still satisfies `0<=h_{i,R}<=1`. Let

`nu_R = T_#( prod_i g_{i,R}(x_i) dx )`,
`mu_R = T_#( prod_i h_{i,R}(x_i) dx )`.

Because `prod_i g_{i,R} <= prod_i h_{i,R}` pointwise,

`nu_R <= mu_R <= C Leb`.                                                   (2.1)

Now the truncated product densities `prod_i g_{i,R}` increase pointwise to `prod_i f_i`. Hence for every Borel set `E`, monotone convergence gives

`nu_R(E) -> mu(E):=T_#(prod_i f_i dx)(E)`.

Passing to the limit in (2.1) yields `mu(E)<=C Leb(E)` for every finite-measure Borel `E`, and therefore for all Borel `E`. No moment, centering, tail-rate, or support-radius estimate appears. QED.

A quantitative error bound is also immediate:

`0 <= mu(E)-nu_R(E) <= 1-prod_i(1-tau_{i,R}) <= sum_i tau_{i,R}`.           (2.2)

Thus tails cost only their probability mass during the approximation and cost **zero** in the final constant.

### Why ordinary normalized truncation is the wrong operation

Conditioning a density on a small truncation can violate the admissible class: if `f=1_[0,1]` and one conditions on `[0,epsilon]`, the normalized density has height `1/epsilon`. The completion construction above never renormalizes the retained mass; it embeds the retained subprobability law as a positive submeasure of an admissible compact probability law. This is the key reason the constant is preserved.

## 3. Uniform Fourier-L1 bounds also localize without tail estimates

The same completion gives a second closure statement tailored to the current Fourier programme.

### Theorem 3.1 (Fourier compactification)

Assume that for every compactly supported admissible product law one has the uniform output characteristic-function bound

`int_R |phi_R(t)| dt <= K`,                                                (3.1)

with `K` independent of the support locations and radii. Then every arbitrary admissible product law satisfies the same bound `int|phi|<=K`. Consequently it has a continuous density bounded by `K/(2 pi)`.

### Proof

The completed coordinates satisfy

`||h_{i,R}-f_i||_1 <= 2 tau_{i,R}`.

Since all factors have `L1` norm `1`, the telescoping product inequality gives

`|| prod_i h_{i,R} - prod_i f_i ||_1 <= 2 sum_i tau_{i,R} -> 0`.           (3.2)

Pushforward cannot increase total variation, and therefore

`|phi_R(t)-phi(t)| <= 2 sum_i tau_{i,R}`                                  (3.3)

for every `t` (indeed uniformly in `t`). Hence `phi_R(t)->phi(t)` pointwise. Fatou applied to (3.1) yields

`int |phi(t)| dt <= liminf_R int |phi_R(t)| dt <= K`.

Fourier inversion then gives the stated continuous density bound. QED.

This is important operationally: a future integrated-Fourier proof may assume compactly supported coordinate laws **without any separate moment or tail argument**, provided its constant is uniform in support geometry.

## 4. Bang-bang extremal localization for the target small-ball functional

Compact support can be reduced further, exactly at the target small-ball level.

### Lemma 4.1 (one-coordinate bathtub extremizer)

Let `K` be a bounded measurable set with `|K|>=1`, let `g:K->[0,1]` be measurable, and let

`D(K)={ f: 0<=f<=1, supp(f) subset K, int f=1 }`.

Then

`sup_{f in D(K)} int_K g f = sup_{A subset K, |A|=1} int_A g`.             (4.1)

Proof: choose `lambda` with `|{g>lambda}|<=1<=|{g>=lambda}|`, choose a measurable subset of the level set `{g=lambda}` so that

`A={g>lambda} union B`

has measure `1`, and write

`int g(f-1_A)=int (g-lambda)(f-1_A) <= 0`.

The inequality is pointwise by the signs on `{g>lambda}` and `{g<lambda}`. Lebesgue measure is non-atomic, so the required `B` exists.

### Theorem 4.2 (product bang-bang reduction)

Fix bounded support sets `K_i` and an output interval `I`. For any measurable `T:R^n->R`,

`sup_{f_i in D(K_i)} int 1_{T(x) in I} prod_i f_i(x_i) dx`

is exactly

`sup_{A_i subset K_i, |A_i|=1} |{x in prod_i A_i : T(x) in I}|`.           (4.2)

Proof: with all coordinates except `i` fixed, the objective is linear in `f_i`, with coefficient

`g_i(x_i)=int 1_{T(x) in I} prod_{j!=i} f_j(x_j) dx_{-i}`,

and `0<=g_i<=1`. Apply Lemma 4.1 to coordinate `1`, then `2`, ..., `n`. Each replacement is by an indicator density and never decreases the objective. Indicators are themselves admissible, giving equality of the suprema. QED.

### Corollary 4.3 (finite-union geometric equivalence)

For a fixed constant `C`, the full quadratic-form target is equivalent to the following geometric statement:

For every target matrix `A`, every bounded interval `I`, and every choice of sets `E_i` that are **finite unions of bounded intervals with total length exactly `1`**,

`| { x in E_1 x ... x E_n : x^T A x in I } | <= C |I|`.                  (4.3)

The forward implication is immediate because `1_{E_i}` are admissible probability densities.

For the reverse implication, first use Theorem 2.1 to reduce to compactly supported product densities. Theorem 4.2 replaces them, for the fixed interval `I`, by indicator densities `1_{A_i}` of bounded measurable sets of measure `1`, without decreasing the small-ball probability. By Lebesgue regularity, each bounded measurable `A_i` can be approximated in symmetric difference by a finite union of bounded intervals. Adjust the total length to exactly `1` by shaving a total excess length from endpoints or adding one disjoint interval carrying the deficit. Thus there are finite unions `E_i^(m)` with

`|E_i^(m)|=1`,   `|E_i^(m) Delta A_i| -> 0`.

The telescoping product inequality gives

`|| prod_i 1_{E_i^(m)} - prod_i 1_{A_i} ||_1 <= sum_i |E_i^(m) Delta A_i| -> 0`,

so the corresponding output probabilities converge for every fixed event `I`. Applying (4.3) and taking the limit proves the compact small-ball bound, and Theorem 2.1 removes the compact-support restriction. QED.

Thus **no smoothness, moments, connected support, or tail decay is needed in the input-law search**. Any counterexample to the full conjecture can be approximated, at any witnessing small-ball scale, by independent uniforms on finite unions of intervals of total length `1` in each coordinate. Conversely, proving (4.3) with one universal `C` proves the full target with that same `C`.

Important scope: the number of fragments and their diameter are not bounded by this reduction. A proof whose constant grows with fragment count, support diameter, or location does not close the target.

## 5. Exact translation covariance

If `a in R^n` and `x=y+a`, then

`x^T A x = y^T A y + 2 (A a)^T y + a^T A a`.                              (5.1)

The Hessian is still `2A`, so the eigenvalues relevant to the target are unchanged. Therefore any proof that recenters distant fragments must be uniform in the translation-generated linear coefficient `2Aa`; paying a factor depending on `|a|` would contradict the target's translation freedom. The compactification proof above avoids such a payment entirely.

Equation (5.1) also gives an exact affine reformulation: support translations correspond to affine quadratic polynomials whose linear term lies in `Range(A)`. Output translation by the constant `a^T A a` does not change an `L^infinity` density bound.

## 6. Application of a completed other-account result

I consumed the complete fleet03/B05 report

`yspennstate/math-open-problems@c828d2ee2f8acef5eb96892bc8a9a25594db0f51`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T113800Z-fleet03-B05-qform-r11/REPORT.md`.

That report proves a delocalized Fresnel--Brascamp--Lieb theorem from a projected Wiener bound and leaves a selected-large-mode weighted Wiener estimate as its first unpaid implication. Theorem 3.1 above applies directly to that mechanism: to prove such a uniform Wiener/Fourier-L1 estimate, it is enough to prove it for compactly supported coordinate densities, with a constant uniform in support geometry; unbounded support then follows by (3.2)--(3.3) and Fatou.

The bang-bang reduction does **not** automatically apply to `int|phi|`, because the absolute value destroys multilinearity. It applies to the target small-ball functional, where the coordinatewise objective is genuinely linear. This distinction is essential.

No completed current-qform handoff from the assigned `fleet03/B14` partner was visible at the source read, so no stale pre-qform artifact was substituted.

## 7. Consistency with the mandatory pointwise-decay correction

Compact localization does not revive the refuted pointwise oscillatory claim. The phase-aligned construction in current research already chooses a **finite union of intervals of total length `1`** on which the quadratic phase is nearly constant. Hence the pointwise-decay counterexample survives inside the exact reduced class (4.3).

The usable Fourier statement is instead Theorem 3.1: a **uniform integrated** Fourier bound proved on compact inputs transfers globally by Fatou.

## 8. What moved and what remains

**Target-level change:** yes, a lossless equivalence/reduction is proved. The arbitrary-law, arbitrary-support target is exactly reduced to the finite-union geometric small-ball problem (4.3), with the same constant `C`.

**Full-problem status:** OPEN. No universal `C` for (4.3) is proved here.

**First remaining implication for B14:** establish a dimension-free geometric small-ball estimate for the finite-union unit-measure product sets in (4.3), uniformly in the number, locations, and separations of fragments, for general rotated indefinite `A` with three eigenvalues `|lambda|>=1`; or construct a genuine finite-union counterexample. For the integrated-Fourier route, it is enough to prove the needed uniform compact-support estimate, since tails are now eliminated by Theorem 3.1.

## 9. Source pins and integrity

Start control main observed: `a1c684c2b92f8206373b93d5b433d2c4376a7aa9`.
Pre-write control recheck main observed: `21f8b8cdde140cba387de73334c93ed02a671fda`.
Owner-control revision: `2026-09-22.5`; programme `QFORM-DENSITY-3EIG-20260922`.
Current-research source read at the start control commit; partner theorem source pinned above to its immutable math-open-problems commit.

Changed-file privacy review for this report: mathematical text and repository source pins only; no credentials, scheduler identifiers, machine paths, email content, private personal data, benchmark material, or unrelated source excerpts. No paid API/model, remote workflow, public posting, or permission mutation was used.
