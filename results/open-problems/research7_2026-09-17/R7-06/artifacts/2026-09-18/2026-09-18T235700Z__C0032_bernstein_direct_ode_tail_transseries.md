# C0032 — Bernstein/Stieltjes structure, a direct radial ODE for rational index, and the all-orders far-tail transseries

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), arXiv:1109.3343v4, heavy-tailed limiting law `mu_alpha`; underlying scalar law: Charles Bordenave, Pietro Caputo and Djalil Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011), arXiv:1006.1713v5.

Status: theorem-sized **PARTIAL / OPEN** progress.  This artifact does not claim source-level closure or novelty.  It continues the exact global parameterization and Mellin transform established in the two preceding R7-06 runs.  The frozen campaign metric `M_jet` was already saturated at `+infinity`, so the present source-relevant global progress is honestly `M_jet: +infinity -> +infinity`.

Source check, 2026-09-18 UTC: arXiv:1006.1713 remains v5 (14 October 2011) and arXiv:1109.3343 remains the survey source.  Bounded searches for a corrigendum to the heavy-tail density theorem, a later all-radius closed form, and a later source-matching solution did not expose one.  This is negative evidence only.  The preceding run's proposed correction of the printed far-tail exponent remains an R7-06 derivation pending independent audit.

## 1. Established starting equations

Put

\[
\beta=\alpha/2\in(0,1),\qquad
c_\beta=\Gamma(1-\beta),\qquad
C_\beta=\Gamma(1-\beta)\Gamma(1+\beta).
\]

Let `S,S'` be iid positive beta-stable variables in the Bordenave--Caputo--Chafai normalization

\[
\mathbb E e^{-tS}=\exp[-c_\beta t^\beta].
\tag{1.1}
\]

Write

\[
r=|z|^2,\qquad Y(r)=y_*(r)^2,
\]

and define the ratio coordinate and one scalar transform

