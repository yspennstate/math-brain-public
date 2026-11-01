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
