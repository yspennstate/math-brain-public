# QFORM B17: two-heavy/shared-bank Gaussian-completion no-escape theorem

Run: `20260923T021034Z-account03-B17-QFORM-r22`  
Account/slot: `account03/B17`  
Status: `NEW_SUPPORTING_THEOREM`; full QFORM remains `OPEN / NOT PROVED`; full-target continuity remains open; `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope

The owner target is the unrestricted statement: for independent real inputs with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of magnitude at least one, prove a universal essential density bound for the quadratic form (and separately, if possible, continuity), or produce a valid counterexample.

This report does **not** solve that full target. It rules out a new sharp-witness mechanism: two arbitrary macroscopic cap-one coordinates coupled to one diffuse uniform bank through a genuinely nonseparable rank-three form. The result is uniform over the two heavy laws, even when they depend on the bank size and have arbitrary disconnected, translated, or fragmented supports.

The argument does not use post-rotation independence, pointwise van-der-Corput decay, arbitrary-joint quadratic coarea, conditional density moments, a bounded fragment count, or a single-minor reciprocal estimate.

## 2. Gaussian-completion theorem for an arbitrary cap-one heavy pair

Let `(U,V)` have an arbitrary joint probability density `rho` on `R^2` satisfying

\[
0\le \rho(u,v)\le 1,\qquad \iint\rho=1.
\]

Let `G` be independent of `(U,V)` with

\[
G\sim N(0,\sigma^2),\qquad \sigma^2=\frac1{12}.
\]

Define

\[
Q_\infty=V^2-2UG.
\]

Then `Q_infty` has a bounded continuous density, and

\[
\boxed{
\|p_{Q_\infty}\|_\infty\le C_\times
:=2^{13/6}\sqrt{\frac3\pi}\,\Gamma(5/4)^{2/3}
=4.109270566451296\ldots<3\sqrt2.
}
\tag{2.1}
\]

The theorem permits **every** joint density `rho<=1`; therefore it applies a fortiori to the heavy pair obtained from two independent cap-one physical coordinates after an orthogonal two-dimensional change of variables.

### 2.1 Conditional kernel

For fixed `(u,v)` with `u!=0`, the conditional law of `V^2-2uG` has density at `s`

\[
K_s(u,v)=\frac{c}{|u|}\exp\!\left[-a\frac{(v^2-s)^2}{u^2}\right],
\qquad
c=\sqrt{\frac3{2\pi}},\qquad a=\frac32.
\tag{2.2}
\]

The set `u=0` is Lebesgue-null, and Tonelli gives

\[
p_{Q_\infty}(s)=\iint \rho(u,v)K_s(u,v)\,du\,dv.
\tag{2.3}
\]

The pointwise singular factor `1/|u|` cannot be bounded uniformly, so the relevant object is the **two-dimensional distribution function of the kernel**.

### 2.2 Exact level-set geometry

For `delta>0` define

\[
L_s(\delta)=\big|\{v\in\mathbb R:|v^2-s|<\delta\}\big|.
\]

For every real `s` and every `delta>0`,

\[
\boxed{L_s(\delta)\le2\sqrt{2\delta}.}
\tag{2.4}
\]

Proof. If `s<0`, the set is empty when `delta<=-s`, and otherwise its length is `2sqrt(delta+s)<=2sqrt(delta)`. If `s>=0` and `delta>=s`, its length is `2sqrt(s+delta)<=2sqrt(2delta)`. Finally, if `s>=0` and `delta<s`, its length is

\[
2\big(\sqrt{s+\delta}-\sqrt{s-\delta}\big).
\]

The square of the bracket is

\[
2s-2\sqrt{s^2-\delta^2}
=\frac{2\delta^2}{s+\sqrt{s^2-\delta^2}}
\le2\delta,
\]

which again gives (2.4). `square`

Fix `lambda>0`. If `K_s(u,v)>lambda`, put `w=|u|`. Then necessarily

\[
0<w<\frac c\lambda,
\]

and

\[
|v^2-s|<\delta(w)
:=w a^{-1/2}\left[\log\frac{c}{\lambda w}\right]^{1/2}.
\]

Using both signs of `u` and (2.4),

\[
\begin{aligned}
\mu_s(\lambda)
&:=\big|\{(u,v):K_s(u,v)>\lambda\}\big|\\
&\le4\sqrt2\,a^{-1/4}
\int_0^{c/\lambda}w^{1/2}
\left[\log\frac{c}{\lambda w}\right]^{1/4}dw\\
&=D\lambda^{-3/2},
\end{aligned}
\tag{2.5}
\]

where

\[
\int_0^1x^{1/2}(-\log x)^{1/4}dx
=\frac{\Gamma(5/4)}{(3/2)^{5/4}}
\]

and therefore

\[
\boxed{
D=\frac{2^{13/4}\Gamma(5/4)}{(3\pi)^{3/4}}.
}
\tag{2.6}
\]

Thus `K_s` has a translation-uniform weak-`L^{3/2}` bound in the **original two-dimensional heavy plane**. This is precisely the aggregation that the invalid one-dimensional fiber-supremum mechanisms miss.

### 2.3 Bathtub/layer-cake closure

Since `rho<=1` and has mass one,

\[
\begin{aligned}
p_{Q_\infty}(s)
&=\int_0^\infty\iint\rho(u,v)1_{\{K_s>\lambda\}}\,du\,dv\,d\lambda\\
&\le\int_0^\infty\min\{1,\mu_s(\lambda)\}\,d\lambda\\
&\le\int_0^\infty\min\{1,D\lambda^{-3/2}\}\,d\lambda.
\end{aligned}
\]

At `lambda_0=D^{2/3}`, the two terms meet, and hence

\[
\int_0^\infty\min\{1,D\lambda^{-3/2}\}\,d\lambda
=D^{2/3}+2D D^{-1/3}=3D^{2/3}.
\]

Substituting (2.6) gives exactly (2.1).

### 2.4 Analytic strict comparison with `3 sqrt(2)`

Log-convexity of the Gamma function at the midpoint `5/4` between `1` and `3/2` yields

\[
\Gamma(5/4)^2<\Gamma(1)\Gamma(3/2)=\frac{\sqrt\pi}{2}.
\]

Therefore

\[
C_\times
<2^{11/6}\sqrt3\,\pi^{-1/3}
=4.214366766119976\ldots.
\]

The latter is strictly smaller than `3sqrt(2)` because its cube comparison reduces to

\[
16<3\sqrt3\,\pi,
\]

which follows already from `pi>3.14`. Thus the strict inequality in (2.1) is analytic, not a numerical inference.

### 2.5 Continuity in the Gaussian-completion theorem

For later use, a general one-dimensional estimate is convenient. Let `h` be a probability density with `||h||_infty<=M` and define

\[
T_{h,s}(u,v)=\frac1{2|u|}h\!\left(\frac{v^2-s}{2u}\right).
\]

For every fixed `u!=0`,

\[
\boxed{
\int_\mathbb R T_{h,s}(u,v)\,dv
\le\sqrt{\frac{2M}{|u|}},
}
\tag{2.7}
\]

uniformly in `s`. For `u>0`, the change of variables `z=(v^2-s)/(2u)` gives

\[
(2u)^{-1/2}\int_a^\infty h(z)(z-a)^{-1/2}dz,
\quad a=-s/(2u).
\]

Among all `0<=h<=M` of mass one, bathtub maximization places `h=M` on `[a,a+1/M]`; the integral is then `2sqrt(M)`. This proves (2.7), and `u<0` is identical after reflection.

Consequently, uniformly in `s`,

\[
\iint_{|u|<\varepsilon}\rho(u,v)T_{h,s}(u,v)\,du\,dv
\le4\sqrt{2M\varepsilon}.
\tag{2.8}
\]

For Gaussian `h`, on `|u|>=epsilon` the kernel is continuous in `s` and dominated by an integrable multiple of `rho`; (2.8) handles the small-`u` strip. Letting `epsilon` tend to zero proves continuity of `p_{Q_infty}`. This continuity statement is only for this theorem's scope.

## 3. Exact finite-dimensional target family

For every integer `m>=1`, let `X_{1,m},X_{2,m}` be independent random variables with arbitrary probability densities `f_m,g_m<=1`; these laws may depend on `m`. Let

\[
W_{m1},\ldots,W_{mm}\stackrel{\rm iid}{\sim}\mathrm{Unif}[-1/2,1/2]
\]

be independent of the heavy pair, and put

\[
S_m=\frac1{\sqrt m}\sum_{k=1}^mW_{mk}.
\]

Let `R_m` be the `(m+2) x 3` matrix whose columns are the first two physical coordinate vectors and the unit bank vector

\[
b_m=(0,0,m^{-1/2},\ldots,m^{-1/2})^T.
\]

Thus `R_m^T R_m=I_3`. Define

\[
B=\begin{pmatrix}
1/2&-1/2&-1/\sqrt2\\
-1/2&1/2&-1/\sqrt2\\
-1/\sqrt2&-1/\sqrt2&0
\end{pmatrix}.
\tag{3.1}
\]

If

\[
u=(1/2,1/2,1/\sqrt2)^T,
\]

then `||u||=1` and `B=I-2uu^T`. Hence `B^2=I` and its spectrum is exactly `{1,1,-1}`. Set

\[
\boxed{A_m=R_mBR_m^T.}
\tag{3.2}
\]

Because `R_m` is an isometry onto its three-dimensional range, the nonzero spectrum of every finite `A_m` is exactly

\[
\boxed{\{1,1,-1\}.}
\tag{3.3}
\]

This is not diagonal in the independent coordinates: each of the two singleton coordinates couples to every bank coordinate with coefficient `-1/sqrt(2m)`, and the two singleton coordinates also couple to each other.

The associated quadratic form is

\[
Q_m=\frac12(X_{1,m}-X_{2,m})^2
-\sqrt2\,S_m(X_{1,m}+X_{2,m}).
\]

Define the orthogonal heavy-plane coordinates

\[
U_m=\frac{X_{1,m}+X_{2,m}}{\sqrt2},\qquad
V_m=\frac{X_{1,m}-X_{2,m}}{\sqrt2}.
\]

Then

\[
\boxed{Q_m=V_m^2-2U_mS_m.}
\tag{3.4}
\]

The orthogonal map has absolute Jacobian one, so `(U_m,V_m)` has joint density

\[
\rho_m(u,v)=
 f_m\!\left(\frac{u+v}{\sqrt2}\right)
 g_m\!\left(\frac{u-v}{\sqrt2}\right),
\]

and therefore

\[
0\le\rho_m\le1,\qquad\iint\rho_m=1.
\tag{3.5}
\]

No independence of `U_m,V_m` is asserted or used.

## 4. Uniform local-limit transfer: no hidden finite-width spike survives

Weak convergence `S_m=>G` alone is insufficient for a density-peak conclusion. Here a direct uniform transfer estimate closes that gap, **uniformly over the arbitrary `m`-dependent heavy laws**.

Let `h,h'` be probability densities on `R` with

