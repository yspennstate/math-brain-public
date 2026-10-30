# Independent reconstruction of the canonical bilinear-root argument

Let all vector spaces be over \(\mathbb F_2\), and define
\[
 P_{r,a,b,c}(x,y)=(-1)^{x\cdot y+a\cdot x+b\cdot y+c}
 (1-2\mathbf 1_{\{y=0\}}).
\]
For a Boolean function \(f\), write
\[
 U(f)=\sum_S p_S\log_2\frac{\pi(S)}{p_S},\qquad
 p_S=\widehat f(S)^2,\quad
 \pi(S)=\sum_{T\supseteq S}p_T,
\]
and
\[
 G(f)=\sum_i\left(U(f)-\frac{U(f|_{z_i=0})+U(f|_{z_i=1})}{2}\right).
\]

## 1. Root normalization

The Walsh transform of \((-1)^{x\cdot y+a\cdot x+b\cdot y+c}\) has
magnitude \(2^{-r}\) at every one of the \(2^{2r}\) frequencies.  The
point flip at \(y=0\) adds a correction supported on the single
\(x\)-frequency layer \(\alpha=a\), of magnitude \(2^{1-r}\).  On that
layer it reverses the original signs; it changes no squared coefficient.
Thus
\[
 p_{\alpha,\beta}=2^{-2r},\qquad H(P)=2r,\qquad U(P)=r.
\]
This checks the exact normalization: \(p\) is a probability measure and no
factor of two is missing at the defect layer.

## 2. Physical-coordinate influence

For each \(x_i\), the edge derivative is controlled by \(y_i\), so exactly
half the edges are pivotal.  For each \(y_i\), all ordinary edges are
pivotal when \(x_i+b_i=1\).  On the unique exceptional pair
\(\{0,e_i\}\), the defect reverses that condition to \(x_i+b_i=0\).
The count remains exactly one half.  Hence every one of the \(2r\)
physical inputs has influence \(1/2\), and
\[
 I(P)=r.
\]
This calculation is basis-sensitive; it is not invariant under an arbitrary
invertible recombination of the physical inputs.

## 3. Restriction charges

Restricting \(y_i\) leaves either a rank-\((r-1)\) point-defect phase or a
rank-\((r-1)\) pure quadratic phase, up to characters and irrelevant bits.
Both children have \(U=r-1\), so \(\Delta_{y_i}U=1\).

For an \(x_i\)-restriction, put \(d=r-1\) and let \(a'\) be \(a\) with bit
\(i\) deleted.  The child law factors as a free uniform \(d\)-cube times a
uniform law on
\[
 A_{a',q}=\{(s,\gamma):\gamma=q\oplus\mathbf 1_{\{s=a'\}}\}.
\]
If \(h=|a'|\), direct upper-fiber counting gives
\[
 \Delta_{x_i}U=1+2^{-r}C_d(h),
\]
where
\[
 C_d(h)=d-h-\sum_{j=0}^{h-1}{h\choose j}
 \log_2(1-2^{-(d-j)}).
\]
The elementary bound \(-\log_2(1-z)\le2z\) for \(0\le z\le1/2\) yields,
for \(d\ge4\),
\[
 C_d(h)\le d-h+2^{1-d}(3^h-2^h)
 \le d+2(3/2)^d\le2^d.
\]
The finite cases \(d=0,1,2,3\) satisfy the same bound directly.  Therefore
\(\Delta_{x_i}U\le3/2\), and
\[
 G(P)\le r\left(1+\frac32\right)=\frac52r=\frac52 I(P).
\]

For disjoint products, squared Fourier mass and upper caps tensorize, so
\(U,H,I\), and the coordinatewise sum \(G\) are additive.  The same
constant therefore holds for disjoint products of the displayed roots.

## 4. Scope falsifier

The preceding proof uses the matched physical form \(x\cdot y\).  It cannot
be promoted unchanged to every invertible bilinear form \(x^TMy\).  Take
\(r=3\), rows
\[
 M=(111,101,011)_2,qquad a=111_2,qquad b=0,
\]
and apply the same point defect at \(y=0\).  This matrix is invertible and
the root squared spectrum is still uniform, with \(U=I=3\).  Exact rational
Walsh arithmetic and rational outward logarithm intervals certify
\[
 8.127349609262319346647853<G<
 8.127349609262319346647854,
\]
and hence
\[
 G/I>2.709116536420773115549284>5/2.
\]
The counterexample refutes only the overbroad physical-basis extension.  It
does not touch the canonical theorem and is not an FEI counterexample.

## 5. Remaining leaf

An \(x\)-restriction creates positive bilinear codimension and two unequal
masses on the exceptional Fourier layer.  The source gives an exact cap
formula for this descendant, but no uniform signed estimate for its full
restriction charge.  Thus restriction closure, a universal GU' inequality,
and full FEI remain open.
