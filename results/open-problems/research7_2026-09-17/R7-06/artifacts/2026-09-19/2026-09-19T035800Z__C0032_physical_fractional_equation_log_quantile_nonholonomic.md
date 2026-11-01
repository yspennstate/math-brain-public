Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0032 — an all-index physical fractional equation, an exact log-quantile representation, and a physical non-holonomicity theorem

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), heavy-tailed limiting law `mu_alpha`; underlying scalar characterization: Bordenave–Caputo–Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011).

Date: 2026-09-19 UTC.

Methods executed in this artifact: **B3 (prove something stronger), B18 (say it in another language), B22 (read the failures, not the successes).**

Status: **PARTIAL / OPEN**.  No source-level closure is claimed.

## 1. Recalled exact normal form

Put

\[
\beta=\alpha/2\in(0,1),\qquad
c_\beta=\Gamma(1-\beta),\qquad
C_\beta=\Gamma(1-\beta)\Gamma(1+\beta).
\]

Let `S,S'` be independent positive beta-stable variables normalized by

\[
\mathbb E e^{-tS}=\exp\{-c_\beta t^\beta\},
\]

and set `T=SS'`.  Previous R7-06 work proved the exact Stieltjes coordinate

\[
q_\beta(a)=\mathbb E\frac{T}{a+T},                                      \tag{1.1}
\]

and the physical **squared-radius** map

\[
R_\beta(a)
 =a\left(\frac{q_\beta(a)}{C_\beta}\right)^{1/\beta}.                    \tag{1.2}
\]

`R_beta` is a smooth strictly increasing bijection from `(0,infinity)` onto itself.  If

\[
Q_\beta(r):=1-\mu_\alpha\{|z|^2\le r\},
\]

then

\[
Q_\beta(R_\beta(a))=q_\beta(a),                                          \tag{1.3}
\]

and the planar radial density satisfies

\[
g_\alpha(\sqrt{R_\beta(a)})
 =-\frac{q_\beta'(a)}{\pi R_\beta'(a)}.                                  \tag{1.4}
\]

The point of this run is to remove the inverse `R_beta^{-1}` from a direct equation, then to understand exactly what kind of inverse remains when one asks for a value at a prescribed physical radius.

---

## 2. B3 — prove something stronger: a direct all-beta physical fractional-dilation equation

### 2.1 A Mellin equation with an overlap strip

The Mellin transform of `q_beta` itself is useful near the origin but its natural strip makes a beta-shift awkward.  Differentiate once in the scale variable and define the positive function

\[
f_\beta(a):=-a q_\beta'(a)
 =\mathbb E\frac{aT}{(a+T)^2}.                                           \tag{2.1}
\]

For `-1<Re(s)<beta`, Tonelli/Beta integration and the stable moment formula give

\[
\begin{aligned}
\widehat f_\beta(s)
&:=\int_0^\infty a^{s-1}f_\beta(a)\,da \\
&=\mathbb E[T^s]\int_0^\infty\frac{u^s}{(1+u)^2}\,du \\
&=c_\beta^{2s/\beta}
  \frac{\Gamma(1+s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)}.                   \tag{2.2}
\end{aligned}
\]

Indeed

\[
\mathbb E S^s
=c_\beta^{s/\beta}\frac{\Gamma(1-s/\beta)}{\Gamma(1-s)},
\qquad s<\beta,
\]

and

\[
\int_0^\infty\frac{u^s}{(1+u)^2}\,du
=\Gamma(1+s)\Gamma(1-s).
\]

Now both `s` and `s+beta` lie in the strip of (2.2) whenever

\[
-1<\Re s<0.
\]

A direct Gamma calculation yields

\[
\boxed{
\widehat f_\beta(s+\beta)
=\Psi_\beta(s)\widehat f_\beta(s),
}\qquad -1<\Re s<0,                                                       \tag{2.3}
\]

where

\[
\boxed{
\Psi_\beta(s)
=(\beta c_\beta)^2
\frac{\Gamma(1+s+\beta)\Gamma(1-s)}
{s^2\Gamma(1+s)\Gamma(1-s-\beta)}.
}                                                                        \tag{2.4}
\]

The only nontrivial simplification is

\[
\frac{\Gamma(-s/\beta)}{\Gamma(1-s/\beta)}=-\frac{\beta}{s}.
\]

### 2.2 Exact dilation-functional equation

Let

\[
A:=a\frac{d}{da}.
\]

With the Mellin convention in (2.2), `A` corresponds to multiplication by `-s`:

\[
\mathcal M[Ah](s)=-s\,\mathcal M[h](s).
\]

Also

\[
\mathcal M[a^\beta h](s)=\widehat h(s+\beta).
\]

Therefore (2.3) is exactly the nonlocal dilation equation

\[
\boxed{
\Psi_\beta(-A)f_\beta=a^\beta f_\beta,                                  \tag{2.5}
}
\]

where `Psi_beta(-A)` is defined by its Mellin multiplier (2.4) on any vertical line `-1<c<0`.  Equivalently, formally displaying the Gamma functional calculus,

\[
\Psi_\beta(-A)
=(\beta c_\beta)^2
\frac{\Gamma(1-A+\beta)\Gamma(1+A)}
{A^2\Gamma(1-A)\Gamma(1+A-\beta)}.                                     \tag{2.6}
\]

Equation (2.5) is exact; no asymptotic approximation is involved.

### 2.3 Conjugation into physical squared radius

Let

\[
D:=r\frac{d}{dr},\qquad y(r):=D\log Q_\beta(r).
\]

Differentiate (1.2) in logarithmic coordinates.  If

\[
\lambda(a):=A\log R_\beta(a),
\]

then by (1.3)

\[
\lambda
=1+\frac1\beta A\log q_\beta
=1+\frac{\lambda}{\beta}D\log Q_\beta.
\]

Hence

\[
\lambda=\frac{\beta}{\beta-y}.
\]

Thus the pullback of the dilation generator `A` to physical squared radius is the nonlinear first-order operator

\[
\boxed{
\mathscr A_Q
:=\frac{\beta}{\beta-D\log Q}\,D.                                    \tag{2.7}
}
\]

In particular

\[
f_\beta(a(r))=-\mathscr A_Q Q(r)=:F_Q(r)>0.                             \tag{2.8}
\]

Raising (1.2) to the beta power gives the exact algebraic relation

\[
a(r)^\beta=\frac{C_\beta r^\beta}{Q(r)}.                               \tag{2.9}
\]

Conjugating (2.5) by the physical change of variable and using (2.8)-(2.9) yields the promised direct equation:

\[
\boxed{
\Psi_\beta(-\mathscr A_Q)F_Q
=\frac{C_\beta r^\beta}{Q}\,F_Q,
\qquad
F_Q=-\mathscr A_QQ.                                                      \tag{2.10}
}
\]

Boundary data are

\[
Q(0)=1,\qquad Q(r)\downarrow0\quad(r\to\infty).                         \tag{2.11}
\]

**Interpretation.**  Equation (2.10) contains no PWIT variable, no stable expectation, no self-consistent `y_*`, and no explicit inverse symbol `R_beta^{-1}`.  For arbitrary beta it is nonlocal: the Gamma quotient is a Mellin/dilation multiplier.  For rational beta, repeated finite shifts collapse to the finite nonlinear ODE structure obtained in the preceding runs.  Thus the rational/irrational distinction is already visible at the operator level: rational beta closes after finitely many commensurable shifts; irrational beta retains an intrinsically fractional dilation operator.

This is stronger than merely evaluating `R_beta^{-1}` numerically, but it is **not** promoted to source closure: (2.10) is a nonlinear nonlocal physical equation, not a standard closed-form formula for `g_alpha(rho)`.

---

## 3. B18 — say it in another language: the entire radial law is a quantile of an explicit log-stable-logistic convolution

The Stieltjes factor in (1.1) has an elementary probability interpretation that makes the remaining inverse much more concrete.

Let `E_1,E_2` be independent Exp(1), independent of `S,S'`.  The ratio

\[
V:=E_1/E_2
\]

has CDF

\[
\mathbb P(V\le x)=\frac{x}{1+x},\qquad x>0.                             \tag{3.1}
\]

Define

\[
W_\beta:=SS'\frac{E_1}{E_2}=TV.                                        \tag{3.2}
\]

Conditioning on `T` gives

\[
\mathbb P(W_\beta\le a)
=\mathbb E\frac{a}{a+T}
=1-q_\beta(a).                                                          \tag{3.3}
\]

Combining (1.2)-(1.3) and (3.3) proves:

### Theorem 3.1 — exact radial quantile formula

Let `X_beta=log W_beta`, and let `K_beta(u)` be its strictly increasing quantile function, `0<u<1`.  Then the squared-radius quantile `r_beta(u)` of `mu_alpha` is

