# Lemma II.B (2D bounded-density anti-concentration): the non-Gaussian two-projection local CLT

**Status: fully proved** (real and complex), self-contained modulo standard one-variable
facts that are proved here. This is the non-Gaussian replacement for the Gaussian
"Two-slab and two-disk estimate" (Lemma 4.X of `gaussian_row_submatrices_acha_strong.tex`,
eqs. `real-cond`/`complex-cond`), and it is exactly the *two-projection local central
limit theorem* requested in `parts/open_problems.tex`, Problem `prob:pc`.

Throughout, $\F\in\{\R,\C\}$, $d_\F=\dim_\R\F\in\{1,2\}$, and $|\cdot|$ is the modulus on
$\F$ and the Euclidean norm on $\R^k$.

---

## 1. Setup and statement

Let $x=(x_1,\dots,x_m)\in\F^m$ have **i.i.d.** entries with

- mean zero: $\EE x_1=0$;
- unit variance (and proper/circular when $\F=\C$): $\EE|x_1|^2=1$, and for $\F=\C$ also
  $\EE x_1^2=0$;
- a Lebesgue density $f$ on $\F\simeq\R^{d_\F}$ with $\|f\|_\infty\le K$.

Let $u,v\in\F^m$ be **deterministic** unit vectors that are **delocalized**:
$$
\|u\|_\infty,\ \|v\|_\infty\ \le\ \beta:=m^{-1/2+\delta},\qquad 0<\delta<\tfrac12 .
$$
Put $\rho=\langle u,v\rangle=\sum_j u_j\overline{v_j}$ (Hermitian inner product) and
$$
S_1=\langle x,u\rangle=\sum_{j=1}^m x_j\,\overline{u_j},\qquad
S_2=\langle x,v\rangle=\sum_{j=1}^m x_j\,\overline{v_j},
$$
so $(S_1,S_2)\in\F^2$. Define the single–form small ball and the pair
$$
p(t)=\PP\{|S_1|\le t\},\qquad
q(t)=\PP\{|S_1|\le t,\ |S_2|\le t\}.
$$
Fix a separation constant $\kappa_0\in(0,1)$ and assume $|\rho|\le 1-\kappa_0$.

> **Lemma (2D bounded-density anti-concentration).**
> Under the assumptions above there is a function $o(1)=o_{K,\kappa_0,\delta}(1)\to0$ as
> $m\to\infty$, **uniform over all unit delocalized $u,v$ with $|\rho|\le1-\kappa_0$ and over
> all $0<t\le1$ with $t\to0$**, such that
> $$
> \boxed{\,q(t)\ \le\ \bigl(1+o(1)\bigr)\,\frac{p(t)^2}{(1-|\rho|^2)^{\,d_\F/2}}\,}
> $$
> i.e.
> $$
> q(t)\le(1+o(1))\,\frac{p(t)^2}{\sqrt{1-\rho^2}}\quad(\F=\R),
> \qquad
> q(t)\le(1+o(1))\,\frac{p(t)^2}{1-|\rho|^2}\quad(\F=\C).
> $$
> Equivalently, $(S_1,S_2)$ has a bounded continuous joint density $g_m$ on $\F^2$ and
> $$
> \sup_{w\in\F^2}\bigl|g_m(w)-\Gamma_\Sigma(w)\bigr|\xrightarrow[m\to\infty]{}0
> \quad\text{uniformly for }|\rho|\le1-\kappa_0,
> $$
> where $\Gamma_\Sigma$ is the centered ($\F$-)Gaussian density with covariance
> $\Sigma=\begin{psmallmatrix}1&\rho\\\bar\rho&1\end{psmallmatrix}$, whose value at the origin is
> $\Gamma_\Sigma(0)=\dfrac{a_{d_\F}^2}{(1-|\rho|^2)^{d_\F/2}}$, $a_1=(2\pi)^{-1/2}$, $a_2=\pi^{-1}$.

The displayed constants are **exactly** those of the Gaussian source: with
$s=\sqrt{1-|\rho|^2}$ the source's conditional bounds are
$q\le 2t^2/(\pi s)$ ($\F=\R$) and $q\le t^4/(1-|\rho|^2)$ ($\F=\C$), and these are reproduced
below (Remark in §6). Here $\rho$ is **fixed** by the deterministic $u,v$; the averaging over
random normals that produces the source's extra factor $1+C/D$ is downstream, in the
second-moment assembly (§7).

---

## 2. Strategy

Write the proof for the joint density and then read off $q$ and $p$.

1. **(§3) Single-variable characteristic-function bound.** From finite variance and absolute
   continuity (which bounded density supplies) we get one constant $\eta>0$ with
   $|\psi(\theta)|\le e^{-\eta\min(|\theta|^2,1)}$, where $\psi$ is the (common) entry
   characteristic function. We also record $\psi\in L^2$.
2. **(§4) Geometry of the coefficient frame.** The vectors carrying the two forms have small
   norm (delocalization) and second-moment matrix $\Sigma$ with $\lambda_{\min}(\Sigma)\ge\kappa_0$.
   A Cauchy–Binet argument extracts well-conditioned transverse pairs.
