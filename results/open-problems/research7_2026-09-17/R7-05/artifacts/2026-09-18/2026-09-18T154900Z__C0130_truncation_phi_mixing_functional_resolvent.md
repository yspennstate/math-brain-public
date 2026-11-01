Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0130 — monotone truncation obstruction, summably-mixing transfer asymptotics, and an infinite-environment functional resolvent

Target: `C0130`, Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895 (2012; journal 2013), Problem 3.12, printed p. 13.

Date: 2026-09-18.

Status of this artifact: **PARTIAL relative to the full source**. It proves three source-valid results. First, it identifies exactly why the already-proved finite-depth formulas cannot simply be sent to infinite cookie depth: the required interchange is a monotone continuity statement for the never-return probability, overlapping an explicit open continuity problem in Zerner (2005). Second, it replaces the finite-state Poisson equation from the preceding R7-05 report by a bounded Gordin decomposition and proves the same `n^{-bar(delta)}` transfer law for a genuinely infinite-memory, summably phi-mixing stationary class. Third, it proves a complete contractive first-defect resolvent theorem on the full environment state space for arbitrary stationary dependence at fixed finite depth under uniform upper ellipticity. None of these claims is promoted to a solution of the unrestricted `(SE)+(POS_1)` branch.

The admission-fixed metric remains

`M_closed` = largest finite cookie depth `M` for which there is an evidenced exact closed escape-probability formula valid for every i.i.d. bounded cookie-stack law neutral after visit `M` in the transient regime.

The preceding all-depth theorem already gives every finite `M`, so this artifact does **not** redefine the metric:

\[
M_{\rm closed}=\infty\quad\text{(all finite i.i.d. depths), unchanged.}
\]

Here and below `infinity` in that metric means unbounded over finite depths, not an infinite non-placebo stack.

---

## 1. Source scope and cumulative inputs

Problem 3.12 asks, in the transient one-dimensional case, to compute

\[
p_{\rm esc}=P_0[X_n\ne0\ \text{for every }n\ge1].
\]

The source places this immediately after its one-dimensional recurrence/transience theorem. The cumulative R7-05 record has already proved:

1. an exact finite-dimensional signed-resolvent formula for every finite-depth law in the source's `(IID)+(BD)+(WEL)` branch;
2. a scalar transfer theorem for spatial-periodic positive environments;
3. a finite-state spatial-Markov transfer theorem and exact finite escape resolvent for bounded positive elliptic stacks with stationary average drift `bar(delta)>1`.

Those results are reused only at their proved scope. In particular, no i.i.d. factorization is imported into the dependent arguments below.

For a stack at spatial site `x`, write its right-jump probabilities as

\[
p_{x,1},p_{x,2},\ldots,
\]

and put

\[
\alpha_{x,i}=2p_{x,i}-1.
\]

In the positive branch, `alpha_{x,i}>=0`. For a finite depth `M`, all cookies after `M` are neutral, and

\[
\delta_x=\sum_{i=1}^M\alpha_{x,i}.
\]

The forward branching transition at a site is defined by letting `S_k` be the number of successes before the `k`-th failure in the site's Bernoulli sequence. The population update is `k -> S_k`; state zero is absorbing. For a fixed finite depth `M`, the cumulative high-state calculation gives, for `k>=M`,

\[
P_{x,k}(z)=T(z)^k B_x(z),
\qquad
T(z)=\frac1{2-z},
\tag{1.1}
\]

where in a deterministic environment

\[
B_x(z)=\prod_{i=1}^M\big((1-\alpha_{x,i})+\alpha_{x,i}z\big).
\tag{1.2}
\]

For positive cookies, `B_x` is itself a probability generating function. Declaring (1.1) for every `k>=0` therefore defines a genuine auxiliary stochastic kernel. The true and auxiliary positive-population kernels differ only in rows

\[
\mathcal B=\{1,\ldots,M-1\}.
\tag{1.3}
\]

That finite-row defect is algebraic and does not use spatial independence.

---

# 2. B7 — take the depth limit: a precise continuity obstruction

The tempting route to the full positive stationary-ergodic branch is: truncate an infinite positive stack after depth `M`, compute the finite-depth escape probability, and let `M` tend to infinity. The first two steps are legitimate. The last step is not automatic.

