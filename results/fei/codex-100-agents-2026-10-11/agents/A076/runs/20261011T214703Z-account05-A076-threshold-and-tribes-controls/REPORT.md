# A076 / B16: threshold and tribes control ledger

## exact target, quantifiers, hypotheses and units

For finite uniform Boolean signs derive exact threshold, tribes and disjoint threshold-composition spectra, including every physical input in influence. Entropy is Shannon entropy in bits. The packet is locally complete with author proofs; full FEI remains OPEN and independent acceptance is pending.

The current intake actually tested is A046-1, `B09-BIASED-BLOCK-UNCERTAINTY@1`, with P_A=M_A+Delta_A. A is one entire tribe and original inputs are uniform, so Delta_A=0. Definitions are reused; the pending helper itself is not assumed.

## sources actually read, revisions and theorem locators

The execution protocol revision is 2026-10-11-execution-v2. The campaign README/status, registries, packet status, stream next actions, A076 assignment, relevant plan sections, earlier B05/B09/B19 reports and supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING were consulted. The board snapshot is 2026-10-11 21:45 UTC; no earlier A076 result appears. B16 STREAM_NOTES.md was absent at start and recheck; no B16 lead report was available.

The current 38-page threshold text, Proposition 7.1 (67)-(70) and Corollary 7.8, was read for the exact composition interface. Introductions and selected theorem sections of all four supplied paper texts were consulted; older abstracts identify superseded versions. Percolation Theorems 1.1-1.6 are background only. Full-paper review and acceptance are not claimed. Three relevant supplemental source notes were read in full. Exact file hashes/read scopes are in SOURCE_MANIFEST.json. A046's complete frozen intake was consumed when it became available during this stage.

## complete derivation or exact first unsupported line

STRUCTURED_CONTROLS.tex is the complete derivation. Equations (1)-(4) give all symmetric-threshold coefficients and odd-majority closed forms. Equations (5)-(10) give exact tribes multiplicities, degree PGF, influence and entropy. Equations (11)-(12) give explicit all-large-w error bounds, yielding H/I->4. Equations (18)-(23) reconstruct balanced disjoint substitution and recursive/mixed majority controls without assuming a biased weighted-threshold theorem.

The new live-candidate substitution is (24)-(29): the full-tribe conditional spectrum yields the exact M_A. Physical restriction is constant with probability q and leaves t-1 tribes otherwise, giving exact L_A and J_A. For t=floor(lambda*2^w), unbalanced lambda!=ln2 gives M_A/I_A->4,J_A/I_A->0,L_A/I_A->4. At lambda=ln2 the three limits are 3,1,4. This forces K>=4 in any universal whole-block M_A<=K I_A or L_A<=K I_A, without establishing that such a finite K exists. The empty residual fiber is exceptional at balance and is treated separately rather than taking a nonuniform limit through lambda=ln2.

Independent marginal coding costs M/I~w for tribes and ~ell for recursive majority, although H/I->4. Spectral-size entropy is only O(log w) or O(ell), so H(S conditional on |S|) retains asymptotically the whole entropy. These are explicitly scoped payment obstructions, not a conjecture disproof. The first still unsupported universal line is a dimension-free, nonreusing payment of actual conditional block cost plus terminal entropy for arbitrary Boolean functions; this run does not assert it.

## executed validation with domain, arithmetic, commands and outputs

Before each validation extension, out/FROZEN_SPEC.json and out/BLOCK_VALIDATION_SPEC.json froze the helpers, domains, counts, arithmetic, symmetry, memory estimate and <=60-second runtime. Command:

`python -X utf8 runs\20261011T214703Z-account05-A076-threshold-and-tribes-controls\code\check_controls.py`

The final execution checks 81 actual truth tables: 63 symmetric thresholds (n=1..9, every r=0..n+1), 15 tribes (w,t=1..4,wt<=12), recursive majority3 depths 1 and 2, and majority3-of-majority5 on 15 bits. Integer FWHT and Fraction coefficients independently check every predicted coefficient, Parseval, spectral versus physical-edge influence, closed odd-majority coefficients, active-block multiplicities and all conditional Fourier fibers for the first tribe. Exact recursive-majority entropy is checked using powers-of-two denominators.

Result: **62798 exact assertions passed**, observed helper runtime **1.561 seconds**. Floating entropy/channel values are diagnostics, not sign certificates; all infinite-family statements use the analytic bounds in the derivation. The estimate was 30 MB; no >300 MB/heavy job or dimension escalation was used. This is author validation in a different representation, not external independent review.

## proof dependencies and changed downstream conclusions

The spectra are derived directly from Walsh expansion, pivotal counting and elementary probability. Claim A076-TRIBES-PAYMENT-DISCRIMINATION@1 depends on A076-STRUCTURED-SPECTRA@1. A046/B09 contributes definitions only, so rejection of the pending B09 upper bound would not invalidate the derived M_A,J_A,L_A formulas. No upstream unproved inequality is used.

A046 receives an explicit whole-tribe constant obstruction K>=4 and the balanced channel signature (3,1,4). A015 receives an exact ledger showing how whole-set entropy differs from independent-coordinate descriptions. These are handoff recommendations: downstream use has not been observed. Two complete author-proved claims are left for review, respecting the stream's unreviewed-claim cap.

## one next mathematical action and independent reviewer

A092 should independently reconstruct (24)-(29), concentrating on the empty-residual fiber at lambda=ln2; A088 is the alternate reviewer. A046 can substitute these formulas when freezing a nonreusing whole-block payment. Review and subsequent adoption are separate from local artifact completion.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=[A076], STRUCTURED_CONTROLS.tex, CONTROL_DISCRIMINATION.json, SOURCE_MANIFEST.json, both frozen specs, code and validation output are saved in this assigned run folder. STATUS.md, WORKLOG.md and LEARNED.md are updated only in A076. out/PERSISTENCE_RECEIPTS.json records readback hashes. No git operation, external message, shared-ledger mutation, supervisor upload or mirror receipt is claimed. All files are below 20 MB.
