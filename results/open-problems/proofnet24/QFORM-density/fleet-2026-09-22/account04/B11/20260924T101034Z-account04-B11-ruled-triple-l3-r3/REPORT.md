SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B11, 2026-09-24T10:10:34Z.
attacking: a full-line rough-input receiver for a ruled physical triple, uniform through both pivot signs and the null-pivot interface.

# A determinant-only ruled physical-triple theorem with constant 6

Programme: QFORM-DENSITY-3EIG-20260922.
Run: 20260924T101034Z-account04-B11-ruled-triple-l3-r3.
Status: NEW AMBIENT TARGET-LEVEL BRANCH / FULL-LINE INTERVAL BOUND / CONTINUITY ON THIS BRANCH / FULL QFORM OPEN.
Execution: WITHOUT_VERIFIED_BRAIN.

No moment, support, Gaussian, log-concavity, connected-support, post-rotation independence, conditional density cap, arbitrary-joint coarea theorem, pointwise quadratic-phase decay, or half-line-to-full-line inference is used.

## 1. Fresh completed inputs

The newest completed account01/B05 theorem is
QFORM-MIXED-L3-SQUARE-RECEIVER-v1, source

- math-open-problems@4fea394eafc8bce4f335cce2a6150ed50f95ed1a
- proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260924T100503Z-account01-B05-QFORM-auto11/REPORT.md.

For mutually independent cap-one \(H,L,W\), arbitrary Borel \(q\), and \(t\lambda\ne0\), it proves

\[
q(H)+2tHL+\lambda(W-s)^2+c
\quad\Longrightarrow\quad
p\in C_0,\qquad
\|p\|_\infty\le6|t|^{-2/3}|\lambda|^{-1/3}.
\tag{1.1}
\]

The proof is rough-input valid: it combines an \(L^3\) density bound for the complete bilinear-hub phase with an \(L^{3/2}\) bound for the independent square, before taking any supremum.

The completed account01/B11 theorem
QFORM-LDL-FULL-TWOJACOBIAN-NONZERO-v1 is source-pinned at

- math-open-problems@339d40cb2285b8d51cf07423514354bdd702833f
- proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260924T064232Z-account01-B11-QFORM-auto11/REPORT.md.

It supplies the exact punctured-pivot two-Jacobian used in Section 4 below.

## 2. Main ambient theorem

### Theorem — QFORM-RULED-PHYSICAL-TRIPLE-DET6-v1

Let \(A\) be any real symmetric \(n\times n\) matrix. Suppose three literal original coordinates \(h,\ell,w\) have principal block

\[
B=A[\{h,\ell,w\},\{h,\ell,w\}]
=
\begin{pmatrix}
a&t&0\\
t&0&0\\
0&0&\lambda
\end{pmatrix},
\qquad t\lambda\ne0.
\tag{2.1}
\]

All other entries of \(A\), including every coupling from this triple to its complement and the complete complementary self block, are arbitrary.

For every independent original-coordinate product law with one-dimensional density caps at most one, \(Q=X^TAX\) has a continuous density in \(C_0(\mathbb R)\) and

\[
\boxed{
\|p_Q\|_\infty
\le 6(|t|^2|\lambda|)^{-1/3}
=6|\det B|^{-1/3}.
}
\tag{2.2}
\]

Equivalently, for every interval \(I\),

\[
\boxed{
\Pr\{X^TAX\in I\}
\le6|\det B|^{-1/3}|I|.
}
\tag{2.3}
\]

If \(\sigma=s_3(B)>0\), then \(|\det B|\ge\sigma^3\), and therefore

\[
\boxed{
\|p_Q\|_\infty\le\frac6{\sigma}.
}
\tag{2.4}
\]

In particular, any ambient extension of a block (2.1) with \(|\det B|\ge1\) satisfies the target-level universal bound \(\|p_Q\|_\infty\le6\), regardless of the signs and sizes of all additional eigenvalues.

### Proof

Write the original coordinates as \(U=(H,L,W)\) and the complement as \(Y\). Condition on \(Y=y\). Product structure leaves \(H,L,W\) mutually independent with their original cap-one densities. Every cross coupling to \(y\) becomes an affine term, so the conditional polynomial is

\[
aH^2+2tHL+\lambda W^2+\alpha(y)H+\beta(y)L+\gamma(y)W+c(y).
\tag{2.5}
\]

Translate \(H\) by \(\beta(y)/(2t)\), translate \(W\) by \(\gamma(y)/(2\lambda)\), and absorb the remaining one-variable polynomial and constants into \(q_y(H)\). Coordinatewise translations preserve density caps and independence. The conditional law is therefore exactly in the scope of (1.1), uniformly in \(y\):

\[
\|p_{Q\mid Y=y}\|_\infty
\le6|t|^{-2/3}|\lambda|^{-1/3}.
\tag{2.6}
\]

Averaging conditional interval inequalities gives (2.3), hence absolute continuity and (2.2). Each conditional density is continuous and bounded by the same constant; dominated convergence gives a continuous unconditional representative. Since

