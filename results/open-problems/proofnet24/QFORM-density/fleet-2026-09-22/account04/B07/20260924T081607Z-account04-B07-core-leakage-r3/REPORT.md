SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B07, 2026-09-24T08:16:07Z.
attacking: an actual principal-block spectral gate from top-subspace concentration plus deterministic cross-boundary leakage, and its application to bounded localization of the newest physical Pluecker packet.

# account04/B07 — physical coordinate-core leakage identity

Run: 20260924T081607Z-account04-B07-core-leakage-r3.

Status: NEW ACTUAL-CORE SPECTRAL THEOREM / QUANTITATIVE EXTRACTION ALTERNATIVE / FULL QFORM OPEN.

Continuity is not claimed. All coordinates below are original coordinates. No rotated random variables are declared independent, no support or moment hypothesis is introduced, and no coefficient tail is treated as a small random quadratic error.

## 1. Incoming theorems

The physical-fiber theorem used below is the completed account04/B07 result: if an actual original-coordinate principal block \(B=A[I,I]\), \(|I|=m\), satisfies
\[
s_3(B)\ge \gamma>0,
\]
then, retaining arbitrary outside coordinates, couplings, signs, spectra and conditioning-generated affine terms,
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le \frac{2\sqrt{6\pi m}}{\gamma}.
}
\tag{1.1}
\]

The newest completed designated account01/B07 result actually consumed is math-open-problems@96e0981a393661b45bcf633615cff640f9d93ba8. It produces literal physical structures, including a physical exact-singular pair and, in the global separator branch, a determinant-stable matched physical pair \(K\) plus four disjoint original-coordinate banks carrying the actual rainbow packet
\[
\Omega_K(R,S;C,D)>\frac{p_*^2}{48}
=0.0299385284640443\ldots .
\tag{1.2}
\]

The theorem below does not pretend that (1.2) automatically localizes on boundedly many coordinates. It gives the exact final-matrix test for every proposed bounded localization of that packet.

## 2. Exact physical-core spectral gate

Let \(A=A^T\in\mathbb R^{n\times n}\) satisfy \(s_3(A)\ge1\). Choose three orthonormal eigenvectors with eigenvalues of modulus at least one and put them in the columns of \(U\in\mathbb R^{n\times3}\).

For an original-coordinate set \(I\), write
\[
B=A[I,I],\qquad C=A[I,I^c],
\tag{2.1}
\]
and define
\[
\delta_I:=\|U_{I^c}\|_{\mathrm{op}}^2.
\tag{2.2}
\]

### Theorem 2.1 — QFORM-PHYSICAL-CORE-SPECTRAL-LEAKAGE-GATE-v1

For every physical coordinate set \(I\) with \(|I|\ge3\),
\[
\boxed{
s_3(A[I,I])^2
\ge
1-\delta_I-\|A[I,I^c]\|_{\mathrm{op}}^2.
}
\tag{2.3}
\]

Consequently, whenever the right side is positive,
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le
\frac{2\sqrt{6\pi |I|}}
{\sqrt{1-\delta_I-\|A[I,I^c]\|_{\mathrm{op}}^2}}.
}
\tag{2.4}
\]

This is an actual principal-block gate for the final matrix \(A\). Arbitrarily large and signed additional eigenvalues are retained and can only help the positive \(A^2\) comparison.

### Proof

The physical block identity is exact:
\[
(A^2)[I,I]=B^2+CC^T.
\tag{2.5}
\]

By spectral decomposition of \(A^2\), the three selected modes give
\[
(A^2)[I,I]\succeq U_I\Lambda^2U_I^T\succeq U_IU_I^T,
\tag{2.6}
\]
because each selected \(|\lambda_j|\ge1\). The three nonzero eigenvalues of \(U_IU_I^T\) equal those of
\[
U_I^TU_I=I_3-U_{I^c}^TU_{I^c},
\tag{2.7}
\]
so
\[
\lambda_3((A^2)[I,I])
\ge
\lambda_{\min}(U_I^TU_I)
\ge1-\delta_I.
\tag{2.8}
\]

Using (2.5) and Weyl's inequality,
\[
\lambda_3(B^2)
\ge
\lambda_3((A^2)[I,I])-\|CC^T\|_{\mathrm{op}}
\ge1-\delta_I-\|C\|_{\mathrm{op}}^2.
\tag{2.9}
\]
Since \(B\) is symmetric, \(\lambda_3(B^2)=s_3(B)^2\), proving (2.3). Equation (2.4) follows from the physical-fiber theorem. QED.

## 3. Row-localized version

