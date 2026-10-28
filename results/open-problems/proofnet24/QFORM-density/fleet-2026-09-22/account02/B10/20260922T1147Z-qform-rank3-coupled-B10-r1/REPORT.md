# account02/B10 — rank-three coupled case: hyperbolic-square smoothing and Plucker-average obstruction

**Run:** `20260922T1147Z-qform-rank3-coupled-B10-r1`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** account02/B10, `Rank-three coupled case` / GEOMETRY  
**Classification:** `ESSENTIAL_STEP_APPLIED` plus local `CANDIDATE_REFUTED`; full target **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval was authenticated, but no native learned-memory ingestion/receiver was verified.

## 0. Control pivot and source pins

The stale FEI prompt was superseded by the later owner control in `yspennstate/math-research-brain`: all eighty workers now work only on the quadratic-form density conjecture. The live target is:

> For independent real `X_i` with densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^T A X` has a density with one universal `L^infinity` bound, or give a genuine counterexample.


- `QFORM-POINTWISE-DECAY-FALSE` — arbitrary bounded densities can be phase-aligned, so law-uniform pointwise quadratic Fourier decay is false;
- `QFORM-FIBER-SUP-DIMENSION-LOSS` — unrestricted spectral-fiber suprema can lose dimension;
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` — diagonalizing `A` does not preserve independence.

The live correction inbox was empty at the source snapshot.

Named partner `account03/B10`: no completed current-programme canonical report or handoff was present at fresh path/commit queries, so no partner result is fabricated.

Completed sources actually consumed and applied:

1. **account03/B16**, brain report blob `07109b1e3a16125ab7965e557a73c58e44d10715` (`scheduled_tasks/runs/account03/B16/20260922T113226Z-qform-r11/report.md`). It proves the exact single-square density formula and `L^{3/2}` bound, and independently refutes the invalid pointwise-Fresnel route.
2. **account01/B05**, math-open-problems report blob `09383b90fdc49dcb3479c4ea6ede0b58994bfd8b` (`qform/fleet-2026-09-22/account01/B05/20260922T1136Z-qform-principal2d-B05-r1/REPORT.md`). It proves the physical definite-pair shell bound `pi/sqrt(|det B|)` and records the flat-Walsh localization obstruction.
3. **account02/B06**, report blob `9cced3d58d10574ef548c119c8d5a67276dc870f`, which proves the Plucker determinant-mass identity `sum_{i<j} det(R_{ij})^2=1` for a same-sign spectral plane.
4. **account02/B08**, report blob `212febc02c4c1f3a8e6c073d0a8ed5d2d6b4ea0`, which proves the exact rank-three diffuse-frame theorem `max_i ||u_i||^2<=1/2 => ||p_Q||_infinity<=3e` and isolates the heavy/light branch.

The present result attacks that coupled heavy/local branch without assuming a definite physical pair.

## 1. Compact conditional end-to-end route

For rank exactly three, account02/B08 already closes every frame whose row leverages are at most `1/2`, with universal constant `3e`. Thus the rank-three residual is a genuinely heavy/light geometry.

A physical definite pair closes by account01/B05. The first question is therefore whether an **indefinite coupled triple** can itself supply a dimension-free local smoother without diagonalizing the independent variables.

The new theorem below answers yes for a triangular hyperbolic-square triple. It includes the canonical target form

`Q=2XY+Z^2`,

whose matrix has eigenvalues `1,-1,1`, hence meets the sharp three-large-eigenvalue threshold but has an indefinite `(X,Y)` block. The proof keeps the original coordinate product law and all conditional shifts exactly.

After that positive result, Section 4 tests the natural attempt to average local reciprocal-determinant constants with the B06 Plucker weights. The flat Walsh plane makes that average grow like `n/2`, so determinant mass by itself is not enough: aggregation must occur before the reciprocal local constant is paid.

## 2. Two sharp one-dimensional rearrangement bounds

### Lemma 2.1 — one-sided affine square-root kernel

If `f` is a probability density with `0<=f<=1`, `m!=0`, and `s` is arbitrary, then

`int_R f(x) (s-mx)_+^{-1/2} dx <= 2/sqrt(|m|)`.

The same bound holds with `(mx-s)_+^{-1/2}`.

**Proof.** Translate/reflect so the singularity is at `0` and the positive half-line is used. The kernel is `( |m| x )^{-1/2}` on one side and zero on the other. Under the constraints `0<=f<=1`, `int f=1`, the bathtub principle maximizes its integral by filling the unit interval adjacent to the singularity. Hence

`int_0^1 (|m|x)^(-1/2) dx = 2/sqrt(|m|)`. `QED`

