SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B14, 2026-09-23T06:14:28Z.

# B14 r8 — affine physical-core and aligned rank-drop compiler

Programme: QFORM-DENSITY-3EIG-20260922  
Status: new synthesis and target-level branch; the unrestricted conjecture remains open.  
Continuity: separate.

## 1. Sources and scope

This report uses:

1. the physical-fiber and ruled-surface results in the required Claude package at
   yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837;
2. account01/B14 r30 at
   yspennstate/math-open-problems@fe1b05ba7083f2da708eed681eb13b65236e9209,
   which proves the sharp fragment-mass warning and the coarsen-before-condition one-bank application;
3. account04/B14 r7 at
   yspennstate/math-open-problems@2ac84e141e8e939506cbd5cd8314589141b714d5,
   which establishes cap-preserving rough-law transfer for a conditioning-generated shear.

No rotated random coordinates are declared independent. No moment, bounded-support, connected-support, tail, or attained interval-extremizer assumption is used.

## 2. Full affine physical-core theorem

Let the independent original coordinates split as \(X=(U,Z)\), with \(U\in\mathbb R^3\). Write

\[
Q(U,Z)=U^TBU+2U^TCZ+Z^TDZ,
\]

where \(B=B^T\) is an actual \(3\times3\) principal block. Assume

\[
s_{\min}(B)\ge \sigma>0.
\]

### Theorem 2.1

For arbitrary cap-one marginal densities,

\[
\boxed{\ \|p_Q\|_\infty\le \frac{6\sqrt\pi}{\sigma}. \ }
\]

The estimate permits arbitrary additional spectrum, arbitrary dense \(C,D\), arbitrary translations, and arbitrary fragmented or unbounded supports.

If \(B\) has signature \((2,1)\), with eigenvalues
\(\lambda_1,\lambda_2,-\mu\), define

\[
\tau(z)=z^T\!\left(D-C^TB^{-1}C\right)z .
\]

Then every interval \(I\) also satisfies the sharper moving one-sheet estimate

\[
\boxed{
\Pr\{Q\in I,\ Q\ge\tau(Z)\}
\le C_+(B)|I|
\le \frac{\pi\sqrt2}{\sigma}|I|,
}
\]

where

\[
C_+(B)=
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\frac{d\theta}
{\sqrt{\sin^2\theta/\lambda_1+
       \cos^2\theta/\lambda_2+1/\mu}}.
\]

For signature \((1,2)\), the analogous statement holds on the moving one-sheet side \(Q\le\tau(Z)\), after replacing \(Q\) by \(-Q\).

### Proof

Condition on the outside original coordinates \(Z=z\). The active variables \(U_1,U_2,U_3\) remain independent and cap one, and

\[
Q_z(U)=U^TBU+2(Cz)^TU+z^TDz.
\]

The completed physical-fiber theorem applies directly to this affine polynomial and gives
\(6\sqrt\pi/\sigma\), uniformly in \(z\). Averaging its interval inequality proves the full-line assertion.

For the ruled assertion, complete the square only after conditioning:

\[
Q_z(U)=
\left(U+B^{-1}Cz\right)^TB
\left(U+B^{-1}Cz\right)
+\tau(z).
\]

The translation vector is deterministic for fixed \(z\); therefore the translated active coordinates are still independent and their density caps remain one. The ruled one-sheet theorem gives \(C_+(B)|I|\), uniformly in the translation. Integrating over \(z\) proves the claim.

This argument never evaluates a chosen version of a rough density on a quadratic surface.

## 3. Rough-law and fragment justification

For each marginal \(f_i\), let \(f_{i,\varepsilon}=f_i*\rho_\varepsilon\). Then

\[
0\le f_{i,\varepsilon}\le1,\qquad
\int f_{i,\varepsilon}=1,\qquad
\|f_{i,\varepsilon}-f_i\|_1\to0.
\]