3. **(§5) Local CLT in sup-norm** via Fourier inversion: a quadratic (Lindeberg) expansion on a
   fixed ball, an elementary energy bound on the moderate tail, and a Cauchy–Schwarz/$L^2$
   argument on the far tail give $\int|\phi_m-\widehat{\Gamma_\Sigma}|\to0$, hence
   $\|g_m-\Gamma_\Sigma\|_\infty\to0$.
4. **(§6) Conversion** of the density bound into the small-ball ratio, producing the exact
   constants.

The real case is given in full; §8 records the (identical) complex case with its constants.

We use the real Fourier convention $\widehat h(\xi)=\int e^{i\langle\xi,w\rangle}h(w)\,dw$,
inversion $h(w)=(2\pi)^{-k}\int e^{-i\langle\xi,w\rangle}\widehat h(\xi)\,d\xi$ on $\R^k$.

---

## 3. The single-variable characteristic-function bound

Let $\psi(\theta)=\EE e^{i\theta x_1}$ ($\theta\in\R$, real case) be the entry characteristic
function. Since all entries are i.i.d., $\psi$ is a single fixed function.

> **Lemma A (CF bound).** Assume $\EE x_1=0$, $\EE x_1^2=1$, and $x_1$ has a bounded density
> $f\le K$. Then:
> (a) **(quadratic regime)** there are $c_1>0$ and $\theta_0\in(0,1]$ with
> $|\psi(\theta)|\le e^{-c_1\theta^2}$ for $|\theta|\le\theta_0$;
> (b) **(non-lattice gap)** $\kappa:=\sup_{|\theta|\ge\theta_0}|\psi(\theta)|<1$;
> (c) consequently, with $\eta:=\min\{c_1,\ \log(1/\kappa)\}>0$,
> $$
> |\psi(\theta)|\ \le\ e^{-\eta\min(\theta^2,\,1)}\qquad\text{for all }\theta\in\R;
> $$
> (d) $\psi\in L^2(\R)$, with $\|\psi\|_2^2=2\pi\!\int f^2\le 2\pi K$.

*Proof.* (a) Let $x_1'$ be an independent copy and $Y=x_1-x_1'$ the symmetrization, so
$\EE Y=0$, $\EE Y^2=2$, and $|\psi(\theta)|^2=\EE\cos(\theta Y)$. Using
$1-\cos s\ge \tfrac14 s^2$ for $|s|\le1$,
$$
1-|\psi(\theta)|^2=\EE\bigl(1-\cos\theta Y\bigr)\ \ge\ \tfrac14\theta^2\,\EE\!\left[Y^2\mathbf 1_{|\theta Y|\le 1}\right].
$$
Since $\EE Y^2=2<\infty$, choose $\theta_0\in(0,1]$ so small that
$\EE[Y^2\mathbf 1_{|Y|>1/\theta_0}]\le1$; then for $|\theta|\le\theta_0$,
$\EE[Y^2\mathbf 1_{|\theta Y|\le1}]\ge \EE[Y^2\mathbf 1_{|Y|\le 1/\theta_0}]\ge1$, whence
$1-|\psi(\theta)|^2\ge \tfrac14\theta^2$ and $|\psi(\theta)|\le(1-\tfrac14\theta^2)^{1/2}\le e^{-\theta^2/8}$.
Take $c_1=\tfrac18$. (Only finite variance is used here.)

(b) Because $f$ is a density, $x_1$ is non-lattice and $|\psi(\theta)|<1$ for every
$\theta\ne0$; moreover $f\in L^1\cap L^\infty\subset L^2$, so by Riemann–Lebesgue
$\psi(\theta)\to0$ as $|\theta|\to\infty$. Pick $\Theta$ with $|\psi|\le\tfrac12$ on
$|\theta|\ge\Theta$. On the compact annulus $\theta_0\le|\theta|\le\Theta$ the continuous
function $|\psi|$ attains a maximum, which is $<1$. Hence
$\kappa=\sup_{|\theta|\ge\theta_0}|\psi|<1$.

(c) For $|\theta|\le\theta_0\le1$: $\min(\theta^2,1)=\theta^2$ and
$|\psi(\theta)|\le e^{-c_1\theta^2}\le e^{-\eta\theta^2}$. For $\theta_0\le|\theta|\le1$:
$\min(\theta^2,1)=\theta^2\le1$, and $|\psi(\theta)|\le\kappa=e^{-\log(1/\kappa)}\le e^{-\eta}\le e^{-\eta\theta^2}$.
For $|\theta|\ge1$: $\min(\theta^2,1)=1$ and $|\psi(\theta)|\le\kappa\le e^{-\eta}$.

(d) Plancherel: $\int|\psi|^2=2\pi\int f^2\le2\pi\|f\|_\infty\int f\le2\pi K$. $\qquad\blacksquare$

**Remark (hypotheses).** Lemma A uses only **finite variance** (part a) and **absolute
continuity** (parts b,d; boundedness gives the quantitative $\|\psi\|_2^2\le2\pi K$). *No
sub-Gaussianity and no higher moments are needed.* The constants $\eta,\kappa,\|\psi\|_2$
depend on the law of $x_1$ only; since the entries are i.i.d. this is a single set of
constants. (If the entries were merely independent with a common density bound, one would need
a *uniform* non-lattice gap $\sup_j\kappa_j<1$; this is the only place i.i.d. is genuinely
used, and it is a standard hypothesis.)

