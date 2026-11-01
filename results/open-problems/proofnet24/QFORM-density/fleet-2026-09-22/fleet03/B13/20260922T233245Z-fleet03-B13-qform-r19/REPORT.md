# fleet03/B13 — countable no-pivot extreme-product reduction

Run: `20260922T233245Z-fleet03-B13-qform-r19`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED TARGET-LEVEL REDUCTION / FULL QFORM OPEN / CONTINUITY OPEN**

## 1. Sources and scope

The owner target is the following uniform statement. For every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove

\[
  \Pr\{X^TAX\in J\}\le C|J|
\]

for one universal finite `C`, all intervals `J`, or give a genuine counterexample. No moment, compact-support, log-concavity, connected-support, Gaussian, or post-rotation-independence hypothesis is allowed.


The two mathematical inputs actually applied are:

1. **fleet04/B13 rough geometric transfer**, `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`. Its Lemma 2.1/Corollary 2.2 prove, without an attained infinite-line bathtub maximizer, that every cap-one mass-one density is an `L1` limit of finite convex combinations of indicators of bounded finite unions of intervals of measure one, and hence bounded product functionals have the same supremum on those extreme products.
2. **Newest no-pivot synthesis**, first added at `yspennstate/math-open-problems@29e682234ef18500588293f4e947e79ca768a251`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`. Its Theorem 5.1, using the supplied one-eigenvalue small-ball estimate, reduces full QFORM to a single no-pivot three-large-eigenvalue density statement and gives an explicit constant transfer.

The live corrections excluding uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, worst conditional projection-density moments, post-rotation independence, and universal single-minor selection are retained. None is used below.

## 2. No-pivot slab constants

Fix `tau in (0,1]`. Say that a symmetric matrix `A` is **strictly no-tau-pivot** if

\[
 |A_{ii}|<\tau\quad\text{for every }i,
 \qquad
 |\det A_{\{i,j\},\{i,j\}}|<\tau\quad\text{for every }i\ne j.
\tag{2.1}
\]

Let `C_np(tau)` be the supremum of

\[
 \frac{\Pr\{X^TAX\in J\}}{|J|}
\tag{2.2}
\]

over all finite dimensions, all independent cap-one marginal laws, all nondegenerate intervals `J`, and all strictly no-tau-pivot symmetric `A` with `s_3(A)>=1`.

Define the following countable class `G_tau`. A datum belongs to `G_tau` when:

- `n` is a positive integer;
- `B` is a rational symmetric `n x n` matrix satisfying (2.1) and `s_3(B)>1`;
- `K=[u,v]` has rational endpoints `u<v`;
- one integer `M>=1` is chosen, and for each coordinate a finite set `S_i subset Z` with `|S_i|=M` is chosen;
- `E_i=union_{k in S_i}[k/M,(k+1)/M)`, so `|E_i|=1`;
- the input density is exactly `prod_i 1_{E_i}`.

Let

\[
 C_{\rm grid}(\tau)
 =\sup_{G_\tau}
 \frac{|\{x\in\prod_iE_i:x^TBx\in K\}|}{|K|}.
\tag{2.3}
\]

The class is countable. It imposes **no uniform bound** on `M`, translations, support radius, gaps, or number of connected components.

## 3. Main theorem — exact countable reduction

### Theorem 3.1 — `QFORM-NOPIVOT-COUNTABLE-EXTREME-EQUIVALENCE-v1`

For every fixed rational `tau in (0,1]`,

\[
 \boxed{C_{\rm np}(\tau)=C_{\rm grid}(\tau).}
\tag{3.1}
\]

The same equality holds for quadratic-affine maps `x^TAx+2b^Tx+c` if `b,c` are also rationalized in the grid class.

### Proof

The inequality `C_grid<=C_np` is immediate. We prove the reverse inequality by showing that every strict slab-ratio witness can be replaced by a datum in `G_tau` with arbitrarily small loss.

Fix `R<C_np(tau)`. Choose a no-tau-pivot witness `(A,f_1,...,f_n,J)` with ratio `L>R`.

#### Step 1: open a spectral cushion without leaving the no-pivot class

Write

\[
 d_1=\max_i|A_{ii}|<\tau,
 \qquad
 d_2=\max_{i<j}|\det A_{ij}|<\tau.
\]

Because both inequalities are strict and there are finitely many coordinates, choose `s>1` so close to one that

\[
 sd_1<\tau,
 \qquad
 s^2d_2<\tau,
 \qquad
 L/s>R.
\tag{3.2}
\]

Put `A_1=sA` and `J_1=sJ`. Then

\[
 \{x:x^TA_1x\in J_1\}=\{x:x^TAx\in J\},
\]

`s_3(A_1)>1`, `A_1` is still strictly no-tau-pivot, and the slab ratio becomes `L/s>R`.

#### Step 2: purify the arbitrary marginals with no global optimizer

Apply the completed fleet04/B13 Corollary 2.2 to the bounded kernel

\[
 K(x)=1_{\{x^TA_1x\in J_1\}}.
\]

Its equality of suprema implies that there exist bounded finite unions of intervals `E_i`, each of measure one, such that

\[
 q:=|\{x\in P:x^TA_1x\in J_1\}|>R|J_1|,
 \qquad P=\prod_iE_i.
\tag{3.3}
\]

No threshold set is assumed to attain a global bathtub supremum. The sets may have arbitrarily large diameter and arbitrarily many fragments.

#### Step 3: rationalize the matrix and target interval on the compact product support

The set `P` is bounded. Since `s_3(A_1)>1` and all inequalities in (2.1) are strict, there is an open neighborhood of `A_1` in the finite-dimensional space of symmetric matrices in which both properties remain true. Rational symmetric matrices are dense, so choose rational `B` in this neighborhood and also so close that

\[
 \sup_{x\in P}|x^T(B-A_1)x|<\delta.
\tag{3.4}
\]

Because `q/R>|J_1|`, choose `delta>0` small enough and then a rational interval `K` containing the `delta`-enlargement of `J_1` with

\[
 |K|<q/R.
\tag{3.5}
\]

The inclusion

\[
 \{x\in P:x^TA_1x\in J_1\}
 \subset
 \{x\in P:x^TBx\in K\}
\tag{3.6}
\]

therefore gives

\[
 |\{x\in P:x^TBx\in K\}|>R|K|.
\tag{3.7}
\]

This one-sided argument avoids any assumption that a quadratic level set has zero boundary mass under an intermediate approximation.

#### Step 4: pass to a common rational grid and then to one extreme tuple

For a common mesh `1/M`, let `g_{i,M}` be the conditional expectation of `1_{E_i}` on the grid cells `[k/M,(k+1)/M)`. Since `E_i` is bounded, only finitely many coefficients are nonzero, and

\[
 0\le g_{i,M}\le1,
 \qquad
 \int g_{i,M}=1,
 \qquad
 \|g_{i,M}-1_{E_i}\|_1\to0.
\tag{3.8}
\]

The product densities satisfy the telescoping estimate

\[
 \left\|\prod_i g_{i,M}-\prod_i1_{E_i}\right\|_1
 \le\sum_i\|g_{i,M}-1_{E_i}\|_1.
\tag{3.9}
\]

Choose `M` large enough that the grid-product probability of the fixed event in (3.7) remains greater than `R|K|`.

Write

\[
 g_{i,M}=\sum_k a_{ik}1_{[k/M,(k+1)/M)},
 \qquad 0\le a_{ik}\le1.
\]

The mass constraint is

\[
 \sum_k a_{ik}=M.
\tag{3.10}
\]

Thus the finite coefficient vector lies in the hypersimplex `{a in [0,1]^N: sum a=M}`. Its extreme points are exactly the zero-one vectors with `M` ones. Hence each `g_{i,M}` is a finite convex combination of indicators of unions of exactly `M` grid cells, each union having measure one.

Expanding the product gives a finite convex combination of product-indicator laws. Since their weighted average assigns probability greater than `R|K|` to the slab event, at least one extreme tuple `(E'_1,...,E'_n)` satisfies

\[
 |\{x\in\prod_iE'_i:x^TBx\in K\}|>R|K|.
\tag{3.11}
\]

This tuple, together with rational `B,K` and the common integer `M`, is a datum in `G_tau`. Since every `R<C_np(tau)` is beaten by a grid datum, `C_np<=C_grid`, proving (3.1). ∎

### Affine extension

For `x^TAx+2b^Tx+c`, Steps 1-4 are unchanged after scaling the whole polynomial and rationally approximating `b,c` together with `A` on the compact set `P`. Thus conditioning-generated affine leakage does not break the countable reduction.

## 4. Application to the newest no-pivot synthesis

The newest geometric synthesis proves, subject to its completed one-eigenvalue small-ball input, that a bound `C_0` for the no-tau-pivot three-eigenvalue class implies the full conjecture with

\[
 C_{\rm full}
 \le
 \tau^{-1/2}
 \max\{1+2e^\pi C_0,\ 1+3K_\tau\},
\qquad
 K_\tau=\frac{2}{\sqrt\tau}\bigl[6.2+\log_+(16\sqrt\tau)\bigr].
\tag{4.1}
\]

By Theorem 3.1 one may take `C_0=C_grid(tau)`. Therefore the current full proof graph has been reduced to a **countable finite geometric problem**:

\[
 \boxed{
 C_{\rm grid}(\tau)<\infty
 \quad\Longrightarrow\quad
 C_{\rm full}<\infty.
 }
\tag{4.2}
\]

The converse is immediate because the grid class is a subclass of QFORM. Hence, with the supplied no-pivot synthesis as a dependency, full QFORM essential boundedness is equivalent to finiteness of this countable extreme-product no-pivot slab supremum.

For the concrete choice

\[
 \tau=\frac1{16},
\]

the arithmetic check gives

\[
 K_\tau=60.690354888959128\ldots,
 \qquad
 1+3K_\tau=183.071064666877390\ldots,
\]

and therefore

\[
 \boxed{
 C_{\rm full}
 \le
 \max\{4+185.125541062234134\,C_{\rm grid}(1/16),\
        732.284258667509562\}.
 }
\tag{4.3}
\]

The companion deterministic script `check_transfer.py` and its saved output terminate with `QFORM_B13_R19_TRANSFER_CHECK_PASS`.

## 5. Counterexample localization corollary

If the original QFORM universal essential-density bound is false, then under the completed no-pivot reduction

\[
 C_{\rm grid}(1/16)=\infty.
\]

Equivalently, for every `N` there is a **fully finite rational witness** consisting of a rational strictly no-`1/16`-pivot matrix with `s_3>1`, a rational target interval, and finite rational-grid unit-measure product sets, whose slab ratio exceeds `N`.

Thus rough one-dimensional densities, irrational coefficients, and an attained infinite-line extremizer are not places where a counterexample can hide. Any blow-up can be localized to a finite combinatorial-geometric witness. What cannot be imposed is a uniform bound on mesh denominator, support radius, translation, separation, or fragment count.

## 6. What this does and does not prove

**Proved in this run:**

1. exact equality of the no-pivot arbitrary-law slab supremum with a countable rational finite-grid extreme-product supremum;
2. the same reduction with arbitrary affine leakage;
3. an explicit application of the newest full-to-no-pivot theorem giving (4.3);
4. finite rational counterexample localization if the universal bound fails.

**Not proved:** `C_grid(1/16)<infinity`. Therefore **full QFORM remains OPEN**. The separate existence of a continuous representative for the full output density also remains **OPEN**; this reduction concerns interval domination / essential boundedness.

The next B13 obligation is now exact: prove a constant independent of `n,M`, support radius, translations, gaps and fragment count for

\[
 |\{x\in\prod_iE_i:x^TBx\in K\}|\le C|K|
\tag{6.1}
\]

on the strict no-`1/16`-pivot rational grid class, or construct a sequence of such finite witnesses with ratios tending to infinity. The most relevant live tools are the volume-sampling `D'`/`D_5` bounds and hub/mixed-Fresnel certificates; any use must preserve the same original-coordinate product grid rather than pass to an arbitrary spectral joint density.

No scheduler state, notification state, email/Drive delivery, public release, remote workflow, paid API/model call, or Codex execution was used or changed in this mathematical run.