## 2.1 Monotone truncations

Fix a deterministic positive cookie environment `omega`, so

\[
\omega(x,i)=p_{x,i}\ge\frac12.
\]

For each `M`, define the neutral-tail truncation

\[
\omega^{(M)}(x,i)=
\begin{cases}
\omega(x,i),&i\le M,\\
1/2,&i>M.
\end{cases}
\tag{2.1}
\]

Then coordinatewise

\[
\omega^{(M)}\le \omega^{(M+1)}\le\omega.
\tag{2.2}
\]

Let

\[
e(\eta)=P_{0,\eta}[X_n>0\ \text{for all }n>0].
\tag{2.3}
\]

Zerner's monotonicity theorem for positive environments states that `e(eta)` is increasing in the environment. Hence

\[
e(\omega^{(1)})\le e(\omega^{(2)})\le\cdots\le e(\omega),
\]

so the limit

\[
\boxed{
 e_*(\omega):=\lim_{M\to\infty}e(\omega^{(M)})
}
\tag{2.4}
\]

exists and satisfies

\[
\boxed{e_*(\omega)\le e(\omega).}
\tag{2.5}
\]

In the right-transient positive regime, `e(omega)` is the quenched never-return probability relevant to Problem 3.12: after a first step to the left, right transience forces a later crossing of zero, while a no-return path beginning to the right stays positive.

## 2.2 Finite horizons agree exactly

For `N>=1`, define

\[
E_N=\{X_1>0,\ldots,X_N>0\}.
\]

A path of length `N` can consume at most `N` cookies at any one site. Consequently, for every `M>=N`,

\[
\boxed{
P_{0,\omega^{(M)}}(E_N)=P_{0,\omega}(E_N).
}
\tag{2.6}
\]

This is exact, not asymptotic.

Set

\[
a_{M,N}=P_{0,\omega^{(M)}}(E_N).
\]

Since `E_N` decreases to the infinite-horizon event,

\[
e(\omega^{(M)})=\inf_N a_{M,N}.
\tag{2.7}
\]

On the other hand, (2.6) gives

\[
P_{0,\omega}(E_N)=\sup_M a_{M,N},
\]

and therefore

\[
 e(\omega)=\inf_N\sup_M a_{M,N}.
\tag{2.8}
\]

Combining (2.4), (2.7), and (2.8),

\[
\boxed{
 e_*(\omega)
 =\sup_M\inf_N a_{M,N}
 \le
 \inf_N\sup_M a_{M,N}
 =e(\omega).
}
\tag{2.9}
\]

Thus the entire obstruction is the possible strict minimax gap in (2.9). All finite-time observables stabilize exactly, yet the infinite-time survival event need not commute with the depth limit without a uniform tail estimate.

### Proposition 2.1 — monotone truncation lower envelope

For every positive deterministic environment `omega`, neutral-tail truncation satisfies (2.4)--(2.9). In particular, proving

\[
\boxed{e(\omega^{(M)})\uparrow e(\omega)}
\tag{2.10}
\]

for all positive environments is a genuine continuity theorem, not a consequence of finite-horizon convergence alone.

### Proof

Monotonicity is (2.2) plus Zerner's monotonicity theorem. Equation (2.6) follows because the first `N` steps cannot query a cookie index greater than `N`. Equations (2.7) and (2.8) are continuity from above for the decreasing finite-horizon events. The general inequality `sup inf <= inf sup` gives (2.9). QED.

## 2.3 Why this is not a technicality

Immediately after his monotonicity results, Zerner (2005) explicitly asks whether the return probability and velocity are continuous in the environment. The monotone-from-below statement (2.10) is a particular continuity direction for the same return/never-return observable. Therefore the previous all-finite-depth theorem cannot honestly be promoted to arbitrary infinite positive stacks by writing `M -> infinity` unless this continuity issue is solved under the source hypotheses or under a clearly stated stronger class.

This is the B7 outcome: the limit route does not fail vaguely; it terminates at the exact interchange

\[
\sup_M\inf_N a_{M,N}\stackrel{?}=\inf_N\sup_M a_{M,N}.
\tag{2.11}
\]

