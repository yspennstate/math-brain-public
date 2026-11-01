# fleet01/B13 — exact product-set extremal reduction and collective rank-three smoothing

**Run:** `20260922T113055Z-qform-b13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** `Extremal product laws` (`fleet01/B13`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUBSTANTIVE_PARTIAL_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository synchronization is not native brain ingestion.  
**Full conjecture:** **OPEN / NOT PROVED.**

## 0. Source state and corrections consumed

The invocation initially carried the superseded FEI prompt. Fresh protected-control resolution moved the sole research target to the quadratic-form bounded-density conjecture. The coherent current control used for this report is:

- `yspennstate/math-research-brain@0c91685885872548af61fc232c561c0685c1f5f9`;
- `scheduled_tasks/README.md`, owner control revision `2026-09-22.5`;

Required corrections used:

1. `QFORM-POINTWISE-DECAY-FALSE`: no law-uniform pointwise `|t|^{-1/2}` Fresnel decay is available for one arbitrary density bounded by one;
2. `QFORM-FIBER-SUP-DIMENSION-LOSS`: taking an unrestricted fiber supremum can lose dimension;
3. `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: diagonalizing `A` destroys independence in general.

The live `CORRECTION_INBOX.json` was empty at the source pin above.

The current assignment asks for a rigorous reduction from arbitrary densities `0<=f_i<=1`, `int f_i=1`, to product indicators/mixtures, without assuming intervals or centered uniforms. Section 1 gives an exact reduction. Sections 2--4 then apply it together with a compatible other-account result to close a nontrivial delocalized rank-three obstruction.

