# Uniform sampled drift and recurrence in the two-link unit-file network

There are two links, both of capacity one. Route 0 uses both links,
route 1 uses the first, and route 2 uses the second. Independent Poisson
arrival processes have rates

\[
(\nu_0,\nu_1,\nu_2)=(1/5,1/2,1/2).
\]

Every arriving file has size one. The initial state consists of finitely
many files, each with residual work in \((0,1]\). For fixed
\(\alpha>0\) and fixed positive weights \(\kappa_i\), bandwidth is
allocated by weighted \(\alpha\)-fair sharing, equally among files on
the same route. The state includes all routes and residual works.
Write \(n_i(t)\) for counts, \(W_i(t)\) for workloads, and

\[
M(t)=W_0(t)+\max(W_1(t),W_2(t)),\qquad
a_0=\kappa_0^{1/\alpha}.
\]

Choose a finite \(c>0\) such that

\[
H(u_1,u_2):=(\kappa_1u_1^\alpha+\kappa_2u_2^\alpha)^{1/\alpha}
\le c(u_1+u_2)\quad(u_1,u_2\ge0).                    \tag{1}
\]

For example, \(c=(\kappa_1+\kappa_2)^{1/\alpha}\) suffices.
For equal weights normalized to one and \(\alpha=1\), take \(c=1\).

**Theorem.** For every fixed choice of \(\alpha\) and weights there
are finite \(B\) and \(\varepsilon>0\) such that

\[
\mathbb E_x[M(4)-M(0)]\le-\varepsilon
\quad\hbox{whenever }M(0)>B.                         \tag{2}
\]

There is no count bound or lower bound on individual initial residuals.
For equal weights and \(\alpha=1\), one can take

\[
B=65544,\qquad \varepsilon=\frac{2171}{20480}.          \tag{3}
\]

For every fixed choice of \(\alpha\) and weights, the residual-state
process in this specified unit-file network is positive Harris recurrent.
This theorem concerns this topology and input law; it does not prove
stability for arbitrary networks or general file-size distributions.

## 1. Allocation and a common potential local service

When \(n_0>0\), maximization of the weighted utility gives

\[
\Lambda_0=\frac{a_0n_0}{a_0n_0+H(n_1,n_2)}.             \tag{4}
\]

Indeed, every occupied local route saturates its own link, since otherwise
its allocation could be increased. Its rate is therefore \(1-\Lambda_0\).
If at least one local route is occupied, differentiating the strictly
concave objective after substitution of these tight constraints yields

\[
\kappa_0 n_0^\alpha\Lambda_0^{-\alpha}
=(\kappa_1n_1^\alpha+\kappa_2n_2^\alpha)
 (1-\Lambda_0)^{-\alpha}.
\]

The optimum is interior, by the infinite marginal utility at zero.
Solving gives (4), including logarithmic utility. If no local route is
occupied, \(H=0\) and Pareto efficiency gives \(\Lambda_0=1\), again
consistent with (4).

Define at every state

\[
q(t)=1-\Lambda_0(t),\qquad Q(t)=\int_0^t q(s)\,ds.
\]

Thus \(0\le Q(t)\le t\). Every occupied local route receives aggregate
rate \(q\). This holds also when \(n_0=0\): each occupied local route
then receives one, and \(q=1\). If the entire network is empty, set all
actual allocations to zero, so \(q=1\), with its potential local service
unused. These conventions preserve all the balance equations below.

## 2. Local reflection and the large-local-work region

Let \(w_j=W_j(0)\), \(m=\max(w_1,w_2)\), and let \(A_i(t)\) be
the arrival counts after time zero. Since files have size one,

\[
W_0(t)=W_0(0)+A_0(t)-t+Q(t).                          \tag{5}
\]

For \(j=1,2\), unused potential service on the local route is

\[
L_j(t)=\int_0^t q(s)1_{\{W_j(s)=0\}}\,ds.
\]

The local balance and reflection identities are

\[
W_j(t)=w_j+A_j(t)-Q(t)+L_j(t),\qquad
L_j(t)=\sup_{0\le s\le t}(Q(s)-w_j-A_j(s))^+.           \tag{6}
\]

Here the supremum also includes left limits at arrivals; including them
does not change its value. To verify the second identity directly, the
first and nonnegativity give \(L_j(t)\ge
\sup_{s\le t}(Q(s)-w_j-A_j(s))^+\). In the other direction,
\(L_j\) is continuous, starts at zero and can increase only where
\(W_j=0\). At every such time its value equals
\(Q-w_j-A_j\). Every attained positive level of \(L_j\) can therefore
be approximated by levels at times where this equality holds. Taking the
supremum proves the reverse inequality. There are finitely many arrivals
and departures on each bounded interval, so this reasoning can also be
applied interval by interval.

Since \(A_j\ge0\) and \(Q\) is nondecreasing, (6) implies

\[
L_j(T)\le(Q(T)-w_j)^+,
\qquad Q(T)+W_j(T)\le A_j(T)+\max(w_j,Q(T)).            \tag{7}
\]

