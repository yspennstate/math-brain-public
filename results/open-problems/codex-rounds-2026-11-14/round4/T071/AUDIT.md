# Independent checks of the family-moment method

All checks are analytic. No simulation or numerical program was run.

## 1. Ordered and unordered sampling counts

Proposition 1 uses ordered samples and three possible labelled pairings.
Check its coefficient independently by unordered samples. For each middle
ancestor i there are c_i/2 unordered terminal pairs with different younger
ancestors. If p(i)!=p(j), the pairs have disjoint terminal members. The
number of qualifying unordered four-element sets is therefore

    sum_(i<j: p(i)!=p(j)) (c_i/2)(c_j/2).

Each qualifying four-element set has exactly two middle ancestors, so it
is counted once. Divide by choose(N,4)=(N)_4/24. The result is

    [6 sum_(i<j: p(i)!=p(j)) c_i c_j]/(N)_4
       = [3 sum_(i!=j: p(i)!=p(j)) c_i c_j]/(N)_4
       = 3Q_N.

This verifies both the factor three and the falling-factorial denominator
without using ordered pairings.

## 2. Unequal terminal weights and the older filter

Take N=8. Two middle families A and B each have terminal size three.
Each contains two younger ancestors with positive terminal weights 2 and 1.
Two further middle families each have terminal size one. All other particles
at the intermediate population times have zero terminal descendants. Let A
and B have different ancestors at the additional older time.

For A and B,

    c_A=c_B=(3)_2-(2)_2-(1)_2=6-2=4.

The singleton families contribute zero. Thus the ordered off-diagonal
numerator is 4*4+4*4=32, and (8)_4=8*7*6*5=1680. Formula (4) predicts

    3Q=96/1680=2/35.

Independently, an unordered pair inside A must choose one of its two
weight-2 descendants and its one weight-1 descendant: two choices. There
are two choices in B as well, so four qualifying subsets out of
choose(8,4)=70. The probability is 4/70=2/35.

If A and B instead have the same older ancestor, the correct probability
is zero: both pairs have joined by that older time. Grouping by z makes
the numerator (4+4)^2-(4+4)^2=0, as required.

Replacing all positive w_v by one would replace c_A=c_B=4 by two and give
one quarter of the correct numerator. Omitting the subtraction of the
within-younger-family pairs would instead give c_A=c_B=6 and overcount
four-element subsets that already have a merger at the younger time.
Both shortcuts change the observable.

## 3. Sliding-window geometry and endpoint check

On a path with finite S<U<V and D=1, the event E(s,delta,e) is exactly

    s<S,       U<=s+delta,       s+delta+e<V,

up to endpoint choices of Lebesgue measure zero in s. Thus its allowed s
form an interval, intersected with [0,T], contained in [U-delta,S). Its
length is at most max(0,delta-H), hence at most delta. This directly checks
the integral upper bound with delta=2h.

For the lower bound assume H<=h, G>=epsilon and h<epsilon/4. If S>=h,
every s in [max(0,U-2h),S) works. Its length is

    min(S,2h-H)>=h.

The requirement on V holds because 2h+epsilon/2<epsilon<=G. If S<h,
the interval may be shorter than h. The separate s=0 event works instead:
U<2h and V>=epsilon>2h+epsilon/2. This independently checks why an endpoint
term is necessary and why no assumption about S having a limiting density
at zero is needed.

Every working s gives H<=2h, G>epsilon/2 and S<=T+2h. Its total length
is at most 2h. The integral, divided by h, contributes at most two copies
of the enlarged burst probability, and the endpoint contributes at most
one. This checks the factor three in Proposition 2 separately from the
unrelated factor three for sample pairings in Proposition 1.

The strict inequalities avoid absorption at the deeper observation time.
The lower bound uses a strict margin 2h+epsilon/2<epsilon, so it remains
valid even if G equals epsilon exactly. Branching at an observation time
has probability zero for any deterministic observation time; the pathwise
integral argument also tolerates its finitely many endpoint exceptions.

The history assumption log N>T+2epsilon covers the finite-N burst tests as
well as the four-time observables. In the enlarged burst event, for example,
U<=T+4h<T+epsilon and U+epsilon/2<T+3epsilon/2. Hence whether it persists
long enough is decided before the recorded history ends.

## 4. Calibration by the target coalescent, two derivations

Define the normalized coalescent by the beta-integral rates in PROOF.md.
At four blocks the first-event rate is three. Reaching 2+2 requires a first
pair merger (total rate two) followed by its complementary pair merger
(rate 1/2 among the three remaining blocks). If these events occur after
times u and v, with u+v<=delta, their joint first-two-event density is

    exp(-3u-2v) du dv.

Survival with two blocks until delta+e contributes
exp(-(delta+e-u-v)). Integrating gives

    p_(4,22)(delta) exp(-e)
       = exp(-delta-e)
           integral_0^delta exp(-2u)
             [integral_0^(delta-u) exp(-v) dv] du
       = exp(-delta-e)
           [(1-exp(-2delta))/2-exp(-delta)(1-exp(-delta))]
       = (1/2) exp(-delta-e)(1-exp(-delta))^2.

To require four blocks at the younger backward time s, multiply by
exp(-3s). This proves (8a) by first-event integration.

Independently use forward equations from the initial four-singleton state:

    p_4(t)=exp(-3t),
    p_3'(t)+2p_3(t)=2p_4(t),
    p_22'(t)+p_22(t)=(1/2)p_3(t).

