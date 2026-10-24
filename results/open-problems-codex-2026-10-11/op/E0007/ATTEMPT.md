# E0007 research attempt, 2026-10-12

## Source and scope

Rick Durrett, *Coexistence in stochastic spatial models*, Annals of Applied
Probability 19(2) (2009), 477–496, DOI 10.1214/08-AAP590,
arXiv:0906.2293. Problem 1 is on PDF page 3. States are 0,1,2 on Z^2;
a type i dies at rate delta_i and attempts births at total rate beta_i,
using displacement law p_i. Only vacant targets accept offspring.

The source's exclusion conclusion means P(xi_t(x)=2) tends to zero.
It does not require survival of type 1. The preceding Theorem 1 specifies
translation-invariant initial law with P(xi_0(x)=1)>0. Problem 1 refers
to that conclusion and changes equal death rates to the ratio inequality.
The literal initial-law condition needs qualification: a nonergodic mixture
can have a type-2-only component. This is recorded as a quantifier issue,
not a resolution of the intended competition problem. The principal
unresolved target here uses an i.i.d. initial law with positive probabilities
of both types, a common symmetric finite-range irreducible kernel, positive
death and birth rates, and beta_1/delta_1 > beta_2/delta_2. These extra
restrictions describe a central intended case, not a quotation of the source.

## 1. A self-contained extinction special case

**Proposition.** For every translation-invariant initial law and any
translation-invariant probability dispersal kernel, if beta_2 < delta_2,
then

    P(xi_t(0)=2) <= P(xi_0(0)=2) exp(-(delta_2-beta_2)t).

No assumption on type 1 or on the ratio inequality is needed.

**Proof.** Write rho(t)=P(xi_t(0)=2). The bounded cylinder function
f(eta)=1{eta(0)=2} has generator

    Lf(eta) = -delta_2 1{eta(0)=2}
       + beta_2 1{eta(0)=0} sum_y p(y) 1{eta(-y)=2}.

The incoming sum is at most one, so Lf is bounded. The graphical
construction, or Dynkin's formula for this cylinder function, yields
rho(t)=rho(0)+integral_0^t E[Lf(xi_s)] ds. Summability of p justifies
exchange of expectation and sum by Tonelli. Translation invariance is
preserved by the dynamics. Hence for almost every t,

    rho'(t) <= -delta_2 rho(t)+beta_2 sum_y p(y) rho(t)
             = -(delta_2-beta_2)rho(t).

Absolute continuity and the integrating factor imply that
exp((delta_2-beta_2)t)rho(t) is nonincreasing. This proves the bound. QED.

This proves exclusion in the part of Problem 1 with beta_2 < delta_2.
It does not cover the whole contact-process subcritical regime; the
branching bound is deliberately stated without a critical-value theorem.

### A stronger pair bound for the common nearest-neighbor kernel

**Proposition.** On Z^d, with n=2d nearest neighbors and total birth rate
beta=beta_2, death rate delta=delta_2>0, type 2 becomes locally extinct
from every translation-invariant initial law whenever

    (n-1) beta < n delta.

In particular the condition on Z^2 is beta_2/delta_2<4/3. Type-1
parameters are arbitrary, and no ratio inequality is needed.

**Proof.** The beta=0 case is pure exponential death. Suppose beta>0.
Put r=P(xi_t(0)=2), N_2=sum_{y~0}1{xi_t(y)=2}, and

    q=(1/n) E[1{xi_t(0)=2} N_2],
    b=(beta/n) E[1{xi_t(0)=0} N_2].

All quantities below are functions of t. These are bounded cylinder
expectations and are absolutely continuous by Dynkin's formula. We have

    r'=b-delta r,       0<=q<=r,       0<=b<=beta(r-q).

For the last inequality replace the vacant-site indicator by
1-1{xi_t(0)=2}, and use E[N_2]=n r by translation invariance.
The oriented pair indicator only changes when one of its endpoints dies
or is filled by a type 2. Its death contribution is -2 delta q. Summing
births at the origin contributes (beta/n^2)E[1{xi_t(0)=0}N_2^2].
Births at the other endpoints give the same contribution after translation
and y -> -y in the symmetric neighbor sum. Thus exactly

    q'=-2 delta q+(2 beta/n^2)E[1{xi_t(0)=0}N_2^2]
       >=-2 delta q+(2/n)b,