The product laws converge in total variation, and polynomial pushforward contracts total variation. Hence every uniform interval inequality above passes to the original rough product law with exactly the same constant.

Equivalently, the account01/B14 r30 fragment-mass rule says to retain each localized finite union as one unnormalized marginal through the physical estimate. Normalizing its component intervals separately is neither needed nor valid: a positive cap homogeneity would lose a power of the fragment mass. Thus arbitrary remote fragments and unbounded supports create no localization tax.

## 4. Exact rank-drop endpoint supplied by a coarsened leakage bank

The preceding theorem degenerates when \(s_{\min}(B)\downarrow0\). At the exact rank-two endpoint, account01/B14 r30 supplies a product-safe replacement when the missing direction leaks through one aligned original-coordinate bank.

Let \(B\) have rank two, unit kernel vector \(k\), and both nonzero eigenvalues of modulus at least \(\nu>0\). Split the remaining original coordinates into disjoint banks \(V,Z\), put

\[
W=a^TV,
\]

and assume the coefficient dependence on \(V\) factors through \(W\):

\[
A_{U,V}=\gamma k a^T,\qquad
A_{V,V}=h\,aa^T,\qquad
A_{V,Z}=a b^T.
\]

The blocks \(A_{U,Z}\) and \(A_{Z,Z}\) may be arbitrary. Let \(\eta\) be any certified cap for \(W\). Then account01/B14 r30 gives

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{C_4}{\min\{\nu,|\gamma|/\eta\}},
\qquad
C_4=1000(8+\log4).
}
\]

Using the product-projection cap

\[
\eta\le \frac{\sqrt2}{\|a\|_2}
\]

yields the concrete target inequality

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{C_4}
{\min\{\nu,|\gamma|\|a\|_2/\sqrt2\}}.
}
\]

All conditioning-generated affine terms are allowed by the fixed-core theorem. The bank must be coarsened before conditioning; no fragment is normalized and no overlapping rotated statistics are asserted independent.

## 5. Actual full-target family

Take

\[
B=\operatorname{diag}(1,-1,0),
\qquad |\gamma|\|a\|_2\ge1.
\]

Allow arbitrary \(h,b,A_{U,Z},A_{Z,Z}\) subject only to the factorization in Section 4. The compression of the full matrix to

\[
\operatorname{span}\{e_1,e_2,e_3,a/\|a\|_2\}
\]

contains eigenvalues \(1,-1\) and the two eigenvalues of

\[
\begin{pmatrix}
0&\gamma\|a\|_2\\
\gamma\|a\|_2&h\|a\|_2^2
\end{pmatrix}.
\]

The latter matrix has negative determinant, and its spectral radius is at least
\(|\gamma|\|a\|_2\ge1\). Hence this compression, and therefore the full matrix by interlacing, has at least three eigenvalues of modulus at least one. The preceding bound becomes

\[
\boxed{
\|p_Q\|_\infty
\le \sqrt2\,C_4
<13274.3.
}
\]

This is uniform in the dimension of \(V,Z\), all admissible laws, all translations, arbitrary bank-square curvature \(h\), arbitrary additional spectrum, and dense outside self-couplings.

## 6. What this closes and what remains

The two branches form a scale-honest rank-drop compiler:

- an actual invertible physical \(3\times3\) principal block is paid by the affine physical-fiber theorem;
- an exact rank-two block whose kernel leakage is carried by one coarsened disjoint bank is paid by the account01 fixed-core theorem.

The remaining gap is the near-rank-two chamber and the exact rank-two case with several overlapping, non-factorable leakage statistics. Exact rank drop cannot be treated as a small random quadratic perturbation: under arbitrary unbounded inputs, a small matrix coefficient is not a uniformly small random error. Nor can one condition on overlapping linear statistics and retain product independence.

Thus the full conjecture remains open. The next structural implication must extract either an actual physical-core spectral gate, a disjoint aligned leakage bank, or a genuine joint cross-volume/ridge certificate from the three-global-eigenvalue hypothesis.
