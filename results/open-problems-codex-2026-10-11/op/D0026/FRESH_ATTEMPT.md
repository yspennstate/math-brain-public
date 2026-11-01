# One additional serious attempt (2026-10-11)

Baseline: ATTEMPT.md proves only special cases and reductions. Its sharp
single-infection gap is P_A(x in A(t)) -> q for the simultaneous-neighbor-
refresh dual, from every finite nonempty A. The full conjecture requires
more than this subclass.

## Two approaches not pursued in the first attempt

1. **An infinite-measure reversible heat-kernel argument.** On the countable
   sector of finite nonempty infection sets, detailed balance holds for the
   sigma-finite weight m(A)=(q/(1-q))^|A|. Unlike the equilibrium probability
   space, this space contains the finite-seed starts. Transfer the uniform
   finite-volume spectral gap to l2(m), then combine heat-kernel estimates
   with finite propagation and combinatorial entropy bounds. Test whether
   this excludes not just extinction but low infection cardinality, and
   whether it yields fixed-site occupation convergence. This works with
   singular starts directly instead of seeking global absolute continuity.

2. **A tagged surviving infection and its environment.** In the dual,
   if a ring at occupied x erases a tag at its neighbor y, move the tag
   to x, which remains occupied. Otherwise keep the tag. This constructs
   a nonextinguishing nearest-neighbor tag. A possible neighboring theorem
   is recurrence of a one-dimensional tagged particle in a stationary
   reversible environment. One would need to prove an appropriate invariant
   Palm law, recurrence, and a local regeneration implication. None is
   automatic: left and right instantaneous tag jump rates depend on the
   environment, and recurrence alone does not imply convergence at fixed
   times. This approach would require substantial additional work.

Approach 1 is selected: it has a concrete finite-volume input and a
referee-checkable consequence for the singular-start gap. Approach 2 is
recorded as an unproved research direction, not used as a lemma.

### A referee check on the tagged route

The natural forced-survival tag construction does not inherit the
reversibility required by the most direct neighboring tagged-particle
theorems. On the three-site cycle, consider marked states
s=({0,1}, tag at 0) and u=({1}, tag at 1). At s a ring of occupied
center 1 refreshes both neighbors 0 and 2 to healthy with probability
p^2, leaving center 1 occupied and moving the erased tag to 1. Thus
the joint transition rate s->u is p^2>0. At u the only occupied
ringing center is 1, which never changes its own state or its own tag;
it can create site 0 but cannot move its tag there in that same jump.
Thus the joint rate u->s is zero. Any measure giving both states
positive mass violates detailed balance on this edge. In particular,
a full-support uniform-tag/Palm candidate is not reversible.

This does not refute recurrence of the tag, or rule out a nonreversible
stationary marked law. It identifies a real missing hypothesis for the
naive application of a reversible stationary-environment tracer theorem.
It is an auxiliary construction check, not a counterexample to D0026.

## Inputs to verify, not assume silently

* Does the cited uniform gap concern the nonempty communicating class
  with healthy exterior? The unrestricted chain also has an absorbing
  empty state and therefore has spectral gap zero.
* Does the neighbor-refresh dual have the corresponding finite-volume gap?
* Can the l2(m) estimate be obtained as an actual limit of killed finite
  chains without assuming essential self-adjointness?
* Is the entropy bound on low-cardinality sets strong enough after allowing
  the finite-speed cone to grow linearly?
* Even if infection cardinality is linear, does that control a fixed site?
  This last implication is a possible remaining gap, not a valid shortcut.

## Fresh Lemma 1: uniform finite-volume gaps imply an infinite-sector gap

This lemma is proved with its finite-gap hypothesis explicitly stated.
Verification of that input for the present processes is recorded separately.

**Input subsequently verified:** the finite-gap hypothesis for both models
is established below from the independently inspected book Theorem 4.8,
with a complete interval-to-cycle comparison. The final growth conclusion
is therefore a proved consequence of a published theorem, not left as
a conjecture conditional on a numerical gap extrapolation.

