# Boundary-hole monotonicity and the odd-dimensional polynomial

Status: private author-checked partial candidate. No independent review, no novelty certification, and no claim that the whole source conjecture is solved.

Source: D'Achille, Curien, Enriquez, Lyons and Unel, *Ideal Poisson--Voronoi tessellations on hyperbolic spaces*, archived as `ideal_voronoi_2023`, Proposition 5.1 and equation (5.1), PDF35; Conjecture 7.5, PDF48. The source already computes the dimension-three formula and observes rationality in odd dimensions. Those facts are credited. The claims attempted here are the all-dimensional monotonicity and positive coefficients in every odd dimension. The final addendum gives a candidate counterexample to the even-dimensional positive-power-series clause in its displayed distance variable.

## Exact starting identity

Let $n=d-1\ge1$ and let $H_d(u)$ be the probability that the hyperbolic ball of radius $u\ge0$ about the origin lies inside its ideal Voronoi cell. Write $J_d(u)=1/H_d(u)$. Equation (5.1) and Proposition 5.1 give

$$
J_d(u)=\frac1{c_d}\int_{\mathbb R^n}
\left(\sqrt{\cosh^2u+|x|^2}-\sinh u\right)^{-2n}\,dx,
\qquad
c_d=\frac{\pi^{n/2}\Gamma(n/2)}{\Gamma(n)}.
$$

The normalization follows independently by setting $u=0$ and integrating $(1+|x|^2)^{-n}$ in polar coordinates. In particular $J_d(0)=1$.

## Monotonicity in every dimension

Set $q=e^{2u}$ and substitute $x=e^{-u}z$. Then

$$
e^{-nu}J_d(u)=\frac1{c_d}\int_{\mathbb R^n}D_q(z)^{-2n}\,dz,
\qquad
D_q(z)=\sqrt{(q+1)^2/4+|z|^2}-(q-1)/2.
$$

The denominator is positive. For $z\ne0$,

$$
\frac{\partial D_q(z)}{\partial q}
=\frac{q+1}{4\sqrt{(q+1)^2/4+|z|^2}}-\frac12<0.
$$

Thus the integrand strictly increases with $q$ away from a null set. All integrals are finite by the exact source identity. Pointwise comparison of two values of $q$ proves that $e^{-nu}J_d(u)$ is strictly increasing; no interchange of differentiation and integration is needed. Taking reciprocals proves

$$
u\longmapsto e^{(d-1)u}H_d(u)
\quad\hbox{is strictly decreasing on }[0,\infty).
$$

The strictness follows because the difference of the positive finite integrands is strictly positive on a set of positive Lebesgue measure.

## Positive rational polynomial for odd dimensions

Let $d=2m+1$, so $n=2m$, with integer $m\ge1$. Put $a=e^{-u}$ and $s=\sinh u=(a^{-1}-a)/2$. In the radial integral make the substitution

$$
y=\sqrt{\cosh^2u+r^2}-s.
$$

Its lower endpoint is $a$, and

$$
r^2=(y-a)(y+a^{-1}),\qquad r\,dr=(y+s)\,dy.
$$

After setting $y=az$, the exact integral becomes

$$
J_{2m+1}(u)=C_m a^{-4m}
\int_1^\infty (z-1)^{m-1}(a^2z+1)^{m-1}
\bigl[a^2(2z-1)+1\bigr]z^{-4m}\,dz,
\qquad C_m=\frac{\Gamma(2m)}{\Gamma(m)^2}.
$$

Here the factor $C_m$ is half the ratio of the $(2m-1)$-sphere area to $c_d$. Expand the two bracketed factors as a polynomial in $a^2$. Every coefficient is a strictly positive integrable function of $z>1$: the only apparent subtraction is $2z-1$, which is positive on this domain. The degree is exactly $m$. The resulting integrals are rational because expanding $(z-1)^{m-1}$ reduces them to finite sums of powers of $z$ with integer exponents at most $-2$.

For an explicit formula, let $B$ denote the beta function, and interpret binomial coefficients outside $0,\ldots,m-1$ as zero. Define, for $0\le j\le m$,

$$
b_{m,j}=\binom{m-1}{j}B(3m-j,m)
+\binom{m-1}{j-1}\left[2B(3m-j,m)-B(3m-j+1,m)\right].
$$

This follows from $\int_1^\infty(z-1)^{m-1}z^{j-4m}\,dz=B(3m-j,m)$. All beta arguments are positive integers. Moreover $B(A+1,m)<B(A,m)$, so each displayed coefficient is positive. Hence

$$
p_m(q)=C_m\sum_{j=0}^m b_{m,j}q^{m-j}
$$

is a degree-$m$ polynomial with strictly positive rational coefficients, and

$$
H_{2m+1}(u)=\frac{e^{-2mu}}{p_m(e^{2u})}.
$$

