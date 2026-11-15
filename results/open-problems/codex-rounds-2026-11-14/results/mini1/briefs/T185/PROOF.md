# A sharp linear-workload certificate

## Model and statement

There are finitely many routes `i=1,...,I` and links `j=1,...,J`. Link `j` has capacity `C_j>0`. The incidence matrix `A` has entries in `{0,1}`, and every route uses at least one link. Write

\[
b_i=\min_{j:A_{ji}=1}C_j.
\]

Arrivals on route `i` form independent Poisson processes of rates `nu_i>0`. Their file sizes are independent, identically distributed on each route, independent of arrivals and other routes, strictly positive almost surely, and have finite means `m_i`. Put `rho_i=nu_i m_i`. No further moment or regularity assumption is imposed. The initial state consists of finitely many files with finite positive residual sizes. The state `X(t)` records the route and residual size of every file; files with zero residual size are removed. Within a route, service is divided equally among its files.

For a count vector `n`, let `Lambda_i(n)` be the aggregate service allocated to route `i`. Absent routes receive zero service. The allocation is feasible and Pareto efficient among the present routes: no present coordinate can be increased without decreasing another present coordinate or violating a link constraint. All weighted alpha-fair allocations with `alpha>0` and positive weights have this property. Indeed, their objective is

\[
\sum_{i:n_i>0}\kappa_i n_i U_\alpha(\Lambda_i/n_i),
\qquad
U_\alpha(x)=
\begin{cases}
 x^{1-\alpha}/(1-\alpha),&\alpha\ne1,\\
 \log x,&\alpha=1,
\end{cases}
\]

and every summand is strictly increasing in its service coordinate. A strictly positive feasible allocation exists on every finite active set. The usual alpha-fair maximizer gives positive rates to present routes; for `alpha>=1` zero service has objective minus infinity, and for `0<alpha<1` the right derivative at zero is infinite. Thus the residual-state evolution is well defined between arrivals and departures. Only feasibility and Pareto efficiency will be used below.

Let `W_i(x)` denote the sum of route `i` residual sizes, and define

\[
\beta=\sum_i\frac{\rho_i}{b_i}.
\]

**Theorem.**

1. For every positive vector `w`, the exact minimum weighted service over nonempty count vectors is
   \[
   \inf_{n\ne0}\sum_i w_i\Lambda_i(n)=\min_i w_i b_i. \tag{1}
   \]
2. There exist positive coefficients `w_i`, a number `epsilon>0`, and a finite threshold `R`, such that the extended generator of `L_w(x)=sum_i w_i W_i(x)` satisfies
   \[
   \mathcal G L_w(x)\le-\epsilon
   \quad\hbox{whenever }L_w(x)>R, \tag{2}
   \]
   if and only if `beta<1`. Under the normalization `min_i w_i b_i=1`, the largest possible uniform negative-drift margin is exactly `1-beta`.
3. If `beta<1`, the residual-state process is positive Harris recurrent. For `Y(x)=sum_i W_i(x)/b_i` and the first emptying time `tau_0`,
   \[
   \mathbb E_x\tau_0\le\frac{Y(x)}{1-\beta}. \tag{3}
   \]
   Starting empty, its regenerative cycles have mean length at most
   \[
   \frac{1}{\nu(1-\beta)},\qquad \nu=\sum_i\nu_i. \tag{4}
   \]
   Its invariant law has empty-state probability at least `1-beta`.

The theorem gives a sufficient region contained in the linkwise subcritical region. It does not assert instability outside `beta<1`.

## 1. Minimum weighted service

Fix a nonempty active set. At least one link used by a present route is saturated. Otherwise each such link has strictly positive slack. There are finitely many links, so one present route can have its aggregate rate increased by a sufficiently small positive amount while all other rates stay fixed. This contradicts Pareto efficiency.

Let `j` be a saturated link, and let `q=min_i w_i b_i`. Every route using `j` has `b_i<=C_j`; consequently `w_i>=q/b_i>=q/C_j`. Feasibility, nonnegativity, and saturation give

\[
\sum_i w_i\Lambda_i
\ge\sum_{i:A_{ji}=1}w_i\Lambda_i
\ge\frac q{C_j}\sum_{i:A_{ji}=1}\Lambda_i=q.
\]

Conversely, if only route `i` is present, Pareto efficiency forces its rate to be `b_i`. Choose `i` attaining the minimum of `w_i b_i`. This gives equality and proves (1).

## 2. Exact characterization of linear negative drift

Departures cause no jump in residual workload: the departing residual reaches zero continuously. Between arrival times,

\[
\frac{d}{dt}L_w(X(t))=-\sum_i w_i\Lambda_i(n(t))
\]

at almost every time. A route `i` arrival adds `w_i B_i`. Finite first moments therefore give the extended-generator identity

\[
\mathcal G L_w(x)=a-\sum_i w_i\Lambda_i(n(x)),
\qquad a=\sum_i w_i\rho_i. \tag{5}
\]

This identity can equivalently be read as the compensator identity for the compound Poisson workload input, so it does not require differentiability of a file-size density.

By (1), `a<q` gives uniform negative drift `-(q-a)` at every nonempty state.

For necessity, consider states containing `N` files on route `i` and no files on any other route. Give each file a fixed positive residual `r_i`. One may choose `r_i` below a point with positive file-size tail, so these states also lie in the natural admissible residual state space. Then `L_w=N w_i r_i` tends to infinity, the service is exactly `b_i`, and (5) is exactly `a-w_i b_i`. If (2) holds, letting `N` exceed its threshold gives `a-w_i b_i<=-epsilon` for every `i`. Hence `a<q` is necessary as well as sufficient.

Since `w_i>=q/b_i`,

