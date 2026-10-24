# A029 stage 3: priority transport and a minimal-depth bent gain counterexample

## exact target, quantifiers, hypotheses and units

Boolean signs on independent fair physical bits; entropy in bits,
ordinary influence; D_K=KI-H. r1 is the best relevant root coordinate
entropy-drop/influence ratio. r_d is the best nonempty physical
stopping-tree ratio Pi_H/Pi_I with maximum depth d; r_all allows
all finite physical stopping trees. The domain distinction is essential.

For any m>=1 and any Boolean seed g on m bits, let
F_g(x,y)=(-1)^(x dot y)g(y), p=2^-m. The priority physical tree
described below satisfies the exact arbitrary-seed formulas

  Pi_I=2-p(2+I(g)), Pi_H=4-p(4+H(g)),
  E D_K(leaf)=(K-2)(m-2+2p)+pD_K(g),
  KPi_I-Pi_H=2(K-2)-p[2(K-2)+D_K(g)]

for every real K. No hypothesis H(g)<=KI(g) is imposed or inferred.

For the three-bit point-defect seed, a seven-node depth-four tree
has Pi_H/Pi_I=(184+9log2(3))/102 and therefore
r1-r_all >= (224-9log2(3))/102>524/255>2.05.
Depth four is the first possible gain>2 for this particular root,
certified by an exact finite stopping-cut DP. No globally optimal
ratio or minimum dimension over all Boolean functions is claimed.

The root is a six-variable bent function with H/I=2. Tensor copies
retain this helper violation uniformly in dimensions6t and still
have H/I=2. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md snapshot 2026-10-13 23:49 UTC; B06
STREAM_NOTES.md v2 (2026-10-11 23:26Z), including its A029 gain test;
own STATUS.md and the saved stage-2 proofs/outputs. The board's A029
status was still stage1 although it counted two stages; the interrupted
stage2 artifacts are finalized separately with honest persistence time.
The complete execution protocol revision 2026-10-11-execution-v2 was
read during the prior stage and continues to govern this stage.

A030 LEARNED.md was read for its order-sensitive clipped reserves;
A064 LEARNED.md for terminal reserve/drift sign conventions; A079
rolling facts were searched for correlated-bent overlap. A065
LEARNED.md was absent; no statement was inferred from the absent file.
Their results are context, not proof premises here. B06 R2 and the
baseline physical influence/entropy decomposition are reused exactly.
The stage-2 all-seed paired restriction proof supplies the depth-two
scope; source proof and output hashes are recorded in SOURCE_RECEIPTS.json.
No external-priority or independent-agent-review claim is made.

## complete derivation or exact first unsupported line

DERIVATION.md contains the full arbitrary-seed proof and compact tree.
Sum Fourier characters over x to obtain
Fhat(A,B)=2^-m g(A)(-1)^(A dot B). Thus every coefficient square is
2^-2m, H(F)=2m, I(F)=m. For any root physical coordinate both children
have coefficient magnitudes0 or2^(1-m), so H(child)=2m-2 and r1=4.

Priority tree: query x1,x2,... until the first1, at index i. Query
y1,...,yi and stop. Stop at g when all x are0. On a first1 branch,
fixing the matching y coordinates leaves a paired carrier on m-i
pairs with an actual restricted seed and a global sign. Every such
terminal has H=2(m-i), I=m-i, so its D_K=(K-2)(m-i) is an exact
proved fact. The lone g leaf has physical probability p.

The elementary sum sum_i 2^-i(m-i)=m-2+2p gives the terminal averages

  E I=m-2+2p+pI(g), E H=2(m-2+2p)+pH(g).

Subtract these from root I=m,H=2m to obtain the stated Pi_I,Pi_H.
The first root query has influence1/2, ensuring Pi_I>0. Rearranging
gives the two signed deficit accounts for every K. Their sum is
(K-2)m exactly. At K=2, the full leaf deficit is pD2(g) and the
query credit is -pD2(g). Each account is owned once; the seed is not
assumed certified and is not paid again from descendant credits.

Choose g=-1 only at000. Its spectrum is9/16 at the empty set and
1/16 at each nonempty set, so H(g)=4-(9/8)L, I(g)=3/4, L=log2(3).
The actual compact tree, with coordinates x1,x2,x3,y1,y2,y3, is:

1. Query x1. On x1=1, query y1 and stop.
2. On x1=0, query x2. On x2=1, query y2; stop if y2=1;
   if y2=0, query y1 and stop.
3. On x1=x2=0, query x3. Stop if x3=0; otherwise query y3 and stop.

The complete eight-leaf list and exact squared-spectral entropies are
in out/compact.json. It has the g leaf at weight1/8, two four-bit
bent leaves at weights1/4, four two-bit bent leaves of total weight
5/16, and one constant at weight1/16. These leaves give

  E I=45/32, E H=21/8+H(g)/8,
  Pi_I=51/32, Pi_H=23/8+(9/64)L.

The elementary integer certificate 3^5=243<256=2^8 implies L<8/5.
Hence this tree ratio<496/255 and its gain>524/255>2.05. The
terminal deficit is -5/16+(9/64)L<0; the query credit is
5/16-(9/64)L>0. They cancel exactly to root D2=0.

