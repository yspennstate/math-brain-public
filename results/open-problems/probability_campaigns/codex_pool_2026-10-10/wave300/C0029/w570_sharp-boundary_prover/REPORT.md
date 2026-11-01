The packet proves four boundary claims as author work: joint projective collision constraints, an exact collision probability, the sharp leading collision atom, and a corank-one counterexample to a two-coordinate witness bridge. It also proposes one correction to the prior Gaussian-law statement. Independent review and served-model evidence are pending; the exact-one parent target is not solved here.

The command `python -X utf8 ~/brain_workers/w570/verify_boundary.py` passed 30 joint-partition checks against original matrices of sizes 1-3, exact collision counts over 66,067 normalized matrices of sizes 1-5, and eight rational-rank counterexample checks of sizes 5-12. It used 0.234 CPU seconds and 0.414 wall seconds after a fresh compute gate. No GPU, model load, process-priority change or live-store write was used.

The incorrect baseline treats the row- and column-collision events as independent. It disagrees with exact enumeration in 4 of 5 sizes; the exact formula disagrees in 0 of 5. This is a correctness repair, not a claimed speed improvement. At n=2 the baseline gives 3/4 and the exact answer is 1/2. The two-sparse collision event is only a subset of singularity.

| n | Normalized matrices | Exact collision probability | Incorrect independence probability |
|---|---:|---:|---:|
| 1 | 1 | 0 | 0 |
| 2 | 2 | 1/2 | 3/4 |
| 3 | 16 | 5/8 | 55/64 |
| 4 | 512 | 169/256 | 54511/65536 |
| 5 | 65536 | 5147/8192 | 50339839/67108864 |

At n=1,t=0.1 the exact Gaussian CDF is 0.079655674554; the limiting law gives 0.099675477414. Calling the limiting law finite-size exact introduces an absolute error 0.020019802860.

Reviewer application: apply patches/01_C0029_gaussian_scope.diff to the single C0029-A001 intake row only after checking its old line, then use STORE_CORRECTION.json to revise the named concept through the normal coordinator integration process. The patch preserves historical author text and adds an explicit correction. Do not apply a raw patch to the sqlite store.

Brain draft: ~/math-brain-inbox/w570/bundle_001.json contains 8 entries and 7 relations. Submitted=true, reviewed=false, ingested=false, retrievable=false. A DRAFT submission is not an ingestion or recall receipt. The coordinator alone integrates after the corresponding proof and model-review gates. The hook proposal C0029-w570-01 is in primary_directive/hooks1000/proposals/math-w570.jsonl.

The remaining risk is the collision-free singular/small-singular-value complement. No estimate of its probability is proved, and the exact-one coefficient at intermediate scales remains the single hardest gap. Current openness and novelty are UNKNOWN. Finite checks do not certify an all-n theorem or a formal proof.

NEXT: w572 independently rederives the joint partition count and inclusion-exclusion formula; then examine a coefficient-one small-ball estimate on the complement of the collision event.
