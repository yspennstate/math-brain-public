# Checks — account02/B17 random-location / off-axis Poisson barrier

Run: `20260924T074629Z-account02-B17-QFORM-auto11`.

Status: `PASS` for the exact algebra and numerical constants below. These checks support the proof in `REPORT.md`; they do not by themselves prove the unrestricted QFORM target.

## Exact matrix checks

For

\[
B=\frac17\begin{pmatrix}6&-2&-3\\-2&3&-6\\-3&-6&-2\end{pmatrix}
=I-2nn^T,\qquad n=(1,2,3)^T/\sqrt{14},
\]

direct symbolic multiplication gives

\[
B^2=I_3,\qquad \det B=-1,\qquad \operatorname{spec}(B)=\{1,1,-1\}.
\]

Every displayed entry of `B` is nonzero. For the `3m x 3` bank synthesis matrix `T_m` with `m` copies of `e_j/sqrt(m)` in bank `j`, `T_m^T T_m=I_3`; hence `A_m=T_m B T_m^T` has nonzero spectrum exactly `{1,1,-1}`, and every physical entry is `B_jk/m`, hence nonzero.

## Cap-one support and non-Lindeberg check

The physical density

\[
f_m=1_{[-(1-1/m)/2,(1-1/m)/2]}
+1_{[\sqrt m-1/(2m),\sqrt m+1/(2m)]}
\]

has total support length `(1-1/m)+1/m=1` and takes only values `0,1`. The satellite mass is exactly `1/m`.

For every fixed `0<delta<1`, eventually only the satellite contributes to the bankwise Lindeberg tail. If `R=sqrt(m)` and `ell=1/m`, then

\[
m\,\mathbb E[(X/\sqrt m)^2;\ |X|>\delta\sqrt m]
=\int_{R-\ell/2}^{R+\ell/2}x^2\,dx
=1+\frac1{12m^3}\to1.
\]

Thus the triangular array is genuinely non-Lindeberg.

## Characteristic-function expansion

For one normalized physical summand,

\[
\chi_m(t)=\left(1-\frac1m\right)
\operatorname{sinc}\!\left(\frac{t(1-1/m)}{2\sqrt m}\right)
+\frac1m e^{it}\operatorname{sinc}\!\left(\frac{t}{2m\sqrt m}\right).
\]

Using `sinc z = 1-z^2/6+O(z^4)` at fixed `t`,

\[
\chi_m(t)=1+\frac{e^{it}-1-t^2/24}{m}+O_t(m^{-2}),
\]

so

\[
\chi_m(t)^m\to\exp(-t^2/24+e^{it}-1),
\]

the characteristic function of `N(0,1/12)+Poisson(1)`.

## Pinned Theorem-F receiver check

Writing `B=O diag(1,1,-1) O^T`, the physical eigenframe `V_m=T_mO` obeys

\[
V_m^TV_m=I_3,\qquad \|\operatorname{row}_iV_m\|^2=1/m\le1/2,
\]

and the residual quadratic part is zero. Therefore the pinned completed Theorem F at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

applies with `det G_I=1` and `|lambda_1 lambda_2 lambda_3|=1`, giving

\[
|\Phi_m(t)|\le\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.
\]

The exact `L^1` mass of this majorant is `24*pi`.

## Gaussian cone bound check

For the centered comparator `aZ_1^2+bZ_2^2-cZ_3^2`, with `a,b,c>=v0`, the cone-tip formula is

\[
p(0)=\frac1{4\pi}\int_0^{2\pi}
[bc\cos^2\theta+ac\sin^2\theta+ab]^{-1/2}\,d\theta.
\]

The bracket is at least `2v0^2`, so `p(0)<=1/(2sqrt(2)v0)`. The positive-two-square density and the negative one-square density are both decreasing, hence the difference density is globally maximized at zero.

## Numerical constants

At `s=1/12`,

- `C0 = 3*sqrt(2) = 4.242640687119286...`;
- `C1 = 12*exp(-1/2)/sqrt(2*pi) = 2.9036486942297204...`;
- for every nonzero integer Poisson vector, `D>=12`, hence
  `C12 = exp(-6) C0 + (1-exp(-6)) C1 = 2.9069677235466345...`;
- `P(N=(0,0,0))=exp(-3)`;
- therefore
  `C_Pois = exp(-3) C0 + (1-exp(-3)) C12 = 2.9734669647011334...`.

Certified numerical gaps:

\[
\pi-C_{\rm Pois}=0.16812568888865975\ldots>0,
\]

and

\[
3\sqrt2-C_{\rm Pois}=1.2691737224181523\ldots>0.
\]

Result: `PASS_QFORM_RANDOM_LOCATION_OFFAXIS_POISSON_BARRIER`.
