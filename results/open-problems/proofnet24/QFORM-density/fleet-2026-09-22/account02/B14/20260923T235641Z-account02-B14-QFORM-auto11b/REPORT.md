SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T23:56:41Z.
attacking: third-resource logarithmic receiver closure — keep the entire rank-two product together, derive its translation-uniform logarithmic density envelope, and pay one genuinely independent square before any frozen-slice normalization.

# account02/B14 — whole-product log envelope plus independent-square closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T235641Z-account02-B14-QFORM-auto11b`  
**Status:** new proved affine-uniform supporting theorem + exact-target application + source-valid comparison; full QFORM remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Continuity:** not claimed for the full target; the result below is an essential-density estimate.

## 1. First unpaid implication

The newest compatible designated partner account03/B14 (`math-open-problems@8b915c140db7d5bcecfce69e46eb1b81297af93b`, checks at `571914cc7d3cb368840d3a69a90167d79eff3b3c`) proves that even smooth strict-subcap laws, positive on one connected compact interval, can have a uniformly good frozen-slice half-Frostman profile while the rank-two rough hub

\[
T=2L(X-X')
\]

has

\[
p_T(0)\ge \frac3{16}\log\frac1{2\varepsilon}\to\infty.
\]

Thus the interval-only frozen-slice interface is genuinely insufficient, even after the zero-loss smooth-connected-support reduction. The first unpaid implication for this slot is therefore not to improve that false endpoint, but to aggregate the whole rank-two product before the third curvature is paid.

The calculation below does exactly this for one important localized branch: a hyperbolic physical pair plus one disjoint original-coordinate square. It has no support, moment, connectedness, fragment-count, bridge-floor or translation hypothesis.

## 2. A universal logarithmic envelope for a whole hyperbolic product

Let `U,V` be independent real random variables with probability densities bounded by one, and put

\[
Z=UV.
\]

For `z!=0`, the product density is

\[
p_Z(z)=\int_{\mathbb R} f_U(u)f_V(z/u)\,\frac{du}{|u|}.
\tag{2.1}
\]

### Lemma 2.1 — product log envelope

For almost every `z`,

\[
\boxed{
 p_Z(z)\le 2+2\log_+\frac1{|z|}.
}
\tag{2.2}
\]

**Proof.** Suppose first `0<|z|<1`. Split (2.1) into

\[
|u|\ge1,\qquad |z|\le |u|<1,\qquad |u|<|z|.
\]

On `|u|>=1`, use `f_V<=1` and `1/|u|<=1` to get a contribution at most `int f_U=1`. On the middle annulus, discard both densities and integrate `du/|u|`, giving exactly `2 log(1/|z|)`. On `|u|<|z|`, substitute `v=z/u`; then `|v|>1` and the contribution becomes

\[
\int_{|v|>1}f_U(z/v)f_V(v)\frac{dv}{|v|}\le1.
\]

For `|z|>=1`, split only at `|u|=1`; the same first estimate and the same substitution give one plus one. This proves (2.2). QED.

Consequently, for `a!=0`,

\[
H=2aUV
\]

has

\[
\boxed{
 p_H(x)\le |a|^{-1}\left(1+\log_+\frac{2|a|}{|x|}\right).
}
\tag{2.3}
\]

This bound is already fully translation-compatible. Indeed

\[
2aUV+\alpha U+\beta V
=2a\left(U+\frac\beta{2a}\right)
       \left(V+\frac\alpha{2a}\right)
 -\frac{\alpha\beta}{2a},
\tag{2.4}
\]

and deterministic translations preserve both independence and the density cap.

## 3. One independent square integrates the logarithmic singularity

Let `Y` be independent of `(U,V)`, again with density bounded by one, and let `lambda!=0`. Linear terms in `Y` are removed by completing the square, so it is enough to study

\[
R=H+\lambda Y^2.
\]

From (2.3), for every real `t`,

\[
p_R(t)
\le |a|^{-1}
\left[
1+\mathbb E\log_+\frac{2|a|}{|t-\lambda Y^2|}
\right].
\tag{3.1}
\]

### Lemma 3.1 — translated logarithmic square potential

For every `A,c>0`, every real `t`, and every cap-one probability density of `Y`,

\[
\boxed{
\mathbb E\log_+\frac{A}{|t-cY^2|}
\le4\sqrt{\frac{2A}{c}}.
}
\tag{3.2}
\]

**Proof.** Layer cake gives

\[
\log_+\frac{A}{r}
=\int_0^\infty \mathbf1_{\{r<Ae^{-s}\}}\,ds.
\]

For every `delta>0` and every real `tau`,

\[
\left|\{y:\ |\tau-y^2|<\delta\}\right|
\le2\sqrt{2\delta}.
\tag{3.3}
\]

If `tau<=delta`, the allowed values obey `y^2<tau+delta<=2delta`; if `tau>delta`, the measure is

\[
2\bigl(\sqrt{\tau+\delta}-\sqrt{\tau-\delta}\bigr),
\]

which decreases with `tau` and has limiting maximum `2sqrt(2delta)` at `tau=delta`. After scaling by `c`, the cap-one law of `Y` therefore gives

\[
\Pr\{|t-cY^2|<Ae^{-s}\}
\le2\sqrt{\frac{2A}{c}}e^{-s/2}.
\]

Integrating in `s` proves (3.2). QED.

Taking `A=2|a|` and `c=|lambda|` in (3.2) yields the main estimate.

## 4. `QFORM-HYPERBOLIC-LOG-PLUS-SQUARE-CLOSURE-v1`

Let `U,V,Y` be independent cap-one real probability densities. For arbitrary

\[
a\lambda\ne0,\qquad \alpha,\beta,\gamma,\eta\in\mathbb R,
\]

the quadratic-affine polynomial

\[
Q=2aUV+\lambda Y^2+\alpha U+\beta V+\gamma Y+\eta
\]

has an essentially bounded density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le
\frac1{|a|}+rac8{\sqrt{|a\lambda|}}.
}
\tag{4.1}
\]

