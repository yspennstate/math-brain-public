Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-03 idea-before-code — exact interior mixed-sign winner-max integration

Target remains the exclusively owned `D0025` residual of Seppäläinen Problem 4, with frozen case `K=2`, `Q=(delta_{1/2}+delta_1)/2` and metric `L <= Delta_2(Q)`. The latest certified baseline is

\[
L=\frac{2500000}{29648439}.
\]

The immediately preceding run integrated the exact mixed-sign kernel only on the two edge triples. The remaining loss is not primarily in the one-dimensional kernel anymore; it is in collapsing a *maximum of lower competitors* to a single representative before integration.

This run rotates to **B15 / B25 / B3**.

## B15 — break the symmetry on purpose

On the near-edge strict mixed branch

\[
Y_{-1}>Y_0>\max(Y_1,Y_2),
\]

and on the central strict mixed branch

\[
Y_2>Y_1>\max(Y_{-2},Y_{-1},Y_0),
\]

a first asymmetric attack is to replace the lower maximum by one selected lower coordinate. This gives a valid positive correction, and testing the algebra shows that different anchors are best in the two branches. But the anchor route necessarily discards mass whenever a different lower competitor wins. It is therefore diagnostic rather than final.

## B25 — count the lower maximum exactly by its winner expansion

Let independent shifted exponentials be

\[
Y_i=s_i+E_i,\qquad E_i\sim\mathrm{Exp}(1),
\]

and let `L` be a finite set of lower competitors,

\[
M=\max_{j\in L}Y_j,\qquad m=\max_{j\in L}s_j.
\]

For `y>=m`,

\[
F_M(y)=\prod_{j\in L}(1-e^{s_j-y}).
\]

Expanding and differentiating gives the exact truncated exponential moment

\[
\mathbb E[e^M;M<y]
=\sum_{\varnothing\ne S\subseteq L}(-1)^{|S|+1}|S|e^{\sum_{j\in S}s_j}h_{|S|}(y;m),
\]

where

\[
h_1(y;m)=y-m,
\]

and for `n>1`,

\[
h_n(y;m)=\frac{e^{-(n-1)m}-e^{-(n-1)y}}{n-1}.
\]

This is the exact winner decomposition; no sampling and no lower-anchor replacement remain.

## B3 — prove a stronger reusable chain-max transform

Assume pointwise `s_U<=s_T`. For

\[
\mathcal T_{p,q}
=\mathbb E[e^{pU+qT+M};\ U>T>M],
\]

with `U=s_U+E_U`, `T=s_T+E_T`, put

\[
y_0=\max(s_T,m),\qquad \lambda=2-p-q.
\]

For `p<1`, `lambda>0`, conditioning on `T=y` gives

\[
\mathbb E[e^{pU};U>y]=\frac{e^{s_U-(1-p)y}}{1-p},
\]

so

\[
\mathcal T_{p,q}
=\frac{e^{s_U+s_T}}{1-p}
\int_{y_0}^\infty e^{-\lambda y}\mathbb E[e^M;M<y]\,dy.
\]

Every subset term is elementary. For `|S|=1`,

\[
\int_{y_0}^\infty e^{-\lambda y}(y-m)dy
=e^{-\lambda y_0}\left(\frac{y_0-m}{\lambda}+\frac1{\lambda^2}\right).
\]

For `|S|=n>1`,

\[
\int_{y_0}^\infty e^{-\lambda y}h_n(y;m)dy
=\frac1{n-1}\left[
\frac{e^{-(n-1)m-\lambda y_0}}{\lambda}
-\frac{e^{-(\lambda+n-1)y_0}}{\lambda+n-1}
\right].
\]

In the present four-step LPP reduction, every shift `s_i` is an order statistic of the three first-layer exponentials on each of six order cones. Hence all terms reduce to exact rational exponential-spacing moments.

For the exact mixed-sign residual, set `a=1-theta`, `b=2-theta`, `kappa=theta/((2-theta)(3-theta))` and define

\[
T_1=\mathcal T_{0,\theta-1},\qquad
T_2=\mathcal T_{-a,0},\qquad
T_3=\mathcal T_{-b,1}.
\]

Then the exact residual beyond the already counted global envelope is

\[
C_{\rm mix}=\frac{\theta}{ab}(T_1-T_2)-\kappa(T_1-T_3).
\]

Apply this once to the near-edge branch with

`U=Y_{-1}`, `T=Y_0`, `L={Y_1,Y_2}`,

and once to the central orientation with

`U=Y_2`, `T=Y_1`, `L={Y_{-2},Y_{-1},Y_0}`,

then use reflection for their partners. These events are strict mixed-sign branches and the two central orientations are disjoint (each forces the opposite ordering of `Y_1` and `Y_{-1}`). Thus their positive residuals may be added to the previously certified global-envelope and edge corrections.

The candidate rational Chernoff point to certify next is `theta=117261/200000`. The candidate target is `G_1(0)<=29645831/10000000`, which would move the frozen metric to `2500000/29645831`. These numbers are **not yet certified in this idea record**; the next step is one exact `Fraction` checker implementing the formulas above and the inherited four-step MGF algebra.
