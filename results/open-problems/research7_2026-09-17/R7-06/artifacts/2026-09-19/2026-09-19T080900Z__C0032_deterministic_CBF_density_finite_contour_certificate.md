Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0032 — deterministic complete-Bernstein density, finite-contour certificate, and exact special-index collapse

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), arXiv:1109.3343v4, heavy-tailed Section 6.6 / p. 39 request to identify explicitly the isotropic limiting density `g_alpha`; underlying law and scalar PWIT characterization: Charles Bordenave, Pietro Caputo and Djalil Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011), arXiv:1006.1713.

Date: 2026-09-19 UTC  
Canonical target: `C0032`  
Worker: `R7-06 Hard Conjecture Certificates`  
Methods: **B10 / B24 / B26**  
Status of source after this artifact: **PARTIAL / OPEN**; the formulas below are theorem-level progress, not a source-closure declaration.

## 1. Cumulative input and notation

Put

\[
\beta=\alpha/2\in(0,1),\qquad
c_\beta=\Gamma(1-\beta),\qquad
C_\beta=\Gamma(1-\beta)\Gamma(1+\beta).
\]

Earlier verified C0032 work eliminated the BCC self-consistent scalar and obtained

\[
q_\beta(a)=\mathbb E\frac{T}{a+T},\qquad T=SS',
\tag{1.1}
\]

for iid positive beta-stable variables in the BCC normalization, together with

\[
R_\beta(a)=a\left(\frac{q_\beta(a)}{C_\beta}\right)^{1/\beta}.
\tag{1.2}
\]

If `Q_beta(r)` denotes the radial tail in squared-radius coordinate,

\[
Q_\beta(R_\beta(a))=q_\beta(a).
\tag{1.3}
\]

The exact Mellin transform is

\[
\widehat q_\beta(s)
=c_\beta^{2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)},
\qquad 0<\Re s<\beta.
\tag{1.4}
\]

The previous recovery run introduced the single-valued radius-power map

\[
\boxed{
H_\beta(a)=R_\beta(a)^\beta
=\frac{a^\beta q_\beta(a)}{C_\beta}
}
\tag{1.5}
\]

and proved that `H_beta` is a nonconstant complete Bernstein function on the slit plane

\[
\Omega=\mathbb C\setminus(-\infty,0].
\]

Therefore, for every `x>0`, the equation `H_beta(z)=x` has exactly one root in the whole slit plane, and it lies on `(0,infinity)`.

This run removes the last stable-law notation from `H_beta`, replaces the limiting contour of the previous run by a finite certified contour, and checks exact collapse at the simplest special index.

---

## 2. B10 — derandomize the radius map completely

### 2.1 Standard Stieltjes representation

Since `H_beta` is complete Bernstein, it has a representation

\[
H_\beta(z)=a_0+b_0z+z\int_0^\infty\frac{\sigma_\beta(dt)}{z+t},
\tag{2.1}
\]

with a positive measure satisfying the usual Stieltjes integrability condition.

Here the affine pieces vanish. First,

\[
H_\beta(0+)=0,
\]

so `a_0=0`. Second, because `0<q_beta(a)<=1`,

\[
0\le \frac{H_\beta(a)}a
=\frac{a^{\beta-1}q_\beta(a)}{C_\beta}
\le \frac{a^{\beta-1}}{C_\beta}\longrightarrow0,
\qquad a\to\infty,
\]

hence `b_0=0`. Thus

\[
\boxed{
\frac{H_\beta(z)}z
=\int_0^\infty\frac{\sigma_\beta(dt)}{z+t}.
}
\tag{2.2}
\]

The new point is that the representing measure can be written deterministically from Gamma functions, with no stable random variables left.

### 2.2 Mellin transform of the canonical density

Set

\[
g_\beta(a)=\frac{H_\beta(a)}a
=\frac{a^{\beta-1}q_\beta(a)}{C_\beta}.
\tag{2.3}
\]

For `1-beta<Re s<1`, (1.4) gives

\[
\widehat g_\beta(s)
=\frac1{C_\beta}\widehat q_\beta(s+\beta-1)
\]

