# QFORM B17 r26 — two-heavy / one-diffuse cone-tip no-escape

Run: `20260923T080143Z-account03-B17-QFORM-r26`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control at start: revision `2026-09-22.15`  
Status: `SUPPORTING_SHARP-WITNESS_THEOREM`; full QFORM remains OPEN; full-target continuity remains OPEN; `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

Let `X,Y` be independent real random variables with arbitrary probability densities `f,g` satisfying `0<=f,g<=1`. Let

\[
G\sim N(0,1/12)
\]

be independent of `(X,Y)`, and put

\[
Q_\infty=X^2-Y^2+G^2.
\]

Then the canonical convolution density at the cone tip satisfies

\[
\boxed{
 p_{Q_\infty}(0)\le C_{2h}:=
 \sqrt{\frac6\pi}\int_0^\infty
 w^{-1/2}e^{-6w}\,2\operatorname{arsinh}\!\frac1{2\sqrt w}\,dw .
}
\]

Moreover

\[
C_{2h}=3.8854582723685536471\ldots
\]

and, without relying on that numerical evaluation,

\[
\boxed{
C_{2h}\le \log 24+\gamma+\frac{2}{\sqrt{6\pi}}
<3\sqrt2 .
}
\]

Here `gamma` is Euler's constant. Thus **two completely arbitrary cap-one macroscopic heavy coordinates, one of each sign, plus one minimum-variance Gaussian diffuse direction cannot attain the known `3 sqrt(2)` obstruction at the indefinite cone tip**.

There is an exact source-valid finite-dimensional version. For `m>=3`, let `Z_1,...,Z_m` be independent `Unif[-1/2,1/2]`, independent of arbitrary cap-one `X,Y`, and set

\[
G_m=m^{-1/2}\sum_{k=1}^m Z_k,
\qquad
Q_m=X^2-Y^2+G_m^2.
\]

The physical matrix is

\[
A_m=\operatorname{diag}\!\left(1,-1,\frac1mJ_m\right),
\]

so its nonzero spectrum is **exactly** `{1,-1,1}` for every finite `m`. Every physical input density is at most one. If `p_m` denotes the canonical convolution density, then uniformly over the two arbitrary heavy laws,

\[
\boxed{
\limsup_{m\to\infty}\ \sup_{f,g\le1}p_m(0)\le C_{2h}<3\sqrt2 .
}
\]

The weighted local Edgeworth theorem of the designated partner `account04/B17` yields the sharper source-valid expansion of the common upper envelope

\[
\sup_{f,g\le1}p_m(0)
\le C_{2h}-\frac{J_{2h}}{20m}+O(m^{-2}),
\]

where

\[
J_{2h}=\int_0^\infty k(w)\,2\operatorname{arsinh}\!\frac1{2\sqrt w}\,
H_4(\sqrt{12w})\,dw,
\quad
k(w)=\sqrt{\frac6\pi}w^{-1/2}e^{-6w}.
\]

The deterministic diagnostic gives `J_{2h}=3.87135964150179...`; its sign is not needed for the strict `3 sqrt(2)` exclusion.

## 2. Square-density envelope

If a real random variable `T` has density `r<=1`, the law of `U=T^2` has, for a.e. `u>0`, density

\[
h_U(u)=\frac{r(\sqrt u)+r(-\sqrt u)}{2\sqrt u}.
\]

Hence

\[
0\le h_U(u)\le u^{-1/2},\qquad \int_0^\infty h_U(u)\,du=1.
\tag{2.1}
\]

This uses only the density cap and no moment, support, symmetry, connectedness, or log-concavity assumption.

## 3. Sharp shifted cross-correlation envelope

Let `h_1,h_2` be arbitrary probability densities on `(0,infinity)` satisfying (2.1). For every `w>0`, define

\[
C_{12}(w)=\int_0^\infty h_1(u)h_2(u+w)\,du.
\]

Since `h_2(u+w)<=(u+w)^(-1/2)`, one has

\[
C_{12}(w)\le \int_0^\infty h_1(u)(u+w)^{-1/2}\,du.
\]

The reward `(u+w)^(-1/2)` is decreasing in `u`. Under the constraints

\[
0\le h_1(u)\le u^{-1/2},\qquad \int h_1=1,
\]

the one-dimensional bathtub principle therefore places all available mass as far left as possible. Since

\[
\int_0^{1/4}u^{-1/2}du=1,
\]

the maximizing envelope is `u^(-1/2) 1_(0,1/4)(u)`. Consequently

\[
\begin{aligned}
C_{12}(w)
&\le \int_0^{1/4}\frac{du}{\sqrt{u(u+w)}}\\
&=2\operatorname{arsinh}\sqrt{\frac{1}{4w}}
=2\operatorname{arsinh}\frac1{2\sqrt w}.
\end{aligned}
\tag{3.1}
\]

This is the essential product-preserving step: the second heavy law is used only through its exact square-density cap, while the first is optimized by a genuine cap-one bathtub argument. Fragmented or remotely translated supports are fully allowed.

## 4. Gaussian diffuse direction

For `G~N(0,1/12)`, `W=G^2` has density

\[
k(w)=\sqrt{\frac6\pi}\,w^{-1/2}e^{-6w},\qquad w>0.
\tag{4.1}
\]

Write `U=X^2` and `V=Y^2`. At the cone tip,

\[
Q_\infty=0\iff V=U+W.
\]

Therefore its convolution representative is

\[
p_{Q_\infty}(0)
=\int_0^\infty k(w)
\left[\int_0^\infty h_U(u)h_V(u+w)du\right]dw.
\]

Combining (3.1) and (4.1) proves the integral definition of `C_{2h}`. The majorant is integrable: it is `O(w^{-1/2} log(1/w))` at zero and exponentially decaying at infinity.

## 5. Analytic strict gap below `3 sqrt(2)`

For `w>0`,

\[
2\operatorname{arsinh}\frac1{2\sqrt w}
=-\log w+2\log\frac{1+\sqrt{1+4w}}2.
\]

Because `sqrt(1+4w)<=1+2sqrt(w)` and `log(1+x)<=x`,

\[
2\operatorname{arsinh}\frac1{2\sqrt w}
\le -\log w+2\sqrt w.
\tag{5.1}
\]

If `W=G^2=Z^2/12` with `Z~N(0,1)`, then

\[
\mathbb E[-\log W]=\log24+\gamma,
\qquad
\mathbb E\sqrt W=\frac1{\sqrt{6\pi}}.
\]

Taking expectation in (5.1) gives

\[
C_{2h}\le \log24+\gamma+\frac2{\sqrt{6\pi}}
=4.215928361211258\ldots
<4.242640687119285\ldots=3\sqrt2.
\tag{5.2}
\]

The strict comparison can be certified with elementary rational enclosures (for example `gamma<0.578`, `log 24<3.179`, `pi>3.141`, `sqrt(2)>1.414`), which give the left side `<4.218` and the right side `>4.242`. The high-precision integral value `3.885458...` is diagnostic; inequality (5.2) is the proof.

## 6. Exact finite source-valid transfer and designated-partner application

For the normalized uniform bank

\[
G_m=m^{-1/2}\sum_{k=1}^mZ_k,
\]

let `g_m` be its density and `W_m=G_m^2`. Since `g_m` is even,

\[
k_m(w)=\frac{g_m(\sqrt w)}{\sqrt w},\qquad w>0.
\]

The exact same argument as Sections 2--4 gives, uniformly over arbitrary cap-one heavy laws,

\[
p_m(0)\le
\int_0^\infty k_m(w)\,2\operatorname{arsinh}\frac1{2\sqrt w}\,dw.
\tag{6.1}
\]

Now apply the completed `account04/B17` weighted local Edgeworth theorem from

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

With `sigma^2=1/12`, it states

\[
g_m(y)=\gamma_\sigma(y)
\left[1-\frac1{20m}H_4(y/\sigma)\right]
+O(m^{-2})(1+|y|)^{-8}.
\tag{6.2}
\]

After substituting `y=sqrt(w)` into (6.1), the weighted remainder is integrable because

\[
w^{-1/2}(1+\sqrt w)^{-8}
\operatorname{arsinh}(1/(2\sqrt w))
\]

is integrable at both zero and infinity. Therefore (6.1)--(6.2) yield, **uniformly in the two arbitrary heavy laws**,

\[
p_m(0)\le C_{2h}-\frac{J_{2h}}{20m}+O(m^{-2}),
\]

and in particular

\[
\limsup_m\sup_{f,g\le1}p_m(0)\le C_{2h}<3\sqrt2.
\]

This is an actual application of the designated partner theorem to a new inequality, not merely a citation.

The same partner report supplies the independent exact rotated finite-dimensional witness

\[
p_{Q_m^{\rm partner}}(0)
=3\sqrt2\left(1-\frac{5295}{21952m}+O(m^{-2})\right),
\]

with exact nonzero spectrum `{1,1,-1}` and cap-one physical inputs. Hence if `C_*` denotes the universal QFORM constant (if finite), then

\[
\boxed{
\limsup_m\sup_{f,g\le1}p_m(0)
\le C_{2h}<3\sqrt2\le C_*.
}
\]

Thus the mixed-leverage mechanism “two arbitrary macroscopic opposite-sign coordinates plus one minimum-variance diffuse bank” cannot explain a sharp constant larger than `3 sqrt(2)` at the cone tip.

## 7. Scope and next frontier

This does **not** prove the full QFORM conjecture and does not prove that `3 sqrt(2)` is the universal sharp constant. It controls only the cone-tip value for the stated two-heavy/one-diffuse architecture (and its exact finite uniform-bank realization). Off-center output levels can have a different bathtub geometry because the square-density singularity moves away from the origin. General rotations that mix the two heavy coordinates with the diffuse direction also leave this exact product decomposition.

Accordingly the next B17 witness mechanisms are genuinely different: an off-center/two-sheet optimizer in the two-heavy boundary, a fixed nontrivial rotation mixing the heavy and diffuse directions, or a multiscale configuration with at least two non-collinear shared-coordinate heavy rows. Any claim above `3 sqrt(2)` must be source-valid at finite dimension and survive all current correction constraints.

Continuity is not claimed for the arbitrary-heavy theorem here. The designated partner's exact rotated witness has continuous density; full-target continuity remains open.

## 8. Controls and integrity

The run consumed the current QFORM controls and live corrections before the mathematical write. It does not use law-uniform pointwise van-der-Corput decay, post-rotation independence, arbitrary-joint rank-three coarea, conditional projection-density moments, fixed fragment counts, a single-minor reciprocal estimate, or Monte Carlo extremality. Numerical values in the checker are diagnostics; the strict `3 sqrt(2)` gap follows from the analytic bound (5.2).
