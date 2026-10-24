# account02/B13 — exact bang-bang reduction for bounded product densities

**Run:** `20260922T115714Z-account02-B13-qform-480ba28b`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** `Extremal product laws`  
**Classification:** `PROVED_TARGET-LEVEL_REDUCTION / SUPPORTING_GEOMETRIC_LEMMAS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains **OPEN**. This report proves the exact reduction requested by the B13 card: for every fixed quadratic slab, the supremum over all independent one-dimensional densities `0<=f_i<=1`, `int f_i=1`, is attained in the supremum sense by product indicator laws `f_i=1_{E_i}` with `|E_i|=1`. Moreover the supremum is unchanged if every `E_i` is required to be a bounded finite union of intervals of total length one. No single-interval or centered-uniform extremality is claimed; a quadratic-fiber counterexample below shows that such a strengthening is false.

## 1. Source state and corrections

Fresh control before the mathematical write was `yspennstate/math-research-brain@98dcc2e9e09e141ebd9907cb82dba67cb4721460`, owner revision `2026-09-22.5`. The live correction inbox includes the refutation `QFORM-CROSSMINOR-ALONE-FALSE`; no argument below uses a cross-minor-alone implication. The standing corrections `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, and `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` are also respected.

The assigned partner is `account03/B13`. No completed current-QFORM handoff from that slot existed at the fresh read, so no stale FEI result was imported. A named completed **other-account** result was consumed instead:

`yspennstate/math-open-problems@db7e2efa23166b1ce2e7ef376b69b8e973ccf391`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/account03-B12-20260922T114435Z-349dfcff7c/REPORT.md`.

At the scope used here it proves a uniform density bound `<24.231/lambda` for a flat four-coordinate core with three equal large eigenvalues and arbitrary fourth eigenvalue, by stitching definite-pair and nonsingular-triple mechanisms. I use it in §7 as an already-closed geometric branch after the new product-set reduction.

I also read the underlying pair/triple source
`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`
`qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.

## 2. One-coordinate bathtub lemma

Let
\[
\mathcal D:=\{f:\mathbb R\to[0,1]\text{ measurable}:\int_{\mathbb R}f=1\}.
\]

### Lemma 2.1 — `QFORM-BATHTUB-ONECOORD-v1`

For every bounded nonnegative measurable `h`,
\[
\boxed{
\sup_{f\in\mathcal D}\int h(x)f(x)\,dx
=
\sup_{E\subset\mathbb R,\ |E|=1}\int_E h(x)\,dx.
}
\]

#### Proof

For any `f in D`, layer-cake in `h` gives
\[
\int hf
=
\int_0^{\|h\|_\infty}
\left(\int_{\{h>s\}} f(x)\,dx\right)ds
\le
\int_0^{\|h\|_\infty}
\min\{1,|\{h>s\}|\}\,ds.
\tag{2.1}
\]
The right side is the usual bathtub value: choose a threshold `tau` so that
\[
|\{h>\tau\}|\le1\le|\{h\ge\tau\}|,
\]
and use nonatomicity of Lebesgue measure to fill the remaining measure inside the level set `{h=tau}`. If an exact threshold is inconvenient, the same value is obtained as a supremum by thresholds approaching the quantile. Thus the right side of (2.1) equals
\[
\sup_{|E|=1}\int_E h.
\]
The reverse inequality is immediate because `1_E in D`. QED.

No compact support, continuity, monotonicity, moment, or symmetry assumption on `h` is used.

## 3. Exact product purification

Let `K:R^n->[0,1]` be measurable and define
\[
\Lambda_K(f_1,\ldots,f_n)
:=
\int_{\mathbb R^n}K(x)\prod_{i=1}^n f_i(x_i)\,dx.
\]

### Theorem 3.1 — `QFORM-PRODUCT-BANGBANG-REDUCTION-v1`

