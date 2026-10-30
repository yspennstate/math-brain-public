# QFORM B17 — eventual finite-bank no-overshoot for the one-heavy majority-sign stress family

Run: `20260923T024252Z-fleet02-B17-QFORM-auto11`  
Account/slot: `fleet02/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW_SUPPORTING_THEOREM`; the unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate.

## 1. Exact target-level stress family

For every integer `m>=1` let

\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m).
\tag{1.1}
\]

Since `J_m/m` has eigenvalues `1,0,...,0`, every finite matrix in (1.1) has exact nonzero spectrum

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.}
\tag{1.2}
\]

Put an arbitrary probability density `0<=f_m<=1` on the singleton physical coordinate `X_m`; the law may depend on `m` and may have unbounded, disconnected or arbitrarily fragmented support. On the two banks put independent iid `Unif[-1/2,1/2]` variables, also independent of `X_m`, and write

\[
S_m=m^{-1/2}\sum_{j=1}^mU_j,\qquad
T_m=m^{-1/2}\sum_{j=1}^mV_j.
\]

Then the exact physical-coordinate quadratic form is

\[
\boxed{Q_{m,f}=X_m^2+S_m^2-T_m^2.}
\tag{1.3}
\]

Thus every finite member satisfies the original product-source density cap and exact three-large-eigenvalue hypothesis. No spectral rotation, post-rotation independence, moment assumption on `X_m`, support bound or log-concavity assumption on `X_m` is used.

The previous B17 theorem at
`yspennstate/math-open-problems@06aea167c49a7d7574f1c2f518c756f22413371a`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/B17-20260923T014533Z-r14-multiscale/REPORT.md`, proved for independent `G_+,G_-~N(0,1/12)` that

\[
\sup_{0\le f\le1,\int f=1}
\|p_{X_f^2+G_+^2-G_-^2}\|_\infty
\le C_{\rm maj},
\tag{1.4}
\]
where

\[
\boxed{
C_{\rm maj}=\frac6\pi\left(\frac52+\log\frac43-\gamma_E\right)
=4.221679863602472\ldots
<3\sqrt2=4.242640687119285\ldots .
}
\tag{1.5}
\]

That result left open whether a narrow finite-bank spike could survive while both banks converge weakly to Gaussians. The theorem below closes that escape **uniformly over all `m`-dependent heavy laws**.

## 2. Main theorem

### QFORM-ONE-HEAVY-MAJORITY-EVENTUAL-NOOVERSHOOT-v1

For the source-valid family (1.1)--(1.3),

\[
\boxed{
\limsup_{m\to\infty}
\sup_{0\le f\le1,\int f=1}
\|p_{Q_{m,f}}\|_\infty
\le C_{\rm maj}<3\sqrt2.
}
\tag{2.1}
\]

Consequently there exists a finite `m_0` such that for every `m>=m_0` and every cap-one heavy law `f`,

\[
\boxed{\|p_{Q_{m,f}}\|_\infty<3\sqrt2.}
\tag{2.2}
\]

No explicit `m_0` is claimed because the local-limit input is used qualitatively. In particular, (2.2) does not exclude an overshoot for one of the finitely many bank sizes below `m_0`.

The proof gives a reusable stability lemma: `L^1` convergence of the residual difference-square kernel, together with a uniform logarithmic singularity envelope, upgrades to `L^\infty` convergence **after arbitrary cap-one square mixing**.

## 3. Partner local limit and square pushforward

Let `h_m` denote the density of `S_m`, and let

\[
\gamma(x)=\sqrt{\frac6\pi}e^{-6x^2}
\tag{3.1}
\]

be the density of `N(0,1/12)`.

The completed designated partner result `fleet03/B17`, canonical report
`yspennstate/math-open-problems@f593cf73a4e7547eac4183f8e61062fca5176706`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T021034Z-fleet03-B17-QFORM-r22/REPORT.md`, proves in its Section 4.1 that