In particular,

\[
|a|\ge1,\quad |\lambda|\ge1
\qquad\Longrightarrow\qquad
\boxed{\|p_Q\|_\infty\le9.}
\tag{4.2}
\]

No moment, bounded-support, fragment-count, separation, connectedness, symmetry or log-concavity assumption occurs. All deterministic translations and affine coefficients are already included.

### Ambient localization corollary

Suppose a full quadratic form in independent original coordinates contains three retained coordinates whose principal quadratic block, after permutation, is

\[
B=
\begin{pmatrix}
0&a&0\\
a&0&0\\
0&0&\lambda
\end{pmatrix},
\qquad |a|,|\lambda|\ge1.
\tag{4.3}
\]

Condition on every other **original** coordinate. Arbitrary outside self-curvature and cross-couplings then create only deterministic affine coefficients and a constant in the retained variables, so (4.2) applies on every conditioning fibre. Averaging gives

\[
\boxed{\|p_Q\|_\infty\le9.}
\tag{4.4}
\]

Thus the theorem is a genuine translation-uniform localization branch of the full target, not merely a three-variable statement.

## 5. Application to the newest account03/B14 obstruction

Use the partner's smooth connected strict-subcap laws `L,X,X'`, for which the rank-two quantity

\[
T=2L(X-X')
\]

has a logarithmically diverging peak while every frozen slice enjoys the uniform half-Frostman estimate. Put

\[
D=X-X'.
\]

Young's inequality gives

\[
p_D(d)=\int f_X(x)f_{X'}(x-d)\,dx\le1,
\tag{5.1}
\]

and `D` is independent of `L`. Let `Y` be any further independent cap-one input (it may be chosen from the same smooth connected stress family). Then (4.2), applied to the independent triple `(L,D,Y)`, gives

\[
\boxed{
\|p_{\,2L(X-X')+Y^2}\|_\infty\le9.
}
\tag{5.2}
\]

This is uniform while the partner's bridge height tends to zero, connected support diameter tends to infinity, smoothing scale tends to zero, and fragment geometry becomes arbitrarily remote.

In the original independent variables `(L,X,X',Y)`, the homogeneous matrix is

\[
\begin{pmatrix}
0&1&-1&0\\
1&0&0&0\\
-1&0&0&0\\
0&0&0&1
\end{pmatrix},
\tag{5.3}
\]

with spectrum

\[
\{\sqrt2,-\sqrt2,1,0\}.
\tag{5.4}
\]

Hence (5.2) is squarely inside the owner's exact three-large-eigenvalue target. The same rough rank-two law that defeats the frozen-slice receiver becomes uniformly bounded as soon as a genuinely independent third square is paid **after** whole-product aggregation.

This identifies the proof-order mechanism: the logarithmic singularity is a rank-two product effect; the third square contributes a `sqrt(delta)` level-set measure, and layer cake makes their composition integrable. Normalizing the rank-two frozen slices first destroys this useful aggregate structure.

## 6. Required fixed-source theorem applied to the same family

The fixed required source was freshly read at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed Theorem A states that in dimension three, if every eigenvalue has modulus at least `sigma`, arbitrary linear terms are allowed and

\[
\|p_Q\|_\infty\le\frac{6\sqrt\pi}{\sigma}.
\tag{6.1}
\]

For the aggregated independent triple `(L,D,Y)`, the matrix of `2LD+Y^2` is

\[
\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
\]

whose eigenvalues are `{1,-1,1}`. Since `L,D,Y` all have densities at most one, Theorem A gives the real inequality

\[
\boxed{
\|p_{\,2L(X-X')+Y^2}\|_\infty
\le6\sqrt\pi
=10.6347231054\ldots .
}
\tag{6.2}
\]

The new estimate (5.2) sharpens this to `9` on the same exact-target family. More importantly for this slot, (6.2) independently confirms that the partner's logarithmic rank-two pathology is an obstruction to the frozen-slice proof interface, not to the three-large-eigenvalue conjecture.

## 7. Consequence for localization strategy

The safe order in this branch is now explicit:

\[
\text{whole independent product pair}
\ \longrightarrow\ 
\text{logarithmic envelope}
\ \longrightarrow\ 
\text{independent third square}
\ \longrightarrow\ 
L^\infty,
\]

with translations and outside conditioning handled only through affine-uniformity. No bounded-diameter or fixed-fragment surrogate is needed.

The sharpened first unpaid implication is

**`QFORM-LOG-ENVELOPE-EXTRACTION-OR-WHOLE-VOLUME-EXIT-v1`.** In each surviving no-pivot/near-degenerate configuration, before active fragment normalization, force either (i) a whole original-coordinate/bank hyperbolic product admitting a translation-uniform logarithmic envelope together with a genuinely disjoint independent square resource, or (ii) an existing whole-law D'/D5/projected-crossing/ridge/hub/pair/receiver exit. The remaining hard overlap is when the would-be third curvature is generated by the same active bank as the rank-two product, so no independent square is available after conditioning.

That overlap, not translations, remote fragments, smoothness or connectedness, is the next localization debt.

## 8. Scope audit

This report does **not** prove the unrestricted conjecture and does not claim continuity. It does not use independence after spectral rotation, arbitrary-joint coarea, uniform pointwise quadratic-phase decay, bounded moments/support, log-concavity, fixed fragment count, a uniform bridge floor, or a uniformly conditioned physical minor. It uses only original product independence, cap-one densities, exact affine completion, the explicit product-density identity, and one disjoint independent square.
