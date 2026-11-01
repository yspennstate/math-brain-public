# Independent analytic audit: disjoint unions and exceptional Hamming layers

Date: 2026-10-02. Auditor: independent `union_chain_audit` agent.

**Verdict: PASS for both original drafts and for the subsequently requested
stronger projection/maximal-run theorem.** This certifies the arguments read
and reconstructed below, conditional on the established symmetric-function
FEI theorem. It does not certify research novelty, external peer review, or
FEI for arbitrary weighted finite-crossing functions.

Documents audited:

* `stripe_extension_union_lemma.md`;
* `stripe_extension_almost_symmetric_candidate.md`;
* the stronger maximal-run/projection formulation communicated separately by
  the author, reconstructed in Section 4 below.

The existing `hamming_band_fei.md` was read only to check the reusable entropy
comparison and influence normalization. The author's verification scripts
and their output were not used. Independent checks are in
`independent_union_chain_check.py` and `independent_union_chain_checks.json`.

## 1. Normalization and established input

Write

\[
H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2},\qquad
I(u)=\sum_S|S|\widehat u(S)^2.
\]

For arbitrary real functions, with each cube edge counted once,

\[
I(u)=\frac1{2^{n+1}}\sum_{\{x,y\}\text{ edge}}(u(x)-u(y))^2.
\]

For Boolean functions this is twice the number of changing undirected edges
divided by \(2^n\). Thus the edge normalizations used in both drafts are
correct.

I independently opened the primary manuscript
<https://www.cs.cmu.edu/~odonnell/papers/fei.pdf>. Its Theorem 1 states FEI for
all symmetric Boolean functions with constant 12.04, and its definitions use
base-two spectral entropy and the same total influence. The theorem applies
to arbitrary symmetric label sequences, without monotonicity or bias
conditions.

## 2. Disjoint-union entropy: PASS

For disjoint \(E_1,\dots,E_r\), put \(g_j=1-2\mathbf1_{E_j}\) and
\(f=1-2\mathbf1_{\cup_jE_j}\). For nonempty \(S\),

\[
\widehat f(S)=\sum_j\widehat g_j(S).
\]

This equality deliberately excludes the empty set; the constants do not
sum in the same way. The draft handles that term separately, correctly.

Let \(a=\widehat f(S)^2\), \(b_j=\widehat g_j(S)^2\), and
\(u=\sum_jb_j\). Cauchy–Schwarz gives \(a\le ru\), and Boolean
normalization gives \(a,b_j\in[0,1]\). For
\(e(t)=t\log_2(1/t)\), when \(0<u\le1\), write \(a=tu\):

\[
e(a)=t e(u)-ut\log_2t
\le r e(u)+\frac{\log_2e}{e}u
\le r\sum_j e(b_j)+\frac{\log_2e}{e}u.
\]

The use of \(e(u)\ge0\), the maximum of \(-t\ln t\), and the last
inequality all have the required signs. If \(u>1\), the entropy term is
at most \((\log_2e)/e\), while \(\sum_j e(b_j)\ge0\); the same bound
follows. If \(u=0\), all terms vanish. No division by zero remains.

The empty Fourier term satisfies

\[
e(\widehat f(\varnothing)^2)
=e(1-\operatorname{Var}f)
\le (\log_2e)\operatorname{Var}f.
\]

This follows from \(-(1-v)\ln(1-v)\le v\), valid for \(0\le v\le1\)
with the limiting convention at \(v=1\). If \(p_j=\Pr(E_j)\), then
disjointness gives \(p=\sum_jp_j\le1\), and

\[
\operatorname{Var}f=4p(1-p)
\le4\sum_jp_j(1-p_j)=\sum_j\operatorname{Var}g_j.
\]

Therefore the claimed inequality

\[
H(f)\le r\sum_jH(g_j)
+(\log_2e)(1+1/e)\sum_j\operatorname{Var}g_j
\]

is valid, including empty components, a full union, either majority label,
and constant functions. The natural statement takes \(r\ge1\); an empty
family gives a constant function and is trivial separately.

### Boundary additivity and wide gaps

The influence identity holds exactly when no edge joins distinct components.
More generally, if \(J\) is the number of such joining undirected edges,

\[
\sum_j I(g_j)-I(f)=\frac{4J}{2^n}.
\]

Each joining edge contributes to two component boundaries and to no union
boundary. This confirms both the draft's identity under its hypothesis and
its caution about cancellation without that hypothesis.

Poincaré gives \(\operatorname{Var}g_j\le I(g_j)\). Thus, if every component
has FEI constant \(C\), the union has constant
\(rC+(\log_2e)(1+1/e)\) under the no-joining-edge condition.

