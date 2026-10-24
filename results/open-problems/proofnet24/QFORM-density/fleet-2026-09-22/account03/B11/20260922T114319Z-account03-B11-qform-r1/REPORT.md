# account03/B11 — bilinear Abel smoothing for rotated indefinite triples

Programme: `QFORM-DENSITY-3EIG-20260922`  
Control revision: `2026-09-22.5`  
Run: `20260922T114319Z-account03-B11-qform-r1`  
Status: **ESSENTIAL_SUPPORTING_LEMMA / FULL CONJECTURE OPEN**  
Brain status: **WITHOUT_VERIFIED_BRAIN**

## Fresh task resolution

The live QFORM order supersedes the stale FEI automation label. The exact B11 task is to develop a uniform argument for genuinely rotated signatures `(+, +, -)` and `(+, -, -)`, retain the opposite-sign rank-two logarithmic control, and identify quantitatively how a third direction removes that singularity.

At the fresh control snapshot there was no completed `account04/B11` QFORM handoff. I therefore did not invent partner mathematics. I consumed the closest available same-programme geometric peer result, `account04/B18` (handoff blob `688ac8022c47f7649236b02e2d6c3624d8f9801a`): its Schur-pivot lemma proves that a minority-sign diagonal pivot plus a definite Schur complement gives

`||p_Q||_infinity <= 2 sqrt(pi) / |a det B|^(1/4)`.

The result below attacks a complementary, genuinely rotated saddle branch in which the dangerous rank-two piece is not bounded-density by itself.

## Main lemma: a third square direction Abel-smooths a physical saddle

Let `X,Y,Z` be independent real random variables with probability densities bounded by `1`. Let

`R(X,Y) = 2 b X Y + d Y^2 + alpha X + beta Y + gamma`,

where `b != 0`, and let

`S(Z) = c Z^2 + eta Z + theta`,

where `c != 0`. Then `R+S` has an essentially bounded density and

`||p_{R+S}||_infinity <= 4 / sqrt(|b c|)`.

The same bound remains valid after adding any independent random variable, and therefore after conditioning all coordinates outside a physical principal triple whose quadratic compression, up to a coordinate permutation, is

```
B = [[0, b, 0],
     [b, d, 0],
     [0, 0, c]].
```

Cross terms from those three coordinates to the conditioned outside coordinates only create affine terms and are already covered by the statement.

### Step 1: exact one-dimensional half-potential bound

If `f` is a probability density with `0 <= f <= 1`, then for every `a != 0` and every real `r`,

`integral f(x) (r-a x)_+^(-1/2) dx <= 2 / sqrt(|a|)`.

Indeed the kernel is supported on one side of its singular point and decreases with distance from that point. Among densities bounded by `1` with total mass `1`, the integral is maximized by putting unit density on the adjacent interval of length `1`; its integral is `2/sqrt(|a|)`.

Also, for every density `g <= 1` of mass `1`,

`integral g(y) |y-y0|^(-1/2) dy <= 2 sqrt(2)`.

This is the symmetric decreasing rearrangement bound, attained by the unit interval centered at `y0`.

### Step 2: the rank-two saddle has a uniformly bounded half-order potential

Translate `Y` by `alpha/(2b)`. Translation preserves the density bound and independence. Conditional on the translated value `V=v`, `R` is affine in `X` with slope `2 b v`; every remaining term is only a deterministic shift. Hence for either choice of sign,

`E[(t-R)_+^(-1/2) | V=v] <= 2 / sqrt(2 |b v|)`.

Averaging in `v` and using the preceding symmetric rearrangement estimate gives

`sup_t E[(t-R)_+^(-1/2)] <= 4 / sqrt(|b|)`

and, by reversing sign,

`sup_t E[(R-t)_+^(-1/2)] <= 4 / sqrt(|b|)`.

This is the key quantitative statement. It does **not** assert that the rank-two saddle has bounded density; it asserts exactly the half-order integrability needed by the third square direction.

### Step 3: square-root kernel from the third independent coordinate

Complete the square in `Z`:

`S(Z) = c (Z-z0)^2 + const`.

For any density of `Z` bounded by `1`, the density of `c(Z-z0)^2` is pointwise bounded by

`1 / sqrt(|c| |s|)`

on the half-line having the sign of `c`, and is zero on the other half-line. Therefore, using independence and the two half-potential bounds above,

`p_{R+S}(t)
 <= |c|^(-1/2) E[(sgn(c)(t-R))_+^(-1/2)]
 <= 4 / sqrt(|b c|)`.

This proves the lemma. Adding an independent remainder is convolution with a probability measure and cannot increase the `L-infinity` norm.

## Corollary: a canonical genuinely rotated signature has a universal constant 4

Suppose a physical 3x3 principal block has the displayed form and all three eigenvalues of that block have absolute value at least `1`. Its saddle 2x2 block has determinant `-b^2`, so the product of the absolute values of its two eigenvalues is `b^2`; hence `|b| >= 1`. The third eigenvalue is `c`, so `|c| >= 1`. Consequently

`||p_Q||_infinity <= 4`.

For `c>0` this block has inertia `(2,1)`; for `c<0` it has inertia `(1,2)`. Thus this is a genuinely rotated indefinite three-direction theorem, not a diagonal same-sign reduction.

## Mandatory rank-two logarithmic control

The third direction is genuinely doing work. Take `d=alpha=beta=gamma=0` and let `X,Y` be independent uniforms on `[-1/2,1/2]`. For

`R=2bXY`,

its density is

`p_R(s) = (1/|b|) log(|b|/(2|s|))`,  for `0<|s|<|b|/2`,

so `p_R(s)` diverges logarithmically at `0`. Thus no bounded-density theorem is available from the opposite-sign rank-two saddle alone. The third square contributes the Abel kernel `|u|^(-1/2)`, and Step 2 proves that the logarithmic saddle is uniformly integrable against precisely that kernel, even for arbitrary independent input densities bounded by `1`.

## Relation to account04/B18 and remaining gap

`account04/B18` covers the branch where a physical diagonal pivot has the minority sign and the corresponding Schur complement is definite. The present result covers a complementary zero-diagonal physical saddle branch, including the canonical rotated matrix

```
[[0,b,0],
 [b,d,0],
 [0,0,c]].
```

The full conjecture is **not** proved. The first remaining B11 implication is to remove the exact saddle-axis structure: handle fully coupled inertia `(2,1)/(1,2)` triples whose dangerous saddle pair has nonzero diagonal perturbations and/or couplings to the third coordinate, while retaining a dimension-free constant; after that, one still needs the aggregate-minor passage for delocalized spectral triples. The account02/B15 Hadamard-projector example shows why selecting one well-conditioned principal triple cannot by itself close the high-dimensional target.

No pointwise Fresnel decay, rotation-induced independence, raw fiber-supremum bound, or unsupported continuity claim is used here.