and hence

\[
\widehat g_\beta(s)
=
\frac{c_\beta^{2(s+\beta-1)/\beta}}{C_\beta}
\frac{\Gamma(s+\beta-1)\Gamma((1-s)/\beta)^2}
{\Gamma(2-\beta-s)}.
\tag{2.4}
\]

On the other hand, for `0<Re s<1`,

\[
\int_0^\infty\frac{a^{s-1}}{a+t}\,da
=\frac{\pi}{\sin(\pi s)}t^{s-1}.
\tag{2.5}
\]

Applying Mellin transforms to (2.2) therefore gives

\[
\widehat g_\beta(s)
=\frac\pi{\sin(\pi s)}\widehat\sigma_\beta(s),
\tag{2.6}
\]

where `sigma_beta(t) dt` is the absolutely continuous form of the canonical representing measure. Combining (2.4)–(2.6),

\[
\boxed{
\widehat\sigma_\beta(s)
=
\frac{\sin(\pi s)}{\pi C_\beta}
 c_\beta^{2(s+\beta-1)/\beta}
\frac{\Gamma(s+\beta-1)\Gamma((1-s)/\beta)^2}
{\Gamma(2-\beta-s)},
}
\tag{2.7}
\]

valid on

\[
1-\beta<\Re s<1.
\]

Using Euler reflection,

\[
\boxed{
\widehat\sigma_\beta(s)
=
\frac{c_\beta^{2(s+\beta-1)/\beta}}{C_\beta}
\frac{\Gamma(s+\beta-1)\Gamma((1-s)/\beta)^2}
{\Gamma(2-\beta-s)\Gamma(s)\Gamma(1-s)}.
}
\tag{2.8}
\]

### 2.3 Deterministic inverse-Mellin formula

For any fixed `kappa` with `1-beta<kappa<1`, define

\[
\boxed{
\sigma_\beta(t)
=\frac1{2\pi i}
\int_{\kappa-i\infty}^{\kappa+i\infty}
\widehat\sigma_\beta(s)t^{-s}\,ds,
\qquad t>0.
}
\tag{2.9}
\]

Stirling's formula applied to (2.8) gives exponential decay on vertical lines: for fixed `kappa` in the strip,

\[
|\widehat\sigma_\beta(\kappa+i\tau)|
\le K_{\beta,\kappa}(1+|\tau|)^{m_{\beta,\kappa}}
\exp\{-\pi|\tau|(1/\beta-1)\},
\tag{2.10}
\]

for some finite constants `K,m`. Hence (2.9) converges absolutely and locally uniformly in `t>0`, so it defines a continuous density.

To identify it with the positive CBF measure rather than merely with a formal Mellin inversion, insert (2.9) into the Stieltjes kernel (2.5). On the common Mellin strip the transform equals (2.4), hence the resulting Stieltjes function agrees with `g_beta`. Uniqueness of the Stieltjes representing measure then identifies (2.9) with the positive measure in (2.2). Consequently

\[
\boxed{\sigma_\beta(t)\ge0\quad(t>0)}
\tag{2.11}
\]

and the radius map is now completely deterministic:

\[
\boxed{
H_\beta(z)
=z\int_0^\infty\frac{\sigma_\beta(t)}{z+t}\,dt,
\qquad z\in\Omega,
}
\tag{2.12}
\]

with `sigma_beta` given solely by Gamma functions in (2.8)–(2.9).

The first two derivatives needed below are equally explicit:

\[
\boxed{
H_\beta'(z)=\int_0^\infty\frac{t\sigma_\beta(t)}{(z+t)^2}\,dt,
\qquad
-H_\beta''(z)=2\int_0^\infty\frac{t\sigma_\beta(t)}{(z+t)^3}\,dt.
}
\tag{2.13}
\]

### 2.4 Deterministic Lévy density

Using

\[
\frac z{z+t}=\int_0^\infty(1-e^{-zu})t e^{-tu}\,du,
\]

we obtain the complete-Bernstein Lévy representation