\[
\boxed{
r_\beta(u)
=C_\beta^{-1/\beta}(1-u)^{1/\beta}
\exp\{K_\beta(u)\}.                                                     \tag{3.4}
}
\]

Equivalently, since `alpha=2 beta`, the ordinary radial quantile is

\[
\boxed{
\rho_\alpha(u)
=C_\beta^{-1/\alpha}(1-u)^{1/\alpha}
\exp\{K_\beta(u)/2\}.                                                   \tag{3.5}
}
\]

**Proof.**  By (3.3), if `u=1-q_beta(a)`, then `a=exp K_beta(u)`.  Formula (1.2) gives

\[
r= a\bigl((1-u)/C_\beta\bigr)^{1/\beta},
\]

which is (3.4); taking square roots gives (3.5).  QED.

### 3.2 `X_beta` has an explicit Gamma-quotient transform

For `-1<Re(s)<beta`, independence and the stable moment formula give

\[
\boxed{
\mathbb E e^{sX_\beta}
=\mathbb E W_\beta^s
=c_\beta^{2s/\beta}
\frac{\Gamma(1-s/\beta)^2\Gamma(1+s)}{\Gamma(1-s)}.
}                                                                        \tag{3.6}
\]

Thus the characteristic function is explicitly

\[
\boxed{
\varphi_\beta(t)
=c_\beta^{2it/\beta}
\frac{\Gamma(1-it/\beta)^2\Gamma(1+it)}{\Gamma(1-it)}.
}                                                                        \tag{3.7}
\]

No self-consistent unknown appears.  Standard Fourier inversion gives the density/CDF of `X_beta`, and then (3.5) gives the complete radial quantile of `mu_alpha`.

The cumulant generating function is

\[
\kappa_\beta(s)
=\frac{2s}{\beta}\log c_\beta
 +2\log\Gamma(1-s/\beta)
 +\log\Gamma(1+s)-\log\Gamma(1-s).                                     \tag{3.8}
\]

Hence

\[
\boxed{
\mathbb E X_\beta
=\frac{2}{\beta}(\log c_\beta+\gamma_E)-2\gamma_E,                     \tag{3.9}
}
\]

and, for every integer `n>=2`,

\[
\boxed{
\operatorname{cum}_n(X_\beta)
=(n-1)!\,\zeta(n)
\left(\frac{2}{\beta^n}+(-1)^n-1\right).
}                                                                        \tag{3.10}
\]

In particular

\[
\operatorname{Var}(X_\beta)=\frac{\pi^2}{3\beta^2},                    \tag{3.11}
\]

and

\[
\operatorname{cum}_3(X_\beta)
=4\zeta(3)(\beta^{-3}-1).                                                \tag{3.12}
\]

These identities give exact shape data for the unique one-dimensional quantile obstruction.

### 3.3 Relation to recent explicit Brown-measure quantiles

A current-literature comparison is useful because it prevents a false identification.  Vladislav Kargin, *Free Compressions of R-Diagonal Random Variables and the Semigroup of Brown Measures*, J. Theoret. Probab. 39 (2026), Article 70, published 27 August 2026, defines stable R-diagonal Brown measures by the elementary radial quantile

\[
\rho(t)=\frac{t^{1/2}}{(1-t)^{\delta/2}}.
\]

That family is **not** the BCC heavy-tailed i.i.d. eigenvalue law studied here.  Kargin's stable R-diagonal family has a power-law radial edge/tail mechanism, whereas the BCC law has the stretched-exponential tail recovered below.  Formula (3.5) shows the precise analogy: the BCC law also admits a one-dimensional exact quantile formula, but the elementary term is multiplied by the quantile of the explicit log-stable-logistic convolution `X_beta`.

This comparison supplies a useful standard for what contemporary Brown-measure literature calls an explicit radial identification, but it does not by itself settle the survey's informal word “explicit.”

---

## 4. B22 — read the failures: invertibility is not the right classical-function test; holonomicity is

The preceding STUCK1 diagnosis asked whether the remaining functional inverse could belong to a standard function class.  A useful failure pattern appears in Stefan Gerhold, *Can there be an explicit formula for implied volatility?* (2012): instead of proving that no “closed form” exists, Gerhold proves the relevant inverse is not D-finite.  The same test can be carried out here, but for the **physical BCC law itself**, without making any claim about all possible notions of explicitness.

### 4.1 Re-derivation of the physical stretched-exponential scale

The Mellin representation from the preceding R7-06 work has its first right-hand singularity at `s=beta`, a double pole.  Shifting the contour across this pole gives

