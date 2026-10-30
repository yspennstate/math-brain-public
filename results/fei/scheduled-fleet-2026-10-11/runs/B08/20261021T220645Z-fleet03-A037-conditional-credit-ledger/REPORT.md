# A037: an exercised reset with one original surplus allocation

Full FEI remains OPEN. A biased rare-core history now supports an actually exercised first reset followed by arbitrary private-data product resets, after a quarter-bit prior debit. One original child allocation pays the positive first excess and retains at least 3/20 bit at every stopping frontier. The mathematical rung is a proof with exact finite base certificates, pending independent review. It is not Lean-checked.

## exact target, quantifiers, hypotheses and units

For every n>=3 take the uniform Boolean family F=(-1)^a on x=0, and F=1-2*1[b=1,z=0] on x=1. Begin with the FULL product reference of the root spectrum, query a, and actually reset both references to their actual products. Every later distinct private z query also exercises the product reset. Adaptive orders and arbitrary stopping are allowed; x,b stay unqueried. Units are bits. One fixed a=1-lineage surplus allocation carries both a prior global debit 1/4 and the first conversion excess; every terminal entropy, influence and current reference KL remains explicit.

This source differs from the canonical completed occupancy M used in the previous run and A036's rare-core result. The change is deliberate: it isolates actual sequential withdrawals and hereditary ownership. No earlier occupancy margin or unchanged-reference approximation is imported into the new account. The original source is never restarted after a reset.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. BOARD.md and B08 STREAM_NOTES.md v2 were read at the start and the board was checked again before drafting. Read own STATUS, LEARNED, WORKLOG and the three substantive saved A037 runs; many later stage folders contain only .final markers and are not mathematical deliverables. Own run 20261014T111143Z REPORT Sections 3-5 identifies the unexercised-debit gap. Own 20261014T043944Z REPORT Sections 1-4 supplies the signed reset and terminal conventions. These identities are reconstructed in PROOF.md rather than assumed from an unreviewed claim.

Read the required campaign README/status/registries/next actions and plan, supplemental campaign/claims/counterexamples/seed/mapping sources, and local source notes. Read both threshold versions and both percolation versions from the supplied text files (these are cp1252, explicitly decoded after UTF-8 failed). Threshold Section 8, Proposition 8.6 supplies context for actual shared-data Fourier mixtures; the percolation singularity statements do not assert general FEI. Neither paper is a logical premise for the present elementary proof. The source hash/encoding receipts are in out/SOURCES_READ.json.

Consumed A036's 20261014T083156Z REPORT Sections 4-6 and 20261021T185858Z REPORT signed-recovery discussion, plus A036/A038/A039 LEARNED.md. Their new all-n statements are context, not proof premises. The available stream lead still names an old k=2 benchmark already completed in the saved 20261014T043944Z run; the productive next gap from own rolling state and board is genuine prior-debit ownership. One two-wording read-only math recall was a WEAK MATCH and supplied no theorem. Session wake warned that personal context was stale; that warning was reported before using notes.

## complete derivation or exact first unsupported line

PROOF.md gives the complete argument. At the a frontier put m=n+2,d=2^(1-m), and H_m=entropy of the m-bit point defect. The two children are p_m and -X p_m. Root product outcome probabilities are fair by x-mask symmetry, and H(F)=2+H_(m-1)/2. Thus the uncovered exercised-conversion excess is exactly

    D_m=h2(d)+H_(m-1)/2-H_m.

It obeys 0<D_m<h2(d)<3/5 for m>=5. At m=4, D_m is negative; the first pilot rejected my proposed n>=2 positive sign. The correction is saved in out/PILOT_CORRECTION.md, and the n=2 case remains a checked boundary. Positive signs at m=5..9 use exact rational log intervals, while the all-m tail follows from the explicit point-spectrum expression and H_m-H_(m-1)/2<8d for m>=10.

At every later active point/twist data query, sigma=O+JS-Gamma. Exact scalar formulas prove sigma_l<=0 for l>=2, with sigma_l<=-2*2^(1-l) for l>=6. The three strict small cases and the exact l=2 equality are certified. The proof uses the positive binary entropy series, explicit coherent outcome mass and Bernoulli's inequality; it does not extrapolate finite checks. Since O+mean TC_child-TC_parent=sigma-E<=0, no additional surplus withdrawal is needed after the first reset.

Every descendant of the INITIAL twisted a=1 child has actual S4>=2 (active twisted point defect, or x character); every other descendant has nonnegative S4. Reserve one global bit from that original lineage, whose reach is 1/2. Carry conditional prior debit 1/2 plus first-conversion debit 2[D_m]_+ unchanged into each descendant. Their total is below 17/10, so at least 3/10 conditional, hence 3/20 global, survives. Both the initial reset and every later reset are actually performed in the checker. A signed saving is not booked as a second source bank.