\[
\boxed{\|h_m-\gamma\|_\infty\longrightarrow0.}
\tag{3.2}
\]

The proof there is source-valid and explicit: the characteristic function is
`sinc(t/(2sqrt(m)))^m`, it is dominated by `exp(-t^2/24)` on the expanding central interval, and its outer Fourier tail is bounded by

\[
\frac{4\sqrt m}{(m-1)\pi^{m-1}}.
\tag{3.3}
\]

Because `h_m` and `gamma` are probability densities, (3.2) implies pointwise convergence and Scheffe's lemma gives

\[
\eta_m:=\|h_m-\gamma\|_1\longrightarrow0.
\tag{3.4}
\]

This is the completed partner result actually used in the present proof.

Both densities are even. Let `a_m` and `a_\infty` denote the densities of `S_m^2` and `G^2` respectively. For `u>0`,

\[
a_m(u)=\frac{h_m(\sqrt u)}{\sqrt u},\qquad
a_\infty(u)=\frac{\gamma(\sqrt u)}{\sqrt u}.
\tag{3.5}
\]

The change of variables `u=x^2`, together with evenness, gives the exact identity

\[
\boxed{\|a_m-a_\infty\|_1=\|h_m-\gamma\|_1=\eta_m.}
\tag{3.6}
\]

Let `k_m` be the density of `S_m^2-T_m^2`; equivalently

\[
k_m=a_m*\widetilde a_m,
\qquad \widetilde a_m(x)=a_m(-x),
\tag{3.7}
\]

and define `k_\infty` analogously. Young's inequality and a telescoping difference give

\[
\begin{aligned}
\delta_m:=\|k_m-k_\infty\|_1
&\le \|(a_m-a_\infty)*\widetilde a_m\|_1
   +\|a_\infty*(\widetilde a_m-\widetilde a_\infty)\|_1\\
&\le2\eta_m\longrightarrow0.
\end{aligned}
\tag{3.8}
\]

Ordinary `L^1` convergence is not enough by itself: the kernels have a logarithmic singularity at zero, so one must rule out concentration of the error on very thin sets. The next two sections do exactly that.

## 4. Uniform logarithmic envelope for every finite bank

Ball's one-dimensional cube-slicing bound applied to the unit coefficient vector `(1/sqrt(m),...,1/sqrt(m))` gives

\[
\|h_m\|_\infty\le\sqrt2
\tag{4.1}
\]

for every `m`; also `||gamma||_infty=sqrt(6/pi)<sqrt2`. Put

\[
M=\sqrt2.
\tag{4.2}
\]

For any even probability density `h` with `||h||_infty<=M`, the square density `a` satisfies

\[
a(u)\le M u^{-1/2},\qquad u>0.
\tag{4.3}
\]

If `k` is the difference density of two iid copies of the square, then for `r=|w|>0`,

\[
k(w)=\int_0^\infty a(u)a(u+r)\,du.
\tag{4.4}
\]

For `0<r<=1`, split at `u=1`. The near part obeys

\[
\int_0^1a(u)a(u+r)du
\le M^2\int_0^1\frac{du}{\sqrt{u(u+r)}}
=2M^2\operatorname{arsinh}(r^{-1/2}),
\tag{4.5}
\]

while the tail is at most

\[
M\int_1^\infty a(u)du\le M.
\tag{4.6}
\]

Since `arsinh(r^{-1/2})<=log(3/sqrt(r))` for `0<r<=1`, and for `r>=1` directly `k(w)<=M`, we get the uniform envelope

\[
\boxed{
k(w)\le C_0+M^2\log_+\frac1{|w|},
\qquad C_0=M+2M^2\log3.
}
\tag{4.7}
\]

It applies simultaneously to all `k_m` and to `k_\infty`. Hence, with

\[
d_m(w)=|k_m(w)-k_\infty(w)|,
\quad
A=2C_0=2\sqrt2+8\log3,
\quad B=2M^2=4,
\tag{4.8}
\]

