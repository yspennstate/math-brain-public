# A069 stage 3: a simultaneous mask refund for hierarchy codes

Full FEI remains OPEN. This stage continues the exact two-edit debt of the previous packet, consumes the independent acceptance of stage 2, and replaces separate difference-energy pricing by a Boolean multiplicative ledger. One scoped continuation theorem is author-proved and awaits independent review.

## exact target, quantifiers, hypotheses and units

Uniform actual Boolean signs; entropy and complete prefix-code lengths in bits; I is total physical pivotal influence. For the fixed all-subset hierarchy code L_T(S)=1+sum_v b_v 1{S meets C_v}, define Gamma_T(f)=E L_T(S_f) and W_T(f)=Gamma_T(f)-1. The decoder and Kraft/Gibbs entropy bound H(f)<=Gamma_T(f) were already independently accepted. No code choice is allowed to depend on the realized sample.

Target 1, for every such fixed finite tree and every three Boolean signs g,q1,q2 on the same cube: prove an exact signed-cost ledger for f=g*q1*q2 with one nonnegative simultaneous refund per cell-resampling experiment. Target 2: pay the complete two-mask surcharge by the net mask's physical influence for compatible overlapping subcube masks. The latter have common block C and nonempty exclusive blocks U,V, of arbitrary sizes r,s,t>=1, and an arbitrary nonempty core block Y. Their overlap is genuine and compatible; the edit is sequential flipping/XOR, not union-once flipping. Source g is arbitrary and may depend on all these blocks. Its full source code cost is retained.

The new conclusion is Gamma_T(g*q1*q2)<=Gamma_T(g)+12I(q1*q2) for the explicit common/exclusive-block tree. It does not assert a universal Gamma_T(f)<=K I(f) bound. A conditional paid-core consequence is stated separately.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-13 23:59 UTC, B14 STREAM_NOTES.md v2 (unchanged since 2026-10-11 23:25 UTC), own incoming STATUS/LEARNED and stage-2 derivation. Lead's requested majority/addressing endpoint was completed in stage 2 and is not reopened. Reread execution protocol fei-execution-protocol/2, revision 2026-10-11-execution-v2.

New dependencies and objections: A070 run 20261013T212602Z REPORT and DERIVATION Section 3 accepts A069-ALIGNED-EDIT-ENERGY-ADDRESSING@1 without repair; Section 4, X1-X3, exhibits positive weighted spectral cross-cost even for physically disjoint edits and keeps the sequential XOR intersection correction. A017 run 20261013T220934Z REVIEW.json independently accepts the stage-2 S1-S5 subcube interface only, not the whole addressing/decoder claim. Both scopes are preserved. Source manifest records actual local paths, byte sizes and hashes. No brain write, git, external message or new literature/priority search was used.

The A070 positive-cross objection is used as a test and independently reconstructed below; its new cross theorem is not an unreviewed proof premise. The only reused theorem is the earlier complete hierarchy decoder. The Boolean resampling and pivotal-count proofs are supplied in full in DERIVATION.md.

## complete derivation or exact first unsupported line

DERIVATION.md equations (1)-(10) contain the complete proof. For each internal cell C_v, couple X with X^(v) by independently resampling that cell while retaining all coordinates outside it. For a Boolean sign u let D_v(u)=1{u(X)!=u(X^(v))}. Conditional independent copies and Parseval give

    W_T(u)=2 sum_v b_v P(D_v(u)=1).

Disagreements of a Boolean product combine by XOR. For two signs u,w,

    W_T(uw)=W_T(u)+W_T(w)-4 sum_v b_v P(D_v(u)=D_v(w)=1).

Thus Gamma_T(uw)<=Gamma_T(u)+Gamma_T(w)-1 even with shared physical variables. This is code-cost subadditivity, not the false general Fourier-entropy subadditivity for overlapping products.

For three signs g,q1,q2, let M_v=D_v(g)+D_v(q1)+D_v(q2). Then M_v minus its parity is 2 if M_v>=2 and zero otherwise. Consequently

    Gamma_T(g*q1*q2)=Gamma_T(g)+W_T(q1)+W_T(q2)-R3,
    R3=4 sum_v b_v P(M_v>=2)>=0.

This is one simultaneous refund event for each resampled cell pair, not separate payments for each Fourier pairing. Equivalently R3=R_T(q1,q2)+R_T(g,q1*q2); these two events are disjoint on every resampled pair. The ledger retains positive edit/edit cross terms, source/edit rebates, and the intersection correction through actual Boolean multiplication.

For the compatible-overlap family, let A={C=c*,U=u*}, B={C=c*,V=v*}, q1=1-2*1_A, q2=1-2*1_B. Choose binary block trees and T=(T_Y,(T_C,(T_U,T_V))). A codimension-k subcube mask of density rho has occupation probability 4rho*(1-2^{-|E intersects its fixed coordinates|}) in any cell E, and I=2k*rho. Each event occupies at most three join cells, its common block tree and one exclusive block tree. Hence W_T(qj)<=6I(qj), uniformly in block sizes, with no core-coordinate label charge.

Write c=2^{-r}, a=2^{-s}, b=2^{-t}. Direct physical pivotal counts give

    I(q1*q2)=2c[sa+tb+r(a+b-2ab)],
    I(q1)+I(q2)=2c[sa+tb+r(a+b)].

Since a,b<=1/2, their sum is at most twice the net controller influence. The exact refund then gives

    H(f)<=Gamma_T(f)<=Gamma_T(g)+12I(q1*q2).

