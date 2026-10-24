SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-24T08:06:44Z.
attacking: distribution-free L^3 control of the shared product receiver in the exact fold-aligned stress family, plus exact uniform cone-tip optimization.

# account03/B17 r12 — distribution-free shared-fold receiver and exact cone-tip

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Initial control commit: `math-research-brain@01d9c7a0e377b19ce12e9bf3e31e7f6761f9b6a0`  
Prepublication refreshed control commit: `math-research-brain@d720fd343b34b0499018bb5bcc839a21133e0c3a`  
Owner control revision: `2026-09-22.15`  
Live correction inbox blob at refresh: `ba7aeac3d879f59da5ec8a12daad74ea85714465`  
Memory protocol blob: `0d902d56688f4b5c575f5b921ddf9f6709e88312`.

The unrestricted conjecture is not proved or disproved here. This report addresses the sharp-witness role only. It uses original-coordinate independence throughout and does not invoke a post-rotation independence claim, a pointwise van-der-Corput bound, an arbitrary-joint coarea lemma, or a fiber-supremum estimate.

## 1. Completed partner result actually used

The designated partner `account04/B17` proved `QFORM-SHARED-FOLD-LOGRECEIVER-UNIFORM-v1` in

`yspennstate/math-open-problems@d2795ffa95ffde81e63da02b677fdc3c0ea950a1`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260924T061346Z-account04-B17-QFORM-r7/REPORT.md`.

For independent uniforms on `[-1/2,1/2]` and `0<theta<=1`, it studies

\[
Q_\theta=\theta X^2+2XU+\theta^{-1}U^2+2YV
       =(\sqrt\theta X+\theta^{-1/2}U)^2+2YV.
\tag{1.1}
\]

The original-coordinate coefficient matrix has nonzero spectrum

\[
\{\theta+\theta^{-1},1,-1\},
\tag{1.2}
\]

so every member is an exact target instance. The partner proved the uniform-input global bound

\[
\|p_{Q_\theta}\|_\infty\le 2\sqrt6.
\tag{1.3}
\]

Its stated next step was a distribution-free replacement for the explicit uniform product kernel. That is the first essential implication attacked below.

## 2. A distribution-free product-density `L^3` lemma

### Lemma 2.1
Let `Y,V` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. Let `P=YV`, and let `r` denote its density. Then

\[
\|r\|_3^3\le I_*,
\tag{2.1}
\]

where

\[
I_*=
\frac{1152}{25}+\frac{48}{5}\log5
+\frac{144}{25}(\log5)^2
+\frac{32}{25}(\log5)^3
=81.78688343097915\ldots.
\tag{2.2}
\]

Consequently, if `T=2YV` and `k` is its density, then

\[
\boxed{
\|k\|_3^3\le C_*=\frac{I_*}{4}
=\frac{288}{25}+\frac{12}{5}\log5
+\frac{36}{25}(\log5)^2
+\frac{8}{25}(\log5)^3
}
\tag{2.3}
\]

and

\[
C_*=20.44672085774479\ldots,
\qquad
\|k\|_3\le C_*^{1/3}=2.734478770302084\ldots.
\tag{2.4}
\]

### Proof
For `p!=0`, the standard product-density formula gives

\[
r(p)=\int_{\mathbb R} f(y)g(p/y)\frac{dy}{|y|}.
\tag{2.5}
\]

First, Cauchy--Schwarz yields a global power envelope. Put

\[
F_p(y)=f(y)g(p/y).
\]

Then

\[
\begin{aligned}
r(p)^2
&\le \left(\int F_p(y)\,dy\right)
       \left(\int F_p(y)\frac{dy}{y^2}\right)\\
&\le 1\cdot
\frac1{|p|}\int f(p/v)g(v)\,dv
\le \frac1{|p|}.
\end{aligned}
\tag{2.6}
\]

Thus

\[
\boxed{r(p)\le |p|^{-1/2}.}
\tag{2.7}
\]

Second, for `0<|p|<1/4`, split (2.5) into

\[
|y|<2|p|,\qquad 2|p|\le |y|\le\frac12,
\qquad |y|>\frac12.
\]

On the first piece use `v=p/y`. Since then `|v|>1/2`,

\[
\int_{|y|<2|p|} f(y)g(p/y)\frac{dy}{|y|}
=\int_{|v|>1/2}f(p/v)g(v)\frac{dv}{|v|}
\le 2.
\tag{2.8}
\]

The middle piece is bounded only by the caps,

\[
\int_{2|p|\le|y|\le1/2}\frac{dy}{|y|}
=2\log\frac1{4|p|},
\tag{2.9}
\]

and the last piece is at most `2 int f <=2`. Hence

\[
\boxed{
r(p)\le 4+2\log\frac1{4|p|}
\quad (0<|p|<1/4).
}
\tag{2.10}
\]

Use (2.10) for `|p|<=1/100` and (2.7) outside. Then

\[
\begin{aligned}
\int_{\mathbb R}r(p)^3\,dp
&\le
2\int_0^{1/100}
\left(4+2\log\frac1{4p}\right)^3dp
+2\int_{1/100}^{\infty}p^{-3/2}dp\\
&=
\frac{32}{25}(\log5)^3+\frac{144}{25}(\log5)^2
+\frac{48}{5}\log5+\frac{152}{25}+40,
\end{aligned}
\tag{2.11}
\]

which is exactly (2.2). Finally `k(t)=r(t/2)/2`, so

\[
\int k(t)^3dt
=\frac14\int r(p)^3dp,
\tag{2.12}
\]

giving (2.3). QED.

This lemma allows arbitrary fragmented, disconnected and unbounded supports. No moments or centering are used.

## 3. The square branch has a universal `L^{3/2}` bound

Let `0<theta<=1`, set

\[
a=\sqrt\theta,\qquad b=\theta^{-1/2}=a^{-1},
\]

and for independent cap-one `X,U` define

\[
S=aX+bU,\qquad W=S^2.
\tag{3.1}
\]

Since the density of `bU` is bounded by `1/b=a` and convolution with a probability density does not increase `L^infinity`,

\[
\|p_S\|_\infty\le a.
\tag{3.2}
\]

For `w>0`,

\[
h(w):=p_W(w)
=\frac{p_S(\sqrt w)+p_S(-\sqrt w)}{2\sqrt w}
\le \frac{a}{\sqrt w}.
\tag{3.3}
\]

A useful sharp-enough `L^{3/2}` estimate follows directly from the one-dimensional cap. Put

\[
F(r)=p_S(r)+p_S(-r),\qquad r>0.
\]

Then `F<=2a`, `int_0^infinity F=1`, and after `w=r^2`,

\[
\begin{aligned}
\int_0^\infty h(w)^{3/2}dw
&=2^{-1/2}\int_0^\infty F(r)^{3/2}r^{-1/2}dr\\
&\le \sqrt a\int_0^\infty F(r)r^{-1/2}dr
=\sqrt a\,\mathbb E|S|^{-1/2}.
\end{aligned}
\tag{3.4}
\]

Among probability densities bounded by `a`, the decreasing weight `|s|^{-1/2}` is maximized by density `a` on the centered interval of length `1/a` (the elementary bathtub principle). Therefore

\[
\mathbb E|S|^{-1/2}
\le a\int_{-1/(2a)}^{1/(2a)}|s|^{-1/2}ds
=2\sqrt{2a}.
\tag{3.5}
\]

Combining (3.4)--(3.5),

\[
\int h^{3/2}\le2\sqrt2\,a,
\qquad
\boxed{\|h\|_{3/2}\le2a^{2/3}=2\theta^{1/3}.}
\tag{3.6}
\]

## 4. Distribution-free shared-fold theorem

### Theorem 4.1 — `QFORM-SHARED-FOLD-DISTRIBUTION-FREE-v1`
Let `X,U,Y,V` be independent real random variables with arbitrary probability densities bounded by one. For `0<theta<=1`, define

\[
Q_\theta=\theta X^2+2XU+\theta^{-1}U^2+2YV.
\tag{4.1}
\]

Then `Q_theta` has a bounded continuous density and

\[
\boxed{
\|p_{Q_\theta}\|_\infty
\le B_*\,\theta^{1/3},
\qquad
B_*=2C_*^{1/3}
=5.468957540604169\ldots .
}
\tag{4.2}
\]

The coefficient matrix has exact nonzero spectrum

\[
\boxed{\{\theta+\theta^{-1},1,-1\}.}
\tag{4.3}
\]

### Proof
The algebraic identity from the completed partner theorem is

\[
Q_\theta=S^2+T,
\qquad S=\sqrt\theta X+\theta^{-1/2}U,
\qquad T=2YV.
\tag{4.4}
\]

The variables `S` and `T` are independent because they use disjoint original coordinates. By Sections 2--3, their output densities satisfy

\[
\|p_{S^2}\|_{3/2}\le2\theta^{1/3},
\qquad
\|p_T\|_3\le C_*^{1/3}.
\]

Holder/Young at conjugate exponents gives

\[
\|p_{Q_\theta}\|_\infty
\le \|p_{S^2}\|_{3/2}\|p_T\|_3
\le2C_*^{1/3}\theta^{1/3}.
\tag{4.5}
\]

Continuity is also proved in this branch: translations are continuous in `L^3`, and

\[
|p_Q(q+t)-p_Q(q)|
\le \|p_{S^2}\|_{3/2}
\|\tau_t p_T-p_T\|_3\to0.
\tag{4.6}
\]

The spectrum statement is the partner's exact block calculation: after a coordinate permutation the matrix is

\[
\begin{pmatrix}\theta&1\\1&\theta^{-1}\end{pmatrix}
\oplus
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

whose first block has eigenvalues `theta+theta^{-1},0` and whose second has `1,-1`. QED.

A concrete target-level consequence uses the already established fleet obstruction `C_univ>=3sqrt(2)`. Define

\[
\theta_{\rm sharp}
=\left(\frac{3\sqrt2}{B_*}\right)^3
=\frac{27\sqrt2}{4C_*}
=0.4668690697365586\ldots .
\tag{4.7}
\]

Then for every `0<theta<=theta_sharp` and **every** cap-one choice of the four independent laws,

\[
\boxed{\|p_{Q_\theta}\|_\infty\le3\sqrt2.}
\tag{4.8}
\]

Thus the near-singular shared-fold regime up to the explicit parameter `0.466869...` cannot produce a witness above the known global lower obstruction, even with arbitrary fragmentation/asymmetry/unbounded support.

## 5. Actual inequality combining the completed partner result

For the partner's uniform-input family, both its theorem (1.3) and Theorem 4.1 apply. Hence the same exact target matrices satisfy

\[
\boxed{
\|p_{Q_\theta}^{\rm unif}\|_\infty
\le
\min\left\{2\sqrt6,\ B_*\theta^{1/3}\right\}.
}
\tag{5.1}
\]

The new law-uniform estimate is stronger than the partner's `2sqrt6` estimate whenever

\[
\theta\le
\left(\frac{2\sqrt6}{B_*}\right)^3
=0.7187919549032324\ldots .
\tag{5.2}
\]

This is the required completed-partner application to an actual inequality, not merely a citation.

## 6. Exact cone-tip for the uniform partner family

The same family permits a closed-form stress calculation at output zero.
Let `a=sqrt(theta)`, and set

\[
c=\frac{a^{-1}-a}{2},
\qquad
d=\frac{a^{-1}+a}{2},
\qquad d^2-c^2=1.
\tag{6.1}
\]

For uniform `X,U`, the density of

\[
S=aX+a^{-1}U
\]

is even and, for `r>=0`,

\[
g_\theta(r)=
\begin{cases}
a,&0\le r\le c,\\
d-r,&c<r<d,\\
0,&r\ge d.
\end{cases}
\tag{6.2}
\]

The receiver `T=2YV` has density

\[
k(t)=\log\frac1{2|t|}\,\mathbf1_{0<|t|<1/2}.
\tag{6.3}
\]

Since `d>=1`, put `R=1/sqrt(2)`. At zero,

\[
p_{Q_\theta}(0)
=2\int_0^R g_\theta(r)
\log\frac1{2r^2}\,dr.
\tag{6.4}
\]

If `c>=R`, equivalently `theta<=2-sqrt(3)`, the plateau covers the whole integral and

\[
\boxed{p_{Q_\theta}(0)=2\sqrt{2\theta}.}
\tag{6.5}
\]

If `2-sqrt(3)<theta<=1`, then `0<=c<R`. Using

\[
\int \log\frac1{2r^2}dr
=r\left(\log\frac1{2r^2}+2\right),
\]

and

\[
\int r\log\frac1{2r^2}dr
=\frac{r^2}{2}\left(\log\frac1{2r^2}+1\right),
\]

one obtains

\[
\boxed{
 p_{Q_\theta}(0)
 =\sqrt2(a+a^{-1})-\frac12
 -c^2\left(3+\log\frac1{2c^2}\right),
}
\tag{6.6}
\]

with the last term interpreted by continuity at `c=0`.

This cone-tip is maximized at `theta=1`. Indeed on `0<=c<=1/sqrt2`, using `d=sqrt(1+c^2)`, write

\[
P(c)=2\sqrt2\sqrt{1+c^2}-\frac12
-c^2\left(3+\log\frac1{2c^2}\right).
\]

For `c>0`,

\[
P'(c)=2c\left[
\frac{\sqrt2}{\sqrt{1+c^2}}
-2-\log\frac1{2c^2}
\right]<0,
\tag{6.7}
\]

because the logarithm is nonnegative and `sqrt2/sqrt(1+c^2)<2`. The outer branch (6.5) is increasing in `theta`. Therefore

\[
\boxed{
\sup_{0<\theta\le1}p_{Q_\theta}^{\rm unif}(0)
=2\sqrt2-\frac12
=2.328427124746190\ldots .
}
\tag{6.8}
\]

This is only a cone-tip statement; no claim is made here that zero is the global mode for every `theta`.

## 7. Interpretation for the witness search

The completed partner result showed that the exact fold-aligned uniform family is globally bounded by `2sqrt6`. The new theorem removes the uniform-law restriction in the genuinely near-singular portion and proves a quantitative law-uniform `theta^(1/3)` gain. The product receiver `2YV` retains an `L^3` bound even for arbitrary cap-one fragmented laws; this is precisely the distribution-free replacement requested by the partner's handoff.

The result is not the full conjecture. It uses the exact algebraic decomposition (4.4), hence does not automatically control arbitrary shared-bank convex/two-sheet collars, extra active spectrum, or forms in which the logarithmic receiver is coupled to the square branch through the same original coordinates.

The known universal lower obstruction remains `C_univ>=3sqrt(2)`; this run does not improve that lower bound and does not prove it is sharp. The next B17 witness frontier should therefore force the product receiver to lose the independent convolution structure, or introduce several non-collinear macroscopic shared rows / extra spectrum while preserving an exact target-level density certificate.

Continuity is proved for Theorem 4.1, but full-target continuity remains open.

## 8. Checks recorded

The companion `CHECKS.json` records the exact constants

- `I_* = 81.78688343097915...`,
- `C_* = 20.44672085774479...`,
- `B_* = 5.468957540604169...`,
- `theta_sharp = 0.4668690697365586...`,
- partner crossover `0.7187919549032324...`,
- uniform cone-tip maximum `2sqrt2-1/2 = 2.328427124746190...`.

All computations are consequences of the displayed exact expressions; no Monte Carlo evidence is used.
