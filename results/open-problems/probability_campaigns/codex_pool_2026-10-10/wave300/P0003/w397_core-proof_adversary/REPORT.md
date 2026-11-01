# w397 P0003 review packet

The exact source asks about uniform n-step honeycomb walks from the origin. I recovered Grimmett Question2.2 and corrected the paired packet's initial substitution of a critical chordal ensemble. w396 adopted the correction and now preserves exact remaining length. Current openness is UNKNOWN; this work makes no novelty or solution claim.

I saved an independent finite obstruction before reading the paired proof. A field supported on one interior hexagon satisfies the local vertex identity with zero boundary values, yet has magnitude1 and adjacent jumps1 at arbitrarily small mesh. w398 independently rederived it and issued KEEP. This makes the source's missing compactness premise explicit; it does not show failure of the true SAW observable.

Before/after measurement: the zero field and the nonzero face field have the same zero boundary data and exactly zero vertex residuals. The new field has adjacent jump1 even at mesh2^(-40), and its six-edge system has rank5/nullity1. The exact rational check passed96 configurations,576 vertex equations, and96 deliberately broken controls in0.185523s. Command:

```powershell
python -X utf8 ~/brain_workers/w397/verify_circulation.py --output ~/brain_workers/w397/MEASUREMENTS.json --gate ~/brain_workers/w397/COMPUTE_GATE.json
```

That gate is consumed. A repeat needs a fresh gate with the same limits and any current capacity approval; no further numerical enumeration was run. The result is a finite arithmetic receipt, not a formal theorem receipt or a measured live-recall improvement.

The complete paired-proof audit is REVIEW_w396_proof.md. KEEP: finite deletion/continuation identities, exact-length extension, maximal collar inequality, total variation bound, clearance-based conditional weak-limit bridge under(C), and first-entrance counting injection(U). The attempted collar input H_disk is unproved; it is not established as the single hardest lemma of the whole conjecture. Full identification from length-resolved kernels, H_len, is also unproved. Ordered-curve tightness and continuum conventions remain open; H_5/8 is a separate unproved chordal input. w398 independently kept the boundary-attached tangency example. The relative-normalization boundary case remains draft pending its independent check.

Submitted: two DRAFT bundles,9 entries and6 relations, under ~/math-brain-inbox/w397. The only lemma entry is the w398-kept finite circulation result; the other cards remain definitions/concepts in a draft submission. w398 also recorded KEEP for the paired finite/conditional lemmas and its corrected fixed-length count bound. SUBMISSION_RECEIPT.json records submission, partial review, ingestion and retrievability separately. Ingestion and retrievability are not claimed.

For the reviewer: audit the remaining rows and integrate only the accepted drafts through the validating coordinator. To apply the hook proposal, append the checked line in hook_proposals/math-w397.jsonl to ~/primary_directive/hooks1000/proposals/math-w397.jsonl; patches/01_p0003_circulation_hook.diff is the equivalent unified diff relative to ~. The hook has explicit fire/silent cases and measurement evidence. The global proposal and progress-page writes were staged locally under the worker-only write restriction; PROGRESS_EVENT.txt is the one-line event to post. No live store or global recall-control change was made.

NEXT: Referee-check the relative-error example and remaining draft relations, then bound the mutually avoiding length-resolved counts in(U) for H_disk while keeping H_len explicit.
