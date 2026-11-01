# Second attempt at E0007, 2026-10-12

## Starting gap and two untried approaches

I reread ATTEMPT.md. The outstanding central case is two supercritical
types on Z^2 with a common irreducible dispersal kernel, unequal death
rates and conflicting birth/death advantages. The weighted log-density
identity contains the unbounded-in-sign correction q_2-q_1. A pointwise
ordering of these conditional vacancy probabilities is false.

**Approach A: a fast-birth reduction to a death-birth voter model.**
Set beta_i=K a_i and let K grow while deaths remain fixed. A death creates
a short-lived vacancy. If all neighbors are occupied, its immediate
replacement has type i with probability proportional to a_i times the
number of type-i neighbors. This suggests a fully occupied spin system
with rates

    2 -> 1: delta_2 a_1 f_1 / (a_1 f_1+a_2 f_2),
    1 -> 2: delta_1 a_2 f_2 / (a_1 f_1+a_2 f_2).

This would connect the problem to death-birth evolutionary games and
voter-model perturbations. It could test whether the ratio is the entire
selection criterion. Major missing steps are infinite-volume fast-birth
convergence, analysis of this spin system, and transfer of asymptotic
selection back to finite K. A formal limiting heuristic is not a proof
of exclusion or of a counterexample.

**Approach B: extend the pair Lyapunov function by three-site forks.**
The prior bound beta_2/delta_2<4/3 threw away the positive pair-creation
term from a vacancy with two occupied neighbors. Track both an occupied
center with two occupied neighbors and a vacant center with two occupied
neighbors. Deaths convert the first fork into the second; births create
the first fork from occupied pairs. A nonnegative linear combination of
these densities may have strictly negative drift beyond 4/3.
This route addresses a stronger extinction special case, not the full
two-supercritical-species gap. I select B because every local generator
step and coefficient can be checked exactly; the resulting certificate
can be compared back to the two-type process without closing correlations.

## Derivation for Approach B

Dominate the type-2 occupied set by an ordinary contact process using the
same type-2 death clocks and birth arrows and ignoring type-1 blocking.
Normalize the single-type death rate to 1 and let beta be the total birth
rate. On Z^d put n=2d, I_x=the occupation indicator, and N=sum_{y~0}I_y.
For a translation-invariant law define

    r=E[I_0],
    q=E[I_0 N]/n,
    H=E[I_0 N(N-1)],
    U=E[(1-I_0)N(N-1)].

All are cylinder expectations. The proposed generator relations are

    r'=(beta-1)r-beta q,
    q'=(2 beta/n)r-(2+2 beta/n)q+(2 beta/n^2)U,
    H'>=2 beta(n-1)q-(3+2 beta/n)H,
    U'>=H-(beta+2)U.

The last two inequalities will be verified against the complete local
generator before use. Set G=r-aq-hH-uU. Choosing

    u=2a beta/[n^2(beta+2)],
    h=u/(3+2 beta/n),
    a=beta/[2+2 beta/n-4 beta^2(n-1)/(n^2(beta+2)(3+2 beta/n))]

formally cancels the q,H,U coefficients and gives

    G'<=-kappa r,       kappa=1-beta+2a beta/n.

For n=4 the sign condition simplifies to

    48-4 beta-23 beta^2>0,

which includes beta=34/25=1.36, strictly above 4/3.

## Full proof of the stronger extinction special case

**Theorem.** Let p be uniform on the four nearest neighbors of Z^2.
In the two-type contact process, for arbitrary positive type-1 birth and
death rates, arbitrary initial law, and delta_2>0, type 2 becomes locally
extinct whenever

    beta_2/delta_2 < b_* = (2 sqrt(277)-2)/23 = 1.360288... .

This is a special case because the inequality forces type 2 into a
subcritical region even in the absence of type 1. No novelty relative
to existing one-type critical-value bounds is asserted. The purpose is
to obtain a stronger, fully audited result than the prior attempt.

### 1. Domination and time normalization

Construct a single-type process zeta using precisely the type-2 death
clocks and type-2 birth arrows of the competition process eta. Start
zeta from all sites occupied. A death at x kills both processes' type-2
particle at x when there is one. A birth arrow usable by type 2 in eta
has an occupied source in zeta; if its destination in zeta is empty it
is filled, and if occupied it already satisfies the inclusion. Type-1
events cannot remove or create a type-2 particle. Induction on the
graphical events therefore preserves

    {x:eta_t(x)=2} subset {x:zeta_t(x)=1}.

