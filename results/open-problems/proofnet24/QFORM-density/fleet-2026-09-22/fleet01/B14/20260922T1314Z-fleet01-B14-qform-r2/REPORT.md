# fleet01/B14 — anisotropic principal-triple localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T1314Z-fleet01-B14-qform-r2`  
**Assignment:** translations and localization  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-SUPPORTING THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval was used, but no native learned-memory ingestion is claimed.

## 1. Live target and source pins

The later owner control supersedes the stale FEI prompt. The sole target is the quadratic-form density conjecture: for independent real `X_i` with densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite bound on the density of `Q=X^TAX`, or give a valid counterexample.

Fresh control/corrections were read from `yspennstate/math-research-brain` on main during this run; owner revision remained `2026-09-22.5`. The correction inbox includes the failures of pointwise law-uniform Fresnel decay, single-cross-minor closure, conditional-cap-as-independence, absolute-value Holder/ambiguity, and bounded-diameter localization. None is used below.

Named partner consumed substantively:

- `fleet02/B14`, canonical report `yspennstate/math-open-problems@ea6b7ae2aba8b38748214a4d38f47fa6f790b8e0`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T120110Z-b14-qform-localization-r13/REPORT.md`. It proves tail-free compactification and bang-bang localization with no loss of the small-ball constant. Hence a support-independent estimate proved for finite-union indicator inputs automatically extends to arbitrary admissible densities and supports.

Quantitative predecessor consumed:

- `fleet02/B15`, canonical report `yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`. Its `QFORM-3VAR-AFFINE-PRINCIPAL-v1` gives `||p||_infinity <= (2*pi+3*sqrt(3))/kappa` for an invertible physical principal triple with `kappa=sigma_min(B)`.

This run improves the matrix dependence from `kappa^{-1}` to `(kappa |det B|)^{-1/4}` while preserving arbitrary affine drift, arbitrary support translations/fragments, and arbitrary outside couplings.

## 2. Main theorem

### `QFORM-ANISOTROPIC-PRINCIPAL-TRIPLE-v1`

Let `Y=(Y_1,Y_2,Y_3)` have independent real coordinates with probability densities bounded by one. Let `B` be an invertible real symmetric `3 x 3` matrix, set

`kappa = sigma_min(B) > 0`,  `D = |det B|`,

and let `b in R^3`, `c in R`. Then

`Z = Y^T B Y + 2 b^T Y + c`

has an essentially bounded density satisfying

`||p_Z||_infinity <= K_3 (kappa D)^(-1/4)`,

where

`K_3 = 2 sqrt(6*pi*sqrt(3)) = 11.4277536823...`.

Consequently, if an arbitrary `n x n` symmetric matrix `A` has an original-coordinate principal triple `I`, `|I|=3`, with `B=A[I,I]` invertible, then for every admissible independent product input,

`||p_{X^T A X}||_infinity <= K_3 (sigma_min(B) |det B|)^(-1/4)`.

The estimate is uniform in all couplings between `I` and its complement and in all translations/disconnected fragments of the input supports.

## 3. Exact proof

By completing the square,

`Y^T B Y + 2 b^T Y + c = (Y+B^{-1}b)^T B (Y+B^{-1}b) + c - b^T B^{-1}b`.

Coordinatewise translation preserves independence and the density cap. Thus it suffices to treat `b=c=0`. By the partner's localization theorem one may, if desired, first prove the same support-independent small-ball estimate on finite-union indicator inputs and then lift with zero constant loss; the direct argument below already uses only `F(y)=prod_i f_i(y_i)<=1` and `int F=1`.

Fix an output interval `J` of length `eta>0` and a threshold `R>0`. Split physical space into

`N_R = { y : |B y| <= R }`

and its complement.

### 3.1 Near-gradient region

Write `B=S|B|`, where `S=sign(B)` is symmetric orthogonal, and set

`z=|B|^(1/2) y`.

Then

`y^T B y = z^T S z`,  `dy = D^(-1/2) dz`,

while

`|B y|^2 = z^T |B| z >= kappa |z|^2`.

Hence `N_R` maps inside the Euclidean ball `|z|<=L`, where

`L=R/sqrt(kappa)`.

For every signature of `S` in dimension three,

`| { z : |z|<=L, z^T S z in J } | <= 2*pi*L*eta`.   (3.1)

For definite `S`, the pushforward of volume under `|z|^2` has density `2*pi*sqrt(t)<=2*pi*L`. For signature `(2,1)`, write `z=(u,s)` with `u in R^2`; for each fixed `s in [-L,L]`, the condition `|u|^2-s^2 in J` cuts planar area at most `pi*eta`, and integration over `s` gives `2*pi*L*eta`. Signature `(1,2)` follows by sign reversal.

Since `F<=1`, (3.1) yields

`P(Y in N_R, Y^T B Y in J) <= [2*pi*R/(sqrt(kappa)*sqrt(D))] eta`.   (3.2)

### 3.2 Far-gradient region

On `N_R^c`, at least one original coordinate satisfies

`|(B Y)_i| > R/sqrt(3)`.

Let

`E_i = {Y^T B Y in J, |(B Y)_i|>R/sqrt(3)}`.

Condition on the other two original independent coordinates. As a function of `t=Y_i`,

`g(t)=Y^T B Y`

is quadratic and

`g'(t)=2(BY)_i`.

