# exact target, quantifiers, hypotheses and units

A023/B05 stage 2, run 20261012T010933Z-fleet05-A023-amortized-rarity-budget. All functions are genuine Boolean signs on a uniform physical cube, all entropy and KL units are bits. Let g be any core, a=1-Eg, and use disjoint physical blocks of s>=0 common controls and r,t>=1 exclusive controls. Their specified point indicators are A_s,A_r,A_t, with all shared literals compatible. Define

    F=1+A_s(A_r OR A_t)(g-1),
    u=2^-s, p=2^-r, q=2^-t, beta=p+q-pq.

The two events A_s A_r and A_s A_t share their common physical controls and the SAME core. Their intersection is counted once. The specified stopping rule queries common controls first, then the first exclusive block until its event succeeds or fails, and the second block only if the first fails. Stop at a constant or at g when the union event is resolved. This is finite, physical and adaptive; max depth s+r+t, with no core coordinate queried. Retain terminal entropy u beta H(g).

Primary theorem: if a>=11/16, every control query of this tree is good at the strict threshold K=4, B_v<4d_v whenever d_v>0. Thus its localized odd-face charge sum_(B_v>4d_v) w_v I(g_v h_v)/2 is exactly ZERO, in all dimensions and all independent widths s,r,t. Its queried influence and terminal resources are exactly

    I_ctrl=u a[s beta+r p(1-q)+t q(1-p)],
    I_leaf=u beta I(g), H_leaf=u beta H(g), I(F)=I_ctrl+I_leaf.

The complete erasure/entropy ledger gives H(F)<7I_ctrl+H_leaf, minority/KL debt plus terminal <=4I_ctrl+H_leaf, and minority/KL debt including its 3mu/ln2 allowance plus terminal <9I_ctrl+H_leaf. If g fairly selects ANY bent function on even k>=4 data bits or its one-vertex flip, H(g)/I(g)<3, so H(F)<7I(F), J+terminal<=4I(F), and full sufficient mismatch ledger<9I(F). These statements pay the common controls and shared core only once. They are scoped class results, not universal FEI.

This stage also retracts the erroneous prior A023 acceptance of A021's negative logarithmic remainder; no previous stage file is changed.

# sources actually read, revisions and theorem locators

Read BOARD.md (2026-10-12 01:21 UTC supervisor snapshot), B05 STREAM_NOTES.md v2 (2026-10-11 23:4xZ), own STATUS.md and the full EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2. Initial read attempts failed at the tool host; work started with an explicit access checkpoint and independent algebra, then required sources were obtained before adopting the stream target. Lead direction: correct the A021 review and test two overlapping controls against exact bad-node odd-face transport.

Read Claude B05 run 20261011T225000Z REPORT.md, particularly sections 2-3: odd-face identity/localization and the sign objection. Read A021 stage-2 CORRECTION.md and CLAIMS.json: the corrected A021-UNIFORM-RARE-CORE-EXPANSION@2 and the exposure/order obstruction. Read A022 stage-2 REPORT.md, sections on constant-child transfer and descendant charges, and A025 stage-1 REPORT.md (threshold-2 refutation, strict threshold conventions). A021's v2 is already independently accepted by A087 according to the board; no duplicate acceptance is attempted here. The prior A023 REPORT.md/REVIEW_A021.md are audited for actual dependency, not treated as flawless premises.

No shared indices, other agents' files or brain stores are modified. The earlier campaign/paper sources remain context from stage 1; this stage uses no new external paper theorem, percolation assumption or Internet claim. Source hashes and exact read scope are in out/source_receipts.json. Lead's floating finite ledger supplies motivation only; this stage's finite classifications use rational intervals and its all-width result is proved below.

# complete derivation or exact first unsupported line

## 1. Correct the old review, preserve unaffected mathematics

CORRECTION_A021_REVIEW.md is the source-bound correction. The coefficient 1/j-2/(j-1)+1/(j-2)=2/[j(j-1)(j-2)] is POSITIVE. Hence b(q)=-2(1-q)^2log2(1-q)=2cq-3cq^2+R(q), with R(q)=+4c sum_(j>=3) q^j/[j(j-1)(j-2)]. Its decrement remainder R(u)-R(2u)/2 is negative. The old A023 review's multiplication and its acceptance of A021-UNIFORM-RARE-CORE-EXPANSION@1 were wrong. Retract that acceptance; narrow its report-wide endorsement. The separate exact A021-CONTROL-FIRST-KL-LEDGER@1 remains valid.

