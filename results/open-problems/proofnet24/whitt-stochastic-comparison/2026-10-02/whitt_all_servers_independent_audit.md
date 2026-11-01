# Independent analytic audit: light-traffic counterexample

Date: 2026-10-02. This note independently derives the cubic coefficient and
checks why the finite-level calculation is the coefficient of the actual
infinite FCFS queue. It is a working proof checkpoint, not a priority claim.

## Service laws and convex order

Let E be exponential with mean one. The baseline service law is

    S = E/5 with probability 3/7, and 8E/5 with probability 4/7.

The comparison service law is

    T = E/1000 with probability 200/533,
        and 8E/5 with probability 333/533.

Both have mean one. To couple them, preserve the long branch of S. On its
short branch, replace E/5 by E/1000 with probability 1400/1599 and by
8E/5 with probability 199/1599. These probabilities make the conditional
mean multiplier exactly 1/5. Thus E[T|class,E]=S, and consequently
E[T|S]=S. Jensen proves S <=cx T. The resulting short probability is
(3/7)(1400/1599)=200/533. Every service time is strictly positive almost
surely, and all its moments are finite.

For either law, consider the stationary M/H2/2 FCFS queue with Poisson
arrival rate lambda. Workload coupling with the M/M/2 queue whose service
times are 8E/5 proves stability for every 0<lambda<5/4. PASTA identifies
P(W>0) with the stationary probability of population at least two.

## Analyticity of the infinite stationary model at lambda=0

For a generic H2 service law, let p be the probability of the short
exponential class, q=1-p, and let a,b be its two rates. For every
population n>=2, use phases i=0,1,2 indicating how many short-class jobs
are in service. Put

    M=diag(2b,a+b,2a),
    D=[[2bq,2bp,0],
       [aq,ap+bq,bp],
       [0,2aq,2ap]].

At populations n>=3, D is the downward transition-rate matrix: a completed
job is replaced by a fresh class sampled with probabilities q,p. Upward
transitions have matrix lambda I, and diagonal holding rates are
-(M+lambda I). The matrix-geometric rate matrix solves

    R = Phi_lambda(R)
      = (lambda I+R^2 D)(M+lambda I)^(-1).

This equation is finite dimensional and analytic near (lambda,R)=(0,0).
The derivative with respect to R of R-Phi_lambda(R) there is the identity.
The analytic implicit function theorem gives an analytic solution
R(lambda)=O(lambda).

For small positive lambda this is the minimal nonnegative QBD root, not
merely an arbitrary algebraic branch. Indeed Phi_lambda preserves
nonnegative matrices. On a matrix norm ball of radius K lambda, for a
fixed sufficiently large K, it maps that ball into itself and has
Lipschitz constant O(lambda)<1. Iteration from zero therefore converges
to its unique fixed point in that ball. Such iteration is the minimal
nonnegative root construction. Also spectral radius(R)<1.

Fix empty-state mass provisionally at one and solve the finite boundary
balance equations at populations one and two. At lambda=0 their
nonempty-state generator is pure death, hence its negative is invertible.
Its entries depend analytically on lambda and R(lambda), so its inverse
and the unnormalized boundary masses are analytic. The one-busy vector
is O(lambda). The two-busy balance equation expresses its vector as the
one-busy vector times a lambda arrival matrix and an inverse that remains
bounded; it is O(lambda^2).

The level-n row mass, n>=2, is the two-busy boundary row times R^(n-2).
The normalization factor uses (I-R)^(-1), so it too is analytic and equals
one at zero. This constructs the actual normalized stationary law and
proves

    pi_n=O(lambda^n), n>=2,
    sum_{n>=4} pi_n 1 = O(lambda^4),
    P(W>0) is analytic in lambda near zero.

The summed-tail statement follows directly from the exact expression
pi_2 R^2 (I-R)^(-1)1, so it does not require exchanging an uncontrolled
infinite series with a Taylor expansion.

## Why the cap-three calculation gives the correct cubic term

Let Qcap(lambda) be the finite queue that blocks arrivals at population
three. Its lambda=0 chain has the empty state as its sole recurrent state;
all other states are transient under pure death. Its augmented stationary
linear system (replace one balance equation by normalization) is therefore
invertible at zero and remains analytically invertible nearby.