On the relevant part of the line, `|g'(t)|>2R/sqrt(3)`. A quadratic has at most two monotone branches there. Each branch has preimage length at most

`eta / (2R/sqrt(3))`,

so both branches together have length at most `sqrt(3)*eta/R`. Because the conditional one-coordinate density is bounded by one,

`P(E_i | Y_hat_i) <= sqrt(3)*eta/R`.

Summing the three coordinate covers gives

`P(Y in N_R^c, Y^T B Y in J) <= [3*sqrt(3)/R] eta`.   (3.3)

### 3.3 Optimize

Combining (3.2) and (3.3),

`P(Y^T B Y in J) <= [ a R + b/R ] eta`,

with

`a=2*pi/(sqrt(kappa)*sqrt(D))`,  `b=3*sqrt(3)`.

The exact minimizer is `R=sqrt(b/a)`, giving

`min_R (aR+b/R)=2 sqrt(ab)`

`= 2 sqrt(6*pi*sqrt(3)) (kappa D)^(-1/4)`.

Therefore every interval is charged at most `K_3 (kappa D)^(-1/4)` times its length. Radon-Nikodym yields the stated `L^infinity` density bound.

For the high-dimensional corollary, condition on all coordinates outside the principal triple. The conditional polynomial is

`x_I^T B x_I + 2 b(w)^T x_I + c(w)`.

The theorem is uniform in `b(w),c(w)`, so averaging conditional laws preserves the same bound. QED.

## 4. Strict quantitative improvement over the current principal-triple theorem

Let the singular values of `B` be `s_1>=s_2>=s_3=kappa`. Then `D=s_1 s_2 kappa`, so

`(kappa D)^(-1/4) = (s_1 s_2)^(-1/4) kappa^(-1/2)`.

Thus the new estimate reads

`||p_Z||_infinity <= K_3 (s_1 s_2)^(-1/4) kappa^(-1/2)`.   (4.1)

Because `D>=kappa^3`, it always implies

`||p_Z||_infinity <= K_3/kappa`,

and `K_3=11.42775368... < 2*pi+3*sqrt(3)=11.47933772...`, so it strictly improves the predecessor even in the isotropic worst case.

More importantly, if two singular values are at least one and only the third is small, then

`||p_Z||_infinity <= K_3/sqrt(kappa)`,

improving the previous `O(kappa^{-1})` loss to `O(kappa^{-1/2})`. This is the useful anisotropic gain for localization/extraction arguments.

## 5. Translation and fragment stability

The theorem does not use support diameter, support connectivity, moments, centering, or a bounded number of fragments. Translation-generated affine terms are removed exactly by completing the square in the physical principal triple. The partner's tail-free compactification therefore transfers the estimate to arbitrary unbounded supports with the same constant.

This is compatible with the live `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE` correction: no bounded-diameter or single-interval reduction is made.

## 6. What this does and does not close

This is a genuine supporting theorem, not the full conjecture. A global three-large-eigenvalue hypothesis need not supply one physical principal triple for which `kappa*|det B|` has a dimension-free lower bound; flat/delocalized rank-three examples can make every fixed coordinate triple quantitatively small.

The first unpaid implication is therefore an aggregate extraction statement, not another local estimate:

> From the three-large-eigenvalue hypothesis, either extract a physical principal triple with dimension-free lower control of `kappa*|det B|`, **or** route the complementary delocalized mass into one of the already proved aggregate smoothers (diffuse Brascamp-Lieb, rectangular multi-pivot singular-spectrum aggregation, or hyperbolic-square aggregation) without paying reciprocal tiny minors before summation.

The present theorem improves the price of every near-nonsingular physical triple from linear to square-root sensitivity in its weakest singular direction, which enlarges the quantitative basin available to such an extraction.

## 7. Status

**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-SUPPORTING THEOREM`.

**Full QFORM target:** OPEN / NOT PROVED.

No pointwise oscillatory decay, conditional-independence substitution, fixed cross-minor universality, centered-interval localization, or universal `C=pi` claim is used.