\[
\|h\|_\infty,\|h'\|_\infty\le M,
\qquad
\delta=\|h-h'\|_\infty.
\]

For a joint density `rho<=1` of mass one define

\[
P_h(s)=\iint\rho(u,v)\frac1{2|u|}
 h\!\left(\frac{v^2-s}{2u}\right)du\,dv.
\]

Then for every `epsilon>0`,

\[
\boxed{
\|P_h-P_{h'}\|_\infty
\le\frac{\delta}{2\varepsilon}
+8\sqrt{2M\varepsilon}.
}
\tag{4.1}
\]

Indeed, on `|u|>=epsilon`, the integrand difference is bounded by `delta/(2epsilon)` and `rho` has mass one. On `|u|<epsilon`, apply (2.7) separately to `h` and `h'`, use `rho<=1`, and integrate `|u|^{-1/2}`. In particular, setting `epsilon=delta^{2/3}` shows

\[
\|P_h-P_{h'}\|_\infty=O_M(\delta^{1/3})
\quad\text{as }\delta\downarrow0.
\tag{4.2}
\]

### 4.1 Uniform convergence of the normalized uniform-bank density

Let `g_m` be the density of `S_m`, and let `gamma_sigma` be the `N(0,1/12)` density. The characteristic function is

\[
\widehat g_m(t)=\operatorname{sinc}\!\left(\frac{t}{2\sqrt m}\right)^m.
\tag{4.3}
\]

Pointwise, it converges to `exp(-t^2/24)`. More importantly, for
`|t|<2pi sqrt(m)`, Euler's product for `sin x/x` and `log(1-y)<=-y` give

\[
|\widehat g_m(t)|\le e^{-t^2/24}.
\tag{4.4}
\]

For `|t|>=2pi sqrt(m)`, `|sinc x|<=1/|x|` yields, for `m>1`,

\[
\int_{|t|\ge2\pi\sqrt m}|\widehat g_m(t)|dt
\le\frac{4\sqrt m}{(m-1)\pi^{m-1}}.
\tag{4.5}
\]

Dominated convergence on the expanding interior, together with (4.5) and the Gaussian tail, gives

\[
\|\widehat g_m-e^{-t^2/24}\|_{L^1}\longrightarrow0.
\]

Fourier inversion therefore implies

\[
\boxed{
\delta_m:=\|g_m-\gamma_\sigma\|_\infty\longrightarrow0.
}
\tag{4.6}
\]

For all sufficiently large `m`, both sup norms are at most (say) `M=2`.

### 4.2 Uniform heavy-law conclusion

Let

\[
\widetilde Q_m=V_m^2-2U_mG,
\qquad G\sim N(0,1/12)
\]

with the same `(U_m,V_m)` and independent `G`. By (4.1)-(4.6),

\[
\sup_{f_m,g_m\le1}
\|p_{Q_m}-p_{\widetilde Q_m}\|_\infty\longrightarrow0,
\tag{4.7}
\]

where the supremum is over every choice of the two independent cap-one heavy input laws, including `m`-dependent choices.

The Gaussian-completion theorem (2.1), applied to `rho_m` from (3.5), now gives the source-valid asymptotic no-escape inequality

\[
\boxed{
\limsup_{m\to\infty}
\sup_{f_m,g_m\le1}\|p_{Q_m}\|_\infty
\le C_\times
=4.109270566451296\ldots
<3\sqrt2.
}
\tag{4.8}
\]

This is stronger than weak convergence: it precludes an `m`-dependent narrow density spike in this family.

For `m>=2`, the Irwin-Hall bank density `g_m` is bounded and continuous. Combining continuity on `|u|>=epsilon` with the uniform small-`u` estimate (2.8) proves that every `Q_m` in this family has a continuous density, even when the two heavy input densities are merely measurable. Full-target continuity is **not** claimed.

## 5. Designated partner result applied to an actual sharp inequality

The completed designated partner `account04/B17` result is:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

It constructs exact finite independent cap-one rotated forms with spectrum `{1,1,-1}` and proves

\[
p_{Q_m^{\rm partner}}(0)
=3\sqrt2\left(1-\frac{5295}{21952m}+O(m^{-2})\right),
\]

so the optimal universal QFORM constant, if finite, must satisfy

\[
C_*\ge3\sqrt2.
\tag{5.1}
\]

Combining (4.8) with this completed partner theorem gives the actual inequality

\[
\boxed{
\limsup_{m\to\infty}
\sup_{f_m,g_m\le1}\|p_{Q_m}\|_\infty
\le4.1092705664\ldots
<3\sqrt2
\le C_*.
}
\tag{5.2}
\]

Thus a genuinely rotated two-heavy-plus-one-diffuse-bank Gaussian-completion mechanism has a **strict asymptotic gap** from the known sharp obstruction. Any witness reaching or exceeding `3sqrt(2)` must use a mechanism not reducible to this architecture: for example a more diffuse three-bank geometry, several non-collinear mesoscopic rows, or genuinely multiscale/non-Gaussian aggregation.

This applies the designated partner's completed result quantitatively rather than merely citing it.

## 6. Numerical/exact arithmetic checks

The sibling checker verifies the reflection identity, the exact nonzero spectrum mechanism, and the constants. Executed arithmetic output for this run:

```text
Gamma(5/4) = 0.90640247705547727
D = 1.6031170166704007
C_cross = 4.109270566451297
3sqrt2 = 4.2426406871192857
gap = 0.1333701206679887
coarse_upper = 4.2143667661199764
coarse_gap = 0.028273920999309254
16 < 3sqrt3*pi: True
max |B^2-I| = 2.220446049250313e-16
```

These checks support arithmetic only; the theorem is established by the analytic proof above. No Monte Carlo histogram is used.

## 7. Remaining gap

The unrestricted QFORM theorem is still open. This run does not rule out finite/mesoscopic overshoot in unrelated geometries, two or more diffuse coupled banks with non-Gaussian fragmented sources, or arbitrary added spectrum. The next nonredundant B17 stress direction is therefore a **two-diffuse-bank plus one mesoscopic shared row** (or a genuinely multiscale fragmented three-bank frame), where the weak-`L^{3/2}` two-heavy-plane reduction no longer applies.

The desired continuous representative is proved only for the family in Sections 2-4; continuity for the full owner target remains open.

## 8. Source/control state


Repository transport was genuine, but no authenticated native mathematical-memory receiver-use event occurred. Status remains `WITHOUT_VERIFIED_BRAIN` / `full_brain_connected=false`.