The direct-transform checker also minimizes expected terminal D2
over all physical stopping cuts of maximum depths3 and4. Its
Bellman recursion is min(actual terminal D2, average of child
envelopes), minimizing over every still-free coordinate. Every
comparison is exact equality of prime-log vectors or a strict
rational-interval sign. It proves minimum cut D2=0 at depth3 and
-5/16+(9/64)L at depth4. By R2 at a D2=0 root, negative cut D2
is equivalent to a paid-tree ratio below2. Thus maximum depth4 is
necessary and sufficient for gain>2 on this witness. This is not a
certificate that the selected tree globally minimizes Pi_H/Pi_I.

Stage2 proves depth-two gain2 for every paired seed and every m:
all codimension<=2 leaves have D2>=0 through the unmatched-pair
core law, and a paired query attains ratio2. It also proves arbitrary
tree gain2 on quadratic bent roots. The lead's unrestricted reading
of "bent 2k: gain exactly2" is false on this cubic root; these narrower
statements survive. The n<=4 certificate needs no correction.

The first unsupported universal line is a bound on the complete
terminal-inclusive account for arbitrary roots at one absolute K.
A small Pi_H/Pi_I alone is insufficient: the actual terminal seed
may have D_K<0, even when the bent parent is already FEI2-certified.
We open no new broad universal candidate while the pending-review
queue is capped; this is the lead-requested helper test and its repair.

## executed validation with domain, arithmetic, commands and outputs

Before execution: SPEC.json and VERIFY_SPEC.json froze the actual
Boolean families, case counts, arithmetic, memory and runtime. Commands
from A029, with this run's path prefixed:

  python -X utf8 code/check.py --pilot
  python -X utf8 code/check.py
  python -X utf8 code/verify.py

Pilot: one priority tree, 121 exact assertions, 0.0117s. Full: every
seed on1,2,3 variables, 276 priority trees, 3,688 internal nodes and
3,964 leaves, 14,495 assertions PASS, 3.2557s. The helper reconstructs
actual truth tables, integer Walsh spectra and physical boundaries,
uses Fraction reach weights, and stores entropy as exact rational
prime-log linear forms. It checks both terminal averages and the
node sums, plus the complete signed account at K=2,4,17/3. No float
or numerical logarithm is used.

Independent implementation of the compact tree and stopping cut:
direct character sums instead of FWHT, its own physical tables and
boundaries, fixed eight-leaf list instead of the primary tree walker.
3,381 assertions PASS; 473 actual restrictions; 0.1701s. Entropy
forms use basis1,log2(3). Exact equality is checked algebraically.
For strict comparisons, ln x is bounded by the80-term atanh expansion
with z=(x-1)/(x+1), tail<=2z^161/[161(1-z^2)]. Compute L=1+ln(3/2)/ln2
using positive outward rational division; z<=1/3. The checker asserts
that every nonzero comparison interval has a strict sign. The main
counterexample sign itself is the simpler integer-power certificate.
This is a second implementation by A029, not independent-agent review.

All jobs estimated at<=40MB; none required the >300MB memory gate.
No GPU, dimension escalation, shell background helper or n=6 ambient
function census was used. Saved outputs: out/pilot.json, checks.json,
compact.json, independent.json, checks.log and verify.log.

## proof dependencies and changed downstream conclusions

B06 R2 is the sole external proof premise for interpreting gain and
signed credit; all spectra and priority identities are proved directly.
Stage2's paired restriction theorem is a local proof dependency for the
surviving depth-two claim, not for the counterexample certificate.

Consumers A028/A064 receive an all-seed signed terminal transport with
one explicit physical influence partition. A030's clipped-prefix
order dependence is a separate object; our exact additive accounts
depend only on the terminal partition. A087/A094 can reconstruct the
cut and strict logarithmic sign. B06/B20 should narrow only the
unrestricted all-bent/gain<=2 benchmark. No claimed universal FEI
theorem or the earlier finite certificate is invalidated.

## one next mathematical action and independent reviewer

NEXT: insert a certified signed terminal-core deficit into an actual
two-branch shared-control selector ledger, and price the coherent
query correction from that single owned reserve. Use the current
A087/A064 terminal conventions and keep both physical child costs.
Retire further bounded-depth gain searches: the unrestricted helper
is refuted and the apparent gain is exactly terminal debt. Reviewers:
A087 (physical/terminal ownership), A094 (exact certificate), with
A064/A028 as downstream consumers and B06 lead for dispatch.

## actual persistence receipts or precise save blocker

All four protocol files, code, frozen specifications, proofs and exact
outputs are saved under the assigned stage3 run. STATUS.md, WORKLOG.md
and LEARNED.md are current. The interrupted stage2 four-file contract
is separately completed with its actual finalization time. Local
artifact and source hashes are in ARTIFACT_RECEIPTS.json and
SOURCE_RECEIPTS.json. No remote-copy or independent review receipt
is asserted; the supervisor remains responsible for those steps.

**Universal bridge:** This stage advances C019 by a general arbitrary-seed
priority transport with exact terminal and query accounts at every K,
and by a minimal-depth actual Boolean counterexample to the proposed
+2 gain shortcut (gain>2.05 at depth4). The surviving depth-two and
quadratic cases are separated explicitly. What remains is a uniform
payment with the terminal seed deficit retained, not another bound on
the queried ratio. NEXT uses this owned signed deficit at a coherent
shared-control split, directly targeting the unpaid term in full FEI
rather than extending an already FEI2-known bent class.
