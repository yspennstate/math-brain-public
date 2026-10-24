Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# I0006: inverse-square opacity and typical critical Weibull tilts in the first endpoint case

Status: **proved restricted analytic theorems / PARTIAL relative to canonical I0006**.  
Owner: `R7-06`; native ID `6aabe827777c8191a43330b4a87d481d`.  
Canonical target: `I0006`.  
Admission: `research7_2026-09-17/R7-06/admissions/2026-09-18T100120Z__I0006.md`.  
Previous mandatory diagnosis: `research7_2026-09-17/R7-06/runs/2026-09-18/2026-09-18T135500Z__report.md` (creation commit `a62c99cfd3cfa26ab0ef719328c9fd75e0c89d21`).

No source-level closure or publication-novelty claim is made. The canonical frozen metric `M_crit(d)` remains zero. This note executes the STUCK1 recovery on the simplest unresolved source-valid case, `d=5`, `gamma=5/2`, using the precommitted methods **B3 / B11 / B28**.

## 1. What this run tries to decide

At `d=5`, `gamma=5/2`, earlier R7-06 work proved

\[
 c(\log t)^{2/5}
 \le a_t:=\mathbb E u_t(0)
 \le C(\log t)^{2/5}(\log\log t)^{3/5}.
\tag{1.1}
\]

It also proved that the *unreflected* critical Green fluctuation has the sharp cost

\[
\Phi_5(s):=
\frac{s^{5/2}}{(\log(e+s))^{3/2}},
\tag{1.2}
\]

and that reflection is exactly transparent to a downward perturbation `eta` whenever

\[
G_j\eta\le u_j^z
\quad\text{for every relevant Bellman time }j.
\tag{1.3}
\]

The STUCK1 diagnosis identified the missing object as the source-law probability geometry of that transparency/contact condition. The recovery question is therefore deliberately narrower:

> Does the critical inverse-square profile that optimizes the raw Green fluctuation have enough strength to create a genuine obstacle for Bellman paths, at the same `Phi_5(s)` large-deviation cost?

The answer proved below is **yes, for every continuation truncated at height `O(s)`**. Moreover, for the smooth symmetric Weibull law with density proportional to `exp(-|x|^(5/2))`, the product exponential tilt that realizes the critical Green deviation is, with tilted probability tending to one, inverse-square negative on an inner ball that retains `1-o(1)` of the logarithmic scale. Thus the critical Gibbs tilt is not typically reflection-transparent there: it typically contains an opaque core.

What remains is sharply isolated: **boundary-continuation overshoots above the `O(s)` cap**. Controlling those overshoots at the `Phi_5(s)` scale would be a route to deciding the slowly varying factor; this note does not supply that final estimate.

## 2. Setup: the Bellman problem and an inverse-square weight

Let `P` be simple-random-walk averaging on `Z^5`. For deterministic rewards `z`, the finite-horizon reflected recursion is

\[
u_0^z=0,
\qquad
u_{n+1}^z=(z+Pu_n^z)_+,
\tag{2.1}
\]

with optimal-stopping representation

\[
u_n^z(x)=
\sup_{\tau\le n}
\mathbb E_x\sum_{j=0}^{\tau-1}z(X_j).
\tag{2.2}
\]

Put

\[
w(x)=\frac1{1+|x|^2},
\qquad
f(x)=\frac12\log(1+|x|^2).
\tag{2.3}
\]

For `R>=2`, let

\[
T_R=\inf\{j\ge0:|X_j|\ge R\}.
\tag{2.4}
\]

The point of `w` is criticality: in dimension five, a Green optimizer has magnitude proportional to `|x|^{-2}`, while `f` is the logarithmic dual potential whose discrete Laplacian is of order `|x|^{-2}`.

## 3. B3 — a stronger quenched statement: inverse-square rewards are an opacity barrier

### Lemma 3.1 (discrete logarithmic supersolution)

