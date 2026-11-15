# Two-link stability with bounded through files and finite-mean local files

There are two links of capacity one. Route 0 uses both links, route 1
uses only link 1, and route 2 uses only link 2. For each route i, arrivals
form a Poisson process of rate nu_i>0, with independent identically
distributed file sizes B_i>0. Arrival processes and all marks are mutually
independent. Suppose

\[
  B_0\le b_0<\infty\quad\hbox{almost surely},\qquad
  \mathbb E B_i<\infty\quad(i=0,1,2).
\]

Write rho_i=nu_i E B_i and assume strict linkwise subcriticality:

\[
 \delta:=1-\rho_0-\max(\rho_1,\rho_2)>0.                 \tag{1}
\]

Fix alpha>0 and positive route weights kappa_i. At each state, the
weighted alpha-fair allocation maximizes

\[
 \sum_{i:n_i>0}\kappa_i n_i U_\alpha(\Lambda_i/n_i),
 \quad \Lambda_0+\Lambda_1\le1,\quad
 \Lambda_0+\Lambda_2\le1,
\]

where U'_alpha(s)=s^{-alpha}. Absent routes have allocation zero, and each
present route divides its allocation equally among its files. The state
X(t) records the finite collections of residual file sizes on the routes;
completed files are removed. The workload on route i is W_i, and

\[
 M=W_0+\max(W_1,W_2).
\]

**Theorem.** On the residual state space with route-0 residuals at most b_0,
there exist finite T>0, B>0 and epsilon>0 such that

\[
 M(x)>B\quad\Longrightarrow\quad
 \mathbb E_x[M(X(T))-M(x)]\le-\varepsilon.                \tag{2}
\]

There is no bound on initial finite file counts, no lower bound on
individual residuals, and no bound on local residuals. The residual-state
process is positive Harris recurrent. It remains positive Harris
recurrent if all finite residual states, including arbitrary finite
route-0 residuals, are admitted as initial states.

The theorem concerns this topology and independent marked Poisson input.
It does not cover unbounded through-file distributions, arbitrary
networks, or renewal arrivals.

## 1. Allocation and workload balance

Put a_0=kappa_0^{1/alpha} and

\[
 H(u_1,u_2)=(\kappa_1u_1^\alpha+\kappa_2u_2^\alpha)^{1/\alpha}.
\]

Fix c>0 with H(u_1,u_2)<=c(u_1+u_2) for nonnegative arguments.
For example c=(kappa_1+kappa_2)^{1/alpha} works: each u_j is at most
u_1+u_2, and raising to alpha, multiplying and adding proves the bound.
When alpha=1, c=max(kappa_1,kappa_2) suffices.

If n_0>0, strict increase of the objective forces every occupied local
route j to saturate its link, so Lambda_j=1-Lambda_0. If any local route
is occupied, differentiation of the reduced strictly concave objective
gives

\[
 \kappa_0n_0^\alpha\Lambda_0^{-\alpha}
 = (\kappa_1n_1^\alpha+\kappa_2n_2^\alpha)
   (1-\Lambda_0)^{-\alpha}.
\]

The occupied rates are positive by the infinite marginal utility at zero.
Solving gives

\[
 \Lambda_0=\frac{a_0n_0}{a_0n_0+H(n_1,n_2)}.            \tag{3}
\]

If no local is occupied this formula gives Lambda_0=1, as required by
Pareto efficiency. If n_0=0, each occupied local has rate one. Define

\[
 q(t)=1-\Lambda_0(t),\qquad Q(t)=\int_0^t q(s)\,ds,
\]

with Lambda_0=0 when route 0 is empty. Thus q=1 even if the entire
network is empty, but each empty local route leaves its potential service
unused. Every occupied local receives aggregate rate q, and 0<=Q(t)<=t.

Let N_i(t) count arrivals after time zero and let U_i(t) be the sum of
their file sizes. For w_i=W_i(0), pathwise balance gives

\[
 W_0(t)=w_0+U_0(t)-t+Q(t),                              \tag{4}
\]

and, for j=1,2,

\[
 W_j(t)=w_j+U_j(t)-Q(t)+L_j(t),\qquad
 L_j(t)=\int_0^t q(s)1_{\{W_j(s)=0\}}\,ds.              \tag{5}
\]

The deterministic allocation is fixed between arrivals and departures.
There are finitely many arrivals on every bounded interval, and no file
can depart twice. Hence these equations define a nonexplosive process
with a unique path from each finite state. The Poisson input with
independent marks and its memoryless future make the full residual-state
process strong Markov. Workloads alone are not asserted to be Markov.

## 2. Reflection and the pathwise drift estimate

The regulator in (5) satisfies

