# A029 / B06: actual child-deficit transport and depth-two gain

## exact target, quantifiers, hypotheses and units

All functions are actual Boolean signs on the uniform cube; H uses bits,
I is total ordinary physical influence, and D_K=KI-H. Full FEI remains OPEN.
The B06 lead's v1 direction replaces rederivation of its R2 telescope with
a bounded measurement of nonlocal gain. For nonconstant f define

  r1(f)=min_{i:Inf_i>0} [H(f)-average H(f_i)]/Inf_i(f),
  r2(f)=min_{T:1<=depth(T)<=2,Pi_I>0} Pi_H(T)/Pi_I(T).

The root must query a relevant coordinate. Each actual physical child may
stop or query a remaining relevant coordinate, independently. The second
query may differ by branch. Root-only trees are included. Pi_H is root
entropy minus weighted terminal entropy; Pi_I is root influence minus
weighted terminal influence. Constants have no divided ratio.

**Certified finite result:** for every nonconstant f in dimensions 1..4,
0<=r1-r2<=2. The maximum is exactly 2. Equality holds precisely for
(a) functions with two essential variables that are signed input/output
variants of AND2, and (b) four-variable bent functions. Here bent means
all 16 squared Fourier coefficients are 1/16. There are 976 equality
truth tables across the enumerated dimensions: 8, 24, 48 AND2 extensions
in dimensions 2,3,4 respectively, and 896 essential four-variable bent
functions. This finite result is not extrapolated to arbitrary n.

**Analytic scoped result:** for the original B05 sparse activated bent
point-surgery family with even k>=4, r=2k, delta=2^-k, p=2^-r,
both physical selector children satisfy D_4>=p(k-3), and the selector
parent satisfies

  D_4(f)>=p[k-3-delta(3k+1/2)]>0.

This explicitly pays an unbounded local-selector ratio from proved child
slack at K=4. No universal induction hypothesis is used for these children.

## sources actually read, revisions and theorem locators

Primary rules: EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2
(read in full); README.md, CURRENT_STATUS.md, CLAIM_REGISTRY.json,
OBSTRUCTION_REGISTRY.json; A029 entry of PACKET_STATUS.json; B06 entry
of STREAM_NEXT_ACTIONS.json; campaign plan B06 packet contracts and
obstruction/consumer passages. The on-disk registries are earlier snapshots
than BOARD.md, read at stage start (2026-10-11 22:37 UTC), and B06
STREAM_NOTES.md v1 (22:38Z). R2 is the supplied baseline; it is not
presented as a new result here. The direction followed is the A029
depth-two-versus-local census.

Supplement: CAMPAIGN.md, CLAIMS.md (C005,C013,C018,C019),
COUNTEREXAMPLES.md, SEED_LEMMAS.md, NATIVE_MAPPING.md; source notes
ERASURE_REDUCTION.md sections 1,2,4, BLOCK_RESTRICTION_IDENTITY_2026-09-18.md
sections 1..4, and LOG_ALLOCATION_CURATED.md sections 4..6.
Earlier B05 run 20261011T193057Z-fleet01-B05-rare-restrictions REPORT.md
and B19 run 20261011T195038Z-fleet01-B19-independent-review REPORT.md
were read for the actual b,b',G,H definitions, means and influences.

Context papers: threshold_paper_38pp.txt Proposition 8.6 / equations
(75)..(79), Corollaries 8.7,8.8 and composition interfaces; earlier
threshold_paper_29pp_earlier_version.txt Proposition 7.1 / (64)..(67).
Percolation 30pp and 31pp versions: introduction, entropy units and
Theorems 1.1,1.2,1.3,1.6. Their geometric hypotheses are not premises
of this work. The earlier percolation version has a conditional pivotal
overlap exponent where the 30pp version states an unconditional exponent;
neither statement is used. Source SHA256 receipts are in SOURCE_RECEIPTS.json.
No external literature priority or novelty is claimed.

## complete derivation or exact first unsupported line

### What the largest gap means analytically

