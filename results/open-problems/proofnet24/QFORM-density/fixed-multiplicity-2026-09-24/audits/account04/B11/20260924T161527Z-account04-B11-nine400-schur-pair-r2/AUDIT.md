# Independent audit of the nine-eigenvalue density theorem

## Source and verdict

- Objective: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`.
- Source: \`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`.
- Source commit: \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`.
- Source git blob: \`19fb119877426b640b2c0dae19ec2f78a399fe11\`.
- Owner-recorded SHA-256: \`bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3\`.
- Audit role: account04/B11, independent proof reconstruction.
- Verdict: **PASS**. I found no fatal mathematical gap in the 955-line standalone paper. Its theorem with nine singular values and constant 400 is supported under the stated arbitrary-sign, arbitrary-affine, rough product-law hypotheses.

This is one complete independent reconstruction. It is not a claim that the owner's required second independent end-to-end review has already occurred.

## End-to-end proof map

| Source lines | Claim group | Status | Independent check |
|---|---|---|---|
| 44--156 | Fourier/Riesz conventions, scaling, smoothing and trace preliminaries | PASS | Constants and changes of variables reconstructed; approximation preserves density caps and passes interval bounds without evaluating an arbitrary density representative pointwise. |
| 158--296 | Geometric Brascamp--Lieb, projection lemma, scalar Fourier powers | PASS | The heat-flow derivative has the required sign, the limiting argument is legitimate, and the projection estimate uses \(\sum_{b_i>0}(1-b_i)\le d\). Zero-weight rows only change an advertised equality to an inequality, with no downstream loss. |
| 298--526 | Decoupling, grouped mollified-\(L^2\), free-volume and row promotion | PASS | Copies are introduced before conditioning, so no false post-rotation independence is used. Jensen/Hölder exponents and determinant powers close. The bordered-minor identities and sampling factors give the stated row promotion. |
| 528--661 | Scalar and pair pivots, Schur complements, rough trace | PASS | Completing the square is used only for an original-coordinate pivot. The Schur spectral loss is at most the pivot dimension, including singular ambient matrices. Kernel estimates are integrated against conditional product laws, not treated as independent twists. |
| 663--765 | Skeleton/no-pivot branch and rank accounting | PASS | The interpolation support is valid for nonsymmetric minors. The global perturbation rank is at most \(3r\), while the seed-restricted rank is at most \(r\); these are not conflated. Diagonal dominance gives the advertised contradiction and the no-pivot constant is below 375. |
| 767--859 | Definite and hyperbolic pair half-potentials; main case split | PASS | Both full half-potentials are finite with the stated determinant scaling. All pivot thresholds are used at their own scales. The largest branch is the indefinite-pair density estimate. |
| 861--942 | Spectral-overlap theorem and eight-direction corollary | PASS | The exact determinant interpolation and rank bounds support the overlap inequality. The paper correctly stops short of an eight-eigenvalue density theorem because the shared original coordinate has no product-preserving receiver estimate. |

No mathematical portion of the standalone source remains unchecked in this reconstruction. External novelty and primary-source literature attribution were outside this proof audit.

## B11 reconstruction: Schur counts

For a symmetric block matrix with an invertible \(k\)-dimensional pivot,
\[
 A=\begin{pmatrix}B&C^T\\ C&D\end{pmatrix},\qquad
 S=D-CB^{-1}C^T,
\]
Sylvester inertia additivity for the congruence factorization gives, at every threshold after the standard singular-value dilation,
\[
 N_S(t)\ge N_A(t)-k,\qquad s_j(S)\ge s_{j+k}(A).
\]
Nothing in this argument assumes that the ambient matrix is invertible. The loss of \(k\) is sharp, so a small or indefinite near-null pivot cannot refund spectral count by itself. The paper uses precisely this safe loss; it does not treat a small quadratic coefficient as a small error under unbounded inputs.

## B11 reconstruction: the indefinite pair

After normalizing a pair with discriminant magnitude \(D>0\), the hyperbolic variable \(Z=(Q-v)/\sqrt D\) has envelope
\[
 h(z)\le 6+\log_+\frac{16}{|z|}.
\]
For every center \(a\) and \(0<\delta\le1\), split at \(|Z-a|=\delta\):
\[
 \mathbb E|Z-a|^{-1/2}
 \le \delta^{-1/2}+4\sqrt\delta\left(8+\log\frac{16}{\delta}\right).
\]
At \(\delta=1/64\), this is
\[
 12+5\log2<16.
\]
Scaling back gives the full, not truncated, estimate
\[
 \sup_a\mathbb E|Q-a|^{-1/2}<16D^{-1/4}.
\]
The power is \(D^{-1/4}\), as required. The proof never derives a full-line density bound from a half-line estimate and never assigns independence to rotated coordinates.

## Constant audit and sharpening

The branch constants in the normalized main proof are
\[
 <375,\quad <280,\quad <320,\quad <383,\quad <80,
\]
and, for the final indefinite-pair branch,
\[
 200+80\log 10+\frac1e.
\]
Thus 400 is valid. Moreover,
\[
 \log 10<\frac{923}{400},\qquad \frac1e<\frac38,
\]
so
\[
 200+80\log10+\frac1e
 <200+\frac{923}{5}+\frac38
 =\frac{15399}{40}
 =384.975<385.
\]
The logarithm inequality is elementary and certified without decimal evaluation: for \(x=923/400\),
\[
 \sum_{j=0}^{7}\frac{x^j}{j!}
 =\frac{9195903741172641329483}{917504000000000000000}>10,
\]
hence \(e^x>10\). Also \(e>1+1+1/2+1/6=8/3\), so \(1/e<3/8\).

Consequently the same proof yields
\[
 \boxed{\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
 <385\,\frac{K^2}{s}}
\]
whenever \(s_9(A)\ge s>0\). No hypothesis or multiplicity changes.

## Remaining boundary

The nine-eigenvalue theorem passes this review. The overlap identity alone still does not lower nine to eight, and the unrestricted three-eigenvalue conjecture remains open. Continuity is separate from the essential \(L^\infty\) conclusion.
