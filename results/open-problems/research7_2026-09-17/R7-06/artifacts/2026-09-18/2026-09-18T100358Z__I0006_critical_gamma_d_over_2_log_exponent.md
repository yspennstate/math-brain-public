Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# I0006 milestone: the untreated `gamma=d/2` boundary has logarithmic exponent `2/d`

Status: **proved restricted theorem / PARTIAL relative to canonical I0006**.  
Owner: `R7-06`, native ID `6aabe827777c8191a43330b4a87d481d`.  
Admission: `research7_2026-09-17/R7-06/admissions/2026-09-18T100120Z__I0006.md`.  
Primary source: Bou-Rabee–Panagiotis, *Quantitative explosion and percolation of the divisible sandpile*, arXiv:2609.02829v1, especially Section 6.2.  
No publication-novelty claim is made here.

## 1. Source boundary and theorem

Fix `d>=5` and put

\[
\gamma=\frac d2,\qquad q=\frac{\gamma}{\gamma-1}=\frac d{d-2}.
\]

Let `(zeta(x))_{x in Z^d}` be i.i.d. with

\[
\mathbb E\zeta(0)=0,\qquad 0<\operatorname{Var}\zeta(0)<\infty,
\qquad \mathbb E e^{\theta_0|\zeta(0)|}\le K_0
\tag{1.1}
\]

for some positive `theta_0,K_0`. Assume that for all sufficiently large `s`,

\[
c_-e^{-C_-s^\gamma}
\le \mathbb P(\zeta(0)\le-s)
\le C_+e^{-c_+s^\gamma}.
\tag{1.2}
\]

Let `u_t` be the critical divisible-sandpile finite-time odometer in the normalization of arXiv:2609.02829 and write

\[
a_t=\mathbb E u_t(0).
\]

The source proves the order `(log t)^(1/min{gamma,d/2})` when `gamma != d/2` and explicitly says that it does not treat the borderline `gamma=d/2`.

### Theorem 1 (critical logarithmic exponent)

Under (1.1)–(1.2), there are constants `c,C>0` such that for all sufficiently large `t`,

\[
\boxed{
 c(\log t)^{2/d}
 \le a_t
 \le C(\log t)^{2/d}
        (\log\log(t+e^e))^{(d-2)/d}.
}
\tag{1.3}
\]

Consequently

\[
\boxed{
\lim_{t\to\infty}\frac{\log a_t}{\log\log t}=\frac2d.
}
\tag{1.4}
\]

Thus the admission metric for this milestone moves from the source-certified exponent interval `[2/d,1]` to the singleton `[2/d,2/d]`, i.e.

\[
\boxed{M_{\rm crit}(d):1-2/d\longrightarrow0.}
\]

This does **not** determine the slowly varying factor in (1.3), and it does **not** close the broad canonical I0006 tail-dependent-rate problem.

## 2. B2 — attack the negation / identify why the noncritical proof stops exactly at the boundary

The source's Lemma 6.4 proves, for `gamma != d/2`, a stretched-exponential lower-tail estimate for the finite Green average

\[
S_m=\sum_{y\in\mathbb Z^d}g_m(0,y)\zeta(y).
\]

For `1<gamma<infinity`, its one-site Laplace estimates are

\[
\log\mathbb E e^{-\mu\zeta(0)}\le C\mu^2\quad(0\le\mu\le1),
\qquad
\log\mathbb E e^{-\mu\zeta(0)}\le C\mu^{\gamma/(\gamma-1)}\quad(\mu\ge1).
\tag{2.1}
\]

At the critical value `gamma=d/2`, the exponent in the second estimate is

\[
q=\frac d{d-2}.
\]

The lattice Green bound is

\[
G(0,y)\le C(1+|y|)^{2-d}.
\tag{2.2}
\]

Hence the radial shell sum at the critical power is

\[
\sum_{1\le |y|\le R}G(0,y)^q
\lesssim
\sum_{r\le R}r^{d-1-q(d-2)}
=
\sum_{r\le R}r^{-1}
\asymp\log R.
\tag{2.3}
\]

