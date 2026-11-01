# A second genuine tail change from the retained signed-tag refund

All logarithms, entropies and cross entropies are in bits. Every physical
coordinate is uniform and independent initially. The construction is actual
Boolean: a is A079's four-bit row, b=1-a^2 is an indicator, a*b=0, and
F=a+z*b*h, for an arbitrary Boolean seed h on a disjoint cube. These same
relations hold after every physical controller restriction. Write A=ahat,
B=bhat, beta=E b^2, alpha=1-beta, m=E h, r=m^2, p=hhat^2. Parseval gives
sum_U A_U B_U=0. References are complete normalized laws, including their
reference-only atoms. Initial influence pricing is a SUPPLIED hypothesis.

## 1. Independent reconstruction of the incoming A032 reset

Supply normalized R with finite CE(p,R), t=R(empty). The tagged reference is
Q(0,U,T)=A_U^2 1[T=empty], Q(1,U,T)=B_U^2 R(T).
For r<1 and t<1 let R_tail and p_tail be the normalized nonempty laws.
For any prescribed nonempty law S and 0<=epsilon<1, put
M=(1-epsilon)R_tail+epsilon S. The signed children G_sigma=a+sigma*b*h
have references

    Q'_sigma(U,empty)=(A_U+sigma*m*B_U)^2,
    Q'_sigma(U,T)=B_U^2(1-r)M(T), T nonempty.                 (1)

