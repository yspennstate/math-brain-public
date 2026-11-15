# An explicit high-noise uniqueness criterion

Consider spins in {0,1} on Z^2. Every site has an independent Poisson clock
of rate one. At a clock ring the probability of setting the spin to 1, when
k of its four nearest neighbors have spin 1, is

\[
p_\varepsilon(k)=
\begin{cases}
\varepsilon,&k=0,1,\\
1/2,&k=2,\\
1-\varepsilon,&k=3,4.
\end{cases}                                                   \tag{1}
\]

Thus ties are resampled fairly, regardless of the previous spin. Throughout,
0 <= epsilon <= 1/2. The parameter epsilon is the probability of choosing the
minority at a strict majority, not the probability of fair noise resampling.

**Theorem.** The process (1) has exactly one stationary probability measure
whenever

\[
(2-4\varepsilon)(1-\varepsilon^3/2)<1.                         \tag{2}
\]

In particular it has a unique stationary measure for every
epsilon in [2481/10000, 1/2]. This is a sufficient condition only.

## 1. Construction and extremal measures

Attach an independent uniform mark U in [0,1] to each clock ring. Set the
updated spin to 1 if U <= p_epsilon(k), and to 0 otherwise. The same clocks
and marks couple any two initial configurations. The sequence p_epsilon(k)
is nondecreasing, so coordinatewise order is preserved.

This construction defines a Feller process on the compact product space
{0,1}^{Z^2}. To justify the infinite construction, explore the dependencies
of any finite set of spins backwards through a bounded time interval. At a
clock ring a dependency can be replaced by at most four dependencies, so
the number explored is bounded by a continuous-time branching process with
finite per-particle rate and at most four children. Its population has finite
expectation at each finite time and cannot explode. Hence each such
exploration is almost surely finite. The same argument, by truncating an
exploration to a finite spatial set, gives continuity of the semigroup on
local continuous functions and then on all continuous functions.

Write S_t for the semigroup. The laws delta_0 S_t increase in stochastic
order with t: delta_0 S_s >= delta_0, and applying the order-preserving S_t
gives delta_0 S_{s+t} >= delta_0 S_t. Similarly delta_1 S_t decrease. Their
limits exist. Indeed, probabilities that all sites in any specified finite
set are 1 are monotone; these probabilities determine every finite-dimensional
law by inclusion-exclusion. Compactness then gives weak limits, denoted
mu^- and mu^+. The Feller property and the semigroup identity show that both
limits are stationary. They are translation invariant.

Every stationary law nu satisfies mu^- <= nu <= mu^+, because
delta_0 S_t <= nu S_t = nu <= delta_1 S_t for all t. It therefore suffices to
prove mu^- = mu^+.

There is a translation-invariant stationary coupling lambda of mu^- and mu^+
for the shared-clock dynamics, supported on ordered pairs (eta,xi), eta<=xi.
Here is a construction that does not assume convergence of the joint law.
Start the pair at (0,1), and average its laws from time 0 to T. Compactness
gives a convergent subsequence of these averages. For any fixed s and bounded
continuous f, the difference between the average of S_s f and that of f is
bounded in absolute value by 2s||f||_infinity/T. The joint process is Feller
by the same finite-dependency argument. Thus any limit is stationary.
Its marginals are mu^- and mu^+, since the individual laws converge to these
limits. Order and translation invariance pass to the limit.

In this stationary coupled process let

\[
D_x=\xi_x-\eta_x\in\{0,1\},\qquad d=\mathbb E_\lambda D_x.
\]

Translation invariance makes d independent of x. Expectations below refer
to this stationary coupling and its future Poisson clocks and marks.

## 2. The stationary disagreement identity

Put a=1/2-epsilon, and let K_x(eta) be the number of 1 neighbors of x.
At a ring of x the expected new disagreement, conditional on the pre-ring
pair, is

\[
q_x(\eta,\xi)=p_\varepsilon(K_x(\xi))-
                         p_\varepsilon(K_x(\eta)).
\]

This follows by integrating the shared uniform mark between the two
thresholds. Only rings at x change D_x. Applying stationarity to the bounded
local function D_x therefore gives

\[
d=\mathbb E_\lambda q_x.                                      \tag{3}
\]

For a neighbor y of x define B_{x,y} to be the event that the other three
neighbors of x have one common value in both configurations. Explicitly,
either eta_z=xi_z=0 for all z in N(x)\{y}, or eta_z=xi_z=1 for all such z.

Change the four neighbor spins from eta to xi one at a time, in a fixed
order. Each change contributes either 0 or a to the increment of
p_epsilon: its consecutive increments, for k=0,1,2,3, are 0,a,a,0.
The contribution at y is at most a D_y. If B_{x,y} holds, that contribution
is zero: the other spins sum to 0 or 3 throughout the telescoping procedure,
and p_epsilon(0)=p_epsilon(1), p_epsilon(3)=p_epsilon(4).
Consequently the following deterministic inequality holds:

\[
q_x\le a\sum_{y\sim x}D_y(1-\mathbf1_{B_{x,y}}).               \tag{4}
\]

