# A two-time criterion for three sampled lineages

The result below reduces the three-label part of the N-BBM conjecture to a
joint law of two times. It also rules out convergence in the Skorokhod J1
topology on the finite partition space. It does not establish the required
joint law for N-BBM.

## 1. Definitions and statement

Let E be the five partitions of {1,2,3}. Write o for the partition into three
singletons, p_ij for the partition with the pair {i,j} and the remaining
singleton, and z for the one-block partition.

For each N, let Pi_N be a right-continuous, coarsening E-valued process
starting at o. Assume its law is invariant under permutations of {1,2,3},
every jump merges exactly two blocks, and it reaches z at a finite time.
Consequently it follows the path o -> p_J -> z, with times

    S_N = inf{t : Pi_N(t) != o},
    C_N = inf{t : Pi_N(t) = z},
    H_N = C_N - S_N > 0.

Here J_N is one of the three unordered pairs. All times in this note are on
the rescaled clock. For N-BBM one would take a_N = kappa (log N)^3 and use
physical backward time a_N t. The constant kappa is not determined here.

Let B be the restriction to three labels of the Bolthausen–Sznitman
coalescent, normalized to give two blocks merger rate one. Its defining rate
for a specified k-subset of b current blocks is

    lambda_(b,k) = integral_0^1 x^(k-2) (1-x)^(b-k) dx.