Restrict the true infinite stationary row pi to populations at most three,
giving pi_A. The balance residual pi_A Qcap is the sum of the removed
outgoing arrival term from population three and the incoming downward
term from population four. Both are O(lambda^4), since pi_3=O(lambda^3)
and pi_4=O(lambda^4). Also pi_A1=1+O(lambda^4). Applying the bounded
augmented inverse shows pi_A-pi_cap=O(lambda^4). Adding the infinite
tail, also O(lambda^4), proves that the capped and actual delay
probabilities agree through degree three.

## Independent closed-form cubic coefficient

Assume p/a+q/b=1. Put

    u=(q/b,p/a),
    tau=(q^2/(2b^2),pq/(ab),p^2/(2a^2)).

The coefficient of lambda in the one-busy stationary vector is u; the
empty-state coefficient is -1. The coefficient of lambda^2 in the
two-busy vector is tau, found by dividing its arrival-source row by M.
In particular tau1=(p/a+q/b)^2/2=1/2.

The downward source from tau to the one-busy level is exactly u, while
the lambda arrival loss from the one-busy level is also u. Thus the
coefficient of lambda^2 in the one-busy vector is -u.

At order lambda^3 the population-three row is tau M^(-1). Population-two
balance then gives its cubic row as

    -tau-tau M^(-1)+tau M^(-1)D M^(-1).

Summing population-two and population-three cancels the middle term.
Consequently the actual infinite queue satisfies

    P(W>0)=lambda^2/2+c3 lambda^3+O(lambda^4),
    c3=-1/2+tau M^(-1)D M^(-1)1.

This formula independently reproduces the finite cap-three recursion.

For the baseline (p,a,b)=(3/7,5,5/8), exact rational evaluation gives

    c3(S)=-643/2700.

For the comparison law (p,a,b)=(200/533,1000,5/8), it gives

    c3(T)=-64056049/256320100.

Their difference is

    c3(S)-c3(T)=4068754/346032135>0.

Hence

    P(W_S>0)-P(W_T>0)
      =(4068754/346032135)lambda^3+O(lambda^4)>0

for every sufficiently small positive lambda. This disproves the proposed
usual stochastic ordering of the stationary waiting times, despite the
strictly positive service laws being in convex order. The asymptotic
argument establishes an open interval of counterexamples but does not
specify an explicit endpoint of that interval.

## Audit conclusion

The analytic route is valid. Its essential details are the identification
of the implicit root with the nonnegative QBD root, use of the geometric
tail to prove analyticity of the infinite normalization, and the bounded
finite augmented inverse in the cap-three comparison. The two rational
cubic coefficients were independently evaluated from the displayed
three-by-three formula and match the original recursive calculation.

## Further audit: the entire finite hyperexponential class

The strengthened result in `whitt_light_traffic_proof.md` also passes.
Here the mixing means a_i are positive, probabilities p_i are positive,
and the finite index set has size k. Write m=sum p_i a_i and u_i=p_i a_i.

The unordered busy phase space has k(k+1)/2 entries. All arguments above
use only finitely many phases, a positive diagonal total-completion-rate
matrix, and a nonnegative downward matrix. Consequently the analytic
implicit-function, small-arrival contraction, boundary inversion,
geometric-tail, and cap-three residual arguments carry over verbatim.
The contraction constants may depend on the fixed class parameters, as
is appropriate for the asserted small-lambda existence theorem.

The leading one-busy coefficients are u_i. The leading two-busy
coefficients are tau_ii=u_i^2/2 and tau_ij=u_i u_j for i<j, so their
total is m^2/2. This follows directly from class-specific arrival sources
and exponential completion rates, without an independence assumption
on stationary busy jobs.

For each class, exact stationary work conservation gives expected busy
class-i servers lambda p_i a_i. Therefore the one-busy quadratic
coefficient is -m u_i, since the leading two-busy phases contribute
u_i m to the count of busy class-i servers. Alternatively, the downward
source into class i from tau is u_i; this cancels the one-busy arrival
loss, leaving the empty-state linear coefficient -m times p_i.

The same level-two/level-three balance calculation then gives

    c3=-m^3/2+tau M^(-1)D M^(-1)1.