\[
 L_j(t)=\sup_{0\le s\le t}(Q(s)-w_j-U_j(s))^+.           \tag{6}
\]

Indeed, nonnegativity of W_j gives one inequality since L_j is
nondecreasing. For the reverse inequality, L_j is continuous and increases
only at times when W_j=0, where (5) gives L_j=Q-w_j-U_j. Every positive
level reached by L_j can be approximated at such times. Taking the
supremum gives (6). At upward arrival jumps one can include left limits;
the supremum is unchanged because Q is continuous.

Since U_j is nonnegative and nondecreasing,

\[
 L_j(T)\le(Q(T)-w_j)^+,
 \quad Q(T)+W_j(T)\le U_j(T)+\max(w_j,Q(T)).             \tag{7}
\]

Set m=max(w_1,w_2). Maximizing (7), adding (4), and subtracting w_0+m
yields

\[
 M(X(T))-M(x)
 \le U_0(T)-T+\max(U_1(T),U_2(T))+(Q(T)-m)^+.           \tag{8}
\]

In particular, if m>=T, the last term is zero. This needs no through
population or size bound.

## 3. A negative input benchmark with finite means alone

Define

\[
 d(T)=(\rho_0-1)T+\mathbb E\max(U_1(T),U_2(T)).          \tag{9}
\]

For h>0, let U_j^h(T) be the sum of min(B_j,h) over the route-j arrivals,
and put

\[
 v_j^h=\nu_j\mathbb E\min(B_j,h)^2,\qquad
 \eta(h)=\sum_{j=1}^2\nu_j\mathbb E(B_j-h)^+.
\]

Conditioning on the Poisson count and then on its independent marks gives

\[
 \mathbb E U_j^h(T)=\rho_j^hT,
 \quad\operatorname{Var}(U_j^h(T))=v_j^hT,
 \quad\rho_j^h=\nu_j\mathbb E\min(B_j,h)\le\rho_j.
\]

In detail, the conditional variance contributes nu_j T Var(min(B_j,h));
the variance of the conditional mean contributes
nu_j T (E min(B_j,h))^2. Their sum is v_j^hT.
Let R_j=U_j-U_j^h>=0. For r=max(rho_1,rho_2), each j satisfies

\[
 U_j(T)\le rT+|U_j^h(T)-\rho_j^hT|+R_j(T).
\]

Taking the maximum, bounding by the sum of both deviations and remainders,
and using Cauchy–Schwarz proves

\[
 \mathbb E\max(U_1(T),U_2(T))
 \le rT+(\sqrt{v_1^h}+\sqrt{v_2^h})\sqrt T+\eta(h)T.
                                                               \tag{10}
\]

Finite first moments imply eta(h)->0 by dominated convergence. First
choose finite h with eta(h)<=delta/4, and then finite T>0 with
(sqrt(v_1^h)+sqrt(v_2^h))/sqrt(T)<=delta/4. Equations (1), (9) and (10)
then give

\[
 d(T)\le-\delta T/2=:-\gamma<0.                         \tag{11}
\]

Only input marks were truncated in this estimate. No comparison or
monotonicity assertion about truncated queueing systems has been used.

For later explicit examples, if local second moments are finite, write
v_j=nu_j E B_j^2. Independence and
max(u,v)=(u+v+|u-v|)/2 give the sharper bound

\[
 d(T)\le-\delta T+\tfrac12\sqrt{(v_1+v_2)T}.           \tag{12}
\]

To see this with unequal means, write D=U_1-U_2 and use
E|D|<=|E D|+sqrt(Var D), where Var D=(v_1+v_2)T.

## 4. The count threshold uses a size cap only on route 0

Suppose w_0>T and put R=w_0-T>0. Equation (4) implies W_0(t)>=R for
0<=t<=T. As every through residual is at most b_0,

\[
 n_0(t)\ge W_0(t)/b_0\ge R/b_0.                       \tag{13}
\]

For each local route j, let o_j(t) count original files still present,
and b_j(t) count files that arrived after time zero and are still present.
Original counts are nonincreasing. Write L=N_1(T)+N_2(T); then
b_1(t)+b_2(t)<=L. This bound counts files and does not bound their work.

Fix an integer K>=1 and let h_*=m(1+L/K). If o_j(t)>K, then o_j(s)>K
for all s<t. On that interval the original files on route j receive rate

\[
 q(s)\frac{o_j(s)}{o_j(s)+b_j(s)}
 \ge q(s)\frac K{K+L}.
\]

They can receive at most their initial work w_j. Therefore
K Q(t)/(K+L)<=w_j<=m, whence Q(t)<=h_*. In particular, whenever Q(t)>h_*,
both original local counts are at most K. At almost every such time,
(3) and (13) give

