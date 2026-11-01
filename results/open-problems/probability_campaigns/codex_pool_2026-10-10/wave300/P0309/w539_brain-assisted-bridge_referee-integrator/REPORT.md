# P0309 referee report, 2026-10-10

The recovered campaign intake asks for a low-positive-temperature crystalline 3D Coulomb or Riesz Gibbs phase but leaves the exponent, ensemble, and order parameter unspecified. Lewin's 2022 review treats 3D BCC/FCC phases as numerical expectations and proves a fluid theorem only in a different small-activity regime. Current openness is **UNKNOWN**.

I independently checked w538's O1-O4 and B1, including negative near-collision curvature, conditional Dirichlet Bragg order, coherent-phase failure, and exponentially rare circular branch. All are KEEP within their exact assumptions. I checked w537 C1-C5, including the full-law Bragg second moment to pressure-slope implication; all are KEEP as conditional or abstract results. Reproductions and gaps are in `CLAIMS.jsonl` and `review/W537_VERDICTS.jsonl`. The single hardest parent gap is a uniform unconditioned Bragg bound, or equivalent subexponential mass for an ordered Fourier event, in an actual 3D Riesz Gibbs law. Pressure existence, local uniform integrability and zero-field Gibbs closure remain additional inputs. No P0309 solution is claimed.

My provisional O2 shows a near-collision relative transverse Hessian contribution `-4s epsilon^(-s-2)+O(1)` for a pair Hamiltonian plus locally smooth terms. This defeats a global Brascamp-Lieb transfer; w542's required independent audit is pending. The primary-source and math-brain hypothesis comparison is in `ATTEMPT.md`.

Measurement: `python -X utf8 ~/.claude/dreaming/brain.py recall "P0309 probability Riesz crystalline proof mistakes"` returned 0/3 directly relevant top hits. I submitted one scoped hook proposal to `~/primary_directive/hooks1000/proposals/brain-w539.jsonl`; no live recall behavior was changed. A local Python JSON/schema check validated 3/3 draft files, 5/5 w537 verdict rows, 3/3 bundle audit rows, and exact byte equality for the submitted inbox copy. `bundle_001.json` and `bundle_002.json` overlap author bundles and are retained only as reviewer copies.

Apply: The validating coordinator may review and ingest the unique source-scope draft at `~/math-brain-inbox/w539/bundle_003.json`; it was written atomically from a `.part` file. Its state is submitted, with review and ingestion pending. Do not ingest the two overlapping local reviewer bundles. `review/BUNDLE_AUDIT.jsonl` records one relation-type FIX and two status-review rows for the author bundles. No live code, math store, or global recall file was edited here.

Apply the relation correction, after the author confirms its bundle version, with `git -C ~ apply --no-index ~/brain_workers/w539/patches/01_w537_relation_type.diff`. The matching `git apply --no-index --check` command returned exit 0; the author bundle itself was not edited by this worker.

The direct team_comm route to the named probability integration contact failed with `not in a team` and then `no such team`. The shared progress page carries the handoff instead. Bundle digests are left to the validating integrator as required by BUNDLE_SPEC.

NEXT: Have w542 check O2; then test the probability cost of any proposed controlled crystalline region under the unrestricted Riesz law, and verify served-model provenance before final proof-review promotion.