---

## 4. Geometry of the coefficient frame

For the real case set $w_j=(u_j,v_j)\in\R^2$ (real $u,v$). Then for $\xi=(\xi_1,\xi_2)\in\R^2$,
$$
c_j(\xi):=\langle\xi,w_j\rangle=\xi_1u_j+\xi_2v_j,\qquad
\xi_1S_1+\xi_2S_2=\sum_j c_j(\xi)\,x_j .
$$
Two identities are immediate from $\|u\|=\|v\|=1$, $\langle u,v\rangle=\rho$:
$$
M:=\sum_{j=1}^m w_jw_j^{\!\top}=\Sigma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
\qquad
\sum_{j=1}^m c_j(\xi)^2=\xi^{\!\top}\Sigma\,\xi .
\tag{4.1}
$$
Since $\lambda_{\min}(\Sigma)=1-|\rho|\ge\kappa_0$ and $\lambda_{\max}(\Sigma)=1+|\rho|$,
$$
\sum_j c_j(\xi)^2=\xi^{\!\top}\Sigma\xi\ \ge\ \kappa_0|\xi|^2,
\qquad
\det\Sigma=1-\rho^2\ge\kappa_0 .
\tag{4.2}
$$
Delocalization gives the uniform smallness of each coefficient:
$$
|c_j(\xi)|\le |\xi|\,|w_j|\le\sqrt2\,\beta\,|\xi|,\qquad |w_j|\le\sqrt2\,\beta .
\tag{4.3}
$$

> **Lemma B (transverse pairs).** With $M=\Sigma$, $\det\Sigma\ge\kappa_0$, there exist two
> disjoint index pairs $\{p_1,q_1\}$, $\{p_2,q_2\}$ (for $m$ large) such that
> $$
> \bigl|\det[\,w_{p_i}\mid w_{q_i}\,]\bigr|\ \ge\ \Delta:=\frac{\sqrt{\kappa_0}}{m}\qquad(i=1,2).
> $$

*Proof.* Let $W=[w_1\mid\cdots\mid w_m]\in\R^{2\times m}$, so $WW^{\!\top}=\Sigma$. Cauchy–Binet
gives $\det(WW^{\!\top})=\sum_{p<q}\det[w_p\mid w_q]^2=\det\Sigma\ge\kappa_0$. As there are
$\binom m2<m^2/2$ pairs, some pair has $\det[w_p\mid w_q]^2\ge 2\kappa_0/m^2$, i.e.
$|\det|\ge\sqrt{2\kappa_0}/m\ge\Delta$. Remove that pair; the residual matrix
$\Sigma-w_{p_1}w_{p_1}^{\!\top}-w_{q_1}w_{q_1}^{\!\top}$ differs from $\Sigma$ in operator norm
by at most $2\cdot2\beta^2=4\beta^2$, so its determinant is $\ge\kappa_0-O(\beta^2)\ge\kappa_0/2$
for large $m$; repeat to get the second pair with $|\det|\ge\sqrt{\kappa_0}/m=\Delta$. $\blacksquare$

The characteristic function of $(S_1,S_2)$ factorizes:
$$
\phi_m(\xi):=\EE\,e^{i(\xi_1S_1+\xi_2S_2)}=\prod_{j=1}^m\psi\bigl(c_j(\xi)\bigr),
\qquad
\widehat{\Gamma_\Sigma}(\xi)=e^{-\frac12\xi^{\!\top}\Sigma\xi}.
\tag{4.4}
$$

---

## 5. Local central limit theorem (sup-norm), real case

> **Proposition C.** Under the standing assumptions, $(S_1,S_2)$ has a bounded continuous
> density $g_m$ and
> $$
> \varepsilon_m:=\sup_{w\in\R^2}\bigl|g_m(w)-\Gamma_\Sigma(w)\bigr|
> \ \le\ \frac1{(2\pi)^2}\int_{\R^2}\bigl|\phi_m(\xi)-\widehat{\Gamma_\Sigma}(\xi)\bigr|\,d\xi
> \ \xrightarrow[m\to\infty]{}\ 0,
> $$
> uniformly over delocalized unit $u,v$ with $|\rho|\le1-\kappa_0$.

We first establish two deterministic bounds.

### 5.1 Energy bound for the tail

> **Lemma D.** For every $\xi\in\R^2$,
> $\displaystyle F(\xi):=\sum_{j=1}^m\min\!\bigl(c_j(\xi)^2,\,1\bigr)\ \ge\ \tfrac{\kappa_0}{4}\,\min\!\bigl(|\xi|^2,\ \beta^{-2}\bigr).$

*Proof.* **(i) $|\xi|\le(\sqrt2\,\beta)^{-1}$.** By (4.3) all $|c_j(\xi)|\le1$, so by (4.2)
$F(\xi)=\sum_j c_j(\xi)^2\ge\kappa_0|\xi|^2$. Here $|\xi|^2\le\tfrac1{2}\beta^{-2}\le\beta^{-2}$,
so $F(\xi)\ge\kappa_0\min(|\xi|^2,\beta^{-2})\ge\tfrac{\kappa_0}4\min(|\xi|^2,\beta^{-2})$.

