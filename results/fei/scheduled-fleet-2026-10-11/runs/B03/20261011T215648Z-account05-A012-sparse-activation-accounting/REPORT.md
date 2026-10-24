# A012 / B03: sparse activation accounting

## exact target, quantifiers, hypotheses and units

For every Boolean sign g on a uniform data cube and every r>=1 fresh point controls, account for the entire entropy and influence of F=1+A_r(g-1). Identify a proved, nonvacuous admission class closed under the operations used in the tensor/balancing/activation reduction and prove whether the hidden seed enters that class. Entropy is in bits, original-cube I is total physical influence, and biased I used in the composition proof is spectral mean set size. Full FEI remains OPEN.

Result: restriction-hereditary admission reflects the original seed exactly through activation and balanced tensor powers. The explicit globally read-once AND/OR/parity certificate class R is closed under the required operations and has H<=C0 I, C0=2+4/ln2<8. Its membership is equivalent before and after activation. An actual three-bit multiplexer core is excluded, as are all its activations and activated balanced tensor powers. Overlapping substitution is not a closure of R. This is a proper certified class and an admission audit interface, not a universal representation theorem. The class FEI bound and optimal-constant rarity reduction are recovered source results; no novelty is claimed for them.

## sources actually read, revisions and theorem locators

Execution protocol was read completely: fei-execution-protocol/2, revision 2026-10-11-execution-v2. Campaign README, CURRENT_STATUS, claim/obstruction/packet registries, STREAM_NEXT_ACTIONS, A012 assignment contract, and the LaTeX plan were read, with attention to B03 acceptance tests, O-ACTIVATION-EQUIV, G-J-COST and G-LOWSEL-COLLISION. BOARD.md was read at stage start and rechecked during finalization. The specified B03 STREAM_NOTES.md did not exist; this precise access failure does not prevent the packet.

The supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted, particularly C013, C018-C020, C035, X003, X007 and X011. Sources consulted include LOG_ALLOCATION_CURATED sections 3-5, ROUTE_MAP_CURATED activation/admission controls, OVERLAPPING_PRODUCT_NOTE, and reductions/paper/forests.tex (posteriorforest and foresttarget). Prior B05 and B19 reports were read for the accepted local-no-go scope. B09 is review context only and supplies no proof premise. The updated board exposed A011's completed run 20261011T213831Z-account05-A011-representation-existence; its REPORT and CLAIMS were read and its low-boundary continuation is consumed below. A011's claim is pending review, not an accepted premise.

Threshold paper 38-page text SHA256 36a5953075759ea1085b005cb92352d364693c45a37fc35260d3b39f21cde20c: Proposition 7.1, Corollary 7.2, Lemma 7.5, Corollary 7.7, Proposition 8.9, Corollary 8.10. Earlier 29-page text SHA256 056e86b12567f3ba766d4aaeb8beb97042151eee3094c1bcd0d27e6ca32a1007: same Section 7 interfaces, earlier equation numbers 64-69. The 30-page and earlier 31-page percolation texts were consulted at their definitions and opening theorem/geometry scope: no percolation claim is used in this proof. In particular a geometric local guard does not automatically certify an arbitrary activated core. Exact local source hashes are in out/SOURCE_RECEIPTS.json. Online retrieval and brain queries were unnecessary; all mathematics used here is reconstructed from the supplied local primary sources and elementary identities.

## complete derivation or exact first unsupported line

The source-complete derivation is HIDDEN_CORE_TEST.md, with the requested mathematical deliverable ACTIVATION_ADMISSION.tex. The generalized activation ledger keeps empty-data, nonempty-control and constant atoms, reducing to the source's balanced identity. The tensor regime r_t=ceil(2log2(t+1)) preserves the seed ratio and sends minority probability and total influence to zero; its selector entropy remainder is at most 4r_t+2log2(e) after dividing by p_t.

For any sign- and restriction-closed class containing constants and literals, with disjoint-product and fresh-activation closure, restriction of the controls and all but one tensor factor proves exact membership reflection. For R, an activation certificate is OR(-ell_1,...,-ell_r,g), and the product-biased corrected entropy and deficit identities telescope over globally disjoint child blocks. A complete induction for Theta<=2R0 supplies the AND/OR/parity gate constants and hence H<=C0 I. Every terminal is a literal or constant; no core is silently assigned zero coding cost.

The proper-class proof is analytic, supplemented by complete three-bit membership enumeration. The balanced multiplexer has all influences 1/2, incompatible with every possible root split of an AND/OR/parity read-once certificate. Restriction reflection excludes its whole activated tensor family. Yet OR(AND(x,y),AND(-x,z)) computes it, proving explicitly that overlap breaks the certificate.

