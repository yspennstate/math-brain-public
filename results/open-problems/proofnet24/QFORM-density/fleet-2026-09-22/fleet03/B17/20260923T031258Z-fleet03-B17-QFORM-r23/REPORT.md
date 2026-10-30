# QFORM B17: one-heavy majority-sign Gaussian-completion ceiling

Run: `20260923T031258Z-fleet03-B17-QFORM-r23`  
Account/slot: `fleet03/B17`  
Status: `NEW_SUPPORTING_THEOREM`; full QFORM remains `OPEN / NOT PROVED`; full-target continuity remains open; `WITHOUT_VERIFIED_BRAIN`.

## 1. Result and scope

The exact owner target is the unrestricted quadratic-form bounded-density conjecture for independent real inputs with densities bounded by one and a real symmetric matrix having at least three eigenvalues of magnitude at least one. This report does **not** solve that full problem. It closes the complementary one-heavy **majority-sign** witness architecture that remained open after the previous B17 minority-sign and two-heavy analyses.

Let `X` be any real random variable with probability density `0<=f<=1`; no moment, centering, connected-support, compact-support, or regularity assumption is imposed. Let `G_+,G_-` be independent of `X` and of one another, with

\[
G_+,G_-\sim N(0,\sigma^2),\qquad \sigma^2=1/12.
\]

Put

\[
Q_\infty=X^2+G_+^2-G_-^2.
\]

Then `Q_infty` has a bounded continuous density and

\[
\boxed{
\|p_{Q_\infty}\|_\infty
\le C_{\rm maj}
:=\frac{29}{25}\frac{\Gamma(1/4)^2\sqrt3}{2\pi}
=4.2034017268746133719\ldots
<3\sqrt2.
}
\tag{1.1}
\]

The same mechanism lifts uniformly to the exact finite target family

\[
A_m=\operatorname{diag}(1,P_m,-P_m),\qquad
P_m=J_m/m,
\tag{1.2}
\]

with one arbitrary cap-one heavy coordinate and two independent centered-uniform banks. Every `A_m` has exact nonzero spectrum `{1,1,-1}`. If the heavy law is allowed to depend arbitrarily on `m`, then nevertheless

\[
\boxed{
\limsup_{m\to\infty}
\sup_{0\le f_m\le1,\ \int f_m=1}
\|p_{Q_m}\|_\infty
\le C_{\rm maj}<3\sqrt2.
}
\tag{1.3}
\]

Thus this mixed-leverage family cannot realize the sharp obstruction supplied by the completed `fleet04/B17` all-diffuse rotated witness.

## 2. Difference-of-Gaussian-squares kernel

Let

\[
R=G_+^2-G_-^2.
\]

Its characteristic function is

\[
\phi_R(t)
=(1-2i\sigma^2t)^{-1/2}(1+2i\sigma^2t)^{-1/2}
=(1+4\sigma^4t^2)^{-1/2}.
\]

Fourier inversion gives the classical `K_0` density

\[
\boxed{
h_\sigma(r)=\frac1{2\pi\sigma^2}
K_0\!\left(\frac{|r|}{2\sigma^2}\right).
}
\tag{2.1}
\]

Equivalently, using

\[
K_0(y)=\int_0^\infty e^{-y\cosh u}\,du,
\tag{2.2}
\]

we obtain, after conditioning on `X=x`,

\[
p_{Q_\infty}(s)=\int_{\mathbb R}f(x)h_\sigma(s-x^2)\,dx
\le I_\sigma(s),
\tag{2.3}
\]

where

\[
I_\sigma(s):=\int_{\mathbb R}h_\sigma(s-x^2)\,dx.
\]

Therefore it is enough to bound `I_sigma` uniformly in the output level `s`. Notice that this step uses only `f<=1`; arbitrary fragmentation and translation of the heavy law are retained.

## 3. Uniform exponential-kernel lemma

For `beta>0` define

\[
J_\beta(s)=\int_{\mathbb R}e^{-\beta|s-x^2|}\,dx.
\]

### Lemma 3.1
For every `beta>0` and every real `s`,

\[
\boxed{J_\beta(s)\le\frac{29}{25}J_\beta(0)
=\frac{29}{25}\sqrt{\frac\pi\beta}.}
\tag{3.1}
\]

#### Proof for `s<=0`
Here `|s-x^2|=|s|+x^2`, so

\[
J_\beta(s)=e^{-\beta|s|}\sqrt{\pi/\beta}\le J_\beta(0).
\]

#### Reduction for `s>0`
Put `z=sqrt(beta s)` and scale `y=sqrt(beta)x`. Then