FIRST UNSUPPORTED UNIVERSAL LINE: supply such a hereditary source-owned eligibility certificate for arbitrary unequal non-flat cores under their ORIGINAL prescribed occupancy reference, or pay its actual first conversion, without renewing a terminal bank. The positive result here concerns one full-product source family. It supplies no all-dimensional FEI constant and no Boolean H/I counterfamily.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json preceded all search. From A037:

    python -X utf8 -B runs/20261021T220645Z-fleet03-A037-conditional-credit-ledger/code/check.py --pilot
    python -X utf8 -B runs/20261021T220645Z-fleet03-A037-conditional-credit-ledger/code/check.py
    python -X utf8 -B runs/20261021T220645Z-fleet03-A037-conditional-credit-ledger/code/audit.py

Pilot: n=2 and scalar dimensions 2..6, 284 exact assertions PASS after the documented sign correction. Final main: n=2..6 actual Boolean truth tables, both a children, all private-data depths, scalar dimensions 2..20; 6491 counted exact/interval assertions PASS in 0.667912s. Integer Walsh spectra, Fraction kernels and physical-edge influence counts check the raw functions. Forty-term positive atanh expansions with rigorous tails and outward 2^-160 rounding certify all signs. Exact powers of two have exact logs. Every terminal H,I,TC/current-reference KL, S4 and old booked debit is saved in out/CHECK.json.

Independent implementation out/AUDIT.json: 18 checks PASS in 0.186046s, using literal character sums, exact prime-log coefficient cancellation and separate sixty-term Fraction log intervals. It imports no main checker or interval helper. The first actual conversion identity and four direct Bayes-to-product reset identities cancel exactly; finite sign bases are reproduced. This is a second implementation by A037, not external independent review. Dropping the unqueried-x hypothesis allows a twisted defect to reach a constant with zero surplus, an explicit scope countercontrol.

One core-Lean target states only the scaled integer budget: bank>=20, first debit<=12 and prior<=5 imply bank>=3+first debit+prior. Fresh memok exited0. The bounded 35-second attempt returned RUNTIME_UNVERIFIED after about36 seconds with no compiler output; no formal target or axiom receipt passed. out/LEAN.json preserves the result and source/compiler hashes. No retry or full Mathlib job was launched. The mathematical entropy result is proved in prose with exact base certificates, not by Lean.

Main memory estimate90MB and audit40MB; measured peak unrecorded. No research job expected above300MB. No GPU, dimension escalation, detached work, git, mail, brain write, shared-tree mutation or deletion. The governor reported normal state; concurrent memory holders were reported and left running. The protocol's older endpoint is superseded by the user's explicit 2026-10-23 14:49 UTC campaign endpoint; no schedule was changed.

## proof dependencies and changed downstream conclusions

The new proof is self-contained finite Fourier/KL/entropy algebra with exact finite base certificates. Existing B08/A039 compensated identities are credited and reconstructed. This is a scoped exercised-transaction application, not another broad universal candidate. Prior generic chain rules and the already completed control/selector benchmark are not repeated as new progress.

A036/A038/A039/A050 can now distinguish actual multiple reference replacements from a single delayed conversion: after the first paid product reset on this family, every further private-data product reset is nonpositive, and the original allocation survives branchwise. Canonical occupancy history and arbitrary-core bank eligibility remain open. No earlier claim is superseded or refuted by this different-source result. Independent review by A088/A094 and shared-index adoption are pending.

## one next mathematical action and independent reviewer

Next: carry the ORIGINAL completed occupancy source through an exercised first reset on a core whose two data children are unequal and nonconstant; pay its next signed conversion from the same remaining ancestor allocation with both terminals. This tests the source change and hereditary eligibility absent here, rather than repeating point-defect entropy bounds. A088/A094 should reconstruct PROOF.md and the finite bases; A039/A050 should audit the prior-charge and full-terminal ownership. No outbound messages were sent.

## actual persistence receipts or precise save blocker

Saved the four protocol files, PROOF.md, self-contained check/audit code, own interval primitives, frozen specifications, exact outputs, failed-pilot correction, core-Lean source and timeout receipt. Rolling STATUS/WORKLOG/LEARNED are updated. out/PERSISTENCE.json checks exact field keys, matching progress/delta, statement hash and artifact hashes/size limits. Local save is verified; supervisor copying, private mirrors, brain ingestion, adoption and independent acceptance remain unobserved.

Universal bridge: This moves C024 history transfer and C019 stopping-tree payment from an unexercised final conversion to a full-product-source history with an actually paid positive first debit and arbitrary later exercised private-data resets, after a genuine quarter-bit prior ledger booking. The same original allocation retains at least 3/20 bit at every frontier; all terminal costs remain. The universal constant improves by zero. The missing bridge is prescribed occupancy-reference conversion and hereditary eligibility for arbitrary unequal non-flat cores. NEXT attacks those exact missing hypotheses in the existing source/history ledger, the shortest route toward universal payment rather than another isolated class FEI bound.