Let S be the countable space of finite nonempty subsets of Z. Fix r>0,
and m(B)=r^|B|. Suppose a conservative Markov process on S is the fixed-time
limit, from each finite start, of finite-cycle chains on cycles C_n whose
size tends to infinity. Assume their nonempty-sector reversible weights are
m_n(B)=r^|B|, their spectral gaps are at least gamma>0, and the embedding
identifies every fixed finite collection of states for all sufficiently large
n. Fixed-time convergence here means convergence of each transition
probability between embedded finite subsets, e.g. via a finite-speed coupling.

Then the process is reversible with respect to m and, from each A in S,
its time-t law has counting-space density h_{A,t}(B)=P_t(A,B)/m(B) with

sum_B m(B) h_{A,t}(B)^2 <= exp(-2 gamma t)/m(A).           (H1)

In particular for every set E of states with m(E)<infinity,

P_A(B_t in E) <= exp(-gamma t) sqrt(m(E)/m(A)).           (H2)

Proof. The cycle's normalizing constant is
Z_n=sum_{B nonempty subset C_n} r^|B|=(1+r)^|C_n|-1 -> infinity.
Let h_{A,0}=1_{A}/m(A). For the finite cycle, reversibility identifies
P_t h_{A,0}(B)=P_t(A,B)/m(B). Spectral diagonalization on the finite
reversible Hilbert space gives

||P_t h_{A,0}||_{l2(m_n)}^2
 <= exp(-2 gamma t)||h_{A,0}||_{l2(m_n)}^2
      +(1-exp(-2 gamma t)) (sum_B m_n(B)h_{A,0}(B))^2/Z_n
 = exp(-2 gamma t)/m(A)+(1-exp(-2 gamma t))/Z_n.

This is the exact constant-mode correction; it must not be omitted at
finite n. For any fixed finite collection F of infinite-sector states,
pass to the transition-probability limit in the sum over F. Let n tend
to infinity in the displayed bound, then increase F to exhaust S.
Monotone convergence of the nonnegative sums proves (H1).
Detailed balance on each finite cycle passes to each pair A,B, giving
m(A)P_t(A,B)=m(B)P_t(B,A). Summing over A and using conservativity
shows sum_A m(A)P_t(A,B)=m(B), so m is invariant as well as reversible.
Finally weighted Cauchy-Schwarz on E proves (H2). QED.

This argument avoids an essential-self-adjointness assumption and any
exchange of n->infinity with t->infinity: n tends to infinity for each
fixed t, and the bound is already uniform in n and valid for every t.
The countable-space density h is NOT a density with respect to pi.

## Finite-gap input and boundary caution

The source, PDF page 27 in the proof of (6.2), explicitly states that
the FA-1f chain on the finite circle restricted to configurations with
at least one vacancy has a spectral gap uniformly positive in circle
size. We use that nonempty-sector statement, on even circles of size
at least four. It is distinct from the unrestricted healthy-exterior
chain, whose empty absorbing class makes its gap zero.

Source page 26 is less explicit about conditioning and cannot be read
literally as a positive gap for the unrestricted healthy-exterior chain.
Using periodic nonempty chains bypasses that ambiguity. Independent
verification has now been completed below.

### Independent verification of FG (completed)

Hartarsky and Toninelli, *Kinetically Constrained Models*, arXiv:2412.13634,
Theorem 4.8, printed page 39 / PDF page 49, states for a one-dimensional
general KCM of fixed range R on a finite interval Lambda, restricted to
any irreducible component C, that

T_rel <= (2/q)^[C_R log min(|Lambda|,2/q)].

