# A057 stage 2: the capped recentered activation bank is paid

## exact target, quantifiers, hypotheses and units

The B12 lead asks for a physical-tree payment of the minimum outer-allocation envelope, starting with the original sparse-bent family. This stage proves a scoped all-dimensional payment for every Boolean core u, every fresh point activation F=1+A_r(u-1), r>=1, and every complete adaptive core-first physical tree followed by all control queries. Entropies here are bits. Put p=2^-r, a=1-Eu, K=4+2/(e ln2). The cumulative capped current biased gate bank is at most K p I(u)+5rp a<=K I(F). The constant is approximately 5.0615; the exact symbolic value is used in the proof. A partial core-tree prefix has a separately conserved variance/control reserve. This is not a complete inner-and-terminal entropy payment and does not prove FEI.

## sources actually read, revisions and theorem locators

Read BOARD.md at the stage start, snapshot 2026-10-12 00:39 UTC, B12 STREAM_NOTES.md v2 (23:30 UTC), own STATUS/LEARNED/NEXT_HANDOFF, and EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. The lead assigns the biased identity to A056 and the capped physical-tree bank to A057; this stage follows that allocation instead of rederiving the already completed identity as a new result.

Read in full: A056 stage 20261011T233147Z REPORT, BIASED_ERASURE_INTERFACE and CLAIMS; A024 REPORT stage 20261011T223622Z; B12 lead's L1/L2/R1 claim statements; A059 REVIEW_A057.md stage 20261011T224320Z. A023/A021/A089 learned facts supplied sparse-bent and accounting context. A027 stage 20261011T234627Z report's theorem/proof/terminal/reserve sections and rolling facts distinguish its signed entropy-transport result from this positive cap price. Source snapshots and SHA256 pins are in out/SOURCE_RECEIPTS.json. The earlier stage's exact coherent source is retained there and was not imported anew. No external literature novelty or entire-manuscript audit is claimed.

The A059 review independently reconstructs both A057 v1 claims with no repair. Its acceptance is consumed and recorded locally; original author artifacts and shared registries remain unchanged. REVIEW_A056.md independently reconstructs the biased pair identities and envelope, with a distinct physical activation checker. It records acceptance at source scope, not acceptance of a universal C019 theorem.

## complete derivation or exact first unsupported line

PROOF.md supplies the complete analytic argument. At a core node let m be the actual mean, v=1-m^2, beta the singleton coefficient, t=beta^2, and d its physical influence. The positive gate erasure is
M(s)=Phi((1-p+pm)^2,p^2s)+p(1-p)Phi((1-m)^2,s),
with Phi(s,t)=(s+t)h2(t/(s+t)). The capped envelope is C=min{M(v),(t/v)M(v)+pt log2(v/t)}; t=0 and v=0 give zero. This is A056's current induced-bias outer erasure, not a uniform gate erasure reused after restriction.

The proof shows Phi(s^2,t^2)<=2st in bits by a monotone ratio calculation. The shifted empty-control row obeys (1-p+pm)^2+p^2v<=1. In the second cap branch its p^2 t log2(1/v) term combines with p t log2(v/t), leaving p t log2(1/t)+p(1-p)t log2(v). The latter term is nonpositive. Thus
C<=4p(1-p)d+p^2(2r+1/ln2)t+p t log2(1/t).

The retained rarity term is bounded by [2/(e ln2)]p d. Mean-martingale conservation gives sum w t=Var(u)-E Var(core_leaf), while ordinary physical influence gives sum w d=Pi_I(u). Hence the prefix is at most
[4p(1-p)+p^2/ln2+2p/(e ln2)]Pi_I(u)+2rp^2 V_drop.

For complete core trees, V_drop=Var(u)<=2a and Pi_I=I(u), so the prefix costs at most K pI(u)+2rp a. The control suffix only visits an r-bit point defect with probability a/2. Every point-defect queried erasure is <=3 times that query's influence, so the suffix costs <=3rp a. This gives K p I(u)+5rp a<=K I(F). The prefix's terminal control reserve and the suffix's consumed control influence are accounted for together; the same budget is not reopened at each depth.

The exact erasure ledger retains the negative core empty-pair subtraction:
B_tree(F)=p[B_tree(u)-sum w Phi(m_v^2,t_v)]+sum w M_v(t_v)+expected suffix erasure.
The physical entropy ledger retains the analogous nonempty inner decrement plus actual terminal entropy for partial core trees. Their general payment is not inferred from the cap bound. With outer JS paid separately, the complete-tree inner decrement remains bounded by the explicit pH(u), which is FEI-strength for arbitrary u.

