# fleet03/B14 — countable localization skeleton for quadratic-form density

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `fleet03-B14-20260922T113509Z-69b5c0c6`  
**Assignment:** translations and localization  
**Status:** `TARGET_LEVEL_REDUCTION / FULL_CONJECTURE OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Live target and corrections

The live owner order supersedes the earlier FEI assignment. The target is: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^T A X` has an essentially bounded density with one universal dimension- and law-independent constant.

This report retains the current corrections: law-uniform pointwise stationary-phase decay is false for arbitrary disconnected densities; rotating to the eigenbasis does not preserve independence; and naive spectral-fiber suprema can lose dimension. Nothing below uses those retired shortcuts.

## 2. Named partner result consumed

I use the completed fleet04/B14 result

`fleet04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1`

whose canonical report is `yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`, blob `30ebe93170ba26fb57dc128ee0116762de1d9f26`.

That report proves two target-level reductions with **no loss in the optimal constant**:

1. for each fixed small-ball interval, the coordinatewise bathtub principle reduces arbitrary densities `0<=f_i<=1`, `int f_i=1`, to indicator densities `1_{E_i}` with `|E_i|=1`;
2. each measurable measure-one set can be approximated in total variation by a compact finite union of intervals of total length one.

Hence the full density problem is equivalent to the same problem for product uniforms on compact finite interval unions, with arbitrary locations, diameters, fragment counts and separations.

The new step below makes this localization **countable and quantitative**, while keeping the exact same best constant. This is useful for rigorous finite-resolution certificates and for falsification searches: no exotic unbounded or noncomputable input law is needed to witness failure of a universal constant.

## 3. Direct no-moment compactification lemma

Before the countable reduction, there is a simple constructive tail lemma that is useful independently of the bathtub argument.

### Lemma 1 — trim and refill without renormalization

Let `f` be any probability density on `R` with `0<=f<=1`. There are compactly supported probability densities `g_R` with `0<=g_R<=1` and

`||g_R-f||_1 -> 0`.

### Proof

Let

`m_R=int_{[-R,R]} f`, `delta_R=1-m_R`.

Choose any bounded interval `J_R` disjoint from `[-R,R]` and of length `delta_R`, and define

`g_R = f 1_{[-R,R]} + 1_{J_R}`.

Then `0<=g_R<=1`, `int g_R=m_R+delta_R=1`, and `g_R` has bounded support. Moreover

`||g_R-f||_1 <= int_{R\[-R,R]} f + |J_R| = 2 delta_R ->0`.

No normalization factor, moment bound, centering or connected-support assumption is introduced. QED.

For finitely many coordinates, the product-density estimate

`|| prod_i f_i - prod_i g_i ||_1 <= sum_i ||f_i-g_i||_1`

follows by telescoping. Pushforward under any measurable map contracts total variation. Consequently a universal output-density constant proved for compactly supported admissible inputs automatically extends to arbitrary supports with **exactly the same constant**.

## 4. Dyadic finite-fragment approximation with an explicit error

For `m>=0`, call a set a **level-m dyadic unit set** if

`D = union_{k in S} [k 2^{-m}, (k+1)2^{-m})`

for a finite `S subset Z` with exactly `2^m` elements. Every such `D` has Lebesgue measure exactly one. Locations of the cells are unrestricted.

### Lemma 2 — finite unions reduce to equal-width dyadic cells

Let `E` be a compact union of `r` disjoint bounded intervals with `|E|=1`. For every sufficiently fine dyadic level `m`, there is a level-m dyadic unit set `D_m` such that

`|E triangle D_m| <= 2 r 2^{-m}`.

### Proof

Partition `R` into level-m dyadic cells. Cells that do not meet the boundary of `E` are either wholly inside or wholly outside `E`. At most `2r` cells meet the `2r` interval endpoints.

Let `N_full` be the number of cells wholly contained in `E`. Since `|E|=1`, in units of a cell length the total occupancy is exactly `2^m`. Hence

`N_full <= 2^m <= N_full + N_boundary`.

Take every full cell and choose exactly `2^m-N_full` of the boundary cells. The resulting union has exactly `2^m` cells and therefore measure one. The symmetric difference is contained entirely in the boundary cells, whose total length is at most `2r 2^{-m}`. QED.

Thus finite-fragment product laws can be approximated in total variation by product laws supported on equal-width dyadic cells, and the approximation error is explicit:

`d_TV( tensor_i 1_{E_i} dx, tensor_i 1_{D_i} dx ) <= (1/2) sum_i |E_i triangle D_i|`.

## 5. Main theorem — a countable skeleton has exactly the same best constant

For a real symmetric matrix `A`, let `s_3(A)` be its third largest singular value, equivalently the third largest absolute eigenvalue. Define the **dyadic-rational skeleton** to consist of instances with:

- finite `n`;
- each input density equal to `1_{D_i}` for a level-`m_i` dyadic unit set `D_i` as above;
- `A` a symmetric matrix with rational entries and `s_3(A)>=1`;
- the test interval `I=(a,b)` with rational endpoints `a<b`.

Let `C_full` be the optimal small-ball/density constant for the full conjecture and `C_skel` the supremum of

`P(X^T A X in I)/|I|`

over the dyadic-rational skeleton.