No claim is made that (2.10) is equivalent to Zerner's full topology-unspecified continuity question. It is a concrete monotone instance of that obstacle.

---

# 3. B21 — import Gordin's martingale approximation for summably mixing environments

The preceding finite-state Markov theorem used a finite Poisson equation to control the weighted centered drift

\[
\sum_j\frac{\delta_j-\bar\delta}{u+j}.
\]

That finite-state hypothesis is unnecessary. A projective martingale decomposition is enough.

## 3.1 A source-valid infinite-memory subclass

Assume now that the spatial stack process is two-sided stationary and ergodic, has deterministic finite depth `M`, and for some `kappa in (0,1/2]`,

\[
\frac12\le p_{x,i}\le1-\kappa,
\qquad 1\le i\le M,
\tag{3.1}
\]

with `p_{x,i}=1/2` for `i>M`. No Markov or finite-state assumption is made.

Let

\[
\bar\delta=E\delta_0>1,
\qquad
X_x=\delta_x-\bar\delta.
\tag{3.2}
\]

We impose a strong but transparent dependence condition solely for this theorem: the two-sided stack sequence is **summably phi-mixing**. In one standard convention,

\[
\phi(n)=
\sup\{|P(B\mid A)-P(B)|:
A\in\mathcal F_{-\infty}^0,
B\in\mathcal F_n^\infty,
P(A)>0\},
\tag{3.3}
\]

and

\[
\boxed{\sum_{n\ge1}\phi(n)<\infty.}
\tag{3.4}
\]

The same property holds for the reversed stationary sequence.

## 3.2 A bounded Gordin decomposition

Work with the reversed drift sequence

\[
Y_j=X_{-j},\qquad j\in\mathbb Z,
\]

and filtration

\[
\mathcal G_j=\sigma(Y_r:r\le j).
\]

For a bounded centered future random variable at separation `n`, the phi-mixing definition gives the standard conditional-expectation estimate

\[
\|E[Y_n\mid\mathcal G_0]\|_\infty
\le 2\|Y_0\|_\infty\phi(n).
\tag{3.5}
\]

Thus (3.4) implies

\[
\sum_{n\ge0}
\|E[Y_n\mid\mathcal G_0]\|_\infty<\infty.
\tag{3.6}
\]

Define

\[
G_j=\sum_{m=0}^\infty E[Y_{j+m}\mid\mathcal G_j].
\tag{3.7}
\]

The series converges in `L^infinity`, uniformly in `j`, and stationarity makes `(G_j)` stationary. Moreover,

\[
E[G_{j+1}\mid\mathcal G_j]
=G_j-Y_j.
\tag{3.8}
\]

Define

\[
D_{j+1}=G_{j+1}-E[G_{j+1}\mid\mathcal G_j].
\tag{3.9}
\]

Then `(D_{j+1},G_{j+1})` is a bounded martingale-difference sequence and

\[
\boxed{
Y_j=G_j-G_{j+1}+D_{j+1}.
}
\tag{3.10}
\]

This is the exact replacement for the finite-state Poisson coboundary.

## 3.3 Harmonic weights converge with exponential moments

Fix `u>=1` and put

\[
a_j=(u+j)^{-1}.
\]

Using (3.10), summation by parts gives

\[
\begin{aligned}
\sum_{j=0}^{n-1}a_jY_j
={}&a_0G_0-a_{n-1}G_n\\
&+\sum_{j=1}^{n-1}(a_j-a_{j-1})G_j
+\sum_{j=0}^{n-1}a_jD_{j+1}.
\end{aligned}
\tag{3.11}
\]

The first three terms converge absolutely because `G_j` is uniformly bounded and

\[
\sum_{j\ge1}|a_j-a_{j-1}|<\infty.
\]

The martingale term converges almost surely and in `L^2` because `D_j` is bounded and

\[
\sum_j a_j^2<\infty.
\]

Furthermore, conditional Hoeffding applied to the bounded martingale differences yields, for every fixed real `theta`,

\[
\boxed{
\sup_n E\exp\left(
\theta\sum_{j=0}^{n-1}a_jD_{j+1}
\right)<\infty.
}
\tag{3.12}
\]

Consequently the partial sums in (3.11) converge with uniformly bounded exponential moments of every fixed order.

## 3.4 The transfer product