**(ii) $|\xi|>(\sqrt2\,\beta)^{-1}$.** Split $[m]$ into small/big coefficients
$\mathcal S=\{j:|c_j|\le1\}$, $\mathcal B=\{j:|c_j|>1\}$; then $F(\xi)=\sum_{\mathcal S}c_j^2+|\mathcal B|$.
If $|\mathcal B|\ge\tfrac{\kappa_0}{4}\beta^{-2}$, then $F\ge|\mathcal B|\ge\tfrac{\kappa_0}{4}\beta^{-2}$.
Otherwise, using (4.2) and $\max_jc_j^2\le2\beta^2|\xi|^2$ (4.3),
$$
\sum_{\mathcal S}c_j^2=\xi^{\!\top}\Sigma\xi-\sum_{\mathcal B}c_j^2
\ge\kappa_0|\xi|^2-|\mathcal B|\,2\beta^2|\xi|^2
>\kappa_0|\xi|^2-\tfrac{\kappa_0}{4}\beta^{-2}\,2\beta^2|\xi|^2
=\tfrac{\kappa_0}{2}|\xi|^2 ,
$$
so $F\ge\tfrac{\kappa_0}{2}|\xi|^2>\tfrac{\kappa_0}{2}\cdot\tfrac1{2}\beta^{-2}=\tfrac{\kappa_0}{4}\beta^{-2}$.
In both subcases $F\ge\tfrac{\kappa_0}{4}\beta^{-2}=\tfrac{\kappa_0}{4}\min(|\xi|^2,\beta^{-2})$
(the min equals $\beta^{-2}$ once $|\xi|^2\ge\beta^{-2}$, and equals $|\xi|^2\le\beta^{-2}$ on the
intermediate range, where the displayed bound $\ge\tfrac{\kappa_0}4\beta^{-2}\ge\tfrac{\kappa_0}4|\xi|^2$ still holds). $\blacksquare$

Combining Lemma A(c) with Lemma D,
$$
|\phi_m(\xi)|=\prod_j|\psi(c_j(\xi))|\le e^{-\eta F(\xi)}\le \exp\!\Bigl(-\tfrac{\eta\kappa_0}{4}\min(|\xi|^2,\beta^{-2})\Bigr).
\tag{5.1}
$$

### 5.2 Integrability ($\phi_m\in L^1$) via the transverse pairs

Let $Q=\{p_1,q_1,p_2,q_2\}$ from Lemma B. Bounding the $m-4$ other factors by $1$ and using
Cauchy–Schwarz over $\R^2$,
$$
\int_{\R^2}\prod_{j\in Q}|\psi(c_j(\xi))|\,d\xi
\le\Bigl(\int|\psi(c_{p_1})\psi(c_{q_1})|^2\Bigr)^{1/2}\Bigl(\int|\psi(c_{p_2})\psi(c_{q_2})|^2\Bigr)^{1/2}.
$$
For the $i$-th pair, the map $\xi\mapsto(c_{p_i}(\xi),c_{q_i}(\xi))=[w_{p_i}\mid w_{q_i}]^{\!\top}\xi$
is linear with Jacobian $|\det[w_{p_i}\mid w_{q_i}]|\ge\Delta$, so by the change of variables and
Lemma A(d),
$$
\int_{\R^2}|\psi(c_{p_i})|^2|\psi(c_{q_i})|^2\,d\xi=\frac{\|\psi\|_2^4}{|\det[w_{p_i}\mid w_{q_i}]|}\le\frac{\|\psi\|_2^4}{\Delta}.
\tag{5.2}
$$
Hence
$$
\int_{\R^2}|\phi_m(\xi)|\,d\xi\le\int_{\R^2}\prod_{j\in Q}|\psi(c_j(\xi))|\,d\xi\le\frac{\|\psi\|_2^4}{\Delta}\le\frac{m\,\|\psi\|_2^4}{\sqrt{\kappa_0}}<\infty .
\tag{5.3}
$$
Thus $\phi_m\in L^1(\R^2)$. Fourier inversion is valid: $g_m(w)=(2\pi)^{-2}\int e^{-i\langle\xi,w\rangle}\phi_m(\xi)\,d\xi$
is a bounded continuous function, and it is the density of $(S_1,S_2)$. The displayed
$\varepsilon_m$ bound in Proposition C then follows because both $g_m$ and $\Gamma_\Sigma$ are
inverse transforms of $L^1$ functions ($\widehat{\Gamma_\Sigma}\in L^1$ since
$\det\Sigma\ge\kappa_0$).

### 5.3 The comparison integral $\to0$

Fix $\varepsilon>0$. Write $\int_{\R^2}|\phi_m-\widehat{\Gamma_\Sigma}|=\mathrm{I}+\mathrm{II}+\mathrm{III}$ over
$\{|\xi|\le R\}$, $\{R<|\xi|\le\beta^{-1}\}$, $\{|\xi|>\beta^{-1}\}$, for a constant $R$ to be
fixed.