A score edge changes by at most \(2w_{\max}\). Strictly larger gaps
therefore prevent joining edges for all endpoint conventions. Equality in
the gap bound would require an additional endpoint analysis and is properly
excluded. The application to slabs is conditional on the separate slab
theorem; this audit does not use the slab proof to prove the union lemma.

## 3. Original arbitrary-layer theorem: PASS

For a uniformly random coordinate permutation \(\Pi\), its maximal-chain
point \(X_r^\Pi\) is uniform on layer \(r\), and its edge
\((X_r^\Pi,X_{r+1}^\Pi)\) is uniform among the
\((n-r)\binom nr\) edges between the two layers. Consequently the
symmetric comparator \(g_\Pi(x)=f(X_{r(x)}^\Pi)\) has the correct
layer marginal and satisfies

\[
\mathbb E_\Pi I(g_\Pi)=I(f).
\]

No monotonicity enters this counting argument. If \(f\) is constant on a
layer, every chain comparator agrees with it throughout that layer, so
\(f-g_\Pi\) has the required support.

The large-dimension adjacency estimate applies to noncontiguous layers:
the induced layer graph is a disjoint union of paths, with each block no
longer than the total number of exceptional layers. Cauchy–Schwarz bounds
its edge blocks for arbitrary signed real functions. The factor
\((n+1)\cos(\pi/(k+1))\) and the influence factor \(1/2\) are correct.

For the small-dimension argument, let \(\delta_\Pi=\Pr(f\ne g_\Pi)\).
At a fixed layer with positive fraction \(q_r\), both the mean disagreement
with \(f\) and the mean disagreement of two independent comparators equal
\(2q_r(1-q_r)\). Thus