Suppose \(|I|=m\) and
\[
\|A[i,I^c]\|_2\le\varepsilon,\qquad i\in I.
\tag{3.1}
\]
Then
\[
\|A[I,I^c]\|_{\mathrm{op}}^2
\le\|A[I,I^c]\|_F^2
\le m\varepsilon^2.
\tag{3.2}
\]
Therefore
\[
\boxed{
s_3(A[I,I])^2\ge1-\delta_I-m\varepsilon^2,
}
\tag{3.3}
\]
and
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le
\frac{2\sqrt{6\pi m}}
{\sqrt{1-\delta_I-m\varepsilon^2}}
}
\tag{3.4}
\]
when the denominator is positive.

For the concrete gate
\[
\delta_I\le\frac14,\qquad
\varepsilon\le\frac1{2\sqrt m},
\tag{3.5}
\]
one obtains
\[
s_3(A[I,I])\ge2^{-1/2}
\tag{3.6}
\]
and hence
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le4\sqrt{3\pi m}.
}
\tag{3.7}
\]

Smallness in (3.1) is used only for deterministic operator control of the finite physical boundary. It is never converted into probabilistic smallness of a quadratic error under unbounded inputs.

## 4. Quantitative coordinate-core extraction

For an interval \(J\), put
\[
\rho_J=\frac{\Pr\{X^TAX\in J\}}{|J|}.
\tag{4.1}
\]
Equation (2.4) implies that if
\[
\rho_J>2\sqrt{6\pi m},
\tag{4.2}
\]
then every physical \(m\)-coordinate candidate core \(I\) satisfies
\[
\boxed{
\delta_I+\|A[I,I^c]\|_{\mathrm{op}}^2
\ge
1-\frac{24\pi m}{\rho_J^2}.
}
\tag{4.3}
\]
Under (3.1),
\[
\boxed{
\delta_I+m\varepsilon^2
\ge
1-\frac{24\pi m}{\rho_J^2}.
}
\tag{4.4}
\]

Thus a high-ratio survivor cannot possess a bounded physical core that simultaneously captures the three-large-eigenvalue subspace and is weakly coupled across its physical boundary.

## 5. Application to the newest account01/B07 packet

Take the account01/B07 preserved pair \(K\) and actual rainbow banks from (1.2). Let \(I\) be any bounded original-coordinate localization containing \(K\) and chosen physical subsets of the four banks that retain the desired part of the packet. Applying Theorem 2.1 to this literal \(I\) gives
\[
\boxed{
\rho_J
\le
\frac{2\sqrt{6\pi |I|}}
{\sqrt{1-\|U_{I^c}\|_{\mathrm{op}}^2
-\|A[I,I^c]\|_{\mathrm{op}}^2}}
}
\tag{5.1}
\]
whenever the denominator is positive.

In particular, if \(|I|=m\), the selected top-subspace escape is at most \(1/4\), and every boundary row has norm at most \(1/(2\sqrt m)\), then
\[
\boxed{
\rho_J\le4\sqrt{3\pi m}.
}
\tag{5.2}
\]

Thus the bounded-core branch of the newest physical packet is paid. Any unpaid high-density survivor must satisfy at least one of:

1. the packet cannot be retained on universally boundedly many physical coordinates;
2. every such localization loses a fixed amount of the selected three-dimensional spectral subspace;
3. every such localization has fixed-size final-matrix cross-boundary operator norm.

The packet size is retained as structural currency, but it is not falsely promoted by itself to spectral concentration or small boundary coupling.

## 6. Necessity of the boundary charge

For
\[
A=\begin{pmatrix}0&I_3\\ I_3&0\end{pmatrix},
\qquad I=\{1,2,3\},
\tag{6.1}
\]
one has \(s_3(A)=1\), while \(A[I,I]=0\) and \(\|A[I,I^c]\|_{\mathrm{op}}=1\). Thus concentration information without charging the physical boundary cannot force an actual principal block.

Additional large spectrum causes no cancellation in (2.6); it enters \(A^2\) positively. This is why the theorem is valid with arbitrary remaining spectrum.

The full conjecture remains open. The next B07 task is to force an aggregate receiver when every bounded localization of the newest physical packet is support-diffuse, spectrally escaping, or strongly boundary-coupled. Continuity remains separate.

## Source pins and corrections

- Required Claude baseline: math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837.
- Latest designated account01/B07 theorem consumed: 96e0981a393661b45bcf633615cff640f9d93ba8.
- Previous account04/B07 coordinate-core theorem: dab16464e87c939cc0cf3fd01d070045290192fa.
- Corrections retained: no universally good principal minor or cross-rank-three cut; no post-rotation independence; no deletion of nonzero coefficient tails; no small-operator-norm-to-small-random-error step.
