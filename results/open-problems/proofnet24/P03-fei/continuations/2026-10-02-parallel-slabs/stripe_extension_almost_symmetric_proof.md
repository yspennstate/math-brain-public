# FEI with finitely many nonsymmetric Hamming layers

Date: 2026-10-02. **Complete proof, internally audited; novelty unverified.**

This removes monotonicity and contiguity from the [completed Hamming-band theorem](../2026-10-02-hamming-band/hamming_band_fei.md). It also gives a finite-crossing consequence for
weighted sums with bounded total deviation from equal weights. All input
distributions are uniform on the cube; entropy logarithms are base 2.

The [earlier candidate](stripe_extension_almost_symmetric_candidate.md)
is preserved with its weaker constant. Internal analytic checks are
recorded in the [author review](stripe_union_and_chain_author_review.md)
and [heat/entropy audit](stripe_almost_symmetric_heat_audit.md), with separate
[root review](stripe_union_chain_root_audit.md) and
[maximum-run audit](stripe_chain_maxrun_heat_audit.md), plus a full
[second analytic audit](union_chain_independent_audit.md).
The [finite checker](stripe_extension_verify_union_and_chains.py) and its
[results](stripe_extension_union_and_chains_verification.json) test 616
functions against 47,172 fully enumerated maximal chains through
dimension 6. These checks do not certify research novelty or replace
external peer review.
The separately written [independent checker](independent_union_chain_check.py)
and its [results](independent_union_chain_checks.json) test all 65,812 Boolean
functions through dimension 4, 4,000 additional functions in dimensions
5 and 6, 16,368 subsets of Hamming layers, and 3,000 attained-crossing
weighted-score examples. Integer chain/boundary identities and the
projection and maximum-run entropy bounds all pass.

## Theorem

Let \(f:\{-1,+1\}^n\to\{-1,+1\}\) be arbitrary. Suppose there is a set
\(\Lambda\subseteq\{0,\ldots,n\}\) of size at most \(k\) such that
\(f\) is constant on every Hamming layer outside \(\Lambda\). Its
constant label may vary arbitrarily between layers. Then
\[
 \boxed{H(f)\le\bigl(25+32(k+1)^2\bigr)I(f).}\tag{1}
\]
For \(k=0\), use the established symmetric-function FEI constant 12.04
directly. Constants and \(n=0\) are immediate; below \(n\ge1\).

The only established FEI input is Theorem 1 of Ryan O'Donnell, John Wright,
and Yuan Zhou, *The Fourier Entropy–Influence Conjecture for certain
classes of Boolean functions* (ICALP 2011):
\(H(g)\le12.04 I(g)\) for every symmetric Boolean function. The primary
author-hosted paper is
<https://people.eecs.berkeley.edu/~jswright/papers/fei.pdf>, PDF page 3
(printed page 2). The entropy comparison
\[
 H(f)\le2H(g)+32n\Pr(f\ne g)\tag{2}
\]
for arbitrary Boolean \(f,g\) was proved in Section 1 of
[the earlier Hamming-band proof](../2026-10-02-hamming-band/hamming_band_fei.md) and is reused unchanged.

