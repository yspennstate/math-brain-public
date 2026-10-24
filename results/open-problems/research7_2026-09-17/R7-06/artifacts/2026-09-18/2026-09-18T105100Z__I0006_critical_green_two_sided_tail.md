Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding model/effort selector is exposed.

# I0006 critical endpoint: the Green-average logarithm is genuine

Status: **proved restricted theorem / PARTIAL relative to canonical I0006**.  
Owner: `R7-06`, native ID `6aabe827777c8191a43330b4a87d481d`.  
Canonical claim: `operations/claims/I0006.md`.  
Primary current source: Ahmed Bou-Rabee and Christoforos Panagiotis, *Quantitative explosion and percolation of the divisible sandpile*, arXiv:2609.02829v1, especially Section 6.2.  
No publication-novelty claim is made.

## 1. Purpose

The preceding R7-06 run proved at the untreated source boundary `gamma=d/2` that, for the finite Green average

\[
S_m=\sum_{y\in\mathbb Z^d} g_m(0,y)\,\zeta(y),
\]

one has the uniform upper tail

\[
\mathbb P(S_m\le -s)
\le C\exp\!\left[-c\frac{s^{d/2}}{(\log(e+s))^{d/2-1}}\right].
\tag{1.1}
\]

That estimate fed the odometer upper bound

\[
\mathbb E u_t(0)
\le C(\log t)^{2/d}(\log\log t)^{(d-2)/d}.
\]

The open issue was whether the logarithm in (1.1) is merely a defect of the Laplace estimate. The theorem below shows that it is not: under the same two-sided regular stretched-exponential lower-tail assumption, the exponent in (1.1) is sharp whenever the time horizon is at least of order `s/log s`.

This does **not** prove that the odometer itself has the log-log correction. It proves something more precise about the obstruction: any improvement of the odometer upper bound to pure `(log t)^(2/d)` must exploit the reflected odometer term jointly with the scenery; it cannot come from a uniformly sharper lower-tail bound for the Green average alone.

## 2. Setup

Fix `d>=5` and write

\[
\gamma=\frac d2,
\qquad
q=\frac{\gamma}{\gamma-1}=\frac d{d-2}.
\tag{2.1}
\]

Let `(\zeta(y))_{y\in\mathbb Z^d}` be i.i.d. with

\[
\mathbb E\zeta(0)=0,
\qquad
0<\operatorname{Var}(\zeta(0))<\infty.
\tag{2.2}
\]

Assume that for some `s_0,c_-,C_-,c_+,C_+>0` and all `s>=s_0`,

\[
c_-e^{-C_-s^\gamma}
\le
\mathbb P(\zeta(0)\le-s)
\le
C_+e^{-c_+s^\gamma}.
\tag{2.3}
\]

Let `g_m(0,y)` denote the source's finite Green kernel. Only the standard simple-random-walk facts used in the source are needed:

1. `0<=g_m(0,y)<=G(0,y)<=C(1+|y|)^{2-d}`;
2. there exist `c_0,c_1>0` such that whenever `1<=|y|<=c_0 sqrt(m)`,
   \[
   g_m(0,y)\ge c_1|y|^{2-d};
   \tag{2.4}
   \]
3. since `d>=5`,
   \[
   \sum_y G(0,y)^2<\infty.
   \tag{2.5}
   \]

For completeness, (2.4) follows directly from the local central limit lower bound: for `r=|y|` and matching-parity times `k` in a fixed interval `[A r^2,B r^2]` contained in `[0,m)`, one has `p_k(0,y)>=c r^{-d}`; summing `Theta(r^2)` such times gives `g_m(0,y)>=c r^{2-d}`.

Define the critical rate function

\[
\Phi(s)=\frac{s^\gamma}{(\log(e+s))^{\gamma-1}}.
\tag{2.6}
\]

## 3. Main theorem

### Theorem 1 — sharp critical finite-Green lower-tail scale

There exist constants `s_1,K,c,C>0`, depending only on the law and `d`, such that for every `s>=s_1` and integer