\[
F(a)=a^{-\beta}\{\beta\log a+\eta_\beta+o(1)\},                         \tag{4.1}
\]

and the exact CDF identity is

\[
q_\beta(a)=C_\beta F(a),\qquad
R_\beta(a)^\beta=a^\beta F(a).                                          \tag{4.2}
\]

Consequently

\[
R_\beta(a)^\beta=\beta\log a+\eta_\beta+o(1),                          \tag{4.3}
\]

and eliminating `a` yields, for some explicit `D_beta>0`,

\[
\boxed{
Q_\beta(r)
\sim D_\beta r^\beta e^{-r^\beta}
\qquad(r\to\infty).
}                                                                        \tag{4.4}
\]

The constant from the previous residue computation is

\[
D_\beta
=\frac{\Gamma(1+\beta)}{\Gamma(1-\beta)}
\exp\{-2\gamma_E-\beta[\psi(\beta)+\psi(1-\beta)]\}.                  \tag{4.5}
\]

The Mellin contour has exponential Gamma decay.  Applying any fixed number of Euler derivatives only inserts polynomial factors on the contour, so the residue expansion may be differentiated term-by-term to any prescribed finite order.  Therefore, for every fixed integer `j>=0`,

\[
\boxed{
\frac{Q_\beta^{(j)}(r)}{Q_\beta(r)}
=(-\beta)^j r^{j(\beta-1)}(1+o(1)).                                    \tag{4.6}
}
\]

For `j=0` this is interpreted as `1`.

### 4.2 Physical non-D-finiteness for irrational beta

Recall that a D-finite function satisfies a nonzero linear differential equation with polynomial coefficients.

### Theorem 4.1

If `beta` is irrational, the physical squared-radius tail `Q_beta(r)` is **not D-finite over C(r)**.

**Proof.**  Suppose

\[
\sum_{j=0}^m P_j(r)Q_\beta^{(j)}(r)=0                                  \tag{4.7}
\]

with polynomials `P_j`, not all zero.  Let `d_j=deg P_j` for nonzero `P_j`, and let `p_j` be its leading coefficient.  Divide (4.7) by `Q_beta(r)`.  By (4.6), its `j`th nonzero term is

\[
p_j(-\beta)^j r^{d_j+j(\beta-1)}(1+o(1)).                             \tag{4.8}
\]

For cancellation of the largest power of `r`, at least two exponents in (4.8) must agree.  If `i\ne j`, equality means

\[
d_i+i(\beta-1)=d_j+j(\beta-1),
\]

hence

\[
\beta-1=\frac{d_j-d_i}{i-j}\in\mathbb Q,
\]

contradicting irrationality of beta.  Thus one term has a unique maximal exponent and cannot cancel.  Contradiction.  QED.

### Corollary 4.2 — the source radial density is non-D-finite for irrational alpha

Since

\[
g_\alpha(\rho)=-\frac1\pi Q_\beta'(\rho^2),                           \tag{4.9}
\]

(4.4)-(4.6) give

\[
\boxed{
g_\alpha(\rho)
\sim \frac{\beta D_\beta}{\pi}
\rho^{4\beta-2}e^{-\rho^{2\beta}}
=\frac{\beta D_\beta}{\pi}
\rho^{2\alpha-2}e^{-\rho^\alpha}.
}                                                                        \tag{4.10}
\]

The same dominant-balance proof, now with derivative scale `rho^(alpha-1)`, shows that a polynomial-coefficient linear ODE would require equality of two exponents

\[
d_i+i(\alpha-1)=d_j+j(\alpha-1),
\]

forcing `alpha` rational.  Therefore

\[
\boxed{
\alpha\notin\mathbb Q
\quad\Longrightarrow\quad
g_\alpha(\rho)\text{ is not D-finite}.                                 \tag{4.11}
}
\]

This conclusion is stronger than saying a particular inverse-Struve notation was not found: for every irrational alpha it rules out the whole D-finite/holonomic class, which contains a large portion of the classical special functions.

It does **not** rule out D-algebraic or more general special-function representations.

### 4.3 Rational beta lies on the other side of a genuine differential-algebraic divide

Previous R7-06 work proved that `q_beta(a)` is D-finite exactly when `beta` is rational.  If

\[
\beta=p/q\in\mathbb Q\cap(0,1),
\]

then `q_beta` is D-finite, hence D-algebraic.  Formula (1.2) uses multiplication and a rational power, so `R_beta(a)` is D-algebraic on the positive branch.  The class of univariate D-algebraic functions is closed under functional inverse and composition (constructively; see B. Teguia Tabuguia, *Operations for D-Algebraic Functions*, 2023).  Therefore `R_beta^{-1}` is D-algebraic, and so are