Take g to be a signed AND of two variables. Its four squared Fourier
coefficients are 1/4, so H(g)=2 and I(g)=1; both influences are 1/2.
Each coordinate restriction is one constant and one signed dictator,
both of entropy zero. Thus Delta_i H=2 and r1=4. Query one coordinate,
then query the dictator child and stop the constant child. Pi_H=2 and
Pi_I=1, so r2=2. No proper tree on these two variables can consume more
than all influence or erase more than all entropy; the root-only ratio
is 4 and the complete tree ratio is 2.

At K=2, the root debt Delta_i H-K Inf_i equals 1. Actual child deficits
are 0 and 2, so the weighted reserve is exactly 1. Revealing the dictator
uses its influence but produces zero entropy drop, creating credit 2
at child reach probability 1/2. All terminal deficits are zero. The
credit is spent once at the parent; it is not also retained at a leaf.

A genuinely four-essential-variable equality witness is truth mask 854
in the stated least-significant-coordinate convention. Root coordinate
0 has child masks 30 and 17. Up to signs they are zg and g on the
remaining variables, with H=2 in both branches and I=2 and 1. The root
has flat spectrum, H=4, I=2, Delta_0 H=2 and Inf_0=1/2. Query the
independent character z in the zg child and stop the other child:
Pi_H=2, Pi_I=1. The terminal entropy is still 2! At K=2 the children
have deficits 2 and 0, paying root debt 1 exactly. This exhibits the
entropy-preserving child query that makes nonlocal payment possible.

Every essential n=4 equality table is a quadratic Boolean sign with a
nonsingular alternating 4x4 adjacency matrix. The classification script
checks this directly by Boolean Mobius transform and direct Walsh sums,
and reconstructs the complete set from 28 nonsingular graphs times 32
affine signs. The four graph degree multisets are matching (1,1,1,1),
path (1,1,2,2), triangle with attached leaf (1,2,2,3), and complete
graph (3,3,3,3). For any quadratic, squaring the Walsh transform shows
that its Fourier support is an affine translate of the image of its
adjacency matrix, with equal masses; hence entropy equals matrix rank.
For completeness: the autocorrelation at shift t is zero unless At=0,
and otherwise is a sign character on ker(A). Fourier inversion of that
character gives the stated affine flat support of size 2^rank(A).

In the first three graph types, query the neighbor of a leaf vertex.
Both three-variable children have rank 2, hence H=2; the leaf coordinate
is isolated and its derivative is constant, with influence 1 in one
child and 0 in the other. Query it only in the influence-1 child.
The resulting entropy cost is 2 and influence cost is 1. For the
complete graph, each child is a rank-2 triangle; query any child
coordinate in both branches. Each two-variable leaf retains a quadratic
edge and H=2, while queried child influence is 1/2. Again the costs
are 2 and 1. Every root has local ratio 4.

These trees are optimal analytically too. After any root query, a
rank-2 three-variable child graph is either one edge plus an isolated
vertex, a two-edge path, or a triangle. A second query that drops
entropy has (Delta H,Inf)=(2,1/2). Queries preserving entropy have
influence 1/2, except an isolated vertex which has influence 0 or 1.
For that isolated case the two sibling influences are complementary,
so the weighted influence Z of all entropy-preserving second queries
is at most 1/2. Let E be weighted influence of the entropy-dropping
second queries. Then

  Pi_H=2+4E, Pi_I=1/2+Z+E<=1+E,
  Pi_H/Pi_I>=(2+4E)/(1+E)>=2.

Thus the gain 2 for all 896 bent functions is explained without relying
only on numerical pattern recognition. The finite census excludes every
other equality class and every larger gap.

### Actual-child transport on B05

The complete proof is saved immediately in B05_TRANSPORT.md. Here are
the steps needed to audit the budget. For F=1+A(u-1), mu=Eu in [0,1],
c=1-mu, its constant coefficient is 1-pc; nonempty-control/empty-data
coefficients have magnitude pc; each nonempty-data coefficient p uhat(T)
is repeated 2^r times. With h(t)=-t log2 t, the exact entropy is

  H(F)=p[H(u)-h(mu^2)]+2rp[(1-mu^2)+(1-p)c^2]
       +p(1-p)h(c^2)+h((1-pc)^2).

