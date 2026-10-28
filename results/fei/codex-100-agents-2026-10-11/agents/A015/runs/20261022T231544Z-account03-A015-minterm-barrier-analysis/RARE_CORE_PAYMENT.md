# Rare leafless cores: a complete same-queue payment

The original queue admits a paid two-root description on a vanishing-mass
leafless prime family. No positive controller bank is assumed.
All costs are base-two ideal lengths and gamma=6/5. The queue is exactly
forests.tex items(i)--(iv), conditioned on a nonempty initial root set.
Failed and infinite runs retain their missing mass.

## A general bounded coordinate-cover certificate

Take N distinct signed conjunction gates of the same positive width W, actual
rarity pi=2^-W, with one fixed positive vector lambda_l=1/N. The original
packing rows hold because their sum is one. Use one full physical order per
gate. Suppose h fixed ORIGINAL gates cover every relevant coordinate.
For each nonempty output set A, assign coordinates to the first of these h
gates containing them; discard empty owned blocks. This specifies c<=h distinct
roots, disjoint nonempty owned subsets and no children. These are legitimate
original queue events even if their roots are not a minimal source-SCC root
set. No partition-family or selected-lift equality is used here.

For a specified nonempty s-subset B of a width-W gate, theta_s(i)>=
(s/W)^gamma and Z_s<=binom(W,s)<=2^W. Consequently the exact probability of
choosing size s, then B, then zero children is at least

    p_visit >= (s/W)^(gamma*s) / [2s(s+1)2^W] >= 2^(-4W).  (1)

To prove the last inequality, size loss log[s(s+1)]<=2s, since s,s+1<=2^s.
Also s log(W/s)<=log(e)(W-s)<(3/2)(W-s). Thus total loss is at most
W+(9/5)(W-s)+2s+1 <=3W+1<=4W. All denominators are positive: 1<=s<=W.
The bound uses actual size, subset normalizer and the single zero-child
count factor1/2; it does not incorrectly charge a zero-child factor per
selected coordinate. Other ranks or extra full orders only increase the
lower theta bound; the fixed one-order reference suffices.

Let z=pi/N and D=(1+z)^N-1. Exact Bernoulli inclusion AND absence factors,
divided by the ORIGINAL nonempty-root probability, give z^c/D for the
specified root set. Binomial expansion and pi<=1/2 give

    0<D<=sum_(j>=1) pi^j=pi/(1-pi)<=2pi.

Combining this with (1), the selected successful-event subprobability Q obeys

    Q(A)>=2^[-1-c log N-(5c-1)W]
         >=2^[-1-h log N-(5h-1)W]                       (2)

for EVERY nonempty A. Distinct A have different output unions, hence disjoint
events. A queue empties after at most h visits in these events. The unchanged
queue may have additional finite or infinite runs; (2) needs neither their
enumeration nor almost-sure termination. This is an upper-cost certificate
from a selected ACTUAL event family, never a lower-cost transfer from a
selected family to all events. Here Q(A) is the selected-event mass; the
original whole-output mass Q_*(A) is at least Q(A). We pay the FULL selected
event length -log Q(A); other compatible runs can only reduce the actual
whole-output code cost. Every present/absent root, name, rarity, size, subset and child
count factor is included. There are no uncharged attachments or permutations.

## Actual Boolean family and original prime table

For integers m>=2, r>=0, and 0<=t<=max(1,floor(m/4)), set

    B=1_{|x|>=m-t}1_{|y|>=m-t},
    F=2 A_r B-1,  p=2^-r,

where x,y are disjoint m-bit blocks and A_r is the conjunction of r fresh
uniform satisfied literals (A_0=1). This is a sign Boolean function on
n=2m+r coordinates. Its exact positive prime supports contain all controls,
any m-t left coordinates and any m-t right coordinates. Every minimal true
input has exactly these positive coordinates; monotonicity removes negative
literals from any prime. Thus N=binom(m,t)^2 and W=2(m-t)+r. The uniform
vector1/N is fixed BEFORE any output set is selected. Every data packing row
is (m-t)/m, every control row is one. For t>=1, every variable belongs to
multiple primes: this is leafless incidence with unbounded worst-case read.