### Theorem 3

`C_full = C_skel` (with the value `+infinity` allowed).

In particular, the full conjecture is true with a constant `C` **iff** every skeleton instance satisfies

`P(X^T A X in I) <= C |I|`.

### Proof

The inequality `C_skel<=C_full` is immediate because every skeleton instance is admissible for the full problem.

For the reverse implication, assume every skeleton instance obeys the bound with some finite `C`. By the fleet04/B14 partner theorem, it is enough to prove the same bound for inputs `1_{E_i}` where each `E_i` is a compact finite union of intervals of measure one.

Fix such an instance `(n,A,E_1,...,E_n,I)` and an arbitrary error tolerance. By Lemma 2 choose dyadic unit sets `D_i` so close that the product total-variation error is at most `eta`. Therefore

`P_E(Q_A in I) <= P_D(Q_A in I) + eta`.

The product support `K=prod_i D_i` is compact. Put

`R_K^2 = sup_{x in K} ||x||_2^2 < infinity`.

Choose `delta>0`. Since rational symmetric matrices are dense, first replace `A` by `(1+delta)A`, whose third singular value is at least `1+delta`, and then choose a rational symmetric matrix `B` so close to `(1+delta)A` that

`s_3(B)>=1`

and

`||B-A||_op R_K^2 <= rho`,

where `rho>0` can be made arbitrarily small by taking `delta` and the rational approximation error small. Weyl's singular-value inequality gives the spectral condition.

For every `x in K`,

`|x^T B x - x^T A x| <= ||B-A||_op ||x||_2^2 <= rho`.

Hence, pointwise on the product support,

`{x: x^T A x in I} subset {x: x^T B x in I^{+rho}}`,

where `I^{+rho}` is obtained by expanding both endpoints by `rho`. Choose a rational-endpoint interval `J` containing `I^{+rho}` with

`|J| <= |I| + 2 rho + tau`

for arbitrary `tau>0`. The skeleton hypothesis gives

`P_D(Q_B in J) <= C |J|`.

Combining,

`P_E(Q_A in I) <= C(|I|+2rho+tau)+eta`.

Let the dyadic mesh tend to zero and then `rho,tau ->0`. This gives

`P_E(Q_A in I) <= C|I|`.

The partner reduction then transfers the same inequality, without any constant loss, to all independent densities bounded by one. The interval characterization gives an essentially bounded output density with norm at most `C`. Thus `C_full<=C_skel`, proving equality. QED.

## 6. Consequences

### Corollary 4 — counterexamples can be taken from a countable class

If the full conjecture is false in the sense that no finite universal density constant exists, then for every `M<infinity` there is a dyadic-rational skeleton instance with

`P(X^T A X in I) > M |I|`.

Thus a genuine counterfamily never needs a pathological noncompact density, a fractal support, irrational interval endpoints, or an irrational matrix. It may be chosen from a countable family of finite data.

This does **not** make the conjecture a finite verification problem: `n`, dyadic resolutions, cell locations, fragment counts encoded by the selected cells, rational matrix heights, and interval scales remain unbounded.

### Corollary 5 — what a rigorous computation may legitimately certify

A computation on a bounded range of `n`, mesh, locations or matrix heights certifies only that bounded subclass. A proof that establishes one constant uniformly over the entire countable skeleton, however, automatically proves the full essentially-bounded-density statement with the identical constant.

### Corollary 6 — arbitrary translations and distant fragments remain genuinely live

The skeleton leaves the integer cell indices completely unrestricted. Therefore the reduction removes unbounded *individual* supports and infinitely fragmented laws as separate analytic issues, but it does **not** smuggle in a diameter, moment, centering or separation bound. Any successful estimate must remain uniform as the selected dyadic cells move arbitrarily far apart.

## 7. Continuity caveat

The reduction above concerns the target-level `L^infinity`/small-ball assertion. Total-variation approximation plus a uniform `L^infinity` bound does not by itself produce a continuous representative in the limit. The owner's stronger continuity request therefore remains a separate regularity step unless a uniform modulus or another continuity mechanism is proved.

## 8. First unpaid implication

After this localization, the remaining obstacle is not tails or nonmeasurable law complexity. It is a uniform geometric estimate on a completely explicit class:

> product uniforms on finitely many equal-width dyadic cells of total length one in each coordinate, rational symmetric `A` with `s_3(A)>=1`, and rational test intervals.

The matrix/law parameters remain unbounded. The fleet02/B06 Hadamard construction shows why one cannot close this by extracting a single bounded-size physical coordinate block: curvature can be spectrally large but coordinatewise delocalized. A successful next step must aggregate distributed curvature/minors or supply an averaged small-ball/Fourier mechanism that survives arbitrary dyadic fragment locations.

## Classification

- full quadratic-form conjecture: **OPEN / NOT PROVED**;
- fleet04/B14 extreme-product + compact finite-fragment reduction: **CONSUMED, PROVED SOURCE INPUT**;
- trim-and-refill compactification: **PROVED**;
- dyadic unit-set approximation with explicit error: **PROVED**;
- exact countable dyadic-rational skeleton equivalence: **PROVED TARGET-LEVEL REDUCTION**;
- continuity for the full target: **OPEN**.