\[
\boxed{
H_\beta(z)=\int_0^\infty(1-e^{-zu})\ell_\beta(u)\,du,
\qquad
\ell_\beta(u)=\int_0^\infty t e^{-tu}\sigma_\beta(t)\,dt.
}
\tag{2.14}
\]

Its Mellin transform is also explicit. Whenever the integrals converge,

\[
\boxed{
\int_0^\infty u^{v-1}\ell_\beta(u)\,du
=\Gamma(v)\widehat\sigma_\beta(2-v),
\qquad 1<\Re v<1+\beta.
}
\tag{2.15}
\]

Equations (2.8), (2.9), and (2.15) are the deterministic canonical Stieltjes/Lévy data requested by B10.

### 2.5 Function-class consequence

The inverse Mellin integrand (2.8) is a finite product/quotient of Gamma functions whose arguments are affine in `s` with slopes `1` and `1/beta`. Therefore (2.9) is a Fox-H-type Mellin–Barnes representation for arbitrary real `beta in (0,1)`.

If `beta=p/q` is rational in lowest terms, Gauss multiplication removes the rational slopes and reduces (2.9) to a finite Meijer-G expression. This is consistent with the classical rational-index stable-density formulas of Penson–Górska; what is new in the present derivation is the canonical CBF/Stieltjes density attached to the BCC physical radius map, not the existence of rational-index stable Meijer-G formulas themselves.

---

## 3. B24 — replace the limiting contour by a finite certified contour

The previous recovery run wrote the inverse as a limit of contours tending to the boundary of the disk. The global one-root theorem in fact permits a finite contour once a completely explicit bracket is certified.

### 3.1 Disk geometry and a finite root bracket

Use the conformal map

\[
\chi(w)=\left(\frac{1+w}{1-w}\right)^2,
\qquad |w|<1,
\tag{3.1}
\]

from the unit disk onto `Omega`, and its positive-axis inverse

\[
\phi(a)=\frac{\sqrt a-1}{\sqrt a+1}.
\tag{3.2}
\]

For `0<r<1`, define

\[
A_-(r)=\left(\frac{1-r}{1+r}\right)^2,
\qquad
A_+(r)=\left(\frac{1+r}{1-r}\right)^2=A_-(r)^{-1}.
\tag{3.3}
\]

Fix `x>0`. If

\[
\boxed{
H_\beta(A_-(r))<x<H_\beta(A_+(r)),
}
\tag{3.4}
\]

then strict monotonicity on the positive axis places the unique root

\[
a_*=H_\beta^{-1}(x)
\]

inside `(A_-(r),A_+(r))`. Therefore

\[
w_*=\phi(a_*)
\]

satisfies `|w_*|<r`.

Since the global CBF root theorem excludes every other root in the slit plane, the argument principle gives the exact finite-contour identity

\[
\boxed{
w_*
=\frac1{2\pi i}\oint_{|w|=r}
 w\,
\frac{H_\beta'(\chi(w))\chi'(w)}
{H_\beta(\chi(w))-x}\,dw.
}
\tag{3.5}
\]

Thus the former `r -> 1` contour limit is unnecessary. Once (3.4) holds, the radial-contour truncation error is **exactly zero**.

A canonical radius requires no hidden root. For example let

\[
r_n=1-2^{-n},\qquad n=1,2,\ldots,
\tag{3.6}
\]

and choose the first `n` for which (3.4) holds. Such an `n` exists because `A_-(r_n)->0`, `A_+(r_n)->infinity`, `H_beta(0+)=0`, and `H_beta(infinity)=infinity`.

### 3.2 Quantitative denominator certificate

For certification one also wants a lower bound for the denominator on the chosen contour.

Put

\[
F(w)=H_\beta(\chi(w))-x,
\qquad
c_r=\frac{1-r^2}{1+r^2}>0.
\tag{3.7}
\]

If `z=chi(w)` and `|w|=r`, then

\[
|\arg z|\le 4\arctan r<\pi,
\qquad |z|\ge A_-(r).
\tag{3.8}
\]

For every `t>=0`, elementary plane geometry gives