Using h(t)<=(1-t)/ln2, (1-mu^2)+c^2=2c and the actual activation
influence I(F)=p[I(u)+rc] gives

  H(F)<=pH(u)+4rpc+2p/ln2,
  D_4(F)>=p[4I(u)-H(u)-2/ln2].

For the actual b,b' cores, Eu=sqrt(delta) or sqrt(delta)-2delta,
I(u)=k/2 or k/2+2k delta. Both means lie in [0,1]. The elementary
dimensional entropy bound H(u)<=k gives D_4(G),D_4(H)>=p(k-3), using
ln2>2/3. These are proved child facts, not assumptions of full FEI.

Selector influence is d=p delta=2^-3k. By the baseline split identity,
conditioning and the scalar JS bound,

  Delta_y H<=h2(d)+(2/ln2)d<=d(3k+3/ln2),
  Delta_y H-4d<=p delta(3k+1/2).

Since 2^-k(3k+1/2) decreases for k>=4 and equals 25/32 at k=4,
the averaged child reserve is larger than the selector debt. B06 R2
then gives the stated strictly positive lower bound on D_4(f).
This succeeds on the original all-coordinate obstruction while keeping
the whole child entropy in the ledger. It does not pay arbitrary cores.

### Nonreuse and the exact remaining universal gap

Use B06 R2 as the accounting interface, with b_v=K Inf_{i_v}-Delta_{i_v}H.
For every physical cut L, D_K(root)=sum_{rho in L} w_rho D_K(f_rho)
plus the b_v terms strictly above the cut. Expanding a child replaces
its deficit by its descendant cut deficits and increments; it never adds
them to the unexpanded deficit. Finite induction on successive cuts
gives an ownership rule for all transfers: each terminal deficit and
each signed increment has exactly one owner, identified by physical
node and reach probability. Internal reserves may be used as shorthand
only until expanded. Negative terminal deficits must remain signed.

The repeated-slack mistake has an actual Boolean witness: for m-bit
parity, D_K=Km, but summing weighted actual deficits of every internal
node in a complete tree gives K*m*(m+1)/2. All that apparent extra
reserve consists of the same still-unqueried coordinates repeated at
successive cuts. There is no entropy debt in this example, so any such
reserve-summing rule is already invalid on a trivial FEI case.

Disjoint tensors of m signed AND2 factors retain r1=4 and r2=2. A tree
that clears one factor consumes influence 1 and entropy 2, leaving the
other factors intact. More sharply, for F=g_AND2*h on disjoint variables,
the same tree has Pi_H=2, Pi_I=1 and terminal functions equal to signed
h. Thus D_K(F)=D_K(h)+(K-2). The cheap depth-two step does not erase or
prove the seed's entropy bound. A universal proof still needs a physical
tree whose total paid increments plus actual terminal deficits establish
D_K>=0 for every seed, at one dimension-independent K. This is the
first unsupported universal line. No new broad universal candidate is
opened while B06's pending-review queue is capped.

## executed validation with domain, arithmetic, commands and outputs

All specifications were written before their searches: SPEC.json,
VERIFY_SPEC.json and STRUCTURE_SPEC.json. No symmetry reduction was
used. No job exceeded 300 MB estimated RAM; no memory-gate call or
GPU was needed. No dimension escalated beyond the frozen n=4 census.

Commands, from A029 folder:

  python -X utf8 runs/20261011T223746Z-fleet05-A029-child-deficit-transport/code/census.py --maxn 3
  python -X utf8 runs/20261011T223746Z-fleet05-A029-child-deficit-transport/code/census.py --maxn 4
  python -X utf8 runs/20261011T223746Z-fleet05-A029-child-deficit-transport/code/verify.py
  python -X utf8 runs/20261011T223746Z-fleet05-A029-child-deficit-transport/code/structure.py

The pilot finished in 0.019 seconds. The full census completed in
11.917 seconds, checking 65,804 nonconstant truth tables and 3,799,698
candidate trees. Counting constants, dimensions 1..4 contain 65,812
truth tables; the helper also processes the two zero-dimensional signs.
Every spectrum uses integer FWHT; coordinate influence is independently
checked against its physical edge boundary. Entropy comparisons use
rigorous rational atanh bounds rounded outwards to the grid 2^-80.
No floating-point value participates in a sign or optimum decision.

