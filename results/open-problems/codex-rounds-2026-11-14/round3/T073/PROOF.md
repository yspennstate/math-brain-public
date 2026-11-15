# A local propagation correction to the high-noise uniqueness bound

At each site of Z^2 a rate-one Poisson clock updates the spin in {0,1}.
If k of the four nearest neighbors have spin 1, the new spin is 1 with
probability

\[
p_\varepsilon(k)=
\begin{cases}
\varepsilon,&k=0,1,\\
1/2,&k=2,\\
1-\varepsilon,&k=3,4.
\end{cases}                                                     \tag{1}
\]

Ties are fairly resampled independently of the previous spin. Assume
0 <= epsilon <= 1/2 and put a=1/2-epsilon. Write

\[
C_0(\varepsilon)=4a(1-\varepsilon^3/2),\qquad
C_1(\varepsilon)=C_0(\varepsilon)
                 -\frac{17}{630}\varepsilon^4a^4.              \tag{2}
\]

**Theorem.** If C_1(epsilon)<1, the process (1) has exactly one stationary
probability measure. There is a unique number e_1 in (0,1/4) for which
C_1(e_1)=1, and the criterion holds precisely when epsilon>e_1 in [0,1/2].
Exact rational arithmetic gives

\[
\frac{146438707495522750369}{590295810358705651712}
 < e_1 <
\frac{1171509659964182002953}{4722366482869645213696}.          \tag{3}
\]

In particular, uniqueness holds throughout [0.24807685,1/2]. The earlier
criterion C_0(epsilon)<1 does not cover epsilon=0.24807685.
The improvement concerns high noise only.

## 1. An ordered stationary coupling

At every clock ring attach an independent uniform mark U in [0,1] and set
the spin to 1 precisely when U<=p_epsilon(k). Sharing these clocks and
marks preserves coordinatewise order because p_epsilon is nondecreasing.

This graphical construction gives a Feller process on the compact product
space {0,1}^{Z^2}. Here are the construction details needed below. For a
finite set of observed sites and a bounded time interval, explore
backward through the clocks. A dependency is replaced at an update by at
most four dependencies. The number of explored dependencies is dominated
by a branching process of rate one per dependency with four children per
branching. Its expected size at time t is at most its initial size times
e^{3t}; its expected total number of branchings in a bounded interval is
finite. Thus the exploration is almost surely finite. Truncating this
finite exploration to a large finite spatial region proves continuity of
the semigroup on cylinder functions. Uniform approximation then proves the
Feller property on continuous functions. The same reasoning applies to the
coupled process.

Let S_t denote the one-copy semigroup. The laws delta_0 S_t increase in
stochastic order: delta_0 S_s >= delta_0, and applying the order-preserving
S_t proves delta_0 S_{t+s} >= delta_0 S_t. The analogous laws delta_1 S_t
decrease. For every finite set A, the increasing cylinder event that all
spins of A equal 1 has a monotone probability. These probabilities determine
all finite-dimensional distributions by inclusion-exclusion. Consequently
the two laws converge weakly to measures mu^- and mu^+. Feller continuity
and the semigroup identity make these limits stationary. Both are
translation invariant. Every stationary law nu satisfies

\[
\mu^-\le\nu\le\mu^+,                                        \tag{4}
\]

by applying S_t to delta_0<=nu<=delta_1 and letting t tend to infinity.
No translation invariance of nu is required.

For the shared-clock pair started at (0,1), average the joint laws over
[0,T]. Compactness gives a subsequential weak limit lambda. Applying the
coupled semigroup for a fixed duration s changes the average expectation
of any bounded continuous function f by at most 2s||f||_infinity/T.
Feller continuity makes lambda stationary. Its marginals are mu^- and
mu^+, because their unaveraged laws already converge. It is supported on
ordered pairs and is translation invariant, as are the starting pair and
the dynamics.

Run the pair (eta,xi) from lambda, independently of future clocks and
marks. Put

\[
D_z=\xi_z-\eta_z,\qquad d=\mathbb E D_z.
\]