The preceding definition explicitly uses mu=pi(.|C). All state spaces
are finite and each facilitating-state probability is at least q. This
is the precise needed component-wise uniform bound, not a boundary-pinned
bound or an infinite-volume equilibrium bound. Choose binary site spaces,
infection event {0} of probability q, range R=1, update family {{-1},{1}},
and healthy exterior. The nonempty class is irreducible by ATTEMPT.md,
Proposition 5; the conditional stationary law is exactly the required
Bernoulli(q) infection law conditioned nonempty. The theorem gives

gap(F_interval) >= g(q):=(2/q)^[-C_1 log(2/q)] > 0,

uniformly over intervals of length at least two. When the interval's
endpoints are joined to form a cycle, the FA constraint can only become
satisfied at more configurations. The stationary conditioned law and
variance denominator are unchanged, so D_cycle>=D_interval pointwise
after integrating over that law. Thus gap(F_cycle)>=g(q) as well.
Cycles of size at least three suffice, and an even-size subsequence
can be used throughout Fresh Lemma 1. This proves FG from the published
Theorem 4.8 and an explicit form comparison. Shapira's separate note
does not prove this uniform bound: its finite-graph theorem is an upper
bound in a volume-density scaling regime; it is not used as FG.

Consequently Fresh Lemmas 1-3 apply unconditionally to the present
models with gamma=g(q) for FA-1f and gamma=g(q)/2 for the dual. A stronger
finite-dimensional comparison below permits gamma=g(q) for both.

## Fresh Lemma 2: the dual inherits half the finite-cycle gap (proved)

On a fixed cycle of at least three sites, encode infection/membership
by xi_x in {0,1}, and use product Bernoulli(q) conditioned nonempty.
Let P_y be the independent Bernoulli(q) coordinate heat-bath projection
when applied in a term whose occupied center x differs from y. Write

Q=sum_x xi_x(P_{x-1}P_{x+1}-I),
B=sum_x xi_x[(P_{x-1}-I)+(P_{x+1}-I)],
F=FA-1f generator with rates facilitated by at least one occupied neighbor.

Then D_F <= D_B <= 2 D_Q (and D_Q <= D_B). Hence if gap(F)>=g,
then gap(Q)>=g/2 on this nonempty cycle.

Proof. The B chain is BABP: the rate of a coordinate heat-bath update
at y is xi_{y-1}+xi_{y+1}. This is at least the FA-1f update rate
1{xi_{y-1}+xi_{y+1}>0}, so the pointwise sum-of-coordinate-variance
Dirichlet forms give D_F<=D_B. Both use exactly the same conditioned
stationary law, so their variance denominators agree.

For each occupied center x, conditioning xi_x=1 removes the global
nonempty conditioning entirely: the other coordinates again have the
independent Bernoulli law. This justifies working with actual commuting
coordinate-average projections at the two distinct neighbors. Decompose
the function in these two coordinates into its constant component and
three orthogonal components: dependence only on left, only on right,
and the genuine left-right interaction. Let their squared norms after
averaging over the remaining coordinates be a,b,c>=0. The x contribution
to D_Q is [q/(1-p^n)](a+b+c), whereas its contribution to D_B is
[q/(1-p^n)](a+b+2c), where n is the cycle size and p=1-q.
The factor is the conditional probability of xi_x=1 under the
nonempty product law. In unconditioned product measure it would be q.
Thus the former lies between half the latter and the latter. Sum over x.
This avoids asserting that coordinate projections preserve the nonempty
space when no occupied center is fixed; that assertion would be false.
Applying the variational characterization of the spectral gap completes
the proof. QED.

For the infinite dual and the primal, m(B)=(q/(1-q))^|B|. Nonexplosion
and fixed-time finite-cycle approximation follow from their historical-
hull bounds already established in ATTEMPT.md. Consequently (H1)-(H2)
hold with gamma=g for the primal and gamma=g/2 for the dual. The required
uniform positive gap g(q) is verified above; Fresh Lemma 4 improves the
dual's admissible constant to the same g(q).

## Fresh Lemma 3: heat-kernel decay forces linear cardinality (proved under FG)

