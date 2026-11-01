SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B11, 2026-09-24T09:16:18Z.
attacking: the source-disjoint third-curvature branch of the nonzero-pivot LDL/two-sheet collar.

# Source-disjoint third curvature closes the punctured LDL collar

Programme: QFORM-DENSITY-3EIG-20260922.
Run: 20260924T091618Z-fleet04-B11-source-disjoint-ldl-r2.
Status: NEW TARGET-VALID BRANCH / CONTINUOUS DENSITY ON THIS BRANCH / FULL QFORM OPEN.
Execution: WITHOUT_VERIFIED_BRAIN.

No moment, support, Gaussian, log-concavity, post-rotation independence, arbitrary-joint coarea, or pointwise quadratic-phase decay is used.

## 1. Inputs used at their proved scope

The completed fleet01/B11 theorem
QFORM-LDL-FULL-TWOJACOBIAN-NONZERO-v1
is source-pinned at

- math-open-problems@339d40cb2285b8d51cf07423514354bdd702833f
- proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260924T064232Z-fleet01-B11-QFORM-auto11/REPORT.md.

The completed fleet01/B05 theorem
QFORM-RANK2-INDEPENDENT-SQUARE-BRIDGE-v1
is source-pinned at

- math-open-problems@4971375a7b03b979ca3bb1c6b31e4af71f7a1276
- proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B05/20260923T233435Z-fleet01-B05-QFORM-auto17/REPORT.md.

The first gives the exact full two-Jacobian and puncture compensation. The second converts the rank-two block plus a genuinely independent square into a full-line density bound.

## 2. Source-disjoint LDL normal form

Let the exact-rank-three spectral bookkeeping matrix be

\[
M=\begin{pmatrix}
a&r&0\\
r&b&0\\
0&0&d
\end{pmatrix},
\qquad
s=\min_j|\lambda_j(M)|>0.
\tag{2.1}
\]

Let \(Z,Y,W\) be normalized linear forms in the original independent inputs whose coefficient vectors are orthonormal. Assume the support of the coefficient vector of \(W\) is disjoint from the union of the supports of the coefficient vectors of \(Z,Y\). Thus \(W\) is genuinely independent of the entire source bank carrying \((Z,Y)\); no independence between \(Z\) and \(Y\) is asserted.

Allow arbitrary affine terms and translations, and write

\[
Q=aZ^2+2rZY+bY^2+\ell_1Z+\ell_2Y+c
  +d(W+\theta)^2.
\tag{2.2}
\]

Because \(M\) is block diagonal, \(d\) is an eigenvalue and the two eigenvalues of

\[
B_2=\begin{pmatrix}a&r\\r&b\end{pmatrix}
\tag{2.3}
\]

are the other two eigenvalues of \(M\). Consequently

\[
|d|\ge s,
\qquad
D_2:=|\det B_2|\ge s^2.
\tag{2.4}
\]

## 3. Main theorem

### Theorem — QFORM-LDL-SOURCE-DISJOINT-THIRD-CURVATURE-v1

Under (2.1)-(2.2), for every independent original-coordinate product law with one-dimensional density caps at most one, \(Q\) has a continuous density in \(C_0(\mathbb R)\) and

\[
\boxed{
\|p_Q\|_\infty
\le 128\sqrt2\,D_2^{-1/4}|d|^{-1/2}
\le \frac{128\sqrt2}{s}.
}
\tag{3.1}
\]

If \(W\) itself is one literal original coordinate, or more generally has density cap at most one, then

\[
\boxed{\|p_Q\|_\infty\le \frac{128}{s}.}
\tag{3.2}
\]

The statement is uniform in \(a\), including as \(a\to0\), uniform in the shear \(r/a\) on the punctured side, and valid for every sign pattern of the three nonzero eigenvalues.

### Proof

The first source bank carries the rank-two quadratic polynomial

\[
R=aZ^2+2rZY+bY^2+\ell_1Z+\ell_2Y+c.
\]

Its homogeneous matrix has rank exactly two and nonzero determinant magnitude \(D_2\). The disjoint bank carries the normalized linear form \(W\), whose density satisfies \(\|p_W\|_\infty\le\sqrt2\) by the product-projection theorem. Since the banks are disjoint, \(R\) and \(W\) are genuinely independent.