because N_2 is a nonnegative integer and N_2^2>=N_2. This includes
type-1 blocking: the vacancy indicator is retained throughout.

Choose a=n beta/[2(n delta+beta)] and k=1-2a/n=n delta/(n delta+beta).
The assumption gives 0<a<1/2 (indeed a<1/2 is equivalent to
(n-1)beta<n delta), and k>0. For F=r-aq, use the lower bound on q'
and then the upper bound on b, with the positive coefficient k:

    F' <= k b-delta r+2a delta q
        <= (k beta-delta)r+(2a delta-k beta)q
         = -gamma r,
    gamma=delta[n delta-(n-1)beta]/(n delta+beta)>0.

Since (1-a)r<=F<=r, this implies F'<=-gamma F and hence

    r(t) <= F(0)/(1-a) exp(-gamma t).

This tends to zero. QED. This elementary lower-bound method is not claimed
as a new critical-value result. It gives a checked special case directly
in the competition model without assuming that the other type is absent.

## 2. Complete mean-field exclusion argument

Let beta_i,delta_i>0 and u_1(0)>0, u_2(0)>=0, u_1(0)+u_2(0)<=1.
The source ODE is

    u_i' = u_i [beta_i(1-u_1-u_2)-delta_i].

The closed simplex is forward invariant: u_i=0 is invariant by uniqueness,
and on u_1+u_2=1 the derivative of their sum equals
-delta_1 u_1-delta_2 u_2<0. The polynomial vector field therefore has
a global solution in the simplex. For positive initial u_i the explicit
scalar integrating-factor formula ensures u_i(t)>0 for finite t.
If u_2(0)=0 exclusion is immediate. Otherwise, putting
c=delta_2/beta_2-delta_1/beta_1>0 gives the exact identity

    d/dt [log(u_2)/beta_2-log(u_1)/beta_1] = -c.

Integrating and raising to the positive power beta_2 yields

    u_2(t) = u_2(0) (u_1(t)/u_1(0))^(beta_2/beta_1)
                         exp(-beta_2 c t)
           <= u_2(0) u_1(0)^(-beta_2/beta_1) exp(-beta_2 c t).

Thus u_2(t) tends exponentially to zero. QED. This is an ODE result,
not a proof for the interacting particle system.

## 3. Precisely where the spatial version fails

For rho_i(t)=P(xi_t(0)=i)>0, define

    q_i(t) = sum_y p(y) P(xi_t(0)=0,xi_t(-y)=i)/rho_i(t).

Translation invariance implies 0<=q_i<=1. The exact first-moment equations
are rho_i'=rho_i(beta_i q_i-delta_i). Consequently

    d/dt [log(rho_2)/beta_2-log(rho_1)/beta_1]
       = q_2-q_1-c.

The vacancy probabilities seen by the two types need not be equal.
Positive initial marginals remain positive at every finite t: the event
that the initial type-i particle at the origin has no type-i death up
to t has probability rho_i(0)exp(-delta_i t), and births never overwrite
an occupied site. Thus the logarithms and integrated equations are
legitimate throughout any finite interval when rho_i(0)>0.
For any interval on which both densities are positive, integration gives

    rho_2(t) = rho_2(0) (rho_1(t)/rho_1(0))^(beta_2/beta_1)
       exp(beta_2 integral_0^t (q_2(s)-q_1(s)-c) ds).

In particular, a bound integral_0^t(q_2-q_1) ds <= (c-epsilon)t+C
for some epsilon>0 would imply exclusion. No such bound is proved here.

**Exact counterexample to the proposed pointwise inequality q_2<=q_1.**
Use the common nearest-neighbor kernel on Z^2, uniform on the four
neighbors. Make a period-6 striped configuration according to the
first coordinate modulo 6:

    1,1,1,0,2,0.

