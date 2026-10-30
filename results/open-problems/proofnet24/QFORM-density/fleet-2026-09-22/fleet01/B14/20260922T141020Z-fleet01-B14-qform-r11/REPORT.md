# fleet01/B14 — subcritical localization closes a physical hyperbolic-square block

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner revision:** `2026-09-22.5`  
**Run:** `20260922T141020Z-fleet01-B14-qform-r11`  
**Assignment:** translations and localization  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL MATRIX BRANCH PROVED / FULL CONJECTURE OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source pins

The full target remains open: for arbitrary independent real coordinates with densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a dimension-free bound on the density of `X^T A X`.

Fresh control was read at math-research-brain commit `cc11f162b6476b407e38059370043c8661214cdd`, owner revision `2026-09-22.5`. Relevant live corrections were consumed: no law-uniform pointwise Fresnel decay, no independence after spectral rotation, no naive fiber-supremum closure, no cross-minor-alone closure, no conditional-cap substitute for genuine independence, no bounded-diameter localization, and no single-Schur-rank2 extraction.

The named partner actually applied is fleet02/B14, canonical report

`yspennstate/math-open-problems@2e0f363a166b694e6b91a8eb6dc59f1488c5cba8:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T125819Z-fleet02-B14-QFORM-r12/REPORT.md`.

That report proves (i) lossless localization to finite-fragment indicator inputs, (ii) exact median-gauge/range-affine translation equivalence, and (iii) the subcritical packing/rearrangement estimate

`int f(x) |x-a|^{-theta} dx <= 2^theta/(1-theta)`

for every probability density `0<=f<=1`, every anchor `a`, and `0<=theta<1` (first on the finite-fragment extreme class, then by its lossless localization). The present proof uses the exact case `theta=1/2`, not merely the statement that distant fragments are harmless.

## 2. A uniform L^3 theorem for products of arbitrary cap-one variables

### Lemma 2.1 — subcritical half-moment

If `f` is a probability density on `R` with `0<=f<=1`, then for every `a in R`,

`int_R f(x) / sqrt(|x-a|) dx <= M := 2 sqrt(2)`.              (2.1)

This is exactly the partner's subcritical packing/rearrangement theorem at `theta=1/2`; the extremizing measure-one set is the centered interval of radius `1/2`.

### Lemma 2.2 — product density is uniformly in L^3

Let `X,Y` be independent real random variables with probability densities `f,g<=1`. Let `H=XY`. Then `H` is absolutely continuous and its density `h` satisfies

`||h||_3^3 <= 8 M^3 + M^2`,                                  (2.2)

hence

`||h||_3 <= (8 M^3+M^2)^(1/3)`,  `M=2sqrt(2)`.                (2.3)

#### Proof

For `z!=0`, the standard product-density formula is

`h(z)=int_R f(x) g(z/x) dx/|x|`.                              (2.4)

Apply Cauchy-Schwarz with weights `|x|^{-1/2}` and `|x|^{-3/2}`:

`h(z)^2 <= A(z) B(z)`,                                       (2.5)

where

`A(z)=int f(x)g(z/x)|x|^{-1/2} dx <= M`                      (2.6)

by Lemma 2.1, and

`B(z)=int f(x)g(z/x)|x|^{-3/2} dx`.                          (2.7)

In `B`, set `y=z/x`. Since `dx=|z||y|^{-2}dy`,

`B(z)=|z|^{-1/2} int f(z/y)g(y)|y|^{-1/2}dy
     <= M |z|^{-1/2}`.                                       (2.8)

Therefore

`h(z) <= M |z|^{-1/4}`.                                      (2.9)

On `|z|<=1`,

`int h(z)^3 dz <= M^3 * 2 int_0^1 z^{-3/4}dz = 8M^3`.        (2.10)

On `|z|>1`, (2.9) gives `h<=M`, and since `int h=1`,

`int_{|z|>1} h^3 <= M^2 int h <= M^2`.                       (2.11)

This proves (2.2). No support radius, fragment count, moments, or centering enters. QED.

A useful feature is that (2.9) is obtained from a genuinely subcritical localization exponent. The critical reciprocal kernel `1/|x|`, which the partner showed can incur logarithmic fragmentation loss, never appears as a quantity to be summed by itself.

## 3. Uniform L^{3/2} theorem for one square

### Lemma 3.1

Let `Z` have density `r<=1`, and let `S=Z^2`. Then `S` has density `s` on `(0,infinity)` satisfying

`s(v) <= v^{-1/2}`,                                          (3.1)

and

`||s||_{3/2}^{3/2} <= 5`, hence `||s||_{3/2} <= 5^(2/3)`.    (3.2)

#### Proof

For `v>0`,

`s(v)=[r(sqrt(v))+r(-sqrt(v))]/[2sqrt(v)] <= v^{-1/2}`.       (3.3)

Since `int s=1`, split at one:

`int_0^1 s(v)^(3/2) dv <= int_0^1 v^{-3/4}dv =4`,            (3.4)

while on `v>=1`, (3.1) gives `s<=1`, so

`int_1^infinity s^(3/2) <= int_1^infinity s <=1`.            (3.5)

QED.

The same estimates hold for `(Z-z0)^2` for any translation `z0` because the translated coordinate density remains bounded by one.

## 4. Hyperbolic-square density theorem

### Theorem 4.1 — `QFORM-HYPERBOLIC-SQUARE-BLOCK-v1`

Let `X,Y,Z` be independent real variables with arbitrary densities bounded by one. Let `a,c` be nonzero real numbers. For arbitrary real affine coefficients `r,s,t,u`, define