There is a finite constant `C_5` such that for every `x in Z^5`,

\[
\boxed{
(Pf)(x)-f(x)\le C_5 w(x).
}
\tag{3.1}
\]

#### Proof

Extend `f` to `R^5`. Its Hessian is

\[
D^2f(x)=
\frac{I}{1+|x|^2}
-
\frac{2xx^T}{(1+|x|^2)^2},
\tag{3.2}
\]

so

\[
\|D^2f(x)\|\le \frac3{1+|x|^2}.
\tag{3.3}
\]

For `|x|>=2`, every point `x+t e_i`, `|t|<=1`, satisfies

\[
1+|x+t e_i|^2\ge c(1+|x|^2)
\tag{3.4}
\]

with a universal positive `c`. The central-difference identity gives

\[
f(x+e_i)+f(x-e_i)-2f(x)
=
\int_{-1}^1(1-|t|)\,\partial_{ii}f(x+t e_i)\,dt,
\tag{3.5}
\]

hence its absolute value is at most `C/(1+|x|^2)`. Averaging over the five coordinate directions proves (3.1) outside the finite ball `|x|<2`; increasing `C_5` handles that ball. ∎

### Corollary 3.2 (inverse-square occupation is necessary for escape)

Let `sigma` be any stopping time and let `n<infinity`. Put

\[
\tau=T_R\wedge\sigma\wedge n,
\qquad
p=\mathbb P_0(T_R\le\sigma\wedge n).
\tag{3.6}
\]

Then

\[
\boxed{
\mathbb E_0\sum_{j=0}^{\tau-1}w(X_j)
\ge
\frac{p}{2C_5}\log(1+R^2).
}
\tag{3.7}
\]

#### Proof

The bounded-time Dynkin identity and Lemma 3.1 give

\[
\mathbb E_0 f(X_\tau)-f(0)
=
\mathbb E_0\sum_{j<\tau}(Pf-f)(X_j)
\le
C_5\mathbb E_0\sum_{j<\tau}w(X_j).
\tag{3.8}
\]

Here `f(0)=0` and `f>=0`. On the event `T_R<=sigma wedge n`, one has `|X_tau|>=R`, hence

\[
f(X_\tau)\ge\frac12\log(1+R^2).
\]

Taking expectations yields (3.7). ∎

The inequality is deliberately one-sided and therefore robust: no radial symmetry of the stopping rule is assumed.

### Theorem 3.3 (capped-continuation opacity)

Consider the following stopped Bellman crossing problem in `B_R={x:|x|<R}`. Before first exit, the reward satisfies

\[
z(x)\le-Aw(x),\qquad x\in B_R,
\tag{3.9}
\]

with `A>0`. A controller may stop at any time and receive zero, or, if the walk reaches `B_R^c` by time `n` before stopping, receive a nonnegative terminal continuation `H` satisfying

\[
0\le H\le B.
\tag{3.10}
\]

If

\[
\boxed{
A\log(1+R^2)\ge 2C_5B,
}
\tag{3.11}
\]

then the value at the origin is exactly zero: immediate stopping is optimal.

#### Proof

Fix any admissible stopping rule `sigma` and use `tau,p` from (3.6). Its expected payoff is at most

\[
Bp-A\mathbb E_0\sum_{j<\tau}w(X_j).
\tag{3.12}
\]

By (3.7), this is at most

\[
p\left[B-rac{A}{2C_5}\log(1+R^2)\right]\le0.
\tag{3.13}
\]

Every strategy therefore has payoff at most zero, while stopping immediately gives zero. ∎

This is stronger than an expectation estimate for the killed Green kernel: it is a *quenched, all-stopping-rules* obstacle statement. The logarithm appears as an unavoidable path cost, not as an artifact of summing a radial Green bound.

### Corollary 3.4 (exact location of the uncapped failure)