For x in [1,2], z=(x-1)/(x+1)<=1/3 and
ln x=2 sum_{j=0}^{N-1} z^(2j+1)/(2j+1)+R, with
0<=R<=2 z^(2N+1)/[(2N+1)(1-z^2)]. N=90 is used.
Integer logs are reduced to [1,2]; division by the positive ln2 interval
is outward. Dyadic log endpoints are exact. Entropy endpoints use
H=2n-4^-n sum_s W_s^2 log2(W_s^2). Ratios are compared by integer
cross multiplication. The global maximum upper endpoint is EXACTLY 2,
and the AND2 witness lower endpoint is EXACTLY 2.

The second implementation completed in 22.648 seconds. It uses direct
character sums instead of FWHT, independently derived physical boundary
influences, a distinct log series -ln(1-t)=sum_{j=1}^N t^j/j with remainder
at most t^(N+1)/[(N+1)(1-t)], t<=1/2, N=160, and precision 2^-72.
It certifies every tree implicitly via a min-cost depth-two dynamic
program: K=r1_upper-2, root debt plus each branch's minimum of stopping
cost 0 and second-query debt is >=0. Hence every tree's ratio is at
least r1-2. It reproduces all 976 equality masks. This is a second
implementation by A029, **not independent-agent acceptance**.

structure.py verifies all 896 bent equality masks by direct transforms,
the complete 28*32 quadratic parameterization, and positive rational
B05 transport lower bounds for even k=4..40. The analytic proof covers
all even k>=4; formula checks are not its all-k proof. Outputs:
out/census_n4.json, out/census.log, out/verification.json,
out/verify.log, out/structure.json, out/structure.log.

## proof dependencies and changed downstream conclusions

Baseline C005 / ERASURE_REDUCTION sections 1,2 and B06 R2 provide the
physical entropy/influence identities. B05's accepted family and B19's
review provide a source-bound stress construction. No B09 biased claim,
no unproved universal FEI assumption, and no percolation theorem is used.
The finite result is self-contained after the definitions; the all-k
transport uses the baseline scalar JS bound and explicit B05 means.

A028/A064 can use the AND2 and bent equality examples as positive
nonlocal-payment controls, the parity reserve-summing example as a
negative ownership control, and the B05 bound as proof that this
particular local no-go is compensated by actual child slack. A052 must
retain negative and positive descendant deficits rather than replacing
them by nonnegative assumed reserves. None of these deltas settles C019.

## one next mathematical action and independent reviewer

NEXT: test whether the depth-two gain bound r1-r2<=2 survives an
arbitrary-core selector whose two physical branches retain the same
core, deriving a structural bound or an explicit Boolean counterfamily
without discarding terminal D_K. This extends the attained quadratic
mechanism toward the hard arbitrary seed and can distinguish bounded
lookahead from a genuinely global stopping rule. Do not repeat n<=4
enumeration or the baseline telescope. Independent reviewers: A087
(physical reserve/terminal ownership) and A094 (exact interval and
optimization reconstruction), with B06 lead overseeing the next scope.

## actual persistence receipts or precise save blocker

All outputs are local to the authorized A029 run folder. CLAIMS.json,
PROGRESS.json, PACKET_DELTA.json, CHILD_DEFICIT_TRANSPORT.tex and
SLACK_FLOW.json accompany this report; STATUS.md, WORKLOG.md and
LEARNED.md are current. SOURCE_RECEIPTS.json records source hashes;
ARTIFACT_RECEIPTS.json records final file hashes and sizes. No save
blocker remains. Supervisor copying, GitHub mirror verification, and
independent review have not occurred within this stage and are not claimed.

**Universal bridge:** This stage advances C019 stopping-tree payment by
an exactly measured two-level gain (maximum 2 through n=4), an analytic
payment of the original B05 selector obstruction at K=4 from actual
child reserves, and an explicit nonreuse interface with a Boolean
overcount witness. What remains is a dimension-independent payment for
arbitrary-core terminal deficits, not merely more good finite examples.
The shortest next route is to transport or falsify this attained
depth-two mechanism on selectors with an arbitrary seed: the AND2*h
identity exposes precisely the unpaid seed and avoids another isolated
class census.
