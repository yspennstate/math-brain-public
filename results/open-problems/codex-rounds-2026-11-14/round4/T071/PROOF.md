# Descendant-family moments for disjoint merger bursts

The estimates below apply to binary branching Brownian motion with selection
of the N rightmost particles, with branching rate one. They give an exact
population observable for the four-lineage obstruction in the preceding
report. A direct estimate of that observable is proved for short physical
windows. The estimate does not establish the required log-cubed-time limit.

## 1. Observation regime and notation

Let N>=4. Start N particles at the origin at physical time zero. Take an
ordered uniform sample of four distinct particles at the deterministic time

    tau_N = (log N)^4,

and use the backward clock

    a_N = (log N)^3.

Thus backward time t refers to physical time tau_N-a_N t. This specifies
an observation regime, without asserting that this clock gives unit pair
merger rate. All finite-N identities also hold for arbitrary deterministic
starting positions and any positive a_N and admissible observation time.

Write Pi_N(t) for the ancestral partition of the sample. Each jump merges
two current blocks. The branching times are distinct almost surely; removal
of a particle and crossing of spatial trajectories do not identify ancestors.
Set

    S_N = inf{t: #Pi_N(t)<=3},
    U_N = inf{t: #Pi_N(t)<=2},
    V_N = inf{t: #Pi_N(t)=1},
    H_N = U_N-S_N,          G_N = V_N-U_N.

Let D_N indicate that the two-block partition has sizes 2+2. If necessary,
complete the genealogy after backward time log N by exchangeable binary
mergers at distinct later times. This makes the times finite and does not
change any fixed window for large N. The calculations below only use
recorded history, never this completion.

For positive T,h,epsilon define

    B_N(T,h,epsilon)
       = {S_N<=T, H_N<=h, G_N>=epsilon, D_N=1}.

The target exclusion is

    lim_(h down to 0) limsup_(N to infinity)
       P(B_N(T,h,epsilon)) = 0                              (1)

for each fixed T,epsilon>0. It is necessary for convergence to a
Bolthausen–Sznitman coalescent with any fixed positive rate multiplier.

## 2. A population observable at four deterministic times

Fix s>=0 and delta,e>0 with s+delta+e<=log N. The four physical times are

    t_0 = tau_N-a_N(s+delta+e),
    t_1 = tau_N-a_N(s+delta),
    t_2 = tau_N-a_N s,
    t_3 = tau_N.

They are ordered t_0<t_1<t_2<=t_3. All ancestors in the definitions below
are actual particle identities, not spatial positions.

For every particle v at t_2 let w_v be its number of descendants at t_3.
For every particle i at t_1 put

    d_i = sum_(v descended from i at t_2) w_v,

    c_i = (d_i)_2
             - sum_(v descended from i at t_2) (w_v)_2,

where (x)_k=x(x-1)...(x-k+1). Since the w_v sum to d_i,

    c_i = sum_(v != v', both descended from i at t_2) w_v w_v'.       (2)

This is a nonnegative integer: it counts ordered pairs of terminal
particles that have different ancestors at t_2 and the same ancestor i at
t_1. The use of terminal descendant counts w_v is essential.

Let p(i) be the ancestor of i at t_0. For each particle z at t_0 put

    zeta_z = sum_(i: p(i)=z) c_i.

Define the nonnegative fourth-degree family statistic

    Q_N(s,delta,e)
       = [sum_(z != z') zeta_z zeta_z']/(N)_4
       = [(sum_i c_i)^2 - sum_z zeta_z^2]/(N)_4.             (3)

The sums over distinct indices in (2) and (3) are ordered sums. All these
quantities are defined from the full population forest before choosing the
sample.

**Proposition 1.** Let E_N(s,delta,e) be the event that Pi_N(s) consists of
four singletons, Pi_N(s+delta) has sizes 2+2, and Pi_N(s+delta+e) still has
two blocks. Conditional on the full population forest up to t_3,

    P(E_N(s,delta,e) | forest) = 3 Q_N(s,delta,e).            (4)

In particular,

    P(E_N(s,delta,e)) = 3 E Q_N(s,delta,e).                  (5)

**Proof.** First prescribe the pairing {1,2}|{3,4}. If labels 1 and 2
have ancestor i at t_1 but different ancestors at t_2, there are exactly
c_i ordered choices for their terminal particles. Labels 3 and 4 similarly
have c_j choices for a second ancestor j at t_1.

The two pairs must still be distinct at t_0. This is exactly the condition
p(i)!=p(j). It implies i!=j and also implies that every particle selected
in the first pair differs from every particle selected in the second.
The within-pair distinctness is already enforced by (2). Thus the number
of ordered samples for this prescribed pairing is

    sum_(i,j: p(i)!=p(j)) c_i c_j
       = sum_(z!=z') zeta_z zeta_z'.

There are (N)_4 equally likely ordered samples. This proves that the
conditional probability for the prescribed pairing is Q_N. The three
possible pairings are disjoint and exhaustive for E_N. Summing proves (4).
Taking expectations proves (5). No independence between selected descendant
families has been used. □

In particular 0<=Q_N<=1/3 for every realized population forest.

## 3. Sliding windows give an equivalent family-moment criterion

For 0<h<epsilon/4, and log N>T+2epsilon, define

    A_N(T,h,epsilon)
       = 3 E Q_N(0,2h,epsilon/2)
           + (3/h) integral_0^T E Q_N(s,2h,epsilon/2) ds.

These quantities require only the recorded history, since
T+2h+epsilon/2<T+epsilon. The stronger history condition also makes all
burst events in (6) independent of the arbitrary completion.

**Proposition 2.** For all such parameters,

    P(B_N(T,h,epsilon))
       <= A_N(T,h,epsilon)
       <= 3 P(B_N(T+2h,2h,epsilon/2)).                     (6)

Consequently (1), for every T,epsilon>0, is equivalent to

    lim_(h down to 0) limsup_(N to infinity)
       A_N(T,h,epsilon) = 0                                (7)

for every T,epsilon>0.

**Proof.** Fix a sample path in B_N(T,h,epsilon) and suppress N in its
merger times. First suppose S<h. Then U=S+H<2h. Also

    V=U+G>=U+epsilon>=epsilon>2h+epsilon/2.

The path therefore lies in E_N(0,2h,epsilon/2).

Now suppose S>=h. For every

    s in I = [max(0,U-2h), S)

the partition at s has four blocks, and s+2h>=U. Moreover,

    s+2h+epsilon/2
       < S+2h+epsilon/2
       <= U+2h+epsilon/2
       < U+epsilon
       <= V.

Thus E_N(s,2h,epsilon/2) holds throughout I. The interval I lies in [0,T]
and its length is at least h. Indeed, if U-2h>=0 its length is
2h-H>=h; otherwise its length is S>=h. These facts give the pathwise bound

    1_B <= 1_(E_N(0,2h,epsilon/2))
              + (1/h) integral_0^T 1_(E_N(s,2h,epsilon/2)) ds.

Tonelli's theorem and (5) give the first inequality in (6).

For the reverse inequality, if E_N(s,2h,epsilon/2) occurs, then

    s<S<U<=s+2h,
    V>s+2h+epsilon/2.

In particular H<=2h, G>epsilon/2 and D_N=1. For s in [0,T] this implies
B_N(T+2h,2h,epsilon/2). The allowable s lie in [U-2h,S), an interval of
length at most 2h. Hence, pathwise,

    integral_0^T 1_(E_N(s,2h,epsilon/2)) ds
       <= 2h 1_(B_N(T+2h,2h,epsilon/2)).

The endpoint event E_N(0,2h,epsilon/2) also implies this B event. Applying
(5) once more proves the second inequality in (6): the endpoint contributes
at most one copy of its probability, and the integral contributes at most
two copies.

Condition (7) implies (1) by the first inequality. Conversely, fix T and
epsilon and take 2h<1. By monotonicity in the first argument,

    A_N(T,h,epsilon)
       <= 3 P(B_N(T+1,2h,epsilon/2)).

Condition (1) at T+1 and epsilon/2 makes the iterated upper limit zero.
This proves the equivalence. □

One sufficient estimate, stated entirely in population variables, is that
for every T,e>0 there are finite C_(T,e) and delta_0>0 such that

    limsup_N sup_(0<=s<=T) E Q_N(s,delta,e)
       <= C_(T,e) delta^2,       0<delta<delta_0.             (8)

Indeed, use delta=2h, e=epsilon/2 in A_N. Its iterated upper limit at fixed
h is at most

    12 C_(T,epsilon/2) (h^2+T h),

which tends to zero. Estimate (8) is sufficient, not asserted necessary.
The equivalent condition (7) requires an averaged estimate and can hold
without (8).

For calibration, in the normalized four-label Bolthausen–Sznitman
coalescent the probability of E(s,delta,e) is

    (1/2) exp(-3s-delta-e) (1-exp(-delta))^2.                (8a)

Thus convergence to this normalized coalescent would force E Q_N at fixed
s,delta,e to converge to (8a) divided by three. Its leading small-delta term
is delta^2 exp(-3s-e)/6. Formula (8a) follows from the defining specified
k-block rates integral_0^1 x^(k-2)(1-x)^(b-k) dx. Two independent derivations
are in AUDIT.md. This calibrates the sufficient estimate; it is not an
established limit for the N-BBM observable.

## 4. A non-asymptotic N-BBM bound at the sampling endpoint

The following estimate uses physical time. Let ell>=0 and observe a uniform
four-particle sample at a deterministic time tau>=ell, starting with any
N-particle configuration. Write nu_i for the number of terminal descendants
of particle i at tau-ell.

**Proposition 3.** For N>=4,

    P(the sample has a 2+2 ancestral partition at tau-ell)
       <= min(1,
          12 exp(2ell)(exp(ell)-1)^2 / ((N-2)(N-3))).        (9)

The bound is uniform over the positions and ancestry before tau-ell.

**Proof.** Conditional on the population at tau-ell, grow an independent
unselected binary BBM tree from each of its N particles. Obtain N-BBM by
pruning a particle and its future descendants whenever selection removes
it. This construction embeds every selected family in its unselected tree.
If Y_i is the size of that tree after time ell, then nu_i<=Y_i pathwise.
The variables Y_i are independent Yule population sizes, each started from
one individual, regardless of the starting positions.

The conditional sampling formula is

    P(2+2 | forest)
       = [3 sum_(i!=j) (nu_i)_2 (nu_j)_2]/(N)_4.            (10)

For clarity, for each specified pairing the two ordered terminal pairs
must belong to two different initial families. There are
sum_(i!=j)(nu_i)_2(nu_j)_2 choices, and three pairings. This gives (10).

For a Yule process Y(t), whose transition y to y+1 has rate y, let
m_1(t)=E Y(t) and m_2(t)=E (Y(t))_2. The generator gives

    m_1'=m_1,                 m_1(0)=1,
    m_2'=2m_2+2m_1,          m_2(0)=0.

The first equation gives m_1(t)=exp(t). Multiplying the second equation by
exp(-2t), integrating from zero, and multiplying back yields

    m_2(t)=2 exp(2t)(1-exp(-t))
           =2 exp(t)(exp(t)-1).                            (11)

Domination and independence of the unselected Y_i imply, for i!=j,

    E[(nu_i)_2(nu_j)_2 | configuration at tau-ell]
       <= [2 exp(ell)(exp(ell)-1)]^2.

There are N(N-1) ordered pairs of different initial particles. Substituting
in (10) and cancelling N(N-1) gives the second argument of the minimum in
(9). The trivial probability bound gives its first argument. □

At s=0 the younger time t_2 in Section 2 is the sampling time itself, so
every w_v equals one and c_i=(nu_i)_2, with ell=a_N delta. Requiring the
two families to have distinct ancestors at the additional older time can
only decrease the numerator. Thus (9) also gives

    3 E Q_N(0,delta,e)
       <= min(1,
          12 exp(2a_N delta)(exp(a_N delta)-1)^2
             / ((N-2)(N-3))).                              (12)

This estimate does not require any assumed coalescent limit.

For 0<eta<1/2 and 0<=ell_N<=(1/2-eta)log N, (9) gives the uniform bound

    P(2+2 at physical backward time ell_N)
       <= 12 N^(2-4eta)/((N-2)(N-3))
       = (12+o(1)) N^(-4eta).                              (13)

Indeed exp(2ell)(exp(ell)-1)^2<=exp(4ell). In the chosen clock these
physical windows have length at most (1/2-eta)/(log N)^2.

## 5. What remains on the log-cubed scale

For fixed positive rescaled delta, ell=a_N delta grows as delta(log N)^3.
The right side before the minimum in (12) grows like exp(4ell)/N^2.
It therefore supplies no vanishing bound on this scale. Proposition 3 does
not prove (7) or (8).

For s>0, the variables w_v in (2) are future descendant counts over a
physical interval of length a_N s. They need not be equal or independent of
the short-interval family structure. Replacing them by one changes the
event being counted. The short-window Yule bound therefore cannot simply
be reused uniformly in s.

The next N-BBM estimate can be stated precisely as (7), with Q_N given by
(2)-(3), for the explicit observation regime of Section 1 or another
justified regime. It controls the off-diagonal products of family collision
increments whose ancestors remain separate at the older time. Even proving
this exclusion would leave the holding-time and marked-transform limits
from the preceding report to be established. No physical rate constant or
full genealogy convergence is obtained here.
