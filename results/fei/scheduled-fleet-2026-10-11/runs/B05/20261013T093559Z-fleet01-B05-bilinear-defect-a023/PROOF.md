# Arbitrary-rank bilinear-control / point-defect retained-credit theorem

All vector spaces below are over \(\mathbb F_2\). Let
\(x\in\mathbb F_2^s\), \(y\in\mathbb F_2^m\), let
\(M\in\mathbb F_2^{s\times m}\) have rank \(r\ge1\), and put
\[
q(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c},\qquad
d_m(y)=1-2\mathbf1_{\{y=0\}},\qquad P=qd_m.            \tag{1}
\]

## Theorem

For any Boolean function \(h\) on a disjoint block and \(F=Ph\), every
finite adaptive or pruned physical restriction tree \(T\) querying only
variables of \(P\) satisfies
\[
 U(F)-\sum_{\ell\in L(T)}w_\ell U(F_\ell)
 \le \frac{25}{4}I_{x,y}(F).                           \tag{2}
\]
The terminal packet \(U(h)\) is retained exactly once. The constant is
independent of \(s,m,r,M\), row and column overlaps, affine phases, tree
depth/order, dyadic leaf probabilities, and the dimension and spectrum of
\(h\). Moreover the base function satisfies
\[
 U(P)\le H(P)\le\frac{25}{4}I(P).                      \tag{3}
\]

The class is restriction stable after adjoining affine-bilinear phases and
rank-zero parity-shifted point defects. Thus this extends the single-centre
star theorem to arbitrarily many overlapping selector centres and arbitrary
bilinear rank.

## 1. Exact spectrum

Let \(A=\operatorname{im}M\subseteq\mathbb F_2^s\) and
\(B=\operatorname{row}M\subseteq\mathbb F_2^m\). The affine-bilinear phase
\(q\) has Fourier support
\[
 (a+A)\times(b+B),
\]
with all \(2^{2r}\) nonzero coefficients of magnitude \(2^{-r}\). This is
the usual orthogonality calculation: summing first over \(x\) imposes
\(My=\alpha+a\), and the remaining sum over the resulting coset vanishes
unless \(\beta+b\in B\).

Since \(q(x,0)=(-1)^{a\cdot x+c}\), multiplying by the point defect changes
the Fourier vector by
\[
 \widehat P(\alpha,\beta)-\widehat q(\alpha,\beta)
 =-2^{1-m}(-1)^c\mathbf1_{\{\alpha=a\}}.              \tag{4}
\]
Thus every one of the arbitrarily many overlapping centres is compressed
into one exceptional \(x\)-frequency layer.

Put \(u=2^{-r}\), \(\eta=2^{1-m}\), and \(k=m-r\). Outside the layer
\(\alpha=a\), there are \((2^r-1)2^r\) atoms of probability \(u^2\). In
the exceptional layer there are
\[
2^r\text{ atoms of probability }(u-\eta)^2,
\qquad
2^m-2^r\text{ atoms of probability }\eta^2.           \tag{5}
\]
These probabilities sum to one. Formula (5), including its signs before
squaring, is the complete normalization and overlap accounting.

## 2. Exact entropy and the uniform excess bound

Every \(x\)-frequency layer in \(a+A\) has total probability \(2^{-r}\).
All ordinary layers are uniform on \(2^r\) frequencies. In the exceptional
layer, the normalized total mass outside \(b+B\) is
\[
 \rho_k=4,2^{-k}(1-2^{-k})                            \tag{6}
\]
for \(k\ge1\); put \(\rho_0=0\). Hence the exact Shannon entropy is
\[
 H(P)=2r+2^{-r}E_k,                                    \tag{7}
\]
where
\[
 E_0=0,qquad
 E_k=h_2(\rho_k)+\rho_k\log_2(2^k-1)\quad(k\ge1).      \tag{8}
\]

The excess is uniformly bounded by \(9/4\). Indeed \(h_2\le1\). For the
second term:

- \(k=1\) gives zero;
- \(k=2\) uses \(\log_2 3<5/3\), giving less than \(5/4\);
- \(k=3\) uses \(\log_2 7<20/7\), equivalently
  \(7^7<2^{20}\), giving less than \(5/4\);
- \(k=4\) uses \(\log_2 15<4\), giving less than \(1\);
- for \(k\ge5\),
  \(\rho_k\log_2(2^k-1)<4k/2^k\le5/8\).

Therefore
\[
                         E_k<\frac94.                  \tag{9}
\]

At least \(r\) rows of \(M\) are nonzero. For each such row, the
corresponding \(x_i\) is pivotal on exactly half of the \(y\)-cube; the
factor \(d_m\) cancels in the derivative. Consequently
\[
 I(P)\ge I_x(P)\ge\frac r2.                            \tag{10}
\]
Combining (7)--(10), and noting that
\(2^{-r}/r\le1/2\) for \(r\ge1\), gives
\[
 H(P)<2r+\frac94,2^{-r}
 \le \left(4+\frac94\right)I(P)
 =\frac{25}{4}I(P).                                    \tag{11}
\]
Since \(U\le H\), (3) follows.

## 3. Complete-tree retained credit

Exact disjoint tensor additivity yields
\[
U(Ph)=U(P)+U(h),\qquad U(P_\ell h)=U(P_\ell)+U(h).
\]
The reach weights sum to one, so the arbitrary terminal packet cancels once:
\[
U(F)-\sum_\ell w_\ell U(F_\ell)
=U(P)-\sum_\ell w_\ell U(P_\ell)
\le U(P).                                               \tag{12}
\]
Equations (3) and (12) prove (2). No nodewise positive-part estimate, no
freshness assumption between centres, and no depth-dependent sum is used.

## 4. Restrictions and rank-zero boundary

Restricting an \(x\)-coordinate deletes a row of \(M\) and changes only an
affine term. Restricting \(y_j=0\) deletes a column and preserves a lower-
dimensional point defect; restricting \(y_j=1\) kills the defect and leaves
an affine-bilinear phase. Thus the generated class is physically
restriction closed.

If the rank drops to zero, the function is a character times \(d_m\). When
the character uses a defect coordinate, \(H<3\) and total influence is at
least \(1/2\), so \(H<6I\). For the raw defect, with
\(\delta=2^{-m}\),
\[
H(d_m)\le\frac{4\delta}{\ln2}+8(m-1)\delta
\le8m\delta=4I(d_m).                                   \tag{13}
\]
Pure affine-bilinear phases obey their standard quadratic FEI bound. Hence
the same \(25/4\) constant covers every restriction boundary.

## Exact scope

The theorem has one point-defect cylinder but arbitrarily many overlapping
bilinear selector centres. It does not cover two or more point-defect
cylinders, a general nonflat shared core, or a directional payment using only
the coordinates actually queried by a pruned tree. In those cases (4) is
replaced by several exceptional layers whose upper filters can intersect.
Full FEI remains open.
