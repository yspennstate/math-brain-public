# Pair disagreement slack in the fair-tie majority process

Each site of Z^2 has a rate-one Poisson clock. At a ring the spin is set
to 1 with probability

\[
p_e(k)=\begin{cases}
e,&k=0,1,\\
1/2,&k=2,\\
1-e,&k=3,4,
\end{cases}                                                   \tag{1}
\]

where k counts the 1 spins at the four nearest neighbors. In particular,
ties are fairly resampled, independently of the previous spin. Assume
0<=e<=1/2 and put a=1/2-e. Define

\[
\begin{aligned}
C_0(e)&=4a(1-e^3/2),\\
C_1(e)&=C_0(e)-\frac{17}{630}e^4a^4,\\
C_2(e)&=C_1(e)-\frac4{15}e^5a^3-\frac{16}{81}e^6a^3.
\end{aligned}                                                  \tag{2}
\]

**Theorem.** If C_2(e)<1, the process (1) has exactly one stationary
probability measure. There is a unique e_2 in (0,1/4) with C_2(e_2)=1,
and this sufficient criterion holds precisely for e>e_2 in [0,1/2].
The following bounds are exact:

\[
\frac{38387847911459845608705571}{154742504910672534362390528}
<e_2<
\frac{9596961977864961402176393}{38685626227668133590597632}.
                                                               \tag{3}
\]

Thus e_2 is approximately 0.24807565273432671232676944, and uniqueness
holds throughout [0.248076,1/2]. The preceding criterion C_1(e)<1 does
not cover e=0.248076. This theorem gives no positive-noise coexistence
conclusion.

## 1. Stationary ordered coupling

Give every clock ring an independent uniform mark U in [0,1]. Set the
new spin to 1 if U<=p_e(k), and otherwise to 0. The function p_e is
nondecreasing, so sharing clocks and marks preserves coordinatewise order.

The graphical construction defines a Feller process on the compact
product space {0,1}^{Z^2}. Indeed, backward exploration from finitely many
sites over a bounded time interval replaces each dependency by at most
four at a rate-one ring. A branching process with this rule has expected
population bounded by the starting population times exp(3t), and has
finite expected total number of rings on a bounded interval. The
exploration is therefore almost surely finite. Truncating it to a large
finite spatial set proves continuity of the semigroup on cylinder
functions, and uniform approximation proves the Feller property. The same
argument applies to the ordered pair process.

Let S_t be the one-copy semigroup. Attractiveness gives
delta_0 S_{s+t}>=delta_0 S_t and delta_1 S_{s+t}<=delta_1 S_t.
The probabilities of the increasing cylinder events that all spins of
a given finite set are 1 therefore converge. Inclusion-exclusion gives
convergence of every finite-dimensional distribution, and compactness
gives weak limits mu^- and mu^+. The Feller property and semigroup
identity show these limits are stationary. They are translation invariant.
Every stationary measure nu satisfies

\[
\mu^-\le\nu\le\mu^+,                                        \tag{4}
\]

by applying S_t to delta_0<=nu<=delta_1 and letting t tend to infinity.
The measure nu need not be translation invariant.

Start the ordered pair process at (0,1) and average its laws over [0,T].
Any subsequential weak limit lambda is stationary: for each fixed s,
applying the pair semigroup changes the average of a bounded continuous
function f by at most 2s||f||_infinity/T. Feller continuity passes this
identity to the limit. Its marginals are mu^- and mu^+, since their
unaveraged laws converge. Order and translation invariance also pass to
the limit.

Run (eta,xi) from lambda, independently of future clocks and marks, and put

\[
D_z=\xi_z-\eta_z,\qquad d=\mathbb E D_z.
\]

Translation invariance makes d independent of z. If K_x counts the
1-neighbors of x, let

\[
q_x=p_e(K_x(\xi))-p_e(K_x(\eta)).
\]

An update at x has expected new disagreement q_x. The generator applied
to D_x is q_x-D_x, so stationarity yields

\[
\mathbb E q_x=d.                                             \tag{5}
\]

## 2. The local inequality

Write N(x) for the four neighbors of x and put

\[
M_x=\sum_{y\in N(x)}D_y,\qquad
T_x=\sum_{\substack{A\subset N(x)\\|A|=3}}\prod_{y\in A}D_y
    =\binom{M_x}{3}.
\]

For y in N(x), let B_{x,y} mean that all three sites in N(x)\{y}
are common in the two copies and equal to one another. For an unordered
pair A contained in N(x), define E_A by