For the infinite lattice, the finite-range graphical construction makes
the ancestry of a fixed finite observation up to fixed time a.s. finite,
by domination by a bounded-rate branching process. This justifies the
same eventwise induction. The law of zeta is translation invariant,
irrespective of eta's initial law. Change time to s=delta_2 t and put
b=beta_2/delta_2. The normalized single-type process has death rate 1
and per-edge birth rate b/4. It suffices to prove its occupation
probability r(s) tends to zero from the all-occupied initial state.

### 2. Exact first and pair equations

Write I_x=1{zeta(x)=1}, N=sum_{y~0}I_y, and

    r=E[I_0], q=E[I_0 N]/4,
    H=E[I_0 N(N-1)], U=E[(1-I_0)N(N-1)].

These bounded cylinder expectations are absolutely continuous and
Dynkin's formula permits the following derivatives a.e. No independence
of sites is assumed. Translation invariance gives E[N]=4r, so
E[(1-I_0)N]=4(r-q). The origin dies at rate 1 and is filled at rate
(b/4)N when vacant, hence

    r'=(b-1)r-bq.

The pair expectation q has death term -2q. A birth at the origin changes
I_0 N by N, and has rate (b/4)N, so its contribution to q' is
(b/16)E[(1-I_0)N^2]. Births at the other endpoints of the oriented
pairs contribute the same quantity: translate the endpoint to the origin
and reverse the direction in the symmetric neighbor sum. Consequently

    q'=-2q+(b/8)E[(1-I_0)N^2]
      =(b/2)r-(2+b/2)q+(b/8)U.

### 3. Fork inequalities, retaining all needed dependencies

The variable I_0 N(N-1) is the sum of ordered triples I_0 I_y I_z,
with distinct neighbors y,z. Each triple has three different occupied
sites; deaths therefore contribute exactly -3H to H'. A birth at a
vacant center increases this function and is omitted only from a lower
bound. If the center is occupied and a neighbor y is vacant, filling y
increases N(N-1) by 2N. Its actual birth rate is at least b/4 because
the occupied center is one of y's neighbors. There are 4-N such vacant
neighbors. Their contribution is at least

    (b/2)E[I_0 N(4-N)]
      =(b/2)(3 E[I_0 N]-H)=6bq-(b/2)H.

It follows that

    H' >= 6bq-(3+b/2)H.

For (1-I_0)N(N-1), an occupied-center death creates a vacant fork,
contributing H. Deaths of the two occupied endpoints give -2U.
A birth at the vacant center removes N(N-1); its rate is (b/4)N<=b,
so its contribution is at least -bU. Births at neighbors can only
increase the function while the center is vacant. Therefore

    U' >= H-(b+2)U.

Both inequalities retain the true birth rates wherever the direction
matters. They neither replace neighboring occupation by its density
nor assume a randomly independent environment.

### 4. Explicit Lyapunov certificate

For b>=0 define

    P=b^3+9b^2+44b+48,
    a=2b(b+2)(b+6)/P,
    h=b^2/(2P),
    u=b^2(b+6)/(4P),
    kappa=(48-4b-23b^2)/P,
    G=r-aq-hH-uU.

The denominator is positive and a,h,u are nonnegative. Combining the
two exact equations and the two lower bounds, with the negative
coefficients -h and -u, gives

    G' <= [(b-1)-ab/2]r
          +[-b+a(2+b/2)-6bh]q
          +[h(3+b/2)-u]H
          +[-ab/8+u(b+2)]U.

Substituting the displayed coefficients cancels the q,H,U terms
exactly. The r coefficient equals -kappa. Thus G'<=-kappa r.
These are rational identities; their denominators and sign assumptions
are specified, rather than inferred from a numerical fit.

### 5. Nonnegativity is essential and is proved separately

For N in {0,1,2,3,4}, N(N-1)<=3N. Thus

    0<=H<=12q,       0<=U<=12(r-q),       0<=q<=r.

It follows that

    G >= (1-12u)r-(a+12h-12u)q
      >= m r,
    m=min(1-12u,1-a-12h).

Also G<=r. The two numerators defining m are

    P(1-12u)=-2b^3-9b^2+44b+48,
    P(1-a-12h)=-b^3-13b^2+20b+48.

For 0<=b<=7/5 the first numerator is at least
48-2(7/5)^3-9(7/5)^2=3109/125>0; the second is at least
48-(7/5)^3-13(7/5)^2=2472/125>0. Here the nonnegative
linear terms were discarded, and powers were bounded using b<=7/5.
Hence m>0 throughout this interval. In particular G is nonnegative,
a necessary point that would fail for some poorly chosen corrections.

