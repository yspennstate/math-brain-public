# Propagation of the terminal-weighted family moment

All branching rates are one and branching is binary. At each branch the
leftmost particle is deleted, so the population size remains N. The results
below are finite-N estimates. They do not prove a genealogy limit.

## 1. The frozen forest polynomial

Fix deterministic physical times t_0<t_1<t_2<=t_3 and N>=4. At t_2 give
each particle its own color v. Let i(v) be its ancestor at t_1, and let
p(i) be the ancestor of i at t_0. These maps are frozen after t_2. Write
W_v(u) for the number of descendants of color v at time t_2+u, so
W_v(0)=1 and sum_v W_v(u)=N.

For a vector x=(x_v) of nonnegative integers put

    c_i(x) = sum_(v!=v': i(v)=i(v')=i) x_v x_v',
    zeta_z(x) = sum_(i: p(i)=z) c_i(x),
    F(x) = sum_(z!=z') zeta_z(x) zeta_z'(x),
    Q(u) = F(W(u))/(N)_4.

All sums over unequal indices are ordered. This Q(t_3-t_2) is exactly the
terminal-weighted statistic in round 4. In particular

    c_i(x) = (sum_(v:i(v)=i) x_v)_2
                 - sum_(v:i(v)=i) (x_v)_2.

To see its polynomial structure, let C be the set of ordered quadruples
(a,b,c,d) of t_2 particles satisfying

    a!=b, c!=d, i(a)=i(b), i(c)=i(d),
    p(i(a))!=p(i(c)).

The last inequality forces the two pairs to be disjoint. Thus all four
colors in any member of C are distinct, and

    F(x) = sum_((a,b,c,d) in C) x_a x_b x_c x_d.             (1)

Consequently F has nonnegative coefficients, is homogeneous of degree
four, and has degree at most one in each separate variable. The older
ancestor filter remains part of C throughout.

For a uniform ordered sample of four distinct particles at t_2+u, the
probability, conditional on the full forest, of four distinct t_2
ancestors, a 2+2 partition at t_1, and two distinct ancestors at t_0 is

    3 Q(u).                                               (2)

Indeed (1) counts samples for the prescribed pairing {1,2}|{3,4}; dividing
by (N)_4 gives its probability. The three possible pairings are disjoint.
This also gives 0<=Q(u)<=1/3.

## 2. Conditional propagation and the selection loss

Let H_2 be the history of the population positions and forest through t_2.
For every deterministic L>=0 with the future process defined,

    E[Q(L) | H_2] <= exp(4L) Q(0).                         (3)

Here Q(0) uses the genuine unweighted t_2 population. It is not substituted
for Q(L) in the sampling identity.

**Proof by unselected trees.** Conditional on H_2, grow independent
unselected BBM trees from the N particles at t_2. Prune the selected deaths
and their future descendants to obtain N-BBM. If Y_v(L) is the size of
the unselected tree of color v, then W_v(L)<=Y_v(L) pathwise. Tree sizes
are independent Yule processes and E Y_v(L)=exp(L). Hence for four distinct
colors,

    E[W_a(L)W_b(L)W_c(L)W_d(L) | H_2] <= exp(4L).

Sum over C in (1). Since F(1)=|C|, this proves (3). No independence of
the selected families is assumed. □

There is also an exact expression for what is lost through selection.
It clarifies the term a stronger estimate would have to control. If e_a
denotes a coordinate unit vector and partial_b F the formal derivative,
then for any current selected configuration with color counts x,

    generator F(x) = 4 F(x) - R,
    R = sum_(particles r) partial_(b(r)) F(x+e_(a(r))) >= 0. (4)

Here a(r) is the color of the particle that branches, and b(r) is the color
of the particle removed after that branch. If ties require random choices,
the summands mean their conditional expectations. Each particle branches
at rate one. The derivative is evaluated after the birth.

To verify (4), first add the child without deleting anyone. Multilinearity
gives F(x+e_a)-F(x)=partial_a F(x). Summing over parents yields

    sum_a x_a partial_a F(x) = 4 F(x),

because every monomial in (1) has four distinct factors. Now remove one
particle of color b. The loss is

    F(x+e_a)-F(x+e_a-e_b) = partial_b F(x+e_a).

It is nonnegative: the derivative has nonnegative coefficients and the
post-birth coordinates are nonnegative. This identity also holds when a=b;
the birth and death then cancel. Brownian motion contributes zero, since
F depends only on color counts. This proves (4).

Put r(u)=R(u)/(N)_4. Dynkin's formula and an integrating factor give

    E[Q(L) | H_2]
      = exp(4L) Q(0)
          - integral_0^L exp(4(L-u)) E[r(u) | H_2] du.       (5)

For completeness, all color counts are at most N, F is a fixed finite
polynomial, and total branching rate is N. Thus F and the jump generator
are bounded at this fixed N, the conditional expectation is absolutely
continuous, and the integrating-factor calculation is valid. Formula (5)
proves (3) a second way, retaining the selection deaths explicitly.

## 3. A weighted short-window estimate away from sampling

Write ell=t_2-t_1 and L=t_3-t_2. Uniformly over starting positions and
over the older forest,

    3 E Q(L) <= min(1,
       12 exp(4L+2ell)(exp(ell)-1)^2 / ((N-2)(N-3))).       (6)

The bound does not depend on t_1-t_0, provided that older history exists.
It also holds conditional on the history through t_1, with the expectation
on the left interpreted accordingly.

To prove it, apply (3) and then (2) with sampling at t_2. Dropping the
older filter only increases that sampling probability. If nu_i is the
number of t_2 descendants of particle i at t_1, its remaining bound is

    P(2+2 at t_1 for a sample at t_2)
      = 3 E sum_(i!=j) (nu_i)_2(nu_j)_2 / (N)_4.

Independent unselected Yule families dominate nu_i. Their second factorial
moment is 2 exp(ell)(exp(ell)-1). Thus the right side is at most

    3 N(N-1) [2 exp(ell)(exp(ell)-1)]^2/(N)_4,

which gives (6). The other argument of the minimum follows from (2).

In the exact regime of round 4, a_N=(log N)^3 and tau_N=(log N)^4,
the result reads, whenever s+delta+e<=log N,

    3 E Q_N(s,delta,e) <= min(1,
       12 exp(4a_N s+2a_N delta)(exp(a_N delta)-1)^2
             / ((N-2)(N-3))).                             (7)

This retains both terminal weights and the older ancestor filter. For
fixed N and fixed physical L, (6) is O(ell^2) as ell tends to zero.
It is not uniform on the conjectured rescaled clock: for fixed s,delta>0
the second argument in (7) tends to infinity.

For example the round-4 sliding-window argument now gives an explicit
bound away from the sampling endpoint on a physical clock. Define S,U,V,
H=U-S,G=V-U,D as in that report, but in physical time. If 0<h<epsilon/4
and the observation time tau satisfies tau>T+2h+epsilon, then

    P(S<=T,H<=h,G>=epsilon,D=1)
       <= min(1, K_N(h) [1+(exp(4T)-1)/(4h)]),
    K_N(h) = 12 exp(4h)(exp(2h)-1)^2 / ((N-2)(N-3)).       (8)

Indeed its endpoint window probability is at most K_N(h), and the window
starting at s is at most exp(4s)K_N(h) by (6) with ell=2h, L=s. Integrate
over 0<=s<=T, divide by h, and use the lower sliding-window inequality.
The history assumption covers the event and all these windows. For fixed
T,epsilon, the expression before the minimum has leading term

    12(exp(4T)-1)h/((N-2)(N-3)) + O_(N,T)(h^2).

This is a physical-time estimate, not the required iterated limit at
fixed positive rescaled T.

## 4. Sharpness for actual N-BBM

The factor exp(4L) in (3) cannot be decreased in a bound uniform over N and
particle positions. More strongly, it is asymptotically attained for
L<= (1-eta)log N, for any fixed eta in (0,1), by the configurations below.

Take N>=5. At the younger time mark four particles by colors 1,2,3,4
and place them in [N,N+1]. Put the remaining N-4 particles in [-1,1].
Give colors 1 and 2 one middle ancestor A, and colors 3 and 4 another
middle ancestor B. Give every other younger color its own middle ancestor.
Require A and B to have distinct older ancestors. Two additional middle
particles have no descendants at the younger time, so the middle
population also has N particles. Then

    c_A(x)=2x_1x_2,  c_B(x)=2x_3x_4,
    F(x)=8x_1x_2x_3x_4,
    Q(0)=8/(N)_4.                                        (9)

All other c_i are zero. The older filter is therefore fully present.
These marked configurations are compatible with N-BBM prefixes: start
with two separated leaders and N-2 particles near zero; the two leaders
each branch once, killing two low particles, while the other particles
do not branch. Before that interval let the two leaders have distinct
ancestors. Brownian paths staying in suitable tubes and the stated
finite branching pattern have positive probability. The estimates below
hold uniformly over the displayed position intervals, so exact positions
need not be conditioning events of positive probability.

Grow independent unselected trees from the younger population. For the
four leaders let Y_j(u) be their Yule sizes and put Z(u)=sum_(j=1)^4 Y_j(u).
Write P_L=product_(j=1)^4 Y_j(L).

Let A_N(L) be the event that some ancestral path in any of these N
unselected trees has Brownian displacement at least N/3 in absolute value
by time L. For L>0,

    P(A_N(L)) <= b_N(L)
      := 4 N exp(L) exp(-N^2/(18L)).                       (10)

Here is a direct justification. Conditional on its branching tree, each
terminal leaf's concatenated Brownian path has the law of a Brownian
motion of duration L. The expected number of leaves is N exp(L).
Reflection and a Gaussian exponential bound give

    P(sup_(u<=L)|B(u)|>=r) <= 4 exp(-r^2/(2L)).

Every earlier path is extended by a terminal leaf because the unselected
trees have no deaths. Thus the expected number of bad terminal paths
bounds the probability of any bad path. Set r=N/3 to get (10).

On A_N(L)^c all leader descendants stay strictly to the right of all low
descendants: their positions are at least 2N/3 and at most 1+N/3,
respectively. If also Z(L)<N, no leader descendant is removed before L.
To check this, induct over selected branching events. At any such event
the unselected leader population is at most Z(L)<N. If no leader has yet
been killed, the post-birth selected population contains a low particle;
the leftmost deletion therefore removes a low particle. This preserves
all leaders. Consequently

    W_j(L)=Y_j(L), j=1,2,3,4,
         on {Z(L)<N} intersect A_N(L)^c.                  (11)

Always W_j(L)<=Y_j(L). Independence and the Yule moments give

    E P_L = exp(4L),
    E[P_L Z(L)] = exp(4L)(8exp(L)-4),
    E P_L^2 = exp(8L)(2-exp(-L))^4.                        (12)

For the second identity, sum four terms, each equal to
E Y_1(L)^2 [E Y_1(L)]^3, and use
E Y_1(L)^2=2exp(2L)-exp(L). The third follows by multiplying four such
second moments.

Using (11), the loss from the unselected product is bounded by

    E[P_L 1_{Z(L)>=N}] + E[P_L 1_{A_N(L)}].

Bound the first term by E[P_L Z(L)]/N, and the second by Cauchy–Schwarz
and (10). It follows that

    0 <= 1 - E[product_j W_j(L)]/exp(4L)
       <= (8exp(L)-4)/N
             + (2-exp(-L))^2 sqrt(b_N(L)).                (13)

In particular, at each fixed L the right side tends to zero. By (9),

    E Q(L)/Q(0) -> exp(4L).                               (14)

Thus any replacement for exp(4L) valid for every N, position and compatible
marked forest must be at least exp(4L) at each L. If instead
0<L_N<=(1-eta)log N, the first term in (13) is at most 8N^(-eta).
The second tends to zero uniformly in this range, since exp(L_N)<=N and
L_N<=log N, while exp(-N^2/(18L_N)) decays faster than every power of N.
Hence the ratio in (14), divided by exp(4L_N), tends to one in this range.

One can also see a nonvanishing amplification of the sampling probability.
Set L_N=log(N/16), for N>16. The right side of (13) is at most
1/2-4/N+o(1). Equations (2), (9) and exp(4L_N)=(N/16)^4 give

    liminf_N 3 E Q(L_N) >= 12/16^4 = 3/16384 > 0,
         whereas 3Q(0)=24/(N)_4 -> 0.                    (15)

This uses deterministic future durations. For each N the assertion holds
conditionally on any frozen marked state of the indicated form; it is
not an unconditional statement for the all-zero long-time regime.

## 5. Remaining estimate

The propagation lemma controls terminal weights, but its optimal uniform
factor is too large on log-cubed horizons. Formula (15) also prevents a
position-uniform replacement by a bounded factor even on logarithmic
future horizons. The separated-leader example is not the observation
regime prescribed in round 4 and does not contradict the conjecture.

The missing input is information about the law of the actual spatial
configuration and its frozen ancestral colors at the younger time. In
particular, a useful application of (5) would have to control the
selection-loss integral for those random states, or estimate the
four-distinct-color descendant kernel after averaging over that law.
Neither estimate is established here. The averaged off-diagonal moment
on fixed rescaled windows, the marked-transform limits, the physical
clock constant and the full genealogy convergence remain open here.