Choose the phase uniformly in {0,...,5}; the resulting law is translation
invariant. (It is even ergodic under the full translation group, since
that group acts transitively on its six phases.) Here rho_1=1/2,
rho_2=1/6. A type-1 site sees on average 2/(3*4)=1/6 vacant nearest
neighbors: only the two exterior columns each have one vacant neighbor.
A type-2 site has two horizontal vacant neighbors and two occupied
vertical neighbors, so q_2=1/2. Therefore q_2-q_1=1/3>0.
This is an exact initial-time calculation and refutes the pointwise
inequality; it is not a counterexample to eventual exclusion. In
particular with beta_1=4,delta_1=1,beta_2=3,delta_2=1, the ratio gap
c=1/12 is smaller than 1/3 and the weighted log-density difference
initially increases although type 1 has the higher ratio. Equal-death
exclusion is nevertheless known: a monotone log-density proof cannot
replace its more delicate argument.

## 4. Finite model check, with its limitation

On the two-vertex graph, start with one individual of each type. Both
targets are occupied, so before the first death no birth can change the
state. The two independent exponential death clocks have rates delta_1
and delta_2. The first death eliminates its type globally; it can never
return because there is no mutation. The probability type 2 disappears
first is therefore delta_2/(delta_1+delta_2), independently of birth rates.
For beta_1=8,delta_1=4,beta_2=1,delta_2=1, type 1 has the larger
ratio (2>1) but is the last surviving type only with probability 1/5.
This is a proved finite-graph result, not a counterexample on Z^2.
Both species eventually die on this finite graph, so the source's local
exclusion conclusion there is vacuous.
For completeness, in every unit interval the graphical construction has
a fixed positive chance of no birth attempts and at least one death mark
of each type at each site. This event forces the empty configuration
regardless of the starting state. Disjoint intervals use independent
Poisson increments, so the probability it never occurs is zero.

## 5. Coordinatewise favorable rates: a full comparison reduction

For common finite-range kernel p, suppose beta_1>beta_2 and
delta_1<=delta_2. Start from an i.i.d. law with positive type-1
probability. These parameters imply the ratio ordering. Under the known
equal-death exclusion theorem, they imply exclusion in the unequal-death
process as follows. This is a reduction to that theorem, not a new proof
of the equal-death theorem itself.

Let eta be the desired process and zeta have the same birth rates and
both death rates equal to delta_2, starting from the identical random
configuration. Order single-site states by 2<0<1. For every directed
edge x->y, use a common type-i birth-attempt clock of rate beta_i p(y-x).
The update changes an empty y to i precisely when x=i. Each of the
two update maps preserves this order. To verify this, a type-1 update
can only raise a target. If it raises a lower target, the upper source
is also 1, and an upper target that is 0 is raised as well; if the upper
target is 1 the order already holds. If the upper target is 2, the lower
target cannot have been 0. For a type-2 update the dual reasoning holds:
it only lowers a target, and if it lowers an upper target the lower
source is also 2; a lower target that is 0 is lowered as well, while
a lower target already 2 is harmless. It cannot lower an upper target
that dominates a lower target 1.

At each site use common type-1 death clocks of rate delta_1 and common
type-2 death clocks of rate delta_2, with each type-specific clock killing
only its type. Their maps 1->0 and 2->0 separately preserve 2<0<1.
Finally add type-1 death clocks of rate delta_2-delta_1 to zeta only.
This extra update lowers zeta and hence preserves zeta<=eta. Thus by
induction over the graphical events zeta_t<=eta_t. The usual finite-range
graphical construction passes this finite-space argument to Z^d: the
backward dependency set of a finite space-time observation is almost
surely finite at fixed time, being dominated by a continuous-time branching
process with bounded rates. There is no explosion in finite time.

The required generators are correct: zeta type 1 dies at total rate
delta_2, eta type 1 at delta_1, and both have the specified remaining
rates. Hence {eta_t(x)=2} is a subset of {zeta_t(x)=2}, so

    P(eta_t(x)=2)<=P(zeta_t(x)=2) -> 0.