The value of d does not depend on z. If K_x counts the 1-neighbors of x,
the expected disagreement immediately after an update at x is

\[
q_x=p_\varepsilon(K_x(\xi))-p_\varepsilon(K_x(\eta)).
\]

The generator applied to D_x is q_x-D_x. Stationarity gives

\[
\mathbb E q_x=d.                                             \tag{5}
\]

## 2. The additional local slack

Let M_x=sum_{y in N(x)}D_y and define

\[
T_x=\sum_{\substack{A\subset N(x)\\|A|=3}}\prod_{y\in A}D_y
    =\binom{M_x}{3}.
\]

For y in N(x), let B_{x,y} be the event that all three sites in
N(x)\{y} are common in the two copies and equal to one another. The
following deterministic bound strengthens the earlier local bound:

\[
q_x\le a\left[\sum_{y\in N(x)}D_y(1-\mathbf1_{B_{x,y}})
                         -\frac12 T_x\right].               \tag{6}
\]

To prove it, write p_epsilon(k)=epsilon+a g(k), where

\[
(g(0),g(1),g(2),g(3),g(4))=(0,0,1,2,2).
\]

The successive increments of g are 0,1,1,0. Changing the four lower
neighbor spins to the upper ones one at a time therefore bounds the total
increment of g by sum D_y. If B_{x,y} holds, changing coordinate y has
zero increment: the other three spins sum to 0 or 3, and the relevant
increment of g is zero. This proves (6) without its T_x term.

If M_x<=2, then T_x=0, so this already proves (6). If M_x>=3, every
D_y*1_{B_{x,y}} is zero, since at least one other neighbor disagrees.
Always q_x<=2a. For M_x=3 the bracket on the right of (6) is
3-(1/2)*1=5/2>=2. For M_x=4 it is 4-(1/2)*4=2.
This proves (6) in every case, including a=0.

## 3. The earlier blocking term, re-derived

For every y in N(x),

\[
\mathbb E[D_y\mathbf1_{B_{x,y}}]
                     \ge\frac{\varepsilon^3}{2}d.            \tag{7}
\]

Fix T>0 and consider a ring at y at time r in (0,T], with s=T-r.
Require no further ring at y, at least one ring at each of the three
sites in N(x)\{y}, and last marks at those sites either all at most
epsilon or all greater than 1-epsilon. Its conditional probability given
the entire history through the ring at r is

\[
e^{-s}(1-e^{-s})^3\,2\varepsilon^3.
\]

The last marks force these three sites to a common value, irrespective
of all other spins and intervening updates. If D_y(r)=1 just after the
ring, it remains 1 through T. At most one ring r of y has no later ring.
Consequently, D_y(T)*1_{B_{x,y}(T)} is at least the sum over the candidate
rings of their post-ring disagreements times these successful events.

Take expectations by inserting a ring at each deterministic r with
intensity dr. The pre-ring pair has stationary law lambda; its fresh
mark gives expected post-ring disagreement E q_y=d by (5). Future clocks
and marks are independent of this history. This Poisson insertion formula
thus gives the lower bound

\[
2\varepsilon^3d\int_0^T e^{-s}(1-e^{-s})^3\,ds
  =\frac{\varepsilon^3d}{2}(1-e^{-T})^4.
\]

The left side of (7) is independent of T. Letting T increase proves (7).
This argument uses independence from the history at r, rather than
independence of neighboring spins conditional on a disagreement at T.

## 4. Broadcasting to three neighbors

For each fixed triple A in N(x), the new estimate is

\[
\mathbb E\prod_{y\in A}D_y
           \ge\frac{17}{1260}\varepsilon^4a^3d.               \tag{8}
\]

At epsilon=0 or epsilon=1/2 the right side of (8) is zero, so (8) is
immediate. Assume 0<epsilon<1/2 in its proof. The construction for each
triple is a rotation of the following construction, which omits the west
neighbor and takes A to be the north, east, and south neighbors of x.
No rotation invariance of lambda is needed. Label the four diagonal
sites, clockwise along the relevant path, as