**Term over $\{|\xi|>R\}$ from the Gaussian.** $\int_{|\xi|>R}\widehat{\Gamma_\Sigma}=\int_{|\xi|>R}e^{-\frac12\xi^{\!\top}\Sigma\xi}\le\int_{|\xi|>R}e^{-\frac{\kappa_0}2|\xi|^2}d\xi$,
which is $\le\varepsilon$ once $R=R(\kappa_0,\varepsilon)$ is large. Fix such $R$.

**(I) Fixed ball $|\xi|\le R$: quadratic expansion.** By Lemma A's hypotheses,
$\psi(\theta)=1-\tfrac12\theta^2+\theta^2\omega(|\theta|)$ with $\omega(s)\to0$ as $s\to0$
(the standard expansion for finite second moment; one fixed $\omega$ since the entries are
i.i.d.). For $|\xi|\le R$, (4.3) gives $\max_j|c_j(\xi)|\le\sqrt2\,\beta R\to0$, so each
$\psi(c_j)$ is within $O(\beta^2R^2)$ of $1$ and
$$
\log\psi(c_j(\xi))=-\tfrac12 c_j(\xi)^2+c_j(\xi)^2\,\omega^*(\sqrt2\beta R),
$$
where $\omega^*(s)\to0$ absorbs $\omega$ and the $\log(1+\cdot)$ error. Summing and using (4.1),
$$
\log\phi_m(\xi)=-\tfrac12\xi^{\!\top}\Sigma\xi+E_m(\xi),\qquad
|E_m(\xi)|\le\omega^*(\sqrt2\beta R)\sum_j c_j(\xi)^2=\omega^*(\sqrt2\beta R)\,\xi^{\!\top}\Sigma\xi\le 2R^2\,\omega^*(\sqrt2\beta R).
$$
Since $\beta=m^{-1/2+\delta}\to0$, $\sup_{|\xi|\le R}|E_m(\xi)|\to0$, hence
$\sup_{|\xi|\le R}|\phi_m(\xi)-\widehat{\Gamma_\Sigma}(\xi)|\to0$ and
$\mathrm{I}\le\pi R^2\sup_{|\xi|\le R}|\phi_m-\widehat{\Gamma_\Sigma}|\to0$. (Only $\beta\to0$ is used;
this is where delocalization makes the quadratic term dominate.)

**(II) Moderate tail $R<|\xi|\le\beta^{-1}$.** Here $\min(|\xi|^2,\beta^{-2})=|\xi|^2$, so by (5.1)
$|\phi_m(\xi)|\le e^{-\frac{\eta\kappa_0}{4}|\xi|^2}$, and with the Gaussian term,
$$
\mathrm{II}\le\int_{|\xi|>R}\Bigl(e^{-\frac{\eta\kappa_0}{4}|\xi|^2}+e^{-\frac{\kappa_0}{2}|\xi|^2}\Bigr)d\xi\ \le\ \varepsilon
$$
once $R$ is large (independently of $m$); enlarge the earlier $R$ if necessary.

**(III) Far tail $|\xi|>\beta^{-1}$.** The Gaussian part is $\le\int_{|\xi|>\beta^{-1}}e^{-\frac{\kappa_0}2|\xi|^2}\to0$.
For $\phi_m$, split off $Q$ as in §5.2: the remaining $m-4$ indices have second-moment matrix
with $\lambda_{\min}\ge\kappa_0/2$ (Lemma B proof), so Lemma D applied to them gives, for
$|\xi|>\beta^{-1}$,
$$
\sum_{j\notin Q}\min(c_j^2,1)\ \ge\ \tfrac{\kappa_0/2}{4}\min(|\xi|^2,\beta^{-2})=\tfrac{\kappa_0}{8}\beta^{-2}.
$$
Therefore, using Lemma A(c) on $j\notin Q$ and then (5.2)–(5.3) on $j\in Q$,
$$
\int_{|\xi|>\beta^{-1}}|\phi_m(\xi)|\,d\xi
\le e^{-\frac{\eta\kappa_0}{8}\beta^{-2}}\int_{\R^2}\prod_{j\in Q}|\psi(c_j(\xi))|\,d\xi
\le e^{-\frac{\eta\kappa_0}{8}\,m^{1-2\delta}}\cdot\frac{m\,\|\psi\|_2^4}{\sqrt{\kappa_0}}\ \to\ 0 .
$$
So $\mathrm{III}\to0$.

Combining, $\limsup_m\int|\phi_m-\widehat{\Gamma_\Sigma}|\le 2\varepsilon$; as $\varepsilon$ was
arbitrary, the integral $\to0$, proving Proposition C. All thresholds and constants depend only
on $(K,\kappa_0,\delta)$, so the convergence is uniform over the stated class. $\blacksquare$

---

## 6. From the density bound to the small-ball ratio