The first unsupported universal line is a common-budget payment of nonempty inner-decrement sums and terminal entropies under a universally valid physical selection policy. For overlapping events with two different cores, even the present two-multiplicity-class gate formula and ownership of control reserve must be rederived; no such extension is claimed. Fresh repeated point controls on a single core collapse to one activation and do not create a new mechanism.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the v1 pilot and main. The 32-case pilot passed in 0.2726 seconds. The first main run reached the 60-second watchdog with no mathematical assertion failure; out/v1_main_stop.json preserves the event. FROZEN_SPEC_V2.json then freezes caching of repeated exact states, unchanged domain, a 60-second pilot and a 120-second main limit. This is a runtime optimization, not a new dimension or search domain. Estimated memory was 70 MB initially and 100 MB for cached v2; no >300 MB job or heavy job was started.

Commands: python -X utf8 runs/20261012T003930Z-account05-A057-coherent-restriction-remainder/code/check.py --pilot, then the same command without --pilot.

V2 pilot: 32 cases PASS. Main: all Boolean cores on n=2,3, r=1,2,3, forward and reverse complete core orders, 1632 actual activation trees; plus the original bent-marker core k=4,6, r=1,2,4,8,12 in marker-first and marker-last order, 20 compressed trees. This includes the original sparse-bent r=2k cases. No symmetry reduction, random sampling, automatic dimension escalation, or Boolean proxy was used.

Main PASS: 10912 exact assertions/certificates in 5.5327104000607505 seconds. Caching means identity counts are distinct evaluated states rather than the number of repeated occurrences. The output records 964 exact biased erasure and 964 exact biased decrement state identities, 1208 cap certificates and singleton bounds, 1652 variance telescope and capped-budget certificates, and 1632 complete-tree erasure/influence identities. Integer Walsh/Fraction spectra reconstruct actual small physical cubes; compressed sparse cases use exact control multiplicities. Rational prime-log coefficient equality proves the identities. Forty-eight-term atanh-series intervals with explicit tails certify signs; a factorial-series interval for e and rational log(2) bound certifies the exact K. Displayed floating ratios are diagnostics only. The maximum observed certified upper ratio was 1.2979823748602934, which is not an optimal universal constant claim.

## proof dependencies and changed downstream conclusions

The A056 v2 positive-sector split and minimum envelope are independently reconstructed in REVIEW_A056.md. The new price uses elementary packet entropy bounds, the Boolean singleton coefficient domination, and physical influence/mean-variance telescopes, all proved in PROOF.md. It does not assume full FEI, ignore core entropy, use the balanced class at biased nodes, or apply overlapping-product entropy subadditivity. A059's review supplies local independent acceptance of A057 v1; the new payment awaits its own independent review.

A056/A059/A064/A097 can now substitute the actual capped activation-bank price on any specified core-first fresh-point tree, rather than placing an unpaid cap at every depth. A027's signed entropy transport remains a different, compatible statement; this stage controls the positive capped gate envelope itself and does not re-advertise the known H<=8I sparse-bent result.

## one next mathematical action and independent reviewer

Test a priority-composed two-core activation whose two point-control events share one physical control bit. Derive the actual signed gate pairs and a single common control reserve while retaining both terminal core entropies. This is the first ownership extension that does not merely stack equivalent fresh point activations. Reviewers A091 (primary) and A090 (alternate) should independently reconstruct the variance-log cancellation, prefix reserve, and point-defect suffix bound; A024 can challenge the subtraction and induced-bias scope. Reviews of this new payment have not run.

## actual persistence receipts or precise save blocker

All required run files, proof/review, frozen specs, helper code, outputs, source snapshots and rolling files are written only inside A057. Claim and progress keys are checked against the protocol; the explanatory suffix of its packet_ids field is normalized to the JSON key packet_ids. PROGRESS and PACKET_DELTA are byte-identical. out/PERSISTENCE.json gives file sizes and hashes after readback; no artifact exceeds 20 MB. Shared registries, other agents' files, brain stores and repositories are untouched. Supervisor adoption/mirror copies and new independent review are pending.

## Universal bridge

This stage moves C019 stopping-tree payment by paying the lead's complete capped recentered gate bank, including the control suffix, at K=4+2/(e ln2) on every core-first fresh point-activation tree, with an explicit partial-prefix variance reserve. It removes this outer charge even for arbitrary biased cores and preserves all inner empty-sector credits. Universal inner-decrement and terminal payments, and common-reserve ownership for two distinct cores with overlapping controls, remain open. NEXT tests that first genuine ownership extension rather than another isolated gate class or a repeated activation transfer that still hides arbitrary core entropy.
