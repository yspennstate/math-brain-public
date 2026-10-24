Prepared the ten assigned problems as 14 draft nodes and 16 typed relations. All 12 distinct existing logical targets resolve. The results are ready for blind review; KEEP receipts and counted open-problem solutions are both zero.

The main new candidate is P0242: an explicit reversible four-state family, lumped to three states by stationary flows, has optimal stationary-stopping times tending to 2 and 3. Any universal comparison constant must therefore be at least 3/2 if the proof survives review. This extends the earlier finite 1.48220 witness to an exact asymptotic lower bound; it gives no universal upper bound or novelty certificate.

Measurements: `python -X utf8 p0242_family.py` passed 50 symbolic hitting, stationarity, and detailed-balance identities in 2.428 seconds. At parameter 1000 its exact ratio is 24076090051009/16078132074513 = 1.4974432315538901. `python -X utf8 check_results.py` independently matched 200 fundamental-matrix entries, passed 79 exact finite-field nilpotency cases, and passed the checks for all ten problems in 0.587 seconds. `python -X utf8 validate_bundle.py` passed schema, endpoint-quote, dependency-cycle, and existing-target checks. These timings measure computation, not shell startup.

| Problem | Saved result |
|---|---|
| P0189 | Exact nilpotency and strong convergence; cached Brown-measure theorem confirms the candidate mismatch. |
| P0390 | Infinite-volume weighted-covariance criterion for a power saving; finite conservation alone is insufficient. |
| C0100 | Conditional periodic-patch frequency theorem; weak height convergence alone does not determine frequencies. |
| P0031 | Exact square-root sparse-clock threshold, with an almost-sure sufficient condition. |
| P0242 | Candidate lower bound K>=3/2 under stationary-flow lumping. |
| C0011 | Corrected Ray-Knight identity, marginal Chernoff rate, and held/unverified exact-domain status. |
| C0070 | Exact Poisson extinction-duality rate; sharp hypercube conditioning remains unproved here. |
| C0105 | Explicit prime-phase moment-averaging window, with no claim about the zeta remainder. |
| C0153 | Finite-energy obstruction to wiring every fixed boundary vertex with probability tending to one. |
| P0025 | Exact signed boundary-occupation criterion for log separation; its Brownian long-time sign is unproved. |

Lean returned SETUP_UNVERIFIED before starting a compiler because the compute telemetry status was unknown or distressed. No result is labeled Lean-checked. The experiment scripts use synthetic comparison models where stated; they do not settle the corresponding open problems.

Apply: after w347's KEEP and the required full proof checks, the reviewer ingests only the kept entries with the existing draft integrator from ~/math-brain-inbox/w333/bundle_001.json. `patches/01_math_bundle.diff` records this complete draft addition. The worker did not run an integrator or write a store.

Two evidence-backed hook proposals and four fire/silent controls are in `hook_proposals.jsonl`, `evidence/hook_controls.json`, and `patches/02_math_hooks.diff`; they are proposals, with no live fires measured.

The concrete blind request is `AUDITOR_REQUEST.md`. COMMON.md forbids "the agent mesh's send commands", so its id/count/path relay and the required progress event are saved in `AUDITOR_RELAY.json` and `progress_request.json` for a permitted reviewer relay. The directed team inbox was read through a read-only SQLite connection; it had no unread messages.

NEXT: w347 independently audit the 14 entries; the reviewer relays the saved request/progress event and lands only KEEP results.
