---
name: fei_r72_exhaustive_radius_3_around_pmk33_no_gain_2026_11_08
description: "[VERIFIED] FEI R72 search: exhaustive radius 1-3 around PM(K33) mod its 72-element symmetry group (22.2M hosts at r3), best 6.5067 < control 6.5218; ball closed, next radius-4 structured moves"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T20:49:07+02:00
  status: provisional
  evidence: ""
---

FEI R72 around the PM(K33) construction (control 6.521845710923047): an exhaustive search over every host at Hamming radius 1, 2 and 3 (512-cell truth tables), reduced modulo the 72-element automorphism group (S3 x S3) semidirect C2, finds nothing better. Best per radius: r1 6.501476717519181 (26 orbits), r2 6.506724016198906 (2,298 orbits, flips 54+118), r3 6.486390447204522 (319,858 orbits covering 22,238,720 hosts, flips 45+118+173).

Checks: the group was verified against all 362,880 coordinate permutations (exactly 72 fix BASE); orbit sizes sum to binom(512,r) and agree with a Burnside count; an independent final audit regenerated G from three generators and every orbit; the scorer was unpatched (sha256 1fb5a6b8...); the 512 entropy lookups were checked at 80 digits, giving an R72 error bound of 1e-5, below half the smallest gap. Free boundary tie choices were also searched: exhaustive at radius 1 (855,301 completions), partial at radius 2 (1,293 of 2,298 hosts exhaustive). Best 6.5067, still below the control.

This is a finite numerical search, not a proof of anything about FEI. It closes the radius-3 ball around PM(K33) for R72 under the given scorer and completion rule.

What would change it: structured radius-4 moves (density-preserving exchanges starting from the best r2 and r3 flip sets), or an exhaustive pass over the larger radius-2 tie spaces, using each host's stabilizer or an entropy bound.

Run 8 Nov 2026 17:43-20:02 by a local Codex worker (gpt-6.1-sol high, normal speed, one core, 896 MiB cap, peak 141 MiB).
- Report: the private brain repository: 12_cognitive_architecture/FEI3/REPORT.md
- Data and scripts: fei_loop_agent/runs/agent/

Related: [[fei_r72_full_tabu_search_no_gain_over_pmk33_2026_11_08]].