\[
|z+t|
\ge \cos\!\left(\frac{|\arg z|}{2}\right)(|z|+t)
\ge c_r(|z|+t).
\tag{3.9}
\]

Using the deterministic representation (2.13),

\[
|H_\beta'(z)|
\le c_r^{-2}H_\beta'(A_-(r)).
\tag{3.10}
\]

Moreover

\[
\chi'(w)=\frac{4(1+w)}{(1-w)^3},
\qquad
\chi''(w)=\frac{8(2+w)}{(1-w)^4},
\tag{3.11}
\]

so on `|w|=r`,

\[
C_{1,r}:=\sup|\chi'(w)|
\le\frac{4(1+r)}{(1-r)^3},
\qquad
C_{2,r}:=\sup|\chi''(w)|
\le\frac{8(2+r)}{(1-r)^4}.
\tag{3.12}
\]

Hence

\[
\boxed{
L_r:=\sup_{|w|=r}|F'(w)|
\le C_{1,r}c_r^{-2}H_\beta'(A_-(r)).
}
\tag{3.13}
\]

Let

\[
w_k=re^{2\pi i k/N},\qquad
 d_{r,N}=\min_{0\le k<N}|F(w_k)|.
\tag{3.14}
\]

Every point of the circle lies within angular distance at most `pi/N` of a grid point. The arc distance is at most `pi r/N`; therefore

\[
\boxed{
\delta_{r,N}:=
 d_{r,N}-\frac{\pi rL_r}{N}
\le \min_{|w|=r}|F(w)|.
}
\tag{3.15}
\]

Whenever `delta_{r,N}>0`, nonvanishing of the contour denominator is rigorously certified.

### 3.3 Explicit quadrature-error certificate

A second derivative bound follows from (2.13) and (3.9):

\[
|H_\beta''(z)|
\le c_r^{-3}[-H_\beta''(A_-(r))].
\tag{3.16}
\]

Thus

\[
\boxed{
M_r:=\sup_{|w|=r}|F''(w)|
\le
c_r^{-3}[-H_\beta''(A_-)]C_{1,r}^2
+c_r^{-2}H_\beta'(A_-)C_{2,r}.
}
\tag{3.17}
\]

Parameterize `w(theta)=r exp(i theta)`. Formula (3.5) becomes