The assigned partner `fleet02/B13` had no source-visible qform handoff at the control pin above, so no partner theorem is fabricated. I instead substantively consume the compatible fleet02/B15 theorem at

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8:qform/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`.

That report proves a three-original-coordinate principal-block theorem and, crucially for this run, exhibits the flat rank-three projector `A=UU^T` with row leverage `3/n`, for which every fixed principal triple has curvature only `O(1/n)` although the total Cauchy--Binet determinant mass is one. Its first unresolved geometry is exactly distributed/delocalized rank-three curvature rather than a single good coordinate block.

## 1. Exact extremal reduction to arbitrary measure-one product sets

Let

`D = { f:R-> [0,1] measurable : int_R f = 1 }`.

No continuity, moment, support, centering, or connectedness is assumed.

### Lemma 1.1 — one-coordinate bathtub identity

For every nonnegative measurable `g:R->[0,infinity]`,

\[
\boxed{
\sup_{f\in D}\int g(x)f(x)\,dx
=
\sup_{E\subset R:\ |E|=1}\int_E g(x)\,dx .
}
\tag{1.1}
\]

Here `E` ranges over measurable sets and `|E|` is Lebesgue measure.

### Proof

For `f in D`, layer cake gives

\[
\int gf
=
\int_0^\infty\int_{\{g>t\}} f(x)\,dx\,dt.
\]

Since `0<=f<=1` and `int f=1`,

\[
\int_{\{g>t\}}f
\le \min\{1,|\{g>t\}|\}.
\]

Hence

\[
\int gf
\le
\int_0^\infty \min\{1,|\{g>t\}|\}\,dt.
\tag{1.2}
\]

By the standard bathtub/top-level-set construction on the nonatomic Lebesgue space (take all points above a threshold and, if necessary, the required amount of a level set), the right side is exactly

\[
\sup_{|E|=1}\int_E g.
\]

Conversely every `1_E`, `|E|=1`, belongs to `D`. This proves (1.1). `QED`.

The lemma is an exact supremum identity; no weak compactness, moment assumption, or assertion that one interval is extremal is used.

### Theorem 1.2 — `QFORM-PRODUCT-INDICATOR-EXTREMAL-v1`

Let `K:R^n->[0,infinity]` be measurable. Then

\[
\boxed{
\sup_{f_1,...,f_n\in D}
\int_{R^n}K(x)\prod_{i=1}^n f_i(x_i)\,dx
=
\sup_{|E_1|=\cdots=|E_n|=1}
\int_{E_1\times\cdots\times E_n}K(x)\,dx .
}
\tag{1.3}
\]

### Proof

Fix `f_2,...,f_n` and integrate them out. The objective is a nonnegative linear functional `int g_1 f_1`, so Lemma 1.1 replaces the supremum over `f_1` by the supremum over indicators of measure-one sets. Then fix that first indicator and repeat for coordinate 2, and so on. Because only finitely many coordinates are present, iterating the exact one-coordinate supremum identity proves (1.3). The reverse inequality is automatic because every product indicator is an admissible product density. `QED`.

### Corollary 1.3 — exact geometric form of the qform small-ball problem

For every real quadratic form `Q` and every Borel set `B subset R`,

\[
\boxed{
\sup_{f_i\in D}\Pr\{Q(X)\in B\}
=
\sup_{|E_i|=1}
\left|\{x\in E_1\times\cdots\times E_n:Q(x)\in B\}\right|.
}
\tag{1.4}
\]

In particular, the target density bound follows if one proves the **pure geometric product-set inequality**

\[
\boxed{
\left|\{x\in E_1\times\cdots\times E_n:Q(x)\in J\}\right|
\le C|J|
}
\tag{1.5}
\]

for every interval `J`, every measurable `E_i` of measure one, and every target-admissible `Q`.

Indeed (1.4) then gives `mu_Q(J)<=C|J|` for every interval. By outer regularity/covering open sets by intervals, `mu_Q<=C Leb`; therefore `Q(X)` is absolutely continuous and its Radon--Nikodym density is at most `C` almost everywhere. This proves the target's essential-supremum conclusion. It does **not** by itself prove the owner's stronger optional request for a continuous representative.

This is a complete reduction of the arbitrary-law part of the conjecture: a worst-case law may be sought among independent uniforms on completely arbitrary measurable sets of measure one. It does **not** justify replacing those sets by intervals, centered sets, or symmetric sets.

## 2. A collective Fourier theorem for delocalized rank-three forms

The preceding reduction makes a geometric/product-set formulation exact, but the flat rank-three obstruction of fleet02/B15 still defeats every proof that first selects one coordinate triple. The next theorem closes that obstruction by using all physical coordinates simultaneously.

Let `U` be an `n x 3` real matrix with orthonormal columns. Write its row vectors as `u_i in R^3`, and define the leverage scores

\[
c_i=|u_i|^2,
\qquad
\sum_i u_i u_i^T=I_3,
\qquad
\sum_i c_i=3.
\tag{2.1}
\]

Let `Lambda=diag(lambda_1,lambda_2,lambda_3)` with `|lambda_j|>=1`; signs are arbitrary.

### Theorem 2.1 — `QFORM-RANK3-DELOCALIZED-BLHY-v1`

Assume

\[
\boxed{\max_i c_i\le\frac12.}
\tag{2.2}
\]

For independent real `X_i` with arbitrary densities `0<=f_i<=1`, `int f_i=1`, put

\[
Y=U^T X,
\qquad
Q=Y^T\Lambda Y.
\]

Then for every `t!=0`,

\[
\boxed{
|\phi_Q(t)|
\le
\min\left\{1,\left(\frac{\pi e}{|t|}\right)^{3/2}\right\},
}
\tag{2.3}
\]

and hence `Q` has a bounded continuous density satisfying

\[
\boxed{
\|p_Q\|_\infty\le3e<8.155.
}
\tag{2.4}
\]

The theorem is valid for signatures `(3,0)`, `(2,1)`, `(1,2)`, `(0,3)`.

### Proof, Step 1: collective characteristic-function integral

Let

\[
\varphi_i(s)=\mathbb E e^{isX_i}.
\]

The characteristic function of `Y=U^T X` is

\[
\psi_Y(\xi)
=
\prod_i\varphi_i(u_i\cdot\xi).
\tag{2.5}
\]

For every row with `c_i>0`, set

\[
a_i=\sqrt{c_i},
\qquad
v_i=u_i/a_i,
\]

so `|v_i|=1` and

\[
\sum_i c_i v_i v_i^T=I_3.
\tag{2.6}
\]

Rows with `c_i=0` can be omitted.

The geometric rank-one Brascamp--Lieb inequality applied to (2.6) says

\[
\int_{R^3}\prod_i g_i(v_i\cdot\xi)^{c_i}\,d\xi
\le
\prod_i\left(\int_R g_i\right)^{c_i}.
\tag{2.7}
\]

Put `q_i=1/c_i>=2`, `p_i=q_i/(q_i-1)=1/(1-c_i)`, and

\[
g_i(s)=|\varphi_i(a_i s)|^{q_i}.
\]

Since `q_i c_i=1`, the left side of (2.7) is exactly

\[
J:=\int_{R^3}\prod_i|\varphi_i(u_i\cdot\xi)|\,d\xi.
\tag{2.8}
\]

Therefore

\[
J
\le
\prod_i
\left(
 a_i^{-1}\int_R|\varphi_i(r)|^{q_i}\,dr
\right)^{c_i}
=
\prod_i a_i^{-c_i}\|\varphi_i\|_{q_i}.
\tag{2.9}
\]

### Step 2: sharp Hausdorff--Young cancels the leverage entropy

Use the Fourier convention

\[
\varphi_i(s)=\int_R e^{isx}f_i(x)\,dx.
\]

The sharp one-dimensional Hausdorff--Young inequality gives, for conjugate `p_i,q_i`,

\[
\|\varphi_i\|_{q_i}
\le
(2\pi)^{1/q_i}
\left(
\frac{p_i^{1/p_i}}{q_i^{1/q_i}}
\right)^{1/2}
\|f_i\|_{p_i}.
\tag{2.10}
\]

Because `0<=f_i<=1` and `int f_i=1`,

\[
\|f_i\|_{p_i}\le1.
\]

Substituting `1/q_i=c_i`, `p_i=1/(1-c_i)`, `q_i=1/c_i`, and `a_i=\sqrt{c_i}` into (2.9)--(2.10), the factors `c_i^{c_i/2}` cancel **exactly**:

\[
a_i^{-c_i}\|\varphi_i\|_{q_i}
\le
(2\pi)^{c_i}(1-c_i)^{-(1-c_i)/2}.
\tag{2.11}
\]

Thus

\[
J
\le
(2\pi)^{\sum c_i}
\exp\left(
\frac12\sum_i[-(1-c_i)\log(1-c_i)]
\right).
\tag{2.12}
\]

For `0<=c<=1/2`,

\[
-(1-c)\log(1-c)\le c,
\tag{2.13}
\]

because the difference between the left side and `c` has derivative `log(1-c)<=0` and vanishes at zero. Since `sum c_i=3`,

\[
\boxed{
J\le(2\pi)^3e^{3/2}.
}
\tag{2.14}
\]

This is the key dimension-free aggregation: the small row scales that would make any one principal triple useless are exactly cancelled by the sharp Hausdorff--Young constants when all rows are used together.

### Step 3: three-dimensional Fresnel transform

For `t!=0`, the quadratic Fresnel identity in `R^3`, justified by Gaussian regularization, yields

\[
|\mathbb E e^{itY^T\Lambda Y}|
\le
\frac{1}{(4\pi|t|)^{3/2}\sqrt{|\det\Lambda|}}
\int_{R^3}|\psi_Y(\xi)|\,d\xi.
\tag{2.15}
\]

Since `|det Lambda|>=1`, (2.14) gives

\[
|\phi_Q(t)|
\le
\frac{(2\pi)^3e^{3/2}}{(4\pi|t|)^{3/2}}
=
\left(\frac{\pi e}{|t|}\right)^{3/2}.
\tag{2.16}
\]

Together with the trivial `|phi_Q(t)|<=1`, this proves (2.3).

The regularization is harmless because the right side of (2.15) is finite by (2.14); one may insert a Gaussian cutoff in the Fresnel representation and pass to the limit by the standard distributional identity plus dominated/Fatou bounds.

### Step 4: Fourier inversion

The majorant in (2.3) is integrable. Hence `Q` has a bounded continuous density and

\[
\begin{aligned}
\|p_Q\|_\infty
&\le {1\over2\pi}\int_R|\phi_Q(t)|\,dt\\
&\le {1\over\pi}\left[
\int_0^{\pi e}1\,dt
+
\int_{\pi e}^\infty(\pi e/t)^{3/2}\,dt
\right]\\
&={1\over\pi}(\pi e+2\pi e)
=3e.
\end{aligned}
\]

This proves (2.4). `QED`.

### Why this does not contradict the pointwise-decay correction

The correction `QFORM-POINTWISE-DECAY-FALSE` permits, for each fixed large frequency, a **single** one-dimensional law to align its square phase and make its quadratic characteristic function nearly one. In the diagonal three-variable case, the three leverage scores are `1,1,1`, so condition (2.2) fails maximally. Theorem 2.1 obtains pointwise decay only in the genuinely distributed regime, where every physical coordinate carries at most half of the three-dimensional spectral leverage and the full product of all characteristic factors is controlled collectively by Brascamp--Lieb plus sharp Hausdorff--Young.

## 3. Direct application to the fleet02/B15 flat obstruction

Fleet02/B15 constructs, for Sylvester-Hadamard orders, an `n x 3` matrix `U` with orthonormal columns and every row satisfying

\[
|u_i|^2={3\over n}.
\]

Its flat rank-three projector `A=UU^T` has exactly three nonzero eigenvalues, all equal to one, while every physical principal triple has smallest eigenvalue at most `3/n`. Thus fixed-triple conditioning necessarily loses dimension.

For every `n>=6`, however,

\[
\max_i|u_i|^2={3\over n}\le{1\over2}.
\]

Theorem 2.1 applies with `Lambda=I_3` and gives immediately

\[
\boxed{
\|p_{|U^TX|^2}\|_\infty\le3e,
}
\tag{3.1}
\]

uniformly in `n` and in all independent input densities bounded by one.

The same proof applies to the signed Hadamard rank-three family `U diag(1,1,-1)U^T` highlighted by other workers: signature does not enter the Brascamp--Lieb/Hausdorff--Young estimate, and `|det Lambda|=1` in the Fresnel step.

Thus the exact delocalized rank-three family that defeats every single-minor localization is **not** an obstruction to the conjecture: its distributed curvature can be aggregated dimension-freely, with explicit constant `3e`.

This substantively consumes fleet02/B15's exact source result: its Proposition 4.1 is the test family, and its unresolved aggregate-minor bridge is paid for this entire leverage-`<=1/2`, rank-three class by a different collective mechanism.

## 4. What is proved, and what remains unpaid

### Proved in this run

1. **Exact arbitrary-density extremal reduction.** For every nonnegative measurable kernel, and in particular every qform sublevel event, the supremum over independent densities bounded by one equals the supremum over products of arbitrary measure-one indicator sets. This is dimension-free and introduces no interval/symmetry assumption.
2. **Exact geometric target equivalence.** A universal `C|J|` bound for intersections of quadratic slabs with arbitrary measure-one product sets implies the full essential-supremum density conclusion.
3. **Collective rank-three smoothing.** If `A=U Lambda U^T` has rank exactly three, `|lambda_j|>=1`, and every coordinate leverage `|u_i|^2<=1/2`, then `||p_Q||_infinity<=3e`, with all signatures allowed.
4. **Flat Hadamard obstruction closed.** The fleet02/B15 delocalized rank-three projector family, for which every fixed principal triple degenerates like `1/n`, satisfies the universal `3e` density bound.

### Not proved

The full conjecture permits:

- a rank-three spectral subspace with one or more physical leverage scores `>1/2`;
- additional nonzero spectral directions outside the chosen three large eigenvalues, including small and opposite-sign directions;
- arbitrary cancellation/coupling from those extra directions.

Theorem 2.1 cannot simply discard those extra quadratic terms, because they depend on the same independent coordinates and therefore do not convolve independently with the selected rank-three piece.

### First exact missing implication

The next structural bridge is:

> **QFORM-HYBRID-LEVERAGE-EXTRA-DIRECTIONS-v1.** Starting from the exact product-set reduction (1.4), prove a dimension-free decomposition/conditioning inequality which either (a) retains a three-dimensional spectral block with effective leverage at most `1/2`, so Theorem 2.1 applies, or (b) exploits the few high-leverage physical coordinates without replacing the remaining dependent quadratic contribution by an uncharged convolution. The bridge must also allow the remaining spectral directions of the full matrix without discarding their dependence.

For the rank-exactly-three problem, the first unresolved case is therefore the **localized leverage regime** `max_i|u_i|^2>1/2`. For the owner's full matrix problem, one additionally needs a source-valid way to include the rest of `A`.

A promising route is to keep the product-set formulation and perform high-leverage coordinate slicing before the collective Fourier step, rather than selecting one fixed principal triple. Any such argument must pass the rank-two opposite-sign logarithmic control and must not reintroduce the refuted one-dimensional pointwise Fresnel bound.

## 5. Status

**Classification:** `ESSENTIAL_STEP_APPLIED / SUBSTANTIVE_PARTIAL_THEOREM`.

The arbitrary-law extremal reduction is complete, and a genuinely delocalized signed rank-three family is solved with an explicit dimension-free constant. This is not a proof of the full target. No novelty or publication-priority claim is made. No source-visible fleet02/B13 qform result existed at the coherent control pin, so none is attributed or invented.
