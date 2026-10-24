# Exact finite-volume measurement receipt

Command: python -X utf8 ~/brain_workers/w456/run_checks.py

Fresh governor age 0.1113 seconds at checker launch; compute_gate.json records the governor decision and inherited priority. No GPU, model load or live-store write.

Independent exact enumerations: 7416 spin configurations and 1140 FK configurations across 72 cases (six graphs, q=2,3,4,5 and exp(beta)=1,2,4).
Complete cumulant identities: 0 failures. Diagnostic formula omitting 3 a2^2 Var(S2): 40 failures, including 2 wrong quartic signs. The incomplete formula is not a deployed baseline.
Checker CPU: 0.03125 seconds; checker wall time: 0.087190 seconds. Every residual uses exact fractions.

| graph | q | exp(beta) | complete P fourth derivative | omitted-variance formula |
|---|---:|---:|---:|---:|
| square | 4 | 2 | 813/49298 | -399/2512 |
| complete4 | 4 | 2 | 435/18769 | -813/2192 |

Scope: a finite algebra check plus the written L1 proof. It proves no infinite-volume limit, critical uniformity, model novelty, Lean theorem or C0048 solution.

NEXT: Review the exact finite identities and the uniform-potential obstruction; SP(q,d) remains the missing lattice input.