New dependency delta: for the control-first point activation of the literal y, D=2(1-p), I_sel=rp and I=p(r+1). A011's uncompressed transcript cost is 2D=4(1-p), with cost/I=4(2^r-1)/(r+1) diverging although the function is in the certified class R. Any exact witness W retaining the physical leaf label satisfies H(W|S)>=D-H(F)>=2(1-p)-4rp-2p log2(e), tending to two bits. These calculations are reconstructed independently from the actual Boolean tree, so no unreviewed A011 theorem is needed. They show exactly why posterior erasure must occur before paying the complete witness by influence; they refute neither FEI nor every possible representation.

First unsupported line for a universal application: "Every Boolean function admits a representation relaxing global read-once labels whose complete expected whole-set witness cost is <=K I." This is false for the unchanged R representation because the multiplexer is outside R; a new paid-reuse rule is needed. No bound on the overlap/collision cost or foresttarget is established in this run.

## executed validation with domain, arithmetic, commands and outputs

Frozen before execution: out/FROZEN_SPEC.json, helper A012-exact-v1, all 256 labelled three-bit Boolean cores, r=1,2,3 (768 activations), complete read-once truth-table closure on <=3 original labels. No symmetry reduction and no dimension escalation. Memory estimate 30 MB; maximum runtime 60 seconds, no heavy job and no memok requirement. No GPU, random search, background worker or window.

Command from the A012 folder:

    python -X utf8 runs\20261011T215648Z-account05-A012-sparse-activation-accounting\code\validate.py

Output: out/validation.json, PASS, 5,268 exact assertions, 0 failures, helper elapsed 0.6009093000320718 seconds. Integer FWHT and Fraction arithmetic verify coefficients, normalization, exact entropy atom histograms, and physical versus spectral influence. Exhaustive formula closure has 152 three-bit members and 912 checked coordinate restrictions. out/mux_certificate.json provides the excluded table, coefficients and influence vector. All-dimensional entropy inequalities rest on the analytic proof, with no floating entropy calculation offered as a certificate. The source file hash is 9902fb8629ef61b742bcb1947440749664d70f14a4dfc6436334de711c94cded.

## proof dependencies and changed downstream conclusions

One bundled source-complete local claim is proposed for independent review, not accepted: A012-HEREDITARY-ACTIVATION-ADMISSION@1. It includes the reflection theorem, explicit certified class/exclusion and the newly consumed transcript obstruction. The gate and composition proof is reconstructed completely, with source attribution to the threshold paper. No B09 pending claim or proposed universal FEI bridge is used as a premise. The updated board shows A011's complete pending claim; A011 plus this A012 package reach the per-stream author-candidate cap, subject to any other unindexed live outputs. Next work must prioritize review/repair or consume that dependency rather than open another broad candidate.

A011 can use the reflection test for an admission rule after ensuring each closure actually holds. A013 can use the explicit closure/nonclosure distinction. A002/A005/A021 can use the exact extraction from activated tensor cores. Treating a rare root plus an opaque arbitrary core as a proved easier endpoint is invalid. A read-once certificate is a sufficient structural condition; it is not assumed of all functions, and already-known class bounds are not presented as universal progress.

## one next mathematical action and independent reviewer

Next action: A086 (primary) or A094 (alternate) reconstruct the hereditary reflection, multiplexer exclusion and physical-label posterior lower bound; then A011 optimize its complete low-boundary code on activated y, retaining H(W|S), before extending to activated balanced tensor cores. This consumes A011's actual new interface and isolates the first unavoidable latent-label erasure. Reviewers have not yet responded or accepted this claim. Source-bound handoff is via these saved files, not a message to another agent.

## actual persistence receipts or precise save blocker

All files are saved only inside A012's assigned workspace and immutable designated run directory. Mandatory CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are generated with precisely the protocol fields; packet_ids is ["A012"]. STATUS.md is two lines, WORKLOG.md is appended with a dated entry, and LEARNED.md records the proved identities, admission reflection and explicit failure of overlap closure. out/PERSISTENCE_RECEIPTS.json records local hashes and sizes. Local persistence is verified by code/check_artifacts.py. No shared registry, another agent folder, brain, git, mail, trading tree or source tree was changed. Supervisor copying, remote mirror verification, adoption, publication and downstream mathematical use are not claimed. No save blocker remains; missing B03 lead notes remain an advisory-source gap only.

## Universal bridge

This stage moves C020 whole-set witness cost by supplying an exact hereditary admission filter and a proper fully certified leaf class, plus an explicit failure of A011's uncompressed transcript on activated y: cost/I diverges and at least two asymptotic bits of physical-label posterior entropy must be erased. It does not reduce the numerical universal foresttarget residual or prove a finite universal K. What remains is a constructive representation with every reuse and complete witness charge paid, retaining the arbitrary seed after activation and terminal restriction. The NEXT is the shortest local route toward that universal bridge because it directly consumes A011's live low-boundary interface, isolates the necessary posterior saving on the easiest admitted rare core, and then stress-tests the repair on activated arbitrary tensors rather than recomputing another settled class bound.