An exact rational witness is R(1/2)=1/2-c/4>31/224>0 because ln2>56/81. The repaired v2 upper remainder follows by bounding each positive tail coefficient by 2/3. This confirms the objection without relying on a floating decimal. The first A023 family/tree claim used its direct node formula, elementary entropy inequalities and exact influence counting; neither R nor the decrement remainder occurred. Its constants and family theorem survive unchanged. No new contribution to A021 v2 is asserted, and no copied accepted v1 status may continue to authorize its false tail sign.

## 2. Exact resources for the overlapping events

At a common control coordinate, pivotality needs all other common controls active, the union of exclusives active, and g=-1. Its influence is u a beta. Each first-exclusive coordinate has influence u a p(1-q); each second-exclusive coordinate has influence u a q(1-p). Data influences are u beta times the core influences. Summing yields the stated partition. Terminal core probability is u beta, not u(p+q); paths where both events hold still have one copy of g and one terminal bill.

The rule is determined only by previously queried physical values. A mismatch of a common control stops immediately. A successful first exclusive event resolves the union and stops at g. If it fails, query the second exclusive event, stopping at its first mismatch or its success. A fixed-order tree that queries skipped irrelevant controls has the same ledger, since those splits have B=d=I(child product)=0; this equivalence is used by the finite implementation.

## 3. A local exposure inequality, not a guessed transfer

Consider a first-exclusive node with l controls remaining. Write C for the second event, whose conditional probability remains q, and rho=2^-(l-1). Its children are

    f0=1+C(g-1),
    f1=1+[C+(1-C)A_(l-1)](g-1).

Disagreement is d=a rho(1-q)/2. In Fourier fibers involving a NONEMPTY subset of the remaining l-1 first-exclusive controls, f0 has zero coefficient. Therefore each such parent packet has equal spectral-bit masses and B=2e. The squared point indicator's fraction on its empty label is rho, so these fibers have total mismatch (1-rho)d and erasure 2(1-rho)d exactly. All other fibers have total mismatch rho d and total packet mass M<=1. Concavity gives their erasure <=M h2(rho d/M)<=h2(rho d), since the latter expression increases with M. This is valid for signed mismatch as well as magnitude minority: binary entropy is the same whichever half is smaller. No unsigned substitution is made in a KL formula.

Using h2(x)<=x log2(e/x), obtain

    B/d<=2(1-rho)+rho log2(e/(rho d)).

The more general sufficient criterion is a(1-q)>e/8. Under this criterion rho d>e rho^2/16 and

    B/d<2+2rho[1+log2(1/rho)]<=4.

The final inequality is dyadic, not a continuous maximization: rho=2^-j and (j+1)2^-j<=1 for every integer j>=0, with equality only j=0,1. In our two-event class q<=1/2 and a>=11/16, so a(1-q)>=11/32>e/8. This proves first-exclusive goodness in all widths, independent of core dimension or Fourier details.

For a common-control node the inactive child is constant and the active child is an activation of the union-core function. After the first-exclusive event fails, a second-exclusive node is likewise constant-child. For any such split define d=Pr(child=-1). Its signed packet formula is

    Jsgn=d-d^2+d^2 log2((1-2d+2d^2)/d^2),
    B<=Jsgn+c d <=[1+c+2c/e]d<4d,

where d log2(1/d)<=c/e. At d=0 the split contributes zero. This formula remains valid for a negative child mean; minority allocation and signed allocation are not equated. Thus every node before the certified core is reached is good.

Rational constants: ln2>2(1/3+1/81)=56/81, hence c<81/56. Also 65/24<e<65/24+1/100<11/4: the exponential tail from 1/5! is bounded by the geometric ratio 1/6. These bounds prove 1+c+2c/e<4, 4+2c<7 and 4+3c<9 by Fraction arithmetic. The detailed exposure proof is saved immediately in OVERLAP_GOOD_NODE_PROOF.md.

## 4. Complete cost, terminal entropy and face ownership