we have

\[
d_m(w)\le A+B\log_+\frac1{|w|}.
\tag{4.9}
\]

Let

\[
\mu_m(\lambda)=|\{w\in\mathbb R:d_m(w)>\lambda\}|.
\tag{4.10}
\]

Chebyshev and (3.8) give for every `lambda>0`

\[
\mu_m(\lambda)\le\frac{\delta_m}{\lambda}.
\tag{4.11}
\]

For `lambda>A`, (4.9) gives the independent exponential estimate

\[
\boxed{
\mu_m(\lambda)\le2\exp\left[-\frac{\lambda-A}{B}\right].
}
\tag{4.12}
\]

The combination (4.11)--(4.12) is the uniform-integrability input that weak convergence alone lacks.

## 5. Square-preimage lemma and the transfer modulus

For every measurable `E subset R` of finite measure and every real `s`,

\[
\boxed{
|\{x\in\mathbb R:s-x^2\in E\}|\le2\sqrt{|E|}.
}
\tag{5.1}
\]

Indeed, setting `F=(s-E) intersect [0,infinity)`, the two branches of `x -> x^2` give

\[
|\{x:x^2\in F\}|=\int_Fu^{-1/2}du.
\tag{5.2}
\]

Among subsets of `[0,infinity)` of measure `b`, the decreasing function `u^{-1/2}` has maximal integral on `[0,b]`, equal to `2sqrt(b)`, and `|F|<=|E|`. This proves (5.1).

By layer cake and (5.1), uniformly in `s`,

\[
\begin{aligned}
\int_{\mathbb R}d_m(s-x^2)dx
&=\int_0^\infty
 |\{x:d_m(s-x^2)>\lambda\}|d\lambda\\
&\le2\int_0^\infty\sqrt{\mu_m(\lambda)}d\lambda.
\end{aligned}
\tag{5.3}
\]

For any `Lambda>A`, use (4.11) below `Lambda` and (4.12) above it. This gives the explicit bound

\[
\boxed{
T_m:=\sup_s\int d_m(s-x^2)dx
\le4\sqrt{\delta_m\Lambda}
 +4\sqrt2\,B\exp\left[-\frac{\Lambda-A}{2B}\right].
}
\tag{5.4}
\]

Since `delta_m->0`, first choose `Lambda` large and then `m` large to get

\[
\boxed{T_m\longrightarrow0.}
\tag{5.5}
\]

For an explicit modulus, whenever `0<delta_m<1`, taking

\[
\Lambda=A+B\log(1/\delta_m)
\tag{5.6}
\]

gives

\[
T_m\le
4\sqrt{\delta_m\,[A+B\log(1/\delta_m)]}
+4\sqrt2\,B\sqrt{\delta_m}.
\tag{5.7}
\]

Thus the singular difference-square kernel is stable after cap-one square mixing at the natural `sqrt(delta log(1/delta))` scale.

## 6. Uniformity over arbitrary fragmented heavy laws

For any cap-one probability density `f`, conditioning on `X_f=x` gives

\[
p_{Q_{m,f}}(s)=\int_{\mathbb R}f(x)k_m(s-x^2)dx,
\tag{6.1}
\]

and analogously

\[
p_{Q_{\infty,f}}(s)=\int f(x)k_\infty(s-x^2)dx.
\tag{6.2}
\]

The only property of the heavy law now used is `0<=f<=1`. Therefore

\[
\begin{aligned}
|p_{Q_{m,f}}(s)-p_{Q_{\infty,f}}(s)|
&\le\int f(x)d_m(s-x^2)dx\\
&\le\int d_m(s-x^2)dx
\le T_m.
\end{aligned}
\tag{6.3}
\]

Taking the supremum over both `s` and all admissible heavy laws,

\[
\boxed{
\sup_f\|p_{Q_{m,f}}-p_{Q_{\infty,f}}\|_\infty\le T_m\to0.
}
\tag{6.4}
\]

