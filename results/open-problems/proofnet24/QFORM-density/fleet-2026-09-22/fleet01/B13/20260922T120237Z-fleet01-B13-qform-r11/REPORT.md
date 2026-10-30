# fleet01/B13 — convex-hull extremal law theorem and nonlinear Fourier transfer

**Run:** `20260922T120237Z-fleet01-B13-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** `Extremal product laws`  
**Classification:** `ESSENTIAL_STEP_APPLIED / STRUCTURAL_TRANSFER / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full conjecture:** **OPEN / NOT PROVED.**

## 0. Source state and corrections

Fresh protected controls moved this invocation away from the superseded FEI prompt and onto the sole live target:

> For independent real `X_i` with densities `0<=f_i<=1` and real symmetric `A` having at least three eigenvalues with absolute value at least one, prove that `Q=X^T A X` has density bounded by one universal finite constant.

The coherent source state used for the mathematics was `yspennstate/math-research-brain@b00183d9a30ed16f931f01b4053792092ccccd7d`, revision `2026-09-22.5`; before publication the control branch was re-resolved at `21f8b8cdde140cba387de73334c93ed02a671fda`, with no later owner stop or target change observed in the intervening diff.

Corrections consumed:

1. `QFORM-POINTWISE-DECAY-FALSE`: a law-uniform pointwise Fresnel decay estimate is false for arbitrary density-bounded inputs.
2. `QFORM-FIBER-SUP-DIMENSION-LOSS`: unrestricted fiber suprema may lose dimension.
3. `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: orthogonal diagonalization does not preserve independence.
4. Fresh event `QFORM-CROSSMINOR-ALONE-FALSE` (`fleet02/B09`, canonical report commit `fa592b592c61bd1597aa8cf3270c3c9f58f410bf`): a nonsingular cross minor alone does not pay the quadratic shell unless the required pivot-side structure is also present.

This run does **not** repeat the previous B13 product-kernel bathtub theorem or the delocalized rank-three theorem. Those were archived at `yspennstate/math-open-problems@15deb1a797502f6d8d98dc7f0cd60eb43a41dd3` and its follow-up claim cards. The new point here is a genuine **convex-hull / mixture theorem** which applies to nonlinear convex output functionals, in particular the integrated absolute characteristic function. Coordinate-by-coordinate bathtub arguments do not directly handle that nonlinear functional.

A source-visible qform result from the assigned partner `fleet02/B13` was not present when checked; no partner theorem is fabricated. I instead substantively apply the compatible existing-worker finite-fragment theorem `fleet04/B14@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322` and the exact bathtub/stability result `fleet03/B15@3615dc06403453ba4df2e50dabf33c210db07865`.

---

## 1. The one-dimensional admissible density class is an L1 closed convex hull of indicator laws

Define

\[
\mathcal D
:=
\left\{f\in L^1(\mathbb R): 0\le f\le1\ \text{a.e.},\ \int_{\mathbb R}f=1\right\},
\]

and

\[
\mathcal E
:=
\left\{1_E: E\subset\mathbb R\ \text{measurable},\ |E|=1\right\}.
\]

### Theorem 1 — `QFORM-L1-CONVEX-HULL-EXTREMES-v1`

\[
\boxed{
\mathcal D
=
\overline{\operatorname{co}}^{\,L^1}(\mathcal E).
}
\tag{1.1}
\]

Equivalently, every admissible density is an `L^1` limit of finite convex combinations of uniform densities on arbitrary measurable sets of Lebesgue measure one.

### Proof

First, `\mathcal D` is convex and closed in `L^1`. Indeed, if `f_m\to f` in `L^1`, then `\int f=1`; after passing to a subsequence, `f_m\to f` almost everywhere, so `0\le f\le1` almost everywhere. Hence

\[
C:=\overline{\operatorname{co}}^{L^1}(\mathcal E)\subset\mathcal D.
\]

Suppose for contradiction that some `f\in\mathcal D` lies outside `C`. By Hahn--Banach separation in `L^1`, there exists `h\in L^\infty(\mathbb R)` such that

\[
\int h f
>
\sup_{g\in C}\int h g
=
\sup_{|E|=1}\int_E h.
\tag{1.2}
\]

But the one-coordinate bathtub identity gives, for every bounded real measurable `h`,

\[
\sup_{g\in\mathcal D}\int hg
=
\sup_{|E|=1}\int_E h.
\tag{1.3}
\]

For completeness, if `h` is signed, add a constant `M\ge\|h\|_\infty`; because every admissible `g` and every `1_E` has mass one, this adds the same constant to both sides. The nonnegative case follows from the usual layer-cake/top-level-set argument. Since `f\in\mathcal D`, (1.3) contradicts (1.2). Therefore `C=\mathcal D`. `QED`.

### Extreme points

The theorem is consistent with the exact extreme-point classification: the extreme points of `\mathcal D` are precisely the indicators `1_E`, `|E|=1`. If `f` takes values strictly between zero and one on a positive-measure set, choose two disjoint positive-measure pieces on which `f` stays uniformly away from `0,1`, and perturb by opposite small constants with equal integrals. Thus `f` is not extreme. Conversely an indicator cannot be split nontrivially while remaining between `0` and `1`.

The closed-convex-hull statement is stronger than merely knowing the extreme points: it provides the approximation needed below for nonlinear convex functionals.

---

## 2. Finite-interval-union generators suffice

The compatible fleet04/B14 theorem at commit

`8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`

proves that every measurable `E` of measure one admits sets `E_m`, each a bounded finite union of intervals of total length exactly one, with

\[
|E_m\triangle E|\to0.
\tag{2.1}
\]

Applying that theorem to the generating set `\mathcal E` in (1.1) gives immediately:

### Corollary 2 — `QFORM-FINITE-FRAGMENT-CONVEX-HULL-v1`

Let `\mathcal E_{\rm fin}` be the indicators of bounded finite unions of intervals of total length one. Then

\[
\boxed{
\mathcal D
=
\overline{\operatorname{co}}^{\,L^1}(\mathcal E_{\rm fin}).
}
\tag{2.2}
\]

Thus fractional densities, unbounded supports and infinitely fragmented sets can all be removed **before** studying any convex total-variation lower-semicontinuous output functional.

This is a substantive application of the fleet04/B14 result: its finite-fragment localization is promoted from a statement about the linear shell functional to a generating theorem for the entire admissible one-dimensional law class.

One can further choose rational endpoints after an arbitrarily small symmetric-difference perturbation while preserving total length one, so there is also a countable dense generating family. This is useful for falsification or compactly indexed approximations, but a finite sweep over that family is of course not a proof of a uniform inequality.

---

## 3. Product laws are total-variation limits of finite mixtures of product indicators

Fix `n`. For each `i`, choose

\[
g_i^{(m)}
=
\sum_{r=1}^{N_{i,m}}\alpha_{i,r}^{(m)}1_{E_{i,r}^{(m)}},
\qquad
\alpha_{i,r}^{(m)}\ge0,
\qquad
\sum_r\alpha_{i,r}^{(m)}=1,
\]

with `|E_{i,r}^{(m)}|=1` and

\[
\|f_i-g_i^{(m)}\|_1\to0.
\tag{3.1}
\]

Then

\[
G_m(x)
:=
\prod_{i=1}^n g_i^{(m)}(x_i)
=
\sum_{r_1,\ldots,r_n}
\left(\prod_i\alpha_{i,r_i}^{(m)}\right)
1_{E_{1,r_1}^{(m)}\times\cdots\times E_{n,r_n}^{(m)}}(x).
\tag{3.2}
\]

So `G_m` is a finite convex mixture of **product-indicator probability densities**.

Moreover, the telescoping product identity gives the exact dimension-additive bound

\[
\boxed{
\left\|
\prod_i f_i-
\prod_i g_i^{(m)}
\right\|_{L^1(\mathbb R^n)}
\le
\sum_{i=1}^n\|f_i-g_i^{(m)}\|_1.
}
\tag{3.3}
\]

Indeed, each telescoping term factorizes in `L^1`, and every untouched marginal has integral one.

Hence the product input law converges in total variation to finite mixtures of product-indicator laws. For any measurable map `T:\mathbb R^n\to\mathbb R`, in particular `T=Q(x)=x^TAx`, pushforward cannot increase total variation, so

\[
T_\#(G_mdx)\to T_\#\left(\prod_i f_i(x_i)dx\right)
\quad\text{in total variation}.
\tag{3.4}
\]

---

## 4. A general nonlinear extremal-transfer theorem

The previous product-kernel bathtub theorem only applies directly to separately linear positive objectives. The next result handles genuinely nonlinear output functionals.

### Theorem 3 — `QFORM-CONVEX-OUTPUT-TRANSFER-v1`

Let `T:\mathbb R^n\to\mathbb R` be measurable. Let `\Phi` be any extended-real functional on probability measures on `\mathbb R` satisfying:

1. `\Phi` is convex;
2. `\Phi` is lower semicontinuous under total-variation convergence.

Then

\[
\boxed{
\sup_{f_1,\ldots,f_n\in\mathcal D}
\Phi\!\left(T_\#\bigotimes_i(f_i dx_i)\right)
=
\sup_{|E_1|=\cdots=|E_n|=1}
\Phi\!\left(T_\#\bigotimes_i(1_{E_i}dx_i)\right).
}
\tag{4.1}
\]

The same supremum is obtained if each `E_i` is required to be a bounded finite union of intervals of total length one.

### Proof

The `\ge` inequality is immediate because product indicators are admissible product densities.

Let

\[
M:=
\sup_{|E_i|=1}\Phi\left(T_\#\bigotimes_i1_{E_i}dx_i\right).
\]

If `M=+\infty` there is nothing to prove. Otherwise, for arbitrary `f_i\in\mathcal D`, use (3.2)--(3.4). Write

\[
\mu_m=T_\#(G_mdx)
=
\sum_\alpha w_{m,\alpha}\mu_{m,\alpha},
\]

where every `\mu_{m,\alpha}` is the output law from a product-indicator input and `w_{m,\alpha}` are nonnegative weights summing to one. Convexity gives

\[
\Phi(\mu_m)
\le
\sum_\alpha w_{m,\alpha}\Phi(\mu_{m,\alpha})
\le M.
\tag{4.2}
\]

By (3.4) and total-variation lower semicontinuity,

\[
\Phi(\mu)
\le
\liminf_m\Phi(\mu_m)
\le M.
\]

Taking the supremum over arbitrary admissible `f_i` proves (4.1).

Finally, fleet04/B14 supplies total-variation approximation of each indicator law by bounded finite interval unions of the same mass. Applying lower semicontinuity once more shows that the finite-fragment subclass has the same supremum. `QED`.

---

## 5. Exact nonlinear reduction for the integrated Fourier route

For a probability measure `\mu` on `\mathbb R`, define

\[
\Phi_{\rm F}(\mu)
:=
\int_{\mathbb R}|\widehat\mu(t)|\,dt
\in[0,\infty].
\tag{5.1}
\]

This functional is convex. It is also lower semicontinuous in total variation: if `\mu_m\to\mu` in total variation, then

\[
|\widehat\mu_m(t)-\widehat\mu(t)|
\le
\|\mu_m-\mu\|_{\rm TV,*}
\to0
\]

uniformly in `t` (up to the harmless convention-dependent factor two), and Fatou gives

\[
\int|\widehat\mu|
\le
\liminf_m\int|\widehat\mu_m|.
\tag{5.2}
\]

Applying Theorem 3 with `T=Q` proves the exact identity

### Corollary 4 — `QFORM-FOURIER-L1-EXTREME-TRANSFER-v1`

\[
\boxed{
\sup_{f_i\in\mathcal D}
\int_{\mathbb R}
\left|
\int_{\mathbb R^n}e^{itQ(x)}\prod_i f_i(x_i)\,dx
\right|dt
=
\sup_{|E_i|=1}
\int_{\mathbb R}
\left|
\int_{E_1\times\cdots\times E_n}e^{itQ(x)}\,dx
\right|dt.
}
\tag{5.3}
\]

The right side is unchanged if every `E_i` is a bounded finite union of intervals of total length one.

This is the main new implication of the run. The current research state explicitly leaves open a **uniform integrated characteristic-function estimate** after the pointwise route was refuted. Equation (5.3) shows that this nonlinear integrated problem can be attacked entirely on finite-fragment product indicators, with no later loss when one returns to arbitrary densities `0<=f_i<=1`.

In particular, if one proves for all target-admissible `A` and all such product sets that

\[
\int_{\mathbb R}
\left|
\int_{\prod_iE_i}e^{itx^TAx}\,dx
\right|dt
\le M,
\tag{5.4}
\]

then every admissible product density satisfies the same bound, and Fourier inversion yields

\[
\|p_Q\|_\infty\le \frac{M}{2\pi}.
\tag{5.5}
\]

No coordinatewise optimization of an absolute value is required.

---

## 6. The target concentration norm is also a convex output functional

Define

\[
\Phi_{\rm conc}(\mu)
:=
\sup_{a<b}\frac{\mu((a,b))}{b-a}.
\tag{6.1}
\]

This is a supremum of continuous affine functionals under total variation, hence convex and lower semicontinuous. It is finite exactly when `\mu` is absolutely continuous with density bounded by `\Phi_{\rm conc}(\mu)` almost everywhere: the interval bound extends to open sets and then to Borel sets, giving `\mu\le C\,\mathrm{Leb}`.

Thus Theorem 3 recovers the exact product-set reduction for the target density norm in one stroke:

\[
\boxed{
\sup_{f_i\in\mathcal D}\Phi_{\rm conc}(Q_\#\otimes_i f_i dx_i)
=
\sup_{|E_i|=1}\Phi_{\rm conc}(Q_\#\otimes_i1_{E_i}dx_i).
}
\tag{6.2}
\]

This agrees with the separately linear bathtub theorem, but the proof now sits inside a reusable convex-mixture framework that also covers the Fourier `L^1` norm.

The exact bathtub/stability theorem of fleet03/B15 at

`3615dc06403453ba4df2e50dabf33c210db07865`

adds a finer fact for the **linear fixed-interval** objective: any near-extremizing product law is coordinatewise close, away from score-tie plateaus, to threshold indicators for the actual conditional shell score. Combining that peer theorem with (2.2) and (6.2) yields the following clean structural picture:

- for the target small-ball functional, extreme and near-extreme behavior is carried by threshold-like product indicators;
- for the nonlinear integrated Fourier functional, extreme reduction still holds by convex-mixture transfer even though coordinatewise bathtub linearity is unavailable;
- arbitrary fractional marginals do not create a separate obstruction in either route.

---

## 7. The pointwise-decay obstruction survives even on finite interval unions

It is important not to misread the extreme-law reduction as a repair of the refuted pointwise Fourier strategy. The failure already occurs inside the finite-fragment generating class.

Fix `s>0` and `0<\delta<\pi`. For integers `k` large enough that `2\pi k>\delta`, define

\[
I_k
=
\left[
\sqrt{\frac{2\pi k-\delta}{s}},
\sqrt{\frac{2\pi k+\delta}{s}}
\right].
\tag{7.1}
\]

The intervals are pairwise disjoint, and on every `I_k`,

\[
|sx^2-2\pi k|\le\delta,
\qquad
\Re e^{isx^2}\ge\cos\delta.
\tag{7.2}
\]

Their lengths satisfy

\[
|I_k|
=
\frac{2\delta/\sqrt s}
{\sqrt{2\pi k+\delta}+\sqrt{2\pi k-\delta}}
\ge
\frac{\delta}{\sqrt{s(2\pi+\delta)}}\,k^{-1/2},
\tag{7.3}
\]

so `\sum_k|I_k|=\infty`. Therefore a **finite** union of these intervals has total length exceeding one. Take whole components until the accumulated length is below one and then a subinterval of the next component, obtaining a bounded finite union `E` with `|E|=1` and

\[
\boxed{
\left|\int_E e^{isx^2}\,dx\right|
\ge
\Re\int_E e^{isx^2}\,dx
\ge
\cos\delta.
}
\tag{7.4}
\]

Because `s` is arbitrary, no law-uniform positive power decay can hold even on the finite-interval-union extreme laws.

For three independent copies and the diagonal positive form

\[
Q=x_1^2+x_2^2+x_3^2,
\]

choosing the same phase-aligned `E` in each coordinate gives

\[
|\phi_Q(s)|
\ge
(\cos\delta)^3.
\tag{7.5}
\]

Thus the fresh convex reduction preserves the existing correction `QFORM-POINTWISE-DECAY-FALSE`; it does not bypass it. Any Fourier proof must exploit **integration/averaging in frequency**, not a universal pointwise envelope.

---

## 8. What changed mathematically

### Old structural state

The previous B13/B14/B15 work proved that fixed small-ball probabilities are maximized by product indicators and that arbitrary indicator sets can be approximated by bounded finite interval unions. Those arguments are tied to positive separately linear kernels such as `1_{Q\in J}`.

### New implication paid

This run proves that the entire admissible density class is the `L^1` closed convex hull of those extreme laws, and therefore that **every convex total-variation lower-semicontinuous output functional has exactly the same worst case on product indicators**. In particular the nonlinear functional

\[
\mu\mapsto\int|\widehat\mu(t)|dt
\]

has an exact extreme-product reduction, equation (5.3).

This directly advances the surviving integrated-Fourier pathway: one may now work only with finite-fragment product indicators without carrying arbitrary fractional densities through the oscillatory analysis.

### Remaining unpaid implication

The first unpaid target-level step is still geometric/oscillatory rather than measure-theoretic:

> Prove either a universal shell estimate or a universal integrated-Fourier estimate for `Q=x^TAx` on products of bounded finite interval unions of total length one, uniformly in fragment count, positions, translations, dimension, and all target-admissible rotated indefinite matrices `A`.

The fresh `QFORM-CROSSMINOR-ALONE-FALSE` event forbids paying this merely from a nonsingular cross block without the required pivot-side structure. The pointwise phase-alignment construction above forbids replacing the integrated problem by a pointwise decay estimate.

The previous B13 theorem already closes the exactly-rank-three regime with all coordinate leverage scores at most `1/2`; the localized/high-leverage regime and full matrices with additional spectral directions remain open.

---

## 9. Status and source-integrity notes

**Classification:** `ESSENTIAL_STEP_APPLIED / STRUCTURAL_TRANSFER`.

Proved here:

- `QFORM-L1-CONVEX-HULL-EXTREMES-v1`;
- `QFORM-FINITE-FRAGMENT-CONVEX-HULL-v1` (using fleet04/B14);
- `QFORM-PRODUCT-MIXTURE-TV-v1`;
- `QFORM-CONVEX-OUTPUT-TRANSFER-v1`;
- `QFORM-FOURIER-L1-EXTREME-TRANSFER-v1`;
- `QFORM-FINITE-FRAGMENT-POINTWISE-NOGO-v1`.

Not proved:

- a uniform integrated Fourier bound for the full target;
- a uniform geometric shell bound for arbitrary rotations;
- the full quadratic-form density conjecture.

The assigned partner `fleet02/B13` had no qform output visible during the dependency checks, so no result is attributed to it. Compatible peer results from fleet04/B14 and fleet03/B15 were actually used as described above. No public release, scheduler mutation, paid model/API call, remote workflow, permission change, or email was used.

Privacy/source review for this report was a manual changed-file review only: the report contains mathematical statements, repository source pins and nonsecret run identifiers; it contains no credentials, scheduler IDs, machine paths, unrelated private material, or held-out benchmark content.