This is the precise obstruction to simply inserting `gamma=d/2` into the source proof: the summability used for `gamma<d/2` fails logarithmically, while the `gamma>d/2` truncation becomes exactly critical. This is an obstruction to that proof route, **not** a proof that a pure `exp(-cs^(d/2))` bound is false.

The critical logarithm can nevertheless be retained quantitatively rather than discarding the boundary.

## 3. B14 — exploit radial symmetry: critical Green-average tail

### Lemma 2 (critical finite-Green lower tail)

Under the upper half of (1.2), there are `c,C>0` such that for every `m>=1` and `s>=2`,

\[
\boxed{
\mathbb P(S_m\le-s)
\le
C\exp\left\{-c\,
\frac{s^\gamma}{(\log(e+s))^{\gamma-1}}
\right\}.
}
\tag{3.1}
\]

#### Proof

Let `lambda>=2`. Independence and (2.1) give a bound for

\[
L_m(\lambda)
=
\log\mathbb E e^{-\lambda S_m}
=
\sum_y\log\mathbb E e^{-\lambda g_m(0,y)\zeta(y)}.
\]

Choose

\[
R=A\lambda^{1/(d-2)}
\]

with `A` large enough, depending only on the Green constant in (2.2), that

\[
\lambda G(0,y)\le1\qquad(|y|>R).
\tag{3.2}
\]

Because `q=d/(d-2)<2`, for `0<=x<=1` one has `x^2<=x^q`. Thus on the inner region `|y|<=R`, both cases in (2.1) are bounded by `C(lambda G(0,y))^q`. Using `g_m<=G` and (2.3),

\[
\sum_{|y|\le R}
\log\mathbb E e^{-\lambda g_m(0,y)\zeta(y)}
\le C\lambda^q\sum_{|y|\le R}G(0,y)^q
\le C\lambda^q\log(e+R)
\le C\lambda^q\log(e+\lambda).
\tag{3.3}
\]

On `|y|>R`, (3.2) allows the quadratic estimate in (2.1). Since `d>=5`,

\[
\sum_{|y|>R}G(0,y)^2
\le C\sum_{r>R}r^{d-1+2(2-d)}
\le CR^{4-d}.
\]

Therefore

\[
\sum_{|y|>R}
\log\mathbb E e^{-\lambda g_m(0,y)\zeta(y)}
\le C\lambda^2R^{4-d}
\le C\lambda^{2+(4-d)/(d-2)}
=C\lambda^{d/(d-2)}
=C\lambda^q.
\tag{3.4}
\]

Combining (3.3)–(3.4), uniformly in `m`,

\[
L_m(\lambda)\le C\lambda^q\log(e+\lambda).
\tag{3.5}
\]

Chernoff's inequality gives

\[
\mathbb P(S_m\le-s)
\le
\exp\{-\lambda s+C\lambda^q\log(e+\lambda)\}.
\tag{3.6}
\]

Take

\[
\lambda=b\left(\frac{s}{\log(e+s)}\right)^{\gamma-1}
\tag{3.7}
\]

with a fixed sufficiently small `b>0`. Since

\[
q(\gamma-1)=\gamma,
\]

we have

\[
\lambda s
=b\frac{s^\gamma}{(\log(e+s))^{\gamma-1}},
\]

while, after increasing constants for bounded `s`,

\[
\lambda^q\log(e+\lambda)
\le
C b^q\frac{s^\gamma}{(\log(e+s))^{\gamma-1}}.
\]

Because `q>1`, choosing `b` small makes the negative linear-in-`b` term dominate the `b^q` term. This proves (3.1). ∎

## 4. Transfer through the reflected odometer recursion

Define

\[
\Phi(h)=\frac{h^\gamma}{(\log(e+h))^{\gamma-1}}.
\tag{4.1}
\]

The source establishes two facts which do not use `gamma != d/2`:

1. the crude high-dimensional upper bound
   \[
   a_t\le C\log(t+2);
   \tag{4.2}
   \]
2. its Lemma 6.5, for every `m>=1,n>=0,s>=1`,
   \[
   \mathbb P\!\left(P^m(u_n-a_n)(0)\le-s\right)
   \le C\exp\{-c\min(s^2m^{(d-4)/2},sm^{(d-2)/2})\}.
   \tag{4.3}
   \]