Here is its proof, so this note is self-contained. Write \(\delta=\Pr(f\ne g)\)
and \(d=f-g\), so \(\|d\|_2^2=4\delta\). If \(\delta=0\), (2) is
immediate. Otherwise put \(M=1+4\delta\) and form the probability laws
\[
 Q_S=\widehat f(S)^2,\qquad
 P_S=\frac{\widehat g(S)^2+\widehat d(S)^2}{M}.
\]
The inequality \((b+c)^2\le2(b^2+c^2)\) gives \(Q\le2M P\).
If probability laws satisfy \(Q\le K P\), then
\(P=Q/K+(1-1/K)R\) for another probability law, so entropy concavity
and nonnegativity give \(H(Q)\le K H(P)\). Apply this with \(K=2M\),
then the entropy upper bound for a mixture, to obtain
\[
 H(f)\le2H(g)+8\delta H\left(\frac{\widehat d^2}{4\delta}\right)
       +2M h_2(4\delta/M)
 \le2H(g)+8\delta n+2M h_2(4\delta/M).
\]
The normalized difference spectrum is a law on \(2^n\) sets, giving the
last inequality. Because \(\delta>0\) is a cube probability,
\(\delta\ge2^{-n}\), and also \(\delta\le1\). Consequently
\[
 \begin{aligned}
 2M h_2(4\delta/M)
 &=2\log_2 M+8\delta\log_2\frac{M}{4\delta}\\
 &\le8\delta\left(\log_2e+\log_2(1/\delta)+\log_2(5/4)\right)\\
 &\le8\delta\left(n+\log_2e+\log_2(5/4)\right).
 \end{aligned}
\]
Together with \(8\delta n\), this is less than \(32\delta n\) for
\(n\ge1\), proving (2).

## 1. Random maximal chains give symmetric comparators with exact influence

Choose a uniformly random permutation \(\Pi\) of the \(n\) coordinates.
Let \(X_r^\Pi\) be the cube point whose positive coordinates are the
first \(r\) elements of \(\Pi\), for \(0\le r\le n\). These points
form a maximal chain. Define the symmetric Boolean comparator
\[
 g_\Pi(x)=f(X_{r(x)}^\Pi),\qquad
 r(x)=\#\{i:x_i=+1\}.
\]
The sequence of labels \(g_\Pi(r)\) need not be monotone.

At a fixed layer \(r\), the chain point \(X_r^\Pi\) is uniform on that
layer. Thus, for \(q_r=\Pr(f=+1\mid r)\),
\[
 \Pr_\Pi(g_\Pi(r)=+1)=q_r.\tag{3}
\]
In particular, \(d_\Pi=f-g_\Pi\) is supported on \(\Lambda\).

The random edge \((X_r^\Pi,X_{r+1}^\Pi)\) is uniform among all edges
between layers \(r\) and \(r+1\). There are
\((n-r)\binom nr\) such edges. A symmetric function contributes
\(2(n-r)2^{-n}\binom nr\) to total influence precisely when its labels
on those two layers differ. Averaging over the chain therefore yields
\[
 \boxed{\mathbb E_\Pi I(g_\Pi)=I(f).}\tag{4}
\]
This counts changing edges without using monotonicity.

### A sharper exact Dirichlet identity

For real functions let
\(I(u)=\sum_S|S|\widehat u(S)^2=\langle u,\mathcal L u\rangle\),
where \(\mathcal L u=\tfrac12\sum_i(u-u^{\oplus i})\) is the cube
Laplacian with eigenvalue \(|S|\) on \(\chi_S\). Let \(P_{\rm sym}\)
be the average of all coordinate-permutation operators. This is the
self-adjoint orthogonal projection onto symmetric functions: group
averaging is idempotent, and inverses occur with the same uniform law.
Each coordinate permutation commutes with \(\mathcal L\), so
\(P_{\rm sym}\) does too.

Equation (3) says \(\mathbb E_\Pi g_\Pi=P_{\rm sym}f\). Therefore,
using (4),
\[
 \begin{aligned}
 \mathbb E_\Pi I(d_\Pi)
 &=I(f)+\mathbb E_\Pi I(g_\Pi)
       -2\langle f,\mathcal L\mathbb E_\Pi g_\Pi\rangle\\
 &=2I(f)-2\langle f,\mathcal L P_{\rm sym}f\rangle\\
 &=2I(f)-2\langle P_{\rm sym}f,\mathcal L P_{\rm sym}f\rangle.
 \end{aligned}
\]
The last equality holds because \(\mathcal L P_{\rm sym}f\) lies in the
range of the orthogonal projection. Consequently,
\[
 \boxed{\mathbb E_\Pi I(d_\Pi)
       =2[I(f)-I(P_{\rm sym}f)]\le2I(f).}\tag{5}
\]