Adding (5), maximizing (7) over \(j\), and subtracting the initial
maximum workload gives the pathwise bound

\[
M(T)-M(0)
\le A_0(T)-T+\max(A_1(T),A_2(T))+(Q(T)-m)^+.            \tag{8}
\]

In particular, if \(m\ge T\), the last term vanishes. This handles
both large local workloads and one large local workload, regardless of
through workload or population size.

Put

\[
d(T)=-\frac45T+\mathbb E\max(A_1(T),A_2(T)).             \tag{9}
\]

The local counts are independent Poisson variables of means \(T/2\).
Their difference has mean zero and variance \(T\). Consequently

\[
d(T)=-\frac3{10}T+\frac12\mathbb E|A_1(T)-A_2(T)|
\le-\frac3{10}T+\frac12\sqrt T.                       \tag{10}
\]

Thus \(d(4)\le-1/5\). From (8),

\[
\mathbb E_x[M(T)-M(0)]\le d(T)\quad\hbox{if }m\ge T.    \tag{11}
\]

## 3. A count-threshold bound when through work is large

Assume \(W_0(0)>T\), and let

\[
R=W_0(0)-T>0,\qquad L=A_1(T)+A_2(T).
\]

The through workload stays at least \(R\) up to time \(T\). Every
residual remains at most one, so \(n_0(t)\ge W_0(t)\ge R\).
Formula (4) therefore holds throughout this interval, even if original
through files depart.

For \(j=1,2\), let \(o_j(t)\) be the number of original local files
still present and let \(b_j(t)\) be the number of local files arriving
after time zero that are still present. Thus \(n_j=o_j+b_j\),
\(o_j\) is nonincreasing, and \(b_1+b_2\le L\).

Fix an integer \(K\ge1\). If \(o_j(0)>K\), let \(\tau_j\) be the
first time in \([0,T]\) when \(o_j\le K\), or \(T\) if that does not
happen. Set \(\tau_j=0\) if \(o_j(0)\le K\), and let
\(\tau=\max(\tau_1,\tau_2)\). These times are used only for a
pathwise estimate; no stopping or independence assertion about the
selected route is needed.

If \(\tau>0\), choose a route \(j\) attaining this maximum.
For almost every \(t<\tau\), its original count is greater than \(K\).
Its original files receive aggregate service

\[
q(t)\frac{o_j(t)}{o_j(t)+b_j(t)}
\ge q(t)\frac{K}{K+L}.
\]

They can receive at most their initial work \(w_j\). Integration gives

\[
Q(\tau)\le w_j(1+L/K)\le m(1+L/K).                    \tag{12}
\]

For \(\tau=0\), the same bound follows from \(Q(0)=0\).
If \(\tau<T\), both original local counts are at most \(K\) after
\(\tau\). By (1) and (4), for almost every such time,

\[
q(t)=\frac{H(n_1(t),n_2(t))}{a_0n_0(t)+H(n_1(t),n_2(t))}
\le\frac{c(2K+L)}{a_0R}.
\]

If \(\tau=T\), there is no remaining interval. Combining both cases
with (12) proves

\[
Q(T)\le m(1+L/K)+\frac{cT(2K+L)}{a_0R}.               \tag{13}
\]

No minimum original residual or maximum original count was used.
Since the right side of (13) minus \(m\) is nonnegative, (8) implies

\[
\mathbb E_x[M(T)-M(0)]
\le d(T)+\frac{mT}{K}+\frac{cT(2K+T)}{a_0R}.           \tag{14}
\]

Here \(\mathbb EL=T\). If \(m<T\), it follows in particular that

\[
\mathbb E_x[M(T)-M(0)]
\le d(T)+\frac{T^2}{K}+\frac{cT(2K+T)}{a_0R}.          \tag{15}
\]

This is the estimate missing when the original local work is bounded
but does not tend to zero.

## 4. Uniform drift and constants

Take \(T=4\). Choose any integer \(K\) such that \(16/K<1/10\),
and choose finite \(R_0\) large enough that

\[
\frac{4c(2K+4)}{a_0R_0}<\frac1{10}-\frac{16}{K}.
\]

Set \(B=R_0+8\). If \(M(0)>B\) and \(m\ge4\), (11) gives
drift at most \(-1/5\). If \(m<4\), then

\[
W_0(0)-4=M(0)-m-4>R_0.
\]

Equation (15) gives drift less than \(-1/10\). Thus (2) holds,
for example with \(\varepsilon=1/10\) and this choice of \(B\).

For equal weights and \(\alpha=1\), choose \(K=256\) and
\(R_0=65536\). The error in (15) is at most

\[
\frac{16}{256}+\frac{4(512+4)}{65536}
=\frac1{16}+\frac1{32}+\frac1{4096}.
\]

Its addition to \(-1/5\) is

\[
-\frac15+\frac1{16}+\frac1{32}+\frac1{4096}
=-\frac{2171}{20480}.
\]

This is greater than \(-1/5\), so it bounds both cases and proves (3).

## 5. Return to a bounded-workload set