If t>=1, choose the prime omitting the first t coordinates on each side and
the prime omitting the NEXT t on each side. Their omitted sets are disjoint
because 2t<=m, including m=2,3,t=1. Their union is the entire physical
coordinate set. These are two ORIGINAL primes from the SAME full table;
all unused primes remain present with their absent-root factors. For t=0
there is one prime and one root suffices. In (2) use h<=2, log N<=2m and
W<=n. Therefore, uniformly in all parameters and all nonempty A,

    -log Q(A)<=1+4m+9W<=12n.                            (3)

The resulting complete nonempty spectral cross-entropy satisfies

    C_Q=sum_(A!=empty) Fhat(A)^2 log(1/Q(A))<=12n Var(F).  (4)

This upper-bounds the complete actual-queue code cost C_* because Q_*>=Q.
It neither discards inherited
core cost nor restarts a reference after exposure: the FINAL full prime
table, lambda, D, orders and all output sectors are priced directly once.
Intermediate scale refactoring is not used. The certificate includes
nonminimal two-root runs that need not belong to the earlier distributed
selected family, so its cost is not identified with that earlier Psi.

## Pay the ambient dimension from the TRUE rare-core influence

Write S=sum_(j=0)^t binom(m,j), q=S2^-m and b=q^2. Direct pivotal counting gives

    I_g=4m q binom(m-1,t)2^-m,
    I(F)=p[I_g+2r b],
    Var(F)=4pb(1-pb).                                    (5)

When t<=m/4, adjacent binomial ratios give
S<=binom(m,t)(m-t+1)/(m-2t+1). Using
binom(m-1,t)=(m-t)binom(m,t)/m yields

    I_g/b>=4(m-t)(m-2t+1)/(m-t+1)>=m.                    (6)

The last inequality uses (m-t)/(m-t+1)>=1/2 and
m-2t+1>=m/2. The only extra parameter cases are (m,t)=(2,1),(3,1);
their exact I_g/b values are8/3 and6, respectively, so (6) still holds.
All divisions have positive q,b and m-t+1. Thus

    n Var(F)<=4npb<=8 I(F),
    C_Q<=96 I(F)                                        (7)

for EVERY declared m,t,r. Both sides may tend to zero; no lower positive
controller influence is assumed. With t=1 and m->infinity, b=(m+1)^2/4^m
is exactly A007's requested vanishing-mass leafless stress test.

For completeness, H(F)<=107 I(F) follows from this reference, with no
unspecified source K_ref. Indeed b<=9/16: the extra boundary m=2,t=1 attains
it, while t<=m/4 lies strictly above the half-threshold and q<=1/2.
Also pb>=2^-n. Therefore Var(F)>=pb>=2^-n, since pb<=9/16<3/4, and
h2(Var(F))<=(n+3/2)Var(F)<=11 I(F), as n>=4.
Subprobability coding gives H(F)<=h2(Var(F))+C_Q<=107I(F).
This class already has a threshold-composition description; no novelty of its
FEI theorem is claimed. The NEW result is the complete cost certificate on
the unchanged original high-read leafless prime queue with rare core mass.

## Exact remaining universal line

The two-root certificate pays O(n) bits per nonempty spectral set. It works
here because n Var(F)<=8I(F), proved from the binomial rare-tail margin.
For arbitrary Boolean covers, neither a bounded coordinate-cover number nor
this influence/variance ratio is available. Near the central threshold band,
the crude ambient payment can grow like sqrt(m); one must use actual
subset/rank expectation rather than replace every visit by4W, or group the
regular gates and pay the complete new reference. No universal representation
existence lemma or full FEI statement is inferred.