\[
\boxed{
\sup_{f_1,\ldots,f_n\in\mathcal D}
\Lambda_K(f_1,\ldots,f_n)
=
\sup_{\substack{E_1,\ldots,E_n\subset\mathbb R\\|E_i|=1}}
\int_{E_1\times\cdots\times E_n}K(x)\,dx.
}
\tag{3.1}
\]

#### Proof

Fix an admissible tuple. With all coordinates except `i` frozen define
\[
h_i(t)
=
\int_{\mathbb R^{n-1}}
K(x_1,\ldots,x_{i-1},t,x_{i+1},\ldots,x_n)
\prod_{k\ne i} f_k(x_k)\,dx_{-i}.
\]
Tonelli gives measurability, and because `0<=K<=1` and every other factor has mass one,
\[
0\le h_i(t)\le1.
\]
Lemma 2.1 allows replacement of `f_i` by an indicator `1_{E_i}`, `|E_i|=1`, without decreasing the value, up to an arbitrarily small error if one uses a supremizing threshold. Repeat for `i=1,...,n`. The total error can be made arbitrarily small, so
\[
\sup_{\mathcal D^n}\Lambda_K
\le
\sup_{|E_i|=1}\Lambda_K(1_{E_1},\ldots,1_{E_n}).
\]
The reverse inequality is trivial because every indicator of a unit-measure set is an admissible density. QED.

The replacement is made in the **original independent coordinates**. No rotation, spectral recoding, or independence-after-rotation assumption is used.

## 4. Exact equivalence with a geometric quadratic-slab problem

For a real symmetric `A`, interval `J`, and
\[
Q_A(x)=x^TAx,
\]
take
\[
K_{A,J}(x)=1_{\{Q_A(x)\in J\}}.
\]
Then Theorem 3.1 gives
\[
\boxed{
\sup_{f_i\in\mathcal D}
\Pr_{f_1\otimes\cdots\otimes f_n}(Q_A(X)\in J)
=
\sup_{|E_i|=1}
\left|
\left\{
x\in\prod_iE_i:Q_A(x)\in J
\right\}
\right|.
}
\tag{4.1}
\]

Define the concentration function
\[
M_A(\varepsilon)
:=
\sup_{a\in\mathbb R}
\sup_{f_i\in\mathcal D}
\Pr(Q_A(X)\in[a,a+\varepsilon]).
\]
Then exactly
\[
\boxed{
M_A(\varepsilon)
=
\sup_{a\in\mathbb R}
\sup_{|E_i|=1}
\left|
\left\{
x\in\prod_iE_i:
a\le x^TAx\le a+\varepsilon
\right\}
\right|.
}
\tag{4.2}
\]

Hence the owner's bounded-density conjecture is equivalent, for its essential-supremum conclusion, to the following geometric statement:

> There is a universal finite `C` such that for every `n`, every real symmetric `A` with at least three eigenvalues of absolute value at least one, every measurable unit-measure sets `E_i`, every `a`, and every `epsilon>0`,
> \[
> \left|
> \{x\in\prod_iE_i:a\le x^TAx\le a+\epsilon\}
> \right|
> \le C\epsilon.
> \tag{4.3}
> \]

Indeed (4.3) gives the same interval estimate for arbitrary admissible densities by (4.1). A finite Borel measure satisfying `mu(I)<=C|I|` for every interval is dominated by `C` times Lebesgue measure, hence has a Radon-Nikodym density bounded by `C` almost everywhere. This proves the requested essentially bounded density. It does **not** by itself prove the owner's stronger optional request for a continuous representative.

Conversely, a uniform density bound implies (4.3), so this is an exact reformulation, not a one-way relaxation.

## 5. Finite-union localization with no loss

Let `U` be the class of bounded finite unions of intervals of total Lebesgue measure one.

### Theorem 5.1 — `QFORM-FINITE-UNION-REDUCTION-v1`