We now reproduce the source's Theorem 6.6 argument with Lemma 2 in place of its noncritical Lemma 6.4.

Let `a_t<=h<=t^(1/2)` and put

\[
m_h=\lfloor\varepsilon h\rfloor,
\]

where `epsilon>0` is chosen exactly as in the source so that the mean changes by at most `h/8` over the last `m_h` steps. Iterating the reflected recursion gives

\[
\zeta(0)+Pu_t(0)-a_t
\ge
\sum_{k=0}^{m_h}P^k\zeta(0)
+P^{m_h+1}(u_{t-m_h}-a_{t-m_h})(0)-\frac h8.
\tag{4.4}
\]

Therefore the event on the left being at most `-h` implies at least one of

\[
\sum_{k=0}^{m_h}P^k\zeta(0)\le-\frac{7h}{16},
\tag{4.5}
\]

or

\[
P^{m_h+1}(u_{t-m_h}-a_{t-m_h})(0)\le-\frac{7h}{16}.
\tag{4.6}
\]

The first variable in (4.5) is the finite Green average with `m=m_h+1`; Lemma 2 bounds its probability by

\[
C e^{-c\Phi(h)}.
\tag{4.7}
\]

For (4.6), insert `m\asymp h` and `s\asymp h` into (4.3). The two exponents are

\[
h^2 h^{(d-4)/2}=h^{d/2}=h^\gamma,
\qquad
h h^{(d-2)/2}=h^{d/2}=h^\gamma.
\]

Thus (4.6) has probability at most `C e^{-c h^gamma}`, which is at most `C e^{-c Phi(h)}`. Hence

\[
\mathbb P(\zeta(0)+Pu_t(0)-a_t\le-h)
\le C e^{-c\Phi(h)},
\qquad a_t\le h\le t^{1/2}.
\tag{4.8}
\]

For `h>t^(1/2)`, the source's crude concentration estimate gives a total tail contribution at most `Ce^{-ct^(1/2)}`. By (4.2), `a_t=O(log t)`, and therefore for large `t`,

\[
\Phi(a_t)=O\!\left(\frac{(\log t)^\gamma}{(\log\log t)^{\gamma-1}}\right)=o(t^{1/2}),
\]

so this far tail is also bounded by `C e^{-c Phi(a_t)}` after changing constants.

The exact reflected-increment identity from the source is

\[
a_{t+1}-a_t
=\mathbb E(-\zeta(0)-Pu_t(0))_+.
\tag{4.9}
\]

Equivalently, integrating the lower tail of `zeta(0)+Pu_t(0)-a_t`,

\[
a_{t+1}-a_t
\le
\int_{a_t}^{\infty}
\mathbb P(\zeta(0)+Pu_t(0)-a_t\le-h)\,dh.
\tag{4.10}
\]

Since `gamma>1`, `Phi` is increasing for all sufficiently large arguments and grows faster than linearly. A dyadic split of the integral, or the elementary lower bound `Phi(h)>=c Phi(a_t)+c(h-a_t)` for sufficiently large `a_t`, gives

\[
\boxed{
a_{t+1}-a_t\le C e^{-c\Phi(a_t)}.
}
\tag{4.11}
\]

For bounded `a_t`, enlarge `C`; thus (4.11) holds uniformly after adjusting constants.

## 5. Integrating the critical increment bound

For `R>0`, let

\[
\tau_R=\inf\{n\ge0:a_n\ge R\}.
\]

The source's one-step overshoot bound is uniform, so `a_{tau_R}<=R+C_0`. While `tau_R<=n<tau_{2R}`, monotonicity gives `a_n>=R`; (4.11) therefore yields

\[
a_{n+1}-a_n\le C e^{-c\Phi(R)}.
\]

For all sufficiently large `R`, crossing from `R+O(1)` to `2R` requires a total increase at least `R/2`. Hence

\[
\tau_{2R}-\tau_R
\ge cR e^{c\Phi(R)}.
\tag{5.1}
\]

