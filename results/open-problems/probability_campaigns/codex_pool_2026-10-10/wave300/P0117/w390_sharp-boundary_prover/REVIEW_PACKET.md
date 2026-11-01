# Review requested from w392

The deliverable is a quantitative **special case**, not a proof of all P0117 bigeodesics. Exact author claims are saved individually in CLAIMS.jsonl; PROOF.md contains the complete argument. Current openness and novelty are UNKNOWN, because a recent primary manuscript claims the full standard moment version. SOURCE_STATUS.json and reports/PRIOR_ATTEMPT_DIGEST.md separate this claim from verified source scope.

The result: for finite nonconstant iid nonnegative weights on ambient Z^2, choose 0<=l<h with positive low and high masses, K=1+4l/(h-l), and C=2K log(1/p_h)+(K+4)log(1/p_l). No geodesic ray can eventually stay in a deterministic tube of width w(n) with limsup w(n)/sqrt(log n)<1/sqrt(C). A countable rational-coefficient argument gives the simultaneous ray lower bound. A constant iid law is the necessary-assumption counterexample for fixed strips.

Please audit these exact obligations:

1. Every strip-confined crossing must pay for each vertical cut, even for a nonmonotone path. The bypass has at most m+4w+2 cheap edges and is strictly cheaper.
2. The event probability multiplies distinct iid edges. Spacing m+1 separates both connector columns. The proof conditions on no selected path.
3. The dyadic no-trap probabilities are summable under the strict coefficient threshold. Independence across annuli is not asserted or required.
4. Eventual confinement and injectivity force the ray toward one horizontal infinity. The chosen crossing subpath stays within the slab; it cannot hide a wide excursion.
5. The final countable intersection excludes all rays simultaneously for all integer centers. It does not take an uncountable union of null exceptional-direction events.

The hardest remaining gap is explicit: an unrestricted bigeodesic can wander outside every tube this proof covers. There is no bridge closing that gap. The nonconstant atomic extension is local to tube exclusion and makes no assertion about all atomic-law bigeodesics.

Finite checks: **NOT RUN**. A fresh resource gate reported distress and 87.4% CPU. The saved executable `resource_checked_geometry.py` will run the small exact checker only after a permitted fresh gate and records the result. Its prospective endpoint/control cases are not pass receipts. There is no formal-check receipt or admitted placeholder.

Closing update: the second fresh gate at 05:12:41 UTC also denied the checker (distress, 88.0% CPU). Preserve both receipts, geometry_gate_initial.json and geometry_gate.json. The mathematical proof remains an author proof requiring your independent audit.

The six-entry, seven-relation DRAFT was submitted at 04:58:20 UTC to ~/math-brain-inbox/w390/bundle_001.json. The identical local copy is bundles/bundle_001.json; SUBMISSION_STATUS.json records its state. The source license is owner-own-work; all five mathematical entries remain labeled author-proved and pending independent review. Artifact structure passed with resolved relation ends and no dependency cycle; this is not a mathematical verdict. Submitted/reviewed/ingested/retrievable are separate flags.

Statement-only packet was sent to w391 before this proof packet, receipt msg-359aec8887. The adversary was instructed to attempt independently. A review by w392 is requested; no independent keep is claimed. New results introduced by w392 require w395's independent review.

The review request was delivered to w392 at 05:02:43 UTC, receipt msg-7f406ee054. The final mesh peek was blocked by a busy database; no independent verdict has been retrieved. Both submission leases have been released. STATUS.md is NEEDS_REVIEW.

NEXT: Return a verdict for w390-L1, L2, T3, C4 and boundary-5, naming any exact failed assumption or proof step; do not promote the unrestricted P0117 target.

Coordinator relay: reports/PROGRESS_EVENT.json contains the one-line progress command staged under the worker's folder boundary, and patches/02_math_hooks_w390.diff stages two evidence-based hooks. These are separate from the mathematical review.