For either process starting from a finite nonempty A, let N_t be its
infection/membership count. Assume (H1)-(H2) with gamma>0. There exist
alpha=alpha(q,gamma)>0 and c0>0 such that, for all sufficiently large t,

P_A(N_t <= alpha t)
 <= exp(-c0 t) + m(A)^(-1/2) exp(-3 gamma t/4).           (C1)

Here the time threshold may depend on the initial span, but alpha and c0
do not. Consequently almost surely N_t is bounded below by a positive
multiple of t at ALL sufficiently large real times, not merely integers.

Proof of (C1). Let [a,b] contain the initial set, and H0=b-a+1. For
both processes, the number of historical-hull extensions is dominated
by a rate-2 Poisson process, with each extension increasing its length
by at most two. For FA-1f the actual extension rate is at most 2q and
increments are only one, so this common looser bound is also valid.
In the dual a boundary occupied site rings at rate one and can add only
the adjacent outside site, except a singleton can add both sides. The
historical hull is monotone and a ring at an interior site cannot add
an infection outside it. Predictable thinning with additional fictitious
rings supplies the claimed Poisson domination. This also justifies the
bound when a historical endpoint is no longer currently occupied.

For I_t=[a-ceil(8t), b+ceil(8t)], failure to contain the current infection
set implies historical length growth greater than 8t. Therefore
P_A(B_t not subset I_t) <= P(Pois(2t)>=4t).
Chernoff's inequality with exponential parameter log(2) gives
P(Pois(2t)>=4t)<=exp(-(4 log(2)-2)t). Take c0=4 log(2)-2>0.
This Markov bound remains valid for noninteger 4t. For t>=H0+2,
L=|I_t|=H0+2 ceil(8t)<=17t.

Set r=q/(1-q)>0, and choose

theta=min(1/2, gamma/(68r)),
alpha=min(1, gamma/(4 log(1/theta))).

Then 0<theta<1, alpha>0, 17r theta<=gamma/4, and
alpha log(1/theta)<=gamma/4. For the finite state set
E_t={B: empty != B subset I_t, |B|<=floor(alpha t)}, a direct binomial
generating-function bound gives

m(E_t) = sum_{k=1}^{floor(alpha t)} binomial(L,k) r^k
       <= theta^(-alpha t) (1+r theta)^L
       <= exp([alpha log(1/theta)+17 log(1+r theta)]t)
       <= exp(gamma t/2).

To verify the first inequality, for every included integer k<=alpha t,
theta^k>=theta^{alpha t}; multiply the term by theta^k and sum, then
bound by the FULL binomial sum, including k=0. If floor(alpha t)>L,
the sum is understood to stop at L and the same argument remains valid.
The last inequality uses log(1+u)<=u for u>=0. Apply (H2) to E_t:
P_A(B_t in E_t)<=m(A)^(-1/2)exp(-3 gamma t/4).
Adding the cone-failure probability proves (C1). QED.

Proof of the all-real-times consequence. Let c=min(c0,3 gamma/4)>0
and C_A=1+m(A)^(-1/2), so P_A(N_s<=alpha s)<=C_A exp(-cs)
at every sufficiently large deterministic s. Both processes have total
state-changing rate at most 2N_s, and any downward jump reduces N by
at most two (at most one for FA-1f). Fix integer n and put
k_n=floor(alpha n/2). If some s in [n,n+1] has N_s<=k_n, either this
already holds at n or a downward jump in (n,n+1] takes N across that
threshold. Immediately before such a jump, N<=k_n+2. Its counting
intensity is therefore bounded by
2(k_n+2) 1{N_{s-}<=k_n+2}.
For n>=4/alpha, k_n+2<=alpha n<=alpha s throughout the unit interval.
At deterministic s there is almost surely no jump exactly at s, so the
bound on N_{s-} has the same probability as that on N_s. Integration
of the compensator and the preceding pointwise bound gives

P_A(inf_{s in [n,n+1]}N_s<=k_n)
 <= C_A exp(-cn)+2(k_n+2)C_A exp(-cn).