\[
a=\frac r{Y(r)},\qquad
F(a)=\mathbb E(S'+a/S)^{-\beta}.
\tag{1.2}
\]

The previous R7-06 work proved the exact global elimination

\[
Y(a)=F(a)^{1/\beta},\qquad
r(a)=aF(a)^{1/\beta},\qquad
r(a)^\beta=a^\beta F(a),
\tag{1.3}
\]

with `a -> r(a)` a smooth strictly increasing bijection of `[0,infinity)`.

The Mellin transform is

\[
\boxed{
\widehat F(s):=\int_0^\infty a^{s-1}F(a)\,da
=c_\beta^{-1+2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}
{\Gamma(1+\beta)\Gamma(1-s)}
}
\tag{1.4}
\]

for `0<Re s<beta`.

For the squared-radius CDF

\[
M(r)=\mu_\alpha\{|z|^2\le r\},\qquad Q(r)=1-M(r),
\]

the preceding run proved the exact one-transform identity

\[
\boxed{Q(r(a))=C_\beta F(a).}
\tag{1.5}
\]

It also proved the leading far-tail expansion

\[
F(a)=a^{-\beta}(\beta\log a+\eta_\beta)+o(a^{-\beta}),
\tag{1.6}
\]

where

\[
\eta_\beta=-2\gamma_E-2\log\Gamma(1-\beta)
-\beta\{\psi(\beta)+\psi(1-\beta)\}.
\tag{1.7}
\]

The present run attacks the remaining inversion problem by three different Section-B moves: **B1 change category**, **B12 find what is conserved**, and **B29 add the points at infinity**.

---

## 2. B1 — change category: the radial CDF is governed by Stieltjes and complete-Bernstein functions

The idea is to stop viewing `F` merely as a stable-law expectation and instead place the exact CDF transform in a rigid analytic function class.

Let

\[
T=SS'>0.
\]

The preceding CDF calculation gives

\[
Q(r(a))=\mathbb E\frac{T}{a+T}.
\tag{2.1}
\]

For this section abbreviate

\[
q(a):=Q(r(a)),\qquad m(a):=M(r(a))=1-q(a).
\]

### Theorem 2.1 — exact Stieltjes/CBF classification

For every `0<beta<1`:

1. `q` is a Stieltjes function and
   \[
   q(a)=\int_{(0,\infty)}\frac{\nu(dt)}{a+t},
   \qquad \nu(dt)=t\,\mathbb P(T\in dt).
   \tag{2.2}
   \]
2. `m` is a complete Bernstein function.
3. The CDF odds
   \[
   h(a):=\frac{m(a)}{q(a)}=\frac1{q(a)}-1
   \tag{2.3}
   \]
   is also a complete Bernstein function, with `h(0)=0` and `h(infinity)=infinity`.
4. The spectral law is exactly reconstructed from this single CBF by
   \[
   \boxed{
   M(r(a))=\frac{h(a)}{1+h(a)},\qquad
   Q(r(a))=\frac1{1+h(a)},
   }
   \tag{2.4}
   \]
   and
   \[
   \boxed{
   r(a)^\beta=\frac{a^\beta}{C_\beta(1+h(a))}.
   }
   \tag{2.5}
   \]

#### Proof

From (2.1),

\[
q(a)=\mathbb E\frac{T}{a+T}
=\int_{(0,\infty)}\frac{t}{a+t}\,\mathbb P(T\in dt).
\]

Thus (2.2) holds with `nu(dt)=t P(T in dt)`.  The Stieltjes integrability condition is automatic:

\[
\int\frac{\nu(dt)}{1+t}
=\mathbb E\frac{T}{1+T}<1.
\]

In particular `q` extends holomorphically to `C \ (-infinity,0]`, is positive on `(0,infinity)`, and maps the upper half-plane into the lower half-plane.  Directly,

\[
(-1)^n q^{(n)}(a)
=n!\,\mathbb E\frac{T}{(a+T)^{n+1}}>0
\tag{2.6}
\]

for every `n>=0`.

Next,

\[
\frac{m(a)}a
=\mathbb E\frac1{a+T}
\tag{2.7}
\]

is Stieltjes.  The standard analytic characterization of complete Bernstein functions says that a nonnegative function `f` is CBF exactly when `f(a)/a` is Stieltjes.  Hence `m` is CBF.

Since `q` maps the upper half-plane into the lower half-plane and never vanishes there, `1/q` maps the upper half-plane into itself.  Subtracting the real constant `1` preserves that half-plane mapping.  For real `a>0`, `0<q(a)<1`, so

\[
h(a)=q(a)^{-1}-1>0.
\]

The analytic characterization therefore also makes `h` a complete Bernstein function.  Since `q(0)=1`, `h(0)=0`; since `q(a)\downarrow0`, `h(a)\uparrow\infty`.  Equations (2.4) are algebraic consequences of the definition of `h`, while (1.3) and (1.5) give

\[
r^\beta=a^\beta F(a)=\frac{a^\beta q(a)}{C_\beta}
=\frac{a^\beta}{C_\beta(1+h(a))},
\]

which is (2.5).  QED.

### Theorem 2.2 — a classical-inversion obstruction

Although `h` is a CBF, its inverse is **not** a Bernstein function (hence not a complete Bernstein function) for any `0<beta<1`.

#### Proof

From (1.5)--(1.6),

\[
q(a)=C_\beta a^{-\beta}
(\beta\log a+\eta_\beta+o(1)).
\]

Therefore

\[
h(a)\sim\frac{a^\beta}{C_\beta\,\beta\log a}.
\tag{2.8}
\]

Writing `x=a^beta`, so that `beta log a=log x`, gives

\[
h(a)\sim\frac{x}{C_\beta\log x}.
\]

Asymptotic inversion yields

\[
\boxed{
 h^{-1}(t)\sim [C_\beta t\log t]^{1/\beta}.
}
\tag{2.9}
\]

Because `1/beta>1`,

\[
\frac{h^{-1}(t)}t\longrightarrow\infty.
\tag{2.10}
\]

Every Bernstein function `f` with `f(0)=0` is increasing and concave, hence `f(t)/t` is nonincreasing and in particular `f(t)=O(t)` as `t -> infinity`.  Equation (2.10) is incompatible with that property.  Thus `h^{-1}` is not Bernstein.  QED.

### B1 outcome

The category change is useful but also gives a clean no-go statement.  The complete radial CDF is controlled by a canonical CBF `h`, but **standard Bernstein-class inversion cannot be the missing closed form**: the inverse exits the Bernstein hierarchy because of its superlinear regular variation.  Any explicit all-alpha inverse must use a larger class or an independent structural identity.

---

## 3. B12 — find what is conserved: a Mellin shift yields a finite direct ODE for every rational beta

The Mellin transform (1.4) has an exact shift symmetry whenever `beta` is rational.  This produces a differential equation without the PWIT fixed point, without the auxiliary ratio parameter, and without a stable-law expectation.

Write

\[
\beta=\frac pq\in(0,1),\qquad \gcd(p,q)=1.
\tag{3.1}
\]

### 3.1 Exact shift identity

From (1.4), using `p/beta=q`,

\[
\frac{\widehat F(s+p)}{\widehat F(s)}
=(-1)^p(\beta c_\beta)^{2q}
\frac{\prod_{j=0}^{p-1}(s+j)^2}
{\prod_{k=0}^{q-1}(s+\beta k)^2}.
\tag{3.2}
\]

Indeed:

\[
\frac{\Gamma(s+p)}{\Gamma(s)}
=\prod_{j=0}^{p-1}(s+j),
\]

\[
\frac{\Gamma(1-s)}{\Gamma(1-s-p)}
=(-1)^p\prod_{j=0}^{p-1}(s+j),
\]

and

\[
\frac{\Gamma(1-(s+p)/\beta)}{\Gamma(1-s/\beta)}
=(-1)^q\frac{\beta^q}{\prod_{k=0}^{q-1}(s+\beta k)}.
\]

The last ratio is squared, so its sign disappears.

Define the Euler operator

\[
D_a=a\frac d{da},
\]

and the two polynomial differential operators

\[
P_p(D)=\prod_{j=0}^{p-1}(D-j)^2,
\qquad
R_{p,q}(D)=\prod_{k=0}^{q-1}(D+p-\beta k)^2.
\tag{3.3}
\]

Under the Mellin convention (1.4), `D_a` acts as multiplication by `-s`, while multiplication by `a^p` shifts the Mellin argument by `p`.  Equation (3.2) is therefore exactly equivalent to

\[
\boxed{
P_p(D_a)F
=(-1)^p\frac{a^p}{(\beta c_\beta)^{2q}}
R_{p,q}(D_a)F.
}
\tag{3.4}
\]

This is the differential equation underlying the rational-index Meijer-G formula from the preceding run, now derived directly from the conserved Mellin shift.

### 3.2 Eliminate `a`: a direct nonlinear ODE for the radial tail

The point of B12 is not merely to recover the Meijer-G equation.  We can eliminate `a` itself.

Let

\[
\mathcal D=r\frac d{dr},\qquad
\sigma(r)=\mathcal D\log Q(r).
\]

Set

\[
L=\frac{d\log r}{d\log a}.
\]

From

\[
r=a\left(\frac{Q(r)}{C_\beta}\right)^{1/\beta},
\]

differentiation with respect to `log a` gives

\[
L=1+\frac{\sigma}{\beta}L,
\]

hence

\[
\boxed{L=\frac\beta{\beta-\mathcal D\log Q}.}
\tag{3.5}
\]

Thus on every function pulled back from the radial variable,

\[
D_a=\mathscr A_Q,
\qquad
\boxed{
\mathscr A_Q:=
\frac\beta{\beta-\mathcal D\log Q}\,\mathcal D.
}
\tag{3.6}
\]

Also, from `r^beta=a^beta Q/C_beta`, raising to the `q`th power gives

\[
\boxed{a^p=r^p\left(\frac{C_\beta}{Q}\right)^q.}
\tag{3.7}
\]

Because `F=Q/C_beta`, the constant `C_beta` cancels from the differential operators in (3.4).  Substituting (3.6)--(3.7) yields the direct radial equation

\[
\boxed{
P_p(\mathscr A_Q)Q
=(-1)^p\Lambda_\beta\,r^pQ^{-q}
R_{p,q}(\mathscr A_Q)Q,
}
\tag{3.8}
\]

where

\[
\boxed{
\Lambda_\beta
=\frac{C_\beta^q}{(\beta c_\beta)^{2q}}
=\left(\frac{\Gamma(\beta)}
{\beta\Gamma(1-\beta)}\right)^q.
}
\tag{3.9}
\]

Equation (3.8) contains **no** `y_*`, **no** auxiliary parameter `a`, and **no** stable expectation.  It is a finite-order nonlinear ODE in the source variable `r=|z|^2` for every rational `beta`.

The natural origin data are explicit.  First,

\[
Q(0)=1.
\tag{3.10}
\]

Let

\[
m_u=\mathbb E S^{-u}
=\frac{\Gamma(1+u/\beta)}
{\Gamma(1+u)c_\beta^{u/\beta}}.
\]

Differentiating `F` at zero and using

\[
\beta C_\beta m_{\beta+1}=m_1
\]

gives

\[
\boxed{
Q'(0)=-m_1^2 C_\beta^{1/\beta}.
}
\tag{3.11}
\]

All higher finite origin derivatives are already explicit Gamma expressions by the saturated `M_jet=+infinity` theorem from the preceding run, so (3.8) comes with an explicit full formal germ at the origin.

### 3.3 Exact alpha=1 specialization

For `beta=1/2`, `(p,q)=(1,2)` and

\[
\Lambda_{1/2}=4.
\]

Equation (3.8) becomes

\[
\boxed{
\mathscr A_Q^2Q
=-4rQ^{-2}
(\mathscr A_Q+1)^2
(\mathscr A_Q+\tfrac12)^2Q.
}
\tag{3.12}
\]

This is a direct fourth-order nonlinear equation for the squared-radius tail in the alpha=1 heavy-tailed circular law.  It is exactly compatible with the previously derived Struve/Bessel parameterization; no probabilistic fixed-point variable appears in (3.12).

### B12 outcome

For **every rational alpha/2**, the source law now has both a standard Meijer-G parameterization and a finite direct radial ODE.  The remaining obstacle is not a hidden PWIT recursion in the rational cases: it is the analytic inversion / acceptable-explicitness question and, for irrational beta, the absence of a finite Mellin shift.

---

## 4. B29 — add the point at infinity: the complete far-tail transseries

The previous run extracted only the first right-hand Mellin pole at `s=beta`.  The entire pole lattice of (1.4) can be read, and infinity becomes a regular transseries boundary after compactification.

### 4.1 Pole lattice and resonance

The right-half-plane singularities of `widehat F` occur at

\[
s=n\beta,\qquad n=1,2,3,\ldots,
\tag{4.1}
\]

from `Gamma(1-s/beta)^2`.

Ordinarily these are double poles.  If

\[
n\beta=m\in\mathbb N,
\tag{4.2}
\]

then `1/Gamma(1-s)` has a simple zero and lowers the pole to first order.  For rational `beta=p/q`, this resonance occurs periodically, exactly when `q | n`.

For a nonresonant index `n` define

\[
\boxed{
A_n=
\frac{\beta^2 c_\beta^{2n-1}\Gamma(n\beta)}
{\Gamma(1+\beta)\Gamma(1-n\beta)((n-1)!)^2}
}
\tag{4.3}
\]

and

\[
\boxed{
B_n=-A_n\left[
\psi(n\beta)+\psi(1-n\beta)
+\frac2\beta\{\gamma_E-H_{n-1}+\log c_\beta\}
\right],
}
\tag{4.4}
\]

where `H_0=0`.

At a resonant `n` with `m=n beta` a positive integer define

\[
\boxed{
C_n=(-1)^{m+1}
\frac{\beta^2c_\beta^{2n-1}((m-1)!)^2}
{\Gamma(1+\beta)((n-1)!)^2}.
}
\tag{4.5}
\]

### Theorem 4.1 — all finite asymptotic orders of `F`

For any fixed right-shift line `sigma>0` that is not a pole, Mellin inversion can be moved from the fundamental strip to `Re s=sigma`.  Every pole crossed contributes its residue, and the remaining integral is `O(a^{-sigma})`.  Equivalently, for every fixed `N` and every pole-avoiding

\[
\sigma_N\in(N\beta,(N+1)\beta),
\]

one has

\[
\boxed{
\begin{aligned}
F(a)
={}&\sum_{\substack{1\le n\le N\\ n\beta\notin\mathbb N}}
 a^{-n\beta}(A_n\log a+B_n)\\
&+\sum_{\substack{1\le n\le N\\ n\beta\in\mathbb N}}
 C_n a^{-n\beta}
+O(a^{-\sigma_N}).
\end{aligned}
}
\tag{4.6}
\]

#### Proof

Near a nonresonant pole `s=n beta+epsilon`, put `h=n-1`.  The standard Gamma expansion at the negative integer `-h` gives

\[
\Gamma(1-s/\beta)
=\frac{(-1)^h}{h!}
\left[-\frac\beta\epsilon+H_h-\gamma_E+O(\epsilon)\right].
\tag{4.7}
\]

Squaring (4.7), multiplying by the analytic remainder of (1.4), and differentiating the analytic remainder logarithmically gives the Laurent coefficients (4.3)--(4.4).  Because the inverse Mellin factor is `a^{-s}`, shifting the contour right contributes minus the residue; the double pole therefore contributes

\[
a^{-n\beta}(A_n\log a+B_n).
\]

If `n beta=m` is an integer, then

\[
\frac1{\Gamma(1-s)}
=(-1)^m(m-1)!\,\epsilon+O(\epsilon^2),
\tag{4.8}
\]

which cancels one order of the double pole in (4.7).  The remaining simple-pole residue gives exactly (4.5).

Finally, Stirling's formula on any fixed vertical line gives exponential decay

\[
|\widehat F(\sigma+it)|
\le C_\sigma(1+|t|)^{K_\sigma}
 e^{-\pi|t|/\beta}.
\tag{4.9}
\]

Hence the shifted Mellin integral is absolutely controlled and is `O(a^{-sigma})`.  Repeating the shift across arbitrarily many poles proves (4.6) to every prescribed finite order.  QED.

Two exact consistency checks are built into the residue formula.  For `n=1`,

\[
A_1=\beta,\qquad B_1=\eta_\beta,
\]

which recovers (1.6) exactly.  For `beta=1/2`, `n=2` is the first resonance and

\[
\boxed{C_2=\pi/2,}
\tag{4.10}
\]

matching the next term in the exact alpha=1 Struve/Bessel expansion.

### 4.2 Compactify infinity

Introduce

\[
x=r^\beta,\qquad y=a^{-\beta}.
\tag{4.11}
\]

Because `x=a^beta F(a)=F(a)/y`, (4.6) becomes the transseries boundary equation

\[
\boxed{
x=-\log y+\eta_\beta
+\sum_{n\ge2}y^{n-1}\Phi_n(\log y),
}
\tag{4.12}
\]

understood to any fixed finite asymptotic order, where

\[
\Phi_n(\ell)=
-\frac{A_n}{\beta}\ell+B_n
\quad(n\beta\notin\mathbb N),
\tag{4.13}
\]

and

\[
\Phi_n(\ell)=C_n
\quad(n\beta\in\mathbb N).
\tag{4.14}
\]

The leading approximation is

\[
y_0=e^{\eta_\beta-x}.
\]

Finite-order asymptotic reversion of (4.12) now gives a completely recursive transseries.

### Theorem 4.2 — all-orders radial-tail transseries

For every fixed integer `N>=1` there are explicit polynomials `P_1,...,P_N`, each determined algebraically from the residue data (4.3)--(4.5), with

\[
\deg P_j\le j,
\]

such that

\[
\boxed{
y=e^{\eta_\beta-x}
\left[
1+\sum_{j=1}^N P_j(x)e^{-jx}
+O(x^{N+1}e^{-(N+1)x})
\right].
}
\tag{4.15}
\]

Consequently, since the exact identities `Q=C_beta F` and `F=xy` imply `Q=C_beta x y`, one has

\[
\boxed{
Q(r)=D_\beta x e^{-x}
\left[
1+\sum_{j=1}^N P_j(x)e^{-jx}
+O(x^{N+1}e^{-(N+1)x})
\right],
\qquad x=r^\beta,
}
\tag{4.16}
\]

where

\[
D_\beta=C_\beta e^{\eta_\beta}.
\tag{4.17}
\]

#### Proof

Substitute

\[
y=e^{\eta_\beta-x}(1+u)
\]

into the finite truncation of (4.12).  Since `e^{eta_beta-x}` is exponentially small and every `Phi_n` is at most affine in `log y`, comparison of successive powers of `e^{-x}` determines the coefficient of `u` uniquely at every order.  At order `j`, only the already determined lower-order coefficients and the pole data through `n=j+1` occur.  Products of at most `j` affine factors in `x` show inductively that the resulting coefficient is a polynomial of degree at most `j`.  The remainder in (4.6), together with `y asymp e^{-x}`, propagates to the displayed `O(x^{N+1}e^{-(N+1)x})` remainder after taking one additional Mellin term if necessary.  This proves (4.15).  Equation (4.16) follows from the exact identity `Q=C_beta x y`.  QED.

The first correction is explicit.  If `beta != 1/2` at `n=2` (more generally, if `2 beta` is not an integer),

\[
\boxed{
P_1(x)=e^{\eta_\beta}
\left[
\frac{A_2}{\beta}(x-\eta_\beta)+B_2
\right].
}
\tag{4.18}
\]

For the resonant `beta=1/2` case,

\[
P_1(x)=e^{\eta_{1/2}}C_2=2e^{-\gamma_E}.
\tag{4.19}
\]

Since `x=sqrt(r)` there, (4.16) yields the sharpened alpha=1 tail

\[
\boxed{
1-M(r)=2e^{-\gamma_E}\sqrt r\,e^{-\sqrt r}
\left[
1+2e^{-\gamma_E}e^{-\sqrt r}
+O(\sqrt r\,e^{-2\sqrt r})
\right].
}
\tag{4.20}
\]

Differentiating (4.16) term by term gives the planar density to every finite exponential order.  With `x=rho^alpha`,

\[
g_\alpha(\rho)
=\frac{\beta D_\beta}{\pi}
\rho^{\alpha-2}e^{-x}
\left[
 x-1+\sum_{j=1}^N \widetilde P_j(x)e^{-jx}
+O(x^{N+2}e^{-(N+1)x})
\right],
\tag{4.21}
\]

where each `tilde P_j` is an explicitly computable polynomial.  Its leading term reproduces the preceding run's corrected density asymptotic

\[
g_\alpha(\rho)
\sim\frac{\beta D_\beta}{\pi}
\rho^{2\alpha-2}e^{-\rho^\alpha}.
\]

### B29 outcome

The point at infinity is no longer represented by a single leading estimate.  The exact Mellin pole lattice determines **every finite far-tail order**, including a periodic resonance phenomenon for rational beta.  This makes the proposed correction of the BCC far-tail theorem substantially more rigid: both its leading rate and all subleading exponential sectors are fixed by the same exact transform.

---

## 5. What moved mathematically and what did not move metrically

The fixed metric was saturated in the preceding run:

\[
\boxed{M_{\rm jet}:+\infty\longrightarrow+\infty.}
\]

So the metric records **NO MOVEMENT** and the ordinary unchanged count becomes `1 -> 2`.  This is not a bookkeeping-only run: it adds three source-relevant global results that are independent of the origin-jet metric:

- a Stieltjes / complete-Bernstein classification of the entire radial CDF together with a proof that the inverse leaves the Bernstein class;
- a direct finite nonlinear radial ODE for every rational `alpha/2`, eliminating both the PWIT fixed-point unknown and the auxiliary parameter;
- an all-orders far-tail transseries, including exact residue formulas and rational-index resonances.

The source target is nevertheless still **PARTIAL / OPEN**.  For general irrational beta, no finite Mellin-shift ODE exists by the present route, and the monotone transform still requires inversion.  The survey's informal word “explicit” also does not specify whether a monotone Mellin-Barnes parameterization counts as full identification.  The correction of the printed far-tail exponent, though now supported by a full residue hierarchy and the exact alpha=1 certificate, still requires an independent P26 audit plus a distinct OTHER-track audit before it could enter any closure claim.

## 6. Next nonrepeating attacks

The next ordinary C0032 run, if ownership/source status remains unchanged, should not repeat B1/B12/B29 or the preceding B7/B11/B30 triple.  A useful next triple is:

- **B4 — prove something weaker completely:** isolate the rational-index source theorem as a self-contained explicit-law theorem and determine exactly what remains between it and the survey's requested identification;
- **B19 — make it an algorithm:** turn the monotone `F/a` parameterization into a certified arbitrary-alpha evaluator/inverter with a rigorous a priori error bound from Mellin tails and Stieltjes monotonicity;
- **B23 — do what the proposer did not expect:** test whether irrational beta is genuinely outside finite-order D-finite / Meijer-G closure, so that a Fox-H/Mellin-Barnes plus inverse representation may be provably maximal within classical holonomic functions.

If that next ordinary run leaves the frozen metric unchanged again, it will be the third consecutive ordinary no-movement run and the following R7-06 iteration must be the Section-I thinking-only STUCK1 diagnosis rather than another ordinary lemma run.
