# account01/B18 — exact product-set reduction and sharp linear-image transfer

**Run:** `20260922T115514Z-qform-B18-a01`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Literature-to-proof transfer  
**Classification:** `PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  

## 1. Exact target and correction status

The live target is: for every `n`, independent real `X_i` with densities `0 <= f_i <= 1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^T A X` has an essentially bounded density with one universal dimension-independent bound.

The full conjecture remains **OPEN / NOT PROVED**. This run does not use the refuted law-uniform pointwise Fourier-decay claim, does not rotate and then pretend coordinates remain independent, and does not use a single cross-minor as sufficient. The current correction `QFORM-CROSSMINOR-ALONE-FALSE` was consumed before this write.

The assigned partner `account02/B18` had no completed qform artifact at retrieval time. I therefore did not invent a partner result or wait. I substantively used the compatible completed `account02/B12` report at `yspennstate/math-open-problems@39b363886b16b0d29919b0c0f45bedd997c47c44:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T115433Z-account02-B12/REPORT.md`, in particular its source-valid rule that conditioning outside an original-coordinate block preserves the product law on the remaining coordinates and turns cross terms into linear tilts.

## 2. Exact extremal reduction: arbitrary bounded densities -> unit-measure product sets

Let `D={f:R->[0,1] measurable: integral f=1}`. Let `Phi:R^n->S` be measurable and `B subset S` measurable. Define

`T(f_1,...,f_n)=integral 1_{Phi(x) in B} prod_i f_i(x_i) dx`.

### Theorem 2.1 (bang-bang/product-set reduction)

`sup_{f_1,...,f_n in D} T(f_1,...,f_n)` equals

`sup_{|E_1|=...=|E_n|=1} |{x in E_1 x ... x E_n: Phi(x) in B}|`,

where the `E_i` are arbitrary measurable subsets of `R` of measure one.

#### Proof

Fix all densities except `f_i` and define

`h_i(t)=integral 1_{Phi(x_1,...,t,...,x_n) in B} prod_{j!=i} f_j(x_j) dx_{-i}`.

Then `0<=h_i<=1` and the objective is `integral h_i f_i`. For any measurable `h:R->[0,1]` and `f in D`, layer cake gives

`integral h f = integral_0^1 integral_{h>s} f dx ds <= integral_0^1 min(1, |{h>s}|) ds`.

The right side is exactly `sup_{|E|=1} integral_E h`: choose a unit-measure set from the top level sets of `h` (Lebesgue measure is nonatomic; if the active support has measure below one, fill the remainder where `h=0`). Thus `f_i` can be replaced by an indicator `1_{E_i}`, `|E_i|=1`, without decreasing the objective. Iterate over all coordinates. The reverse inequality is immediate because indicators of unit-measure sets are admissible densities. QED.

### Corollary 2.2 (exact geometric reformulation)

For every interval `I`,

`sup_{independent X_i, ||f_i||_infty<=1} P(X^T A X in I)`

`= sup_{|E_i|=1} |{x in prod_i E_i: x^T A x in I}|`.

Hence the owner target is equivalent to one universal `C` such that

`|{x in prod_i E_i: x^T A x in I}| <= C |I|`

for every admissible `A`, every interval `I`, and every measurable unit-measure `E_i`.

This does **not** reduce to interval supports: highly fragmented measurable sets remain allowed, consistent with the phase-aligned-density obstruction to pointwise Fourier decay. The argument also works after conditioning outside any original-coordinate block, because the remaining conditional law is still the original product law; this is the point at which the account02/B12 conditioning mechanism is applied.

## 3. Primary-literature transfer: sharp density of every linear image

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1, proves that for a product density whose one-dimensional factors are bounded by one, every `k`-dimensional orthogonal projection has density bounded by `2^{k/2}`.

### Theorem 3.1 (general full-rank linear image bound)

Let `T` be a real `k x n` matrix of rank `k<n`. For independent `X_i` with densities bounded by one,

`||p_{TX}||_infty <= 2^{k/2}/sqrt(det(T T^T))`.

#### Proof

Set `S=(TT^T)^{1/2}` and `U=S^{-1}T`. Then `UU^T=I_k`, so `UX` is an orthogonal `k`-dimensional projection after identifying the row space with `R^k`. The primary theorem gives `||p_{UX}||_infty<=2^{k/2}`. Since `TX=S(UX)`, change of variables gives the displayed bound because `det S=sqrt(det(TT^T))`. QED.

### Corollary 3.2 (three spectral coordinates)

For any three orthonormal eigenvectors `r_1,r_2,r_3` of `A`,

`Y=(<r_1,X>,<r_2,X>,<r_3,X>)`

has

`||p_Y||_infty <= 2^{3/2}=2 sqrt(2)`.

This is a genuine dimension-free statement under exactly the owner's arbitrary bounded-density hypotheses.

## 4. Why this does not close the quadratic theorem

In eigenbasis coordinates `(Y,W)`,

`Q=lambda_1 Y_1^2+lambda_2 Y_2^2+lambda_3 Y_3^2+R(W)`.

The marginal density of `Y` is bounded, but `Y` and `W` are generally dependent after rotation, so one may not convolve the three-square law with an independent remainder. This is the live no-independence-after-rotation correction.

A generic bounded joint density is also insufficient in the indefinite case. For `q(y)=y_1^2+y_2^2-y_3^2`, use cylindrical coordinates and then `u=r-z`, `v=r+z`; then `q=uv` and volume element is `(u+v)du dv dtheta/4`. For any `delta>0`, take

`R_delta={R<=v<=R+L, 0<=u<=delta/v, theta in Theta}`

with `Theta` chosen so `|R_delta|=1`. Then `1_{R_delta}` is a probability density bounded by one, but `0<=q<=delta` everywhere on its support, so `P(q in [0,delta])=1`. Thus bounded joint density alone cannot yield a universal q-density bound. This is **not** a counterexample to the owner target because such a three-dimensional law need not be an orthogonal image of a one-dimensional product law; it only proves that product structure cannot be discarded after rotation.

## 5. Literature scope check

Egor Kosov, *Oscillatory integrals with polynomial phase and regularity of distributions*, arXiv:2511.02679 (2025), Theorems 1.6--1.7, gives dimension-free regularity/oscillatory estimates for product measures but assumes each one-dimensional density has **bounded variation**. The owner target assumes only `0<=f_i<=1`, so this source does not cover the target. The phase-aligned-density correction makes this distinction material.

I did not find a source-exact prior theorem in the checked literature having all four required features simultaneously: arbitrary independent densities bounded only in `L^infty`, arbitrary dimension, arbitrary rotation/indefinite signature, and only three eigenvalues of magnitude at least one. This is a search result, not a novelty claim.

## 6. Exact change and unpaid implication

**Proved:** all input-law extremization transfers exactly to uniforms on arbitrary measurable unit-measure sets.  
**Proved from primary literature:** every rank-`k` linear image satisfies `||p_{TX}||_infty<=2^{k/2}/sqrt(det(TT^T))`; in particular the three selected spectral coordinates have density at most `2 sqrt(2)`.

**First unpaid implication:** exploit that the rotated joint law is the orthogonal image of a **product-set law**, not an arbitrary bounded joint density, to prove a curved-disintegration estimate

`|{x in prod E_i: x^T A x in I}| <= C |I|`

from three large eigenvalues. A marginal bound alone, a fiber supremum, or a generic bounded-joint-density coarea estimate is insufficient. A concrete next route is to combine the product-set reduction with an **averaged** family of source-valid original-coordinate pair/triple blocks rather than selecting one tiny coordinate minor. The live `QFORM-CROSSMINOR-ALONE-FALSE` correction forbids treating an isolated cross minor as sufficient.

## 7. Source pins

- live control before write: `yspennstate/math-research-brain@428ea8b10266994fcacde3ef4075758875004c18`, owner revision `2026-09-22.5`;
- correction consumed: `scheduled_tasks/work/shared/qform-density-2026-09-22/events/account02/B09/20260922T115241Z-account02-B09-QFORM-r1/QFORM-CROSSMINOR-ALONE-FALSE.json`;
- compatible peer consumed: `yspennstate/math-open-problems@39b363886b16b0d29919b0c0f45bedd997c47c44:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T115433Z-account02-B12/REPORT.md`;
- primary theorem: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1;
- scope check: Kosov, arXiv:2511.02679, Theorems 1.6--1.7.

Scoped manual privacy review performed on this single changed file; no full repository scanner was available in this runtime. No credentials, scheduler IDs, machine paths, unrelated private data, public release, permission change, email, Drive, or paid/remote compute action was used.
