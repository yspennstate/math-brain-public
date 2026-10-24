SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-23T23:19:29Z.
attacking: same-constant continuous regularity for a range-aligned semidefinite physical core, with an arbitrary-dimensional dense cross-coupling target family.

# account04/B15 — dense skew-involutive range-aligned family

Programme: QFORM-DENSITY-3EIG-20260922  
Run: 20260923T231929Z-account04-B15-range-aligned-c0-r9  
Status: TARGET-CLASS FAMILY PROVED / ACCOUNT01 B15 APPLIED / SAME-CONSTANT C0 APPLIED / FULL QFORM OPEN  
Execution: WITHOUT_VERIFIED_BRAIN.

## 1. New result

For every \(m\ge1\), \(a\ge1\), and real \(R\in\mathbb R^{2\times m}\), define, in the original coordinates \((X_1,X_2,X_3,Z_1,\ldots,Z_m)\),
\[
A_{a,R}=
\begin{pmatrix}
aI_2&0&R\\
0&0&0\\
R^T&0&-aI_m
\end{pmatrix}.
\tag{1.1}
\]
The cross matrix \(R\) may be dense, arbitrarily large, and of unrestricted width. For every independent cap-one product law,
\[
Q_{a,R}=a(X_1^2+X_2^2)+2(X_1,X_2)RZ-a\|Z\|_2^2
\]
has
\[
\boxed{
p_{Q_{a,R}}\in C_0(\mathbb R),\qquad
\|p_{Q_{a,R}}\|_\infty\le {2\pi\over a}\le2\pi.
}
\tag{1.2}
\]
Every \(A_{a,R}\) is literally in the owner target: apart from the inactive third physical coordinate, every eigenvalue has modulus at least \(a\). Thus there are at least three eigenvalues of modulus at least one.

This arbitrary-dimensional family shows that dense, unbounded cross coupling is not itself a height or regularity obstruction when the outside curvature has the exact opposite scalar action. The unrestricted conjecture remains open.

## 2. Sources and corrections

Fresh controls were read at math-research-brain main commit a05302d52d58e6fa6d55dee11dc356c85c477dab, with owner-control revision 2026-09-22.15.

The completed account01/B15 input is math-open-problems@fc9d06c78e03b4e1ad924f49fb9ab0f03018d2cd, run 20260923T220552Z-account01-B15-QFORM-auto11. Its exact interval theorem is applied below.

The same-constant regularity compiler is account04/B15 at math-open-problems@a1654d5fe319f483999583921d127819e40bc868, run 20260923T221909Z-account04-B15-ruled-trace-c0-r8.

The newest complementary B15 source checked before publication is account02/B15 at math-open-problems@7a0ffb7d9c4c6074cc6e13375db70828740e1bd4. It proves a collective rank-one Schur repair and a genuine obstruction to adding arbitrary leaf curvature through a worst-fibre grouped argument. The family here instead uses an exact algebraic cancellation.

Retained corrections: no post-rotation independence, arbitrary-joint coarea height, pointwise rough trace, universal pointwise quadratic-phase decay, guaranteed good single minor, or inference of continuity from essential boundedness alone.

## 3. Exact spectral gate

Delete the inactive \(X_3\) row and column:
\[
H_{a,R}=
\begin{pmatrix}
aI_2&R\\
R^T&-aI_m
\end{pmatrix}.
\tag{3.1}
\]
Direct multiplication gives
\[
H_{a,R}^2=
\begin{pmatrix}
a^2I_2+RR^T&0\\
0&a^2I_m+R^TR
\end{pmatrix}.
\tag{3.2}
\]
The cross blocks vanish because \(aR+R(-aI_m)=0\). Hence
\[
H_{a,R}^2\succeq a^2I_{m+2}.
\tag{3.3}
\]
Since \(H_{a,R}\) is symmetric, all its \(m+2\) eigenvalues have modulus at least \(a\). Therefore
\[
\operatorname{rank}A_{a,R}=m+2\ge3.
\tag{3.4}
\]
If \(\sigma_1,\ldots,\sigma_r\) are the nonzero singular values of \(R\), the paired eigenvalues are
\[
\pm\sqrt{a^2+\sigma_j^2},
\]
with unpaired \(+a\) and \(-a\) eigenvalues. No probabilistic assertion or coordinate rotation is used here.