\[
D_y=1\ (y\in A),\qquad
\eta_z=\xi_z=b\ (z\in N(x)\setminus A)
\quad\hbox{for some }b\in\{0,1\}.
\]

These six events are disjoint. Define H_x=sum_{|A|=2}1_{E_A}.
The needed deterministic inequality is

\[
q_x\le a\left[\sum_{y\in N(x)}D_y(1-1_{B_{x,y}})
                    -\frac12T_x-H_x\right].                 \tag{6}
\]

For its proof, p_e(k)=e+a g(k), with g=(0,0,1,2,2). The consecutive
increments of g are 0,1,1,0. Telescoping from the lower neighbor vector
to the upper gives a total increment at most M_x. A disagreeing
coordinate contributes zero when the other three coordinates are common
and equal, removing the B_{x,y} terms. If M_x=0 there is no increment.
If M_x=1, the gap after this removal is zero: the increment is zero
when the other three are all 0 or all 1, and is one otherwise.

If M_x>=2, all D_y 1_{B_{x,y}} vanish. When M_x=2, let c be the number
of common 1-neighbors among the two remaining sites. The lower and upper
counts are c and c+2. For c=0,1,2 the increments of g are 1,2,1,
respectively. The gap from M_x=2 is thus exactly H_x. When M_x=3,
the counts are (0,3) or (1,4), the increment is 2, the gap is 1,
and T_x=1. When M_x=4 the increment is 2, the gap is 2, and T_x=4.
In these last two cases H_x=0. This proves (6); it also covers a=0.

## 3. A last-ring estimate

The following device will be used several times. Fix a source site v,
an observation time T, and a source ring r in (0,T], with s=T-r.
Require that the source have no later ring. Suppose a future success
event, when D_v(r)=1 immediately after the source ring, has conditional
probability at least

\[
\beta e^{-s}(1-e^{-s})^n,                                    \tag{7}
\]

uniformly over the post-ring history. Assume success implies a target
event F at T. The source can have at most one ring with no later ring,
so pathwise

\[
1_{F(T)}\ge
\sum_{r\in\mathcal P_v\cap(0,T]}D_v(r)1_{\{\text{success from }r\}}.
                                                               \tag{8}
\]

Insert a source ring at a deterministic r. Its pre-ring pair has law
lambda, and its independent mark gives expected post-ring disagreement
E q_v=d by (5). Future clocks and marks are independent of this history;
the uniform lower bound (7) can therefore be multiplied by D_v(r) and
averaged. The unit-rate Poisson insertion formula applied to (8) gives

\[
\mathbb P(F)\ge\beta d\int_0^T e^{-s}(1-e^{-s})^n\,ds
       =\frac{\beta d}{n+1}(1-e^{-T})^{n+1}.
\]

Here the insertion formula sums over possible rings with intensity dr;
inserting a deterministic ring leaves all earlier randomness unchanged.
The conditional bound is on future randomness and is uniform in the
pre-ring state. It does not assume independence conditional on D_v(T)=1.
Stationarity makes the left side independent of T, so letting T increase
proves

\[
\mathbb P(F)\ge\frac{\beta}{n+1}d.                           \tag{9}
\]

For clock constraints, consider n distinct nonsource sites required to
ring at least once after r. This has probability (1-e^{-s})^n.
Conditional on that event, their last ring times are independent and
identically distributed with continuous distribution. If L of their n!
orders satisfy the constraints, the clock portion of beta is L/n!.
Including the integral in (9) changes this to L/(n+1)!.

## 4. The preceding blocking and triple bounds

First, for each y in N(x),

\[
\mathbb E[D_y1_{B_{x,y}}]\ge\frac{e^3}{2}d.                  \tag{10}
\]

Use y as source. Hold its disagreement after r by requiring no further
ring. Require the other three neighbors of x to ring after r, and force
their last marks either all into [0,e] or all into (1-e,1]. A mark in
[0,e] forces a common 1, and one in (1-e,1] forces a common 0, regardless
of the inputs. These two disjoint choices have total probability 2e^3.
They imply B_{x,y}(T), and the source still disagrees. Taking n=3 and
beta=2e^3 in (9) proves (10).

Next, for each specified triple A in N(x),

\[
\mathbb E\prod_{y\in A}D_y\ge\frac{17}{1260}e^4a^3d.        \tag{11}
\]

It suffices to describe A={N,E,S} relative to x; the other triples are
rotations of this geometry. Take x as source and hold its disagreement.
The four diagonal helpers, in order NW,NE,SE,SW, are forced at their
last rings to alternating common values, either 0,1,0,1 or 1,0,1,0.
Each of the three receiver last rings must follow the last rings of its
two adjacent diagonal helpers. All seven sites must ring after r.