### 6. Parameter range and extinction

The quadratic Q(b)=48-4b-23b^2 is strictly decreasing on b>=0.
Its unique positive root is b_*=(2 sqrt(277)-2)/23. We have
Q(4/3)=16/9>0, Q(34/25)=12/625>0, and Q(7/5)=-67/25<0.
Thus 4/3<34/25<b_*<7/5. For 0<=b<b_* we have kappa>0
and m>0. Since r>=G,

    G'<=-kappa r<=-kappa G.

The absolutely continuous integrating-factor inequality yields

    r(s)<=G(s)/m<=G(0)/m exp(-kappa s).

The all-occupied initial state has r(0)=q(0)=1, H(0)=12, U(0)=0,
so G(0)=1-a-12h, which is positive and finite. Reversing the time
normalization and using the occupied-set domination proves

    P(eta_t(x)=2) <= [G(0)/m] exp(-delta_2 kappa t) -> 0

for every site x and every initial law. This completes the proof.

The equality case b=b_* has kappa=0 and is not proved by this
certificate. The central case of two supercritical competing types is
still untouched: the theorem proves a stronger extinction special case,
not the whole ratio conjecture.

## Checks in progress

The symbolic cancellation, the local fork inequalities, and all finite
generator computations will be checked independently. Only after those
checks pass will the new claim be entered as proved_special_case.

## Refinement: keep the common center-birth term

The preceding proof is valid, but bounding the two center-birth
contributions separately loses information. Define

    T=(b/4)E[(1-I_0)N^2(N-1)].

It is the very same center-birth contribution with opposite signs in
the two fork equations. The proof of Step 3 gives the sharper bounds

    H'>=6bq-(3+b/2)H+T,
    U'>=H-2U-T,
    0<=T<=bU.

The last inequality follows pointwise from 0<=N<=4. The exact first
and pair equations of Step 2 remain unchanged. For G=r-aq-hH-uU,
these relations imply

    G' <= [(b-1)-ab/2]r
         +[-b+a(2+b/2)-6bh]q
         +[h(3+b/2)-u]H
         +[-ab/8+2u]U+(u-h)T.

When u>=h, replace T by its upper bound bU, giving the U coefficient
-ab/8+(b+2)u-bh. Now use the following new coefficients; those of
the earlier certificate must not be mixed with them:

    P_new=b^3+7b^2+36b+48,
    A_new=2b(b^2+6b+12),
    a=A_new/P_new,
    h=b^2/(2P_new),
    u=b^2(b+6)/(4P_new),
    kappa_new=(48-12b-17b^2)/P_new.

They are nonnegative for b>=0 and satisfy u=h(3+b/2)>=h.
Substitution gives the four exact algebraic identities

    -b+a(2+b/2)-6bh=0,
    h(3+b/2)-u=0,
    -ab/8+(b+2)u-bh=0,
    (b-1)-ab/2=-kappa_new.

Consequently G'<=-kappa_new r. The same pointwise bounds
H<=12q, U<=12(r-q), 0<=q<=r show

    m_new r<=G<=r,
    m_new=min(1-12u,1-a-12h).

Here positivity also requires a fresh check because the coefficients
changed. Its two numerators are

    P_new(1-12u)=-2b^3-11b^2+36b+48,
    P_new(1-a-12h)=-b^3-11b^2+12b+48.

For 0<=b<=7/5 these are bounded below respectively by
2619/125 and 2962/125: discard the nonnegative linear terms and bound
the powers using b<=7/5. Both are strictly positive. In addition,

    P_new(a+12h-12u)=b(24-b^2)>=0

in this interval. Thus m_new=1-a-12h. From the all-occupied initial
state G(0)=m_new, exactly. This proves the clean bound

    r(s)<=exp(-kappa_new s)

whenever kappa_new>0.

The quadratic 48-12b-17b^2 is strictly decreasing for b>=0, and
its positive root is

    b_ref=(2 sqrt(213)-6)/17=1.3640611199207557... .

It is below 7/5 since the quadratic at 7/5 equals -53/25<0.
It is above the preceding root: at every b>0 the two quadratics differ
by (48-12b-17b^2)-(48-4b-23b^2)=2b(3b-4), which is positive
for b>4/3, including the preceding root. Both roots exceed 4/3.
For 0<=b<b_ref all required signs hold and kappa_new>0.

Combining this with Step 1's graphical domination establishes the
**strongest proved special case of this second attempt**:

    If beta_2/delta_2 < (2 sqrt(213)-6)/17,
    then for every initial law and every x,
    P(eta_t(x)=2) <= exp(-delta_2 kappa_new t) -> 0,