## 4. Account01/B15 applied at an actual inequality

Partition the original coordinates as
\[
U=(X_1,X_2,X_3),\qquad Z\in\mathbb R^m.
\]
Then
\[
A_{a,R}=
\begin{pmatrix}B&C\\C^T&D\end{pmatrix},
\quad
B=a\,\operatorname{diag}(1,1,0),
\quad
C=\begin{pmatrix}R\\0\end{pmatrix},
\quad
D=-aI_m.
\tag{4.1}
\]
The physical block \(B\) is positive semidefinite of rank two, with nonzero eigenvalues \(a,a\), and
\[
\operatorname{Range}(C)\subseteq\operatorname{Range}(B).
\tag{4.2}
\]
The completed account01/B15 minority-null endpoint theorem therefore yields, for every Borel \(E\subset\mathbb R\),
\[
\boxed{
\Pr\{Q_{a,R}\in E\}
\le {2\pi\over\sqrt{a\cdot a}}|E|
={2\pi\over a}|E|.
}
\tag{4.3}
\]
This is the partner theorem applied at the required actual inequality. It is independent of \(m\), \(R\), and the input laws. Its rough-input justification is at interval/measure level; no pointwise trace of a rough density is evaluated.

Thus
\[
\|p_{Q_{a,R}}\|_{\infty,\mathrm{ess}}\le {2\pi\over a}.
\tag{4.4}
\]

## 5. Same-constant continuity after height

By (3.4), the full matrix has rank at least three. The completed fixed-target theorem supplies a \(C_0\) density for this exact rough product instance. Combining that qualitative theorem with (4.3), the same-constant compiler gives
\[
p_{Q_{a,R}}\in C_0(\mathbb R),
\qquad
\|p_{Q_{a,R}}\|_\infty\le {2\pi\over a}.
\tag{5.1}
\]
Indeed, if the continuous representative exceeded \(2\pi/a\) at one point, it would exceed that value on an interval, contradicting (4.3).

Continuity is added only after height. This is not another absolute-continuity argument, and no class-uniform modulus of continuity is claimed.

## 6. General range-aligned diagnostic

For a symmetric block matrix
\[
A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix},
\]
with \(B\succeq0\) of rank two and \(\operatorname{Range}(C)\subseteq\operatorname{Range}(B)\), let
\[
S=D-C^TB^\dagger C.
\]
An invertible block shear gives the congruence
\[
L^TAL=\begin{pmatrix}B&0\\0&S\end{pmatrix},
\]
so
\[
\boxed{\operatorname{rank}A=2+\operatorname{rank}S.}
\tag{6.1}
\]
Thus \(S\ne0\) is exactly the algebraic gate needed to invoke the rank-at-least-three \(C_0\) compiler after account01 pays the height. Congruence alone is not an eigenvalue-size estimate.

For (1.1),
\[
S=-aI_m-a^{-1}R^TR\prec0.
\tag{6.2}
\]
The stronger target spectral gate comes from the exact square identity (3.2).

## 7. Exact status

Proved:

1. An arbitrary-dimensional, arbitrarily dense and arbitrarily large cross-coupling family belongs to the literal target.
2. Every admissible product law has interval constant \(2\pi/a\), by account01/B15 at (4.3).
3. Every output has a canonical \(C_0\) density with the same constant.
4. No support, moment, smoothness, log-concavity, Gaussian-mixture, identical-law, or post-rotation independence hypothesis is used.

Not proved:

1. The bare condition \(s_3(A)\ge1\) does not force such a range-aligned physical core.
2. General dense transverse coupling need not have the opposite-scalar cancellation (3.2).
3. The higher-rank/sign-indefinite Schur problem in the newest account02/B15 report remains open.
4. No uniform continuity modulus is obtained.
5. The unrestricted conjecture remains OPEN; no counterexample is produced.

A next B15 step is to test broader deterministic anticommutation conditions and bounded matrix perturbations of (3.1), treating perturbations only through deterministic spectral gates—not as small random quadratic errors under unbounded inputs.
