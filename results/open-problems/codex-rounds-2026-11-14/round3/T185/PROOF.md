# A nonlinear workload obstruction in the two-link network

## Statement

There are two links, each of capacity one. Route 0 uses both links, route 1
uses only the first, and route 2 uses only the second. Arrivals are independent
Poisson processes of rates

\[
 (\nu_0,\nu_1,\nu_2)=(1/5,1/2,1/2).
\]

Every arriving file has size one. Thus the route loads are these same numbers,
and each link has load \(7/10<1\). The state consists of finitely many files
with positive residual sizes at most one. Write \(n_i\) for route counts and
\(W_i\) for the sum of route \(i\) residual sizes. Service within each route is
equal among its files.

Fix any \(\alpha>0\) and positive weights \(\kappa_i\). Aggregate rates
\(\Lambda_i(n)\) maximize

\[
 \sum_{i:n_i>0}\kappa_i n_i U_\alpha(\Lambda_i/n_i),
 \qquad \Lambda_0+\Lambda_1\le1,\quad
 \Lambda_0+\Lambda_2\le1,
\]

where \(U_\alpha'(s)=s^{-\alpha}\); absent routes have rate zero.

**Theorem.** Let \(d>0\). Suppose \(F:\mathbb R_+^3\to\mathbb R\) is
positively homogeneous of degree \(d\), continuously differentiable on the
nonzero orthant, including its boundary, and \(F(e_0)>0\). Differentiability
at a boundary point means that \(F\) has a continuously differentiable local
extension to a neighborhood of that point. Define

\[
 V(x)=F(W_0(x),W_1(x),W_2(x)).
\]

There are admissible states \(x_N\), with \(V(x_N)\to\infty\), for which

\[
 \lim_{N\to\infty}N^{1-d}\mathcal G V(x_N)
 \ \ge\ \frac{dF(e_0)}5>0. \tag{1}
\]

In particular, no such \(V\) has uniformly strictly negative generator drift
outside a finite \(V\)-sublevel set. The obstruction also occurs in states
reachable with positive probability from empty, as detailed below. No
monotonicity or convexity of \(F\) is assumed.

The result concerns pointwise generator drift. It does not exclude a
nonsmooth or nonhomogeneous workload function, a function of residual
profiles, or drift sampled over a time interval. It does not imply instability.

## 1. Service when only one local route is present

Let \(j\in\{1,2\}\), and suppose only routes 0 and \(j\) are present. The
common link imposes \(\Lambda_0+\Lambda_j\le1\). The other link only imposes
\(\Lambda_0\le1\), which is redundant. Strict increase of the objective makes
the common-link constraint tight. Both rates are positive. Differentiating
with respect to aggregate rates gives

\[
 \kappa_0 n_0^\alpha\Lambda_0^{-\alpha}
 =\kappa_j n_j^\alpha\Lambda_j^{-\alpha}.
\]

This equation also follows directly for \(\alpha=1\) from the logarithmic
objective. Put \(a_i=\kappa_i^{1/\alpha}>0\). Solving the equation and the
tight capacity constraint yields

\[
 \Lambda_0=\frac{a_0n_0}{a_0n_0+a_jn_j},\qquad
 \Lambda_j=\frac{a_jn_j}{a_0n_0+a_jn_j}. \tag{2}
\]

For an integer \(N\ge1\), construct \(x_N^{(j)}\) with \(N\) route-0 files,
each of residual one, and \(N^3\) route-\(j\) files, each of residual
\(N^{-4}\). There are no files on the other local route. All residuals are
admissible for unit-size files, and

\[
 W(x_N^{(j)})=Ne_0+N^{-1}e_j,\qquad
 u_N^{(j)}:=W(x_N^{(j)})/N=e_0+N^{-2}e_j. \tag{3}
\]

Writing \(r_j=a_j/a_0\), formula (2) becomes

\[
 \Lambda_0(x_N^{(j)})=\frac1{1+r_jN^2}\longrightarrow0,
 \qquad
 \Lambda_j(x_N^{(j)})=\frac{r_jN^2}{1+r_jN^2}\longrightarrow1. \tag{4}
\]

Thus both sequences of normalized workloads approach \(e_0\), but their
limiting service vectors are \(e_1\) and \(e_2\), respectively.

## 2. Generator and its scaling limit

At any state with positive residuals, the workload evolves between arrivals as
\(W_i'=-\Lambda_i(n)\). Departures have no workload jump. A route-\(i\)
arrival adds \(e_i\). Consequently the local generator of \(V\) is

\[
 \mathcal G V(x)
 =\sum_{i=0}^2\nu_i\{F(W(x)+e_i)-F(W(x))\}
   -\sum_{i=0}^2\Lambda_i(n(x))\partial_iF(W(x)). \tag{5}
\]

All terms in (5) are finite. The formula needs neither a stationary law nor
an integrability assertion about one: it is the derivative over a sufficiently
short interval from the fixed finite state, before its first departure,
together with the Poisson arrival terms.

Write \(g_i=\partial_iF(e_0)\). Homogeneity and differentiation give

\[
 \partial_iF(Nu)=N^{d-1}\partial_iF(u). \tag{6}
\]

For any \(u_N\to e_0\), the fundamental theorem of calculus gives

\[
 \begin{aligned}
 N^{1-d}\{F(Nu_N+e_i)-F(Nu_N)\}
 &=N\{F(u_N+N^{-1}e_i)-F(u_N)\}\\
 &=\int_0^1\partial_iF(u_N+sN^{-1}e_i)\,ds
 \longrightarrow g_i. \tag{7}
 \end{aligned}
\]

The last convergence follows from continuity of the gradient in a fixed
neighborhood of \(e_0\); convergence of its arguments is uniform in
\(s\in[0,1]\). In particular this includes arrivals onto the absent local
route.

Apply (6)–(7) with (3) and use (4) in (5). For \(j=1,2\),

\[
 \lim_{N\to\infty}N^{1-d}\mathcal G V(x_N^{(j)})
 =D_j:=\frac15g_0+\frac12g_1+\frac12g_2-g_j. \tag{8}
\]

## 3. The incompatible inequalities

The two limiting drifts have sum

\[
 D_1+D_2=\frac25g_0. \tag{9}
\]

Radial differentiation of \(F(te_0)=t^dF(e_0)\) at \(t=1\) gives

\[
 g_0=dF(e_0)>0. \tag{10}
\]

Equivalently, choose \(j\) minimizing \(g_1,g_2\); then

\[
 D_j=\frac15g_0+\frac12|g_1-g_2|
 \ge\frac{dF(e_0)}5>0. \tag{11}
\]

Choose this fixed \(j\) and let \(x_N=x_N^{(j)}\). Equations (8) and (11)
prove (1). For all sufficiently large \(N\), they also give the explicit
eventual bound

\[
 \mathcal G V(x_N)\ge\frac{dF(e_0)}{10}N^{d-1}>0. \tag{12}
\]

Finally, by continuity and homogeneity,

\[
 V(x_N)=N^dF(u_N^{(j)})\sim N^dF(e_0)\longrightarrow\infty. \tag{13}
\]

This proves the stated obstruction, including when \(0<d<1\). In that case
the positive drifts may tend to zero, but they still contradict negative
drift outside any finite sublevel set.

## 4. Accessibility from empty

Equal residuals within a route need not occur from empty under Poisson
arrivals. The following construction removes reliance on that coincidence.
Fix the selected \(j\), take \(N\ge2\), and set

\[
 K=N^3,\qquad r=N^{-4},\qquad \eta=N^{-8},\qquad
 T=K(1-r).
\]

Starting empty, consider the event that there are exactly \(K\) route-\(j\)
arrivals and no other arrivals during an interval of length \(\eta\), then
no arrivals for time \(T\), then exactly \(N\) route-0 arrivals and no other
arrivals during a final interval of length \(\eta\). Independent Poisson
increments and strictly positive arrival rates give this event strictly
positive probability for every fixed \(N\).
More explicitly, writing \(\nu=\nu_0+\nu_1+\nu_2=6/5\), its probability is

\[
 e^{-\nu(T+2\eta)}
 \frac{(\nu_j\eta)^K}{K!}
 \frac{(\nu_0\eta)^N}{N!}>0. \tag{14a}
\]

No file departs during the first interval, since it starts with residual one
and can receive at most \(\eta<1\) service. At the end of that interval all
local residuals belong to \([1-\eta,1]\). While only these \(K\) files remain,
their aggregate service is one, so their individual rates are \(1/K\).
There is no departure in the middle interval: until a hypothetical first
departure, every residual is bounded below by

\[
 1-\eta-T/K=r-\eta>0,
\]

which rules out that departure. At its end all local residuals belong to
\([r-\eta,r]\). During the final interval every local file receives at most
\(\eta/K\) service, because its aggregate route rate is at most one. Hence
they remain present, with residuals in
\([r-\eta-\eta/K,r]\). Through-route residuals belong to \([1-\eta,1]\),
and they too remain present.

Let \(z_N\) be any state at the end of this event. Its counts are exactly
\((n_0,n_j)=(N,N^3)\), and its workloads satisfy

\[
 N(1-\eta)\le W_0(z_N)\le N,\qquad
 N^{-1}-N^3\eta-\eta\le W_j(z_N)\le N^{-1},\qquad
 W_{3-j}(z_N)=0. \tag{14}
\]

Thus \(W(z_N)/N\to e_0\), uniformly over the event. Formula (4) is unchanged,
and the gradient and finite-difference convergences in (6)–(7) are uniform
over (14). It follows that (8), (12), and (13) hold uniformly for these
reachable sets as well, with the same selected \(j\) and all sufficiently
large \(N\).

## 5. What the obstruction requires of a further argument

This example has deterministic files and link loads strictly below capacity.
Its obstruction is the loss of count and residual-profile information when
only total route workloads are retained. A local route can contain
\(N^3\) almost completed files and receive almost unit service while its
workload is only \(N^{-1}\). The smooth homogeneous function has essentially
the same gradient for either choice of that local route, and (9) forces a
positive drift for at least one choice.

These states last only a short time. At the exact states (3), for all
sufficiently large \(N\), if there is no arrival, all local files finish after

\[
 \frac{W_j}{\Lambda_j}
 =N^{-1}\left(1+\frac1{r_jN^2}\right),
\]

which tends to zero. Their instantaneous positive drift therefore gives no
obstruction to a negative drift over a longer interval. A proof of stochastic
stability may still exploit that distinction, or use a function that retains
residual-profile information or is outside the class in the theorem.

To justify this clearing-time formula, until the first departure the rates
are constant. No through-route file can depart before time \(N\): there
are \(N\) such files of residual one and each receives at most \(1/N\)
service per unit time while they all remain present. The displayed local
clearing time is less than \(N\) for all sufficiently large \(N\), so no
through-route departure changes the rates before the local files clear.