\[
\frac{J_\beta(s)}{J_\beta(0)}
=\frac2{\sqrt\pi}H(z),
\tag{3.2}
\]

where

\[
H(z)=D(z)+R(z),
\]

\[
D(z)=e^{-z^2}\int_0^z e^{t^2}\,dt,
\qquad
R(z)=e^{z^2}\int_z^\infty e^{-t^2}\,dt.
\tag{3.3}
\]

It therefore suffices to prove

\[
H(z)\le \frac{29\sqrt\pi}{50}.
\tag{3.4}
\]

#### Small range `0<=z<=2/5`
Trivially `D(z)<=z`. Also

\[
R'(z)=2zR(z)-1.
\]

The Mills estimate

\[
R(z)\le\frac1{2z}\qquad(z>0)
\]

follows from `t>=z` in

\[
\int_z^\infty e^{-t^2}dt
\le z^{-1}\int_z^\infty t e^{-t^2}dt.
\]

Hence `R` is decreasing and `R(z)<=R(0)=sqrt(pi)/2`. Integrating

\[
R'(u)\le 2uR(0)-1
\]

from zero to `z` gives

\[
R(z)\le R(0)-z+R(0)z^2.
\]

Thus

\[
H(z)\le R(0)(1+z^2)
\le \frac{\sqrt\pi}{2}\left(1+\frac4{25}\right)
=\frac{29\sqrt\pi}{50}.
\tag{3.5}
\]

#### Middle range `2/5<=z<=1`
The Dawson series is

\[
D(z)=z-\frac23z^3+\frac4{15}z^5-\frac8{105}z^7+\cdots .
\]

For `z<=1`, successive absolute terms have ratio at most `2/3`, so alternating-series truncation gives

\[
D(z)\le P_5(z):=z-\frac23z^3+\frac4{15}z^5.
\tag{3.6}
\]

For `R`, set

\[
c=4/\pi,
\qquad
r_c(z)=\frac1{z+\sqrt{z^2+c}}.
\]

A direct differentiation shows that the sign of

\[
r_c'(z)-2zr_c(z)+1
\]

is the sign of

\[
(c-1)\sqrt{z^2+c}-z.
\]

Using `pi>157/50`, hence `c<200/157`, one checks exactly at `z=2/5` that

\[
\left(\frac{200}{157}-1\right)^2
\left(\frac4{25}+\frac{200}{157}\right)
=\frac{10406172}{96747325}
<\frac4{25}.
\tag{3.7}
\]

The required sign is therefore nonpositive for every `z>=2/5`. If `e=r_c-R`, then

