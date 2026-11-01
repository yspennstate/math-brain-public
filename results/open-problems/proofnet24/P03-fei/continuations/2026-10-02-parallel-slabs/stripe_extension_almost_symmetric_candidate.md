# FEI with finitely many nonsymmetric Hamming layers

Date: 2026-10-02. **Candidate extension; independent audit requested.**

This removes monotonicity and contiguity from the completed theorem in
`hamming_band_fei.md`. It also gives a finite-crossing consequence for
weighted sums with bounded total deviation from equal weights. All input
distributions are uniform on the cube; entropy logarithms are base 2.

## Theorem

Let \(f:\{-1,+1\}^n\to\{-1,+1\}\) be arbitrary. Suppose there is a set
\(\Lambda\subseteq\{0,\ldots,n\}\) of size at most \(k\) such that
\(f\) is constant on every Hamming layer outside \(\Lambda\). Its
constant label may vary arbitrarily between layers. Then
\[
 \boxed{H(f)\le\bigl(25+64(k+1)^2\bigr)I(f).}\tag{1}
\]
For \(k=0\), use the established symmetric-function FEI constant 12.04
directly. Constants and \(n=0\) are immediate; below \(n\ge1\).

The only established FEI input is O'Donnell–Wright–Zhou's 2011 symmetric
function theorem \(H(g)\le12.04 I(g)\). The entropy comparison
\[
 H(f)\le2H(g)+32n\Pr(f\ne g)\tag{2}
\]
for arbitrary Boolean \(f,g\) was proved in Section 1 of
`hamming_band_fei.md` and is reused unchanged.

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
This counts changing edges without using monotonicity. Quadratic influence
and \((u-v)^2\le2u^2+2v^2\) give
\[
 \mathbb E_\Pi I(d_\Pi)\le4 I(f).\tag{5}
\]

## 2. Mean disagreement is controlled by the exceptional layers

Set \(\delta_\Pi=\Pr(f\ne g_\Pi)\). We prove
\[
 n\mathbb E_\Pi\delta_\Pi\le2(k+1)^2 I(f).\tag{6}
\]

For large dimension, the adjacency argument from the band proof applies
to any real function \(u\) supported on the layers in \(\Lambda\).
The induced layer path is a disjoint union of consecutive blocks, each
having at most \(k\) vertices. Its top adjacency eigenvalue is at most
\(2\cos(\pi/(k+1))\). The same Cauchy–Schwarz edge bound therefore gives
\[
 \langle u,Au\rangle
 \le(n+1)\cos(\pi/(k+1))\|u\|_2^2.
\]
Consequently, when \(n\ge(k+1)^2\),
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
Poincaré and (5) imply \(\mathbb E\delta_\Pi\le2I(f)\). When
\(n<(k+1)^2\), this implies (6). Hence (6) holds in all dimensions.

## 3. Finish and finite-crossing consequence

Average (2) over \(\Pi\), apply symmetric FEI, and use (4), (6):
\[
 H(f)\le24.08I(f)+64(k+1)^2I(f)
 \le\bigl(25+64(k+1)^2\bigr)I(f).
\]

Now let \(f(x)=F(\sum_i w_ix_i)\), where \(F\) has at most \(m\)
fixed crossings, and suppose that for some \(c>0\), after coordinate
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