At each selected receiver ring its inputs include the source pair (0,1),
one common 0, and one common 1. Its outer axial input is an arbitrary
ordered pair (l,u) in {(0,0),(0,1),(1,1)}. Its lower and upper input
counts are 1+l and 2+u. The differences of update probabilities in these
three cases are a,2a,a. Thus each selected receiver update produces a
disagreement with conditional probability at least a.

To justify multiplication of these lower bounds, fix the clock schedules
and one helper assignment. Condition the selected helper marks into their
forcing intervals. Fix all remaining randomness except the selected
receiver marks. Those marks are still independent uniforms. Reveal them
in chronological order: causality makes each pre-ring state a function
only of previously revealed selected marks. The source and the two
adjacent helpers have their required values throughout the relevant
interval. Consequently each conditional success probability is at least a,
and all three succeed with probability at least a^3. Conditioning on
other marks occurring later does not affect the independent selected
uniform or any earlier state. Each selected ring is the site's last
before T, so every resulting disagreement persists to T.

The seven-clock partial order is the alternating path

\[
NW<N>NE<E>SE<S>SW.
\]

Its number of linear extensions is 272. Indeed, ranking the seven times
in this displayed order gives a permutation with descent set {2,4,6}.
Permutations with descents allowed only at chosen cuts are increasing
inside each resulting block and are counted by the corresponding
multinomial coefficient. Inclusion-exclusion gives

\[
\begin{aligned}
L&=\frac{7!}{2!2!2!1!}
 -\left(\frac{7!}{2!2!3!}+\frac{7!}{2!4!1!}
                         +\frac{7!}{4!2!1!}\right)
 +\binom72+\binom74+\binom76-1\\
 &=630-210-105-105+21+35+7-1=272.
\end{aligned}
\]

There are two disjoint helper assignments, each with forcing probability
e^4. Applying (9) with n=7 yields
2e^4a^3*272/8!=17e^4a^3/1260, proving (11). For e=0 or a=0 the
right side is zero and no conditioning on forcing intervals is needed.
This endpoint observation applies also to the next two bounds.

## 5. Adjacent pair events

For each adjacent pair A in N(x),

\[
\mathbb P(E_A)\ge\frac1{15}e^5a^2d.                         \tag{12}
\]

Take A={N,E}. Hold a source disagreement at x after r. Use the three
helpers NW,NE,SE, forcing their last common values to 0,1,0 or 1,0,1.
Require the last ring of N to follow those of NW and NE, and that of E
to follow those of NE and SE. Force the remaining neighbors S and W
at their last rings to a common value b, with b either 0 or 1. All
seven nonsource sites must ring after r.

The two selected receivers each have a source disagreement, a common 0,
a common 1, and an arbitrary ordered axial input at their last rings.
The three-case calculation in Section 4 and its chronological conditional
argument give success probability at least a^2 for both. The forced
values of S and W impose no further ordering constraint: these sites
are neither receivers nor diagonal helpers. Their earlier histories
may influence other sites, but the selected helper marks overwrite
those histories, and the axial inputs are unrestricted.

The two helper assignments have total mark probability 2e^3. The two
equal blocker assignments have total mark probability 2e^2. These
choices use distinct marks and produce four disjoint combined assignments,
of total probability 4e^5. On success, N and E disagree at T while
S and W are common and equal; hence E_A holds.

The five constrained clock vertices form the path

\[
NW<N>NE<E>SE.
\]

The number of orders is the number of permutations on five elements
with descent set {2,4}. By the same block inclusion-exclusion calculation,
it is

\[
\frac{5!}{2!2!1!}-\binom52-\binom54+1=30-10-5+1=16.
\]

The two blocker clocks are free. Choose the five path positions among
seven positions and order the two distinct blockers in the rest. This
gives L=16*binom(7,5)*2!=672 allowed orders. Equation (9), with n=7,
then proves

\[
\mathbb P(E_A)\ge4e^5a^2\frac{672}{8!}d
                         =\frac1{15}e^5a^2d.
\]

Rotation gives the same construction for each of the four adjacent
pairs; rotation invariance of lambda is unnecessary.

## 6. Opposite pair events

For each opposite pair A in N(x),

\[
\mathbb P(E_A)\ge\frac8{81}e^6a^2d.                         \tag{13}
\]