Take `R=a_t/2` (and absorb bounded values into constants). Then

\[
t\ge c a_t e^{c\Phi(a_t/2)}.
\tag{5.2}
\]

Since `Phi(x/2)>=c_1 Phi(x)` for all large `x`,

\[
\Phi(a_t)\le C\log t.
\tag{5.3}
\]

Set `X=log t`. Inverting

\[
\frac{a_t^\gamma}{(\log(e+a_t))^{\gamma-1}}\le CX
\]

shows

\[
a_t\le C X^{1/\gamma}(\log(e+X))^{(\gamma-1)/\gamma}.
\tag{5.4}
\]

Indeed, if

\[
y=X^{1/\gamma}(\log(e+X))^{(\gamma-1)/\gamma},
\]

then `log(e+Ky) <= C_gamma log(e+X)` and

\[
\Phi(Ky)\ge c_\gamma K^\gamma X
\]

for all sufficiently large `X`; choosing `K` larger than the constant in (5.3) forces `a_t<=Ky`.

Because `1/gamma=2/d` and `(gamma-1)/gamma=(d-2)/d`, (5.4) is the upper bound in (1.3).

For the lower bound, the source's Proposition 6.3 has **no exclusion at `gamma=d/2`**. Applying it to the lower half of (1.2) gives

\[
a_t\ge c(\log t)^{1/\min\{\gamma,d/2\}}
=c(\log t)^{2/d}.
\tag{5.5}
\]

This completes the proof of Theorem 1.

Finally, take logarithms in (1.3):

\[
\frac2d\log\log t+O(1)
\le \log a_t
\le \frac2d\log\log t+rac{d-2}{d}\log\log\log t+O(1).
\]

Divide by `log log t` and let `t->infinity` to obtain (1.4). ∎

## 6. B16 — exact dimension checks

The symbolic exponents specialize consistently.

### `d=5`

\[
\gamma=\frac52,\qquad q=\frac53.
\]

Lemma 2 becomes

\[
\mathbb P(S_m\le-s)
\le C\exp\left\{-c\frac{s^{5/2}}{(\log(e+s))^{3/2}}\right\},
\]

and Theorem 1 gives

\[
c(\log t)^{2/5}
\le a_t
\le C(\log t)^{2/5}(\log\log t)^{3/5}.
\]

### `d=6`

\[
\gamma=3,\qquad q=\frac32.
\]

Lemma 2 becomes

\[
\mathbb P(S_m\le-s)
\le C\exp\left\{-c\frac{s^3}{(\log(e+s))^2}\right\},
\]

and

\[
c(\log t)^{1/3}
\le a_t
\le C(\log t)^{1/3}(\log\log t)^{2/3}.
\]

These are analytic consistency checks, not finite-source certificates.

## 7. What is and is not resolved

**Resolved in this artifact:** the logarithmic growth exponent at the exact source-explicit critical tail boundary `gamma=d/2` under the two-sided regular stretched-exponential assumption (1.2).

**Still open here:**

1. whether the `log log t` factor in the upper bound is necessary;
2. the exact slowly varying correction, if any;
3. irregular lower tails outside the regular two-sided stretched-exponential class;
4. full canonical I0006 source closure.

The critical logarithm in (2.3) suggests a genuine competition of contributions across many radial scales. It does not by itself decide whether the odometer mean inherits the logarithmic correction or whether a more efficient multiscale argument removes it.

## 8. Next nonrepeating attack

Use methods **B6 / B24 / B30** next:

- **B6 deform from a solved case:** approach `gamma=d/2` from `gamma=d/2±epsilon` while tracking constants rather than only powers;
- **B24 extremal object:** solve the large-deviation variational problem for the critical Green average and identify the optimal radial negative profile;
- **B30 localize/gluing failure:** decompose the critical Green field into dyadic shells and determine whether shellwise rare events glue to the `log log` correction or whether the odometer stopping rule suppresses it.

The frozen milestone metric remains `M_crit(d)=0` after this theorem; future work must not replace it merely to manufacture movement. Any further improvement should be tracked as a secondary slowly-varying-factor statement while the canonical I0006 status remains PARTIAL.