The right side is summable in n. First Borel-Cantelli proves that only
finitely many such intervals have a downcrossing or low initial count.
Eventually N_s>k_n, hence N_s>alpha n/2>=alpha s/4 for s in [n,n+1]
and n>=1. Thus liminf_{t->infinity} N_t/t>=alpha/4 almost surely.
An upper linear bound follows from the same monotone historical-hull
Poisson bound and its Chernoff tail at integer times, then monotonicity
of that hull on each intervening interval. QED.

This proves a cardinality statement, which is stronger than the source's
diameter growth statement as a conclusion, but we make no claim of
literature novelty. The external input FG must be kept visible.

## Exact obstruction to reaching the target by this estimate alone

The local occupation test does NOT have finite m-mass. For every fixed x,
m({B:x in B})=infinity and m({B:x not in B})=infinity. For example,
each singleton {y}, y!=x, contributes r>0 to the latter sum, while
each pair {x,y} contributes r^2>0 to the former. The centered occupation
function 1{x in B}-q is not in l2(m), since its nonzero squared value
is bounded below on these two infinite families. Hence (H1) and
spectral convergence cannot be applied to that function.

Inside I_t the occupation event has mass
r(1+r)^(|I_t|-1), exponentially large in cone size. Applying (H2)
loses a factor exp(O(t) log(1+r)), which the gap gamma need not beat.
Even a hypothetical favorable sign would bound the occupation probability
toward zero, not establish its limit q, so such a usage must be audited.

Linear cardinality and finite propagation also do not logically exclude
local escape: the deterministic sets {floor(t)+1,...,floor(2t)} have
linear size and lie in a linear cone, yet eventually avoid every fixed
site. These sets are NOT claimed to be FA-1f trajectories or a
counterexample. They falsify only the proposed implication from the two
growth estimates to fixed-site occupation convergence.

The precise remaining gap is still P_A(x in B_t)->q for the dual,
followed by the separate extension beyond the single-infection primal
subclass. The new estimate rules out bounded or sublinear total
cardinality as a potential mechanism, without ruling out local escape.

## Fresh Lemma 4: exact equality of the two finite-cycle spectra (proved)

The numerical gaps agree far more closely than the factor-two comparison
requires. This has an exact explanation. On a cycle with n>=3 sites,
include the empty state temporarily and index all configurations by their
infection sets eta. Define D(A,eta)=(-p/q)^|A intersect eta|.
The full 2^n by 2^n matrix D is the tensor product of n copies of

T = [[1,1],[1,-p/q]],

after consistent indexing. Its determinant on one coordinate is -1/q,
which is nonzero. The tensor product is invertible: taking the tensor
product of the inverse matrices gives its inverse, as can be checked
on product basis vectors. The finite generator identity established in
ATTEMPT.md, Proposition 6, reads

D F_full^T = Q_full D.

For completeness, in infection-set notation the duality kernel is
symmetric in A and eta. The primal generator acts on the eta index;
at an infected-set test index x in A it contributes
(etaSpin_{x-1} etaSpin_{x+1}-1)Phi_A. The two spin-multiplication identities
in that proposition turn these factors into independent Bernoulli(q)
membership refreshes at the two neighbors of occupied dual x. This is
precisely the Q term, including no-op refreshes. All other x contribute
zero. This proves the full matrix identity for every entry.

Both full generators are block diagonal diag(0,F) and diag(0,Q), where
F,Q now refer to their nonempty-class generators. For the primal the
empty set cannot birth and a last infection cannot heal; for the dual
the empty set has no occupied ringing center and an occupied ringing
center survives its own refresh. Order the empty state first, so

