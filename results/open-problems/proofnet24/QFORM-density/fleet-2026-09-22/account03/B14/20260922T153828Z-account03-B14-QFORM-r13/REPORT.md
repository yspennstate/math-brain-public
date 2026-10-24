# account03/B14 — global convex-mixture localization without moments

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Control revision:** 2026-09-22.5  
**Run:** `20260922T153828Z-account03-B14-QFORM-r13`  
**Status:** `TARGET_LEVEL_LOCALIZATION / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections retained

The target remains: for every dimension n, every independent real coordinates with densities `0 <= f_i <= 1`, and every real symmetric matrix A with at least three eigenvalues satisfying `|lambda| >= 1`, prove a universal finite constant C such that

\[
  \Pr\{X^TAX\in I\}\le C|I|
\]

for every bounded interval I, or construct a genuine counterexample. Continuity of the output density is a separate desired conclusion and is not proved here.

This run uses control snapshot `yspennstate/math-research-brain@bc3ca7f6ed1225c1db91048541ec63466325e439`. It preserves the live corrections, especially: no law-uniform pointwise quadratic van-der-Corput bound; no false independence after spectral rotation; no dimension-free naive fiber-sup bound; no universal bounded support diameter; and no universal fixed fragment count for coordinatewise bathtub extremizers.

The completed partner input is account04/B14, report `yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`.
It proves, for every fixed interval I, the exact bathtub inequality

\[
 \Pr_f\{Q\in I\}
 \le \sup_{|E_1|=\cdots=|E_n|=1}
      \Pr_{1_{E_1},\ldots,1_{E_n}}\{Q\in I\},
\]

and shows that each measurable unit set can be approximated by compact finite unions of intervals with no loss of the optimal small-ball constant.

The new result below strengthens this from an interval-by-interval extremal statement to a **simultaneous law-level convex-mixture localization**.

## 2. Main theorem: one-dimensional convex extreme approximation

### Theorem 2.1

Let f be any probability density on R with

\[
0\le f\le1,\qquad \int_{\mathbb R}f=1.
\]

For every `eta>0` there are finitely many weights `theta_r >= 0`, summing to one, and compact finite unions of intervals `E_r` satisfying `|E_r|=1`, such that

\[
\left\|f-\sum_{r=1}^R\theta_r1_{E_r}\right\|_{L^1}<\eta.
\]

Moreover one may choose a positive integer N so that every E_r is, up to null endpoints, a union of exactly N grid cells of length `1/N`. The number R is finite but is not bounded universally; this is consistent with the already-proved no-fixed-fragment-count obstruction.

### Proof

#### Step 1: cap-preserving compactification with no moment assumption

Fix `eta>0`. Choose `R_0` so large that

\[
\delta:=\int_{|x|>R_0}f(x)\,dx<\eta/8.
\]

No moment bound is used; this is only tightness of a probability measure.

Let

\[
J=[R_0+1,R_0+3].
\]

Because `|J|=2` and `\int_J f <= 1`,

\[
 C_J:=\int_J(1-f)\,dx\ge1\ge\delta.
\]

Define

\[
 h(x)=\frac{\delta}{C_J}(1-f(x))1_J(x),
 \qquad
 \widetilde f(x)=f(x)1_{[-R_0,R_0]}(x)+h(x).
\]

Then `0<=h<=1-f` on J, hence `0<=\widetilde f<=1`; also

\[
\int\widetilde f=(1-\delta)+\delta=1.
\]

Its support is compact. Finally,

\[
\|f-\widetilde f\|_1
\le \int_{|x|>R_0}f+\int h
=2\delta<\eta/4.
\]

Thus arbitrary distant tails are removed without renormalizing the truncation and therefore without violating the density cap.

#### Step 2: exact mass-preserving grid projection

For each integer `N>=1`, let `P_N\widetilde f` be the conditional expectation of `\widetilde f` on the grid intervals

\[
 I_{k,N}=[k/N,(k+1)/N),\qquad k\in\mathbb Z.
\]

Write

\[
 s_N=P_N\widetilde f.
\]

Then

\[
0\le s_N\le1,\qquad \int s_N=1,
\]

and only finitely many grid cells have nonzero values because `\widetilde f` is compactly supported. Standard L1 convergence of refining conditional expectations (equivalently, density of step functions plus contractivity of conditional expectation) gives

\[
\|s_N-\widetilde f\|_1\longrightarrow0.
\]

Choose N large enough that this norm is below `eta/2`.

Let the finitely many relevant cells be `I_1,...,I_M`, and let the constant value of s_N on I_j be `a_j`. Since each cell has length `1/N`,

\[
0\le a_j\le1,
\qquad
\sum_{j=1}^M a_j=N.
\]

Hence `a=(a_1,...,a_M)` lies in the finite hypersimplex

\[
 H_{M,N}=\{u\in[0,1]^M:\sum_j u_j=N\}.
\]

#### Step 3: exact hypersimplex decomposition

Every extreme point of `H_{M,N}` is a 0-1 vector with exactly N ones. Indeed, if two coordinates are strictly between zero and one, one can perturb them by opposite sufficiently small amounts while preserving the coordinate box and the sum, contradicting extremality. Exactly one fractional coordinate is impossible because the coordinate sum is the integer N.

Therefore the finite polytope `H_{M,N}` is the convex hull of vectors `v^(r) in {0,1}^M` with exactly N ones. Thus

\[
 a=\sum_{r=1}^R\theta_r v^{(r)},
 \qquad \theta_r\ge0,\quad \sum_r\theta_r=1.
\]

By Caratheodory one may take R at most M, although no universal bound on M is asserted.

For each r, let E_r be the union of those grid cells whose coordinate in `v^(r)` equals one. Then E_r is a bounded finite union of N intervals of length `1/N`, so `|E_r|=1`, and, up to null boundary points,

\[
 s_N=\sum_r\theta_r1_{E_r}.
\]

Replacing half-open cells by closed cells changes no density in L1 and makes E_r compact. Combining the two approximation steps,

\[
\left\|f-\sum_r\theta_r1_{E_r}\right\|_1
\le2\delta+\|\widetilde f-s_N\|_1
<\eta.
\]

This proves Theorem 2.1.

## 3. Product version and total-variation control

### Theorem 3.1

Let `f_1,...,f_n` be arbitrary admissible probability densities. For every `epsilon>0` there exists a finite convex combination

\[
 G(x_1,\ldots,x_n)
 =\sum_{\alpha}\Theta_\alpha
   \prod_{i=1}^n1_{E_{i,\alpha_i}}(x_i),
\]

where each `E_{i,\alpha_i}` is a compact finite union of intervals of total length one, `Theta_alpha>=0`, and `sum_alpha Theta_alpha=1`, such that

\[
\left\|\prod_{i=1}^nf_i-G\right\|_{L^1(\mathbb R^n)}<\epsilon.
\]

Consequently, for every measurable map `T:R^n->R`,

\[
 d_{TV}\!\left(T_\#(\prod_i f_i\,dx_i),\ T_\#(G\,dx)\right)
 \le\frac{\epsilon}{2}.
\]

### Proof

Apply Theorem 2.1 to each f_i with errors `eta_i>0` satisfying `sum_i eta_i<epsilon`, obtaining probability densities

\[
 g_i=\sum_{r_i}\theta_{i,r_i}1_{E_{i,r_i}}.
\]

The elementary telescoping inequality for products of nonnegative L1-normalized functions gives

\[
\left\|\prod_i f_i-\prod_i g_i\right\|_1
\le\sum_i\|f_i-g_i\|_1
<\epsilon.
\]

Expanding the product yields

\[
\prod_i g_i
=\sum_{r_1,\ldots,r_n}
  \left(\prod_i\theta_{i,r_i}\right)
  \prod_i1_{E_{i,r_i}},
\]

which is the required finite convex mixture. Pushforward cannot increase total variation, so the final inequality follows.

This statement is uniform in the locations and separations of all fragments and in all translations. It assumes no moments, no support diameter, and no fixed component count.

## 4. Exact localization corollary for QFORM

Fix a real symmetric A and put `Q(x)=x^TAx`. Let `C_ext(A)` be the least constant such that

\[
 \Pr\{Q(U)\in I\}\le C_ext(A)|I|
\]

for every bounded interval I and every product law with marginal densities `1_{E_i}`, where each E_i is a compact finite union of intervals of total length one.

Then the least constant `C_all(A)` over **all** independent marginal densities `0<=f_i<=1` satisfies

\[
\boxed{C_{all}(A)=C_{ext}(A).}
\]

The inequality `C_ext(A)<=C_all(A)` is immediate because the extreme-product class is admissible. For the reverse inequality, approximate the entire product law by Theorem 3.1. If `mu` is the original Q-law and `mu_m` the approximating finite convex mixture of extreme-product Q-laws, then for every interval I,

\[
 \mu(I)\le\mu_m(I)+d_{TV}(\mu,\mu_m)
 \le C_ext(A)|I|+d_{TV}(\mu,\mu_m).
\]

Letting the approximation error tend to zero gives

\[
 \mu(I)\le C_ext(A)|I|.
\]

Thus the full arbitrary-density problem and the compact finite-fragment extreme-product problem have exactly the same best constant.

This explicitly applies the account04/B14 result to the target inequality. The partner bathtub theorem already gives the same equality interval-by-interval by sequential maximization. The new contribution is stronger in a different direction: the **whole input product law**, and hence the whole output law under Q, is a TV limit of finite convex mixtures of extreme-product laws. The approximating mixture does not depend on the test interval I. Therefore any argument that needs several output intervals, a finite family of test functions, or the complete output distribution can localize once rather than choose a new extremizer for each I.

## 5. Relation to translations, distant fragments and the previous obstruction

This theorem pays the exact localization obligation without introducing hidden compactness assumptions.

1. **Unbounded supports:** handled by the cap-preserving compactification. There is no renormalization factor above one and no moment assumption.
2. **Arbitrary translations:** the sets E_r may occur anywhere. The proof never recenters them, so translation costs are exactly zero at the localization stage.
3. **Distant fragments:** allowed. The compactification radius and the positions of grid cells depend on the input law and requested error.
4. **Fragment counts:** finite for each approximant but not uniformly bounded. In the grid construction every extreme set uses exactly N cells, with N tending upward as the approximation is refined. This is fully compatible with the correction `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`; no fixed M is asserted.
5. **Indefinite rotations:** untouched. A is never diagonalized and coordinate independence is never transferred through a rotation.

In particular, the previous no-fixed-fragment-count construction does not obstruct this theorem: it says no single universal M suffices for all target fibers, while the present theorem deliberately lets N depend on the law and approximation accuracy.

## 6. Density and continuity consequences

The partner report records the standard equivalence between the interval small-ball inequality and existence of an essentially bounded Radon--Nikodym density. Combining that equivalence with Section 4 shows that a universal bound proved on compact finite-fragment extreme products transfers with **exactly the same constant** to every admissible product density.

Continuity does **not** automatically pass from the extreme approximants under only TV convergence and a uniform L-infinity bound. Therefore this report proves no continuity statement for the full output density. A separate uniform modulus, Fourier-integrability statement, or another regularity argument would be required.

## 7. What remains for the full conjecture

The full conjecture remains OPEN. Localization itself is now exact at law level, but the geometric/analytic inequality on extreme product laws is unpaid:

> Prove one universal C such that `P(X^TAX in I)<=C|I|` for every symmetric A with at least three eigenvalues of absolute value at least one and every product of unit-measure compact finite-union indicator densities, uniformly in all component counts, positions and separations.

The theorem here says that solving that localized problem solves the original arbitrary-density problem with the same C; it does not solve the localized geometric inequality.

A useful downstream interface is: workers may now assume a finite convex mixture of compact grid-union product laws **for a finite-accuracy proof or certificate**, provided all estimates are uniform in the grid scale, support location and number of cells. Any estimate that depends on those localization parameters cannot be passed to the full conjecture.

## 8. Source pins

- Fresh control snapshot before publication: `yspennstate/math-research-brain@bc3ca7f6ed1225c1db91048541ec63466325e439`.
- Partner theorem: `yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`.
- Live correction inbox consumed at control snapshot above, including `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`.

No public release, scheduler mutation, email, Drive action, remote workflow, paid model/API/Codex call, or cross-account authentication is used by this result.