\[
 q(t)\le\frac{H(n_1(t),n_2(t))}{a_0n_0(t)}
 \le\frac{c b_0(2K+L)}{a_0R}.                          \tag{14}
\]

If Q(T)<=h_*, the following bound is immediate. Otherwise Q is continuous
and nondecreasing, and its excess above h_* is the integral of its
derivative after crossing h_*. Equation (14) thus gives

\[
 Q(T)\le m(1+L/K)+\frac{c b_0T(2K+L)}{a_0R}.           \tag{15}
\]

No local size bound, lower residual bound, or initial count bound entered
this argument. It also covers the case that an original count stays above
K throughout the interval: in that case Q(T)<=h_* directly.

Put lambda=nu_1+nu_2, so E L=lambda T. Combining (8) and (15), using
nonnegativity of the right side of (15) minus m, gives

\[
 \mathbb E_x[M(X(T))-M(x)]
 \le d(T)+\frac{m\lambda T}{K}
             +\frac{c b_0T(2K+\lambda T)}{a_0R}.        \tag{16}
\]

No independence between L, Q, input work, or threshold events is needed;
the bounds were pathwise before expectations were taken.

## 5. Uniform drift outside a bounded-workload set

Choose T,gamma from (11). Choose a finite integer K>=1 and R_0>0 with

\[
 \frac{\lambda T^2}{K}\le\frac\gamma4,
 \qquad
 \frac{c b_0T(2K+\lambda T)}{a_0R_0}\le\frac\gamma4.
                                                               \tag{17}
\]

Set B=R_0+2T and epsilon=gamma/2. If M(x)>B and m>=T, (8) and (11)
give drift at most -gamma. If m<T, then
w_0-T=M(x)-m-T>R_0. Equation (16) and (17) give drift at most
-gamma/2. These cases exhaust all states above B and prove (2).

More generally, any explicitly verified bound d(T)<=-g<0 can replace
(11), with any K,R_0 for which the two errors in (16), with m<T and
R>=R_0, sum to less than g.

## 6. Finite expected emptying time

Let C={x:M(x)<=B}. An arrival increases M by at most its own size;
between arrivals all workloads are nonincreasing. Thus

\[
 M(X(t))\le M(x)+U_0(t)+U_1(t)+U_2(t).                 \tag{18}
\]

All finite-time workloads are integrable. For the skeleton Y_k=X(kT),
let sigma=inf{k>=0:Y_k in C}. Summing the conditional drift (2) up to
n wedge sigma and using nonnegativity yields

\[
 0\le\mathbb E_x M(Y_{n\wedge\sigma})
 \le M(x)-\varepsilon\mathbb E_x(n\wedge\sigma).
\]

Monotone convergence proves

\[
 \mathbb E_x(T\sigma)\le TM(x)/\varepsilon.             \tag{19}
\]

The same argument applies starting at any stopping time, with a new
skeleton spaced T time units from that time.

While the network is nonempty its total actual service rate is at least
one. With no locals it is one; with one occupied local it is Lambda_0+q=1;
with both locals it is Lambda_0+2q>=1. These cases include n_0=0.
Every state in C has total residual work
W_0+W_1+W_2<=2M<=2B. Therefore no arrivals for D=2B time units guarantees
an empty state at the endpoint. Put

\[
 \nu=\nu_0+\nu_1+\nu_2,\quad a=\rho_0+\rho_1+\rho_2,
 \quad p=e^{-\nu D}>0.
\]

Use (19) to reach C. Run a trial of duration D. If its endpoint is empty,
stop. Otherwise start a T-spaced skeleton at that endpoint, wait until C
is reached, and repeat. Every trial start is a stopping time. Conditional
on its starting history, success has probability at least p by Poisson
independent increments. Also (18) gives E M(X(D))<=B+aD, uniformly over
trial starting states. By (19), the expected return cost after failure,
including its failure indicator, is at most T(B+aD)/epsilon. Thus each
reached trial and its possible return have conditional expected duration
at most

\[
 H=D+T(B+aD)/\varepsilon.
\]

The probability of reaching trial r is at most (1-p)^{r-1}. Summing
expected durations therefore gives a constructed emptying time with
expectation at most TM(x)/epsilon+H/p. The actual first emptying time
tau_empty is no greater, so

\[
 \mathbb E_x\tau_{\rm empty}
 \le TM(x)/\varepsilon+H/p<\infty.                      \tag{20}
\]

This argument neither treats C as compact nor requires a count bound.
It does not divide an unconditional return-cost estimate by a failure
probability.

## 7. Invariance and Harris recurrence

Start empty and wait for the first arrival. Its waiting time has mean
1/nu, and its state has expected M equal to a/nu. By (20), the expected
time from that arrival to the next empty state is finite. Thus cycles
from empty to the next return to empty after at least one arrival are
independent identically distributed, with finite positive mean length Z:

\[
 \mathbb E Z\le1/\nu+Ta/(\nu\varepsilon)+H/p<\infty.
\]

Independence and identical laws follow from the strong Markov property
and fresh Poisson input at the return times. Infinite cycles cannot
accumulate in finite time because their independent exponential idle
portions have a divergent sum almost surely.

Define, for measurable E,

\[
 \pi(E)=\frac{\mathbb E_\varnothing
                \int_0^Z1_{\{X(t)\in E\}}\,dt}{\mathbb E Z}.
                                                               \tag{21}
\]

This is an invariant probability. For bounded measurable f and s>=0,
the Markov property at deterministic t and the fact that {t<Z} is
measurable by time t give, by Fubini,

\[
 \mathbb E\int_0^Z P_s f(X(t))\,dt
 =\mathbb E\int_0^Z f(X(t+s))\,dt.
\]

Subtracting E int_0^Z f(X(t))dt leaves
E int_Z^{Z+s}f(X(u))du-E int_0^s f(X(u))du=0 by regeneration at Z.
Division by E Z proves pi P_s=pi.

Use the irreducibility measure psi=delta_empty. Equation (20) shows that
every finite initial state in the stated residual space reaches empty
almost surely. Thereafter it visits empty in infinitely many cycles,
whose exponential holding times have infinite total length almost surely.
Every measurable set of positive psi measure contains empty, so it has
infinite occupation time almost surely from every initial state. This
proves psi-irreducibility and Harris recurrence. Together with (21), it
proves positive Harris recurrence. No stationary workload moment is
asserted.

## 8. Arbitrary finite initial through residuals

For a finite initial state x, let b_x be the maximum of b_0 and its
initial through residuals. It is finite. All through residuals subsequently
stay at most b_x. The proof through (20) applies with b_x replacing b_0;
its constants may depend on b_x. It follows that every such x has a
finite expected time to empty. Cycles starting empty use only arriving
sizes bounded by b_0, so their common invariant probability is still
(21). The same delta_empty argument proves positive Harris recurrence
on the enlarged space of all finite residual states. Uniform fixed-T
drift across all these enlarged states is not claimed.

## 9. Two explicit examples

First take nu=(1/5,1/2,1/2). Let B_0 and B_2 each be uniform on
{1/2,3/2}, and B_1 uniform on {1/4,7/4}. All means are one, so both link
loads are 7/10. Here b_0=3/2, lambda=1 and

\[
 v_1=25/32,\qquad v_2=5/8,\qquad v_1+v_2=45/32.
\]

At T=8, (12) and sqrt(45/4)<=7/2 give
d(8)<=-12/5+7/4=-13/20. For alpha=1 and all weights one, c=a_0=1.
Choose K=512 and R_0=65536. The two errors in (16) are at most

\[
 \frac{64}{512}
 +\frac{(3/2)8(1024+8)}{65536}
 =\frac18+\frac{387}{2048}=\frac{643}{2048}.
\]

Consequently

\[
 M(x)>65552\quad\Longrightarrow\quad
 \mathbb E_x[M(X(8))-M(x)]\le-\frac{3441}{10240}.         \tag{22}
\]

This uniform estimate uses initial through residuals at most 3/2 but
allows arbitrary finite local residuals.

For an infinite-variance example, keep the same B_0 and nu_0=1/5,
but set nu_1=nu_2=1/3 and let both local size laws satisfy

\[
 \mathbb P(B_j=2^n)=\frac{3}{4^{n+1}},\quad n=0,1,2,\ldots.
\]

The probabilities sum to one, E B_j=3/2 and E B_j^2=infinity. Both link
loads are again 7/10. Direct geometric summation, for integer k>=0, gives

\[
 \mathbb E(B_j-2^k)^+=2^{-(k+1)},\qquad
 \mathbb E\min(B_j,2^k)^2=(3k+4)/4.
\]

Take h=16 (k=4) and T=192 in (10). Then eta=1/48 and v_1^h=v_2^h=4/3;
the two square-root deviation terms are 16 each. Hence

\[
 d(192)\le-\tfrac3{10}\,192+32+192/48=-108/5.
\]

For equal weights and alpha=1, take K=4096 and R_0=2^20. The errors
in (16) are at most 6+2396160/1048576=6+2925/1280. Thus

\[
 M(x)>1048960\quad\Longrightarrow\quad
 \mathbb E_x[M(X(192))-M(x)]\le-\frac{17043}{1280}.       \tag{23}
\]

Here too initial through residuals are at most 3/2; local residuals may
be any finite values. This example illustrates that no local second
moment or bounded support is needed.