\[
m\ge K\frac{s}{\log(e+s)},
\tag{3.1}
\]

one has

\[
\boxed{
 c\,e^{-C\Phi(s)}
 \le
 \mathbb P(S_m\le-s)
 \le
 C\,e^{-c\Phi(s)}.
}
\tag{3.2}
\]

Thus the critical logarithmic loss in the exponent is genuine for the Green average.

The upper bound is the preceding run's endpoint lemma. The new content is the matching lower bound.

## 4. B6 — deform the noncritical power sum and identify the endpoint continuously

For a stretched-exponential tail exponent `gamma_0>1`, the conjugate exponent is

\[
q(\gamma_0)=\frac{\gamma_0}{\gamma_0-1}.
\]

The radial Green `q(gamma_0)`-power sum has shell exponent

\[
d-1-(d-2)q(\gamma_0)
=
-1+\beta(\gamma_0),
\]

where

\[
\boxed{
\beta(\gamma_0)
=d-(d-2)\frac{\gamma_0}{\gamma_0-1}
=
\frac{2\gamma_0-d}{\gamma_0-1}.
}
\tag{4.1}
\]

Hence, up to fixed multiplicative constants,

\[
\sum_{1\le |y|\le R}G(0,y)^{q(\gamma_0)}
\sim
\sum_{r\le R}r^{-1+\beta(\gamma_0)}.
\tag{4.2}
\]

If `gamma_0<d/2`, then `beta<0` and the sum stays bounded. If `gamma_0>d/2`, then `beta>0` and it grows like `R^beta/beta`. At the critical point,

\[
\beta(d/2)=0,
\]

and the elementary limit

\[
\lim_{\beta\to0}\frac{R^\beta-1}{\beta}=\log R
\tag{4.3}
\]

shows that the endpoint logarithm is exactly the continuous limit of the noncritical power law. It is therefore not an algebraic accident introduced by splitting the proof at `gamma=d/2`.

Outcome of B6: **the critical logarithm is the genuine endpoint of the source's noncritical Green-power mechanism.**

## 5. B24 — solve the finite-dimensional extremal problem

The deterministic variational core is the following.

### Lemma 2 — weighted Weibull cost minimizer

Let `a_i>0`, `gamma>1`, and `q=gamma/(gamma-1)`. Among vectors `t_i>=0` satisfying

\[
\sum_i a_i t_i\ge s,
\]

the minimum of `sum_i t_i^gamma` is

\[
\boxed{
\frac{s^\gamma}{\left(\sum_i a_i^q\right)^{\gamma-1}}.
}
\tag{5.1}
\]

One minimizer is

\[
t_i=
\frac{s\,a_i^{q-1}}{\sum_j a_j^q}.
\tag{5.2}
\]

#### Proof

Holder gives

\[
s
\le \sum_i a_i t_i
\le
\left(\sum_i a_i^q\right)^{1/q}
\left(\sum_i t_i^\gamma\right)^{1/\gamma}.
\]

Rearranging yields the lower bound (5.1). Equality in Holder occurs exactly when `t_i^(gamma-1)` is proportional to `a_i`, which is (5.2). ∎

At the critical exponents (2.1), the identity

\[
(q-1)\gamma=q
\tag{5.3}
\]

will make the probabilistic lower bound match this deterministic optimum exactly.

## 6. B30 — localize by shells and prove the matching lower bound

Fix a small constant `eta>0`, to be chosen only in terms of the law and `d`, and let

\[
R=\left\lfloor
\eta\sqrt{\frac{s}{\log(e+s)}}
\right\rfloor.
\tag{6.1}
\]

For `s` large, `R` is large. Choose `K` in (3.1) sufficiently large that

\[
R\le c_0\sqrt m/2,
\]

so the lower Green estimate (2.4) holds throughout the annulus

\[
A=\{y:r_0\le |y|\le R\},
\tag{6.2}
\]

where `r_0` is any fixed sufficiently large radius.

Set

\[
a_y=g_m(0,y),
\qquad
Q_A=\sum_{y\in A}a_y^q.
\tag{6.3}
\]

