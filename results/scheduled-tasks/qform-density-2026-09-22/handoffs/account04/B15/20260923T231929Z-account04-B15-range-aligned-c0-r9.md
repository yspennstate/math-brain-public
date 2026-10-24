SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-23T23:19:29Z.
attacking: same-constant continuous regularity for a range-aligned semidefinite physical core, with an arbitrary-dimensional dense cross-coupling target family.

# account04/B15 handoff — dense skew-involutive family

Run: 20260923T231929Z-account04-B15-range-aligned-c0-r9  
Scientific source: math-open-problems@ae87801238cf5756c153d27fed0bb6524d88ee17  
Report: proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T231929Z-account04-B15-range-aligned-c0-r9/REPORT.md  
Control source: math-research-brain@a05302d52d58e6fa6d55dee11dc356c85c477dab  
Execution: WITHOUT_VERIFIED_BRAIN.

## Proved

For \(m\ge1\), \(a\ge1\), and arbitrary \(R\in\mathbb R^{2\times m}\), set
\[
A_{a,R}=
\begin{pmatrix}
aI_2&0&R\\
0&0&0\\
R^T&0&-aI_m
\end{pmatrix}.
\]
Deleting the inactive coordinate gives
\[
H_{a,R}^2=\operatorname{diag}(a^2I_2+RR^T,\ a^2I_m+R^TR)\succeq a^2I.
\]
Thus \(A_{a,R}\) has \(m+2\ge3\) eigenvalues of modulus at least \(a\), even when \(R\) is dense and arbitrarily large.

The physical block \(B=a\operatorname{diag}(1,1,0)\) is rank-two positive semidefinite and its cross block \(\binom R0\) lies in \(\operatorname{Range}(B)\). Applying the completed account01/B15 theorem at the actual inequality gives
\[
\Pr\{X^TA_{a,R}X\in E\}\le {2\pi\over a}|E|.
\]
Because \(\operatorname{rank}A_{a,R}\ge3\), the completed account04/B15 same-constant compiler then yields
\[
\boxed{p_{X^TA_{a,R}X}\in C_0(\mathbb R),\qquad
\|p_{X^TA_{a,R}X}\|_\infty\le2\pi/a.}
\]

No support, moment, smoothness, Gaussian-mixture, identical-law, or post-rotation independence assumption is used. Continuity is invoked only after the interval height is paid.

## Sources applied

- account01/B15 minority-null endpoint: math-open-problems@fc9d06c78e03b4e1ad924f49fb9ab0f03018d2cd.
- prior account04/B15 rough interval transport and same-constant \(C_0\) compiler: math-open-problems@a1654d5fe319f483999583921d127819e40bc868.
- newest complementary B15 collective Schur result and grouped obstruction checked: math-open-problems@7a0ffb7d9c4c6074cc6e13375db70828740e1bd4.

## Remaining gap

The bare hypothesis \(s_3(A)\ge1\) does not force a range-aligned semidefinite physical core or the opposite-scalar cancellation above. The higher-rank/sign-indefinite Schur remainder remains unpaid. Full QFORM remains OPEN; no uniform continuity modulus is claimed.