For a size-biased old mean pair A,B, the probability that A survives the
first completion is A/(A+B). A fresh original-law mean C starts service;
the expected time until the next completion is AC/(A+C). Accounting for
the unordered old pair and then size-biasing C proves exactly

    tau M^(-1)D M^(-1)1
      =m^3 E[A^2/((A+B)(A+C))],

with A,B,C independent under weights p_i a_i/m. The proposed general
cubic formula is thus correct.

Exchangeability and the common-denominator identity give

    K/m^3=(1/3)E[1-2ABC/((A+B)(A+C)(B+C))].

Since the denominator is at least 8ABC, K>=m^3/4. Equality in that
pointwise AM-GM inequality occurs precisely when A=B=C. With all
positive class weights, a nonconstant mean mixture has positive
probability of unequal triple values. Thus K>m^3/4 in exactly the
nondegenerate case. Duplicate identical means can be merged and do not
affect this condition.

The endpoint construction at 0 and B=max a_i is a martingale coupling.
Poisson thinning identifies its workload process with M/M/2. Zero jobs
can themselves wait, but they add no workload; PASTA applies to all
original arrivals, yielding the stated delay probability. This correctly
compares the ordinary FCFS waiting time, including that of zero jobs.

For the strictly positive endpoint epsilon and B, the probabilities are
(B-m)/(B-epsilon) and (m-epsilon)/(B-epsilon). Substitution into the
two-class excess formula gives

    Delta_epsilon
      =epsilon B m(B-m)(m-epsilon)/(4(B+epsilon)^2)
      <=epsilon m^2(B-m)/(4B).

The proposed choice

    epsilon=min{min_i a_i/2, B Delta/[m^2(B-m)]}

is strictly positive, is smaller than every original mean, and ensures
Delta_epsilon<=Delta/4. Hence the cubic difference is at least
3Delta/4>0. The O(lambda^4) constants may increase when epsilon is
small, but epsilon is fixed before lambda approaches zero. This causes
no gap: an interval of sufficiently small positive lambda still exists.
There is no explicit certified endpoint for that interval in this
analytic argument.

As an independent algebraic check, a dense exact Fraction solve of the
capacity-three generator was performed for two-, three-, and four-class
laws, including a three-label degenerate exponential case and non-unit
means. Every cubic coefficient agrees exactly with the size-biased
triple formula. The proposed epsilon bound also passes exact comparisons.
The files are `whitt_general_light_traffic_independent.py` and
`whitt_general_light_traffic_independent_checks.json`.

Final audit status: the strengthened general finite-hyperexponential
theorem is mathematically valid, including strict positive-service
counterexamples. This audit establishes internal correctness; it does
not certify novelty or independent expert acceptance.

## Further audit: every fixed number of servers c>=2

The strengthened all-server theorem in
`whitt_all_servers_light_traffic_proof.md` also passes independent audit.

The infinite-queue analyticity proof carries over for each fixed c. The
busy phase space now consists of class multisets of size c, and remains
finite. The same rate-matrix equation has derivative zero on its right
side at (lambda,R)=(0,0). Small-positive-lambda contraction identifies
the analytic solution with the minimal nonnegative stationary root.
The boundary pure-death inverse is analytic; coefficient recursion gives
population-j masses O(lambda^j) through j=c. The mass above population
c+1 is exactly a normalized expression involving pi_c R^2(I-R)^(-1),
so it is O(lambda^(c+2)). The restricted infinite stationary row has
both balance and normalization residuals of that order in the capped
system. Its augmented finite inverse remains bounded. Thus capacity
c+1 computes the actual infinite queue's coefficients through degree
c+1, with no unproved tail interchange.

Here is an independently derived finite perturbation argument for the
next coefficient. Put waiting and loss models on the same state set up
to population c+1. In the loss model, the upper states are transient and
unreachable from the closed lower class; assign their arrival-free
completion transitions identically to the waiting model. The common Q0
is pure death. The arrival matrices differ only at full population c:
the waiting matrix sends a unit rate to the same full phase plus one
waiting job and subtracts one from the old state's diagonal, while the
loss matrix rejects the arrival. Denote that matrix difference by E.

Stationary Taylor coefficients are obtained from

    pi_j Q0=-pi_(j-1)Q1, pi_j1=0 for j>=1.