Combining (6.4) with the Gaussian-completion bound (1.4)--(1.5) proves (2.1). Because

\[
3\sqrt2-C_{\rm maj}=0.020960823516813\ldots>0,
\tag{6.5}
\]

(2.2) follows immediately.

This conclusion is uniform even when `f=f_m` changes adversarially with `m`. Thus a sequence of increasingly fragmented or translated heavy laws cannot hide a finite-width peak while the two banks become diffuse.

## 7. Required newest-Claude theorem applied to a finite obstruction

The required source
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, proves Theorem C: for every exact rank-three `(+,+,-)` form with large coefficients `lambda_1,lambda_2,mu>=1`, every source-valid cap-one product law and every `s>=0`,

\[
p_Q(s)\le\pi\sqrt2
\tag{7.1}
\]

in the unit-coefficient case. Applying it to the exact matrices (1.1) gives the genuine finite-dimensional inequality

\[
\boxed{p_{Q_{m,f}}(s)\le\pi\sqrt2\quad\text{for every }m,\ f\le1,\ s\ge0.}
\tag{7.2}
\]

This is a useful obstruction but not a sharp-constant proof because `pi sqrt(2)>3 sqrt(2)`. The present transfer theorem complements (7.2): it rules out **all output locations** at the `3sqrt(2)` scale once the banks are sufficiently diffuse. The companion `RESULTS.md` and `FOURIER_ROUTE_REPORT.md` at the same pinned commit were also read; no pointwise scalar oscillatory-decay claim is imported.

## 8. Interpretation for the sharp constant

The theorem distinguishes two questions that must not be conflated.

* It **rules out an asymptotic witness mechanism**: the exact family `diag(1,J_m/m,-J_m/m)` cannot exceed `3sqrt(2)` for large `m`, even if its one heavy law is changed adversarially with `m`.
* It does **not** prove the unrestricted QFORM conjecture, does not prove that `3sqrt(2)` is the universal sharp constant, and does not rule out a `3sqrt(2)` overshoot at one of finitely many small bank sizes.
* If a finite source-valid example were found with peak above `3sqrt(2)`, that would refute only the candidate sharp constant `3sqrt(2)`, not the existence of a larger universal QFORM constant.

Together with the latest designated partner theorem, which gives a strict `4.1092705664...<3sqrt(2)` bound for a genuinely rotated two-heavy/shared-bank Gaussian-completion family, the plausible witness space is pushed toward finite genuinely coupled configurations, several non-collinear macroscopic rows, or multiscale constructions in which no residual bank is close in density to a Gaussian.

## 9. Dependencies and corrections

Consumed premises:

1. `fleet02/B17` preceding Gaussian-completion theorem at commit `06aea167c49a7d7574f1c2f518c756f22413371a` for the constant `C_maj`.
2. Designated partner `fleet03/B17` local-limit theorem at commit `f593cf73a4e7547eac4183f8e61062fca5176706`, specifically `||h_m-gamma||_infty->0` for the normalized centered-uniform bank.
3. Required newest-Claude Theorem C at exact commit `e5f71d79eff325201dd0274053d20268ce65b837`, applied in (7.2).
4. Ball's cube-slicing density bound in the one-dimensional projection form, only for the explicit centered-uniform banks.

No use is made of uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, post-rotation independence, positive moments of conditional projection-density suprema, a fixed fragment count, a uniformly good single physical minor, or a universal cross-rank-three cut. The live correction inbox was refreshed before publication; the argument is compatible with the listed falsifiers.

## 10. Next unpaid B17 step

The sharp search should now examine either the finitely many small/medium bank sizes in (1.1) with exact cap-one bathtub optimization, or leave the one-heavy architecture and attack genuinely non-collinear multi-heavy finite forms. Repeating another Gaussian-completion limit of the same family is no longer an unpaid implication.