Keep (3.9) and assume (3.11). For an arbitrary nonnegative terminal continuation `H`, let `V_H(0)` be the corresponding crossing value. Then

\[
\boxed{
V_H(0)
\le
\mathbb E_0\!\left[(H_{T_R}(X_{T_R})-B)_+;\,T_R\le n\right],
}
\tag{3.14}
\]

where the notation allows `H` to depend on exit time/remaining horizon.

#### Proof

For every stopping rule, split

\[
H=(H\wedge B)+(H-B)_+.
\tag{3.15}
\]

The payoff with terminal value `H wedge B` is at most zero by Theorem 3.3. The remaining positive term is bounded by its expectation on the unrestricted exit event `T_R<=n`. Take the supremum over stopping rules. ∎

Equation (3.14) is the main output of B3: **once an inverse-square core reaches critical strength, the only way Bellman continuation can defeat it is through an overshoot above the cap**.

## 4. B11 — dualize: the logarithmic potential is a certificate for the minimum crossing cost

Corollary 3.2 has an exact linear-programming interpretation. A stopped random walk determines an occupation measure

\[
\mu(x)=\mathbb E_0\sum_{j<\tau}\mathbf1_{\{X_j=x\}}
\tag{4.1}
\]

and an exit mass `p`. The primal crossing cost is

\[
\sum_xw(x)\mu(x).
\tag{4.2}
\]

The function `f/C_5` is a feasible dual potential because

\[
P(f/C_5)-f/C_5\le w.
\tag{4.3}
\]

Pairing the stopped-flow balance with this potential gives exactly

\[
\boxed{
\sum_xw(x)\mu(x)
\ge p\,\frac{\log(1+R^2)}{2C_5}.
}
\tag{4.4}
\]

Thus the useful dimensionless gluing parameter is

\[
\boxed{
\Omega(A,B,R)
=
\frac{A\log(1+R^2)}{2C_5B}.
}
\tag{4.5}
\]

`Omega>=1` means every continuation capped by `B` is killed before it can compensate the inverse-square cost. This is precisely the multiplier missing from the previous transparency-cone formulation: raw Green efficiency alone says how cheaply a negative profile can be created; `Omega` says whether a Bellman path can cross it.

No claim of exact optimality of the constant `2C_5` is made. The point is the *scale*: inverse-square amplitude times `log R` is dual to capped continuation height.

## 5. The source law can create a fully opaque critical core at the same `Phi_5` cost

This statement uses only the lower-tail half of the admitted source hypotheses, not the special smooth density of Section 6.

Assume for all sufficiently large `r`,

\[
\mathbb P(\zeta(0)\le-r)
\ge c_-e^{-C_-r^{5/2}}.
\tag{5.1}
\]

Let

\[
L_s=\log(e+s),
\qquad
R_s=\left\lfloor\rho\sqrt{\frac{s}{L_s}}\right\rfloor,
\qquad
A_s=K\frac{s}{L_s},
\tag{5.2}
\]

where `rho>0` is fixed and `K` is a sufficiently large fixed constant. Define the inverse-square core event

\[
\mathcal O_s=
\left\{
\zeta(y)\le-\frac{A_s}{1+|y|^2}
\text{ for every }|y|<R_s
\right\}.
\tag{5.3}
\]

### Proposition 5.1 (critical-cost opaque cores)

For every fixed cap factor `b>0`, `K` can be chosen (depending on `b,rho` and the law) so that for all sufficiently large `s`:

1. on `O_s`, the ball `B_{R_s}` is opaque in the sense of Theorem 3.3 to every continuation capped by `B=bs`;
2. there is `C<infinity` such that
   \[
   \boxed{
   \mathbb P(\mathcal O_s)
   \ge
   \exp\{-C\Phi_5(s)\},
   \qquad
   \Phi_5(s)=\frac{s^{5/2}}{L_s^{3/2}}.
   }
   \tag{5.4}
   \]

