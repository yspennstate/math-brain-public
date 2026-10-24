# account01/B06 — curved-fiber integration: an X-ray-only barrier on the two-sheet branch

**Run:** `20260922T120617Z-a01-b06-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Curved fiber integration` / pathway `GEOMETRY`  
**Classification:** `ESSENTIAL_STEP_APPLIED` + `CANDIDATE_ROUTE_REFUTED`; full conjecture **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 0. Fresh control and dependencies

A later owner order superseded the stale FEI payload: all active research is now on the quadratic-form density conjecture. The target is to prove a universal constant `C` such that for every dimension, every independent coordinate law with scalar densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one,

`P(X^T A X in [t,t+h]) <= C h`

for all real `t` and `h>0`, or else give a genuine target counterexample.

Corrections consumed before this derivation:

- `QFORM-POINTWISE-DECAY-FALSE`;
- `QFORM-FIBER-SUP-DIMENSION-LOSS`;
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`;
- `QFORM-CROSSMINOR-ALONE-FALSE`.

The named partner result actually used is **account02/B06**, run `b06-20260922T113045Z-d47192d10a82`, canonical report commit `6902eb62f21a7c833ca27dcca69f34d50e711a7d`, report blob `9cced3d58d10574ef548c119c8d5a67276dc870f`. It proves:

1. a physical definite `2x2` principal block yields the exact curved-fiber bound `pi/sqrt(det B)`;
2. a rank-three Hadamard/Walsh example with spectrum `(1,1,-1,0,...)` can make every fixed physical compression tiny and every physical pair non-definite;
3. a same-sign spectral pair carries a conserved Pluecker determinant-mass measure `w_ij=det(R_ij)^2`, with `sum w_ij=1`.

Thus a successful argument cannot select one bounded-size physical pair; the distributed spectral plane must be aggregated while retaining product structure.

I also use the completed account01/B16 result at canonical report creation commit `8004481452c19f103fd5dd24c2cb4d787860b56a`. That worker converts the valid two-dimensional marginal theorem into an X-ray bound for the three-dimensional spectral marginal and uses the straight-line ruling of one-sheet hyperboloids to prove the majority-sign half of the rank-three `(2,1)` truncation. Its first geometric debt is the two-sheet/minority-sign half, where the level surface has no real-line ruling.

The purpose of this report is to test the strongest possible implication based only on the X-ray information retained by that aggregation.

---

## 1. Statement of the new barrier

Let

`q(x)=x_1^2+x_2^2-x_3^2`.

For a probability density `g` on `R^3`, define its X-ray norm

`X(g)=sup_ell int_ell g dH^1`,

where the supremum is over all affine lines. Equivalently, `X(g)` is the maximum `L^infinity` norm of all two-dimensional orthogonal marginals of `g`.

### Theorem 1 — `QFORM-TWOSHEET-XRAY-ONLY-FALSE-v1`

For every sufficiently small `delta>0` there exists a probability density `g_delta` on `R^3` such that

`X(g_delta) <= 2`,

but the pushforward `q(Y)` for `Y~g_delta` has a density satisfying

`p_{q(Y)}(t) >= 1/(10 delta)`

for every

`t in [-1-delta,-1+delta]`.

Consequently there is no universal estimate of the form

`||p_{q(Y)}||_infinity <= C`

for arbitrary probability densities `g` satisfying only `X(g)<=2`. In particular, the two-dimensional marginal/X-ray cap by itself cannot control the two-sheet branch of the rank-three indefinite quadratic form.

This is **not** a counterexample to the owner target: the constructed `g_delta` is an arbitrary three-dimensional density and is not claimed to be an orthogonal projection of a coordinate-product law. It is a rigorous counterexample to the information-loss step “replace the projected product law by an arbitrary density having only the same X-ray cap.”

---

## 2. The shell density

Fix `0<delta<=1/10` and put

`Z_delta = 2 exp(1/sqrt(delta))`.

Define the upper two-sheet band

`E_delta = {x in R^3: 2 <= x_3 <= Z_delta, |q(x)+1| <= delta}`

and

`a_delta(x) = [1/(2 pi sqrt(delta) x_3)] 1_{E_delta}(x)`.

### Lemma 2.1 — exact normalization and exact quadratic pushforward

`a_delta` is a probability density, and the law of `q(X)` under `a_delta` is exactly uniform on `[-1-delta,-1+delta]`:

`p_{q,a_delta}(t)=1/(2 delta)`

throughout that interval.

### Proof

Write `x_1=r cos theta`, `x_2=r sin theta`, `z=x_3`, and `t=q(x)=r^2-z^2`. Then

`dx_1 dx_2 = r dr dtheta = (1/2) dt dtheta`.

For `z>=2` and `t in [-1-delta,-1+delta]`, one has `r^2=z^2+t>0`. Hence for each fixed `z`,

`int_{|q+1|<=delta} dx_1 dx_2 = pi int_{-1-delta}^{-1+delta} dt = 2 pi delta`.

Therefore

`int a_delta dx`
`= [1/(2 pi sqrt(delta))] (2 pi delta) int_2^{Z_delta} dz/z`
`= sqrt(delta) log(Z_delta/2)`
`=1`.

For a fixed target value `t` in the same interval,

`int_{R^2} delta_D(t-(r^2-z^2)) dx_1 dx_2 = pi`,

so

`p_{q,a_delta}(t)`
`= [1/(2 pi sqrt(delta))] pi int_2^{Z_delta} dz/z`
`=1/(2 delta)`.

`QED`

The shell is spread over an exponentially long logarithmic range in `x_3`; this is what lets it carry total mass one while remaining thin around a single two-sheet level.

---

## 3. A line-intersection lemma

The key point is that the logarithmic weight `1/x_3` exactly offsets the long tangential contact available at large height.

### Lemma 3.1 — weighted line intersection

For every affine line `ell` and every `0<delta<=1/10`,

`int_{ell cap E_delta} dH^1(x)/x_3 <= 30 sqrt(delta)`.

Hence

`X(a_delta) < 5`.

### Proof

Use the Lorentzian quadratic form

`Q_L(x)=x_1^2+x_2^2-x_3^2`

and bilinear form

`B_L(x,v)=x_1v_1+x_2v_2-x_3v_3`.

First suppose `ell` is horizontal. At fixed `x_3=z`, the section `|Q_L(x)+1|<=delta` is an annulus in the horizontal plane. The intersection of any horizontal line with a set of the form

`||y|^2-R^2|<=delta`

has total length at most `2 sqrt(2 delta)`. Since `z>=2`, its contribution to the weighted integral is less than `2 sqrt(delta)`.

Now suppose the line is not horizontal. Parametrize it by Euclidean unit speed as

`x(s)=x_*+s v`, `|v|=1`,

and orient `v` so that `x_3(s)` increases. Each connected component `J` of `ell cap E_delta` has a point `x_*` at its minimum height `z_*=x_{*,3}`. Put

`u=-Q_L(x_*) in [1-delta,1+delta]`,

`alpha=Q_L(v)`,

`beta=B_L(x_*,v)`.

We first establish the local dichotomy

`|beta| >= 1/(5 z_*)`

or

`alpha >= 1/(20 z_*^2)`.

Indeed, set `x'=x_*/sqrt(u)`, so `Q_L(x')=-1`, let `z'=z_*/sqrt(u)`, and put `beta'=B_L(x',v)=beta/sqrt(u)`. The vector

`w=v+beta' x'`

is Lorentz-orthogonal to `x'`, hence tangent to the exact hyperboloid `Q_L=-1`. If

`|beta'| >= 1/(4 z')`,

then

`|beta| >= u/(4 z_*) >= 1/(5 z_*)`.

Otherwise, because `|x'|_Euclid < sqrt(2) z'`,

`|w|_Euclid >= 1-sqrt(2)/4 > 1/2`.

For a tangent vector `w=(w_h,w_3)` at `x'=(x'_h,z')`, the relation

`x'_h . w_h = z' w_3`

and `|x'_h|^2=z'^2-1` imply

`w_3^2 <= (1-z'^{-2}) |w_h|^2`.

Therefore

`Q_L(w)=|w_h|^2-w_3^2 >= |w_h|^2/z'^2 >= |w|_Euclid^2/(2 z'^2) >= 1/(8 z'^2)`.

Since

`Q_L(w)=alpha+beta'^2`

and `beta'^2<1/(16z'^2)`, one gets

`alpha>=1/(16z'^2)>=1/(20z_*^2)`

for `delta<=1/10`. This proves the dichotomy.

Along the line,

`F(s)=Q_L(x(s))+1`

is a quadratic polynomial with second-order coefficient `alpha`:

`F(s)=F(0)+2 beta s+alpha s^2`.

We split into two cases.

**Case A: `|alpha|>=1/(20 z_*^2)`.** For every real quadratic `alpha s^2+2 beta s+c`, completing the square gives the elementary sublevel estimate

`measure{s: |alpha s^2+2 beta s+c|<=delta}`
`<= 2 sqrt(2 delta/|alpha|)`.

Hence the total Euclidean length of the relevant sublevel set is at most

`2 sqrt(40) z_* sqrt(delta) < 13 z_* sqrt(delta)`.

Since `z>=z_*` on `J`, the weighted contribution of this component is less than `13 sqrt(delta)`.

**Case B: `|alpha|<1/(20 z_*^2)`.** The dichotomy forces

`|beta|>=1/(5 z_*)`.

For `0<=s<=z_*`,

`|alpha s|<=1/(20z_*)`,

so

`|F'(s)|=2|beta+alpha s| >= 3/(10z_*)`,

with fixed sign. If `J` had length at least `z_*`, then `F` would vary by at least `3/10`, impossible because it remains in an interval of width `2delta<=1/5`. Thus `J` has length below `z_*`, the derivative lower bound is valid on all of `J`, and

`length(J) <= 2delta / [3/(10z_*)] = (20/3) delta z_* < 7 delta z_*`.

Its weighted contribution is therefore below `7delta<=7sqrt(delta)`.

The preimage of an interval under a quadratic polynomial has at most two connected components. Adding the worst bounds and the horizontal case gives the convenient universal estimate

`int_{ell cap E_delta} ds/x_3 <= 30 sqrt(delta)`.

Finally,

`int_ell a_delta ds`
`<= [1/(2 pi sqrt(delta))] 30 sqrt(delta)`
`=15/pi<5`.

`QED`

---

## 4. Enforcing the same X-ray cap as an actual product projection

The previous shell has X-ray norm below `5`, whereas the current product-marginal theorem used by account01/B16 gives the cap `2`. A harmless filler makes the counterexample match that numerical cap exactly.

Let

`eta(x)=1/8`

on the cube

`C=[20,22] x [0,2] x [0,2]`

and zero elsewhere. This is a probability density. Any line meets `C` in length at most its Euclidean diameter `2sqrt(3)`, hence

`X(eta)<=sqrt(3)/4<1/2`.

Also

`q(x)>=20^2-2^2=396`

on `C`, so `eta` contributes no mass to `q`-values near `-1`.

Define

`g_delta=(1/5)a_delta+(4/5)eta`.

Then `g_delta` is a probability density and

`X(g_delta)`
`<= (1/5)X(a_delta)+(4/5)X(eta)`
`<1+(4/5)(1/2)`
`<2`.

On `[-1-delta,-1+delta]`, however,

`p_{q,g_delta}(t)=(1/5)(1/(2delta))=1/(10delta)`.

This proves Theorem 1.

---

## 5. Consequence for the B06 information budget

### Corollary 5.1 — `QFORM-B06-INFORMATION-SANDWICH-v1`

The two most obvious curvature simplifications are now rigorously excluded:

1. **Localize to one bounded-size physical pair:** account02/B06's exact Hadamard construction refutes this, while its Pluecker identity shows that the same-sign curvature survives only as distributed determinant mass.
2. **Globally aggregate the spectral triple and retain only the universal two-dimensional marginal/X-ray cap:** Theorem 1 refutes this as a sufficient information set on the two-sheet branch.

Therefore any successful B06 proof must retain information strictly between these two losses: it must aggregate the distributed Pluecker curvature **while preserving additional product-law provenance beyond the generic X-ray norm**.

This is precisely the weighted-curved-fiber direction suggested by the partner result. The partner's normalized weights

`w_ij=det(R_ij)^2`, `sum w_ij=1`,

cannot be collapsed either to one large physical minor or to an arbitrary 3D density with bounded line marginals before the two-sheet trace is paid.

A natural next exact implication is therefore:

### `QFORM-PRODUCT-PROJECTION-TWOSHEET-TRACE-v1`

Let `g` be the actual three-dimensional orthogonal marginal of a coordinate-product density `prod_i f_i`, with every `||f_i||_infinity<=1`, onto a spectral triple with signature `(2,1)`. Prove directly, using the product representation and the distributed Pluecker data before information loss, that

`sup_{a>0} int_{q=-a^2} g(y) d sigma(y)/|grad q(y)| <= C`

for a universal constant `C`, or produce a genuine product-projection counterexample.

Theorem 1 proves that the hypothesis “all line marginals of `g` are at most `2`” is not enough for this statement. Some stronger product-projection invariant must enter.

---

## 6. Compact conditional route and remaining debt

A current conditional route is:

1. Among three large eigenvalues choose a same-sign pair.
2. Use account02/B06's determinant-mass identity to avoid any false fixed-pair localization.
3. Use the valid product-marginal theorem to aggregate the selected spectral plane/triple.
4. On a one-sheet level, account01/B16's straight ruling pays the curved trace by line marginals.
5. On a two-sheet level, do **not** discard product provenance and keep only the X-ray cap; Theorem 1 proves that route cannot close.
6. Prove `QFORM-PRODUCT-PROJECTION-TWOSHEET-TRACE-v1` with a genuinely product-preserving weighted mechanism.
7. Even after the isolated rank-three trace is closed, the full matrix still requires transporting the estimate through correlated additional spectral components without pretending they are independent noise.

Thus this run does not prove the owner theorem. It removes a broad false strategy and sharpens the first curved-fiber debt to a product-projection-specific trace inequality.

## 7. Status

**PROVED:** `QFORM-TWOSHEET-XRAY-ONLY-FALSE-v1`; `QFORM-B06-INFORMATION-SANDWICH-v1`.

**APPLIED PARTNER RESULT:** account02/B06 `QFORM-HADAMARD-DELOCALIZED-v1` and `QFORM-SAMESIGN-DETERMINANT-MASS-v1`, canonical report commit `6902eb62f21a7c833ca27dcca69f34d50e711a7d`.

**CANDIDATE ROUTE REFUTED:** controlling the two-sheet/minority-sign quadratic trace using only probability normalization plus the universal two-dimensional marginal/X-ray cap of the three-dimensional spectral projection.

**OPEN:** `QFORM-PRODUCT-PROJECTION-TWOSHEET-TRACE-v1`, correlated additional spectral components, and the full universal quadratic-form density conjecture.
