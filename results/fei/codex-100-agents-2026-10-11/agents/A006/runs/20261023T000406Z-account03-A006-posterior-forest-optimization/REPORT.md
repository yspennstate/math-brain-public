# A006 stage 8: overlapping deletions with the original posterior reference

## exact target, quantifiers, hypotheses and units

For every 2<=a<=b and every labelled bipartite deleted graph H with maximum degree at most two, bound the COMPLETE posterior forest cost of the actual Boolean edge DNF G=K_ab minus H. The proved bound is C<42I; when a>=4, C<(283/8)I<36I. The reference keeps all original surviving primes, both endpoint orders, pi=1/4, one fixed lambda=1/b, and all actual partition runs. Entropy is in bits. The empty surviving graph is constant and treated separately. A reusable broader result for half-dense G on 4<=a<=b is C<(91/8)I+2J log2 b. This is a restricted all-parameter proof and a conditional transfer, not a proof or disproof of full FEI. The exact theorem and hypotheses are in CLAIMS.json and DELETED_DEGREE_TWO.md.

## sources actually read, revisions and theorem locators

At this stage: BOARD.md, B02 STREAM_NOTES.md, own rolling files, machine-wide instructions, protocol revision 2026-10-11-execution-v2, A010 run 20261022T231523Z REPORT.md/GROWING_MATCHING.md/CLAIMS.json and relevant helper/finalizer conventions; A008 run 20261021T234312Z REPORT.md/ROOT_PAYMENT.md and hash convention; A010 earlier run 20261021T161852Z code/finalize.py hash builder. The campaign's older end date in the protocol is superseded by the user's explicit 2026-10-23 deadline. Campaign registries, plans, context papers and earlier stages were inherited from earlier source reads; this report does not assert fresh full-paper rereads. Current source claims and their unchanged canonical hashes are pinned in out/SOURCE_CLAIMS.json; bytes read for main dependencies are pinned in out/SOURCE_PINS.json.

## complete derivation or exact first unsupported line

DELETED_DEGREE_TWO.md supplies the full derivation. Actual singleton-root choices sum exactly to product deg(i)/(32b)^|A|D, with no duplicate root sets or factorial. Generic SCC-rooted forest events supply the remaining mixed-sector mass. The root normalization is paid by <9I/8 at the SAME reference. The physical defect event E has exactly h+w_L+w_R+c4<=9a/2 configurations. Its boundary influence J equals the Fourier Dirichlet energy of delta=-2*1_E. Sector perturbation uses the single budget J_R+J_M<=J, rather than spending J twice. The pivotal lower bound I>=(3/2)a2^-a pays J log b by 12I. The constants are 283/8 for a>=4 and 2963/72 for a=2,3,b>=4; b<=3 costs <75I/8. Before the degree-two count is used, the proof yields the broader half-dense transfer C<(91/8)I+2J log b.

For actual posterior optimization, inf_eta[expected negative log run mass minus H(eta)]=-log Q(A), attained by the posterior q(run)/Q(A). Every event used is an actual run. Restricting to selected legal events gives an upper bound on the complete all-run cost, never a lower certificate for a larger family. This also upper-bounds the joint variational infimum containing this legal weight vector.

First unsupported universal line: paying J log b (or a sharper joint spectral occupation replacement) by an absolute constant times I for unbounded deleted degree or arbitrary prime tables. The degree-two exception count cannot be dropped: the saved outside-domain examples violate it. No full conjecture claim follows from these computations.

## executed validation with domain, arithmetic, commands and outputs

Specifications were frozen before execution in FROZEN_SPEC.json, REVIEW_SPEC.json and ADVERSARIAL_SPEC.json. Pilot: 330 functions, 329 nonconstant, 18,784 physical inputs, 22,116 assertions, PASS in 0.579260 seconds. Full census: all 8,875 labelled maximum-degree-two deleted graphs with 2<=a<=b<=4 (no symmetry reduction), plus six specified larger path/cycle/component fixtures: 8,881 functions, 8,880 nonconstant, 2,056,480 physical inputs and 2,180,788 assertions, PASS in 20.828496 seconds. Integer Walsh transforms and physical flips check the actual Boolean spectra, defect counts, influences, exact Dirichlet identity and sector inequalities. Rational atanh remainder intervals rigorously enclose logarithms; no floating sign is used. Reproduce with python -X utf8 code/check.py using its frozen pilot/full CLI documented in that source. Outputs are out/CHECK.json, out/CHECK_ROWS.jsonl and pilot equivalents.