### Lemma 2.2 — centered inverse-square-root kernel

If `g` is a probability density with `0<=g<=1`, then for every `y0`,

`int_R g(y) |y-y0|^{-1/2} dy <= 2 sqrt(2)`.

**Proof.** The decreasing rearrangement of `|y-y0|^{-1/2}` is maximized by occupying the centered interval of length one. Thus

`int_{-1/2}^{1/2} |u|^{-1/2}du = 2 sqrt(2)`. `QED`

Both inequalities are exact source-law statements; disconnected supports do not evade them.

## 3. Main theorem: hyperbolic-square smoothing with constant 4

### Theorem 3.1 — `QFORM-HYPERBOLIC-SQUARE-v1`

Let `X,Y,Z` be independent real random variables with probability densities at most `1`. Let `a,b` be nonzero reals. Let `H:R->R` and `theta:R->R` be arbitrary measurable functions. Then

`T = 2 a X Y + H(Y) + b ( Z + theta(Y) )^2`

has a density satisfying

`||p_T||_infinity <= 4 / sqrt(|a b|)`.

No continuity, moments, support connectedness, centering, sign restriction, or smoothness of `H,theta` is assumed.

### Proof

Fix `x,y`. Since translation does not change the pointwise density bound of `Z`, the conditional law

`V_y=b(Z+theta(y))^2`

has density

`k_y(v) = [ f_Z(-theta(y)+sqrt(v/b)) + f_Z(-theta(y)-sqrt(v/b)) ] / (2 sqrt(|b v|))`

on the sign-compatible half-line (with the obvious interpretation for `b<0`). Therefore, using `f_Z<=1`,

`k_y(v) <= 1/(sqrt(|b|) sqrt(|v|))`

on that half-line.

Consequently a version of the density of `T` obeys, for every `t`,

`p_T(t)`
`<= |b|^{-1/2} int int f_X(x) f_Y(y)`
`       * [ sigma ( t-H(y)-2a x y ) ]_+^{-1/2} dx dy`,

where `sigma=sign(b)`.

For each fixed `y!=0`, the denominator is a one-sided affine square-root singularity in `x` with slope magnitude `2|a y|`. Lemma 2.1 gives

`int f_X(x) [ sigma(t-H(y)-2a x y) ]_+^{-1/2} dx`
`<= 2/sqrt(2|a y|) = sqrt(2/(|a||y|))`.

(The set `y=0` is Lebesgue-null and may be ignored.) Hence

`p_T(t) <= sqrt(2)/(sqrt(|ab|)) int f_Y(y)|y|^{-1/2}dy`.

Lemma 2.2 yields

`p_T(t) <= sqrt(2)/(sqrt(|ab|)) * 2 sqrt(2)`
`= 4/sqrt(|ab|)`.

The bound is uniform in `t`, and the displayed conditional-density construction also proves absolute continuity. `QED`

### Corollary 3.2 — physical triangular triple in an arbitrary ambient form

Let `Q=X^TAX` with independent coordinate densities at most `1`. Suppose distinct physical coordinates `i,j,k` satisfy, after a permutation,

`A_ii=0`, `A_ik=0`, `a=A_ij!=0`, `b=A_kk!=0`.

The entries `A_jj` and `A_jk` may be arbitrary, and all couplings from `{i,j,k}` to the remaining coordinates may be arbitrary. Then

`||p_Q||_infinity <= 4/sqrt(|A_ij A_kk|)`.

In particular `|A_ij A_kk|>=1` gives the universal bound `4`.

**Derivation.** Condition on all outside coordinates. The conditional polynomial in `(x,y,z)=(X_i,X_j,X_k)` is

`2a xy + c y^2 + 2d yz + b z^2 + alpha x + beta y + gamma z + C`.

Translate `y` by `alpha/(2a)` to remove the `x`-linear term. Then complete the square in `z`; this produces exactly the form in Theorem 3.1 with some measurable (indeed quadratic) `H(y)` and affine `theta(y)`. The bound is uniform in the conditioned outside vector, so averaging preserves it.

### Canonical coupled target case

For

`Q=2XY+Z^2`,

the matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are `1,-1,1`. Therefore this is an exact rank-three indefinite target case, not a two-eigenvalue surrogate, and Theorem 3.1 gives

`||p_Q||_infinity <= 4`.

This case is not covered by the account01/B05 *definite `(X,Y)` pair* mechanism: the `(X,Y)` block is hyperbolic. The new proof shows explicitly how the third square pays the logarithmic singularity of the opposite-sign rank-two hyperbolic factor while keeping the original independent coordinates.

## 4. Genuine falsifier of naive Plucker-weighted local averaging

Account02/B06 supplies the exact same-sign spectral-plane weights

