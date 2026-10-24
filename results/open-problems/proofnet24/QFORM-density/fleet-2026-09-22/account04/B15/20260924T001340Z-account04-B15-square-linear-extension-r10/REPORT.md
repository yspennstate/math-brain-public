SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-24T00:13:40Z.
attacking: extend the newest square-linear leaf C0 receiver to an arbitrary-dimensional target chamber with arbitrary dense conditioned self-coupling.

# account04/B15 — arbitrary dense extensions of a square-linear target core

Programme: \`QFORM-DENSITY-3EIG-20260922\`.
Run: \`20260924T001340Z-account04-B15-square-linear-extension-r10\`.
Full unrestricted QFORM status: \`OPEN_NOT_PROVED\`.

## Sources and scope

Required Claude package retained from
\`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`,
\`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.

The completed partner result actually applied below is account01/B15,
\`yspennstate/math-open-problems@0b451fb08a83f7d58a1f2bfc0eb4ed4cdc9f487c\`,
Theorem 6.1 (\`QFORM-SQUARE-LINEAR-LEAF-C0-v1\`). In original independent coordinates it says that, after conditioning on all remaining coordinates,
\[
Q=R_w(P)+dU^2+a_w(P)U+b_w(P)V,\qquad
b_w(P)=2m\cdot P+\beta(w),
\]
with \(d\ne0\), \(m\ne0\), no \(UV\) term and no \(V^2\) term, has
\[
p_Q\in C_0(\mathbb R),\qquad
\|p_Q\|_\infty\le 6|d|^{-1/3}m_*^{-2/3},
\quad m_*=\max_j|m_j|.
\]
Its proof first pays an interval/essential-height bound and only then invokes dominated conditional-\(C_0\) mixing. Thus continuity is not used as a substitute for bounded density.

## Theorem: arbitrary dense extension of a non-range-aligned physical core

Let \(n\ge4\), let \(A\) be any real symmetric \(n\times n\) matrix, and suppose that on four original coordinates \((X,Z,Y,U)\) its principal block is
\[
B=
\begin{pmatrix}
-1&0&1&0\\
0&-1&0&1\\
1&0&1&0\\
0&1&0&0
\end{pmatrix}.
\tag{1}
\]
Every entry of \(A\) involving the other \(n-4\) coordinates is arbitrary: the outside principal block may be dense and indefinite, and all four core coordinates may couple arbitrarily to the outside.

For every product input with independent real coordinate densities bounded by one,
\[
\boxed{
p_{X^TAX}\in C_0(\mathbb R),\qquad
\|p_{X^TAX}\|_\infty\le6 .
}
\tag{2}
\]
Moreover \(A\) automatically belongs to the full target class: it has at least three eigenvalues of absolute value at least one.

### Proof of the density and continuity statement

Write \(P=(X,Z)\), take the curved leaf to be \(Y\), the linear leaf to be \(U\), and condition on all outside coordinates \(W=w\). The conditioned form is
\[
Q=R_w(X,Z)+Y^2+a_w(X,Z)Y+b_w(X,Z)U,
\tag{3}
\]
where \(R_w\) is an arbitrary quadratic polynomial, \(a_w\) is affine, and
\[
b_w(X,Z)=2Z+\beta(w).
\tag{4}
\]
The arbitrary dense outside block contributes only to \(R_w\); arbitrary outside-to-\(Y\) and outside-to-\(U\) couplings contribute only to the conditioning-dependent affine terms in (3)-(4). They do not alter the physical coefficients
\[
d=A_{YY}=1,\qquad A_{YU}=0,\qquad A_{UU}=0,\qquad
m_*=\max(|A_{XU}|,|A_{ZU}|)=1.
\tag{5}
\]

Applying the completed account01/B15 theorem at the actual inequality gives
\[
\Pr\{X^TAX\in I\}\le 6|I|
\tag{6}
\]
for every interval \(I\). Hence the output has an essentially bounded density of height at most \(6\). The same theorem's dominated conditional-\(C_0\) compiler gives a canonical representative in \(C_0(\mathbb R)\) with no loss in (6). No pointwise evaluation of a rough input density and no post-rotation independence are used.

### Proof of the actual three-eigenvalue gate

After permuting the four core coordinates to \((X,Y,Z,U)\), the block (1) is the direct sum
\[
\begin{pmatrix}-1&1\\1&1\end{pmatrix}
\oplus
\begin{pmatrix}-1&1\\1&0\end{pmatrix}.
\]
Its eigenvalues are
\[
\sqrt2,\quad -\sqrt2,\quad
\frac{-1+\sqrt5}{2},\quad
\frac{-1-\sqrt5}{2}.
\tag{7}
\]
Thus \(B\) has one eigenvalue at least \(1\) and two eigenvalues at most \(-1\).

Order eigenvalues decreasingly. Cauchy interlacing for the principal block gives
\[
\lambda_1(A)\ge\lambda_1(B)=\sqrt2,
\tag{8}
\]
and, from the two negative eigenvalues of \(B\),
\[
\lambda_{n-1}(A)\le\lambda_3(B)=-\sqrt2,\qquad
\lambda_n(A)\le\lambda_4(B)=-\frac{1+\sqrt5}{2}.
\tag{9}
\]
Therefore \(A\) has at least three eigenvalues of absolute value at least one, regardless of the dimension, signs, size, or density of the outside self-coupling and cross-coupling.

This gate is an actual principal-block spectral statement. No matrix-small term is treated as a small random quadratic error.

## What is new relative to the preceding account04/B15 family

The preceding family at
\`math-open-problems@ae87801238cf5756c153d27fed0bb6524d88ee17\`
used exact opposite-sign cancellation and range-aligned semidefinite smoothing. The present class:

- is not based on a range-aligned semidefinite three-coordinate block;
- allows a nonzero curved leaf together with a distinct zero-curvature linear leaf;
- permits an arbitrary dense, indefinite outside principal block;
- permits arbitrary coupling of every core coordinate to every outside coordinate;
- preserves a dimension-free bound \(6\) and a \(C_0\) representative.

## Limits and remaining gap

The unrestricted conjecture remains open. The bare condition \(s_3(A)\ge1\) does not force a four-coordinate principal block of the form (1), nor even the square-linear pattern \(A_{YY}\ne0\), \(A_{YU}=A_{UU}=0\), \(A_{ZU}\ne0\). A generic nonzero \(2\times2\) leaf block reintroduces the unpaid critical/logarithmic singularity. It cannot be called a product twist or discarded as a small random error under unbounded inputs.

The next B15 step is a product-coordinate receiver for a genuinely nonzero indefinite leaf block, averaging its critical singularity against the pivot-generated affine coefficient before taking any fiber supremum.