This definition is also given in Section 1.3 of
[Julien Berestycki, Nathanaël Berestycki and Jason Schweinsberg,
The genealogy of branching Brownian motion with absorption](https://arxiv.org/html/1001.2337v3).

**Theorem.** The following assertions are equivalent:

1. Pi_N converges to B in finite-dimensional distributions.
2. (S_N,H_N) converges weakly to (S,H), where S and H are independent,
   S has exponential law of rate 2, and

       Law(H) = (1/4) delta_0 + (3/4) Exp(1).

3. For every s,r >= 0,

       E exp(-s S_N - r H_N)
           -> (r+4) / [2(s+2)(r+1)].                         (1)

No Markov assumption is imposed on Pi_N.

## 2. Why the assumptions apply to a sample from N-BBM

Take an ordered uniform sample of three distinct particles, assigning the
sample labels 1,2,3 independently of spatial ranks. Relabelling the sample
does not change its law. This is the exchangeability used here; exchangeability
of particles ranked by position is neither assumed nor needed.

Backward ancestral identifications occur at forward branching events. At one
binary branch there are at most two surviving child lineages, so at most two
current sampled ancestral blocks can merge. A selection death alone does not
identify different ancestors. A crossing of Brownian paths does not identify
ancestors either. At fixed N the branching events have total rate N and
distinct times almost surely. Thus two sampled mergers cannot occur at exactly
the same time. These observations hold on any fixed finite backward window,
before and after deterministic rescaling.

The theorem requires a full path with finite merger times. If only a finite
history of physical length L_N is supplied, assume L_N/a_N -> infinity. After
this history ends, complete the path by merging uniformly chosen pairs at
successive, distinct later rescaled times. This preserves sample-label
exchangeability and binary jumps and gives finite merger times. It changes
no fixed bounded backward window for sufficiently large N. Thus the theorem
can be used without assuming a stationary population or proving finite
ancestral depth for the uncompleted history. Its convergence assertions are
then assertions about the chosen sequence of sampled histories.

## 3. The limiting two-time law

For three blocks, each specified pair has rate

    lambda_(3,2) = integral_0^1 (1-x) dx = 1/2,

and the triple has rate

    lambda_(3,3) = integral_0^1 x dx = 1/2.

There are three pair choices and one triple choice. The total first-event
rate is 2, so its time S has law Exp(2). Each of the four choices has
probability 1/4, independently of S: the density that a particular choice
occurs first at time u is (1/2) exp(-2u), which is 1/4 times the density of S.

If the choice is the triple, C=S and H=0. If it is a pair, there are two
blocks left, whose merger rate is

    lambda_(2,2) = integral_0^1 1 dx = 1.

The Markov property of B makes its subsequent holding time Exp(1), independent
of S and of the chosen first pair. This proves the law in assertion 2.
One may realize B using an additional uniform pair J independent of (S,H):

    B(t) = o       if t < S,
           p_J     if S <= t < S+H,
           z       if t >= S+H.                              (2)

The value of J is immaterial when H=0. Both S and C=S+H have continuous
distributions: S has a density, and adding the independent nonnegative H
cannot create an atom.

The joint transform is

    E exp(-sS-rH)
      = [2/(s+2)] [1/4 + 3/(4(r+1))]
      = (r+4)/[2(s+2)(r+1)].                                (3)

## 4. Proof of the equivalence

First, exchangeability implies an exact independence fact at every N. For a
Borel set A of time pairs, the three quantities

    P((S_N,H_N) in A, J_N = {i,j})

are equal: sample-label permutations preserve the times and act transitively
on the three possible pairs. Their sum is P((S_N,H_N) in A). Hence each is
one third of that probability. Therefore J_N is uniform and independent of
(S_N,H_N).

Suppose assertion 1 holds. Put K_N(t)=number of blocks of Pi_N(t), and let K
be the block count of B. For positive s,t, coarsening gives the exact identity

    {S_N <= s, C_N <= t} = {K_N(s) <= 2, K_N(t) = 1}.         (4)

Finite-dimensional convergence therefore gives convergence of the joint CDF
of (S_N,C_N) to that of (S,C). The latter CDF is continuous, because S and C
have continuous marginals. There is no loss of probability at infinity:
P(C_N>M)=P(K_N(M)>1) converges to P(C>M), which tends to zero as M tends to
infinity, and S_N <= C_N. The joint CDF criterion for weak convergence now
gives (S_N,C_N) -> (S,C). Applying the continuous map (s,c) -> (s,c-s) proves
assertion 2.

Conversely, suppose assertion 2 holds. The exact uniformity and independence
just proved give

    (S_N,H_N,J_N) -> (S,H,J),

with J uniform and independent. For any finite list of deterministic times,
formula (2) reconstructs the vector of partitions from these three variables.
That reconstruction is continuous at every (S,H,J) for which none of the
chosen times equals S or S+H. This includes H=0: a shrinking two-block interval
eventually misses each fixed time different from S. The exceptional equalities
have probability zero. The continuous mapping theorem proves assertion 1.

Assertion 2 implies assertion 3 by the bounded continuous functions
exp(-sS-rH) and formula (3).

For completeness, assertion 3 also implies assertion 2 without an unstated
tightness assumption. Set Y_N=exp(-S_N) and Z_N=exp(-H_N). These variables lie
in [0,1]^2. Applying (1) at nonnegative integer s,r gives convergence of every
mixed monomial moment to those of (exp(-S),exp(-H)). Linear combinations give
convergence for polynomials. Uniform approximation of continuous functions on
the compact square by polynomials then gives weak convergence of (Y_N,Z_N).
The limiting variables are strictly positive almost surely. The inverse map
(y,z) -> (-log y,-log z) is continuous there, so the continuous mapping theorem
gives assertion 2. This completes the proof.

## 5. A necessary burst statistic

Under the equivalent assertions, for every T,h>0 the limiting joint CDF gives

    P(S_N <= T, H_N <= h)
      -> (1-exp(-2T)) [1 - (3/4) exp(-h)].                   (5)

The boundary at H=h has zero limiting probability for h>0. Consequently

    lim_(h down to 0) lim_(N to infinity)
      P(S_N <= T, H_N <= h)
      = (1-exp(-2T))/4.                                    (6)

In physical units the event is that the first sampled merger occurs by a_N T
and the two successive sampled merger times differ by at most a_N h. Thus a
positive limiting portion of three-sample histories must have two mergers in
a vanishing fraction of the a_N clock. Formula (6) specifies an iterated
limit. It does not give a rate h_N -> 0 that works uniformly in N, and it
does not assert an atom at zero for any finite N.

There is also a necessary estimate involving only observations on a finite
grid. Fix T>0, an integer m>=1 and delta=T/m. Then

    liminf_N P(H_N <= delta, C_N <= T)
      >= [(2-exp(-delta))/(2(1+exp(-delta)))]
           (1-exp(-2T)).                                   (7)

To prove this, for j=0,...,m-1 use the events

    E_(N,j) = {K_N(j delta)=3, K_N((j+1)delta)=1}.

They are disjoint by coarsening. On each event both binary mergers occur
in (j delta,(j+1)delta], so H_N<=delta and C_N<=T. Their probabilities converge
by assertion 1. Starting from three blocks in B, let u=exp(-delta). The
probability to have two blocks at delta is

    integral_0^delta (3/2) exp(-2v) exp(-(delta-v)) dv
      = (3/2)(u-u^2).

The probability to have three blocks is u^2. Therefore

    p_(3,1)(delta) = 1-(3/2)u+(1/2)u^2.

Summing the limiting grid probabilities gives

    p_(3,1)(delta) sum_(j=0)^(m-1) exp(-2j delta)
      = [p_(3,1)(delta)/(1-u^2)] (1-exp(-2T))
      = [(2-u)/(2(1+u))] (1-exp(-2T)),

which proves (7). Sending m to infinity recovers the constant 1/4.

## 6. Failure of J1 convergence, with a quantitative separation

Equip E with the discrete metric d_E, equal to one for unequal states. On
D([0,T],E), use the bounded metric generating J1

    d_T(x,y) = min(1, inf_lambda max(
         sup_t |lambda(t)-t|,
         sup_t d_E(x(t),y(lambda(t))))),

where lambda ranges over increasing continuous bijections of [0,T]. Let A_T
be the set of coarsening paths starting at o with only binary jumps.

Consider a path y that jumps directly from o to z at a time in (0,T).
For every x in A_T and every lambda, the spatial supremum in this metric
equals one. Indeed, if x ever reaches z, it must visit a two-block partition
on a nonempty interval, whereas y never visits any two-block partition. If x
never reaches z, then x(T) differs from y(lambda(T))=y(T)=z. Thus

    d_T(y,A_T)=1.                                          (8)

Define F_T(x)=inf_(w in A_T) d_T(x,w). Distance to a nonempty set is a bounded
1-Lipschitz function, hence a continuous test function. For every finite-N
genealogy, F_T(Pi_N)=0. For B, F_T(B)=1 exactly when its first event is a
triple in (0,T), and is zero otherwise, apart from null endpoint events.
Section 3 gives

    E F_T(B) - E F_T(Pi_N) = (1-exp(-2T))/4 > 0.             (9)

This holds at every N and every deterministic positive rescaling of its clock.
Weak convergence in J1 would force the difference to tend to zero. It is
therefore impossible, even if the finite-dimensional conjecture is true.
For T=log 2 the separation in (9) is exactly 3/16.

## 7. What this reduction leaves open

The N-BBM-specific task is to establish (1), including its joint dependence,
for a suitable observation regime and time constant. The theorem proves no
such estimate. A result for three labels would still leave every larger
sample to be treated; four labels can also test disjoint merger events.

The unit pair-merger rate is a normalization, not a calculated N-BBM constant.
For B(rho t), rho>0, replace (3) by

    rho(r+4rho) / [2(s+2rho)(r+rho)].

The mixture weights 1/4 and 3/4 and the J1 obstruction remain the same.