## 2. Mean disagreement is controlled by the exceptional layers

Set \(\delta_\Pi=\Pr(f\ne g_\Pi)\). We prove
\[
 n\mathbb E_\Pi\delta_\Pi\le(k+1)^2 I(f).\tag{6}
\]

For large dimension, the adjacency argument from the band proof applies
to any real function \(u\) supported on the layers in \(\Lambda\).
Let \(A\) be cube adjacency and put
\(v_r^2=2^{-n}\sum_{r(x)=r}u(x)^2\). Cauchy–Schwarz on each interlayer
edge set gives
\[
 \langle u,Au\rangle
 \le2\sum_r\sqrt{(n-r)(r+1)}\,v_rv_{r+1}
 \le(n+1)\sum_r v_rv_{r+1}.
\]
The induced layer path is a disjoint union of consecutive blocks, each
having at most \(k\) vertices. Its top adjacency eigenvalue is at most
\(2\cos(\pi/(k+1))\), so the preceding bound gives
\[
 \langle u,Au\rangle
 \le(n+1)\cos(\pi/(k+1))\|u\|_2^2.
\]
Using \(I(u)=\tfrac12(n\|u\|_2^2-\langle u,Au\rangle)\) and
\(1-\cos(\pi/(k+1))\ge2/(k+1)^2\), when \(n\ge(k+1)^2\),
\[
 I(u)\ge\frac{n}{2(k+1)^2}\|u\|_2^2.\tag{7}
\]
Using \(\|d_\Pi\|_2^2=4\delta_\Pi\), averaging (7), and applying (5)
proves (6) in this regime.

