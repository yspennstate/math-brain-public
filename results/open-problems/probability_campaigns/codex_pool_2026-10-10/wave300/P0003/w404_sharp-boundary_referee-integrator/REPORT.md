# w404 P0003 referee report — 2026-10-10

## Found

P0003 is [Grimmett Question 2.2](https://arxiv.org/pdf/2205.07318): a uniform fixed-length honeycomb SAW from the origin, with a free endpoint, suitably rescaled toward SLE(8/3). The question leaves the scale and precise curve-law setup unspecified. The critical-fugacity boundary-to-boundary [chordal conjecture](https://arxiv.org/html/1206.2092) is related but not proved equivalent. The dated `attempted_un` label is historical; current openness remains UNKNOWN after the bounded checks recorded in `SOURCE_STATUS.json`.

The existing C0096 math-brain card mislabels the critical n=1 O(n) interface as site percolation. Its [cited primary source](https://arxiv.org/html/1206.2092) says n=1, z=1/sqrt(3) is the Ising case with a proved SLE(3) interface limit. `CORRECTION_REQUEST.md` gives the exact old and corrected text.

## Reviewed mathematics

- **KEEP:** w402's exact boundary-flux compatibility, cycle-kernel dimension, six-edge mode, bounded-field noncompactness, and minimal face-constraint argument, only for abstract complex midpoint fields. Its six-card draft and seven relations are scoped correctly. Review reproductions are in `REVIEW_PACKET.md` and `CLAIMS.jsonl`.
- **KEEP geometry / FIX initial target attribution:** w403's seven-route honeycomb paths converge to a nonsimple macroscopic loop. I independently derived the all-N bound 4/N and checked its exact weak-convergence near-return criterion. Its later `ATTEMPT.md` has the correct Grimmett scope. Its four-card concept draft and relations are supportable at draft scope.
- **KEEP abstract diagnostic:** w401's generating-function example has A(z)/C(z) tending to 1 on the real axis while coefficient ratios oscillate. It says nothing about actual SAW coefficients.
- **Author result awaiting w407:** `P0003-W404-COUNTER-01` shows domain Markov behavior alone can have a deterministic limit after adding edge-dependent factors. It refutes only that stronger auxiliary bridge and was not bundled as a theorem.

## Measured checks

`python -X utf8 ~/brain_workers/w404/verify_pinch.py` checked N=8,16,32,64,128 with exact rational edge/coordinate tests: **5/5 cases, 5,401 vertices**, all passed in **0.191 s**. At N=128 the measured uniform error was **0.02768**, below w403's 5/N bound **0.03906**. The all-N result comes from the independent proof in `REVIEW_PACKET.md`, not from these five checks.

`python -X utf8 ~/brain_workers/w404/validate_bundle.py bundle_002.json` passed JSON and structural validation: **1 entry, 2 supported relations, 9 JSONL claim rows**. The active inbox draft is `~/math-brain-inbox/w404/bundle_002.json`; the overlapping earlier draft is preserved as `bundle_001.superseded` and is ignored by the integrator. A narrow source-scope hook was submitted at `~/primary_directive/hooks1000/proposals/math-w404.jsonl`. A progress row was logged through `pd_progress.py`.

## Apply and limits

Apply: the coordinator should audit the C0096 source correction in `bundle_002.json`, supersede the erroneous existing card, run the approved draft integrator, and separately confirm ingestion and retrieval. The w402 and w403 bundles are canonical for their own reviewed results; skip the overlapping w404 superseded draft. No live store or recall control was edited here.

Neither accepted auxiliary result proves P0003. The hard gap remains quantitative control of the actual fixed-length SAW law: scale/tightness, macroscopic near-returns, coefficient or ensemble transfer, and SLE identification. Current openness and served-model/account provenance have not been certified by this packet. `BUNDLE_STATE.json` records submitted, reviewed, ingested, and retrievable separately.

NEXT: w407 audits `P0003-W404-COUNTER-01`; the coordinator reviews the C0096 correction and integrates only scoped drafts, then checks retrieval.
