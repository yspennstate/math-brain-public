# C0052 referee handoff, 2026-10-10

## Target

The primary source is Duminil-Copin, arXiv:1707.00520v1, printed p.94, eqs. (7.1)-(7.2), Conjecture 6. Its operational three-dimensional target is that the signed renormalized coupling g_3(beta) fails to tend to zero as beta increases to beta_c. With U4<=0 this means a nonvanishing subsequence of -g_3; a positive full liminf or a unique non-Gaussian field limit is stronger. The 2021 Annals result proves the separate four-dimensional half. Current three-dimensional openness is UNKNOWN after a bounded check. `SOURCE_STATUS.json` records the exact locator and historical intake row.

## Mathematical verdicts

`REVIEW.jsonl` contains the reproductions and scope restrictions:

| Row | Author claim | Verdict | What it establishes |
|---|---|---|---|
| R1 | w474-L1 | KEEP | Sharp Gaussian-sign residual covariance inequality. |
| R2 | w475 contact-001 | KEEP | Finite weighted repeated-site bound, transitive 12/N case. |
| R3 | w475 current bridge | KEEP | Path counterexample to a uniform reverse sprinkling comparison. |
| R4 | w475 source contact count | KEEP | Exact anchored contact formula and its vanishing source-normalized part. |
| R5 | w475 contact-003 | KEEP | General block 12/sqrt(N) rate and test-function bound. |
| R6 | w475 transitivity boundary | KEEP | Nontransitive locked-component example; N^-1/2 exponent is sharp in its broad class. |
| R7 | w474-L2 | KEEP | Associated sign-Gaussian spin field with Gaussian smeared FDD limit. |
| R8 | w474-C1 | KEEP | Counterexample to a broad auxiliary non-Gaussianity implication. |
| R9 | w474-L3 | KEEP_DEDUP | Independent derivation of R4's contact formula; integrate once. |

The hardest independently rederived step is R7: positive-definite covariance by a Gaussian-kernel mixture, positive association by Gaussian interpolation, cubic residual covariance from R1, three shell-count regimes, and the diagonal cutoff in the Gaussian Riemann sum. R3 was also rederived from current parity and independent bridge runs. No verdict above establishes C0052.

## Own boundary lemma and test

`ATTEMPT.md` proves the exact one-dimensional source-normalized coupling g_1(beta)=(-log tanh beta)(e^(-2beta)-3e^(2beta)), tending to -6 as beta tends to infinity. This is a one-dimensional extension of the source normalization, not a 3D theorem. The w479 independent referee request is in `REVIEW_REQUEST_W479.md`; its review is pending. Under `COMPUTE_GATE.json`, `python -X utf8 verify_1d.py` enumerated periodic rings N=8,12,16 at beta=(log 2)/2. The fourth-cumulant density approached its exact infinite-volume value -22 with absolute errors 0.065215099247, 0.001166635148, and 0.000018863225; see `MEASUREMENTS.txt`. This finite check corroborates the written transfer-matrix proof and is not a formal proof receipt.

## Brain and hook handoff

`~/math-brain-inbox/w476/bundle_001.json` is submitted with two concept entries and two evidence-backed associations: precise source quantifiers and w474's broad-bridge counterexample. Local schema check passed; inbox and local bytes matched (4473 bytes). It is not known to be ingested or retrievable. w475's own inbox bundle holds the contact and current-sprinkling concepts, so this packet does not submit duplicate nodes. Served author/referee identities are unavailable; do not promote a theorem before those gates and validating coordinator review.

`HOOK_PROPOSAL.jsonl` and `patches/01_c0052_hook.diff` prepare one narrow math hook with a fire and a silent control, grounded in R7-R8. The worker write restriction kept the proposal out of the live hooks directory. The progress-page script was likewise not run because it writes outside the worker folder; the specifically requested math-brain inbox was the sole task-specific external draft destination.

## Open proof obligation

Establish a positive subsequential lower bound on the properly normalized distinct-site four-point Ursell/current-intersection mass for nearest-neighbor critical Z^3 Ising. Neither anomalous two-point decay, a nonzero local cumulant, repeated-site contacts, nor a mean intersection count supplies this without a model-specific variance/tail argument. The inherited C0052-A001 second-moment route leaves that argument open.

NEXT: w479 independently audits the one-dimensional lemma; the validating coordinator checks served-model evidence, deduplicates peer concepts and integrates the submitted draft only after its gates. Research then targets the distinct-site lower bound.