For small dimension, let \(\Pi,\Pi'\) be independent and write
\(D(\Pi,\Pi')=\Pr(g_\Pi\ne g_{\Pi'})\). Equation (3) implies
\[
 \mathbb E_{\Pi,\Pi'}D(\Pi,\Pi')
 =\mathbb E_\Pi\delta_\Pi,
\]
because both conditional probabilities at a layer equal
\(2q_r(1-q_r)\). Also \(\mathbb E_\Pi\mathbb E g_\Pi=\mathbb E f\).
The comparators are not nested; use the always-valid inequality
\[
 |\mathbb E g_\Pi-\mathbb E g_{\Pi'}|
 \le2D(\Pi,\Pi')
\]
in place of the equality available for monotone thresholds. Thus
\[
 \begin{aligned}
 \operatorname{Var}_\Pi(\mathbb E g_\Pi)
 &=\tfrac12\mathbb E_{\Pi,\Pi'}
       (\mathbb E g_\Pi-\mathbb E g_{\Pi'})^2\\
 &\le2\mathbb E_{\Pi,\Pi'}D(\Pi,\Pi')^2\\
 &\le2\mathbb E_\Pi\delta_\Pi.
 \end{aligned}
\]
It follows that
\[
 \mathbb E_\Pi\operatorname{Var}(d_\Pi)
 =4\mathbb E_\Pi\delta_\Pi
       -\operatorname{Var}_\Pi(\mathbb E g_\Pi)
 \ge2\mathbb E_\Pi\delta_\Pi.
\]
Poincaré and (5) imply \(\mathbb E\delta_\Pi\le I(f)\). When
\(n<(k+1)^2\), this implies (6). Hence (6) holds in all dimensions.

## 3. Finish and finite-crossing consequence

Average (2) over \(\Pi\), apply symmetric FEI, and use (4), (6):
\[
 H(f)\le24.08I(f)+32(k+1)^2I(f)
 \le\bigl(25+32(k+1)^2\bigr)I(f).
\]

There is a sharper bound for one exceptional layer. No two vertices in a
single Hamming layer are adjacent. Thus for each \(d_\Pi\) supported
there, \(\langle d_\Pi,A d_\Pi\rangle=0\) and
\[
 I(d_\Pi)=\tfrac n2\|d_\Pi\|_2^2=2n\delta_\Pi.
\]
Averaging and applying (5) gives \(n\mathbb E\delta_\Pi\le I(f)\).
Hence
\[
 \boxed{H(f)\le56.08 I(f)<57I(f)}
\]
for nonconstant \(f\) with one exceptional layer; the non-strict
\(H(f)\le57I(f)\) includes constants. No monotonicity is required.

For the following corollary, finite crossings mean a designated set of at
most \(m\) real breakpoints: \(F\) is constant on each complementary open
interval, and its labels at the designated points themselves are arbitrary.
This convention includes isolated point anomalies; counting only sign
reversals would not suffice. Now let \(f(x)=F(\sum_iw_ix_i)\) for such
an \(F\), and suppose that for some \(c>0\), after coordinate
sign changes and removal of zero-weight coordinates,
\[
 A=\sum_i|w_i/c-1|<\infty
\]
is bounded independently of dimension. The normalized weighted score
differs from \(\sum_i x_i=2r-n\) by at most \(A\). A layer can be
nonsymmetric only if its score interval
\([2r-n-A,2r-n+A]\) meets at least one crossing of \(F(c\cdot)\).
For a fixed crossing there are at most \(\lfloor A\rfloor+1\) such
layers, because the centers are spaced by 2 and the interval of eligible
centers has length \(2A\). Hence
\[
 k\le m(\lfloor A\rfloor+1),
\]
and (1) gives a dimension-independent FEI constant depending only on
\(m,A\), with no bias or threshold-spacing condition.

The count uses closed intervals and therefore permits attained crossing
points and arbitrary endpoint conventions. When \(A=0\), the function
is exactly symmetric, so the sharper 12.04 constant applies directly.

This is a restricted finite-crossing result. It does not establish FEI for
all arbitrary weighted finite-crossing functions. Novelty is unverified.

## 4. Stronger bound using the longest exceptional run and Dirichlet deficit

The number of exceptional layers can be replaced by the length of their
longest consecutive run. Let \(\ell\) be that length, with \(\ell=0\)
when \(\Lambda\) is empty, and define
\[
 D=I(f)-I(P_{\rm sym}f)
   =I((1-P_{\rm sym})f)\ge0.
\]
The equality follows from the orthogonal projection and its commutation
with the Laplacian. For \(\ell\ge1\),
\[
 \boxed{H(f)\le24.08 I(f)+32(\ell+1)^2D
       \le[25+32(\ell+1)^2]I(f).}\tag{8}
\]
This bound depends on the longest exceptional run, even when the total
number of exceptional layers grows with dimension. The count-\(k\)
theorem (1) follows since \(\ell\le k\) and \(D\le I(f)\).

For the proof, replace \(k\) by \(\ell\) in the adjacency calculation:
the induced exceptional-layer path is a union of blocks whose top
eigenvalues are bounded by \(2\cos(\pi/(\ell+1))\). Equation (7) then
holds with \(\ell\) when \(n\ge(\ell+1)^2\). The exact identity (5)
has right side \(2D\), giving
\(n\mathbb E\delta_\Pi\le(\ell+1)^2D\). For
\(n<(\ell+1)^2\), the same averaged variance argument gives
\(\mathbb E\delta_\Pi\le D\), and hence the identical bound after
multiplying by \(n\). Applying entropy comparison and symmetric FEI
proves (8). If \(\ell=0\), \(f\) is symmetric and the sharper
established 12.04 constant applies.

When exceptional layers are pairwise nonconsecutive, \(\ell=1\), their
union contains no cube edge. Thus for every \(d_\Pi\),
\(I(d_\Pi)=2n\delta_\Pi\), and (5) yields the exact identity
\[
 n\mathbb E\delta_\Pi=D.
\]
The sharper conclusion in this case is
\[
 \boxed{H(f)\le24.08I(f)+32D\le57I(f).}\tag{9}
\]
It permits arbitrarily many pairwise nonconsecutive exceptional layers
with arbitrary labels inside each one.