Take A={N,S} and again hold a source disagreement at x. For N, force
NW and NE to opposite common values before N's last ring. For S, force
SW and SE to opposite common values before S's last ring. The two helper
pairs are disjoint, so there are four assignments, each of forcing
probability e^4. Force the remaining neighbors E and W at their last
rings to the same common value; there are two choices, each of
probability e^2. All eight nonsource sites must ring after r. These
choices have total forcing probability 8e^6. The same conditional
argument as in Sections 4 and 5 gives probability at least a^2 for the
two receiver successes, which persist to T. Success implies E_A.

The constrained clocks split into two disjoint groups of three, with
the receiver required to be last within its group. For independent
identically distributed continuous times, each group has probability
1/3 of this event, independently of the other group. The two blocker
clocks are unrestricted. The allowed fraction of all 8! orders is
therefore 1/9, giving L=4480. Equation (9) now gives

\[
\mathbb P(E_A)\ge8e^6a^2\frac{4480}{9!}d
                         =\frac8{81}e^6a^2d.
\]

Rotation treats the second opposite pair.

## 7. Contraction and numerical interval

Taking expectations in (6) and using (5), (10), and (11) yields

\[
d\le C_1(e)d-a\mathbb E H_x.
\]

There are four adjacent pairs and two opposite pairs. Summing their
bounds (12) and (13) gives

\[
\mathbb E H_x\ge
 \left(\frac4{15}e^5a^2+\frac{16}{81}e^6a^2\right)d.
\]

This summation is valid even though constructions for different pairs
use overlapping clocks: expectations are added separately, and their
target events are disjoint. Also H_x vanishes whenever T_x is nonzero,
so no pair slack has been charged against the previous triple correction.
Consequently

\[
d\le C_2(e)d.                                                \tag{14}
\]

If C_2(e)<1, (14) forces d=0. Since Z^2 is countable, the stationary
ordered pair agrees at every site almost surely. Its marginals coincide,
and (4) proves uniqueness of all stationary probability measures.

On [0,1/4], C_0 is strictly decreasing: 4a decreases strictly and
1-e^3/2 is positive and nonincreasing. Each subtracted correction in
(2) is nondecreasing there. To check this directly, in the interior

\[
\frac{d}{de}(e^m a^n)=e^{m-1}a^{n-1}(ma-ne),
\]

and ma-ne=m/2-(m+n)e is nonnegative on [0,1/4] whenever m>=n.
The three terms have (m,n)=(4,4),(5,3),(6,3). Thus C_2 is strictly
decreasing on [0,1/4]. Its values at the ends satisfy C_2(0)=2 and
C_2(1/4)<=C_0(1/4)=127/128<1. It has a unique root e_2 there.
For e>=1/4, C_2(e)<=C_0(e)<=127/128<1, proving the stated
characterization on [0,1/2]. No global monotonicity of C_2 is required.

For independent exact-arithmetic evaluation, expanding (2) gives

\[
\begin{aligned}
C_2(e)-1={}&1-4e-e^3+\frac{20143}{10080}e^4-\frac5{252}e^5
 +\frac{1529}{11340}e^6\\
 &-\frac{187}{945}e^7-\frac{107}{1890}e^8+\frac{16}{81}e^9.
\end{aligned}                                                  \tag{15}
\]

The endpoints in (3) give respectively positive and negative values of
(15), and differ by 1/154742504910672534362390528. Separately, the
decimal-grid rationals 0.2480756 and 0.2480757 have opposite signs.
At the rational endpoint used in the theorem, exact evaluation gives

\[
\begin{aligned}
C_2(0.248076)&=
\frac{3337855398443582394496741255036654301312159321701}
     {3337860107421875000000000000000000000000000000000}
 =0.999998589222393672254804273783232806\ldots,\\
C_1(0.248076)&=1.000003331257626955193313049185227268\ldots.
\end{aligned}
\]

Thus the new criterion strictly extends the preceding one. The decrease
in the sufficient threshold is approximately 0.00000116726975936.

## 8. Verification and limits

Run from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py
```

The first script independently checks the earlier local inequality,
triple clock coefficient and exact numerical claims. The second checks
all 81 local pairs, reconstructs (1) by random three-input majorities,
checks all six geometric cases and all helper assignments, and counts
clock orders by direct permutations and an independent order-ideal
recursion. The clock coefficients are also derived by the fence formula
and independent triple maxima. It checks the age integrals by exponential
expansion and substitution, the polynomial by coefficient multiplication,
and the root by exact bisection and separate decimal-grid signs.

These finite checks do not formally verify the infinite-volume or
conditional-probability arguments. Those arguments are given above.
There is no conclusion at e=e_2, no result for retained ties or synchronous
updates, and no proof of coexistence at any positive noise. No claim of
an optimal or new published uniqueness bound is made.