\[
\det B=-t^2\lambda,
\tag{2.7}
\]

(2.2) is determinant-only. Finally the product of the three singular values of \(B\) is \(|\det B|\), so \(|\det B|\ge s_3(B)^3\), proving (2.4). QED.

This is a genuine full-line theorem. No one-sheet or half-line estimate is being renamed as a density bound.

## 3. Both indefinite signatures and the null-pivot interface

The eigenvalues of the \(2\times2\) ruled pair are

\[
\mu_\pm=\frac{a\pm\sqrt{a^2+4t^2}}2,
\qquad
\mu_+\mu_-=-t^2.
\tag{3.1}
\]

Thus the pair is always indefinite, for every \(a\), and changing the sign of \(\lambda\) gives respectively the signatures \((2,1)\) and \((1,2)\). The estimate (2.2) is completely independent of \(a\), so it is uniform for

\[
a>0,\qquad a=0,\qquad a<0.
\tag{3.2}
\]

This is precisely the convex/two-sheet collar that the scalar-pivot half-Riesz peel treated nonuniformly. The mixed \(L^3\)-\(L^{3/2}\) receiver pays the third curvature before the scalar peel and removes the logarithm.

## 4. account01/B11 applied at an actual inequality

On the punctured side \(a\ne0\), put

\[
U=H+\frac taL,
\qquad
F=(L,Q_{\{h,\ell,w\}}).
\tag{4.1}
\]

The account01/B11 full two-Jacobian identity gives

\[
J_2F=2\sqrt{a^2U^2+\lambda^2W^2}.
\tag{4.2}
\]

Its shear-area compensation is

\[
|a\lambda|\sqrt{1+(t/a)^2}
=|\lambda|\sqrt{a^2+t^2}
=|Be_1\wedge Be_3|
\ge s_3(B)^2.
\tag{4.3}
\]

Consequently the completed B11 theorem gives the actual inequalities

\[
\boxed{
\Pr\{J_2F\le\tau\}
\le\min\!\left(1,\frac{\pi\tau^2}{2s_3(B)^2}\right),
}
\tag{4.4}
\]

\[
\boxed{
\mathbb E(J_2F)^{-1}
\le\frac{\sqrt{2\pi}}{s_3(B)}.
}
\tag{4.5}
\]

Equations (4.4)-(4.5) explain geometrically why the third direction removes the rank-two logarithmic singularity, but they are not themselves promoted by an arbitrary-joint coarea shortcut. The full density conclusion comes from the product-preserving mixed-\(L^p\) theorem in Section 2.

## 5. Concrete dense ambient family

For arbitrary vectors \(u,v,w\) and arbitrary symmetric \(D\), consider

\[
A=
\begin{pmatrix}
a&1&0&u^T\\
1&0&0&v^T\\
0&0&1&w^T\\
u&v&w&D
\end{pmatrix}.
\tag{5.1}
\]

The visible physical triple has determinant \(-1\). Therefore every cap-one product input satisfies

\[
\boxed{
p_{X^TAX}\in C_0(\mathbb R),
\qquad
\|p_{X^TAX}\|_\infty\le6,
}
\tag{5.2}
\]

uniformly in \(a,u,v,w,D\). The outside coupling may be dense and arbitrarily large; it becomes only an affine term after conditioning on the original outside coordinates.

The isolated triple itself has spectrum

\[
\left\{\frac{a+\sqrt{a^2+4}}2,\,
\frac{a-\sqrt{a^2+4}}2,\,
1\right\},
\tag{5.3}
\]

so at \(a=0\) it is the exact target signature \(\{1,1,-1\}\). For \(a\ne0\), (5.2) remains valid even when one of the two pair eigenvalues has modulus below one; determinant currency, not an incorrect inherited spectral claim, is what pays the density.

## 6. Scope and remaining gap

Proved here:

1. a rough-input full-line interval theorem for every ambient matrix containing the literal ruled block (2.1);
2. determinant-only bound \(6|\det B|^{-1/3}\);
3. scale-covariant spectral bound \(6/s_3(B)\);
4. uniformity across both indefinite signatures and the null-pivot interface;
5. arbitrary dense outside couplings and arbitrary additional spectrum;
6. continuity on this branch.

Not proved:

- existence of such a ruled physical triple from the sole global hypothesis \(s_3(A)\ge1\);
- the general indefinite physical pair with both diagonal entries nonzero;
- shared-source third curvature after a non-product linear transformation;
- the unrestricted conjecture or full-target continuity.

The next B11 implication is the account01/B05 frontier
QFORM-INDEFINITE-PAIR-L3-v1:
prove
\[
\|p_{(H,L)C(H,L)^T+\mathrm{affine}}\|_3
\le C|\det C|^{-1/3}
\]
for every invertible indefinite physical \(2\times2\) block \(C\) and independent cap-one \(H,L\). Coupling this with the shifted-square \(L^{3/2}\) lemma would extend Theorem 2.1 from a ruled pair to every source-disjoint indefinite pair.

Full unrestricted QFORM: OPEN / not proved / not disproved.