\[
a=\sum_i w_i\rho_i\ge q\sum_i\rho_i/b_i=q\beta.
\]

Thus `a<q` implies `beta<1`. Conversely, `w_i=1/b_i` gives `q=1` and `a=beta`, proving the equivalence. When `q=1`, the margin is `1-a<=1-beta`; these same coefficients attain equality. This proves the normalized optimality assertion.

## 3. Expected emptying time

Assume `beta<1`. Let `J(t)` be the sum of `B_i/b_i` over arrivals up to time `t`. It is a compound Poisson process of mean input rate `beta`, so `J(t)-beta t` is an integrable martingale. Write

\[
D(t)=\int_0^t\sum_i\Lambda_i(n(s))/b_i\,ds.
\]

Pathwise workload balance gives `Y(X(t))=Y(x)+J(t)-D(t)`. By (1), `D'(s)>=1` whenever the network is nonempty.

For a nonempty initial state and `T=t wedge tau_0`, the system is nonempty for almost every `s<T`, whence `D(T)>=T`. Optional stopping for the integrable compound Poisson martingale at the bounded stopping time `T` yields `E J(T)=beta E T`. All terms are integrable: `J(T)<=J(t)`, and each route's rate is at most `b_i`, so `D(T)<=I t`. Therefore

\[
0\le\mathbb E_xY(X(T))
=Y(x)+\beta\mathbb E_xT-\mathbb E_xD(T)
\le Y(x)-(1-\beta)\mathbb E_xT.
\]

Let `t` increase to infinity. Monotone convergence proves (3), and in particular `tau_0` is finite almost surely. For an empty initial state, set `tau_0=0` and (3) is immediate.

There is no explosion: a bounded time interval has finitely many arrivals almost surely, and every file departs at most once, so the number of arrivals and departures in that interval is finite. Between these events the rates are fixed functions of the finite count vector.

## 4. Regeneration and positive Harris recurrence

Start at the empty state `0`. The next arrival occurs after an exponential time `H` of mean `1/nu`. Its route is `i` with probability `nu_i/nu`, and its mean normalized size is

\[
\mathbb E Y(X(H))=\sum_i\frac{\nu_i}{\nu}\frac{m_i}{b_i}
=\frac\beta\nu.
\]

Let `T` be the first subsequent return to empty. Applying (3) conditional on the first arrival yields

\[
\mathbb E_0T\le\frac1\nu+
\frac{\beta}{\nu(1-\beta)}
=\frac1{\nu(1-\beta)}.
\]

Every return to empty regenerates the residual-state process: independent Poisson arrivals and independent size marks make the future independent of the past, with the same law as from `0`. Thus successive cycles are independent with the same distribution and finite positive mean length.

For completeness, define the cycle occupation probability

\[
\pi(B)=\frac{\mathbb E_0\int_0^T1_{\{X(t)\in B\}}\,dt}
{\mathbb E_0T}. \tag{6}
\]

This is an invariant probability. To verify invariance, take a bounded measurable `f` and a deterministic `s>=0`. The Markov property and Fubini's theorem give

\[
\mathbb E_0\int_0^T P_s f(X(t))\,dt
=\mathbb E_0\int_0^T f(X(t+s))\,dt.
\]

Subtract `E_0 int_0^T f(X(t))dt`. By shifting integration intervals the difference is

\[
\mathbb E_0\int_T^{T+s}f(X(u))\,du
-\mathbb E_0\int_0^s f(X(u))\,du=0,
\]

where the last equality follows from regeneration at `T`. Dividing by `E_0T` proves `pi P_s=pi`.

To check Harris recurrence directly, use the irreducibility measure `psi=delta_0`. Every initial finite state reaches `0` almost surely by (3), and then spends a positive exponential holding time there. Infinitely many regenerative cycles follow. Their idle portions are independent exponential variables of positive mean, whose sum diverges almost surely. Every measurable set with positive `psi` measure contains `0` and is consequently occupied for an infinite total time almost surely. This proves psi-irreducibility and Harris recurrence. Together with the invariant probability (6), it proves positive Harris recurrence. No claim that the invariant workload has finite mean is needed.

Only the idle portion of a cycle is spent at `0`, up to endpoints of zero Lebesgue measure. Equations (4) and (6) give

\[
\pi(\{0\})=\frac{1/\nu}{\mathbb E_0T}\ge1-\beta.
\]

## 5. A subcritical case no positive linear workload certificate covers

Take two links of capacity `1` and three routes: route `0` uses both links, route `1` uses only the first, and route `2` uses only the second. Set

\[
(\rho_0,\rho_1,\rho_2)=(1/5,1/2,1/2).
\]

The two link loads are both `7/10<1`. All three `b_i` are `1`, whereas `beta=6/5>1`.

An explicit witness works against every positive coefficient vector. Let `a=(1/5)w_0+(1/2)w_1+(1/2)w_2` and let `i` minimize `w_i`, writing its value as `q`. Then `a>=(6/5)q`. At every state containing only route `i` files,

\[
\mathcal G L_w=a-w_i\ge q/5>0.
\]

Increasing the number of such files makes `L_w` arbitrarily large without changing this positive drift. Thus there is no threshold outside which that linear functional has negative drift. This is a counterexample to this certificate, not to stability of the network.

The sufficient region is linkwise subcritical because, for any link `j`,

\[
\frac{\sum_i A_{ji}\rho_i}{C_j}
\le\sum_{i:A_{ji}=1}\frac{\rho_i}{b_i}\le\beta.
\]

For a single link, `beta<1` is exactly the usual subcritical condition. In a general network, a proof of the full linkwise result must go beyond a fixed positive linear functional of route residual workloads with uniform pointwise negative drift. It may still use nonlinear functions, file ages or residual profiles, or drift over state-dependent time intervals.