Apply QFORM-RANK2-INDEPENDENT-SQUARE-BRIDGE-v1 with \(\lambda=d\). It gives

\[
\|p_Q\|_\infty
\le128\sqrt2\,D_2^{-1/4}|d|^{-1/2}.
\]

Using (2.4),

\[
D_2^{-1/4}|d|^{-1/2}
\le (s^2)^{-1/4}s^{-1/2}=s^{-1},
\]

which proves (3.1). If \(\|p_W\|_\infty\le1\), use the general-\(K_W\) form of the same theorem to obtain (3.2). Its convolution proof also gives \(p_Q\in C_0\). QED.

## 4. The fleet01/B11 two-Jacobian applied at an actual inequality

Assume \(a\ne0\), put

\[
U=Z+\frac raY,
\qquad
F=(Y,Q).
\]

The completed fleet01/B11 identity specializes to

\[
J_2F=2\sqrt{a^2U^2+d^2W^2}.
\tag{4.1}
\]

The coefficient area of \((U,W)\) is

\[
A_{UW}=\sqrt{1+(r/a)^2}.
\tag{4.2}
\]

Moreover,

\[
|ad|A_{UW}
=|d|\sqrt{a^2+r^2}
=|Me_1\wedge Me_3|
\ge s^2.
\tag{4.3}
\]

Hence the actual puncture-uniform inequalities from fleet01/B11 are

\[
\boxed{
\Pr\{J_2F\le\tau\}
\le \min\!\left(1,\frac{\pi\tau^2}{2s^2}\right)
}
\tag{4.4}
\]

and

\[
\boxed{
\mathbb E(J_2F)^{-1}\le\frac{\sqrt{2\pi}}s.
}
\tag{4.5}
\]

Equations (4.4)-(4.5) alone are not used as a dependence-blind coarea theorem. The density conclusion (3.1) uses the stronger original-coordinate disjoint-bank factorization. This is exactly the distinction required by the live two-sheet corrections.

## 5. Concrete target family, uniform through the null pivot

For \(0<\varepsilon\le1/16\), \(\sigma\in\{\pm1\}\), and independent cap-one \(H,V,W\), set

\[
Q_{\varepsilon,\sigma}
=\sigma\varepsilon H^2
+2\sqrt{1+\varepsilon}\,HV
+W^2.
\tag{5.1}
\]

Its matrix has spectrum

\[
\{1+\varepsilon,-1,1\}
\quad(\sigma=+1),
\qquad
\{1,-(1+\varepsilon),1\}
\quad(\sigma=-1).
\tag{5.2}
\]

Thus it is in the original three-large-eigenvalue class for both pivot signs. Here \(W\) is a literal disjoint original coordinate, \(s=1\), and (3.2) gives

\[
\boxed{\|p_{Q_{\varepsilon,\sigma}}\|_\infty\le128,\qquad
p_{Q_{\varepsilon,\sigma}}\in C_0(\mathbb R)}
\tag{5.3}
\]

uniformly as \(\varepsilon\downarrow0\). On the punctured side, (4.4)-(4.5) additionally give

\[
\Pr\{J_2F\le\tau\}\le\min(1,\pi\tau^2/2),
\qquad
\mathbb E(J_2F)^{-1}\le\sqrt{2\pi}.
\tag{5.4}
\]

This explicitly shows that the logarithmic divergence of the scalar-pivot half-Riesz peel on this family is a proof-architecture loss: the full two-Jacobian is uniformly integrable and the source-disjoint third square closes the density estimate.

## 6. Exact remaining gap

The theorem closes the nonzero/near-zero LDL collar whenever the third curvature is carried by a disjoint original-coordinate bank. It does not close the shared-source case, where \(W\) overlaps the bank carrying \(Z,Y\). In that case the independent-square convolution is unavailable, while the two-Jacobian bounds (4.4)-(4.5) cannot be converted to a density bound after forgetting product provenance.

The remaining B11 implication is therefore:

QFORM-LDL-SHARED-THIRD-CURVATURE-TWOJACOBIAN-COMPILER-v1:
retain the original product factorization while spending the two-dimensional Jacobian currency before any scalar half-Riesz majorant or worst-fiber envelope.

Arbitrary additional nonseparable spectrum and full-target continuity also remain open.

Full unrestricted QFORM: OPEN / not proved / not disproved.
