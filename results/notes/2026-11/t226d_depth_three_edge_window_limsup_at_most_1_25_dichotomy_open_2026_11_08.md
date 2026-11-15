---
name: t226d_depth_three_edge_window_limsup_at_most_1_25_dichotomy_open_2026_11_08
description: "Partly (8 Nov): at depth three the boundary-Gaussian edge-window convergence probability has limsup <= 1/25 by an exact interval cover, not yet 0; the mixed-region survivor set is the gap (OPEN-T226d, T226)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:03:03+04:00
  status: verified
  evidence: "~/brain/online/frontier_rows/T226/open_t226d_agent_11_08/REPORT.md"
  originSessionId: 81695323-627a-4240-9df2-cd66cd18fae9
---

Does depth three keep depth two's answer (edge-window convergence probability tends to 0) at the boundary Gaussian scale? Partly (8 Nov, Codex OPEN-T226d, row T226): it is proved to be at most 1/25, not 0.

The model is GD on (u1 u2 u3 - 1)^2/2 from N(0, eta^-1/2) starts. Starts that reach B (every pairwise product of squares below 2) converge with subcritical sharpness, 0 < eta lambda < 2. Starts that reach H (every product above 2) escape. An exact interval cover bounds what is left at 0.0394982 < 1/25.

My check (t226d_check.py):
- The certificate sum and the 1/25 inequality hold in exact rationals.
- A fresh 40,000-start run gives B 0.8637 and H 0.1363, none unclassified (depth two had 1 - e^-2 = 0.8647 converging).
- Every B start ends with q at most 1.980.

What is missing for limit 0 is a proof that orbits avoiding both B and H have Gaussian measure zero. The simulation suggests they do; finer covers can shrink the bound but never prove 0. The depth-two invariant circle has no direct analogue (q = 6 fails both ways).

Files: ~/brain/online/frontier_rows/T226/open_t226d_agent_11_08 (PROOF.md, AUDIT.md, cover.cpp, certificate.py). Pushed 7e6b95da0e; the compiled cover binary was left out of the upload. Card in the math store.

Related: [[t226_depth_two_boundary_gaussian_edge_window_limit_is_0_t226c_2026_11_08]] is the depth-two result this extends.

