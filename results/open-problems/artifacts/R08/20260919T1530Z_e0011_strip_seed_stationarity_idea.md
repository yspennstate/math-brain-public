# R08 E0011 — idea before checker code: cardinality obstruction, thin-strip restart geometry, and stationary compactification

Methods this run: **B4 / B23 / B29**.

Entering certified metric: `B_cat >= b21_desc`, with previous diagnostic `log10(b21_desc) ~= -48.42893853604687`; supported unchanged count entering this run is `1`.

## B4 — prove a weaker architecture theorem completely

The preceding run proved that every **rectangular** bare vacancy seed of area at most 14 has an unavoidable all-CO poisoning channel of probability at least `1/64`. The rectangle restriction is artificial. For any finite initially vacant set `A` in an all-CO exterior at `p=1/2`, first-event conditioning gives

`q(A)=2/(2|A|+e(A)) * sum_{v in A} q(A\{v})`, `q(empty)=1`,

where `e(A)` is the number of nearest-neighbour edges induced by `A`.

A purely combinatorial recursion should lower-bound `q(A)` using only `n=|A|` and `e=e(A)`. On the square lattice,

`e(A) <= m(n) := 2n-ceil(2 sqrt(n))`,

because if `A` occupies `r` rows and `c` columns then horizontal edges are at most `n-r`, vertical edges at most `n-c`, and `r+c >= ceil(2 sqrt(n))`.

If `d_v` is the induced degree of `v`, then `e(A\{v})=e-d_v`, `0<=d_v<=4`, and `sum_v d_v=2e`. Therefore define an exact lower envelope `L(n,e)` recursively by minimizing over **all** integer degree sequences satisfying only these necessary constraints (allowing impossible sequences only makes the lower bound weaker, hence safe):

`L(0,0)=1`,

`L(n,e)=2/(2n+e) * min_{d_1+...+d_n=2e, 0<=d_i<=4, 0<=e-d_i<=m(n-1)} sum_i L(n-1,e-d_i)`.

Induction should then give `q(A)>=L(n,e(A))`. If `L(n,m(n))>1/64` for every `n<=14`, then **no bare all-vacant seed of at most 14 sites, of any geometry, can support a universal good-block probability >63/64**. This would make the previous rectangular area-15 threshold cardinality-sharp for the direct all-CO obstruction, because the explicit 3x5 set of size 15 already has `q<1/64`.

## B23 — do the opposite of the compact-seed instinct

The smallest poison-escaping rectangle, 3x5, is compact, but compactness may be dynamically bad. Evaluate the initial vacancy-number drift for a fully vacant `h x w` rectangle in an all-CO exterior.

At `p=1/2`, each CO arrival changes the vacancy count by `-1`. For an O2 arrival on an internal vacant edge, an endpoint on the rectangle boundary has an outside CO neighbour, so the incoming oxygen reacts and contributes `+1` to the vacancy count; an interior endpoint has no CO neighbour initially and survives, contributing `-1`.

For `h,w>=3`, summing endpoint signs over internal edges gives

`L V = -(3/2) h w + (7/2)(h+w) - 8`.

For a `2 x w` strip there are no interior vertices and

`L V = w/2 - 1`.

Thus among rectangles with both sides at least 2, positive initial vacancy drift occurs exactly for `2 x w` (or rotated) with `w>=3`; every rectangle with both sides at least 3 has nonpositive drift. Combining this with the exact all-CO poison probability suggests that **2x8**, not 3x5, is the first rectangular seed that simultaneously (i) beats the `1/64` direct CO-poison budget and (ii) has positive initial vacancy drift. This is a qualitatively different restart candidate: thin rather than compact.

## B29 — add infinity only after a finite-torus identity

On an even finite torus let `Q=N_CO-N_O`. Successful CO adsorption changes `Q` by `+1`; successful O2 adsorption changes it by `-2`, independently of reaction choices. Hence for general source normalization `q/2=1-p`,

`G Q = p V - (q/2) E00 = p V - (1-p) E00`,

with `E00` the number of undirected vacant-vacant nearest-neighbour edges.

For any translation-averaged stationary torus law,

`p rho0 = (1-p)(rho00^h + rho00^v)`.

Take a local weak limit along even tori. Since these are bounded local cylinder observables, the identity passes to the translation-invariant limit. If `rho0>0`, the conditional vacant degree at the origin is therefore

`E[deg_0^vac | 0 vacant] = 2p/(1-p)`.

Since this degree is at most 4, any such stationary non-poisoned limit must satisfy `p<=2/3`. At `p=1/2`, the conditional vacant degree is exactly 2. This gives a clean infinite-volume structural theorem without ever pretending that the infinite total charge `Q` exists.

No metric movement is claimed from any of these ideas unless a complete two-child 1-dependent block certificate is actually produced.