The last limit is the equal-death theorem applied after a common time
rescaling by delta_2, for an initial law with type 1 present almost surely.
For the nearest-neighbor kernel it also follows from the complete
convergence Theorem 1.2 of Mountford–Barrios Pantoja–Valesin, together
with the following elementary fact: infinitely many initially occupied
type-1 sites cannot all disappear by any fixed finite time, since their
independent death clocks each leave a positive probability of no death
up to that time. Applying this at every integer time makes the event S_1
have probability one. An i.i.d. positive type-1 marginal gives infinitely
many such sites almost surely. QED (conditional only on the cited
equal-death complete convergence theorem).

This comparison does not work when both beta_1 and delta_1 are larger,
or when both are smaller. The ratio condition permits both of these
cases. Changing time separately for each type cannot be used as a common
time change of the interacting process.

## 6. The literal nonergodic initial-law issue

Take the nearest-neighbor kernel on Z^2 and choose beta_2 above the
one-type critical total birth rate for death rate 1. Its upper invariant
law mu_2 has theta=mu_2(eta(0)=2)>0, and contains no type 1. This
standard one-type fact is stated in the downloaded asymmetric paper,
PDF p. 2. Choose delta_1=2, delta_2=1, beta_1=3 beta_2. Then the
required strict ratio inequality holds, including unequal deaths.
Let the initial law be

    mu=(1/2)delta_(all type 1)+(1/2)mu_2.

It is translation invariant and has mu(eta(0)=1)=1/2. Conditional on
the second mixture component, no type 1 can ever be created; the process
is the stationary one-type process with law mu_2. Conditional on the
first component there is never a type 2. Linearity in the initial law
therefore gives P_mu(eta_t(0)=2)=theta/2 at every t. This refutes the
literal assertion if it is read with only the marginal-positive
translation-invariant assumption copied from the preceding Theorem 1.
It also refutes that preceding theorem read literally, even when deaths
are equal, so it identifies an omitted initial-state qualification,
not a newly discovered failure of the intended unequal-death conjecture.
No claim of solving the intended open problem is based on this issue.

## 7. Hostile-referee checks and precise scope

- Rate convention: Durrett uses total individual birth rate beta. Later
  nearest-neighbor papers often use per-edge rates. On Z^d their rate
  lambda corresponds to beta=2d lambda. The pair threshold 4/3 is a
  TOTAL birth/death ratio on Z^2, not a per-edge rate.
- Pair generator: independently enumerate all 3^9=19,683 states of a
  3-by-3 periodic nearest-neighbor graph. The script finite_checks.py
  checks 106,434 possible type-2 birth/death transitions by directly
  recounting oriented occupied pairs. Every birth changes the pair count
  by 2N_2 and every type-2 death by -2N_2. It checks the birth and
  integer-square inequalities in every state. This finite verification
  supports the local generator derivation; the infinite-volume proof
  above uses cylinder functions and translation invariance explicitly.
- Pair coefficient choice: finite_checks.py verifies both cancellation
  identities, positivity, and a<1/2 using exact rational arithmetic for
  48 parameter cases in dimensions 1–4, including points approaching
  the threshold. The proof does not infer universal algebra from this
  finite sample; the identities are written explicitly above.
- The stripe calculation is checked with exact fractions: rho_1=1/2,
  rho_2=1/6, q_1=1/6, q_2=1/2. It tests a false intermediate inequality,
  not eventual asymptotics.
- RatioIdentity.lean contains the division-free mean-field cancellation,
  its strict sign under the cross-product inequality, and the spatial
  residual identity. After adding the missing real-number import,
  `lake env lean ~/brain_workers/TRIO_1011/op/E0007/RatioIdentity.lean`
  from ~/lean_verify returned exit 0 (lean_check.txt).
  No sorry, native_decide, or unchecked axiom is used. This checks those
  algebraic lemmas only, not the IPS or ODE arguments. The first failed
  compilation is retained as lean_check_initial_failure.txt.