with b=beta_2/delta_2 in the displayed formula for kappa_new.
The beta_2=0 case is included (kappa_new=1). Type-1 parameters are
arbitrary. At the new endpoint kappa_new=0, so no endpoint claim is made.
This is still a one-type-subcritical special case, not a solution of
the ratio-only competition question.

## Endpoint and a small extension by a stationary finite-energy argument

This argument supplies local extinction, without claiming an exponential
rate, at the refined endpoint and in an explicit interval beyond it.
Let

    C0=1/(3^11 * 5^5 * 13^2),
    epsilon=C0/1000,
    B=b_ref+epsilon.

I prove local extinction from the all-occupied state for every
0<=b<=B. Consequently the two-type exclusion special case extends to
beta_2/delta_2<=B for arbitrary initial law and arbitrary type-1 rates.

### 1. A controlled event creates a strictly dissipative pattern

For an arbitrary initial configuration with the origin occupied, use
the following independent graphical requirements over [0,1]. Let S be
the origin and its four nearest neighbors. Require:

- No origin death in [0,1/2], and at least one origin death in [1/2,3/4].
- At every neighbor, at least one death in [0,1/4] and no deaths in [1/4,1].
- Of the twenty directed incoming edges with target in S, no birth
  arrows at any time, except allow origin-to-right and origin-to-left
  arrows in [1/4,1/2]; require at least one arrow on each of these two
  edges in that window.

This event is independent of the initial configuration. Deaths first
clear all four neighbors. The origin remains occupied until 1/2 and
seeds the right and left neighbors; those two cannot die afterward.
The up and down neighbors stay empty. The origin dies after 1/2 and
cannot be recolonized. Thus at time 1 it is vacant with exactly two
occupied neighbors. No outside state can interfere, since every
incoming arrow to S not explicitly allowed has been forbidden.

The event probability is exactly

    c(b)=exp(-7/2-39b/8) (1-exp(-1/4))^5 (1-exp(-b/16))^2.

For the death factors there are five required death-window events,
no origin deaths for length 1/2, and no neighbor deaths for total length
3. For the birth factors there are eighteen completely forbidden edges
and two edges forbidden for length 3/4 each. Their total forbidden edge
time is 39/2, with per-edge rate b/4. Each allowed window has length
1/4, explaining b/16. These counts are essential to the bound.

If mu is a translation-invariant stationary law with occupation
r=mu(I_0=1), the Markov property and stationarity therefore imply

    mu(I_0=0,N=2)>=c(b)r.

The exact definition of T gives

    bU-T=(b/4)E[(1-I_0)N(N-1)(4-N)]
         >= b mu(I_0=0,N=2)>=b c(b)r.

### 2. Stationary drift inequality

For the refined coefficients, before bounding T the derivation gives

    G'<=-kappa_new r+(u-h)(T-bU).

For a stationary law the left side is zero (G is an expectation of
a bounded cylinder function). Since u-h>=0, the controlled event yields

    0<=-[kappa_new+(u-h)b c(b)]r.

Whenever the bracket is strictly positive, r=0. A translation-invariant
law with zero occupation marginal concentrates on the empty configuration,
by the countable union bound over Z^2. In particular at b=b_ref we have
kappa_new=0 but u-h>0 and c(b)>0, so the bracket is strictly positive.

### 3. All constants for the small extension

For 4/3<=b<=7/5, the elementary inequality exp(x)>=1+x gives
1-exp(-1/4)>=1/5 and 1-exp(-b/16)>=1/13. Also
7/2+39b/8<=413/40<11 and exp(1)<3. Thus c(b)>C0.
For completeness, exp(1)<3 follows from its power series: n!>=2^(n-1)
for n>=2 with strict inequality at n>=3, so the sum of terms n>=2
is strictly below 1. No decimal approximation to an exponential is used.

In this interval P_new<=P_new(7/5)=14358/125, while
b^2(b+4)>=256/27. Therefore

    u-h=b^2(b+4)/(4P_new)>=4000/193833>1/50,
    (u-h)b c(b)>(2/75)C0.

The quadratic at 137/100 equals -3473/10000<0, so
b_ref<137/100. Since epsilon<1/1000, B<1371/1000<7/5.
For b=b_ref+s, 0<=s<=epsilon, we have

    -kappa_new = [(12+34b_ref)s+17s^2]/P_new
               <= [(298/5)s+17s^2]/48 <=2s.