For a stack environment `eta`, define

\[
b_\eta(v)=B_\eta\left(1-\frac1v\right)
=\prod_{i=1}^M\left(1-\frac{\alpha_i(\eta)}{v}\right).
\tag{3.13}
\]

Uniform upper ellipticity in (3.1) keeps every factor bounded away from zero when `v>=1`. Uniformly in `eta`,

\[
\log b_\eta(v)
=-\frac{\delta(\eta)}v+O(v^{-2}).
\tag{3.14}
\]

Let `(eta_j)_{j>=0}` denote the reversed stationary stack sequence. Put

\[
W_n(u)=\prod_{j=0}^{n-1}b_{\eta_j}(u+j).
\tag{3.15}
\]

Combining (3.11)--(3.14),

\[
\log W_n(u)
=-\bar\delta\sum_{j=0}^{n-1}\frac1{u+j}
-\sum_{j=0}^{n-1}\frac{Y_j}{u+j}
+O(1),
\tag{3.16}
\]

where the `O(1)` term converges as `n->infinity`. Since

\[
\sum_{j<n}\frac1{u+j}=\log n+c(u)+o(1),
\]

we obtain:

### Theorem 3.1 — summably-mixing transfer exponent

Under (3.1)--(3.4), for every fixed `u>=1` there is a finite strictly positive random variable `L(u)` such that

\[
\boxed{
n^{\bar\delta}W_n(u)\longrightarrow L(u)
}
\tag{3.17}
\]

almost surely and in `L^q` for every fixed finite `q`. In particular,

\[
\boxed{
E W_n(u)\sim C(u)n^{-\bar\delta},
\qquad
C(u)=E L(u)\in(0,\infty).
}
\tag{3.18}
\]

### Proof

Equation (3.16) plus the convergence of (3.11) gives almost-sure convergence of `n^{bar(delta)}W_n(u)` to a finite positive limit. The only unbounded random partial sum in its logarithm is the weighted martingale in (3.11). Uniform exponential moments (3.12), applied with both signs, give uniform `L^q` bounds for the normalized product for each finite `q`; uniform integrability then gives `L^q` convergence and (3.18). QED.

## 3.5 Why this product is the actual annealed transfer product

For a fixed environment, the `n`-step auxiliary population pgf is

\[
F_{\omega,k}^{(n)}(z)
=T^n(z)^k
\prod_{m=0}^{n-1}
B_{\theta^m\omega}\big(T^{n-1-m}(z)\big).
\tag{3.19}
\]

In the parabolic coordinate `u=(1-z)^{-1}`, the product in (3.19) is

\[
\prod_{j=0}^{n-1}
 b_{\theta^{n-1-j}\omega}(u+j).
\tag{3.20}
\]

By stationarity, the finite block in (3.20) has the same law as

\[
(\omega,\theta^{-1}\omega,\ldots,\theta^{-(n-1)}\omega),
\]

which is precisely the reversed stationary sequence used in (3.15). Thus (3.18) is an annealed transfer asymptotic for the actual spatially dependent auxiliary chain. This statement deliberately does **not** claim quenched convergence at a fixed spatial origin as `n` changes; the stationarity recentering is part of the argument.

## 3.6 Low-state Green summability survives infinite memory

For every fixed integer `r>=1`, direct differentiation of (3.13) and (3.1) gives

\[
\sup_\eta
\left|\frac{d^r}{dv^r}\log b_\eta(v)\right|
\le C_r v^{-r-1},
\qquad v\ge1.
\tag{3.21}
\]

Therefore fixed `u`-derivatives of the product in (3.20) are bounded by a constant times the product itself. Since fixed `z`-derivatives at zero are finite linear combinations of fixed `u`-derivatives at `u=1`, Theorem 3.1 yields, for each fixed starting population `k` and target population `j`,

\[
\boxed{
E\,\mathsf Q_\omega^{(n)}(k,j)
=O_{k,j}(n^{-\bar\delta}).
}
\tag{3.22}
\]

Hence `bar(delta)>1` implies

\[
\boxed{
\sum_{n\ge0}E\,\mathsf Q_\omega^{(n)}(k,j)<\infty
}
\tag{3.23}
\]

for every fixed low-population target `j`.

