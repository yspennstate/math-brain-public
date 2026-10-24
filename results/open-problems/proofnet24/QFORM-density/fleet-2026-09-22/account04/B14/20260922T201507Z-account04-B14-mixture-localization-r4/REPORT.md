# QFORM-DENSITY — B14 law-level mixture localization

Run: \`20260922T201507Z-account04-B14-mixture-localization-r4\`

Status: \`SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN / CONTINUITY_NOT_TRANSFERRED / WITHOUT_VERIFIED_BRAIN\`.

## Theorem

For every probability density \(0\le f\le1\), \(\int f=1\), there are compactly supported densities
\[
g_m=\sum_{\nu=1}^{N_m}\theta_{m,\nu}\mathbf 1_{E_{m,\nu}},
\qquad \theta_{m,\nu}\ge0,\quad \sum_\nu\theta_{m,\nu}=1,
\]
where every \(E_{m,\nu}\) is a finite union of intervals with \(|E_{m,\nu}|=1\), such that
\[
\|g_m-f\|_{L^1}\to0.
\]
Thus every cap-one product law is a total-variation limit of finite convex mixtures of product-indicator laws, and every measurable pushforward has the same property.

Consequently, any uniform estimate
\[
\Pr\{P(U_1,\ldots,U_n)\in I\}\le C|I|
\]
proved for independent \(U_i\sim\mathrm{Unif}(E_i)\), with each \(E_i\) a compact finite interval union of total length one, transfers with the identical constant \(C\) to all independent cap-one densities. The transfer is simultaneous for every interval and bounded measurable test function.

## Proof

First replace \(f\) by
\[
f_R=f\mathbf1_{[-R,R]}+\mathbf1_{F_R},
\]
where \(F_R\subset\mathbb R\setminus[-R,R]\) is bounded and has measure
\(\delta_R=1-\int_{-R}^R f\). Then \(0\le f_R\le1\), \(\int f_R=1\), and
\[
\|f_R-f\|_1\le2\delta_R\to0.
\]

On a grid of mesh \(1/M\), let \(h_M\) be the conditional expectation of \(f_R\). Then \(h_M\to f_R\) in \(L^1\). If \(h_M=a_j\) on the finitely many grid cells \(C_j\), then
\[
0\le a_j\le1,\qquad \sum_j a_j=M.
\]
Hence \(a\) lies in the hypersimplex
\[
\mathcal H_{N,M}=\{a\in[0,1]^N:\sum_j a_j=M\}.
\]
Its extreme points are exactly the \(0\)-\(1\) vectors with \(M\) ones: two fractional coordinates permit an opposite perturbation, and the integer sum rules out exactly one fractional coordinate. Therefore
\[
a=\sum_\nu\theta_\nu v^\nu.
\]
Putting \(E_\nu=\bigcup_{j:v^\nu_j=1}C_j\) gives \(|E_\nu|=M/M=1\) and
\[
h_M=\sum_\nu\theta_\nu\mathbf1_{E_\nu}.
\]

Coordinatewise expansion gives finite mixtures of product indicators. The telescoping inequality
\[
\left\|\prod_i g_i-\prod_i f_i\right\|_1
\le\sum_i\|g_i-f_i\|_1
\]
and contraction of total variation under measurable pushforwards complete the proof.

## Partner application

Apply account01/B14's range-aligned disjoint-bank theorem, run
\`20260922T192403Z-account01-B14-qform-r18\`, canonical
\`math-open-problems@fc439d3b6583c19f36900489b54e4f2c7f54cd0f\`,
componentwise and then use the mixture compiler.

For
\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m),
\]
write
\[
U_m=m^{-1/2}\sum_{j=1}^mX_j,\qquad
V_m=m^{-1/2}\sum_{j=m+1}^{2m}X_j.
\]
For arbitrary independent cap-one inputs,
\[
\boxed{\ \|p_{X_0^2+U_m^2-V_m^2}\|_\infty
\le\pi\sqrt2<4.443\ },
\]
uniformly in \(m\). The same transfer applies to the partner theorem's arbitrary range-aligned outside blocks and couplings. No support radius, moment, translation, separation, or fragment-count parameter appears.

## Continuity and residual

This theorem transfers essential \(L^\infty\) bounds, not continuity: total-variation limits of continuous densities need not be continuous. The full conjecture remains open. The localization-specific obstruction in the active/outside quotient remains kernel leakage \(P_{\ker B}C\).

Fresh control: owner revision \`2026-09-22.15\`; correction inbox blob \`c7000cf3822ae4935a2faf43b89ac92ea65ac0fe\`. No scheduler or notification state was changed.