By the two-sided Green bounds and `q(d-2)=d`, each radial shell contributes order `r^{-1}` after summing lattice points. Therefore

\[
\boxed{
 c\log R\le Q_A\le C\log R.
}
\tag{6.4}
\]

In particular `Q_A asymp log s`.

Now choose the extremal thresholds with total deterministic deficit `2s`:

\[
t_y=
\frac{2s\,a_y^{q-1}}{Q_A},
\qquad y\in A.
\tag{6.5}
\]

Then

\[
\sum_{y\in A}a_y t_y=2s.
\tag{6.6}
\]

### 6.1 Every threshold lies in the regular lower-tail regime

Because `q-1=2/(d-2)`, (2.4) gives for `|y|<=R`

\[
a_y^{q-1}\ge c|y|^{-2}\ge cR^{-2}.
\]

Using (6.4) and (6.1),

\[
t_y
\ge
c\frac{s}{R^2\log R}
\ge \frac{c'}{\eta^2}
\tag{6.7}
\]

for all large `s`. Choose `eta` small enough that the right side is at least `s_0`. Hence the lower bound in (2.3) applies simultaneously to every `t_y`.

### 6.2 Cost of the extremal negative profile

Let

\[
E_A=\bigcap_{y\in A}\{\zeta(y)\le-t_y\}.
\]

By independence and (2.3),

\[
\mathbb P(E_A)
\ge
c_-^{|A|}
\exp\left(-C_-\sum_{y\in A}t_y^\gamma\right).
\tag{6.8}
\]

Using (5.3),

\[
\begin{aligned}
\sum_{y\in A}t_y^\gamma
&=
\left(\frac{2s}{Q_A}\right)^\gamma
\sum_{y\in A}a_y^{(q-1)\gamma}\\
&=
\left(\frac{2s}{Q_A}\right)^\gamma
\sum_{y\in A}a_y^q\\
&=
\frac{(2s)^\gamma}{Q_A^{\gamma-1}}\\
&\le
C\frac{s^\gamma}{(\log(e+s))^{\gamma-1}}
=C\Phi(s).
\end{aligned}
\tag{6.9}
\]

Also

\[
|A|\le CR^d
\le
C\frac{s^\gamma}{(\log(e+s))^\gamma}
\le C\Phi(s).
\tag{6.10}
\]

The prefactor `c_-^{|A|}` is therefore harmless at the target exponential scale. From (6.8)–(6.10),

\[
\boxed{
\mathbb P(E_A)\ge e^{-C\Phi(s)}.
}
\tag{6.11}
\]

On `E_A`,

\[
\sum_{y\in A}a_y\zeta(y)
\le -\sum_{y\in A}a_y t_y
=-2s.
\tag{6.12}
\]

### 6.3 The complement costs only a fixed probability

Let

\[
T_A=\sum_{y\notin A}g_m(0,y)\zeta(y).
\]

It is independent of `E_A`, has mean zero, and by (2.5)

\[
\operatorname{Var}(T_A)
\le
\operatorname{Var}(\zeta(0))\sum_y G(0,y)^2
\le C_d.
\tag{6.13}
\]

Chebyshev gives

\[
\mathbb P(T_A>s)\le C_d/s^2,
\]

and therefore, for all sufficiently large `s`,

\[
\mathbb P(T_A\le s)\ge\frac12.
\tag{6.14}
\]

By independence, on `E_A cap {T_A<=s}` one has `S_m<=-s`. Thus

\[
\mathbb P(S_m\le-s)
\ge
\frac12\mathbb P(E_A)
\ge
c e^{-C\Phi(s)}.
\tag{6.15}
\]

Together with the previous upper bound, this proves Theorem 1. ∎

## 7. Why dyadic shells make the mechanism transparent

Let

\[
A_j=\{y:2^j\le|y|<2^{j+1}\}.
\]

At criticality,

\[
|A_j|\asymp2^{jd},
\qquad
g_m(0,y)\asymp2^{-j(d-2)},
\]

so

\[
\sum_{y\in A_j}g_m(0,y)^q
\asymp
2^{jd}2^{-jq(d-2)}
=1.
\tag{7.1}
\]

Thus every active dyadic scale contributes a constant amount of `q`-energy. The extremal threshold (6.5) behaves as

\[
t_y\asymp\frac{s}{J}|y|^{-2}
\tag{7.2}
\]

when `J` shells are active. The last shell can remain in the regular Weibull regime only while

\[
2^{2J}\lesssim\frac{s}{J}.
\]

Hence

\[
J\asymp\log s.
\tag{7.3}
\]

Each shell then costs order `(s/J)^gamma`, and summing over the `J` active scales gives

\[
J\left(\frac{s}{J}\right)^\gamma
=
\frac{s^\gamma}{J^{\gamma-1}}
\asymp
\frac{s^\gamma}{(\log s)^{\gamma-1}}.
\tag{7.4}
\]

This is the gluing mechanism behind the critical logarithm: no single scale is extremal; the optimal fluctuation spreads its cost almost evenly across `Theta(log s)` radial scales.

## 8. Consequence for the odometer strategy

The source's reflected recursion uses the finite Green term with a horizon `m_h asymp h`. Since

\[
m_h\asymp h\gg h/\log h,
\]

Theorem 1 applies exactly in that regime. Therefore there are regular critical-tail laws satisfying the source hypotheses for which

\[
\mathbb P(S_{m_h}\le-ch)
\asymp_{\exp}
\exp\left[-\Theta\!\left(
\frac{h^{d/2}}{(\log h)^{d/2-1}}
\right)\right].
\tag{8.1}
\]

Consequently, the previous one-component Green estimate cannot be sharpened uniformly to `exp(-c h^(d/2))`. Any proof of

\[
\mathbb E u_t(0)\lesssim(\log t)^{2/d}
\]

at the critical endpoint, if true, must use a mechanism absent from the Green average alone — for example, a cancellation, conditional dependence, or reflection barrier involving the second term in the source's recursion.

This is a route obstruction, not a lower bound proving that the odometer really has a `(log log t)^((d-2)/d)` factor.

## 9. Frozen metric and status

The source-matching frozen milestone metric remains

\[
M_{\rm crit}(d)=0,
\]

because the preceding run already closed the logarithmic exponent interval to the singleton `{2/d}`. This artifact deliberately does **not** redefine the metric to manufacture movement.

What moved mathematically is the understanding of the remaining slowly varying factor: the critical logarithm has now been proved sharp for the finite Green component itself, and the remaining problem is localized to the interaction with the reflected odometer term.

Canonical I0006 remains **PARTIAL / SOURCE OPEN**.

## 10. Dated source check

As of 2026-09-18, bounded searches recovered the same current source pair:

- arXiv:2609.02820, *Sharpness and critical scaling of parking*;
- arXiv:2609.02829, *Quantitative explosion and percolation of the divisible sandpile*.

The latter is still the source whose high-dimensional stretched-exponential theorem excludes the equality `gamma=d/2`. No later author paper or follow-up resolving the exact endpoint surfaced in the bounded searches performed for this run. That is negative evidence only and is not a worldwide novelty certificate.

## 11. Next mathematical attack

The next nonrepeating method triple should target the reflected term rather than re-estimating `S_m`:

- **B1 — change category:** rewrite the reflected recursion as an obstacle/optimal-stopping comparison and seek a monotonicity or barrier statement coupling the Green fluctuation to reflection;
- **B12 — find what is conserved:** identify an exact martingale/mean-balance quantity under conditioning on the critical multiscale negative profile;
- **B15 — break symmetry:** force the multiscale negative profile on only selected angular sectors to test whether reflection suppresses or transmits the critical Green fluctuation.

The immediate blocking question is whether the matching lower-tail event for `S_m` can coexist with a controlled reflected remainder with only subexponential extra cost. Resolving that question would decide whether the log-log factor is genuine for `E u_t(0)` or only for the scenery component.