#### Proof

First, `R_s^2` is asymptotic to `rho^2s/L_s` and

\[
\log(1+R_s^2)=L_s+O(\log L_s).
\tag{5.5}
\]

Hence

\[
A_s\log(1+R_s^2)
=Ks(1+o(1)).
\tag{5.6}
\]

Choose `K>4C_5b`, say. Then (3.11) holds with `B=bs` for all large `s`.

For the probability, the smallest threshold in (5.3) occurs near radius `R_s` and satisfies

\[
\frac{A_s}{1+R_s^2}\ge c\frac K{\rho^2}
\tag{5.7}
\]

for large `s`. Increasing `K` if necessary puts every threshold in the regular lower-tail range of (5.1).

Independence then gives, with `c_0=min(c_-,1)`,

\[
\mathbb P(\mathcal O_s)
\ge
c_0^{N_s}
\exp\left\{-C_-A_s^{5/2}
\sum_{|y|<R_s}(1+|y|^2)^{-5/2}
\right\},
\tag{5.8}
\]

where `N_s=|B_{R_s}|`. In dimension five,

\[
N_s\le CR_s^5
\le C\frac{s^{5/2}}{L_s^{5/2}},
\tag{5.9}
\]

while shell counting gives

\[
\sum_{|y|<R_s}(1+|y|^2)^{-5/2}
\le C(1+\log R_s)
\le CL_s.
\tag{5.10}
\]

Therefore

\[
A_s^{5/2}
\sum_{|y|<R_s}(1+|y|^2)^{-5/2}
\le
C K^{5/2}
\frac{s^{5/2}}{L_s^{3/2}},
\tag{5.11}
\]

and the prefactor cost `|log c_0|N_s` is smaller by one power of `L_s`. This proves (5.4). ∎

This is an obstruction to the optimistic idea that reflection necessarily destroys the critical Green logarithm *more cheaply* than the raw scenery fluctuation. There are source-law configurations, occurring at exactly the critical exponential order, that erect an obstacle strong enough to kill every `O(s)` capped continuation.

It is **not** yet a lower bound for the full odometer increment, because the actual continuation is unbounded. Corollary 3.4 identifies that missing term rather than hiding it.

## 6. B28 — typical configurations under the exact smooth critical Weibull tilt

Now specialize, as required by the STUCK1 recovery, to the cleanest source-valid law:

\[
\nu(dx)=Z^{-1}e^{-|x|^{5/2}}\,dx.
\tag{6.1}
\]

It is symmetric, mean zero, has finite positive variance and all linear exponential moments, and satisfies the admitted two-sided stretched-exponential lower-tail bounds with `gamma=5/2`.

Fix a finite Green horizon `m` and a radius `R` with `m>=C R^2`. Put

\[
a_y=g_m(0,y),\qquad |y|\le R.
\tag{6.2}
\]

The standard finite-Green estimates used in the previous I0006 artifacts give constants `0<c<C<infinity` such that

\[
c(1+|y|)^{-3}
\le a_y\le
C(1+|y|)^{-3},
\qquad |y|\le R,
\tag{6.3}
\]

and consequently

\[
\boxed{
 c\log R
 \le
 Q_R:=\sum_{|y|\le R}a_y^{5/3}
 \le C\log R.
}
\tag{6.4}
\]

For `theta>0`, tilt the product law on `B_R` by the raw Green functional:

\[
\frac{d\mathbb P_\theta}{d\mathbb P}
=
\frac{
\exp\{-\theta\sum_{|y|\le R}a_y\zeta(y)\}
}{
\mathbb E\exp\{-\theta\sum_{|y|\le R}a_y\zeta(y)\}
}.
\tag{6.5}
\]

The coordinates remain independent. At site `y`, writing `h_y=theta a_y`, the tilted density is proportional to

\[
\exp\{-|x|^{5/2}-h_yx\}.
\tag{6.6}
\]

