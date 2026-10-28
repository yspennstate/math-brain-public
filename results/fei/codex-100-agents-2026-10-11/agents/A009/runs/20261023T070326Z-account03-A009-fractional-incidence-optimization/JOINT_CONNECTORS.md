# Collision-free whole-set roots pay arbitrary interacting connectors

All costs are in bits. Take two disjoint complete bipartite blocks
L1--R1 and L2--R2, each K_(m,m), m>=2. Add ANY labelled graph
H subset L1 cross R2, including empty or complete H. Let F be the actual
positive edge DNF. Use precisely all its own original edges as primes,
both endpoint orders, pi=1/4, and lambda=1/(2m) on EVERY edge. The maximum
degree is at most2m, so this single fixed vector satisfies every incidence
constraint. Let Q1 denote the original nonempty-conditioned full queue.
Then its COMPLETE nonempty posterior cost satisfies

    C_F(Q1) < (2499/52) I(F) <49 I(F).                 (T)

This permits arbitrary mutually interacting connectors, not only a matching,
bounded degree, or a bounded number. If H is nonempty the graph is connected.
The full posterior refund, all absent roots, and ONE global normalizer remain.
Here Q1 is the FULL original output law Q_* of forests.tex, not the smaller
mass obtained by retaining only its canonical source-SCC partition forests.

## 1. Collision-free singleton-root assignment

First consider one old K_(m,m), at lambda=1/(2m). For a selected output A
choose independently an incident edge for every selected coordinate, each
uniformly among m choices. A collision occurs precisely when a selected left
and selected right coordinate choose each other. On the no-collision event
all chosen gates are distinct. Each owns its assigned singleton, is an
initial root, and has zero children. These are legal original runs even
when gate SUPPORTS overlap: only owned blocks must partition A.
They are not necessarily canonical partition forests as narrowly defined in
forests.tex: their ownership digraph can have one source SCC but several
chosen roots. The queue itself imposes no such SCC restriction. We use its
FULL output law and never apply the canonical root-disjointness lemma here.

Two assignments producing the same set of gates but different owners have
different selected subsets and hence different actual runs. Fixed root order
gives one run per assignment, with no permutation credit. Each singleton root
has ORIGINAL numerator lambda/(4*4*2)=lambda/32: rarity1/4,
specified singleton subset1/4 and zero-child probability1/2.

Couple all choices to choices for all2m vertices. Removing selected vertices
can only remove collision events, so the minimum no-collision probability
occurs when all vertices are selected. Intersections of k collision events
have nonzero probability only when those k edges form a matching. For the
full selected set the first three inclusion-exclusion sums are

    mu1=1,
    mu2=(m-1)^2/(2m^2),
    mu3=(m-1)^2(m-2)^2/(6m^4).

Bonferroni gives probability(no collision)>=1-mu1+mu2-mu3.
At m=2 this equals1/8. For m>=3, mu2>=2/9 and
mu3/mu2=(m-2)^2/(3m^2)<=1/3; therefore it is at least4/27>1/8.
Consequently EVERY nonempty local A has full numerator

    W(A)>=(1/8) (m lambda/32)^|A|=(1/8)64^-|A|.       (1)

For an empty local set W(empty)=1. This proof uses a finite probability
space and third-order Bonferroni, not independence of collision events.
There are m^|A| assignments before rejection; the gate probabilities are
multiplied only for the actual independent root/subset/count choices.

Combine the two old blocks through the unique FIFO merge. Each tuple of
local all-root runs has exactly one global run in the fixed root ordering.
With D0=(1+1/(8m))^(2m^2)-1, for EVERY nonempty global A,

    Q0(A)>=64^-|A|/(64D0).                            (2)

This is only a selected-mass LOWER bound, used for COST UPPER payment.
It is not a lower bound on the variational infimum. In particular it supplies
full support for the insertion comparison without inspecting F's spectrum.

## 2. Joint physical perturbation, with all connectors together

Let f0 be the old two-block OR, t=2^-m, and h the{0,1} edge-OR indicator
of the WHOLE H on the2m free coordinates L1,R2. Put p=E h and
Ih=sum_i Pr[h(x)!=h(x^i)], with p=Ih=0 for empty H.
Let Z be the event that every R1 and L2 bit is zero. Then EXACTLY

    delta=F-f0=2*1_Z*h.