Both laws normalize to alpha+beta*r+beta*(1-r)=1; the signed cross terms
sum to zero. True children replace M by p_tail. Hence each child's KL is
beta*(1-r)D(p_tail||M), whereas the incoming KL is
beta[d(r||t)+(1-r)D(p_tail||R_tail)]. The actual physical restriction identity
H(F)-mean H(G_sigma)=B_z(F)+JS_z gives the exact increment

    B_z+mean CE(P_sigma,Q'_sigma)-CE(P_F,Q)
      =-JS_z-beta*d(r||t)
       +beta*(1-r)[D(p_tail||M)-D(p_tail||R_tail)].           (2)

The floor M>=(1-epsilon)R_tail bounds the last KL difference by
log2(1/(1-epsilon)). This independently reconstructs
A032-SIGNED-TAG-VACUUM-TAIL-RESET@1 without changing it. If r=1 the actual
seed is constant: use its explicitly known vacuum law, without a tail
division. If beta=0 there is no seed-sector cost; no strict positive slack
is claimed at this endpoint. Finiteness forces t<1 when r<1.

At the ORIGINAL controller root beta=3/8. For every Boolean seed m=+/-1/2,
t=1/2, epsilon=1/8, (2) is strictly less than -1/64, for ANY normalized S:

    d(1/4||1/2)-(3/4)log2(8/7)
       =(3/4)log2(21)-13/4>1/24,

using 21^18>2^79. This is a refund from the CURRENT actual transaction,
not a newly issued influence quota. Old source/controller debits remain.

## 2. Coherent reference invariant after deleting z

For any normalized seed reference R_c with R_c(empty)=m^2 and finite cost,
define C_sigma(a,b,h,R_c) by the true signed vacuum in (1) and
B_U^2 R_c(T) at nonempty T. The initial post-tag law uses
R_c=r*delta_empty+(1-r)M. At a seed query i prescribe, for BOTH physical
children h_tau,

    R_child=Cal(M_i R_c,(E h_tau)^2),                       (3)

where M_i is the full frequency marginal and Cal keeps the conditional
nonempty distribution and replaces its empty mass. Its complete wrapper
reference is C_sigma(a,b,h_tau,R_child). At a controller query i prescribe
C_sigma(a_tau,b_tau,h,R_c), keeping the seed reference unchanged. These
formulas specify the target law before comparing costs; no arbitrary true
nonempty seed spectrum is supplied as a reference.

All zero-sector, constant-seed and zero-tail cases use their explicit
point laws. If an inherited tail has zero reference mass, finite inherited
CE forces zero actual mass there. It is then assigned zero in the fresh
law. No 0/0 is formed. Every old tail atom of positive mass survives with
the specified conditional weight whenever its new block has positive true
mass. Any other deletion of reference-only mass is an explicit reset and
its CE change is included below.

## 3. Exact block-calibration payment for every later physical query

General elementary lemma: let P,Q be normalized, CE(P,Q)<infinity, and let
pi be a finite partition. Replace Q on each block E by
P(E)*Q(.|E). Then

    CE(P,Q)-CE(P,Q_new)=D(pi P||pi Q)>=0.                  (4)

Blocks of zero true mass contribute zero; if Q(E)=0, finiteness forces
P(E)=0 and no conditional law is needed. This is a full normalized-reference
identity, including mass removed from reference-only blocks.

Apply the ordinary physical query first, carrying the SAME full frequency
marginal Qbar. For a seed query, at nonempty remaining seed T this is

    Qbar(U,T)=B_U^2 (M_i R_c)(T).

Its conditional law on the entire nonempty tail factors B_U^2/beta times
the inherited conditional seed tail. The true child's vacuum entries are
(A_U+sigma*(E h_tau)*B_U)^2. The fresh law (3) is exactly (4), using
individual vacuum atoms (U,empty) as blocks and ONE entire nonempty-tail
block. Thus even the conditional controller law at the vacuum is retained
correctly after its coherent signed change.

For a controller query, Qbar(U,T)=(M_i B^2)_U R_c(T) for T nonempty.
Use individual vacuum atoms as blocks, and one nonempty-tail block for
EACH remaining U. Its true block mass is B_child(U)^2*(1-r). Inherited
within-block conditional law is R_c_tail. The fresh coherent reference is
again exactly the block calibration (4). This also pays the change of
controller tail weights; a product or independence claim about the full
signed child law is unnecessary.

For the original physical query j put pbar=M_j P and

    D_occ=D(P||Q)-D(pbar||Qbar)>=0.

This is the conditional occupancy KL, normalized inside each occupied
frequency fiber. The exact no-reset CE chain is
CE(P,Q)-mean CE(P_tau,Qbar)=B_j(P)+D_occ. Combining with (4), separately
for BOTH complete child laws, gives

    B_j+mean CE(P_tau,Q_fresh_tau)-CE(P,Q)
      =-D_occ-mean D(pi_tau P_tau||pi_tau Qbar)<=0.        (5)

This is not an unsupported comparison of wrapper erasure with beta times
source erasure. All coefficients, normalizers, differing child means,
both terminal CEs and both coarse KLs remain explicit.

Induction using physical reach weights proves (5) for EVERY finite adaptive
mixed seed/controller stopping tree after the tag query, with any chosen
subset of nodes performing these prescribed current-reference calibrations.
Unreset nodes retain the entire current marginal. To justify OPTIONAL reset
nodes after several such steps, observe that every nonempty seed-frequency
entry still factors as C(U)*N(T): controller marginalizations change C, seed
marginalizations change N, and the vacuum contribution stays at seed-empty.
At the next chosen coherent reset, use individual vacuum atoms and one
tail block PER U, even if the last query was a seed query. Its inherited
within-block conditional tail is N(T)/sum_nonempty N; its true block mass
is B_current(U)^2*(1-r_current). Thus (4) gives exactly the prescribed
coherent reference with the CURRENT marginalized seed tail. Immediate seed
queries from coherent parents admit the smaller one-tail partition already
displayed. This also proves arbitrary ordinary no-reset continuations. Initial CE and every prior debit are
unchanged. A097's scalar original-source calibration commutation explains
the seed-tail recurrence, but is not assumed in this proof: the coherent
vacuum has many U-atoms, and controller steps require their own blocks.

## 4. Spend the retained refund on a SECOND genuinely changed tail

At any selected post-tag node first perform the paid coherent calibration
if intervening no-reset steps left only an inherited marginal. Then replace
its current conditional nonempty
seed reference M_v by

    M_new=(63/64)M_v+(1/64)S_v,                           (6)

for ANY prescribed normalized nonempty law S_v. Keep the actual signed
vacuum and all full nonempty controller factors. This is a genuine change
of conditional nonempty profile, not just a vacuum calibration. Its exact
additional CE is the true tail mass beta_v*(1-r_v) times
D(p_tail_v||M_new)-D(p_tail_v||M_v), bounded above by

    beta_v*(1-r_v)*log2(64/63).                          (7)

When r_v=1 or beta_v=0 there is no occupied tail and no tail division.
Choose these second changes on ANY adaptive antichain across BOTH tag
branches, with every complementary complete terminal retained. For each
physical controller/seed query the average beta of the children equals
the parent's beta; this follows from E b_child^2 for a controller query,
and beta is unchanged by a seed query. Optional stopping on the finite
tree therefore gives sum_frontier reach(v)*beta_v<=beta_root=3/8.
Equations (5) and (7) bound the TOTAL additional profile-change cost by

    (3/8)log2(64/63)<3/256,                             (8)

because 64^32<2*63^32. A032's actual first reset saved strictly more than
1/64. The SAME original account thus pays (6), retaining strictly more
than 1/64-3/256=1/256, in addition to all other nonnegative refunds.
There is no replacement of the original source quota. Subsequent arbitrary
mixed physical query trees with the current coherent calibrations are
again paid by (5). The original rate K is unchanged whenever its incoming
tagged reference and all already executed debits were paid at that K.

The hypotheses m=+/-1/2, R(empty)=1/2 and first epsilon=1/8 apply at the
ORIGINAL controller root for this explicit numerical bound. Earlier
controller restrictions do not receive the original 3/8 bank anew. A
restricted root instead uses its actual beta and exact first increment.
The identities (1)--(7) themselves hold at arbitrary restrictions and means.

## 5. Explicit non-point source with two nonconstant active terminals

Take h on four bits with negative values exactly at bit-zero-fastest
truth indices {0,1,2,4}. Its mean is 1/2. Querying physical seed bit0 gives
two NONCONSTANT children with means 1/4 and 3/4. Supply R(empty)=1/2 and
a normalized positive nonflat old tail. First mix its tail with a different
positive nonflat target at1/8 as in (1); keep the exact actual tag debit.
Query seed bit0, prescribe both references (3), then apply (6) with positive
nonflat targets on BOTH resulting seed children. All four full signed
terminals and their exact spectra/references are saved, including nonempty
reference-only labels. Query a further seed bit from each newly changed
profile and retain all eight full grandchild costs. This realizes both
conditional nonempty changes with ACTUAL Boolean truth tables. The exact
checker verifies the complete increment is below -1/256; the general
all-dimensional extension is the displayed algebra and finite-tree proof,
not an extrapolation from that fixture.

## First unsupported line and limitations

For arbitrary Boolean h, an initial finite reference satisfying an absolute
influence price with all relevant source debits remains unconstructed.
Equations (1)--(8) do not remove beta*H(h) or supply that price. Arbitrarily
many positive nonempty-profile changes with no specified remaining credits
remain unpaid. The second mixture is funded ONCE on an antichain; the
1/256 remainder must not be reissued at each descendant. The general
block-KL identities are probability facts, not new Booleanity constraints
excluding normalized non-Boolean vectors. Full FEI and universal
C018/C019/C020/C024 remain OPEN. External review of the new extension and
formal verification are separate from the author's paper proof and exact
finite certificates.