\[
w_*
=\frac1{2\pi}\int_0^{2\pi}
\frac{w(\theta)^2F'(w(\theta))}{F(w(\theta))}\,d\theta.
\tag{3.18}
\]

Let the equally spaced quadrature be

\[
Q_N=\frac1N\sum_{k=0}^{N-1}
\frac{w_k^2F'(w_k)}{F(w_k)}.
\tag{3.19}
\]

If `delta=delta_{r,N}>0`, differentiating the integrand with respect to `theta` yields the elementary bound

\[
\left|\frac d{d\theta}
\frac{w^2F'}F\right|
\le
\frac{2r^2L_r}{\delta}
+\frac{r^3M_r}{\delta}
+\frac{r^3L_r^2}{\delta^2}
=:K_{r,N}.
\tag{3.20}
\]

The error of the uniform left-endpoint Riemann sum on a `2pi`-periodic Lipschitz function is at most `pi` times the Lipschitz constant divided by `N`. Hence

\[
\boxed{
|Q_N-w_*|
\le\frac{\pi K_{r,N}}N.
}
\tag{3.21}
\]

This is intentionally a robust certificate rather than an optimized spectral trapezoidal estimate. Every term on the right is determined by positive-axis values of `H_beta,H_beta',H_beta''` and finitely many contour evaluations of `H_beta`; all of these can be enclosed by the exponentially convergent Mellin/Stieltjes formulas in Section 2.

Therefore the all-radius inverse is not only a formal contour representation: it has a finite, deterministic, rigorous approximation procedure with an explicit a posteriori error bound and no hidden real root solve.

---

## 4. B26 — the simplest sporadic index and exact collapse

### 4.1 Exact alpha=1 collapse

For `beta=1/2` (`alpha=1`), previous C0032 work proved

\[
H_{1/2}(a)
=L\!\left(\frac\pi{2\sqrt a}\right),
\tag{4.1}
\]

where

\[
L(z)=\frac\pi2[\mathbf H_0(z)-Y_0(z)]
=\int_0^\infty e^{-z\sinh t}\,dt.
\tag{4.2}
\]

For `|w|<1`, the principal square root of (3.1) is

\[
\sqrt{\chi(w)}=\frac{1+w}{1-w},
\]

because this Möbius map lies in the right half-plane. Thus

\[
\boxed{
H_{1/2}(\chi(w))
=L\!\left(\frac\pi2\frac{1-w}{1+w}\right).
}
\tag{4.3}
\]

Let `Z(rho)=L^{-1}(rho)`. Solving `H_{1/2}(chi(w))=rho` gives

\[
\boxed{
w_*(\rho)=\frac{\pi-2Z(\rho)}{\pi+2Z(\rho)}.
}
\tag{4.4}
\]

Consequently

\[
\boxed{
H_{1/2}^{-1}(\rho)
=\chi(w_*(\rho))
=\left(\frac\pi{2Z(\rho)}\right)^2.
}
\tag{4.5}
\]

Equation (3.5) must return exactly (4.4), because both are the unique root coordinate. Thus the general complete-Bernstein contour inversion collapses exactly to the earlier inverse-Struve representation at the first nontrivial special index. This is a structural consistency theorem, not a numerical coincidence.

### 4.2 Rational beta

For `beta=p/q` in lowest terms, Section 2 already implies that `sigma_beta` is finite Meijer-G after Gauss multiplication. Earlier C0032 work independently derived a Meijer-G formula for the auxiliary transform `F_beta` itself. Substituting either representation into (3.5) produces a finite contour whose integrand consists of finite Meijer-G functions and their derivatives. The global CBF theorem ensures that no additional branch choice is hidden in this rational reduction.

This recovers the familiar rational-index phenomenon from one-sided stable laws while preserving the physical BCC inverse branch globally.

### 4.3 No algebraic sporadic inverse anywhere in the heavy-tail regime

There is also a negative result. Previous Mellin-pole analysis proved

\[
H_\beta(a)=\beta\log a+\eta_\beta+o(1),
\qquad a\to\infty,
\tag{4.6}
\]

for an explicit constant `eta_beta`. Therefore

\[
\boxed{
H_\beta^{-1}(x)
=\exp\!\left(\frac{x-\eta_\beta}{\beta}\right)(1+o(1)),
\qquad x\to\infty.
}
\tag{4.7}
\]

An algebraic function over `C(x)` has a Puiseux expansion at infinity on each branch and hence has only power-law type growth there. The exponential growth in (4.7) is impossible for an algebraic function. Hence

\[
\boxed{
H_\beta^{-1}\text{ is not algebraic over }\mathbb C(x)
\quad\text{for every }0<\beta<1.
}
\tag{4.8}
\]

Thus there is no hidden rational or algebraic exceptional index inside the heavy-tailed interval. This does **not** claim non-elementarity, non-D-algebraicity, or impossibility of broader special-function descriptions.

---

## 5. Physical all-radius formula after B10/B24

For a physical radius `rho>0`, put

\[
x=\rho^\alpha.
\]

Choose any finite `r<1` satisfying (3.4), evaluate `w_*(x)` from the exact finite contour (3.5), and set

\[
a(\rho)=\chi(w_*(x)).
\tag{5.1}
\]

Since `H_beta(a)=x`, the squared-radius tail is

\[
\boxed{
1-\mu_\alpha\{|z|\le\rho\}
=C_\beta\frac{\rho^\alpha}{a(\rho)^\beta}
=C_\beta
\left[
\rho\frac{1-w_*(x)}{1+w_*(x)}
\right]^\alpha.
}
\tag{5.2}
\]

The planar density follows by differentiation; equivalently, using the positive-axis derivative of `H_beta`,

\[
\boxed{
g_\alpha(\rho)
=
\frac{\beta Q(\rho)}{\pi\rho^2}
\left[
\frac{\beta\rho^\alpha}
{a(\rho)H_\beta'(a(\rho))}-1
\right],
}
\tag{5.3}
\]

where `Q(rho)` denotes the tail in (5.2). At `rho=0`, the exact origin value from the earlier local theorem applies.

The key distinction from the original BCC description is now complete: `H_beta`, its derivatives, the inverse branch, the tail, and the density are all described by deterministic Gamma/Mellin/Stieltjes/finite-contour formulas. No PWIT random recursion, stable random variable, self-consistent scalar, or hidden root solve remains in (2.8)–(5.3).

---

## 6. What this does and does not resolve

### Theorems established in this run

1. The canonical CBF representing measure for `H_beta` is absolutely continuous and has the explicit Gamma Mellin transform (2.7)/(2.8) and the deterministic inverse-Mellin density (2.9).
2. `H_beta` therefore has the deterministic Stieltjes and Lévy forms (2.12) and (2.14), with stable random variables eliminated from the final representation.
3. The former limiting inverse contour can be replaced, for every `x>0`, by an exact **finite** contour selected by explicit endpoint inequalities (3.4).
4. The contour denominator and numerical quadrature have explicit rigorous certificates (3.15) and (3.21).
5. At `alpha=1` the general contour inverse collapses exactly to the inverse Struve-second-kind representation (4.4)/(4.5).
6. No `0<beta<1` admits an algebraic inverse `H_beta^{-1}`.

### What is deliberately not claimed

- No claim that a bounded literature search certifies novelty.
- No claim that the source's informal word “explicit” necessarily accepts the representation above without an independent scope judgment.
- No claim of source closure before the required independent P26 audit, distinct OTHER-track audit, and self-contained paper package.
- No claim that `H_beta^{-1}` is non-elementary or non-D-algebraic.
- No claim that the previously identified potential correction to the printed BCC far-tail exponent has received an independent audit here.

The honest source status therefore remains **PARTIAL / OPEN**.

---

## 7. Dated literature check, 2026-09-19 UTC

Fresh bounded searches again located:

- Bordenave–Chafaï, *Around the circular law*, arXiv:1109.3343, as the source survey describing the heavy-tailed limiting law through PWIT/objective-method machinery.
- Bordenave–Caputo–Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, arXiv:1006.1713 / CMP 307 (2011), as the primary construction/implicit-characterization source.
- James Chen and Sheehan Olver, *Computing Inverses of Stieltjes Transforms of Probability Measures*, Mathematics of Computation, published online 2026-01-14, DOI 10.1090/mcom/4159 / arXiv:2410.16178. Their work supplies a highly relevant general precedent for inverse Stieltjes transforms and contour-based recovery, but the located material does not contain the BCC radius map or formulas (2.8)–(5.3).
- K. A. Penson and K. Górska, *Exact and explicit probability densities for one-sided Lévy stable distributions*, arXiv:1007.0193 / Phys. Rev. Lett. 105 (2010), giving explicit known-function formulas for rational stable indices. This is prior art for rational-index stable special functions, not for the BCC physical radius inversion derived here.

The bounded searches did not surface a later source-matching all-alpha/all-radius explicit BCC density formula. This is negative evidence only.

---

## 8. Next mathematical tests

The next ordinary cycle, if C0032 remains active, should not repeat B10/B24/B26. The useful nonrepeating directions are:

- **B5 — add/differentiate the index parameter:** differentiate the deterministic Mellin density and inverse branch with respect to `beta`, aiming for quantitative continuity and endpoint control for the physical density.
- **B17 — look for the constants/functions elsewhere:** compare the canonical density (2.8) and reciprocal-integer reductions with established Fox-H/Thorin/complete-Bernstein tables to decide whether the all-index representation already has a standard named form.
- **B28 — replace “for all beta” by generic beta:** isolate which identities are genuinely exceptional at rational beta and prove a generic-index statement for the inverse-transform complexity rather than forcing a nonexistent uniform holonomic template.

Because the frozen origin-jet metric was already saturated before this run, these global theorems do not increase it. They instead move the source-level representation toward a scope-auditable closure candidate.