### Lemma 6.1 (one-site mode and strong left concentration)

For `h>0`, define

\[
t(h)=\left(\frac{h}{5/2}\right)^{2/3}.
\tag{6.7}
\]

Then `x=-t(h)` is the unique mode of the density (6.6). Moreover there are constants `c,C,t_0>0` such that whenever `t(h)>=t_0`,

\[
\boxed{
\mathbb P_h\{X>-t(h)/2\}
\le C e^{-c t(h)^{5/2}}.
}
\tag{6.8}
\]

#### Proof

Let `gamma=5/2` and

\[
V_h(x)=|x|^\gamma+hx.
\]

On the negative half-line the stationary equation is

\[
\gamma(-x)^{\gamma-1}=h,
\]

so the minimizer is `-t`, `t=(h/gamma)^{1/(gamma-1)}`. At that point

\[
V_h(-t)=-(\gamma-1)t^\gamma.
\tag{6.9}
\]

At `-t/2`,

\[
V_h(-t/2)-V_h(-t)
=
\left(\frac\gamma2-1+2^{-\gamma}\right)t^\gamma,
\tag{6.10}
\]

and the coefficient is strictly positive for `gamma=5/2`. Also `V_h` is convex and strictly increasing on `[-t/2,infinity)`. Its tangent at `-t/2` therefore bounds the numerator integral by a polynomial factor times `exp(-V_h(-t/2))`.

For the denominator, integrate on an interval of width `delta=t^{-(gamma-2)/2}` around `-t`. On that interval `V_h''=O(t^{gamma-2})`, so Taylor's theorem gives

\[
V_h(x)\le V_h(-t)+C
\]

throughout a subinterval of length comparable to `delta`. Hence the denominator is at least a polynomial factor times `exp(-V_h(-t))`. The exponential gap (6.10) dominates the polynomial factors for large `t`, proving (6.8). ∎

The modal negative profile is therefore

\[
 t_y:=t(h_y)
 =c_*\theta^{2/3}a_y^{2/3}.
\tag{6.11}
\]

Using (6.3),

\[
\boxed{
 t_y\asymp
 \theta^{2/3}(1+|y|)^{-2}.
}
\tag{6.12}
\]

This is exactly the inverse-square obstacle from Sections 3–5.

### Proposition 6.2 (the critical product tilt is typically opaque on `1-o(1)` logarithmic scales)

Let `s->infinity`, put `L_s=log(e+s)`, and choose

\[
R=\left\lfloor\rho\sqrt{s/L_s}\right\rfloor.
\tag{6.13}
\]

Choose `theta=theta(s)` so that the *modal weighted deficit* is an overtilt by a fixed factor `kappa>0`:

\[
\sum_{|y|\le R}a_yt_y=\kappa s.
\tag{6.14}
\]

Then

\[
A:=\theta^{2/3}\asymp\frac{\kappa s}{\log R}.
\tag{6.15}
\]

For a sufficiently large fixed `D`, define

\[
\ell_R=D(\log R)^{1/5},
\qquad
R_*=\left\lfloor R/\ell_R\right\rfloor.
\tag{6.16}
\]

If `kappa` and then `D` are sufficiently large fixed constants, then

\[
\boxed{
\mathbb P_\theta\left(
\zeta(y)\le-cA(1+|y|^2)^{-1}
\text{ for every }|y|\le R_*
\right)
=1-o(1).
}
\tag{6.17}
\]

Furthermore

\[
\frac{\log R_*}{\log R}\longrightarrow1,
\tag{6.18}
\]

so the opaque inner core retains asymptotically all of the critical logarithmic scale. In particular, for every fixed `b>0`, taking `kappa` large enough makes the event in (6.17) satisfy the opacity criterion (3.11) with terminal cap `B=bs` for all large `s`.

#### Proof

Equation (6.14) and (6.11) give