Independent source reconstruction: python -X utf8 code/review.py; 40 matching functions by direct character sums, 20 queue graphs, 4,876 canonical histories, 8,310 distinct singleton root choices and 81,047 assertions, PASS in 7.733031 seconds. out/REVIEW.json and REVIEW_A010.md record the arithmetic and all-parameter proof reconstruction. The implementation imports no author helpers. Two outside-domain examples run via python -X utf8 code/adversarial.py: PASS, 12 assertions; the defect counts 7 and 98 show precisely where the degree-two count fails. The latter also verifies the relevant joint-sector identity under half-density; it is not an exact enumeration of the complete forest reference.

All jobs are small and bounded; no dimension was automatically raised. The memory guard exited 1 (1.3 GB physical free versus 4.0 GB required), so no Lean compiler was launched. code/JointEnergy.lean is unverified formal source, with the hold recorded in out/LEAN_ADMISSION.json. No formal acceptance is claimed. Research computations have finished; no research job remains running.

## proof dependencies and changed downstream conclusions

A010-GENERIC-WIDTH-TWO-FOREST-MASS@1 and A010-GROWING-DELETED-MATCHING-COMPLETE-COST@1 have been reconstructed without mathematical repair, at their original canonical hashes; source statements are copied byte-faithfully as JSON values. The new theorem uses the generic mass claim; the matching theorem is reviewed context, not a circular proof dependency. The width-two signed root payment is rederived directly from the physical implicant-fiber cut, not accepted merely because of a source hash. These two reviews reduce source-review debt; the new degree-two theorem still needs independent review.

Correction to A006 stage 7: the raw-text SHA mismatch was mistakenly classified as invalid A010 metadata. The original builder hashes canonical JSON containing both statement and hypotheses, and its recorded digest is valid. out/HASH_CONVENTION_CORRECTION.json pins this distinction. This run supersedes that diagnosis; the earlier run and all other agents' files remain unchanged. Downstream users should retain the source claim version and canonical digest, not perform a metadata repair.

## one next mathematical action and independent reviewer

Ask existing A010 or the B02 lead to independently reconstruct equations (4)--(16), especially the physical boundary normalization and the single sector-energy budget. Then address the universal bottleneck by paying the dense-transfer J log b term or replacing it with a sharper spectral charge for growing-degree overlaps, retaining the same original reference. These named consumers are handoff targets; no message has been sent and no review acceptance is implied.

## actual persistence receipts or precise save blocker

All artifacts are saved locally in this run and the three A006 rolling files are current. out/PERSISTENCE.json records UTF-8 readback, schema validation, matching progress copies, file-size limits and SHA-256 receipts. No remote mirror, supervisor ingestion or downstream mathematical use is asserted. Administrative brain self-care is degraded: the fresh wake failed on attachment timeouts and stale owner-model/state-of-mind sources; those personal notes remain unverified. Mathematical conclusions here use the explicitly named current mathematical sources and saved exact checks. Nothing in the failed wake was used as proof evidence.

## Universal bridge

C020 whole-set witness cost advances from disjoint deleted matching edges to every overlapping deleted path/cycle union, with complete same-prime posterior cost <42I (and <36I for a>=4), and exposes the more general half-dense transfer C<(91/8)I+2J log b. Actual-run posterior entropy and the original normalizer are retained. The remaining universal bridge is an influence payment for the defect's joint spectral occupation beyond bounded deleted degree, not another root estimate. Studying that exact unpaid charge is the shortest continuation toward full FEI because it removes the present structural hypothesis within the existing whole-set coding mechanism; another isolated low-degree census would not remove it.