This extends the finite-state Markov potential estimate to a genuine infinite-memory class. Spatial dependence changes the limiting prefactor but not the power `bar(delta)` under the stated projective/mixing hypothesis.

---

# 4. B4 — a complete weaker theorem: functional first-defect resolvent under arbitrary stationary dependence

The finite-state Markov report made the boundary system finite-dimensional by including the environment state. For a general stationary environment, the environment coordinate is infinite-dimensional. The key observation is that finite dimensionality is **not** needed for uniqueness of the boundary equation: uniform upper ellipticity makes the boundary operator a strict contraction.

This section assumes only:

- stationary (ergodicity is not needed for the algebra below) spatial stack law `P`;
- a deterministic finite depth `M>=2`;
- positive cookies with the uniform bound (3.1).

No mixing, Markov, finite-state, or independence assumption is used in the functional resolvent theorem itself.

## 4.1 Lift the chain to environment x population

Let `theta` be spatial shift. For a deterministic environment `omega`, let

\[
K_\omega(k,j)
\]

be the true one-site forward population transition and

\[
Q_\omega(k,j)
\]

the positive auxiliary transition obtained by declaring (1.1) for every `k`. Define lifted kernels on the state space `Omega x N_0` by

\[
\mathcal K((\omega,k),d\eta\times\{j\})
=\mathbf1_{\{\eta=\theta\omega\}}K_\omega(k,j),
\tag{4.1}
\]

and analogously for `mathcal Q` using `Q_omega`.

The population-zero states are absorbing for the survival question. Put

\[
\mathcal A=\{0,1,\ldots,M-1\}
\]

in the population coordinate, and retain

\[
\mathcal B=\{1,\ldots,M-1\}.
\]

Outside `mathcal B`, the true and auxiliary **positive-population** rows coincide. Thus the two lifted chains can be coupled identically until the first time their population enters `mathcal A`.

## 4.2 Auxiliary first-entrance operators

For `k>=M`, let

\[
\tau=\inf\{n\ge0:V_n\in\mathcal A\}
\]

under `mathcal Q`. Define

\[
r(\omega,k)
=P^{\mathcal Q}_{\omega,k}(\tau=\infty),
\qquad k\ge M,
\tag{4.2}
\]

and set `r(omega,k)=0` for `k<M`.

For a bounded vector-valued measurable function

\[
f=(f_1,\ldots,f_{M-1}),
\qquad f_b:\Omega\to\mathbb R,
\]

define `Hf` on positive populations by

\[
(Hf)(\omega,k)=
\begin{cases}
f_k(\omega),&1\le k<M,\\
E^{\mathcal Q}_{\omega,k}
\left[
 f_{V_\tau}(\theta^\tau\omega)
 ;\tau<\infty,\ V_\tau\in\mathcal B
\right],&k\ge M.
\end{cases}
\tag{4.3}
\]

Then

\[
\|Hf\|_\infty\le\|f\|_\infty.
\tag{4.4}
\]

Let

\[
s(\omega,k)
=P^{\mathcal K}_{\omega,k}(V_n>0\ \text{for all }n\ge0)
\tag{4.5}
\]

be true forward-process survival and `s_B=(s(.,1),...,s(.,M-1))`.

### Lemma 4.1 — functional first-defect decomposition

For every `k>=M`,

\[
\boxed{
s(\omega,k)=r(\omega,k)+(Hs_B)(\omega,k).
}
\tag{4.6}
\]

### Proof

Until population first enters `A`, the true and auxiliary transition rows coincide. If the common path first enters population zero, true survival fails. If it first enters a boundary population `b in B`, the strong Markov property leaves survival probability `s(theta^tau omega,b)`. If it never enters `A`, it never visits a discrepancy row or zero, so the true and auxiliary paths coincide forever and survival occurs. These disjoint cases are exactly (4.6). QED.

## 4.3 The boundary operator

For `b in B`, take one **true** transition from the boundary and then use (4.6). Define

\[
a_b(\omega)
=\sum_{j\ge1}K_\omega(b,j)r(\theta\omega,j),
\tag{4.7}
\]

and

\[
(\mathcal Mf)_b(\omega)
=\sum_{j\ge1}K_\omega(b,j)(Hf)(\theta\omega,j).
\tag{4.8}
\]