`Q = 2 a X Y + c Z^2 + r X + s Y + t Z + u`.                 (4.1)

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= K_HS |a|^{-2/3}|c|^{-1/3}`,             (4.2)

where the explicit universal constant is

`K_HS = (50+800 sqrt(2))^(1/3) < 10.572`.                    (4.3)

In particular, if `|a|>=1` and `|c|>=1`, then `||p_Q||_infinity<10.572`.

#### Proof

Complete the affine terms using only coordinatewise translations:

`2aXY+rX+sY
 =2a (X+s/(2a))(Y+r/(2a)) - rs/(2a)`,                    (4.4)

`cZ^2+tZ = c(Z+t/(2c))^2 - t^2/(4c)`.                        (4.5)

The translated variables remain independent and their densities remain bounded by one. Constants only translate the output. Thus it suffices to treat

`2a X Y + c Z^2`.                                            (4.6)

Let `h` be the density of `XY` and `s` that of `Z^2`. Scaling gives

`||p_{2aXY}||_3 = (2|a|)^(-2/3) ||h||_3`,                   (4.7)

`||p_{cZ^2}||_{3/2} = |c|^(-1/3) ||s||_{3/2}`.              (4.8)

Because `XY` and `Z^2` are independent, the density of their sum is the convolution. Holder/Young with conjugate exponents `3` and `3/2` yields

`||p_Q||_infinity
 <= ||p_{2aXY}||_3 ||p_{cZ^2}||_{3/2}`                      (4.9)

` <= (2|a|)^(-2/3) (8M^3+M^2)^(1/3)
      |c|^(-1/3) 5^(2/3)`.                                  (4.10)

With `M=2sqrt(2)`, cubing the coefficient independent of `a,c` gives

`[2^(-2/3)(8M^3+M^2)^(1/3)5^(2/3)]^3
 = 50+800sqrt(2)`.                                           (4.11)

This proves (4.2)-(4.3). The sign of `c` is irrelevant because reflection of a density preserves every L^p norm. QED.

## 5. Target-level original-coordinate matrix branch

### Corollary 5.1

Let `A` be any real symmetric `n x n` matrix. Suppose there are three ORIGINAL coordinates `(i,j,k)` for which the principal block, after ordering those coordinates, is

`B = [[0,a,0],[a,0,0],[0,0,c]]`,                             (5.1)

with `a c !=0`. No restriction is placed on any entries coupling these coordinates to the other `n-3` coordinates, nor on the outside self block.

Then for every independent cap-one input law,

`||p_{X^T A X}||_infinity
 <= K_HS |a|^(-2/3)|c|^(-1/3)`.                              (5.2)

#### Proof

Condition on every coordinate outside `{i,j,k}`. The selected three coordinates remain independent with their original cap-one densities. All outside couplings become affine terms `rX_i+sX_j+tX_k+u` in the conditional polynomial, while its quadratic selected block remains exactly (5.1). Theorem 4.1 is uniform in those affine coefficients, hence gives (5.2) on every conditional fiber. Averaging the conditional measures preserves domination by the same constant times Lebesgue measure. QED.

If `|a|,|c|>=1`, block (5.1) itself has three eigenvalues `a,-a,c` of absolute value at least one, and (5.2) gives the explicit target-level bound `<10.572` even though the selected quadratic block is indefinite and the hyperbolic pair alone has a logarithmic singularity.

This is qualitatively different from the previously proved definite-pair branch: it closes a genuine `(+,-,+)` / `(+,-,-)` physical block by combining a logarithmically singular hyperbolic product with one square through the `L^3-L^{3/2}` convolution mechanism.

## 6. Why the route respects the live corrections

1. **No rotation:** all variables in the proof are original independent coordinates.
2. **No pointwise Fresnel decay:** the argument is purely real-variable small-ball/density analysis.
3. **No cross-minor-alone claim:** the hyperbolic pair `2aXY` is not claimed bounded in density; the independent square is essential.
4. **No conditional-cap substitute:** only conditioning on outside original independent coordinates is used. The selected three remain genuinely independent; no transformed conditional variables are asserted independent.
5. **No bounded-support or moment assumption:** the partner's subcritical localization theorem supplies (2.1) uniformly over arbitrary fragments and tails, and the proof thereafter uses only density caps and total mass one.
6. **No universal-pi claim:** the explicit branch constant is about `10.5714`, and the known global lower bound above `pi` is not contradicted.

## 7. What moved and what remains

**New proved movement:** the exact original-coordinate hyperbolic-square branch (5.1) now has a dimension-free arbitrary-law density bound with a fully explicit constant. The proof also supplies a reusable analytic module:

`cap-one X,Y  =>  density(XY) uniformly in L^3`,              (7.1)

obtained precisely by paying the partner's subcritical `theta=1/2` localization credit instead of a critical reciprocal-distance sum.

**Full target status:** OPEN. Three large spectral eigenvalues do not force one physical principal block of form (5.1), just as they do not force a uniformly nondegenerate definite pair or principal triple. General `3x3` blocks may contain `X_i^2`, `X_j^2`, `X_iX_k`, and `X_jX_k` terms that cannot be removed by coordinatewise translations without mixing the independent inputs.

The next concrete B14 implication is therefore:

> Determine whether the `L^3-L^{3/2}` mechanism survives a strictly larger original-coordinate indefinite block class, for example `2aXY+bY^2+cZ^2` or a block with one additional `XZ/YZ` coupling, while retaining genuine product provenance. A proof must not use a shear as though it preserved independence. Alternatively, combine this branch with a source-valid matrix decomposition that guarantees either a diffuse-range theorem, a definite physical pair/triple, or a hyperbolic-square block.

This report proves a target-level matrix branch, not the unrestricted three-eigenvalue theorem.
