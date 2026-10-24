# Checks for B14 Gaussian-mixture localization obstruction

Run: `20260924T093427Z-account03-B14-QFORM-auto11`.

## A. Gaussian derivative constant

For `G~N(0,1)` and variance parameter `t>0`,

\[
\|\phi_t'\|_1
=\frac{1}{\sqrt t}\,\mathbb E|G|
=\sqrt{\frac2\pi}\,t^{-1/2}.
\]

At the checked mixture threshold `M=sqrt(2*pi)`,

\[
\sqrt{2/\pi}\,M=2.
\]

Numerically,

- `sqrt(2*pi) = 2.5066282746310002`,
- `sqrt(2/pi) = 0.7978845608028654`,
- product `= 2` to floating-point precision.

The same threshold gives the pointwise cap

\[
M/\sqrt{2\pi}=1.
\]

## B. Fragment variation

For

\[
f_{N,L}=1_{\cup_{k=0}^{N-1}I_k}
\]

with disjoint intervals, every interval contributes one upward and one downward jump, hence

\[
\operatorname{Var}(f_{N,L})=2N.
\]

Therefore weak approximation by Gaussian mixtures with moments `M_j` requires

\[
2N\le\sqrt{2/\pi}\liminf M_j,
\]

or

\[
\liminf M_j\ge N\sqrt{2\pi}.
\]

For `N=2`, this is already `>=5.013256549262...`, twice the allowed owner-normalized value.

## C. Quantitative L1 lower bound

The report proves

\[
\|f_{N,L}-g\|_1\ge\frac{2N-V}{N+L^{-1}}
\]

for every probability density `0<=g<=1` with variation at most `V`.

At `V=2` and `L=10` this becomes

| N | lower bound |
|---:|---:|
| 2 | 0.9523809523809523 |
| 4 | 1.4634146341463417 |
| 8 | 1.7283950617283952 |
| 16 | 1.8633540372670805 |

As `L->infinity` the bound is `2-2/N`, approaching the maximal possible L1 distance `2`.

## D. Partner QFORM matrix

For

\[
B_*=I_3-\frac23 11^T,
\]

one has `B_*^2=I_3`, hence eigenvalues `{1,1,-1}` and least absolute eigenvalue `sigma=1`. The completed account04/B14 theorem therefore gives

\[
\|p_{X^TB_*X}\|_{\infty,\mathrm{ess}}\le6\sqrt\pi
=10.634723105433096\ldots
\]

for every independent cap-one choice of the three marginals, including the separated-fragment and unbounded-support examples in the report.

## E. Scope checks

- No moment of the target rough input law is assumed.
- No compact-support or connected-support assumption is introduced.
- The Gaussian-mixture obstruction concerns only the proposed localization mechanism; it is not a QFORM counterexample.
- The weak-closure argument uses only distributional BV lower semicontinuity and therefore is compatible with the Portmanteau-style limits used elsewhere in the fleet.
- Translation of all fragments leaves the inverse-scale moment and total variation unchanged.
- The partner result used is exactly `math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`.
