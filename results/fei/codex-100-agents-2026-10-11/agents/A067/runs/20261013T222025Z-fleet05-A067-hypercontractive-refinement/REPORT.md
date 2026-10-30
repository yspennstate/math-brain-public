# A067 stage 3: final-mask ownership for shared-core edits

## exact target, quantifiers, hypotheses and units

Pay C019 access for two rare graph-controlled edits sharing an arbitrary Boolean core and control block. Let g(x) be Boolean, z contain r dummy controls, and F=g*(-1)^1_E use the actual final edit mask. Sequential flips use XOR; union-once edits use union. If every core fiber has at most k assignments and k*2^-r<=1/4, the proved universal access statement is

    H(F)-E_z H(F_z) <= K I_controls(F)+2 I_core(F),
    K=4r/(r-log2 k)+2/ln2.

For one assignment per fiber and r>=2, K=4+2/ln2<7. For two assignments per fiber and r>=3, K<=6+2/ln2<9. Every quantity belongs to the final F. One reserve is charged across the whole control tree. The theorem allows arbitrary seed dimension, edit domains and graph control maps, and both events may share their complete active core. It does not admit arbitrary terminal core leaves.

If every actual full-reveal leaf satisfies U<=bI, the complete entropy ledger yields H(F)<=max(K,4+2b)I(F). Thus b=1 gives the same <7/<9 constants in the two regimes. Early U stopping retains remaining control influence and has the larger coefficient K+2+2b. All information is in bits, all physical functions are Boolean signs on uniform cubes. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot 2026-10-13 22:15 UTC at stage start, B14 STREAM_NOTES.md v2 dated 2026-10-11 23:25 UTC, own STATUS.md and stage-2 DERIVATION/code/CLAIMS. Re-read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2, and inspected current CLAIM_REGISTRY navigation. Campaign/supplement and threshold/percolation text background from earlier stages is retained; no new paper theorem is invoked without reconstruction.

New originals read: A088 run 20261012T024518Z REPORT/AUDIT/CLAIMS and n128 scope certificate; A066 run 20261013T215841Z DERIVATION Sections 1-5 and exact v2/transfer claims; A070 run 20261013T212602Z REPORT/DERIVATION/CLAIMS, corrected neutralization Section 1 and projection cross Section 4; A069 run 20261012T043929Z DERIVATION (A1)-(A4),(S1)-(S5); A061 run 20261013T215821Z REPORT and PADDING_EDIT_PROOF Sections 1-5. Actual source hashes are saved in out/SOURCE_MANIFEST.json.

A088 independently accepted the prior A067 padding-access theorem, so that baseline is not reopened. A061 now proves the arbitrary-core local point-edit limits (lambda,B,D)=(1,2,4) and retains the terminal deficit; repeating the one-edit limit is retired. A070 refutes a physical-intersection-only cross bill, including with nonempty retained cores, so this stage works with the final combined mask instead of assuming signed edit orthogonality. The stream lead's direction is followed; its original boundary issue has the explicit A070 v2 repair independently reviewed here.

## complete derivation or exact first unsupported line

DERIVATION.md gives the entire proof. Entropy tensorization, the two-point scalar channel, Boolean edge isoperimetry and the full physical restriction identity are reconstructed on the page. The channel bound J_controls<=2 I_controls/ln2 is already dimension-free and extends to real coefficient fields; it is not the novel Boolean payment.

The nonempty-control spectral mass is exactly alpha=E_x[4a_x(1-a_x)], with a_x the final fiber density. Its empty/nonempty flag gives the control erasure price at most 8r*rho+4rho*log2(1/epsilon), where rho is total edit probability and epsilon is active-core support density. Control-fiber isoperimetry pays the first part at rate 4r/(r-log2 k). The new Boolean ownership step pays the second: on each core edge the edit mismatch probability is <=1/2, so the final F edge is pivotal with at least that probability irrespective of the seed edge's sign. Thus I_core(F)>=I_core(final mask)>=2rho*log2(1/epsilon). This charges a reserve 2I_core ONCE after cancellation, never the sum of two separate ancestral reserves.