For h=1 both active sides are nonempty. Thus flipping any one of the2m
fixed zero coordinates removes an old boundary edge after the insertion.
Free-coordinate crossings of h create new edges inside Z. It follows by
physical boundary counting, and independently by Walsh Dirichlet energy,

    sum_A deltahat(A)^2=4t^2 p,
    sum_A |A|deltahat(A)^2=t^2(4mp+Ih),
    I1=I0+t^2(Ih-4mp),
    I0=8mt^2(1-t)(2-t).                              (3)

All sums in the first two identities include the empty coefficient, which
contributes zero to the degree sum. The indicator Z has probability t^2.
For a fixed zero coordinate its Dirichlet contribution for delta is2t^2 p;
for a free coordinate it is t^2 times that coordinate's flip influence of h.
There is no sum over individual connector cylinders and no renewed energy.

Since p<=1, Ih<=2m, and t<=1/4,

    I1 >=(13/2)mt^2 >0,
    I0/I1 <=21/13.                                   (4)

For the ratio, I1>=I0-4mt^2 and I0>=21mt^2/2. These bounds do not presume
that adding edges increases total influence; it can decrease it.

## 3. Pay the entire perturbation against the OLD full law

Equation(2) gives log(1/Q0(A))<=log D0+6|A|+6.
The root product bound gives log D0<3m/8, using ln2>2/3. Also
D0>=m/4>=1/2, so log D0+6>0. Dropping only the nonnegative empty-frequency
part of the total delta energy, (3) yields

    E_delta(Q0)
      <=(log D0+6)4t^2 p+6t^2(4mp+Ih)
       <t^2[(51/2)mp+24p+6Ih]
      <=(99/2)mt^2.                                 (5)

The last line uses m>=2, p<=1 and Ih<=2m. This pays ALL interacting
connectors in one original-reference occupation comparison. No log m is
charged per selected coordinate; collision-free root choices were summed
once for the WHOLE selected set.

## 4. Only one normalizer increment

Let k=|H|<=m^2, B=1+1/(8m), and D1=B^(2m^2+k)-1.
The old actual runs embed uniquely in the enlarged original table, with
identical numerator. Hence Q1(A)>=D0 Q0(A)/D1. Moreover

    D1/D0=B^k+(B^k-1)/D0 <=B^k(1+4/m),
    log(D1/D0)<=3m/16+6/m.                           (6)

The actual false probability is q1=q0-t^2p, q0=(2t-t^2)^2<=4t^2.
Therefore v1=4q1(1-q1)<=16t^2 and, by(4),

    v1 log(D1/D0)/I1 <=6/13+192/(13m^2)<=54/13.      (7)

The roots of H are absent in the embedded runs but their exclusions are
included through D1. Their labels are not free; they need not be USED for
this cost upper certificate. Final Q1 has precisely the connected graph's
own surviving prime table and fixed feasible weights.

## 5. Complete posterior assembly

The independently reconstructed A010 same-reference old-block bound is
C_f0(Q0)<71I0/8. A006's general insertion inequality at theta=1, also
independently reconstructed, gives

    C_F(Q1)<=2C_f0(Q0)+2E_delta(Q0)+v1 log(D1/D0).

Using(4),(5),(7),

    C_F(Q1)/I1
      <(71/4)(21/13)+198/13+54/13
       =2499/52<49.

No sequence of connector insertions was used, so there is only one factor
two, one perturbation energy and one normalizer increment, independent of k.
Every code probability is a sum of distinct actual original runs, and the
posterior identity is exactly -log Q1(A). Finite checks audit(1)--(7);
Bonferroni, the cylinder identities and these inequalities prove every m,H.

## Universal scope and first unsupported line

This settles arbitrary one-direction connector blocks on two dense components,
not all connected graphs, the SCC-restricted forest residual, global PI-J,
or full FEI. A008's newer full-output
obstruction to every fixed two-polarity prime-queue mixture is consumed as
a reported source result, not independently accepted in this stage. If that
obstruction holds, unrestricted original-prime PI-J is false; this restricted
certificate must not be presented as evidence of its universal closure.
The reusable mechanism here is summing compatible root assignments once for
a whole set, rather than repeated gate/clause naming. A genuinely broader
reference must communicate shared subdictionary tags once and pay their
global law; an influence bound for that global tag/compatibility bill remains
unsupported. That is the shortest universal continuation of this result.