Let $g_{1,m}$ be the density of the single form $S_1$ and $\Gamma_1$ the standard real Gaussian
density ($\Gamma_1(0)=a_1=(2\pi)^{-1/2}$, $\Gamma_1(w)=\Gamma_1(0)e^{-w^2/2}$). The **same**
argument as §5, with the single linear form $S_1=\sum_j u_jx_j$ (coefficients $u_j$,
$\sum u_j^2=1$, $|u_j|\le\beta$), yields a one-dimensional local CLT
$$
\varepsilon_m':=\sup_{w\in\R}|g_{1,m}(w)-\Gamma_1(w)|\xrightarrow[m\to\infty]{}0 .
\tag{6.1}
$$
(One needs only $\sum u_j^2=1$ in place of $\Sigma$; Lemmas A and D and the inversion go through
verbatim in dimension one. For integrability one uses **two** indices: delocalization forces at
least two substantial coefficients — since each $u_j^2\le\beta^2\to0$ while $\sum u_j^2=1$, the
two largest satisfy $u_{(1)}^2\ge1/m$ and $u_{(2)}^2\ge(1-\beta^2)/(m-1)\ge1/(2m)$ — so by
Cauchy–Schwarz $\int_\R|\phi_{1,m}|\le\int_\R|\psi(u_{(1)}\xi)\psi(u_{(2)}\xi)|\,d\xi\le
\|\psi\|_2^2/\sqrt{|u_{(1)}u_{(2)}|}<\infty$, and the far tail is controlled exactly as in §5.3(III).
The same statement holds for $S_2$.)

Write $V_t:=\mathrm{vol}_{d_\F}\{w\in\F:|w|\le t\}$, so $V_t=2t$ ($\F=\R$). Recall the Gaussian
densities are maximized at $0$, and $\Gamma_\Sigma(0)=\dfrac{\Gamma_1(0)^2}{(1-\rho^2)^{1/2}}$
(direct computation: $\Gamma_\Sigma(0)=\frac1{2\pi\sqrt{1-\rho^2}}$, $\Gamma_1(0)^2=\frac1{2\pi}$).

**Upper bound on $q$.** Using $g_m\le\Gamma_\Sigma+\varepsilon_m\le\Gamma_\Sigma(0)+\varepsilon_m$,
$$
q(t)=\int_{|w_1|\le t}\int_{|w_2|\le t}g_m(w_1,w_2)\,dw_2\,dw_1\ \le\ \bigl(\Gamma_\Sigma(0)+\varepsilon_m\bigr)\,V_t^2 .
\tag{6.2}
$$

**Lower bound on $p$.** For $|w|\le t\le1$, $\Gamma_1(w)=\Gamma_1(0)e^{-w^2/2}\ge\Gamma_1(0)(1-\tfrac12t^2)$, so
$$
p(t)=\int_{|w|\le t}g_{1,m}(w)\,dw\ \ge\ \int_{|w|\le t}\bigl(\Gamma_1(w)-\varepsilon_m'\bigr)dw\ \ge\ \Bigl(\Gamma_1(0)(1-\tfrac12 t^2)-\varepsilon_m'\Bigr)V_t .
\tag{6.3}
$$

