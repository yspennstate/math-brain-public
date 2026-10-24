# QFORM-STRICT-THRESHOLD-PRINCIPAL-DELOCALIZATION-v1

**Worker:** account01 / B17 — sharp constant and witnesses  
**Status:** full unrestricted QFORM remains **OPEN / not proved / not disproved**. Continuity remains separate.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Owner continuation acknowledged:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` (revision 2026-09-23.15).  

## 1. New theorem: full-rank strict-target witnesses with no small target-scale principal block

Let
\[
B_H=I_3-\frac23\mathbf1\mathbf1^T
=\frac13\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix},
\qquad B_H^2=I_3,
\]
so \(\operatorname{spec}(B_H)=\{1,1,-1\}\).

For an integer \(m\ge2\), put \(N=3m\). Partition the physical coordinates into three banks of size \(m\), and let \(R_m\in\mathbb R^{3m\times3}\) have every row in bank \(j\) equal to \(e_j/\sqrt m\). Then
\[
R_m^TR_m=I_3,
\qquad
P_m:=R_mR_m^T
\]
is the orthogonal projection onto the three-dimensional bank-constant subspace.

For either \(\sigma\in\{-1,+1\}\), define
\[
\varepsilon_m:=\frac1{2m^2},
\qquad
\boxed{
A_m^{\sigma}
=\left(1+\frac1m\right)R_mB_HR_m^T
+\sigma\varepsilon_m(I-P_m).
}
\]

Because the two summands act on orthogonal invariant subspaces,
\[
\boxed{
\operatorname{spec}(A_m^\sigma)
=
\left\{1+\frac1m,\ 1+\frac1m,\ -\left(1+\frac1m\right),\
\underbrace{\sigma\varepsilon_m,\dots,\sigma\varepsilon_m}_{3m-3}\right\}.
}
\]
Thus every \(A_m^\sigma\) is **full rank** and has three eigenvalues strictly beyond the target threshold \(|\lambda|=1\). The small residual spectrum may be chosen all positive or all negative.

### Entrywise density

For coordinates \(i,j\) in different banks,
\[
(A_m^\sigma)_{ij}=-\frac{2(m+1)}{3m^2}\ne0.
\]
For distinct coordinates in the same bank,
\[
(A_m^\sigma)_{ij}=\frac{m+1}{3m^2}-\frac{\sigma}{2m^3}\ne0,
\]
and on the diagonal,
\[
(A_m^\sigma)_{ii}=\frac{m+1}{3m^2}
+\frac{\sigma}{2m^2}\left(1-\frac1m\right)\ne0
\]
for every \(m\ge2\). Hence the physical matrix is **entrywise nonzero**.

### Principal-submatrix delocalization

Let \(S\subset\{1,\dots,3m\}\), and let \(k_j\) be the number of selected coordinates from bank \(j\). Writing \(R_S\) for the selected rows,
\[
R_S^TR_S=\operatorname{diag}(k_1/m,k_2/m,k_3/m),
\]
so
\[
\|R_S\|_{op}^2=\frac{\max_jk_j}{m}\le\frac{|S|}{m}.
\]
The principal compression obeys
\[
\begin{aligned}
\|A_m^\sigma[S]\|_{op}
&\le \left(1+\frac1m\right)\|R_SB_HR_S^T\|_{op}
+\varepsilon_m\|(I-P_m)[S]\|_{op}\\
&\le \left(1+\frac1m\right)\frac{|S|}{m}+\varepsilon_m.
\end{aligned}
\]
Therefore, whenever \(|S|\le m-1\),
\[
\boxed{
\|A_m^\sigma[S]\|_{op}
\le
\left(1+\frac1m\right)\frac{m-1}{m}+\frac1{2m^2}
=1-\frac1{2m^2}<1.
}
\]
Consequently **any original-coordinate principal submatrix having even one eigenvalue of modulus at least one must contain at least \(m=N/3\) physical coordinates**. In particular no bounded-size principal-minor selection argument can witness the three large eigenvalues uniformly in dimension on this family.

### Vanishing physical leverage

Since
\[
(A_m^\sigma)^2
=\left(1+\frac1m\right)^2P_m+\varepsilon_m^2(I-P_m),
\qquad (P_m)_{ii}=\frac1m,
\]
we have the exact row-leverage formula
\[
\boxed{
\|A_m^\sigma e_i\|_2^2
=rac{(1+1/m)^2}{m}
+\varepsilon_m^2\left(1-\frac1m\right)
\longrightarrow0.
}
\]
Also \(\max_{ij}|(A_m^\sigma)_{ij}|=O(m^{-1})\). Thus target-scale spectrum coexists with vanishing individual entries and vanishing one-coordinate action.

## 2. These full-rank, strict-target matrices still saturate the known lower obstruction

Let the physical inputs be independent
\[
X_i\sim U[-1/2,1/2].
\]
These are cap-one densities. Put
\[
Y_m=R_m^TX.
\]
The three coordinates of \(Y_m\) are independent normalized sums of \(m\) centered unit intervals, each of variance \(1/12\). Hence
\[
Y_m\Longrightarrow G\sim N(0,I_3/12).
\]
Now
\[
Q_m^\sigma=X^TA_m^\sigma X
=\left(1+\frac1m\right)Y_m^TB_HY_m
+\sigma\varepsilon_m X^T(I-P_m)X.
\]
Because \(|X_i|\le1/2\), deterministically
\[
0\le X^T(I-P_m)X\le\|X\|_2^2\le\frac{3m}{4},
\]
so
\[
\left|\varepsilon_mX^T(I-P_m)X\right|
\le\frac{3}{8m}\longrightarrow0.
\]
Slutsky therefore gives
\[
Q_m^\sigma\Longrightarrow G^TB_HG
\stackrel d=G_1^2+G_2^2-G_3^2.
\]

For \(\sigma^2=1/12\), the density of the Gaussian limit at zero is
\[
\begin{aligned}
p_G(0)
&=\int_0^\infty p_{G_1^2+G_2^2}(s)p_{G_3^2}(s)\,ds\\
&=\frac1{2\sqrt2\,\sigma^2}
=\boxed{3\sqrt2}.
\end{aligned}
\]

No continuity assumption on the finite-\(m\) output is needed. Each \(Y_m\) has a three-dimensional absolutely continuous product law, and the nondegenerate three-dimensional quadratic part has critical set only at the origin; coarea gives an absolutely continuous law for the core, while the displayed full-rank physical form is itself a nonconstant polynomial with gradient zero only on a Lebesgue-null set. For every \(h>0\), any density representative therefore satisfies
\[
\|p_{Q_m^\sigma}\|_\infty
\ge\frac{\Pr(|Q_m^\sigma|\le h)}{2h}.
\]
Since the Gaussian limit has no atoms at \(\pm h\), weak convergence yields
\[
\liminf_{m\to\infty}\|p_{Q_m^\sigma}\|_\infty
\ge\frac{\Pr(|G^TB_HG|\le h)}{2h}.
\]
Letting \(h\downarrow0\),
\[
\boxed{
\liminf_{m\to\infty}\|p_{Q_m^\sigma}\|_\infty\ge3\sqrt2.
}
\]
Thus the source-valid unrestricted obstruction remains
\[
\boxed{C_{\mathrm{univ}}\ge3\sqrt2=4.242640687119\ldots .}
\]
This realization is stronger than the bare rank-three bank witness: at every finite \(m\) it is full-rank, entrywise dense, has strict spectral slack \(1/m\), has residual spectrum of either chosen sign, has vanishing physical coefficients/leverage, and hides all target-scale principal spectrum from every subset of fewer than one third of the physical coordinates.

This does **not** prove \(C_{\mathrm{univ}}=3\sqrt2\). The slack \(1/m\to0\), consistent with the previously established Gaussian spectral-slack rigidity.

## 3. Concrete use of the completed account02/B17 theorem

Source-pinned peer input: `math-open-problems@96940cec9f8a2d4ca231a77d1324cfb7c59a87ad`, account02/B17 report
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260924T024313Z-account02-B17-QFORM-auto11/REPORT.md`.

