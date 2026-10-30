# A012 stage 4: two shared bits paid by exact collision ownership

## exact target, quantifiers, hypotheses and units

For every pair of Boolean children G(s,X),H(s,Y) sharing at most two uniform physical data bits, with disjoint private cubes and a fresh selector z, retain both prescribed finite normalized spectral reference costs and pay the complete selector transfer with one physical influence budget. All entropy, CE and KL are bits. References are fixed before spectral sampling and positive on target support; ideal probability costs have a separate integer-prefix rounding convention. Full FEI remains OPEN.

The exact ownership identity B_out=2(d*-delta), d*=min(Inf_z,1-Inf_z), gives B_z<=4d*. Calibrating the at-most-four shared-only atoms produces one complete coherent reference with exact average calibrated terminal debt and CE_F<=average calibrated terminal CE+(4+2/ln2)d*. Thus the one-bit coefficient below seven now covers two shared bits, including a nonlinear common phase. The recursive certified grammar is hereditary and cannot hide an uncertified seed in a rare activation.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-14 01:41 UTC, B03 STREAM_NOTES v2 dated 2026-10-11 23:2xZ, own STATUS, and the complete EXECUTION_PROTOCOL.json v2. Read A013 stage-3 REPORT, CLAIMS, DERIVATION Sections 1-7 and REVIEW_A012; A097 stage-3 REPORT and DERIVATION Sections 1-4; A018 stage-3 REPORT; and A095 stage-3 DERIVATION Sections 1-6, REPORT and CLAIMS. Source paths/hashes are in out/SOURCE_RECEIPTS.json. No new external theorem premise or online priority claim is imported.

The saved one-shared-bit NEXT was already completed by A013 and A097. A013 independently accepted the entire A012 v1 statement; that review is consumed, not copied onto the new version. A095-RANK-KL-EQUIVALENCE@3's new shared-t upper-bound/calibration/debt application is independently reconstructed and accepted locally at exactly that scope. Its rank equivalence, earlier block claims and lower-bound asymptotic claim are not reviewed here. B03's original activation target was completed in stage 2; the latest useful collision dependency determines this stage, with no disagreement with the lead.

## complete derivation or exact first unsupported line

DERIVATION.md gives the all-parameter proof. After sign folding, shared collision minority influence delta obeys delta<=min(d*,4d*^2). Collision entropy is at most h2(delta) by weighted concavity with a zero-minority dummy row. Crucially noncollision entropy is exactly 2(d*-delta), so those rows cannot spend the collision influence again. For d*<=1/4 the resulting scalar bound is B_z/d*<=2+x[1/ln2-2log2 x], x=4d*, whose maximum is 2+2/(sqrt(e)ln2)<4. For d*>=1/4 use max_q[h2(q)-2q]=log2(5/4), giving B_z<4d*. Zero and sign-folding endpoints are explicit. The standard coefficientwise scalar JS inequality adds at most 2d*/ln2.

Calibrate each shared-only child atom separately and preserve its conditional private reference law. Shared row masses in Q are (a_T+(-1)^u b_T)^2/4; private rows have R_child_cal(T)/4 in each selector sector, including off-target private reference mass. Normalization and direct Fourier expansion prove D(P_F||Q)=average calibrated child KL exactly. Calibration removes only its measured categorical KL. All sector identities, shared cancellations, normalizers and arbitrary terminal costs remain.

The original physical identity I(F)=average child I+Inf_z counts each shared coordinate once. Supplied terminal CE bounds give root CE<=max(K_G,K_H,4+2/ln2)I. Extending the literal/constant grammar to mux child intersections of size at most two gives complete CE<7I, using the earlier proved activation bound six, products and signs. Physical restrictions preserve this syntax. Membership reflects back from fresh balanced tensors and rare activations to the original seed.

The new grammar is proper: the four-bit function +1 iff at least two inputs are one has all eight cofactors dependent on all three other bits, excluding an admitted mux root. Seven exact nonproduct rank-one minors exclude disjoint-product roots. Activation is a constant-child mux chain; signs preserve those exclusions. The integer certificate is in out/NONMEMBER_CERTIFICATE.json. Its rare activations therefore remain outside admission. This is no FEI counterexample.

First unsupported line for the same coefficient at three shared bits: the relaxed rare-regime bound has maximum 2+2sqrt(2/e)/ln2>4. This is a limitation of the scalar relaxation, not an actual Boolean refutation of B_z<=4d*. For growing shared width an absolute selector-only coefficient is already refuted by the source bent/point-flip family. Universal source-owned terminal/shared-core reserve and arbitrary terminal reference payment remain unpaid.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede each job: FROZEN_SPEC, SHARDED_SPEC, OPTIMIZED_SPEC and NONMEMBER_SPEC. Estimated memory is 100 MB per Fourier job and 20 MB for the single nonmember certificate, with no planned >300 MB or heavy job, GPU or automatic dimension increase. Each Fourier job has a 55-second internal cutoff and frozen 60-second maximum. Actual peak memory was not instrumented.