Then the true boundary survival vector satisfies the exact functional equation

\[
\boxed{(I-\mathcal M)s_B=a.}
\tag{4.9}
\]

The operator acts on `L^infinity(P;R^{M-1})`, but the next lemma shows that no abstract uniqueness-at-infinity theorem is needed.

### Lemma 4.2 — strict contraction from uniform upper ellipticity

Let

\[
\varepsilon_M=\kappa^{M-1}>0.
\tag{4.10}
\]

Then

\[
\boxed{\|\mathcal M\|_{\infty\to\infty}\le1-\varepsilon_M.}
\tag{4.11}
\]

### Proof

For a boundary population `1<=b<M`, the next population is zero precisely when there are zero successes before the `b`-th failure, i.e. when the first `b` Bernoulli trials at the site are all failures. By (3.1), each failure probability is at least `kappa`. Therefore

\[
K_\omega(b,0)\ge\kappa^b\ge\kappa^{M-1}=\varepsilon_M.
\tag{4.12}
\]

If `||f||_infinity<=1`, then (4.4) gives `|Hf|<=1`, so

\[
|(\mathcal Mf)_b(\omega)|
\le\sum_{j\ge1}K_\omega(b,j)
=1-K_\omega(b,0)
\le1-\varepsilon_M.
\]

Taking the essential supremum proves (4.11). QED.

### Theorem 4.3 — exact contractive functional resolvent

Under the assumptions of Section 4, the true boundary survival vector is the unique bounded solution of (4.9), and

\[
\boxed{
s_B=(I-\mathcal M)^{-1}a
=\sum_{r=0}^\infty\mathcal M^r a,
}
\tag{4.13}
\]

with uniform geometric convergence. More precisely,

\[
\left\|
s_B-\sum_{r=0}^R\mathcal M^r a
\right\|_\infty
\le
\frac{(1-\varepsilon_M)^{R+1}}{\varepsilon_M}
\|a\|_\infty.
\tag{4.14}
\]

### Proof

Lemma 4.2 gives `||M||<1`, so the Neumann series converges in operator norm and is the inverse of `I-M`. Equation (4.9) then has a unique bounded solution. The geometric-series remainder gives (4.14). QED.

This theorem is genuinely beyond the finite-state Markov result: the spatial environment may have arbitrary stationary dependence and infinite memory. What becomes infinite-dimensional is only the boundary **function** `s_B(omega)`, not the number of population boundary levels.

## 4.4 Return to the source escape probability

The sitewise forward-branching/no-return identity is pathwise and does not require spatial independence. In the right-transient positive regime,

\[
\boxed{
p_{\rm esc}
=E\left[p_{0,1}(\omega)\,s(\theta\omega,1)\right].
}
\tag{4.15}
\]

For `M>=2`, `s(theta omega,1)` is a component of the resolvent (4.13). Importantly, under dependent environments the expectation in (4.15) does **not** factor into `E p_{0,1}` times an independent survival probability.

Thus (4.13)--(4.15) are an exact convergent functional computation for every fixed finite-depth, uniformly upper-elliptic positive stationary environment, without an i.i.d., Markov, periodic, or finite-state assumption.

This remains a restricted theorem relative to the full source because `(SE)+(POS_1)` itself does not impose deterministic finite depth or the uniform upper bound `p<=1-kappa`.

## 4.5 Combining B21 and B4 gives a controlled infinite-memory subclass

Under the additional summable phi-mixing and `bar(delta)>1` assumptions of Section 3, (3.22) implies that auxiliary visits to each fixed boundary population have a summable annealed tail. In particular, for fixed starting population `k`, the probability mass of first entries into `B` after time `N` is bounded by

\[
\begin{aligned}
E\,P^{\mathcal Q}_{\omega,k}
(\tau>N,\tau<\infty,V_\tau\in\mathcal B)
&\le
\sum_{n>N}\sum_{b=1}^{M-1}
E\,\mathsf Q_\omega^{(n)}(k,b)\\
&=O(N^{1-\bar\delta}).
\end{aligned}
\tag{4.16}
\]