For an actual split, Delta H=B+JS and JS<=2c d. One elementary proof writes two probabilities as s(1+z),s(1-z) and uses [(1+z)ln(1+z)+(1-z)ln(1-z)]/2<=1-sqrt(1-z^2). The derivative of the difference is z/sqrt(1-z^2)-artanh(z)>=0 on [0,1]. Summing gives JS<=2c mu<=2c d, with mu the magnitude minority mass. Thus the exact entropy telescope gives H(F)<=4I_ctrl+2cI_ctrl+H_leaf. Likewise Jminor<=B and mu<=d give the two required retained-KL bounds without discarding a terminal remainder.

Let Q(f)=2^(1-n) times its number of odd 2-faces, meaning corner product -1. At a split, faces not using that direction partition into child cubes, and faces using it are precisely boundary edges of the child product. Hence Q(f)=I(g_v h_v)/2+[Q(g_v)+Q(h_v)]/2. This proves first-revelation face ownership: every face is charged exactly at the first split along one of its two directions. The stopping tree retains expected Q(leaf), just as it retains expected H(leaf). We do NOT spend every odd face: since all its control nodes are good, the localized bad-node part is exactly zero. Total unlocalized face cost may still be large.

Coordinate ownership is also explicit. There is one common block account s u a beta, not two copies attributed to the two events. The exclusive block accounts include their survival factors (1-q) and (1-p). One terminal core account u beta I(g) pays u beta H(g). Each physical coordinate is queried at most once on any history; every expected debit is included once in I_ctrl. This resolves shared-control/shared-core ownership for this declared two-event family.

## 5. Unconditional all-dimensional terminal family