Commands from A012:

    python -X utf8 runs/20261014T014452Z-fleet05-A012-sparse-activation-accounting/code/check.py pilot
    python -X utf8 runs/20261014T014452Z-fleet05-A012-sparse-activation-accounting/code/check.py full i
    python -X utf8 runs/20261014T014452Z-fleet05-A012-sparse-activation-accounting/code/nonmember.py

Here i runs 0,...,7 and partitions G labels by gi//32 without a symmetry quotient. The pilot exhausts 4,096 three-bit/two-bit pairs with two references each. The completed census exhausts all 65,536 three-bit/three-bit pairs with two shared bits and distinct private bits, with a fixed additional 256-pair two-reference menu. Maximum physical dimension is five. out/EXACT_RESULTS.json aggregates the passed jobs without counting incomplete runs. Each passed output includes its exact assertion count and observed time.

Integer FWHT numerator vectors are compared to coherent signed child coefficients, squared probabilities and influence are independently checked on physical edges. Calibration/reference normalization and entire CE/debt identities use Fraction and exact rational vectors of prime logarithms. Erasure, cap and strict scalar signs use outward rational 32-term atanh bounds with an explicit geometric remainder. No floating-point sign supports a claim. The finite domain supports the separate all-dimensional analytic proof.

The initial pilot stopped on an opposite binary selector convention in the checker, corrected without changing the theorem/domain. The single full job and shard 1 reached the internal runtime cutoff and are explicitly incomplete. Shards 1 and 2 briefly overlapped after an early launch; both were lightweight estimates of 100 MB, and subsequent jobs awaited completion. The final helper reduces Fraction allocations by comparing whole integer numerator vectors, changes no cases or exact equality, and completes the remaining jobs. CHECK_HISTORY.json preserves these events. The integer nonmember certificate independently checks eight cofactors and seven unordered partitions.

Completed totals: 1,095,401 exact assertions (281,095 pilot and 814,306 across the eight full shards), 69,632 distinct layout cases and 8,704 reference cases. Passed job times were 50.615 seconds for the pilot and 45.445, 7.660, 45.697, 3.217, 18.770, 4.198, 36.290, 14.155 seconds for full shards 0..7. Incomplete runs are excluded from these counts.

## proof dependencies and changed downstream conclusions

A012-DISJOINT-PRIVATE-MUX-ADMISSION@2 strengthens the existing narrow packet mechanism, preserving all v1 conclusions and adding a two-shared-bit complete reference at the coefficient 4+2/ln2. Its new proof is author-complete pending independent review. The saved v1 independent acceptance remains scoped to v1. No third broad universal candidate or self-review is opened. A095's original shared-t upper application requires no repair; its independent partial acceptance is separate from this exact ownership refinement.

A013/A097/A095/A086 can consume the two-bit payment without a nonlinear phase translation or free terminal bank. The mathematical gain over A095's t=2 bound is from 4+3/ln2 to 4+2/ln2, while retaining exact terminal KL. Original incidence queue L,S,R and universal cover existence are not thereby paid. The universal conjecture status does not change.

## one next mathematical action and independent reviewer

At three shared bits test the extremal minority-mass relaxation against actual joint collision row masses and conditional Boolean means; seek a coherent row inequality or an actual Boolean witness before assigning a terminal reserve. Keep delta in one physical influence partition and all terminal CEs. Independent reviewer A086, alternate A094; A013/A095 are natural two-bit interface consumers. These are saved source-bound handoffs, not messages or assumed review completions.

## actual persistence receipts or precise save blocker

The four protocol files, complete derivation, frozen specifications, arithmetic/checker code, exact outputs, execution history and nonmember certificate are saved only inside the assigned A012 run. PROGRESS and PACKET_DELTA are byte-identical. code/finalize.py checks exact claim/progress field sets, statement hash conventions, all report fields, two-line STATUS and per-file sizes; out/PERSISTENCE_RECEIPTS.json records local hashes. WORKLOG and LEARNED are appended. Supervisor copying, shared-index adoption, independent v2 acceptance and mirrors remain unobserved.

## Universal bridge

This stage moves C020 whole-set witness cost by conserving collision influence exactly and paying the first nonlinear two-shared-bit reference at the same below-seven coefficient as the one-bit case, with both calibrated terminal debts and every physical budget retained. The proved admission expands to overlap two, remains hereditary under the needed tensor/restriction/activation operations, and has a concrete nonmember whose rarity cannot bypass certification. No universal FEI bound follows: actual three-bit collision constraints, a nonreused reserve at growing shared width and arbitrary terminal reference costs remain. NEXT tests Boolean realizability of the first over-budget scalar row envelope because that separates a real ownership obstruction from looseness of the current bound; another one-bit or disjoint-private census would repeat a paid mechanism.