The last inequality uses s<=1/1000 and P_new>=48. It follows that

    kappa_new+(u-h)b c(b)
       > -2 epsilon+(2/75)C0
        = C0(2/75-1/500)>0.

Every translation-invariant stationary law at b in [b_ref,B] is thus
empty. At b<b_ref extinction has already been proved exponentially.

### 4. Why ruling out stationary occupation gives extinction here

Let nu_t be the law of the ordinary contact process started all occupied.
Binary contact-process attractiveness gives nu_{t+s}<=nu_t in stochastic
order: nu_s<=delta_all_occupied, and apply the monotone transition
semigroup S_t. The limits of increasing cylinder probabilities determine
a weak limit nu_infinity on the compact binary product space (arbitrary
finite-dimensional probabilities follow by inclusion-exclusion).
The finite-range contact-process semigroup is Feller: the finite
backward dependency construction approximates a fixed finite observation
by a finite cylinder, with approximation error tending to zero. Hence
nu_infinity S_s=nu_infinity by taking limits in nu_{t+s}=nu_t S_s.
The limit is translation invariant because every nu_t is.

In the newly added interval the stationary argument forces nu_infinity
to be the all-empty law. Thus nu_t(I_x=1)->0. Applying the graphical
domination from Step 1 proves type-2 local extinction for every initial
law when beta_2/delta_2<=B.

This is a complete stationary argument, not an assertion that absence
of coexistence by itself implies convergence. Monotonicity of the
single-type upper process is what supplies the limit. No quantitative
decay rate is proved on [b_ref,B]. The full two-supercritical-species
competition question remains open in this attempt.

## A boundary-case check on Approach A: the limits do not commute

The fast-birth route needs more than finite-time convergence. This is
already a genuine obstruction in a finite single-type boundary case
of the contact process, not a counterexample to E0007 itself.

Take the two-vertex graph, initially fully occupied, with death rate 1
and per-individual birth rate K to its sole neighbor. Let X_t be the
number of occupied sites and p_j(t)=P(X_t=j). Its nonzero jump rates
are 2->1 at rate 2, 1->2 at rate K, and 1->0 at rate 1. Consequently

    p_1'=2p_2-(K+1)p_1,       p_0'=p_1,
    p_1(0)=p_0(0)=0.

The integrating-factor formula and p_2<=1 imply

    p_1(t)=integral_0^t 2p_2(s)exp(-(K+1)(t-s))ds <=2/(K+1),
    p_0(t)<=2t/(K+1).

For either vertex x, P(x vacant at t)<=p_1(t)+p_0(t), so for
every fixed finite t,

    lim_(K->infinity) P_K(x occupied at t)=1.

For each fixed finite K, on every unit interval there is probability
e^(-2K)(1-e^(-1))^2>0 of no birth arrows and at least one death mark
at each vertex. This empties the graph regardless of its initial state
on that interval. The events over disjoint unit intervals are independent.
The probability that no such event occurs in the first m intervals is
(1-e^(-2K)(1-e^(-1))^2)^m, which tends to zero. Empty is absorbing.
Therefore lim_(t->infinity) P_K(x occupied at t)=0 for each finite K.

The two iterated limits are thus

    lim_K lim_t P_K(x occupied at t)=0,
    lim_t lim_K P_K(x occupied at t)=1.

This proves that an argument passing first to an instantaneous
death-birth process and then reading off its long-time behavior needs
an additional uniform-in-time or block-construction theorem. Merely
establishing a finite-time fast-birth limit would not bridge the central
gap. No infinite-lattice counterexample is inferred from this finite one.

## Final check record and verdict

Exact finite checks passed: 8192 radius-two binary patterns, 40960
site changes, 512 periodic binary configurations, and 4464 nonzero-rate
transitions. Both the initial fork certificate and the refined shared-event
certificate are retained separately in fork_checks.json and
fork_refined_checks.json. The job for the refinement completed in about
175 seconds; memory is limited to small fixed arrays and rational numbers.
forcing_checks.json verifies the twenty incoming edges, forbidden
edge/site times and every rational endpoint margin. Decimal values there
are for display only. The full hostile-referee audit is FORK_REFEREE.md.

The exact forcing constant is C0=1/93555759375, so the extension
epsilon is 1/93555759375000. Its positive stationary-drift margin
is 37/140333639062500. Neither number is obtained by sampling.

VERDICT: PARTIAL. The stronger extinction special case and the finite
limit-interchange counterexample are fully proved above. No proof or
counterexample is obtained for the central two-supercritical species
problem with only birth/death ratio ordering.

Lean verification is still pending; no successful formal check is inferred from source-file presence.