Let \(T=4\), and fix any \(B,\varepsilon\) satisfying (2). Set
\(C=\{x:M(x)\le B\}\). At every arrival the increase of \(M\) is
at most one, and between arrivals \(M\) is nonincreasing. Hence

\[
M(t)\le M(0)+A_0(t)+A_1(t)+A_2(t),                    \tag{16}
\]

so all sampled workloads are integrable from each finite state.
For the skeleton \(Y_k=X(kT)\), let
\(\sigma=\inf\{k\ge0:Y_k\in C\}\). Summing conditional drift
up to \(n\wedge\sigma\), using the Markov property and (2), gives

\[
0\le\mathbb E_xM(Y_{n\wedge\sigma})
\le M(x)-\varepsilon\mathbb E_x(n\wedge\sigma).
\]

Monotone convergence therefore yields

\[
\mathbb E_x\sigma\le M(x)/\varepsilon,
\qquad \mathbb E_x(T\sigma)\le TM(x)/\varepsilon.       \tag{17}
\]

This argument needs no compactness or count bound for \(C\).

## 6. Emptying and regeneration

Write \(\nu=\nu_0+\nu_1+\nu_2=6/5\).
At every nonempty state the sum of actual aggregate service rates is at
least one. If there are no locals, the through rate is one. If there is
one occupied local, the sum is \(\Lambda_0+q=1\). If both locals are
occupied, it is \(\Lambda_0+2q\ge1\). These cases include an empty
through route. The total residual work in \(C\) is at most

\[
W_0+W_1+W_2\le2M\le2B.
\]

Choose a finite \(D\ge2B\). From any state in \(C\), no arrivals
for the next \(D\) time units guarantees an empty state at time \(D\).
The conditional probability of this event is the uniform positive number

\[
p=e^{-\nu D}>0.                                      \tag{18}
\]

For completeness, the following repeated-trial construction proves finite
mean emptying time without treating \(C\) as a compact or petite set.
First use (17) to reach \(C\). From that time run the process for \(D\)
units. If it is empty at the endpoint, stop. Otherwise inspect the process
every \(T\) units starting at that endpoint until it returns to \(C\),
and repeat. All these times are stopping times. Strong Markov and Poisson
independent increments apply at each one.

Conditional on the state at the start of a trial, (16) gives

\[
\mathbb E[M(X(D))]\le B+\nu D.
\]

By (17), the expected subsequent waiting time to \(C\), multiplied
by the indicator that the trial failed, is at most
\(T(B+\nu D)/\varepsilon\). The expected duration of a trial plus
its possible return is consequently at most

\[
H=D+\frac{T(B+\nu D)}{\varepsilon}.
\]

Each conditional failure probability is at most \(1-p\), by (18).
The probability that trial \(r\) is reached is therefore at most
\((1-p)^{r-1}\). Summing the conditional expected durations proves

\[
\mathbb E_x\tau_{\varnothing}
\le\frac{TM(x)}{\varepsilon}+\frac Hp<\infty.            \tag{19}
\]

The actual first emptying time is no later than the stopping time just
constructed, so (19) applies to it. No numerical approximation to the
very small positive probability \(p\) is needed.

Starting empty, wait for the first arrival, of mean waiting time
\(1/\nu\). Its state has \(M=1\). Equation (19) then gives a finite
mean time to the next empty state. Empty-to-empty cycles consisting of
this idle period and subsequent busy period are independent and identically
distributed, with finite positive mean length \(\mathbb E Z\).
There is no explosion, since each bounded interval has finitely many
arrivals and each file can depart only once.

Define the cycle occupation probability, for measurable \(E\), by

\[
\pi(E)=\frac{\mathbb E_{\varnothing}
 \int_0^Z1_{\{X(t)\in E\}}\,dt}{\mathbb E Z}.           \tag{20}
\]

To verify invariance, let \(f\) be bounded measurable and \(s\ge0\).
The Markov property, applied at deterministic times inside the integral
with the measurable indicator \(1_{\{t<Z\}}\), gives

\[
\mathbb E\int_0^Z P_s f(X(t))\,dt
=\mathbb E\int_0^Z f(X(t+s))\,dt.
\]

Subtracting the corresponding integral of \(f(X(t))\) leaves

\[
\mathbb E\int_Z^{Z+s}f(X(u))\,du
-\mathbb E\int_0^s f(X(u))\,du=0,
\]

by regeneration at \(Z\). Division by \(\mathbb E Z\) proves
\(\pi P_s=\pi\).

Finally, use the irreducibility measure
\(\psi=\delta_{\varnothing}\). Every finite initial state reaches
empty almost surely by (19). Every cycle contains an independent
exponential holding time at empty. Infinitely many such cycles occur,
and their total empty holding time diverges almost surely. Every measurable
set of positive \(\psi\)-measure contains empty and thus has infinite
occupation time almost surely from every initial state. This proves
\(\psi\)-irreducibility and Harris recurrence. Together with (20) it
proves positive Harris recurrence.

The restriction to unit arrivals and residuals at most one enters through
both the arrival-count workload identities and the lower bound
\(n_0\ge W_0\). These hypotheses cannot be removed by declaring the
workload vector alone to be a Markov state.