No independence between D_y and B_{x,y} is asserted.

## 3. Fresh noise bounds the missing influence

Fix x and y~x. The required bound is

\[
\mathbb E_\lambda[D_y\mathbf1_{B_{x,y}}]
                       \ge \frac{\varepsilon^3}{2}\,d.         \tag{5}
\]

To prove it, start the stationary pair at time 0, independently of future
clocks and marks, and fix T>0. For a ring at y at time r in (0,T], consider
the following future event, writing s=T-r:

* there is no further ring at y before T;
* each z in N(x)\{y} rings at least once in (r,T];
* the last marks in (r,T] at all three such sites are at most epsilon,
  or all three are greater than 1-epsilon.

Call this event F_r. Conditional on the entire history through the ring at
r, the probability of F_r is

\[
e^{-s}\,2\varepsilon^3(1-e^{-s})^3.                           \tag{6}
\]

Indeed, the no-ring probability at y is e^{-s}. The three other clocks are
distinct independent rate-one clocks. Each rings with probability 1-e^{-s};
conditional on its clock times its last mark is independent and uniform.
The two alternatives for the three marks have probability epsilon^3 each
and are disjoint, up to null endpoints. These facts depend only on future
clocks and marks and not on the coupled spins after the ring at r.

By (1), a mark at most epsilon forces the new spin to 1 in both copies,
whatever their neighbors; a mark greater than 1-epsilon forces it to 0.
Thus F_r implies B_{x,y} at time T. If D_y(r)=1 immediately after the ring,
it remains 1 at T, since there is no further ring at y. Moreover, at most
one ring r of y can satisfy F_r: it has to be the last ring before T.
Pathwise, therefore,

\[
D_y(T)\mathbf1_{B_{x,y}(T)}
 \ge \sum_{r\in\mathcal P_y\cap(0,T]}D_y(r)\mathbf1_{F_r}.      \tag{7}
\]

Here D_y(r) denotes the value after the ring.

For completeness, the expectation of the right side can be computed by
the unit-rate Poisson insertion formula. Insert a ring at a deterministic
time r, retain the stationary pre-ring pair, and draw its independent
uniform mark. The expected post-ring disagreement is E q_y=d by (3).
Future clocks and marks are independent of this pair and mark, so (6)
multiplies this expectation. A rate-one clock gives dr as the intensity
of inserted rings. Equivalently, this formula follows by summing conditional
expectations over intervals of length h, using a one-ring probability
h+O(h^2), and passing to the limit; all quantities here are bounded.
Taking expectations in (7) gives

\[
\begin{aligned}
\mathbb E[D_y(T)\mathbf1_{B_{x,y}(T)}]
&\ge 2\varepsilon^3d\int_0^T e^{-s}(1-e^{-s})^3\,ds\\
&=\frac{\varepsilon^3d}{2}(1-e^{-T})^4.
\end{aligned}                                                  \tag{8}
\]

The left side is independent of T by stationarity. Letting T tend to
infinity proves (5). Notice that the argument never conditions on a
disagreement at time T and then claims that its neighbors are independent.
The independence used in (6) is only from the history at the earlier ring.

## 4. Uniqueness and the explicit rational bound

Combining (3), (4), and (5), and using four neighbors, yields

\[
d\le4a(1-\varepsilon^3/2)d
  =(2-4\varepsilon)(1-\varepsilon^3/2)d.                       \tag{9}
\]

Under (2), d=0. Since the lattice is countable, the stationary coupling is
then supported on eta=xi: the union over all sites of {D_x=1} has probability
zero. Hence mu^-=mu^+, and the squeeze of all stationary measures between
these two laws proves uniqueness.

The factor C(epsilon)=(2-4epsilon)(1-epsilon^3/2) is strictly decreasing on
[0,1/2]: its first nonnegative factor strictly decreases, its second stays
positive and is nonincreasing. It is 2 at 0 and 0 at 1/2. Thus there is one
root epsilon_* of C(epsilon)=1, equivalently

\[
2\varepsilon_*^4-\varepsilon_*^3-4\varepsilon_*+1=0.            \tag{10}
\]

Criterion (2) is precisely epsilon>epsilon_*. To check the asserted rational
endpoint, substitute epsilon=2481/10000 into (10). Exact integer arithmetic,
with denominator 10000^4, gives

\[
2\cdot2481^4-2481^3\cdot10000
 -4\cdot2481\cdot10000^3+10000^4
\]

as the numerator. This integer equals -937568329358. Independently,

\[
C(2481/10000)=\frac{4999531215835321}{5000000000000000}<1.
\]

Thus the stated closed interval is covered. Exact rational bisection gives

\[
\frac{558619565237287}{2251799813685248}<\varepsilon_*
 <\frac{69827445654661}{281474976710656},
\]

so epsilon_* is approximately 0.248076921333013. The bracket has width
1/2251799813685248; its endpoint signs are checked in audit.py. Equality
in (2) is not covered by this proof.

This argument establishes uniqueness in a high-noise interval. It does not
establish coexistence at any positive noise, monotonicity of the coexistence
set in epsilon, or a sharp critical parameter.