**Assembly.** Since $\Gamma_1(0)$ is a fixed positive constant and $1-|\rho|^2\ge\kappa_0$ keeps
$\Gamma_\Sigma(0)\in[\Gamma_1(0)^2,\ \Gamma_1(0)^2\kappa_0^{-1/2}]$ bounded, both
$\varepsilon_m/\Gamma_\Sigma(0)\to0$ and $\varepsilon_m'/\Gamma_1(0)\to0$ uniformly. With $t\to0$,
(6.2)/(6.3) give
$$
\frac{q(t)}{p(t)^2}\ \le\ \frac{(\Gamma_\Sigma(0)+\varepsilon_m)\,V_t^2}{\bigl(\Gamma_1(0)(1-\tfrac12 t^2)-\varepsilon_m'\bigr)^2 V_t^2}
=\frac{\Gamma_\Sigma(0)}{\Gamma_1(0)^2}\bigl(1+o(1)\bigr)
=\frac{1+o(1)}{\sqrt{1-\rho^2}} .
$$
This is the Lemma for $\F=\R$. $\blacksquare$

**Remark (exact match to the Gaussian source).** Tracking constants,
$q(t)\le(\Gamma_\Sigma(0)+o(1))V_t^2=\bigl(\tfrac1{2\pi\sqrt{1-\rho^2}}+o(1)\bigr)(2t)^2=\frac{2t^2}{\pi\sqrt{1-\rho^2}}(1+o(1))$,
identical to the source's conditional estimate $q\le 2t^2/(\pi s)$, $s=\sqrt{1-\rho^2}$. Likewise
$p(t)=\sqrt{2/\pi}\,t\,(1+o(1))$, matching $p_\R(t)=\sqrt{2/\pi}\,t+O(t^3)$.

---

## 7. Where this sits in the assembly; the regime $|\rho|\to1$

In the second-moment proof (source Prop. `prop:upper`), a pair of row-sets $S,T$ with overlap
$D=m-|S\cap T|$ produces two random normals $u_S,u_T$ whose Hermitian overlap is some
$\rho=\rho(S,T)$. The Lemma supplies, **for each fixed pair of (incompressible) normals**, the
conditional bound
$$
q(t)\ \le\ (1+o(1))\,\frac{p(t)^2}{(1-|\rho|^2)^{d_\F/2}} .
$$
Averaging $(1-|\rho|^2)^{-d_\F/2}$ over the law of the random normals reproduces the source's
factor $1+C/D$ (there $\EE(1-\rho^2)^{-1/2}=1+O(1/D)$ over Haar lines, resp.
$\EE(1-|\rho|^2)^{-1}=\frac{D-1}{D-2}$). That averaging is **not** part of this Lemma; it is the
downstream step, and it requires the non-Gaussian input that the normals are delocalized
(incompressible) and that their overlap is $O(D^{-1/2})$ — the separate ingredients listed in
`prob:pc`. The Lemma is exactly the "two-projection local CLT" called for there.

**Validity in $\rho$.** Everything above is uniform for $|\rho|\le1-\kappa_0$, any fixed
$\kappa_0>0$; the constants ($R$, the tail rates, the bounds on $\Gamma_\Sigma(0)$) blow up as
$\kappa_0\downarrow0$. The complementary regime $|\rho|\to1$ corresponds to **small $D$**
(high-overlap row pairs, e.g. $D=2$ where the two normals may coincide). As in the Gaussian
proof, those pairs are handled **separately by combinatorics** together with the trivial,
always-valid bound
$$
q(t)\le\PP\{|S_1|\le t\}=p(t),
$$
not by this Lemma. (In the source this is the $D=2$ term, controlled by
$\PP\{D=2\}\,p(t)^{-1}$ being exponentially small.)

---

## 8. Complex case ($\F=\C$)

Everything transfers by realification $\C\simeq\R^2$, $\C^2\simeq\R^4$; we list the changes.

- **Entry CF.** $\psi_\C(\zeta)=\EE\exp(i\,\mathrm{Re}(\bar\zeta x_1))$, $\zeta\in\C$, is the
  $\R^2$-Fourier transform of the entry density $f_\C\le K$. Lemma A holds with $\theta^2$
  replaced by $|\zeta|^2$: by symmetrization, $|\psi_\C(\zeta)|^2=\EE\cos(\mathrm{Re}(\bar\zeta Y))$
  with $\EE\,\mathrm{Re}(\bar\zeta Y)^2=|\zeta|^2$ (properness: $\EE Y^2=0$, $\EE|Y|^2=2$), giving
  $|\psi_\C(\zeta)|\le e^{-c_1|\zeta|^2}$ for small $|\zeta|$; non-lattice in $\R^2$ and
  Riemann–Lebesgue give the gap $\kappa<1$; hence
  $|\psi_\C(\zeta)|\le e^{-\eta\min(|\zeta|^2,1)}$ and $\|\psi_\C\|_{L^2(\R^2)}^2\le(2\pi)^2K\!\int\! f_\C^2\le CK$.
- **Frame.** For $\xi=(\xi_1,\xi_2)\in\C^2$, $c_j(\xi)=\xi_1u_j+\xi_2v_j\in\C$,
  $\sum_j|c_j(\xi)|^2=\xi^{*}\Sigma\,\xi$ with $\Sigma=\begin{psmallmatrix}1&\rho\\\bar\rho&1\end{psmallmatrix}$
  Hermitian; as a real quadratic form on $\R^4$ its eigenvalues are $1\pm|\rho|$ (each doubled),
  so $\lambda_{\min}=1-|\rho|\ge\kappa_0$ and $\det_\R=(1-|\rho|^2)^2$. Also
  $|c_j(\xi)|\le\sqrt2\,\beta|\xi|$ and $\det\Sigma=1-|\rho|^2\ge\kappa_0$.
- **Transverse pairs (Lemma B).** Complex Cauchy–Binet on $W=[\binom{u_j}{v_j}]_j\in\C^{2\times m}$,
  $WW^{*}=\Sigma$: $\sum_{p<q}|\det_\C[\binom{u_p}{v_p}\mid\binom{u_q}{v_q}]|^2=\det\Sigma\ge\kappa_0$,
  so two disjoint $\C$-basis pairs with $|\det_\C|\ge\sqrt{\kappa_0}/m$ exist. The change of
  variables $\xi\mapsto(c_{p}(\xi),c_{q}(\xi))$ on $\R^4$ has Jacobian $|\det_\C|^2\ge\kappa_0/m^2$,
  so (5.2) becomes $\int_{\R^4}|\psi_\C(c_p)|^2|\psi_\C(c_q)|^2=\|\psi_\C\|_2^4/|\det_\C|^2\le m^2\|\psi_\C\|_2^4/\kappa_0$;
  thus $\phi_m\in L^1(\R^4)$ with $\|\phi_m\|_1\le m^2\|\psi_\C\|_2^4/\kappa_0<\infty$.
- **Lemma D** holds verbatim ($F(\xi)=\sum_j\min(|c_j(\xi)|^2,1)\ge\tfrac{\kappa_0}4\min(|\xi|^2,\beta^{-2})$,
  same proof). The far-tail bound gives $\le e^{-\frac{\eta\kappa_0}8 m^{1-2\delta}}\cdot m^2\|\psi_\C\|_2^4/\kappa_0\to0$.
- **Quadratic term.** $\psi_\C(\zeta)=1-\tfrac14|\zeta|^2+o(|\zeta|^2)$ (properness makes the
  quadratic isotropic), and the proper-complex Gaussian limit has
  $\widehat{\Gamma_\Sigma^\C}(\xi)=e^{-\frac14\xi^{*}\Sigma\xi}$; summing the per-entry expansions
  reproduces it. The Fourier space is $\R^4$, $(2\pi)^2\to(2\pi)^4$ in inversion.

Hence $\sup_{w\in\C^2}|g_m(w)-\Gamma_\Sigma^\C(w)|\to0$, with
$\Gamma_\Sigma^\C(0)=\dfrac1{\pi^2(1-|\rho|^2)}$ and single-form density at $0$ equal to
$a_2=\Gamma_1^\C(0)=\tfrac1\pi$ (standard proper complex Gaussian $\tfrac1\pi e^{-|w|^2}$). With
$V_t=\pi t^2$, the §6 conversion gives
$$
q(t)\le(\Gamma_\Sigma^\C(0)+o(1))V_t^2=\Bigl(\tfrac1{\pi^2(1-|\rho|^2)}+o(1)\Bigr)(\pi t^2)^2=\frac{t^4}{1-|\rho|^2}(1+o(1)),
\qquad p(t)=t^2(1+o(1)),
$$
so
$$
\frac{q(t)}{p(t)^2}\le\frac{\Gamma_\Sigma^\C(0)}{\Gamma_1^\C(0)^2}(1+o(1))=\frac{1+o(1)}{1-|\rho|^2}.
$$
These match the source's complex conditional bound $q\le t^4/(1-|\rho|^2)$ and
$p_\C(t)=t^2+O(t^4)$. $\blacksquare$

---

## 9. Summary of what is used, and risks

- **Proved:** the boxed inequality, for both $\F=\R$ and $\F=\C$, uniformly for
  $|\rho|\le1-\kappa_0$ and $t=t_m\to0$ ($0<t\le1$), with the *exact* Gaussian constants
  $1/\sqrt{1-\rho^2}$ resp. $1/(1-|\rho|^2)$.
- **Characteristic-function bound used:** $|\psi(\theta)|\le e^{-\eta\min(\theta^2,1)}$
  (Lemma A(c)), proved from finite variance (small $\theta$) + absolute continuity / non-lattice
  gap (large $\theta$), with $\psi\in L^2$ from the density bound.
- **Hypotheses actually needed:** mean $0$, **variance $1$** (proper for $\F=\C$), **bounded
  density** $\le K$, and **delocalization** $\|u\|_\infty,\|v\|_\infty\to0$ (the rate
  $m^{-1/2+\delta}$ only quantifies the error as $e^{-c\,m^{1-2\delta}}$). **Sub-Gaussianity is
  not needed** for this Lemma. The i.i.d. assumption is used only to have a single non-lattice
  gap $\kappa<1$ (Lemma A(b)); independent entries with a *uniform* gap would suffice.
- **Where delocalization enters:** (i) §5.3(I), $\max_j|c_j(\xi)|\le\sqrt2\beta|\xi|\to0$ makes the
  quadratic Taylor term dominate on the fixed ball — without it $(S_1,S_2)$ need not be
  asymptotically Gaussian; (ii) Lemma D / §5.3(III), $\beta\to0$ pushes the CF-saturation scale
  $\beta^{-1}\to\infty$, making the far tail super-exponentially small.
- **Regime in $\rho$:** uniform for $|\rho|\le1-\kappa_0$; the case $|\rho|\to1$ (small overlap
  codimension $D$) is *not* covered and is handled in the assembly by combinatorics plus the
  trivial $q(t)\le p(t)$, exactly as in the Gaussian source's $D=2$ treatment.
- **References:** the argument is self-contained; it is the Esseen/Fourier-inversion route to a
  multivariate local limit theorem for densities. Standard background: Petrov, *Sums of
  Independent Random Variables* (Ch. VII, local theorems); Bhattacharya–Rao, *Normal
  Approximation and Asymptotic Expansions* (Thm. 19.1, densities); Bobkov,
  *Closeness of probability distributions in terms of Fourier–Stieltjes transforms* / local-CLT
  papers — for the i.i.d. delocalized-coefficient case the self-contained proof above is cleaner
  than invoking a black-box theorem, since the black-box hypotheses are precisely the
  CF-integrability facts established in §5.
- **Biggest risk / caveat.** The one non-elementary step is the **far-tail integrability**
  ($|\xi|>\beta^{-1}$): the bound $|\psi|\le e^{-\eta}$ there does *not* by itself give
  $\phi_m\in L^1$, and a naive "$|\phi_m|\le e^{-\eta F}$" argument fails because $F$ saturates.
  It is closed here by the transverse-pair Cauchy–Schwarz bound (§5.2), which needs
  $\psi\in L^2$ (bounded density) and a quantitatively transverse pair ($|\det|\gtrsim1/m$ from
  Cauchy–Binet, Lemma B). If one tried to weaken "bounded density" to "non-lattice with finite
  variance," this step would break (no $L^2$ control), and only a *smoothed* small-ball bound
  (Beurling–Selberg majorant) would survive — losing the sharp constant. So bounded density is
  the right hypothesis and is used essentially, but only here and in Lemma A(d). A secondary
  caveat is the uniform non-lattice gap if one drops i.i.d.; with i.i.d. entries there is no
  issue.
```