`w_ij = det(R_{ij})^2`,  `sum_{i<j} w_ij=1`.

A tempting repair of the delocalized case is to prove a local pair bound proportional to `w_ij^{-1/2}` and average it with the natural probability weights `w_ij`. That incurs

`sum w_ij * w_ij^{-1/2} = sum sqrt(w_ij)`.

The flat Walsh plane shows this is dimensionally fatal.

Take

`r_1=(1,...,1)/sqrt(n)`,

`r_2=(s_1,...,s_n)/sqrt(n)`,

where exactly `n/2` of the signs `s_i` are `+1` and `n/2` are `-1`. Then

`det(R_{ij})=(s_j-s_i)/n`.

Hence

- `w_ij=4/n^2` exactly for cross-sign pairs;
- `w_ij=0` otherwise;
- there are exactly `n^2/4` nonzero weights;
- `sum w_ij=1`, as Cauchy--Binet requires;
- but

`sum sqrt(w_ij) = (n^2/4)*(2/n)=n/2`.

Therefore a linear Plucker-weight average of reciprocal-square-root local constants loses a factor `n/2`. In the account01/B05 ellipse normalization the corresponding averaged shell constant is `pi n/2`.

This is a **source-valid counterexample to the naive aggregation rule**, not to the quadratic-form conjecture and not to B06's determinant-mass identity. It sharpens the unpaid implication: one must aggregate the product amplitude / oscillatory or coarea operator **before** paying any `w^{-1/2}` (or analogous reciprocal-minor) local constant.

The included exact checker confirms for `n=8,16,32,64` that the nonzero count is `n^2/4`, total determinant mass is exactly `1`, and `sum sqrt(w)=n/2`; the proof above is arbitrary-dimensional.

## 5. How this applies the current peer state

- **account03/B16 applied:** its exact square-density formula is the outer smoothing kernel used in Theorem 3.1, but here it is coupled to a hyperbolic product and paid by two sharp rearrangement inequalities rather than a false pointwise Fourier decay.
- **account01/B05 applied:** its definite physical-pair theorem is one localized closure branch; Theorem 3.1 supplies a complementary *indefinite* triangular triple branch with no condition-number dependence on `A_jj,A_jk`.
- **account02/B08 applied:** rank-three frames with all leverage scores `<=1/2` are already closed with `C=3e`; the present theorem enlarges the physical-space side of the remaining heavy/light branch.
- **account02/B06 tested:** the Plucker determinant-mass invariant is correct, but naive linear averaging of local reciprocal-minor constants is now decisively ruled out by the exact Walsh calculation.

A useful feature of Corollary 3.2 is that its `3x3` principal block has determinant `-A_ij^2 A_kk`, yet the bound depends only on `sqrt(|A_ij A_kk|)` and is completely insensitive to arbitrarily large `A_jj,A_jk`. Thus it can remain uniform even when the principal block has very poor condition number, a regime where a smallest-singular-value localization bound may be weak.

## 6. First essential missing implication

The rank-three diffuse branch is no longer the missing step. The remaining exact rank-three obstruction is:

### `QFORM-RANK3-HYBRID-HEAVY-LIGHT-v2`

Assume some spectral-frame row has leverage `>1/2`, but no physical definite pair with dimension-free determinant and no triangular hyperbolic-square triple with dimension-free `|A_ij A_kk|` is available. Prove a dimension-free small-ball/density estimate by coupling the finitely many leverage-heavy physical rows to the residual diffuse frame **before** any reciprocal coordinate minor is paid.

The Plucker calculation in Section 4 rules out solving this by a linear average of local bounds. The next viable mechanism must be an operator-level/nonlinear aggregation (for example a capped Brascamp--Lieb decomposition coupled to a physical-space kernel) that keeps the original product amplitude active.

After rank exactly three is closed, the separate full-target issue remains: arbitrary additional nonzero eigenvalues of magnitude below `1` are not independent noise after spectral rotation.

## 7. Status

- Full quadratic-form conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- `QFORM-HYPERBOLIC-SQUARE-v1`: **PROVED supporting theorem**.
- Canonical coupled target `2XY+Z^2`: **PROVED with `C=4`** for arbitrary independent input densities `<=1`.
- Physical triangular triple Corollary 3.2: **PROVED** with `4/sqrt(|A_ijA_kk|)`.
- Naive Plucker-weighted averaging of reciprocal-square-root local constants: **CANDIDATE_REFUTED** by the exact flat-Walsh family.
- Rank-three heavy/light hybrid and the general target: **OPEN**.

No finite census is used as closure. No projected coordinates are assumed independent. No refuted pointwise oscillatory estimate is used.