For every measurable `K:R^n->[0,1]`,
\[
\boxed{
\sup_{|E_i|=1}\int K\prod_i1_{E_i}
=
\sup_{F_i\in U}\int K\prod_i1_{F_i}.
}
\tag{5.1}
\]

#### Proof

Given a measurable `E` of measure one and `eta>0`, regularity of Lebesgue measure gives a bounded finite union of intervals `G` with
\[
|E\triangle G|<\eta.
\]
If `|G|>1`, shave total length `|G|-1` from interval endpoints; if `|G|<1`, add a disjoint interval of length `1-|G|`. The resulting finite union `F` has `|F|=1` and
\[
|E\triangle F|<2\eta.
\tag{5.2}
\]

For two product indicator tuples, telescope
\[
\prod_i1_{E_i}-\prod_i1_{F_i}
=
\sum_i
(1_{E_i}-1_{F_i})
\prod_{k<i}1_{E_k}
\prod_{k>i}1_{F_k}.
\]
Since every other factor has integral one,
\[
\left\|
\prod_i1_{E_i}-\prod_i1_{F_i}
\right\|_{L^1(\mathbb R^n)}
\le
\sum_i|E_i\triangle F_i|.
\tag{5.3}
\]
Therefore the `K`-integrals differ by at most the same quantity. Taking `eta` arbitrarily small proves (5.1). QED.

By approximating interval endpoints, one can further restrict the supremum to finite unions with rational endpoints and total length one. Thus any strict violation of a proposed small-ball constant has a finite-union support witness with an arbitrarily small loss. The number of components is not uniformly bounded by this argument.

## 6. Why “single interval / centered uniform is extremal” is false

The exact bang-bang reduction must retain arbitrary measurable unit sets.

Fix `R>1` and `epsilon>0` so small that
\[
2\ell<1,\qquad
\ell:=\sqrt{R^2+\epsilon}-R.
\]
For the one-dimensional quadratic slab
\[
h(x)=1_{\{R^2\le x^2\le R^2+\epsilon\}},
\]
the support is the disjoint union
\[
B_+=[R,\sqrt{R^2+\epsilon}],
\qquad
B_-=[-\sqrt{R^2+\epsilon},-R],
\]
each of length `ell`.

Choose any measurable filler `F` disjoint from the slab with
\[
|F|=1-2\ell,
\]
and set
\[
E=B_+\cup B_-\cup F.
\]
Then `|E|=1` and
\[
\int_E h=2\ell.
\tag{6.1}
\]
Because the gap between the two slab branches is `2R>2`, any interval of length one intersects at most one branch, hence
\[
\sup_{\substack{I\text{ interval}\\|I|=1}}\int_I h\le\ell.
\tag{6.2}
\]
Thus allowing a disconnected unit-measure set gains a factor exactly `2` over every single unit interval for this quadratic fiber. A centered unit interval can miss the slab entirely.

This is not a counterexample to the QFORM conjecture. It is a rigorous counterexample to the shortcut “after bang-bang purification, assume one centered interval per coordinate.”

## 7. Geometric attack: closed local-curvature branches

The new reduction turns every existing source-valid local density theorem into a geometric slab theorem for product sets with exactly the same constant.

### 7.1 Definite principal pair

If the principal block on original coordinates `{i,j}` is a positive or negative definite matrix `B`, then after conditioning every other original coordinate the remaining polynomial is
\[
z^TBz+2\ell^Tz+c.
\]
Completing the square and applying `y=|B|^{1/2}(z+B^{-1}\ell)` reduces the slab to a Euclidean annulus in `R^2`. Its full-plane area is at most
\[
\frac{\pi\epsilon}{\sqrt{|\det B|}}.
\]
Therefore for arbitrary product sets, and hence arbitrary admissible densities,
\[
\boxed{
\Pr(Q_A(X)\in J)
\le
\frac{\pi}{\sqrt{|\det B|}}\,|J|.
}
\tag{7.1}
\]
This is exactly the definite-pair branch appearing in the consumed principal-block source. Cross couplings to conditioned variables become linear tilts and cost nothing.