D = [[1,1^T],[1,D']],
K = D'-1 1^T.

The Schur complement K is invertible. Explicitly multiplying D on the
left by [[1,0],[-1,I]] and on the right by [[1,-1^T],[0,I]] yields
diag(1,K); both triangular multipliers are invertible. Since D is
invertible, so is K. The lower-right block of the intertwining identity
gives D'F^T=QD'. Also F1=Q1=0, so subtracting 1 1^T gives

K F^T = Q K,
Q = K F^T K^(-1).

Thus F and Q have identical eigenvalues with multiplicities on the
nonempty class, and in particular identical spectral gaps. The transpose
does not change the characteristic polynomial. This argument is exact,
not based on approximate equality of the computed eigenvalues. QED.

This improves the permissible common gamma in the count bound to g(q).
The factor-two Dirichlet proof remains an independent cross-check.
Neither the finite similarity nor its inverse is asserted to act boundedly
on an infinite-volume space of local occupation functions.

## Fresh Lemma 5: an exact infinite-volume Walsh norm identity (proved)

There is also a direct check on (H1) for the dual that requires no passage
of finite-sector spectra to the limit. Write r=q/p and retain Phi_B from
ATTEMPT.md. Independence under pi gives

pi(Phi_B Phi_C)=0 if B!=C,
pi(Phi_B^2)=r^(-|B|)=1/m(B).

Indeed each phi has mean zero and second moment p/q, and a site in
the symmetric difference makes the cross expectation vanish. These
functions form a complete orthogonal basis for mean-zero L2(pi), since
their finite tensor products span every local function and local functions
are dense in L2 of the countable product probability space. Consequently

U h = sum_{B nonempty} m(B)h(B)Phi_B

defines a unitary map from l2(m) onto mean-zero L2(pi): the squared norm
of a finite sum is sum_B m(B)|h(B)|^2, and density extends the map.

Let Q_t(A,B) be the finite-set dual transition kernel. At finite t,
sum_B Q_t(A,B)||Phi_B||_2 is finite: with
K=max(1,r^(-1/2)), it is bounded by E_A K^{H_t}, which is finite by the
historical-hull Poisson exponential-moment bound. Thus the expectation
sum_B Q_t(A,B)Phi_B converges absolutely as a Bochner sum in L2(pi).
The duality (D) already proved in ATTEMPT.md identifies it with
P_t^FA Phi_A, pi-almost surely. Therefore, for
h_{A,t}(B)=Q_t(A,B)/m(B), orthogonality gives the exact identity

sum_B Q_t(A,B)^2/m(B) = ||P_t^FA Phi_A||_2^2.             (W)

One can justify the identity first for finite partial sums, then use their
L2 limit. No formal manipulation of a divergent occupation-series is used.

The infinite equilibrium FA-1f gap is positive for every q. To verify a
sufficient bound from the SAME book theorem used above, put infected
boundary conditions on finite intervals. That chain is irreducible on
all configurations: grow infections inward from the boundary to reach
the full infection state, and reverse the growth path of any target.
Theorem 4.8 supplies T_rel<=1/g(q) with the same g(q) as above, now
under the unconditioned product law. For any local function f, choose
an interval containing its support and immediate neighbors. Its variance
and Dirichlet energy agree with their infinite-product versions, because
all boundary-affected updates are outside the support of f. Hence
g(q) Var_pi(f)<=D_FA(f) for all local f. Closure of the Dirichlet form
extends this Poincare inequality and the spectral theorem gives
||P_t^FA Phi_A||_2^2<=exp(-2g(q)t)/m(A).
Combining with (W) proves (H1) for the dual directly. QED.

This exact Hilbert-space representation explains why stationary spectral
methods CAN bound global growth of the finite-seed dual, despite those
starts being singular relative to pi. It does not prove the target
occupation limit: B -> 1{x in B}-q is outside l2(m), so it is not an
admissible test vector for this unitary/spectral bound. On the primal
side, evaluating P_t Phi_A at the single-infection configuration is an
unbounded functional on L2(pi); L2 decay does not imply that evaluation
tends to zero. This is the same concrete obstruction in two languages.

Explicitly, let C_n be the event that the primal configuration agrees
with a single infection at x on [x-n,x+n]. Then pi(C_n)=q p^(2n)->0.
The local mean-zero functions f_n=1_{C_n}-pi(C_n) have
||f_n||_2^2=pi(C_n)(1-pi(C_n))->0 and ||f_n||_infinity<=1, but
f_n(eta^(x))=1-pi(C_n)->1. Thus even uniform boundedness in addition
to L2 convergence cannot justify evaluation at the singular initial
configuration. This is an obstruction example for an implication,
not a sequence claimed to arise from one fixed FA observable.

## Fresh main conclusion (proved partial result)

For every q in (0,1), there are constants beta(q)>0 and V<infinity
such that for FA-1f and for the simultaneous-neighbor-refresh dual,
from EVERY finite nonempty deterministic infection set A,

beta(q)t <= |A(t)| <= Vt

almost surely for all sufficiently large real t (the random starting
time may depend on A). One can use beta=alpha/4 with alpha from Fresh
Lemma 3 and gamma=g(q) above. For an upper bound, V=17 is enough
eventually after applying the historical-hull Poisson bound at integers
and absorbing the fixed initial span. The exponential lower-tail bound
(C1) also holds with this gamma for both processes.

Proof: FG is proved from book Theorem 4.8; Fresh Lemma 4 transfers the
same gap to the dual; Fresh Lemma 1 gives (H1)-(H2); Fresh Lemma 3
gives (C1) and the all-real-times lower and upper bounds. Each component
of this proof is written out above. This is not a proof of Conjecture 1.

## A further check on the old finite-volume obstruction

The verified gap also gives an all-q finite-volume worst-start mixing
upper bound, so lack of such a bound must NOT be stated as the reason
the original conjecture remains open. For an n-site nonempty finite chain
with stationary law mu_n and gap at least g(q), reversibility gives the
density evolution P_t(1_A/mu_n(A)). Its mean-zero initial squared L2 norm
is 1/mu_n(A)-1. Therefore

||P_t(A,.)-mu_n||_TV
 <= (1/2) exp(-g(q)t) sqrt(1/mu_n(A)-1)
 <= (1/2) exp(-g(q)t + (n/2)log(1/min(q,p))).

The second inequality uses mu_n(A)=q^|A| p^(n-|A|)/(1-p^n)
>=min(q,p)^n. Choosing
t>=[(n/2)log(1/min(q,p))+log(1/(2epsilon))]/g(q)
proves an O_q(n) worst-start mixing bound for fixed epsilon in (0,1/2).
This is another consequence of a known theorem, not a new resolution.

Its direct use for the infinite process still requires a coupled finite
window to remain accurate over that mixing time. Enlarging the window
raises the initial-density cost at the same time it postpones boundary
influence. The gap bound alone does not show that the required constants
permit both demands. The sigma-finite argument above does legitimately
take a fixed-time volume limit, but pays for growing occupation events
through their exponential m-mass. This pinpoints why the finite-volume
bound does not close the local-convergence gap.

## Final disposition of the additional attempt

VERDICT: PARTIAL. The two new approaches are recorded above; the weighted
heat-kernel approach was pursued through a complete linear-cardinality
theorem for every q in (0,1), from every finite nonempty seed, for both
FA-1f and the simultaneous-neighbor-refresh dual. Exact finite-cycle
isospectrality and the infinite Walsh norm identity are also proved.
These are partial results; no novelty relative to the wider literature
is asserted. The full D0026 statement is neither proved nor refuted.

The remaining gap is fixed-site convergence of the dual occupation
probabilities from finite nonempty seeds, followed by the extension to
arbitrary deterministic nonempty primal configurations. The proved
global cardinality growth does not exclude local escape. The Hilbert
space estimates cannot be applied to local occupation indicators, whose
weighted squared norms are infinite, or to singular primal point
evaluation. See FRESH_REFEREE.md and CHECKS.md for the audit and precise
scope of the computational and formal checks.
