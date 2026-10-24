# account02/B10 auto11 — Fejer-kernel constant sharpening

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T141506Z-auto11-account02-B10`  
B10 lens: exact constants, arithmetic, adversarial interfaces.

Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **PROVED CONSTANT IMPROVEMENT.** This does not lower the multiplicity threshold by itself. Combined with the already-complete account02/B10 nine-direction replacement proof, it sharpens that candidate's universal constant. It does **not** solve unrestricted three-eigenvalue QFORM.

## 1. A Fejer replacement for the Gaussian small-ball step

Use the manuscript Fourier convention

\[
\widehat f(t)=\int_{\mathbb R}e^{itx}f(x)\,dx.
\]

For `0<c<2*pi`, put

\[
K_c(x)=\left(\frac{\sin(cx/2)}{cx/2}\right)^2,
\qquad
\widehat K_c(t)=\frac{2\pi}{c}\left(1-\frac{|t|}{c}\right)_+ .
\tag{1.1}
\]

On `|x|<=1`, monotonicity of `sin x/x` on `(0,pi)` gives

\[
K_c(x)\ge m_c:=\left(\frac{\sin(c/2)}{c/2}\right)^2.
\tag{1.2}
\]

Suppose a real random variable `R` satisfies

\[
|\phi_R(t)|\le \left(\frac{4\pi e}{L|t|}\right)^{1/4},\qquad t\ne0.
\tag{1.3}
\]

Then Fourier inversion for the integrable Fejer kernel, followed only by absolute values, gives for every center `a` and `rho>0`

\[
\begin{aligned}
\mathbb P\{|R-a|\le\rho\}
&\le \frac1{m_c}\,\mathbb E K_c((R-a)/\rho)\\
&\le \frac{\rho}{c m_c}
 \int_{|t|\le c/\rho}
 \left(1-\frac{\rho|t|}{c}\right)|\phi_R(t)|\,dt\\
&\le C(c)(\rho/L)^{1/4},
\end{aligned}
\tag{1.4}
\]

where the integral is exact:

\[
2\int_0^1(1-u)u^{-1/4}\,du=\frac{32}{21},
\]

and therefore

\[
C(c)=\frac{32}{21}(4\pi e)^{1/4}c^{-1/4}m_c^{-1}.
\tag{1.5}
\]

Take the rational value `c=6/5`. The alternating sine series gives

\[
\sin(3/5)\ge \frac35-\frac{(3/5)^3}{6}=\frac{141}{250},
\]

hence

\[
m_{6/5}\ge(47/50)^2=2209/2500.
\tag{1.6}
\]

Using the elementary bounds `pi<22/7` and `e<11/4`, fourth powers give the completely rational certification

\[
\left[
\frac{32}{21}\left(\frac56\right)^{1/4}
(4\pi e)^{1/4}\frac{2500}{2209}
\right]^4
<254.822<256=4^4.
\tag{1.7}
\]

For reference, the exact rational upper bound before the decimal in (1.7) is

\[
\left(\frac{32}{21}\right)^4\frac56\cdot4\frac{22}{7}\frac{11}{4}
\left(\frac{2500}{2209}\right)^4,
\]

and `256` minus this rational number equals

\[
\frac{114611114645699036416}{97247699666584761861}>0.
\]

The bound `e<11/4` follows from the exponential series by bounding the tail from `1/4!` by a geometric series of ratio `1/5`; `pi<22/7` is the standard elementary Archimedean inequality (equivalently obtainable from the usual positive rational integral proof).

Thus (1.3) implies the sharper universal small-ball estimate

\[
\boxed{\mathbb P\{|R-a|<\rho\}\le\min\{1,4(\rho/L)^{1/4}\}.}
\tag{1.8}
\]

In the other branch of manuscript Lemma `lem:quarter`, where some diagonal coefficient has modulus at least `L/2`, the manuscript already gives `4 sqrt(rho/L)`, which is at most `4(rho/L)^{1/4}` for `rho<=L`. Therefore (1.8) replaces the manuscript constant `16` by `4` in the **full** lemma, with no new hypothesis.

For `L>=1`, layer cake now gives

\[
\boxed{
\sup_a\mathbb E\log_+\frac1{|R-a|}
\le L_0^{\rm F}:=4+4\log4=4+8\log2.
}
\tag{1.9}
\]

Numerically `L_0^F=9.545177444479563...`, versus the manuscript's `4+4 log16=15.090354...`.

## 2. Keep the exact hyperbolic constant instead of rounding it to six

In the proof of manuscript Lemma `lem:hyperbola`, before the displayed rounding, each hyperbola branch is already shown to have integral at most

\[
\frac{15}{2}\log2+\log_+\frac{32}{\delta\Lambda}.
\]

The two branches are averaged by the prefactor `1/(2 sqrt D)`, and `Lambda>=2/sqrt D`. Hence the proof itself yields the sharper envelope

\[
\boxed{
 p_{q(W)}(z)
\le D^{-1/2}
\left(\frac{15}{2}\log2+
\log_+\frac{16\sqrt D}{|z-v|}\right)
}
\tag{2.1}
\]

for almost every `z!=v`. This is only removal of a safe rounding; all rough-law and exceptional-slice handling is exactly the manuscript's.

## 3. Sharpened pivot half-potential

Retain `eta=1/100`.

### Scalar pivot

The manuscript singular-kernel estimate is

\[
J(d)\le8+3\log_+(1/|d|).
\]

Combining it with (1.9) gives

\[
\boxed{
H(Q)\le \eta^{-1/2}(8+3L_0^F)
=200+120\log4
=366.3553233343868\ldots .
}
\tag{3.1}
\]

The full half-potential therefore obeys

\[
\boxed{
\sup_a\mathbb E|Q-a|^{-1/2}
\le201+120\log4
=367.3553233343868\ldots .
}
\tag{3.2}
\]

### Definite pair

The manuscript bound is unchanged:

\[
H(Q)\le4\pi\eta^{-1/2}=40\pi<126.
\tag{3.3}
\]

### Indefinite pair

Using (2.1), the manuscript log-kernel integral, and `D>=1/100`,

\[
H(Q)\le D^{-1/2}
\left(8+30\log2+4\log(16\sqrt D)\right).
\tag{3.4}
\]

Writing `y=sqrt D>=1/10`, the right side is

\[
y^{-1}(8+30\log2+4\log16+4\log y).
\]

Its derivative is `y^{-2}(4-C-4 log y)` with `C=8+30 log2+4 log16`; this is already negative at `y=1/10` and remains negative thereafter. Hence the maximum occurs at `D=1/100`, giving

\[
H(Q)\le10\left(8+30\log2+4\log(8/5)\right)
=306.744299337813\ldots .
\tag{3.5}
\]

Thus the scalar branch is the largest and the manuscript proposition `prop:pivot-H` may be sharpened from `600` to

\[
\boxed{H(Q)\le200+120\log4<367.}
\tag{3.6}
\]

## 4. Consequence for the pinned seventeen-direction theorem

In the normalized main proof, a scalar pivot leaves at least sixteen unit-scale Schur directions and therefore may use the sharpened nine-direction full half-potential (3.2). The outer square-profile factor is `eta^{-1/2}=10`, so

\[
\|p_Q\|_\infty
\le 10(201+120\log4)
=2010+1200\log4
=3673.5532333438687\ldots .
\tag{4.1}
\]

The no-pivot branch remains `<2400`, the definite-pair branch `<32`, and the sharpened indefinite-pair density bound is below `153`. Consequently the **same pinned seventeen-direction proof**, with only the two justified constant replacements above, yields

\[
\boxed{
 s_{17}(A)\ge s>0
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_\infty
 <3674\,K^2/s.
}
\tag{4.2}
\]

No theorem hypothesis changes.

## 5. Consequence for the complete nine-direction replacement candidate

The prior complete account02/B10 replacement proof at

`improvements/account02/B10/20260924T131229Z-account02-B10-fixedmult-r11/NINE_THRESHOLD_REPLACEMENT.md`

has four normalized terminal branches. Its no-pivot `E_3` receiver remains

\[
\|p_Q\|_\infty\le2370.935.
\]

At a scalar pivot the Schur remainder has at least eight unit-scale singular values. If that remainder has a pivot, use (3.2); if it has no pivot, the replacement proof's `E_2` half-potential is `<153`. Therefore the scalar-pivot branch is again (4.1). The definite and indefinite pair branches are smaller. Hence the complete nine-direction replacement, with this constant patch, gives

\[
\boxed{
 s_9(A)\ge s>0
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_\infty
 <3674\,K^2/s.
}
\tag{5.1}
\]

This is a constant sharpening of an already-written complete replacement proof; it is not a new claim that multiplicity below nine has been closed.

## 6. Adversarial interface checks and remaining threshold debt

The exact finite rank witness in this run's audit simultaneously attains the manuscript completion bounds `rank R=3r` and `rank R_LL=r` at `r=2`; the baseline rank constants therefore cannot be cosmetically lowered.

The fresh account03/B10 structural result proves that, under normalized no-pivot `s_7>=1`, either `V_3>=kappa^3` or a dimension-free **invertible-seed overlap-one** packet is large. I checked its corrected use of nonsingular seeds: the exact determinant-weighted identity holds for `W^times_{2,1}`, while using the unrestricted overlap volume as an equality would be false because singular seeds can have nonsingular bordered extensions.

A second adversarial point is fragmentation: an aggregate overlap-one lower bound cannot in general be replaced by a lower bound on one bordered minor. Fix an invertible `2x2` seed `B=beta I` and take `m` independent anchor coordinates with zero seed-anchor couplings and diagonal residuals `D_h=m^{-1/2}`. Then

\[
\sum_h \det\begin{pmatrix}B&0\\0&D_h\end{pmatrix}^2
=\det(B)^2,
\]

while every individual bordered determinant has modulus `|det B|/sqrt(m)->0`. Thus any seven/eight-direction closure must consume the **aggregate packet**, not select a single large local minor. This is a counterexample to that proof interface, not to a density theorem.

The first unpaid implication remains a product-preserving overlap-one analytic receiver that retains the common original-coordinate anchor through the averaging. Until that is proved, multiplicities seven and eight remain **UNPROVED**, and unrestricted three-eigenvalue QFORM remains **OPEN**.

## Dependency map

Pinned manuscript dependencies retained unchanged:

`Fourier inversion + determinant theorem -> quarter-power Fourier envelope`;
`scalar square profile + Schur count + singular kernels -> scalar pivot`;
`hyperbolic change of variables + log kernel -> indefinite pair`;
`sampled interpolation + restricted rank + random cut -> no-pivot volume bounds`.

New constant-only replacements:

`Fejer kernel (1.1) + existing |t|^{-1/4} envelope -> coefficient 4 small-ball -> L0^F`;
`unrounded hyperbola branch integral -> (2.1)`;
`L0^F + existing pivot arguments -> (3.6)`;
`(3.2) + existing main assembly -> 3674`.

For threshold nine, append the already-complete replacement dependencies:

`grouped product-Fourier compiler + E3 density receiver + E2 half-potential receiver -> nine-direction assembly`.

No post-rotation independence, moment/support/log-concavity hypothesis, bounded-support reduction, or continuity claim is introduced.