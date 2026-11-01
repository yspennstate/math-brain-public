Prepared ten checked problem reports, 20 typed draft nodes, 34 edges quoting both ends, and two hook proposals. Blind audit is PENDING with w347. No open-problem solution is promoted.

The main measured change replaces the cached P0209 numerical check with exact algebra and an analytic normal-distance bound. An unchanged local copy produced four Monte Carlo estimates using 80,000 paths and a Gaussian substitute for the fast chain. The replacement uses zero random paths, verifies six scales exactly, and gives a bound evaluated as 0.49974999995 at t=10,000. Two additional boundary cases s=2,3 pass. The original proof already had the correct rare-event argument; the later memory explanation needed a variance-versus-probability-limit correction. The initial apparent ranking conflict is explicitly superseded in results.jsonl.

| Problem | Saved result and limit of scope | Measurement |
|---|---|---|
| P0209 | Candidate negative answer with rational parameters; uniform-integrability correction | Six exact scales, two boundary cases |
| P0459 | Actual-mean deficit and sufficient simultaneous concentration | 78 exact pairs; 720 edge orders |
| C0130 | Finite-interval escape upper bounds; whole-half-line state correction | Seven intervals; 0.8 to 0.662156 |
| P0088 | Marked birth coupling and conditional exploration bound | 25 vectors; count distance 0 versus marked 1/2 |
| P0336 | Opposite vanishing tilts select different plans | 720 matchings; 36 primary versus one per tilt |
| C0022 | Summable separator criterion; moments alone do not prove singularity | Exact third-moment gap 1/4 with equivalent laws |
| C0076 | Necessary exponent and explicit tightness obstruction | Six scales retain height-one oscillations |
| C0117 | Complete-graph variance and tails with clock convention explicit | 200 exact harmonic cases; 800 cumulant checks |
| P0009 | Added mirror opens a periodic orbit; iid conjecture remains unresolved | Period 12 to a certified unbounded ray |
| P0035 | Exact speed on products of regular trees | 28 bias cases; 296 root patterns |

Reproduce the principal comparison with `python -X utf8 benchmark_p0209.py`; validate the handoff with `python -X utf8 validate_handoff.py`. Each problem's `*_check.py` command is recorded in measurements/. All ten check runs passed. Validation passed all 34 quote matches, dependency acyclicity, schema checks, and two fire plus two silent hook controls.

Risks: author proofs still need blind review; current literature status and novelty were not verified beyond the cached papers. Floating-point evaluations of analytic expressions are not interval-arithmetic certificates. Lean admission returned "Compute status is distressed or unknown", so no Lean certification is claimed. The observed full-process times were 5.16 seconds for the baseline and 7.59 seconds for the replacement; this is a verification-quality comparison, not a speedup or deployed-recall claim.

Apply: after the required KEEP and full proof check, copy `bundles/bundle_001.json` to `~/math-brain-inbox/w337/bundle_001.json`; `patches/01_ten_problem_bundle.diff` names that live target. `patches/02_math_hook_proposals.diff` prepares the two proposals for the usual pair audit. The manager routes `AUDIT_REQUEST_w347.json` and posts `PROGRESS_PENDING.jsonl` on landing. The worker brief's "Write ONLY inside it" and prohibition on mesh send commands are why this handoff remains local for reviewer deployment.

NEXT: w347 blind-audits the 20 entries and 34 edges; claude-4a88bc43 applies only kept material after the full P0209 proof check.