Thus the first-entrance operator `H` can be approximated in annealed `L^1` by a finite-horizon operator with a polynomial tail `O(N^{1-bar(delta)})`. The boundary Neumann series (4.13) independently converges geometrically at rate at most `1-epsilon_M`. This gives two separate, proved convergence mechanisms:

1. **time truncation of the auxiliary first-entrance operator:** polynomial tail `O(N^{1-bar(delta)})`;
2. **number of returns through the true defect boundary:** geometric tail `(1-epsilon_M)^R`.

This is a substantially more explicit computation than a bare stationary-law characterization, while still being honestly restricted to the stated mixing/ellipticity subclass.

---

# 5. What failed, what was proved, and the exact remaining source gap

## B7 outcome

**Failed as a full-source completion route, for a precise reason.** Neutral-tail truncations increase monotonically and all fixed finite horizons stabilize exactly, but the desired infinite-depth limit requires the minimax interchange (2.11). Zerner explicitly posed continuity of the return probability in the environment as an open problem. No continuity theorem was assumed.

## B21 outcome

**Succeeded.** The finite-state Poisson equation is not essential. Summable phi-mixing gives a bounded Gordin decomposition, which gives the same harmonic-weight convergence, uniform exponential moments, `n^{-bar(delta)}` annealed transfer exponent, and summable low-state auxiliary Green kernel for a genuine infinite-memory stationary class.

## B4 outcome

**Succeeded.** At fixed finite depth, arbitrary stationary dependence can be retained by lifting the environment itself into the state variable. Uniform upper ellipticity makes the resulting boundary operator a strict contraction, yielding the exact functional resolvent (4.13), with no finite-state or mixing assumption. With B21's mixing hypothesis, its auxiliary first-entrance term also has a proved finite-time approximation rate.

## Full-source gap

The literal positive stationary-ergodic source branch still permits features not covered here:

- infinitely many non-neutral cookies at a site;
- no uniform upper ellipticity `p<=1-kappa`;
- arbitrary ergodic dependence without a summable projective/mixing condition.

Most importantly, finite-depth formulas cannot be passed to arbitrary infinite positive stacks without controlling the continuity gap (2.11). Therefore the source remains **PARTIAL**, not PROVED.

---

# 6. Dated literature check — 2026-09-18

Primary source rechecked: Kosygina--Zerner, arXiv:1204.1895v2 / journal 2013. Problem 3.12 is still present and asks for the transient never-return probability.

Source-cited special case rechecked: Martin P. W. Zerner, *Multi-excited random walks on integers*, PTRF 133 (2005), Theorem 18, gives the exact two-cookie formula. The same paper's Theorem 16 proves monotonicity of the never-return probability in a positive environment and, immediately before the two-cookie section, explicitly asks whether return probability and velocity are continuous in the environment. This is the precise external antecedent for the B7 obstruction above.

Later class rechecked: Nicholas F. Travers, *Excited Random Walk in a Markovian Environment*, EJP 23 (2018), paper 43 / arXiv:1611.01681, treats a large spatial-Markov class and emphasizes that the general stationary-ergodic setting is much less understood. It does not, in the bounded search performed here, supply a general computation of Problem 3.12's escape probability.

A bounded 2026-09-18 search for later solutions of Problem 3.12, return-probability continuity, and Markov/stationary-ergodic escape formulas did not surface a full source-matching resolution. This is **negative evidence only**, not a novelty or openness certificate.

---

# 7. Next mathematical attack

The next ordinary research triple should be **B5 / B11 / B30**, not repeat B7/B21/B4:

- **B5 — add a tail-strength parameter and differentiate:** interpolate between `omega^(M)` and `omega` in the tail and seek a quantitative derivative/influence bound summable over cookie indices. A summable influence estimate would force the missing continuity (2.10) under an explicit tail condition.
- **B11 — dualize:** rewrite the continuity defect through unused drift / the adjoint branching chain, looking for a monotone integrable quantity whose convergence is easier than path survival itself.
- **B30 — one scale at a time:** impose and solve a single explicit tail condition, e.g. a uniform or integrable residual-drift bound beyond depth `M`, and identify exactly what estimate is needed to glue depth `M` to `M+1`.

The sharp current bottleneck is not finite-depth algebra and not finite-state dependence. It is the infinite-cookie tail continuity of the survival observable.