\[
(e e^{-z^2})'
=(r_c'-2zr_c+1)e^{-z^2}\le0.
\]

Since `e(T)e^{-T^2}->0` as `T->infinity`, integration backward gives

\[
R(z)\le r_c(z),\qquad z\ge2/5.
\tag{3.8}
\]

Also `pi<22/7` implies `c>14/11`, so

\[
R(z)\le\frac1{z+\sqrt{z^2+14/11}}.
\tag{3.9}
\]

The remaining interval is a finite exact-rational check, included in `verify_majority_heavy.py`. Split `[2/5,1]` into the 24 intervals

\[
[a_k,b_k],\quad a_k=\frac25+\frac{k}{40},\quad b_k=a_k+\frac1{40}.
\]

Because `P_5` is increasing and the right side of (3.9) is decreasing,

\[
H(z)\le
P_5(b_k)+\frac1{a_k+\sqrt{a_k^2+14/11}}.
\]

Every one of the 24 inequalities

\[
P_5(b_k)+\frac1{a_k+\sqrt{a_k^2+14/11}}
<\frac{1021}{1000}
\tag{3.10}
\]

is certified using rational arithmetic only: if
`q_k=1021/1000-P_5(b_k)`, (3.10) is reduced to

\[
a_k^2+\frac{14}{11}>(q_k^{-1}-a_k)^2.
\]

The largest diagnostic upper endpoint value occurs for `k=8` and is
`1.0202140316...`; the proof itself uses the exact rational inequalities. Finally,

\[
\left(\frac{1021}{1000}\right)^2
<\left(\frac{29}{50}\right)^2\frac{157}{50}
<\left(\frac{29\sqrt\pi}{50}\right)^2,
\]

so (3.4) follows on the middle range.

#### Large range `z>=1`
The ODE `D'=1-2zD` admits the supersolution

\[
b(z)=\frac{z}{1+2z^2/3}.
\]

Indeed

\[
b'(z)-1+2zb(z)
=\frac{8z^4/9}{(1+2z^2/3)^2}\ge0,
\]

and `b(0)=D(0)=0`, so `D(z)<=b(z)`.

For `1<=z<=3/2`, `b(z)<=sqrt(6)/4<613/1000`, while (3.9) gives `R(z)<2/5`; hence `H(z)<1.013`. For `z>=3/2`, `b(z)<=3/5` and (3.9) gives `R(z)<3/10`, so `H(z)<0.9`. Both are below `29sqrt(pi)/50`. This proves Lemma 3.1. `square`

## 4. Gaussian-completion ceiling

By (2.2), Tonelli, and Lemma 3.1, with

\[
a=(2\sigma^2)^{-1},\qquad \beta=a\cosh u,
\]

we have

\[
I_\sigma(s)
=\frac1{2\pi\sigma^2}
\int_0^\infty J_{a\cosh u}(s)\,du
\le\frac{29}{25}I_\sigma(0).
\tag{4.1}
\]

The zero-level integral is exact. Using

\[
\int_0^\infty y^{\mu-1}K_0(y)\,dy
=2^{\mu-2}\Gamma(\mu/2)^2,
\qquad \mu=1/2,
\]

one obtains

\[
I_\sigma(0)
=\frac{\Gamma(1/4)^2}{4\pi\sigma}.
\tag{4.2}
\]

For `sigma^2=1/12`,

\[
I_\sigma(0)=\frac{\Gamma(1/4)^2\sqrt3}{2\pi},
\]

which proves the stated bound (1.1).

### 4.1 Rigorous strict comparison with `3sqrt(2)`

No floating-point inequality is needed. The standard Stirling upper bound

\[
\Gamma(x+1)
<\sqrt{2\pi}\,x^{x+1/2}
 e^{-x+1/(12x)}
\]

at `x=5/4`, together with
`Gamma(1/4)=(16/5)Gamma(9/4)`, gives

\[
\Gamma(1/4)^2
<\frac{512\pi}{25}
\left(\frac54\right)^{7/2}e^{-71/30}.
\tag{4.3}
\]

Substitution into `C_maj<3sqrt(2)` reduces, after cancellation and squaring, to

\[
e^{71/15}>\frac{1682}{15}.
\tag{4.4}
\]

The degree-10 positive Taylor lower sum already satisfies

\[
\sum_{k=0}^{10}\frac{(71/15)^k}{k!}
=\frac{235615443445788176101}{2092548937500000000}
>\frac{1682}{15}.
\]

Hence the strict comparison is fully certified. Numerically only for orientation,

\[
C_{\rm maj}=4.203401726874613\ldots,
\qquad
3\sqrt2-C_{\rm maj}=0.039238960244672\ldots .
\]

## 5. Continuity in the Gaussian-completion theorem

Let `g` be the density of `X^2`. For `q>0`,

\[
g(q)=\frac{f(\sqrt q)+f(-\sqrt q)}{2\sqrt q}
\le q^{-1/2}.
\tag{5.1}
\]

It has mass one. Therefore

\[
\int_0^\infty g(q)^{3/2}dq
\le\int_0^1q^{-3/4}dq+\int_1^\infty g(q)dq
\le5.
\tag{5.2}
\]

Thus `g in L^{3/2}`. The kernel `h_sigma` belongs to `L^3(R)` because `K_0` has only a logarithmic singularity at zero and decays exponentially at infinity. Since

\[
p_{Q_\infty}=g*h_\sigma,
\]

Holder gives boundedness and translation continuity in `L^3` gives

\[
|p(s+t)-p(s)|
\le\|g\|_{3/2}\|\tau_t h_\sigma-h_\sigma\|_3\to0.
\]

So continuity is proved for this theorem's scope. This is **not** a proof of full-target continuity.

## 6. Exact finite source-valid family and uniform local-limit transfer

Let `X_m` have an arbitrary probability density `f_m<=1`; it may depend on `m`. Independently let

\[
U_{m1},\dots,U_{mm},V_{m1},\dots,V_{mm}
\stackrel{\rm iid}{\sim}\operatorname{Unif}[-1/2,1/2],
\]

and set

\[
S_m=m^{-1/2}\sum_{j=1}^mU_{mj},
\qquad
T_m=m^{-1/2}\sum_{j=1}^mV_{mj}.
\]

With `P_m=J_m/m`, define the `(2m+1)x(2m+1)` physical matrix

\[
A_m=\operatorname{diag}(1,P_m,-P_m).
\]

Its exact nonzero spectrum is `{1,1,-1}`, and

\[
Q_m=X_m^2+S_m^2-T_m^2.
\tag{6.1}
\]

Thus every finite member satisfies the owner's exact spectral and product-input hypotheses. The two bank blocks are nonseparable in the original independent coordinates.

Let `rho_m` be the density of `S_m` and `gamma` the `N(0,1/12)` density. The local-CLT Fourier argument already proved in B17 run `r22` applies verbatim:

\[
\|\rho_m-\gamma\|_\infty\to0.
\tag{6.2}
\]

Since both sides are probability densities, pointwise convergence plus Scheffe gives

\[
\|\rho_m-\gamma\|_1\to0.
\tag{6.3}
\]

Let `a_m` and `a` be the densities of `S_m^2` and `G^2`, extended by zero to the negative line. By symmetry,

\[
a_m(q)=\rho_m(\sqrt q)q^{-1/2},
\qquad
 a(q)=\gamma(\sqrt q)q^{-1/2},
\quad q>0.
\]

Writing `delta_m=||rho_m-gamma||_infinity`, the change of variables `q=x^2` gives

\[
\begin{aligned}
\|a_m-a\|_{3/2}^{3/2}
&=2\int_0^\infty
|\rho_m(x)-\gamma(x)|^{3/2}x^{-1/2}\,dx\\
&\le4\delta_m^{3/2}
+2\delta_m^{1/2}\|\rho_m-\gamma\|_1
\longrightarrow0.
\end{aligned}
\tag{6.4}
\]

The difference-of-squares densities are

\[
h_m=a_m*\widetilde a_m,
\qquad h=a*\widetilde a,
\]

where `tilde a(x)=a(-x)`. Young's inequality with exponents `3/2,3/2,3` yields

\[
\|h_m-h\|_3
\le
(\|a_m\|_{3/2}+\|a\|_{3/2})
\|a_m-a\|_{3/2}
\longrightarrow0.
\tag{6.5}
\]

For the arbitrary heavy law, its square density `g_m` satisfies the uniform estimate from (5.2),

\[
\|g_m\|_{3/2}\le5^{2/3}.
\tag{6.6}
\]

Therefore, uniformly over **all** `m`-dependent cap-one heavy laws,

\[
\|g_m*h_m-g_m*h\|_\infty
\le5^{2/3}\|h_m-h\|_3\to0.
\tag{6.7}
\]

Combining (6.7) with the Gaussian-completion theorem proves (1.3). This is a genuine local-density transfer, not a weak-convergence argument.

For each finite `m`, `a_m in L^{3/2}`, hence `h_m in L^3`; (6.6) and translation continuity in `L^3` also show that `Q_m` has a bounded continuous density. Again, this continuity conclusion is only for the displayed family.

## 7. Application of the designated partner result

Completed `fleet04/B17` proves, for an exact fully rotated three-bank cap-one uniform family with nonzero spectrum `{1,1,-1}`,

\[
p_{Q_m^{\rm partner}}(0)
=3\sqrt2\left(1-\frac{5295}{21952m}+O(m^{-2})\right).
\tag{7.1}
\]

Source: `yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.

Hence every universal constant must satisfy

\[
C_*\ge3\sqrt2.
\tag{7.2}
\]

Applying (7.2) to the actual inequality proved here gives the strict architecture separation

\[
\boxed{
\limsup_m\sup_{f_m\le1}
\|p_{X_m^2+S_m^2-T_m^2}\|_\infty
\le C_{\rm maj}
<3\sqrt2
\le C_*.
}
\tag{7.3}
\]

Thus the sharp obstruction cannot be produced by keeping one physical **majority-sign** coordinate fully localized while Gaussianizing one same-sign and one opposite-sign direction through independent minimum-variance uniform banks. Together with the earlier B17 minority-sign theorem, both one-heavy sign placements in the basic three-mode mixed-leverage architecture are now separated from the all-diffuse `3sqrt(2)` obstruction.

## 8. What this does not prove; next mechanism

The full unrestricted conjecture is still open. This report does not control arbitrary finite-leverage matrices, several heavy coordinates, arbitrary extra spectrum, or multiscale fragmented shared-coordinate constructions. It also does not assert that `3sqrt(2)` is the optimal universal constant.

A nonredundant sharp-witness attack now has to leave the single-heavy/two-diffuse completion architecture. The next natural candidate is a **mesoscopic shared row or several non-collinear heavy rows coupled simultaneously to two diffuse banks**, where the limiting residual is no longer a one-dimensional cap-one square convolved with a fixed Gaussian difference kernel. A genuinely multiscale compound-Poisson/fragmented three-bank limit is another remaining route.

No Monte Carlo or histogram inference is used. The finite constant comparisons are exact rational certificates; decimal values are diagnostics only.