The normalization gives $p_m(1)=1$. The first two cases are

$$
p_1(q)=\frac{q+2}{3},\qquad
p_2(q)=\frac{q^2}{7}+\frac{16q}{35}+\frac25.
$$

The first reproduces the already-known dimension-three formula in Remark 5.2. It is a control, not a newly solved special case.

## An additional odd-dimensional consequence

The polynomial representation makes $J_d(u)$ a positive sum of exponentials with rates in $[n,2n]$. Let $L=\log J_d$. Under the exponential weights, $L'$ is the mean rate and $L''$ its variance. Therefore $L'\ge n$ and $L''\le n^2/4$. The density $f=-H_d'=H_dL'$ satisfies

$$
f'=H_d\bigl(L''-(L')^2\bigr)<0.
$$

This proves the source's proposed decreasing-density property in odd dimensions. It also implies that the median is smaller than the mean. For completeness, if $M>0$ is the median and $v=f(M)>0$, convexity of the survival function gives

$$
H_d(x)\ge\max\{1/2-v(x-M),0\},\qquad x\ge0.
$$

Integrating yields $E X\ge(1/2+vM)^2/(2v)\ge M$, since the difference in the last inequality is $(vM-1/2)^2/(2v)$. Strict convexity makes the first inequality strict on a positive-length interval. The mean is finite by the source exponential tail bound.

## Adversarial checks and remaining gap

The load-bearing points to try to break are the factor from the radial Jacobian, the power $a^{-4m}$, and the distinction between polynomial positivity in $q=e^{2u}$ and power-series positivity in $u$. The check script compares the beta coefficients with an independent expansion and exact integration of the radial polynomial. It also compares the resulting formula with the original angular integral in Proposition 5.1, including even dimensions for the separate monotonicity calculation.

The even-dimensional positive-power-series assertion is not implied by monotonicity. The addendum below supplies a candidate counterexample to that clause in dimension two. No independent referee has checked this packet, and the bounded literature search is not a novelty certificate. Other even-dimensional density and median claims remain unproved here, so this grouped entry retains its partial-candidate classification.

## Addendum: a negative sixth coefficient in dimension two

Author-checked candidate counterexample, 2026-09-07. This uses the source's displayed distance variable $u$ and interprets "power series" as a convergent series in nonnegative integer powers of $u$ about zero. It makes no claim about series in a different variable.

The source's Remark 5.2, equation (5.2), credits its dimension-two formula to earlier work. We do not claim that formula as new:

$$H_2(u)=\frac{\pi}{4\arctan(e^u)\cosh^2u+2\sinh u}.$$

Conjecture 7.5 would require $H_2(u)=e^{-u}/f(u)$ with positive power-series coefficients. Thus $f$ is uniquely determined near zero by

$$f(u)=\frac{(e^u+2e^{-u}+e^{-3u})A(u)+1-e^{-2u}}{\pi},\qquad A(u)=\arctan(e^u).$$

Since $A(0)=\pi/4$ and $A'(u)=1/(2\cosh u)$,

$$A(u)=\frac\pi4+\frac u2-\frac{u^3}{12}+\frac{u^5}{48}+O(u^7).$$

Put $E(u)=e^u+2e^{-u}+e^{-3u}$. The coefficients needed for degree six are $[u^6]E=61/60$, $[u^5]E=-61/30$, $[u^3]E=-14/3$, and $[u]E=-4$. Consequently,

$$[u^6]f(u)=\frac{61}{240}+\frac1\pi\left(-\frac{61}{60}+\frac7{18}-\frac1{12}-\frac4{45}\right)=\frac{61\pi-192}{240\pi}<0.$$

The sign is exact: $\pi<22/7$ gives $61\pi-192<-2/7$. Numerically the coefficient is approximately $-0.000481242280365871$. A function analytic at zero has unique power-series coefficients, so no alternative positive-coefficient series in the same variable can represent this $f$ near zero. This contradicts the stated even-dimensional coefficient clause already at $d=2$.

### Checks and strongest alternative explanation

The coefficient was obtained by exact rational convolution using the recurrence for the reciprocal of $\cosh u$, by high-precision differentiation of the closed formula, and by Cauchy coefficient extraction directly from the original angular integral of Proposition 5.1. The last lane avoids the closed arctangent formula. Reproduction: `check_IPVT_even_coefficients.py`; receipt: `IPVT_even_coefficient_checks.json`.

The strongest interpretation risk is that the authors intended a series in another transformed variable or a different normalization. The archived conjecture writes $f(u)$ in the distance variable and specifies no alternative. The calculation refutes that literal Maclaurin-series clause; it does not refute monotonicity, the odd-dimensional formula, or every possible reformulation. A source clarification or corrected conjecture could change the disposition. The dimension-two hole formula itself is already known; novelty of this coefficient observation has not been established.