### 7.2 Nonsingular principal triple

The consumed principal-triple source proves that if a `3x3` original-coordinate principal block has smallest singular value `kappa`, then
\[
\boxed{
\Pr(Q_A(X)\in J)
\le
\frac{2\pi+3\sqrt3}{\kappa}|J|.
}
\tag{7.2}
\]
Again the estimate survives arbitrary outside coordinates by conditioning.

### 7.3 Consumed account03/B12 flat-fourth theorem

Applying the exact B12 theorem after the present reduction: whenever a four-coordinate principal core is
\[
B=\epsilon\lambda I_4+(\mu-\epsilon\lambda)vv^T,
\qquad
|v_i|=1/2,\ \lambda\ge1,
\]
then every product set `E_i` of unit coordinate measure obeys
\[
\boxed{
\left|
\{x\in\prod_iE_i:x^TAx+\ell^Tx+c\in J\}
\right|
\le
\frac{C_*}{\lambda}|J|,
\qquad
C_*<24.231,
}
\tag{7.3}
\]
uniformly in the fourth eigenvalue `mu`, all outside eigenvalues, and all cross couplings. Thus the B12 stitched pair/triple family is an already-paid branch of the exact geometric formulation, not merely a density theorem in a different normalization.

## 8. What has changed at target level

Before this result, “reduce arbitrary densities to nice supports” was only a heuristic and a centered interval was explicitly unsafe. Now the arbitrary-law quantifier is eliminated **exactly at the level of worst-case small-ball probabilities**:

\[
\boxed{
\text{all bounded product densities}
\iff
\text{unit-measure product indicators}
\iff
\text{bounded finite-union unit product sets},
}
\]
where equivalence means equality of the worst-case slab probability for every fixed `A` and interval.

Therefore a genuine counterexample to the owner conjecture, if one exists, can be searched for among finite unions of intervals in the original coordinates. Conversely, a geometric inequality proved only for that finite-union class is enough for the full arbitrary-density theorem with no loss in the constant.

This does not solve the diffuse/aggregate curvature problem. The remaining hard regime is precisely where no uniformly good fixed principal pair/triple is available and no already-closed flat-fourth core applies. The live correction `QFORM-CROSSMINOR-ALONE-FALSE` also forbids replacing this by a nonsingular cross block alone.

## 9. First unpaid implication

`QFORM-AGGREGATE-BANGBANG-SLAB-v1`:

> Prove a dimension-free bound
> \[
> |\{x\in\prod_iE_i:a\le x^TAx\le a+\epsilon\}|
> \le C\epsilon
> \]
> for bounded finite-union `E_i` of measure one in the regime where the three large spectral directions are delocalized across original coordinates and every fixed low-dimensional principal block is quantitatively weak; or give a genuine product-set counterexample.

The exact reduction above shows that this is not an auxiliary support model: success closes the arbitrary-density quantifier itself. A promising next attack is to combine the aggregate Cauchy-Binet curvature resource from the principal-triple obstruction with the product-set geometry before selecting a single minor.

## 10. Deterministic sanity check

A standard-library exact finite-grid analogue was run for 200 random three-coordinate kernels. Each starting marginal was a rational convex combination of two fixed-cardinality indicator vectors. Sequentially replacing each marginal by the top-weight indicator set never decreased the objective; every final marginal was bang-bang.

For the single-interval falsifier, with `R=2`, `epsilon=0.1`,
\[
\ell=\sqrt{4.1}-2=0.024845673131658\ldots,
\]
so the disconnected support captures `2 ell=0.049691346263317...`, while every unit interval captures at most `ell`. These computations are only sanity checks; the proofs above are analytic.

Full QFORM conjecture remains **OPEN / NOT PROVED**.