The source term is not dropped or renewed in the two edits. The complete code is fixed jointly for the two events. Constants, core means and empty spectral atoms are allowed in the ledger. For g=h(Y), disjoint physical product gives I(f)=I(h)+I(q1*q2), and Gamma_T(g)=Gamma_(T_Y)(h)+2Var(h). If the retained core already has Gamma_(T_Y)(h)<=K I(h), spectral Poincare Var(h)<=I(h) yields H(f)<=max(K+2,12)I(f). This conditional product consequence is not a new literature novelty claim; the shared-variable source-cost identity is the transfer mechanism under study.

The A070 witness g=x1 on two bits, edits (+,+) and (-,+), still has positive weighted difference cross +1/2 with zero edit intersection. The new ledger gives W(g)=W(f)=2, input-mask costs 3/2 each, and simultaneous refund R3=3. It therefore reproduces Gamma(f)=Gamma(g)=3 without using a physical-overlap-only cross bound. Sequential overlap is checked at the level f-g=e1+e2-2e12 before squaring.

First unsupported universal line: for g with controller dependence, use the exact refund to transport a paid source cost and net-controller cost to I(g*q1*q2), while retaining all conditional core costs under one physical influence account. Cancellation can make f constant when g=q1*q2. Also the input-mask-to-net-influence comparison requires the private-block hypotheses; identical masks cancel to the constant mask and defeat such a comparison. Nothing here proves a universal paid source hierarchy or a C019 physical first-query stopping rule. The ownership proved is within cell-resampling experiments, not ownership of a physical restriction-tree budget.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before execution, helper A069-stage3-resampling-v1. Standard-library integer FWHT, exact Fraction, direct cell-resampling pair counts and actual physical pivotal edges; no floating entropy signs. Estimated memory 32 MB, frozen runtime cap 60 seconds with a 55-second guard; no >300 MB job or GPU was used. Command from this run: `python -X utf8 code/check.py`.

Actual out/CHECK.json: PASS, 69,890 cases and 144,390 exact assertions, measured Python runtime 6.499 seconds.

* All 65,536 ordered pairs of three-bit Boolean signs verify exact binary product/refund and nonnegative surcharge.
* A frozen subset of 4,096 Boolean triples verifies the exact simultaneous refund using independent resampling disagreement bitsets. It is explicitly not the full 256^3 triple census.
* 256 overlapping-mask/source fixtures: block sizes (r,s,t,|Y|)=(1,1,1,1),(2,1,1,1),(1,2,1,1),(1,1,2,1),(1,1,1,2), every event assignment, four specified source seeds including controller-dependent and complete-cancellation seeds. These test exact physical influence, fixed-tree mask cost, both refund decompositions and XOR intersection correction.
* Two boundary fixtures reproduce A070's +1/2 cross witness with refund 3 and the excluded identical-mask cancellation.

The compatible cases have exact W_T(q)/I(q) values 8/3,3,19/6,19/6,8/3 for the five block-size choices. These are finite checks of identities and implementation; the all-dimensional constant 12 follows from the analytic proof, not those numerical-looking rational ratios. No previous addressing or majority census was repeated.

## proof dependencies and changed downstream conclusions

The complete prefix decoder/Gibbs bound is A069-STABLE-HIERARCHY-EDIT-PAYMENT@1, independently accepted by A070 in its first stage. Stage-2 A069-ALIGNED-EDIT-ENERGY-ADDRESSING@1 acceptance by A070 is consumed as a review receipt, along with A017's expressly partial S1-S5 review. Earlier source statements and artifacts are unchanged.

One bundled scoped continuation A069-BOOLEAN-MASK-REFUND@1 records the exact generic refund and compatible-overlap surcharge. It introduces no universal FEI candidate. B14's positive-cross obstruction remains valid; only the complete multiplicative cost, with its signed refund, is paid here. A070/A067 can now replace blind weighted triangles on actual Boolean mask products by the exact cell-resampling ledger. A017/B05/B13 should distinguish this code-cost ownership from the still-unproved physical stopping-tree influence ownership. The retained Gamma(g) cannot be treated as a universally certified leaf.

## one next mathematical action and independent reviewer

Next: let g depend on one shared control coordinate with two unequal conditional core references, and compare the exact R3 refund with the lost source/controller physical influence and both conditional terminal bills. This is the first source-dependent cancellation case absent from the independent-core consequence; it directly tests the missing budget conversion rather than another point-edit family. Independent reviewers A070/A088/A094; consumers A017/A067/B05/B13/B20. No messages were sent to them.

## actual persistence receipts or precise save blocker

REPORT.md, DERIVATION.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, frozen spec, checker and exact outputs are saved inside A069. Source/review receipts and byte/SHA256 persistence manifest are in out/. STATUS has exactly STATE/NEXT lines; dated WORKLOG and durable LEARNED facts are current. Protocol field sets and statement hashes are checked by code/finalize.py. Local save is complete; independent acceptance of this new theorem, B20 adoption, supervisor copying and remote mirror verification are pending and not inferred from these receipts.

## Universal bridge

This stage moves C020 whole-set witness cost from a single-edit difference-energy identity to an exact Boolean product ledger with one simultaneous cell refund, and pays the complete surcharge of two genuinely overlapping subcube masks by 12 times their net physical influence while retaining the entire source code bill. Universal paid-source selection and source-dependent cancellation-to-final-influence transport remain open; the proven cell refund is not a C019 stopping-tree payment. NEXT addresses one shared-control source dependency with unequal core references because it is precisely where the source-plus-controller budget ceases to equal final influence, whereas another independent-core class theorem would leave that universal gap untouched. Full FEI remains OPEN.
