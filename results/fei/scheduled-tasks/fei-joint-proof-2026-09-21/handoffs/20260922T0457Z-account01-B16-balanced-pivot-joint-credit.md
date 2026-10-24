# FEI handoff — account01/B16 balanced-pivot joint credit

Source-bound scientific report: `math-open-problems/proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T043923Z-balanced-pivot-joint-credit/REPORT.md`, report blob `41792659fe7c8b5c26aab463caf58b8e1d0448ca`.

Status: `ESSENTIAL_STEP_APPLIED`; full FEI remains OPEN. Bound to `LIMIT-PRIME-GATE-LIFT-v1`, \(C_*=6.5218512\), \(\Gamma_*=\Gamma_{RO}+0.2682048p(1-p)\).

Consumed exactly: account04/B17 biased restriction cocycle, blob `d32321447c5f30282f243d9a2907ec719d483c92`, and account04/B16 character-tube joint-credit theorem.

New source-exact result at a balanced pivot. For restriction Fourier coefficients \(a_S,b_S\), let
\[
T_S=(a_S^2+b_S^2)/2,\quad c_S=2a_Sb_S/(a_S^2+b_S^2),\quad X_S=|c_S|,\quad \rho=1-2\delta=\sum_ST_Sc_S.
\]
With
\[
\Phi(x)=h_2((1-\sqrt{1-x^2})/2)-h_2((1-x)/2),
\]
the exact retained joint information credit is
\[
\mathcal C_j=h_2(\delta)+\mathbb E_T\Phi(X),
\]
and the complete local cocycle contribution is
\[
\mathcal L_{\Gamma,j}=
\frac{\Gamma(r_0)+\Gamma(r_1)}2-\Gamma((r_0+r_1)/2)
+\Gamma(1/2)\delta-1+\mathbb E_T\Phi(X).
\]
Moreover
\[
\Phi''(x)=\frac{\operatorname{atanh}(\sqrt{1-x^2})}{(1-x^2)^{3/2}\ln2}\ge1/\ln2.
\]
Thus, writing \(A=\mathbb E X-|\rho|\), \(V=\operatorname{Var}(X)\),
\[
\mathbb E\Phi(X)\ge\Phi(|\rho|)+\Phi'(|\rho|)A+V/(2\ln2).
\]
The scalar moment relaxation is sharp: a two-angle non-Boolean relaxation attains \(X=|\rho|\) identically, so any further universal improvement must use Boolean realizability/additional source structure rather than another scalar envelope.

Application of account04/B16: replace its base literal by **any balanced Boolean base** \(g(X)\) in the tensor tube \(f_0=g,\ f_1=gh\) on disjoint variables. The entire joint credit tensorizes exactly, so its cap-six payment and the live \(C_*\) reserve remain valid independent of the arity/internal spectrum of both \(g\) and \(h\).

Next exact obstruction/proof target on the owner's all-gate extremality job: rule out (or construct) an actual composition-prime Boolean restriction pair in the dangerous small-disagreement corridor with simultaneously small orientation loss \(A\), small overlap dispersion \(V\), and insufficient potential midpoint refund. Do not iterate an overlap-only scalar envelope; it is now optimally exhausted at the balanced pivot.