\[
\kappa s
=c_*\theta^{2/3}\sum_{|y|\le R}a_y^{5/3}
=c_*AQ_R.
\]

Together with (6.4), this proves (6.15).

For `|y|\le R_*`, (6.3), (6.11), and (6.15) imply

\[
t_y\ge cA(1+R_*)^{-2}
\ge c\frac{A}{R^2}\ell_R^2.
\tag{6.19}
\]

Because `R^2 asymp s/L_s` and `log R asymp L_s`, the ratio `A/R^2` is bounded below by a positive constant depending on `kappa,rho`. Hence

\[
t_y\ge c\ell_R^2,
\qquad
 t_y^{5/2}\ge cD^5\log R.
\tag{6.20}
\]

Lemma 6.1 therefore gives, uniformly on the inner ball,

\[
\mathbb P_\theta\{\zeta(y)>-t_y/2\}
\le C R^{-cD^5}.
\tag{6.21}
\]

There are `O(R^5)` inner sites. Choosing `D` so that `cD^5>6` and applying a union bound gives probability `1-O(R^{-1})` that `zeta(y)<=-t_y/2` simultaneously for all of them. By (6.12), this implies (6.17).

Finally,

\[
\log R_*
=
\log R-\log D-\frac15\log\log R+o(1),
\]

which proves (6.18). On (6.17), the barrier amplitude is a fixed multiple of `A`, so

\[
A\log(1+R_*^2)
\asymp
\frac{\kappa s}{\log R}\log R_*
\asymp\kappa s.
\]

Choose `kappa` large compared with `bC_5` and apply Theorem 3.3. ∎

### Proposition 6.3 (the tilt itself has the critical information scale)

For the product tilt (6.5) calibrated by (6.14),

\[
\boxed{
D(\mathbb P_\theta\|\mathbb P)
\le
C_\kappa\Phi_5(s)
}
\tag{6.22}
\]

for all large `s`.

#### Proof

For one site let

\[
Z(h)=\mathbb E e^{-hX},
\qquad
\varphi(h)=\log Z(h).
\]

Young's inequality gives

\[
h|x|\le\frac12|x|^{5/2}+C h^{5/3},
\]

so

\[
0\le\varphi(h)\le C(1+h^{5/3});
\tag{6.23}
\]

the lower bound uses Jensen and `EX=0`. Convexity of `varphi` implies for `h>=1`

\[
\varphi'(h)
\le\frac{\varphi(2h)-\varphi(h)}h
\le C h^{2/3}.
\tag{6.24}
\]

The one-site relative entropy is

\[
D(\nu_h\|\nu)
=h\varphi'(h)-\varphi(h)
\le C h^{5/3}
\tag{6.25}
\]

for `h>=1`; bounded `h` can be absorbed by a constant. Therefore, by independence,

\[
D(\mathbb P_\theta\|\mathbb P)
\le
C|B_R|+C\theta^{5/3}\sum_{|y|\le R}a_y^{5/3}.
\tag{6.26}
\]

Now `theta^{5/3}=A^{5/2}`. Using (6.4), (6.15), and `|B_R|=O((s/L_s)^{5/2})`,

\[
\theta^{5/3}Q_R
\le
C_\kappa
\frac{s^{5/2}}{(\log R)^{3/2}}
\le C_\kappa\Phi_5(s),
\]

while the volume term is smaller by one power of `L_s`. This proves (6.22). ∎

Propositions 6.2–6.3 make B28 precise: **under an information-optimal-scale tilt for the raw critical Green deficit, an inverse-square opaque core is typical, not exceptional, on all but a `o(log R)` portion of the active logarithmic scales.**

## 7. What changed conceptually

Before this run, there were two pathwise extremes:

- uniform downward shifts, which collapse mean susceptibility;
- the exact transparency cone, on which reflection loses nothing.