Let b be any bent sign on even k>=4 bits and v any vertex. Let b' flip b only at v, and let g choose b or b' by one fresh fair selector. Put delta=2^-k and s_v=b(v). Bent flatness gives I(b)=k/2 and |Eb|=sqrt(delta). An edge-count change gives I_i(b')-I_i(b)=2delta b(v)b(v^i), and selector influence delta. Hence

    I(g)>=k/2-(k-1)delta>=7k/16,
    H(g)<=k+1<=5k/4,
    H(g)/I(g)<=20/7<3.

The exact mean is Eg=Eb-delta s_v, so a>=1-sqrt(delta)-delta>=11/16. Thus every such core meets the exposure hypothesis, with independently unbounded k,s,r,t. Combining its certified terminal cost with section 4 yields H(F)<7I(F), J_tree+terminal<=4I(F), full sufficient mismatch ledger<9I(F). This improves the earlier disjoint-event constants while paying the overlapping point masks. The elementary core H/I bound itself is not claimed as novel.

## 6. Exact finite comparison of four COMPLETE orders

The frozen grid has s=0,1,2; r,t=1,2; k=2,4, with the positive quadratic bent core flipped at zero. That is 24 actual roots, each with four complete orders, plus its control-first stopping tree. Original coordinate order is common/exclusive-A/exclusive-B/data/selector. Orders are explicitly:

- selector-first: selector, all controls, data;
- control-first: all controls, selector, data;
- data-first: data, all controls, selector;
- control-data-selector: all controls, data, selector.

The maximum exact ratios Q_bad,4/I over this declared grid are:

| Complete order | Maximum |
|---|---:|
| selector-first | 14/137 |
| control-first | 12/137 |
| data-first | 0 |
| control-data-selector | 0 |

All 24 stopping trees have Q_bad=0, as the all-width proof predicts. Complete control-first still queries a possibly bad selector in its terminal core; its positive ratio is therefore consistent with zero CONTROL-node cost. The terminal entropy in the stopping theorem is not silently erased. k=2 is only a finite endpoint test, not part of the k>=4 terminal theorem. The zero data-first/grid result is not extrapolated: A021/A022 exhibit other cores whose data-first descendants are bad.

First unsupported universal line: arbitrary overlapping event systems admit a physical reveal order with sufficiently exposed disagreement a(1-q)>e/8 at the needed nodes, or have another single-use payment when that exposure fails, AND their terminal cores have a certified cost. With three or more events q can approach one and the current sufficient criterion may fail. Arbitrary core entropy remains a separate FEI-strength obligation even when a is large. No every-tree or universal selection theorem follows from the finite table.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec out/FROZEN_SPEC.json preceded the search; certificate-only update out/SPEC_CERTIFICATE_UPDATE.json added saved endpoints without changing domain. Helper code/check_overlap.py v1.1 constructs all actual truth tables, uses integer FWHT and Fraction edge counts, represents B-4d as rational prime-log vectors, and decides signs by 24-term outward atanh intervals, allowing a frozen 48-term fallback. Empty vectors are exact equality and are good. No floating sign test, random seed, symmetry omission or automatic dimension increase.

Command from A023: `python -X utf8 runs\20261012T010933Z-fleet05-A023-amortized-rarity-budget\code\check_overlap.py`.

Pilot v1: 24 roots, 96 complete trees, 24 stopping trees; 962 exact assertions; 323 unique node classifications, 50 exact-equality decisions, 24 terms sufficed; observed compute time 0.5971277999924496 seconds. The certificate rerun's exact count/time is in out/validation.json. Results are flushed after every root to out/results.json. Every distinct sign interval and its vector are saved in out/sign_certificates.json. Both passes stayed below the frozen 60-second cap and 100 MB estimate; no >300 MB job was run. This is an implementation check, not independent agent acceptance.

Checks include actual spectrum Parseval, physical influence decomposition at every cached node, direct root odd-face enumeration vs the complete-tree face telescope in all four orders, exact queried/terminal influence partitions, terminal entropy as an exact log vector, and the zero localized control charge. out/constant_certificate.json and the correction record contain rational analytic constants. Schema/file hashes are checked by code/save_metadata.py.

# proof dependencies and changed downstream conclusions

The new exposure and overlap ledger are self-contained: Walsh orthogonality, point-indicator empty-fiber fraction, entropy concavity, the displayed JS scalar inequality, exact influence and face counting, and the bent flat-spectrum definition. The lead's localized bridge motivates the chosen metric; its universal open step is not assumed. A021 v2 is read and its v1 review corrected, but no asymptotic remainder is a premise of this theorem. A022's all-r constant-child result is compatible background; the weaker sufficient bound needed here is independently proved.

Changed conclusions: the old A023 acceptance of the negative-remainder expansion must be withdrawn at its exact source version; the prior A023 first-revelation bound survives the dependency audit. A021/A029/A064 now have an explicit exposure criterion a(1-q)>e/8 and one exact ownership partition for two intersecting compatible subcube events with a shared terminal. A025's threshold-2 refutation remains untouched. This stage repairs and verifies the lead-directed scoped mechanism; it opens no broad universal candidate despite the stream's pending review queue.

# one next mathematical action and independent reviewer

Next: analyze three compatible point events with one common core, in the physical state where two unresolved events make q near one. Use the exact exposure inequality to identify the first failing node; prove a single-use complement/survival payment there or produce an actual growing bad-node face bill. Keep the terminal bank and common-coordinate partition. This consumes the new mechanism rather than widening the finite census.

A087 should reconstruct the empty-activation-fiber split and actual badness signs; A094 should check the strict dyadic inequality, common-control ownership and terminal quantifiers. B20 should propagate the scoped v1 review retraction. Handoffs are saved for supervisor collection; no messages were sent.

# actual persistence receipts or precise save blocker

Saved inside this assigned run: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, CORRECTION_A021_REVIEW.md, OVERLAP_GOOD_NODE_PROOF.md, code/check_overlap.py and code/save_metadata.py, frozen specs, per-root exact results, saved sign/constant certificates, source hashes, schema check and persistence receipts. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current and explicitly supersede the erroneous review lesson. All artifacts are below 20 MB. Old stages and all shared trees are read-only. Initial tool-host timeouts were overcome; no remaining local save blocker. Independent review, supervisor copying, repository mirrors and downstream adoption remain unverified.

**Universal bridge:** This stage moves C019 and B05's localized odd-face bridge by resolving the first shared-coordinate/shared-core case: two compatible rare subcube events have an explicit physical exposure criterion, a control-first tree with exactly zero threshold-4 bad-node face cost, and a complete retained-terminal ledger H<7I on an unbounded activated bent-surgery family. It also retracts an incorrect source-version review without invalidating the previous direct ledger. What remains is payment when unresolved unions make a(1-q) small and when terminal cores lack certificates. The NEXT targets the first exposure failure for three events with a single owned physical budget; this is the shortest route to a universal stopping mechanism because it attacks the newly isolated overlap obstruction rather than another disjoint-family or finite-width result.