That report proves, for arbitrary independent one-dimensional densities bounded by one,
\[
\left\|p_{\beta Y^2+2aXY+2aYZ+\kappa(X-Z)^2}\right\|_\infty
\le\frac{2\sqrt2}{\sqrt{|\kappa a|}},
\qquad \kappa a\ne0.
\]
Apply it at
\[
\beta=\frac12,\qquad a=1,\qquad \kappa=1.
\]
The actual physical matrix is
\[
A_p=
\begin{pmatrix}
1&1&-1\\
1&1/2&1\\
-1&1&1
\end{pmatrix},
\]
with exact characteristic polynomial
\[
(\lambda-2)\left(\lambda^2-\frac12\lambda-2\right),
\]
so
\[
\boxed{
\operatorname{spec}(A_p)
=\left\{2,\frac{1+\sqrt{33}}4,\frac{1-\sqrt{33}}4\right\}.
}
\]
The smallest absolute eigenvalue is \((\sqrt{33}-1)/4>1\), hence this is a strict genuine QFORM target. The peer theorem gives the global arbitrary-law inequality
\[
\boxed{
\left\|p_{X^2+\frac12Y^2+Z^2+2XY+2YZ-2XZ}\right\|_\infty
\le2\sqrt2
<3\sqrt2.
}
\]
So a dense three-variable coupled target can be uniformly far below the sharp known obstruction, while the delocalized bank family above asymptotically attains the obstruction. This sharpens the proof constraint: concentration-preserving reduction cannot in general collapse the target spectrum to a bounded number of original coordinates.

## 4. Proof constraint for the main programme

This family falsifies a whole class of possible sharp-proof heuristics, without refuting the theorem:

- three large eigenvalues need not produce any target-scale bounded-size principal minor;
- they need not produce any order-one physical coefficient;
- they need not produce any order-one single-coordinate leverage;
- full rank and strict \(|\lambda|>1\) do not create a fixed improvement over \(3\sqrt2\) when the spectral excess vanishes;
- entrywise-dense coupling does not itself smooth the near-extremal diffuse mechanism.

A successful universal proof must therefore use an aggregate/product-preserving mechanism (for example a diffuse frame/volume/Fourier receiver), rather than a bounded-coordinate extraction alone.

## 5. Corrections preserved

No independence after arbitrary spectral rotation is used. No pointwise quadratic-phase decay for arbitrary rough densities is used. No arbitrary-joint coarea cap is used. No pointwise value is promoted to a global mode; the lower obstruction is expressed through small-ball probabilities. The interval-to-Borel shortcut remains invalid. The full arbitrary rough-law QFORM theorem remains open, and continuity is not inferred from the height estimate.

`CHECK.py` verifies the exact Householder identities, sample finite spectra and entrywise nonvanishing, the principal-bound scalar identity, and the partner matrix spectrum.