Their zero initial values give

    p_3(t)=2(exp(-2t)-exp(-3t)),
    p_22(t)=(1/2)exp(-t)-exp(-2t)+(1/2)exp(-3t)
           =(1/2)exp(-t)(1-exp(-t))^2.

Multiply by exp(-3s) for the initial four-block survival and exp(-e) for
the final two-block survival to obtain exactly (8a).

Since 1-exp(-delta)<=delta, this probability is at most
(1/2)exp(-e)delta^2. Dividing by three gives expected Q at most
exp(-e)delta^2/6. Its small-delta coefficient is exp(-3s-e)/6.
Thus the uniform quadratic estimate has the right order for the target.
Substituting delta=2h in the definition of A gives

    A_B(T,h,epsilon)
       = (1/2)exp(-2h-epsilon/2)(1-exp(-2h))^2
           [1+(1-exp(-3T))/(3h)]
       = (2/3)h exp(-epsilon/2)(1-exp(-3T))+O(h^2).

In particular the factors in the sliding-window estimate do not mistakenly
force a smaller order than the target's own burst probability, whose leading
term from the preceding report is
h exp(-epsilon)(1-exp(-3T))/3.

## 5. Calibration against the preceding counterexample

The round-3 counterexample has the same total first-event rate three and
the same three-block transition rates, but adds direct 4-to-22 transitions
at total rate 1/4. Its 22 forward equation consequently has an additional
incoming term exp(-3t)/4. At small delta, this gives

    p_22^counter(delta)=delta/4+O(delta^2),

while the target probability is delta^2/2+O(delta^3). Equivalently, subtract
the target and integrate the extra flux:

    p_22^counter(delta)-p_22(delta)
       =(exp(-delta)-exp(-3delta))/8
       =delta/4+O(delta^2).

The counterexample's window probability divided by three therefore equals

    q^counter(s,delta,e)
       = exp(-3s-e)delta/12+O(delta^2)

on bounded s intervals. Whenever population genealogies converge to this
four-label law, (5) forces their expected Q at fixed s,delta,e to converge
to this value. No such population realization is asserted. Substituting
this window probability in the expression for A, with delta=2h, leaves
the nonzero limit

    (1-exp(-3T))exp(-epsilon/2)/6.

The endpoint term tends to zero. Hence the equivalent criterion detects
the earlier counterexample's disjoint events. A test that merely required
Q(s,delta,e) to tend to zero, with no division by the window length, would
fail this check.

## 6. Yule second moment and the constant twelve

Proposition 3 obtains E(Y(ell))_2 from its generator. Independently, the Yule
law from one individual is geometric:

    P(Y(ell)=k)=p(1-p)^(k-1),   k>=1,   p=exp(-ell).

This follows, for example, by substituting it into the forward equations
P_k'=(k-1)P_(k-1)-kP_k and checking P_1(0)=1. Its generating function is

    g(z)=pz/[1-(1-p)z].

Twice differentiating and evaluating at one gives

    E(Y(ell))_2=g''(1)=2(1-p)/p^2
       =2 exp(ell)(exp(ell)-1),

agreeing with the generator calculation (11).

For an independent count of the prefactor in (9), use unordered terminal
four-element sets. For each unordered initial-family pair i<j, the number
of ways is choose(nu_i,2)choose(nu_j,2). Under Yule domination its expected
value is at most [exp(ell)(exp(ell)-1)]^2. There are N(N-1)/2 family pairs.
Dividing their sum by choose(N,4) gives

    [N(N-1)/2] * exp(2ell)(exp(ell)-1)^2
         * 24/[N(N-1)(N-2)(N-3)]
       =12 exp(2ell)(exp(ell)-1)^2/[(N-2)(N-3)].

This reproduces the constant twelve independently of the ordered-sample
formula used in the proof. The selected families are not declared
independent: only their dominating unselected trees are independent,
conditional on the earlier configuration.

Finally check the power in (13) by logarithms. The logarithm of
exp(4ell)/N^2 is 4ell-2log N. At ell=(1/2-eta)log N it is
-4eta log N, so the power is N^(-4eta). The denominator correction is
N^2/[(N-2)(N-3)]=1+O(1/N). The sign and magnitude in (13) follow.

## 7. Attempts that fail and scope limits

- Dropping the older-ancestor filter counts binary resolutions that promptly
  become a quadruple. These need not violate the intended limit.
- Treating surviving family sizes as independent is unjustified under
  selection. Independence enters only after pathwise domination by the
  independent unselected trees.
- Using counts of younger ancestors instead of their terminal descendants
  loses the sampling bias. Section 2 gives an exact finite example.
- The sliding-window estimate needs the endpoint term; an arbitrarily small
  first-merger time could otherwise be missed. It also needs the factor
  1/h in the integrated term; Section 5 shows a counterexample without it.
- The Yule estimate is uniform over positions but grows too rapidly to
  reach the conjectured clock. It cannot supply the uniform quadratic
  moment estimate for fixed positive rescaled delta.
- A bound for s=0 does not control s>0: terminal descendant weights then
  vary and depend on future selection. No estimate for those weights on
  the log-cubed scale has been proved here.
- Formula (1) only excludes one four-label obstruction. It does not give
  the transforms that determine the full four-label law, much less all
  finite samples.

No failure was found in Propositions 1-3. The log-cubed family-moment
estimate, not its finite-N reduction or short-window bound, is unresolved.