- Initial-state qualification: the i.i.d. case avoids the mixture problem.
  Degenerate common dispersal laws can create further quantifier issues;
  no such loophole is used to claim a resolution.
- Endpoint: gamma=0 at (n-1)beta=n delta, so this argument gives no
  decay there. It must not be reported as proving the non-strict case.
- Birth blocking by type 1: retained in b and in the pair-birth generator.
  Replacing this environment by an independent vacancy field would be
  an unjustified closure assumption; no such replacement is made.

## Remaining gap

No proof or counterexample is obtained for competition of the two
supercritical types on Z^2 under unequal death rates and only the ratio
ordering. The exact correlation term above explains why the simple
mean-field proof does not transfer. Literature verification and independent
algebra/finite checks are recorded separately as they complete.

## 8. Short stochastic experiment (finite evidence only)

simulate.py implements the exact uniformized continuous-time process on a 24-by-24 periodic square. Independent potential updates at every site have rate R=max(beta_1+delta_1,beta_2+delta_2). An occupied source of type i dies with probability delta_i/R, attempts a birth with probability beta_i/R (target uniform over four neighbors, accepted only if vacant), and otherwise makes a null update. Empty sources make null updates. Thus every specified death and per-neighbor birth generator rate is reproduced exactly. The global Poisson rate is 576R. Initial states are independent with probabilities (0.1,0.45,0.45). Six replicates per parameter choice use seeds 7007+100*case_id+rep, at times 0,10,30,60. Full trajectories and summary are in simulation.json. The job took about 16 seconds and used arrays of 576 sites, far below 1 GB.

| (beta_1,delta_1; beta_2,delta_2) | ratios | mean rho_1(60) | mean rho_2(60) |
|---|---|---|---|
| (6.0,2.0; 2.8,1.0) | 3>2.8 | 0.439525 | 0.171875 |
| (2.8,1.0; 5.4,2.0) | 2.8>2.7 | 0.426505 | 0.142650 |
| (8.0,4.0; 1.9,1.0) | 2>1.9 | 0.153067 | 0.174190 |

The third case has mean rho_1(10)=0.070602 versus rho_2(10)=0.265336 despite the favorable ratio. At least one finite replicate loses type 1. Neither a transient density disadvantage nor finite extinction refutes the infinite-volume conjecture. The other cases also leave substantial type-2 density at time 60, so the experiment cannot certify asymptotic exclusion. No finite-size extrapolation, significance assertion or infinite-volume conclusion is made.

## Final assessment

VERDICT: PARTIAL. The source is verified and no exact-match published solution was located in the successful bounded searches. The nearest-neighbor extinction bound, mean-field result, coupling reduction, algebraic identities, and explicit failed intermediate inequality are proved with their scopes above. The central two-supercritical-species case with only ratio ordering and unequal deaths remains unresolved. This is the limit of this attempt; no claim of a complete solution is made.

## Second attempt at user request

2026-10-12: The prior final assessment describes the first attempt.
The second attempt and full new proofs are in SECOND_ATTEMPT.md.
Two new routes were considered: fast-birth death-birth voter reduction,
and a Lyapunov function retaining occupied/vacant three-site forks.
The latter was pursued and improves the nearest-neighbor type-2
extinction special case to

    beta_2/delta_2 <= (2 sqrt(213)-6)/17
                     + 1/(1000*3^11*5^5*13^2).

The algebraic root is approximately 1.3640611199207557. This conclusion
holds regardless of type-1 parameters and from every initial law by
single-type graphical domination. The tiny explicit extension includes
the algebraic endpoint, using a stationary finite-energy argument.
For beta_2/delta_2 strictly below the root the proof gives an explicit
exponential rate; no exponential rate is asserted for the extension.
No claim of novelty relative to published one-type critical-value bounds
is made. This is stronger than the first attempt's 4/3 bound.

Exact checks pass on 8192 radius-two patterns and 512 periodic states.
The central remaining gap is unchanged: no exclusion proof or
counterexample for two supercritical types under only the ratio ordering.
VERDICT: PARTIAL.

The new Lean checks are still pending; the written proof and finite checks are saved.