\[
Q_\beta(r)=q_\beta(R_\beta^{-1}(r))
\]

and

\[
g_\alpha(\rho)=-\pi^{-1}Q_\beta'(\rho^2).
\]

Hence

\[
\boxed{
\beta\in\mathbb Q
\quad\Longrightarrow\quad
Q_\beta\text{ and }g_{2\beta}\text{ are D-algebraic}.                 \tag{4.12}
}
\]

At `beta=1/2` the preceding run wrote such a nonlinear ODE explicitly.  Formula (4.12) says that this is not an accident of the Struve case: every rational stable index has a finite algebraic differential equation after physical-radius inversion, even when the equation is too large to be pleasant.

For irrational beta, Theorem 4.1 rules out D-finiteness but does not settle D-algebraicity.  That is now the sharp classical-function boundary left by B22.

---

## 5. What moved mathematically, and what did not

The frozen campaign metric `M_jet` was already saturated at `+infinity`, so it cannot increase in this run.  Nevertheless three genuinely new structural statements were obtained:

1. **All-index direct physical equation.**  Equation (2.10) eliminates the explicit inverse `R_beta^{-1}` in favor of an exact Mellin/dilation Gamma multiplier acting directly on the physical squared-radius tail.
2. **Exact one-dimensional quantile model.**  Equations (3.4)-(3.10) identify the whole radial law through the quantile of `X_beta=log(SS'E_1/E_2)`, whose transform and every cumulant are explicit Gamma/zeta expressions.
3. **Physical non-holonomicity theorem.**  For irrational alpha, the actual source density `g_alpha` is not D-finite; for rational beta the physical law is D-algebraic.

These results materially narrow the meaning of the remaining source obstruction, but the source target remains **PARTIAL / OPEN** under the admission criterion.  In particular, a named all-alpha closed form in physical radius has not been produced, and no semantic decision is made that a monotone quantile or a nonlocal dilation equation automatically counts as the survey's requested “explicit” density.

## 6. Dated literature checks used in this run

Checked 2026-09-19:

- Primary source/current formulation: Bordenave–Chafaï, arXiv:1109.3343, and Bordenave–Caputo–Chafaï, arXiv:1006.1713.  A bounded fresh search did not surface a later source-matching all-radius explicit formula for this `mu_alpha`; this is negative evidence only.
- Bertrand Teguia Tabuguia, *Operations for D-Algebraic Functions*, arXiv:2304.09675 (2023): records closure of univariate D-algebraic functions under composition, functional inverse, and derivation.
- Stefan Gerhold, *Can there be an explicit formula for implied volatility?*, arXiv:1211.4978 (2012): a methodological analogue using non-D-finiteness of an inverse as an obstruction to a large classical-function class.  No theorem from that paper is imported into the BCC proof above.
- Philippe Flajolet, Stefan Gerhold, Bruno Salvy, *On the non-holonomic character of logarithms, powers, and the n-th prime function*, arXiv:math/0501379 (2005): related holonomic-obstruction methodology.  The proof of Theorem 4.1 above is self-contained and uses the BCC tail scale directly.
- Vladislav Kargin, *Free Compressions of R-Diagonal Random Variables and the Semigroup of Brown Measures*, Journal of Theoretical Probability 39, Article 70 (2026), published 2026-08-27: gives an elementary radial quantile for a different stable R-diagonal Brown-measure family.  It is not treated as a resolution of C0032.

A search miss is not a novelty certificate, and the 2026 R-diagonal paper concerns a different limiting object.

## 7. Next methods if the target remains active

This is an ordinary post-STUCK1 run.  The frozen metric does not move, so the post-STUCK1 ordinary unchanged count advances by one.  The next run should not repeat B3/B18/B22.  A useful nonrepeating triple is:

- **B9 (randomize):** exploit the exact `X_beta` representation to seek an infinite-divisibility/self-decomposability identification whose quantile may already have a canonical named inverse;
- **B13 (find what only increases):** search for a monotone differential invariant of the physical CDF that could turn the nonlocal equation (2.10) into a comparison-unique local characterization;
- **B27 (swap the quantifiers):** instead of one named formula valid for all alpha, ask whether there is one finite differential-algebraic schema uniform in rational approximants `p/q -> beta`, and identify exactly what fails in the irrational limit.

No closure audit is requested because C0032 is not closed.