\[
h_0=x+(-1,1),\quad h_1=x+(1,1),\quad
h_2=x+(1,-1),\quad h_3=x+(-1,-1),
\]

and label the three receivers r_0=x+(0,1), r_1=x+(1,0), r_2=x+(0,-1).
Receiver r_j has diagonal neighbors h_j and h_{j+1}.

Start with a source ring at x at time r in (0,T], at which the post-ring
disagreement is 1. For the future interval (r,T] require:

1. No further ring at x.
2. Each of the four helpers h_i and the three receivers r_j rings at
   least once.
3. If t_v is the last ring time of site v in this interval, then
   t_{h_j}<t_{r_j} and t_{h_{j+1}}<t_{r_j} for j=0,1,2.
4. The last helper marks force common values (0,1,0,1) along h_0,...,h_3,
   or force the opposite pattern (1,0,1,0).
5. At each receiver's last ring, the mark produces a disagreement.

Forcing 1 means a mark at most epsilon; forcing 0 means a mark greater
than 1-epsilon. At a receiver's selected last ring, its two adjacent
helpers have already been forced and have no later rings. They therefore
supply one common 0 and one common 1. The source supplies a disagreement
(0,1) and has no later ring. The remaining input, the outer axial
neighbor, can be any ordered pair (l,u) in {(0,0),(0,1),(1,1)}.
The lower and upper counts of 1-neighbors are 1+l and 2+u. The three
possible differences of update probabilities are respectively a, 2a, a.
Thus each receiver's selected update has probability at least a of
producing a disagreement, regardless of its past and of the axial input.

Here is a conditional argument for the product a^3. First fix the local
clock schedules satisfying requirements 1–3 and one of the two forced
helper patterns. Conditioning the four selected helper marks to their
forcing intervals leaves all selected receiver marks independent and
uniform. One can fix all other clock schedules and marks as well: by
causality, the state before a selected receiver ring is then a function
only of the selected receiver marks at earlier times. Reveal those three
marks in chronological order. Each selected mark is independent of the past and
of earlier selected successes. Its conditional success probability is
at least a by the preceding three-case calculation. Requirements on
helper marks that occur later than this receiver's selected ring do not
change this conclusion: those marks belong to other rings, are independent,
and cannot affect an earlier state. Iterating conditional expectations
therefore gives probability at least a^3 for all three successes.
No independence of the resulting receiver spins is asserted.

Each selected receiver ring is its site's last ring before T. Success
therefore makes the three receiver disagreements persist to T, even if
other sites keep updating.

## 5. The seven-clock partial order

Put s=T-r. Requirements 1 and 2 have probability

\[
e^{-s}(1-e^{-s})^7.
\]

Conditional on at least one ring at each of the seven sites, their last
ring times are independent and have the same continuous distribution.
Thus all 7! chronological orderings are equally likely. The inequalities
in requirement 3 form the path

\[
h_0<r_0>h_1<r_1>h_2<r_2>h_3.                                \tag{9}
\]

There are 272 allowed orderings. To count them explicitly, list the ranks
of the seven times in the order of the vertices displayed in (9).
This rank permutation has descent set exactly {2,4,6}. For a subset J
of these three positions, permutations whose descent set is contained
in J are increasing within the blocks cut at J. If those block lengths
are b_1,...,b_m, their number is 7!/(b_1!...b_m!). Inclusion-exclusion
therefore gives

\[
\begin{aligned}
N&=\frac{7!}{2!2!2!1!}
 -\left(\frac{7!}{2!2!3!}
        +\frac{7!}{2!4!1!}+\frac{7!}{4!2!1!}\right)
 +\left(\binom72+\binom74+\binom76\right)-1\\
 &=630-(210+105+105)+(21+35+7)-1=272.
\end{aligned}
\]

The two forced helper patterns have disjoint mark events of probability
epsilon^4 each. By Section 4, conditional on each pattern the three
selected successes have probability at least a^3. Thus, conditional on
the post-source history with D_x(r)=1, the full future event has probability
at least

