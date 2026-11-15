---
name: e0066_nonlinear_extreme_two_cycles_and_coefficient_version_control_2026_11_13
status: verified
type: project
created: 2026-11-13
novelty: not_established
import_status: pending_shared_brain_readonly_in_sandbox
---

For E0066, ordinary convergence is false even for a genuinely nonlinear extreme bistochastic QSO in every m>=4. Take W(x)=(1-x1)x+x1*tau(x), where tau swaps coordinates 1 and 2, and V=P W where P exchanges pairs (1,2) and (3,4). Interior even/odd iterates tend to pairwise-equal vectors with the original pair masses, exchanged each step. A trajectory converges iff x1+x2=x3+x4. Extremality follows from rigidity of the fixed output coordinates of W and zero coefficient constraints. The quadratic Lyapunov loss is exactly 2*x1*(1-x1)*(x1-x2)^2. Full proofs, coefficients and rational checks are in this folder's REPORT.md and data/exact_cycles.json. Independent audit passed: data/audit.json.

Every continuous majorisation-decreasing map on a finite-dimensional simplex has each trajectory asymptotic to one finite cycle, hence Cesàro convergence for every continuous observable. This is known mathematics, not a new solution claim; see Saburov 2016, Makhmudov 2021, and the 2016 paper's reference to Shahidi 2009.

Source-version scar: arXiv:0802.1100v1 Cor. 4.3 incorrectly promotes single-output subset conditions to a full higher-dimensional characterisation. The published 2010 paper explicitly distinguishes these conditions after Thm 2.6. A rational four-type tensor satisfies all those single-slice conditions yet violates the r=2 majorisation inequality by 7/400. The tensor is NOT bistochastic. Do not search the entire necessary outer polytope and label all its vertices bistochastic. For m=3 the conditions are exact and the known 222 vertices are reproduced here, each with an independently checked exact active rank 18. The report leaves the full m=4,5 extreme classification unfinished and gives an exact copositivity formulation instead.

Evidence directory: ~/agent_run/E0066A
Verification: python3 code/audit.py; 7,705 numerical trajectories, exact controls, peak main-run RSS about 114 MiB, one thread, no workers. The cited 2016 paper already contains a linear interior two-cycle example. No novelty assertion is justified from this search.