\[
\mathbb E D(\Pi,\Pi')=\mathbb E\delta_\Pi,
\qquad \mathbb E_\Pi\mathbb E g_\Pi=\mathbb E f.
\]

The inequality \(|\mathbb E g_\Pi-\mathbb E g_{\Pi'}|\le2D\) does not
require nested functions. It gives

\[
\operatorname{Var}_\Pi(\mathbb E g_\Pi)
\le2\mathbb E D^2\le2\mathbb E\delta_\Pi.
\]

Since \(\|f-g_\Pi\|_2^2=4\delta_\Pi\),

\[
\mathbb E\operatorname{Var}(f-g_\Pi)
=4\mathbb E\delta_\Pi-
\operatorname{Var}_\Pi(\mathbb E g_\Pi)
\ge2\mathbb E\delta_\Pi.
\]

All mean terms and factors are correct. Poincaré and the conservative
quadratic bound \(\mathbb E I(f-g_\Pi)\le4I(f)\) prove the claimed
small-dimension estimate. Averaging the entropy comparison proves the
original \(25+64(k+1)^2\) FEI constant.

The inherited entropy comparison was also reconstructed: domination of one
spectral probability law by \(2(1+4\delta)\) times the mixture law, entropy
concavity, the mixture bound, and \(\delta\ge2^{-n}\) give
\(H(f)\le2H(g)+32n\delta\). It includes the empty coefficient and all
\(0\le\delta\le1\); the zero-disagreement case is handled separately.

## 4. Strong projection and maximal-run version: PASS

Let \(P=P_{\mathrm{sym}}\) be coordinate-permutation averaging, and let
\(h=Pf\). Set

\[
D=I(f)-I(h),\qquad
\ell=\text{largest number of consecutive exceptional layers}.
\]

The projection \(P\) is orthogonal and commutes with cube adjacency and
with \(L=(n\mathrm{Id}-A)/2\), the operator satisfying
\(I(u)=\langle u,Lu\rangle\). Hence

\[
D=I(f-h)\ge0.
\]

The chain marginals give \(\mathbb E_\Pi g_\Pi=h\). Using the exact
influence identity above,

\[
\begin{aligned}
\mathbb E_\Pi I(f-g_\Pi)
&=I(f)+\mathbb E I(g_\Pi)-2\langle f,Lh\rangle\\
&=2I(f)-2I(h)=2D.
\end{aligned}
\]

Here \(\langle f,Lh\rangle=\langle h,Lh\rangle\) follows from
orthogonality and commutation; the formula does not assume that \(h\) is
Boolean.

Every connected component of the induced layer path has at most \(\ell\)
vertices. Its top path eigenvalue is therefore at most
\(2\cos(\pi/(\ell+1))\). The previous Cauchy–Schwarz argument gives

\[
\langle u,Au\rangle
\le(n+1)\cos\frac{\pi}{\ell+1}\,\|u\|_2^2
\]

for every \(u\) supported on the exceptional layers, including separated
blocks with arbitrary labels. Put \(s=\ell+1\ge2\). Since
\(1-\cos(\pi/s)\ge2/s^2\), when \(n\ge s^2\),

\[
n-(n+1)\cos(\pi/s)
\ge 2(n+1)/s^2-1\ge n/s^2.
\]

Thus \(I(u)\ge n\|u\|_2^2/(2s^2)\). Applying this to each difference
and averaging gives

\[
2D\ge\frac{2n}{s^2}\mathbb E\delta_\Pi,
\qquad n\mathbb E\delta_\Pi\le s^2D.
\]

For \(n<s^2\), the valid variance bound in Section 3 and Poincaré give
\(2D\ge2\mathbb E\delta_\Pi\), hence again
\(n\mathbb E\delta_\Pi\le s^2D\). Therefore

\[
\boxed{H(f)\le24.08I(f)+32(\ell+1)^2D
\le[25+32(\ell+1)^2]I(f).}
\]

For \(\ell=1\), there are no induced edges at all. Then
\(\langle u,Au\rangle=0\), so
\(I(u)=n\|u\|_2^2/2\) in every dimension. Averaging yields the stronger
exact identity

\[
\boxed{n\mathbb E\delta_\Pi=D.}
\]

Consequently
\(H(f)\le24.08I(f)+32D\le56.08I(f)<57I(f)\). This includes arbitrarily
many exceptional layers if none are consecutive.

For \(\ell=0\), \(f\) is symmetric, every comparator equals \(f\), and
\(D=\delta=0\); use the established sharper constant 12.04 directly.
For \(n=0\), the cube has one point and every Boolean function is constant,
so \(H=I=0\). End layers contain one point and therefore can never be
genuinely nonsymmetric. If the declared exceptional set contains surplus
layers, the bounds remain valid, albeit less sharp.

## 5. Finite-crossing weighted consequence and endpoint wording

The weighted corollary is valid under the usual precise interpretation:
there is a set of at most \(m\) real crossing points such that
\(F:\mathbb R\to\{-1,+1\}\) is constant on each complementary open
interval, with arbitrary labels allowed at the crossing points themselves.
The word “crossings” should be accompanied by this definition in the final
statement. Merely counting sign reversals without controlling isolated
point anomalies would not express the needed hypothesis.

After sign changes, removal of zero weights, and scaling by \(c>0\), the
score lies within \(A=\sum_i|w_i/c-1|\) of \(2r-n\). Any layer whose
closed score interval avoids every crossing lies inside one constant-label
interval, and therefore is symmetric. For one crossing, eligible centers
are lattice points of spacing two in an interval of length \(2A\), so
their number is at most \(\lfloor A\rfloor+1\). Closed intervals correctly
cover every attained endpoint and arbitrary point label. Taking a union
over crossings gives \(k\le m(\lfloor A\rfloor+1)\), and hence also bounds
the longest exceptional run. There is no spacing or bias restriction.

When \(A=0\), weighted score is exactly a function of Hamming layer, so
the function is symmetric for every allowed \(F\), including endpoint
assignments. The 12.04 constant applies directly. Constancy, zero dimension,
and all-zero original weights are also covered separately.

## 6. Independent finite verification

The checker independently constructs cube edges, maximal chains, truth
tables, and Walsh transforms. It uses integer arithmetic for all chain,
variance, boundary-cancellation, projection-energy, and maximal-run
identities. The Fourier-sign convention is irrelevant for the squared
entropy coefficients.

Completed checks:

* all 65,812 Boolean functions in dimensions 1 through 4, each averaged over
  every maximal chain;
* 4,000 additional functions in dimensions 5 and 6, again using every chain,
  including constants and rare events;
* all 65,808 assignments to three disjoint components plus the exterior in
  dimensions 1 through 3, and 10,000 larger random assignments: 75,808 total;
* every nonempty subset of Hamming layers through dimension 12: 16,368
  induced adjacency matrices, checked against the longest-run bound;
* 3,000 weighted finite-crossing examples through dimension 10, with every
  crossing chosen at an attained score and arbitrary endpoint labels.

All checks passed. Chain influence and marginal identities, the variance
inequality, the exact \(2D\) projection formula, the strengthened maximal-run
bound, the exact isolated-layer identity, and the joining-edge cancellation
formula held with integer arithmetic. Union entropy residuals were at most
zero in floating point, and the largest adjacency residual was approximately
\(-1.22\times10^{-16}\). Floating-point entropy and eigenvalue checks used
tolerances only for their numerical evaluation. These checks supplement the
analytic proof; they are not the justification for unbounded dimension.