The coefficients have no mass above population j. Hence the two models'
coefficients agree through degree c. Their degree-(c+1) difference delta
satisfies

    delta Q0=-tau E, delta1=0,

where tau is the leading population-c coefficient. The exact loss-chain
product form gives total tau mass m^c/c! and an iid size-biased class law
conditional on that population. The normalization is included in this
coefficient recursion; no informal rare-arrival argument is needed.

Let f indicate at least c busy servers and let h be the total expected
future f reward under pure death, with h(empty)=0. Then Q0h=-f. From a
full phase of old rates X1,...,Xc, its value is 1/V, V=sum old rates.
With one waiting job, it is 1/V plus the expected full busy time after
the first completion and replacement. Multiplying the displayed
coefficient equation by h proves exactly

    delta f=tau E h
      =(m^c/c!) E_old[
         sum_i Xi/V * E_original_new 1/(V-Xi+Xnew)].

The replacement's original-law probabilities are m Xnew times its
size-biased probabilities. With n=c+1 iid size-biased reciprocal means,
total rate H=sum Xi, and ri=Xi/(H-Xi), this becomes

    Kc=m^(c+1)/(c! n) E sum_(i!=j)ri rj.

The ordered sum and factor 1/n are correct: the pre-symmetrization term
is E sum_(i<n)ri rn, and every possible distinguished new index has the
same expectation. The loss-chain next coefficient is
-m^(c+1)/c!, yielding precisely the claimed waiting next coefficient
Kc-m^(c+1)/c!.

The deterministic odds inequality was checked directly. For two
coordinates with sum t and product z, writing R for the other odds, the
z-dependent part of the unordered pair sum is

    [z+R(t-2z)]/(1-t+z).

Its derivative is ((1-t)-R(2-t))/(1-t+z)^2<0, since t<1 and
R>=1-t. Averaging a maximal/minimal pair increases z and lowers the
pair sum strictly when unequal. Repetition converges to uniformity:
the variance decreases by half the squared range, at least its own
value divided by 2n. Thus its limit is zero. This proves the sharp lower
bound n/[2(n-1)], with strictness at every initial nonuniform vector.

For the upper bound, merging two positive coordinates decreases z and
increases the sum while at least one other positive coordinate remains.
Stop with two positive coordinates, where their odds product is one.
No step merges into the singular one-coordinate boundary. This proves
the upper bound one, and hence

    n/(n-1) <= sum_ordered ri rj <= 2.

Nondegenerate iid service means give positive probability of a nonuniform
reciprocal-rate sample, so the strict excess

    Delta_c=Kc-m^(c+1)/(c!c)>0

is correct. The equal-means control agrees with the usual Erlang-C
expansion, whose next coefficient is
-(c-1)m^(c+1)/(c!c).

The positive endpoint replacement retains convex order by its conditional
mean construction. Its size-biased short probability is
r_epsilon=epsilon(B-m)/(m(B-epsilon)). If none of the n iid classes is
short, the symmetric integrand T equals 1/c; otherwise it is at most
2/n. The union bound gives

    Delta_c(Uepsilon)
      <=m^c(c-1)epsilon(B-m)/(c!c(B-epsilon)).

The proposed epsilon

    min{min_i a_i/2,
        Delta_c c!cB/[8m^c(c-1)(B-m)]}

is positive, is strictly below the original means, is at most B/2, and
makes that bound at most Delta_c/4. Its fixed positive value is selected
before the light-traffic limit, so the analytic remainder establishes
the required interval of positive arrival rates. An explicit endpoint
for that rate interval is still not asserted.

Independent dense Gaussian Fraction solves were performed for both
waiting and embedded loss generators with c=2,3,4,6 and two classes,
c=3 and three classes with a non-unit mean, and a degenerate equal-means
control. Every stationary coefficient equation and normalization was
checked exactly. The next-coefficient differences equal Kc, and the
symmetric formula matches the independently computed waiting
coefficients exactly. The candidate's explicit epsilon choice also
passes exact comparisons of its resulting excess against Delta_c/4.
Files: `whitt_all_servers_independent.py` and
`whitt_all_servers_independent_checks.json`.

Final all-server verdict: the full analytic theorem is internally
correct, including its normalization, strictness, infinite-chain
remainder, and strictly positive endpoint construction. Historical
priority and external acceptance remain separate questions.