All actual leaf entropy remains in H(F)=Q+E H(F_z). The U certificate is conditional, and the early-tree proof keeps unrevealed control influence rather than replacing root control influence by spent influence. No small-fiber hypothesis is silently imposed again at descendants. A one-core/one-control-bit Boolean witness refutes the final-edge ownership comparison when the sparse-fiber cap is removed.

The precise dimension loss is the conditional label step H(S_controls|flag,core)<=r, compared with control-fiber physical influence 2rho(r-log2 k). It yields the displayed r/(r-log2 k), not a logarithm introduced by the real log-Sobolev channel. On a codimension-two subcube with r-2 irrelevant controls, H=2 and I=1 exactly, but the crude flag alphabet bound grows as h2(3/4)+(3/4)r. This isolates a removable dimension overcount. Unequal overlapping large fibers need a conditional source-compatible reference after irrelevant controls are contracted.

The first unsupported universal line is a uniformly paid large-fiber conditional reference and/or actual arbitrary-core leaf admission, with the same final-core reserve owned once. The main access theorem is complete at its stated scope; no line in its proof assumes FEI.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded all searches; FROZEN_DIAGNOSTIC.json preceded the fixed diagnostic replay. No symmetry reduction, author code import, automatic dimension escalation, GPU or background process. Estimated memory <=100 MB, so the >300 MB memok gate was not triggered. One mathematical job ran at a time. Every job was frozen below 60 seconds and completed below that cap.

Commands from this agent folder:

    python -X utf8 runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement/code/check.py pilot
    python -X utf8 runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement/code/check.py full
    python -X utf8 runs/20261013T222025Z-fleet05-A067-hypercontractive-refinement/code/check_diagnostic.py

Pilot: 12 fixed fixtures, 291 assertions, 0.0111 seconds. Full: 14,098 cases, 243,717 assertions, 3.7483 seconds. Domains are all 110 graph-fiber configurations with all m=0,1 seeds and r=2; all 5,476 m=1 Boolean seed/fiber configurations with r=3 and <=2 assignments per fiber; all 8,464 m=2 seed/edit sets of cardinality <=2 in the 32-point cube; and 48 explicit m=3/4/6 constant/dictator/Maj3/pointdefect/bent/addressing fixtures at r=3,4. Maximum dimension 10. Cases overlap and are executions, not a count of distinct functions.

The full checker reconstructs every final Boolean truth table, integer Walsh coefficients, physical core/control pivots, each actual restricted core spectrum, exact influence telescope, alpha and row Parseval. Entropy equalities use rational prime-log coefficient maps, cancelling symbolically before interval evaluation. Signs use 20-term range-reduced positive atanh intervals with proved tail, division by a positive ln2 interval and outward rounding to denominator 2^80. The checker certifies the sharper erasure inequality separately and retains all terminal influence/entropy. A SHA256 digest binds the ordered case certificates; the smallest positive reserve margin and all larger named fixture records are saved.

Of the full cases, 14,094 complete trees meet U<=I at every leaf. Four pointdefect fixtures fail that admission; their actual rejected truth tables and exact U/I are saved in out/DIAGNOSTIC.json. They are not declared certified by the access bound. Early U stopping is also checked on the 12 pilot and 48 named fixtures, with remaining control influence retained. The diagnostic adds eight fixed cases and 31 assertions in 0.0013 seconds: three padded-subcube alphabet-loss certificates, the four leaf rejections, and one compressed real-field ownership guard. The guard uses 16 formal singleton coefficients and a binomial edge count, not a 16-bit truth table or an expanded Boolean search. Final primary certificates contain 244,039 assertions; all executed diagnostic revisions total 244,096. out/EXECUTION_HISTORY.json records the successful initial diagnostic and both real-guard revisions separately; overlapping replays are not counted as new functions. No mathematical failure occurred.

The fixed certificates also reconstruct A066's n128 block-scope inequality using rational ln2 lower bound 842/1215, the ownership-cap counterexample, and A070's exact disjoint-edit cross 1/2. All-dimensional quantifiers and growing-dimension diagnostics are supplied by the analytic proof, not an extrapolation from the finite domain.

