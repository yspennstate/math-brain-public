# QFORM B17 checkpoint — one-heavy majority-sign Gaussian-completion branch

Run: B17-20260923T014533Z-r14-multiscale. Full conjecture remains OPEN.

Exact source-valid finite family:

\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m),
\]

so the nonzero spectrum is exactly \(\{1,1,-1\}\) for every \(m\). Put an arbitrary independent cap-one density on the singleton coordinate and iid \(\mathrm{Unif}[-1/2,1/2]\) laws on both banks. In the diffuse limit,

\[
Q_\infty=X^2+G_+^2-G_-^2,\qquad G_\pm\stackrel{iid}{\sim}N(0,1/12).
\]

The difference \(D=G_+^2-G_-^2=(G_++G_-)(G_+-G_-)\) has density

\[
d(w)=\frac6\pi K_0(6|w|).
\]

For each output \(s\), bathtub optimization over all \(0\le f_X\le1\), \(\int f_X=1\), reduces the exact optimum to a measure-one top set of \(x\mapsto d(|s-x^2|)\). For \(0\le s\le1/8\) that set is \([-1/2,1/2]\); for \(s\ge1/8\) it is \([-a,-b]\cup[b,a]\), \(a-b=1/2\), \(a^2+b^2=2s\). For \(s<0\) it is again the centered interval.

Two rigorous Bessel envelopes appear sufficient to close the branch below \(3\sqrt2\):

1. From \(K_0(z)\le E_1(z)+\log2\le-\log(z/2)-\gamma+z\), for \(0\le s\le1/8\), the optimized density is at most
\[
U(s)=\frac6\pi\left(J(s)-\log3-\gamma+6A(s)\right),
\]
where \(J(s)=\int_{-1/2}^{1/2}-\log|s-x^2|dx\) and \(A(s)=\int_{-1/2}^{1/2}|s-x^2|dx\). Writing \(a=\sqrt s\), direct differentiation gives
\[
U'(a)\propto -2\log\frac{1/2+a}{1/2-a}+24a(2a-1/2)\le0
\]
through \(a\le1/(2\sqrt2)\). Therefore
\[
U(s)\le U(0)=\frac6\pi\left(\frac52+\log\frac43-\gamma\right)=4.2216798636\ldots<3\sqrt2.
\]

2. For \(s\ge1/8\), the distance variable \(|x^2-s|\) on its top measure-one shell is stochastically increasing in \(s\), so the exact optimized kernel integral is maximized at \(s=1/8\). Using \(\cosh t\ge1+t^2/2\),
\[
K_0(z)\le e^{-z}\sqrt{\frac\pi{2z}},
\]
and at \(s=1/8\) this gives
\[
F(1/8)\le 2\sqrt{\frac3\pi}\left[\frac\pi4(1+e^{-3/4})+\operatorname{arcosh}\sqrt2\right]
=3.9826334201\ldots<3\sqrt2.
\]

The required newest-Claude Theorem C at math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 already gives the coarser real obstruction \(p(s)\le\pi\sqrt2\) for every \(s\ge0\) in this (+,+,-) rank-three family. The calculation above is a source-specific refinement designed to close the remaining \(\pi\sqrt2-3\sqrt2\) gap in the one-heavy majority-sign Gaussian-completion branch.

Designated partner fleet03/B17 r21 (brain handoff commit 4a7cd066fae31f7abec97aa260eecab09f80cb7b) independently closes the complementary one-heavy minority-sign branch, with exact limiting optimum \(\sqrt{6\pi}\,\mathrm{erf}(\sqrt{3/2})=3.9801056750\ldots<3\sqrt2\). Final write-up will combine the two sign placements and state explicitly that finite/mesoscopic overshoot remains unexcluded.