The new result places the *critical Green optimizer itself* relative to those extremes. It is not merely a raw profile with cost `Phi_5(s)`. Its inverse-square geometry has a logarithmic crossing cost, and the exact smooth Weibull tilt producing that profile is overwhelmingly likely to contain an opaque inner core of the same logarithmic strength.

Thus the simplest critical endpoint now has the following three-scale structure:

\[
\boxed{
\text{source cost }\Phi_5(s)
\quad\Longleftrightarrow\quad
A\asymp s/\log R
\quad\Longrightarrow\quad
A\log R\asymp s,
}
\tag{7.1}
\]

where the last quantity is exactly the Bellman crossing penalty certified by the dual potential.

This is evidence against treating the transparency cone as the generic critical behavior. It does **not** by itself decide whether the final odometer growth carries the `(log log t)^{3/5}` factor, because the actual Bellman continuation is not capped.

## 8. Exact remaining gap after B3/B11/B28

The remaining formula is now simpler than the previous generic transparency event. On the inverse-square core event, Corollary 3.4 reduces the continuation value to

\[
\boxed{
V_H(0)
\le
\mathbb E_0[(H_{T_R}(X_{T_R})-B)_+;\,T_R\le n].
}
\tag{8.1}
\]

For the source-scale choice

\[
R^2\asymp s/\log s,
\qquad
B\asymp s,
\tag{8.2}
\]

the core itself is available at probability `exp[-O(Phi_5(s))]` and is typically present under the critical smooth-Weibull tilt. Therefore the unresolved source-level question is no longer whether the raw critical optimizer can survive the obstacle or whether reflection can create contact. It is:

> **Can the boundary/continuation overshoot above height `O(s)` be shown negligible at the `Phi_5(s)` scale after the inverse-square core is imposed?**

A positive answer would let the opaque-core event feed a matching lower bound into the source increment mechanism. A negative answer would identify a distinct positive-spike mechanism that defeats the barrier. Neither direction is proved here.

## 9. Method outcomes and metric

- **B3 (prove something stronger): SUCCESS.** Proved an all-stopping-rules quenched opacity theorem and the exact uncapped overshoot reduction (3.14).
- **B11 (dualize): SUCCESS.** `f(x)=0.5 log(1+|x|^2)` is an explicit dual certificate showing that inverse-square occupation costs `Theta(log R)` per unit escape probability.
- **B28 (typical instead of all): SUCCESS.** For the exact smooth critical Weibull law, the raw Green exponential tilt has inverse-square mode and, with tilted probability `1-o(1)`, contains an opaque inner core retaining `1-o(1)` of the logarithmic scales; the total tilt information is `O(Phi_5(s))`.

Frozen canonical milestone metric before: `M_crit(5)=0`.  
Frozen canonical milestone metric after: `M_crit(5)=0`.  
Movement: **NO MOVEMENT** (the metric is already saturated at zero).  
Post-STUCK1 ordinary unchanged sequence: **1 of 3**.  
HARD stuck recoveries used: **1 of at most 2**.

The mathematical progress is structural rather than metric movement: the critical profile is now proved to have a source-cost-matched opacity mechanism, and the missing term is isolated to a single continuation-overshoot quantity.

## 10. Next nonrepeating methods

If no fresher history supersedes this note, the next ordinary run should not repeat B3/B11/B28. The natural fresh triple is:

- **B4 — prove something weaker, completely:** close the critical lower-increment estimate in a source-faithful *capped-continuation* model and record exactly which step uses the cap.
- **B20 — find why the algorithm fails:** treat (8.1) as the failure term and characterize the cheapest scenery mechanism producing `H>B` at the exit scale.
- **B27 — swap quantifiers:** replace the pathwise uniform cap `H<=B` by an annealed excess bound sufficient after multiplying by the opaque-core probability; determine the weakest overshoot estimate that closes the source increment argument.

No checker is created because this run contains analytic theorem-sized claims rather than a finite computational claim.