\[
e^{-s}(1-e^{-s})^7\frac{272}{7!}\,2\varepsilon^4a^3.           \tag{10}
\]

At most one source ring can satisfy the no-later-source-ring requirement.
Pathwise, the product of the three receiver disagreements at T is at
least the sum of D_x(r) times the successful future-event indicators over
source rings r in (0,T]. The same Poisson insertion argument as in
Section 3, now using the lower bound (10), yields

\[
\mathbb E\prod_{y\in A}D_y(T)
 \ge d\,2\varepsilon^4a^3\frac{272}{7!}
                 \int_0^T e^{-s}(1-e^{-s})^7\,ds.
\]

The integral equals (1-e^{-T})^8/8. Letting T increase, using stationarity,
and simplifying 2*272/8!=17/1260 proves (8). The same construction applies
to every omitted receiver by rotation. In particular,

\[
\mathbb E T_x\ge 4\frac{17}{1260}\varepsilon^4a^3d.            \tag{11}
\]

## 6. Contraction and the interval

Taking expectations in (6), then using (5), (7), and (11), gives

\[
\begin{aligned}
d&\le4a\left(1-\frac{\varepsilon^3}{2}\right)d
       -\frac a2\,4\frac{17}{1260}\varepsilon^4a^3d\\
 &=\left[C_0(\varepsilon)-\frac{17}{630}\varepsilon^4a^4\right]d
   =C_1(\varepsilon)d.
\end{aligned}                                                  \tag{12}
\]

If C_1(epsilon)<1, this forces d=0. The lattice is countable, so the
ordered stationary pair then agrees at all sites almost surely. Hence
mu^-=mu^+, and (4) proves uniqueness of all stationary measures.

On [0,1/4], C_0 is strictly decreasing. Indeed, its first nonnegative
factor 2-4epsilon decreases strictly and its second positive factor
1-epsilon^3/2 is nonincreasing. The correction epsilon^4*a^4 equals
[epsilon*(1/2-epsilon)]^4, which is nondecreasing on this interval.
Thus C_1 decreases strictly there. Also C_1(0)=2 and
C_1(1/4)<=C_0(1/4)=127/128<1. This gives the unique root e_1 in (0,1/4).
For epsilon>=1/4, C_1<=C_0<1, so the claimed criterion is precisely
epsilon>e_1 on the full interval [0,1/2].

Writing F(epsilon)=630*(C_1(epsilon)-1), its expanded expression is

\[
F(e)=630-2520e-630e^3+
 \left(1260-\frac{17}{16}\right)e^4
 +\frac{17}{2}e^5-\frac{51}{2}e^6+34e^7-17e^8.                \tag{13}
\]

The rational numbers on the left and right of (3) give respectively
positive and negative F. Their difference is 1/4722366482869645213696.
These exact signs, an independent decimal grid bracket, and equality
between the factored and expanded formulas are checked in audit.py.
At e=0.24807685, exact rational evaluation gives

\[
\begin{aligned}
C_1(e)&=0.999999878141927758593318886796535559\ldots<1,\\
C_0(e)&=1.0000002897895762272616601520125>1.
\end{aligned}
\]

The new threshold is approximately 0.248076820004086075039. The earlier
threshold was approximately 0.248076921333013. Their difference lies
between 1.01328926215*10^{-7} and 1.01328926660*10^{-7}, as follows from
combining the earlier exact bracket with (3).

## 7. Limits and finite verification

The argument gives no uniqueness conclusion at e_1, and no coexistence
conclusion at any positive noise. It uses the fair-resampled tie rule (1),
not a retained-tie rule. No assertion of a sharp transition or monotonicity
of the coexistence set is made.

Run the two independent standard-library audits from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py
```

The second audit enumerates all 81 ordered local pairs; checks the three
possible axial inputs and all rotated diagonal patterns; counts the
seven-clock orderings by permutation enumeration, subset recursion, and
inclusion-exclusion; checks the age integral by exponential expansion;
and evaluates the root and contraction by exact rational arithmetic.
These finite checks support the written proof; they are not a formal
verification of its probabilistic arguments.
