The ten assigned problems now have 16 self-contained draft results and 41 links, saved in two bundles under ~/math-brain-inbox/w340/. All results await w346. The live store was accessed read-only; admission count is zero until the auditor's KEEP. Current openness remains unverified beyond the cached literature.

The main advances over the recorded attempts are a proof for complex two-site determinantal kernels with fixed diagonals, an exact stationary one-server DelayedOff waiting-power curve including later arrivals, and diagonal Gaussian tensor bounds for every p>=2 using the source's repeated-vector norm. P0276 reconstructs an existing candidate and adds independent finite checks; it is not a priority claim.

| Problem | Saved result and scope | Check |
| --- | --- | --- |
| P0276 | Explicit unweighted Abelian Cayley family: product condition, no cutoff; existing candidate reconstructed | 104 eigenvalues and 12 full-state semigroup cases; maximum spectral error 1.34e-15 |
| C0033 | Fixed-diagonal two-site concavity; finite-to-stationary conditional implication | 5,000 complex segments; no violations; probability mass error <=2.23e-16 |
| C0135 | Correct inverse clock scale and uniform backtracking transfer gate | Six logarithmic clock inversions; cached source explicitly uses a uniform estimate |
| P0109 | Moment-free Laplace criterion for iid geodesics in a known sufficient subrange | Degree-six examples give geometric path ratios 0.76471 and <=0.58243, the latter with infinite mean |
| P0441 | M/M/1 stationary waiting-power curve, state fractions, and busy-period area | 80,000 regenerative cycles; every waiting/power discrepancy below 1.62 standard errors |
| C0045 | Exponential box exit bound for homogeneous positive drift | Five absorption systems; exponential bounds hold |
| C0081 | All-orders compact asymptotics do not locate a critical pole | 100-digit checks at four d values; pole shift 1/d despite exponentially small compact error |
| C0123 | Exact bridge deficit and component count in a deterministic paired-block NK landscape | 17 exhaustive landscapes through 12 bits; all counts match |
| P0012 | Diagonal bounds for all p; correct odd/even polynomial norm identities | 1,440 explicit optimizer checks and 100,000 Gaussian norm samples at r=3 |
| P0038 | Finite-energy corridor gate and stretched binary-tree resistance criterion | Exact rational checks through 64 levels; linear lengths give resistance two, exponential lengths diverge |

Reproduce the measurements with `python -X utf8 check_first_batch.py`, `python -X utf8 check_remaining.py`, and `python -X utf8 check_algebra.py`, from this folder. SymPy reduces the DPP atom-product identity, queue waiting identity and busy-fraction identity to zero exactly. `python -X utf8 validate_deliverables.py` checks both draft schemas, every quoted endpoint against the read-only store, all existing logical targets, and dependency acyclicity. SOURCE_REPORT.json preserves the named old attempts; CACHED_SOURCE_REPORT.json records the precise cached paper clauses and limitations. No web search or test-bank access was used.

`python -X utf8 run_lean.py` was attempted. Both checks were refused before compilation with "Compute status is distressed or unknown". The Lean sources and refusal receipts are retained; three identities were instead verified exactly with SymPy. None of the results is labeled Lean-checked.

Scope is the main risk: the entropy proof fixes both diagonals, the queue has one server and no setup cancellation, the NK model is deterministic with paired blocks, and the tensor bound remains diagonal. The clock and pole examples refute inferences rather than solve the original stochastic problems. The FPP range is weaker than the survey's known subcritical range. P0276 has unbounded degree; its literal printed source has no stated degree restriction, while the cited workshop formulation and priority remain unchecked. Numerical checks support the written proofs and cannot substitute for independent review.

Apply after w346 KEEP on every included entry and full proof/scope review: the reviewer runs `python -X utf8 ~/math-brain-build/tools/integrate_drafts.py --only w340`; filter or revise any FIX/DROP entries first. The requested unified diffs are patches/01_first_research_bundle.diff and patches/02_remaining_research_bundle.diff, with headers naming the exact inbox paths.

AUDIT_STATEMENTS.jsonl is the statement-only blind packet; AUDIT_REQUEST.md explains the checks. Three hook proposals and progress events are staged locally for the reviewer to publish under the worker's write fence. No mesh send or live progress-page write was performed.

NEXT: w346 independently audits the 16 statements and their full proofs; the reviewer ingests only kept results. The next mathematical target is jointly varying diagonals in the two-site entropy conjecture.