## proof dependencies and changed downstream conclusions

The main theorem is self-contained. Only the optional terminal corollaries use A067-LOCAL-BOOLEAN-GRANULARITY v1, already independently accepted by A088/A070. Physical identities/telescopes are reconstructed; neither conjectural C018 erasure payment nor universal C019 access is a dependency. The non-Boolean channel bound is separated from the new final-edge Boolean ownership argument, which uses actual sign pivots. An exact normalized real control psi=(1/4)sum of 16 input signs is unchanged by edits at its zero middle layer and z00; its core spectral energy is 1, while the mask core influence is 6435/4096. This invalidates real-field reserve ownership even with the same sparse-fiber cap and confirms the new Boolean step.

REVIEW_AND_CORRECTIONS.md independently reconstructs four incoming versions without repair: A066-POSITIVE-RESTRICTION-HEAT-LEDGER v2; A066-BLOCK-REFINEMENT-HEAT-TRANSFER v1; B14-LEAD-POINT-DEFECT-NEUTRALIZATION v2; A070-TWO-EDIT-PROJECTION-CROSS-LEDGER v1. Source statements/hypotheses/hashes are preserved in CLAIMS.json with acceptance receipts. The repaired neutralization version is A070-authored, not a repair authored by this reviewer. Central adoption remains pending.

Correction: my prior A066 v1 acceptance reconstructed a singleton price but did not explicitly exclude its unqualified block-tree wording. That broad acceptance is withdrawn, using A088's exact Boolean n128 objection; only the block identity and singleton components remain accepted. The author's explicit v2 and retained signed transfer replace it. The majority/address calibration depended only on the block identity and stays accepted. Old run files are unchanged. This correction cannot invalidate the self-contained access theorem.

The source-bound live B14 queue is consumed before opening one new coherent candidate: A067 stage 2 has A088 acceptance, A069 stage 2 has A070 acceptance, and the four remaining repaired/transfer candidates receive the independent reconstructions above. The new candidate is pending independent review and within the two-candidate cap. Receipt, supervisor adoption, downstream mathematical use and remote verification are distinct.

## one next mathematical action and independent reviewer

Build one conditional reference for two unequal overlapping subcube fibers after removing irrelevant controls. Price its actual final-mask control spectrum against physical control influence, keep both actual core leaf entropies, and allocate the existing final-core reserve once. This targets the explicit r-bit label loss that limits the current bounded-multiplicity theorem; another point-edit limit or physical-overlap-only cross bound would repeat a closed or refuted route. Independent reviewers: A070 and A088/A094; consumers A069/A061/A064 and B05/B06/B13/B14/B20.

## actual persistence receipts or precise save blocker

The four protocol files, complete derivation, independent reviews/correction, frozen specifications, code and exact outputs are confined to this prescribed A067 run. out/SAVE_RECEIPT.json records actual local SHA256 hashes and byte sizes, and out/SOURCE_MANIFEST.json pins read-only inputs. Code validates exact protocol key sets, original reviewed statements, new canonical statement hash and byte-identical PROGRESS/PACKET_DELTA. All files are below 20 MB. STATUS has exactly STATE/NEXT lines; WORKLOG is appended and LEARNED records durable facts. No shared indices, other agent folders, brain databases, git trees, mail or remote publication were touched. Local persistence is verified; supervisor copies, mirrors and independent acceptance of the new theorem are unverified.

## Universal bridge

C019 advances from a one-point padding strip to arbitrary final edits with bounded control-fiber multiplicity, including two graph-controlled events sharing their entire active core: Q<=K I_controls+2I_core, with K<9 for k=2,r>=3 and one cancellation-aware final-core reserve. Conditional U-certified complete leaves close the full ledger at max(K,4+2b), but arbitrary core admission remains unpaid and large fibers retain the explicit r/(r-log2 k) label loss. NEXT replaces that precise control-label overcount on unequal overlapping subcube fibers while preserving terminal entropy and the owned reserve; it is the shortest route beyond the now-paid two-event access regime, rather than another isolated one-point class estimate.
