# account02/B12 — rank-one spike transfers all usable spectral mass into the overlap-two channel

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Additional eigenvalue control  
**Status:** PROVED SUPPORTING COUNTEREXAMPLE / FULL TARGET OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. First unpaid implication attacked

The live proof-first programme asks for an exhaustive original-coordinate reduction that remains valid after arbitrary additional eigenvalues. The assigned partner account03/B12 proved the exact overlap decomposition

\[
M_0(A)+M_1(A)+M_2(A)+M_3(A)=e_3(A^2),
\]

where \(M_r\) is the squared \(3\times3\) minor mass over row/column triples with intersection size \(r\), and also proved the physical-three-block theorem: a physical \(3\times3\) block with two same-sign eigenvalues of magnitude at least \(L\) gives density at most

\[
C_*/L,\qquad C_*=24.183038289961516\ldots .
\]

Source: `yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`.

The remaining question is whether an arbitrary added eigendirection can be absorbed by the already-paid definite-pair / well-conditioned-principal-triple mechanisms, or whether a genuinely mixed overlap channel is forced. The family below answers this exactly: one rank-one spike makes every physical pair indefinite and every principal triple ill-conditioned, while asymptotically all of \(e_3(A^2)\) moves into \(M_2\).

## 2. Exact target-class family

Let

\[
v=\frac12(1,1,1,1)^T,\qquad
w=\frac12(1,1,-1,-1)^T,
\]

so \(v,w\) are orthonormal. For \(M>1\), define

\[
A_M=I_4-(M+1)vv^T-\frac32ww^T.
\]

Equivalently,

\[
A_M=
\begin{pmatrix}
 d&s&o&o\\
 s&d&o&o\\
 o&o&d&s\\
 o&o&s&d
\end{pmatrix},
\quad
 d=\frac{3-2M}{8},\quad
 s=-\frac{2M+5}{8},\quad
 o=\frac{1-2M}{8}.
\]

Because \(A_Mv=-Mv\), \(A_Mw=-\tfrac12w\), and \(A_Mu=u\) on \(\{v,w\}^{\perp}\),

\[
\operatorname{spec}(A_M)=\{1,1,-\tfrac12,-M\}.
\]

Thus every \(M>1\) is already in the exact QFORM target class: three eigenvalues have absolute value at least one. Moreover

\[
A_M=A_1-(M-1)vv^T,
\]

so the degeneration below is caused by one additional rank-one eigendirection of arbitrary magnitude. Multiplying the entire family by \(-1\) gives the same obstruction with the spike sign reversed.

## 3. Every physical pair is indefinite

There are only two pair types.

For a same-\(w\)-sign pair, e.g. \(\{1,2\}\), the principal block is

\[
\begin{pmatrix}d&s\\s&d\end{pmatrix}
\]

with eigenvalues

\[
1,\qquad -\frac{2M+1}{4}.
\]

For an opposite-\(w\)-sign pair, e.g. \(\{1,3\}\), the principal block is

\[
\begin{pmatrix}d&o\\o&d\end{pmatrix}
\]

with eigenvalues

\[
\frac14,\qquad \frac{1-M}{2}.
\]

Hence for every \(M>1\) every physical \(2\times2\) principal block is indefinite. No definite-pair branch can pay this family.

## 4. Every physical principal triple becomes singular at scale \(1/M\)

By symmetry all four principal \(3\times3\) blocks have the same characteristic polynomial:

\[
\det(\lambda I-B_M)
=
\frac{(\lambda-1)(8\lambda^2+(6M-1)\lambda-1)}{8}.
\]

Define

\[
\rho_M=
\frac{2}{\sqrt{(6M-1)^2+32}+6M-1}.
\]

Then the triple eigenvalues are

\[
1,\qquad \rho_M,\qquad -\frac1{8\rho_M},
\]

and

\[
\det B_M=-\frac18.
\]

For \(M>1\), \(0<\rho_M<1\) and

\[
\rho_M\le \frac1{6M-1}.
\]

Thus

\[
\sigma_{\min}(B_M)=\rho_M\longrightarrow0
\qquad(M\to\infty),
\]

even though the determinant of every principal triple stays exactly \(-1/8\). In particular, the assigned partner's physical-three-block theorem can only be invoked here with same-sign threshold \(L\le\rho_M\), so its bound necessarily degrades like \(C_*/\rho_M\asymp M\). The arbitrary spike therefore cannot be transported by retaining only that local certificate.

## 5. Exact channel transfer: \(M_2\) absorbs the spike

In dimension four, two distinct \(3\)-subsets intersect in exactly two coordinates, so

\[
M_0=M_1=0.
\]

The four principal triple determinants are all \(-1/8\), hence

\[
M_3=4(1/8)^2=\frac1{16}.
\]

The twelve nonprincipal \(3\times3\) minors have the following exact values: four equal

\[
\frac{4M+1}{8},
\]

four equal

\[
\frac{2M-1}{8},
\]

and four equal

\[
-\frac{2M-1}{8}.
\]

Therefore

\[
M_2
=
\frac{4}{64}\left((4M+1)^2+2(2M-1)^2\right)
=
\frac{3(8M^2+1)}{16}.
\]

On the spectral side,

\[
e_3(A_M^2)
=\frac{6M^2+1}{4}.
\]

Hence exactly

\[
M_2+M_3=e_3(A_M^2),
\]

and

\[
\frac{M_2}{e_3(A_M^2)}\longrightarrow1.
\]

So the one arbitrary large eigendirection does not destroy the exterior-cube resource; it transfers essentially all of it from local principal geometry into the **overlap-two mixed channel**.

## 6. Consequence for the full proof architecture

This is not a counterexample to the QFORM conjecture. It is a counterexample to a stronger structural reduction:

> From three global \(|\lambda|\ge1\), even after one arbitrary rank-one spectral addition, one can always retain either a uniformly definite physical pair or a uniformly invertible physical principal triple.

That reduction is false already in dimension four. The family also shows that controlling only the principal channel \(M_3\) is not stable under arbitrary added eigenvalues: \(M_3\) stays fixed at \(1/16\) while the total target-level resource grows like \((3/2)M^2\).

The source-valid replacement is now sharper: an exhaustive argument must pay the overlap-two channel \(M_2\) (or an equivalent grouped-coordinate/hyperbolic certificate) before taking reciprocal local conditioning constants. This is exactly the channel left unpaid in the partner's exterior-power bookkeeping.

## 7. Corrections respected and remaining implication

No rotation is used to claim independence. No independent-convolution step is used after adding the spike. The result is compatible with the live corrections `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, and `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`.

**Remaining first implication:** derive a source-valid analytic payment for aggregate \(M_2\) overlap-two mass that does not select one inverse minor and keeps the original coordinate product structure. The family \(A_M\) is an exact stress test: any candidate must remain uniform as \(M\to\infty\) although every definite pair is absent and every principal triple has \(\sigma_{\min}\sim1/(6M)\).

Full QFORM status: **OPEN / NOT PROVED**.
