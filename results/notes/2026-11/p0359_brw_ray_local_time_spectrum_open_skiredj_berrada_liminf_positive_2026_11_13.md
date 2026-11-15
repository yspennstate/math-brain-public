---
name: p0359_brw_ray_local_time_spectrum_open_skiredj_berrada_liminf_positive_2026_11_13
description: "P0359 (Aidekon-Hu-Shi arXiv 2409.01048 Open Question 3: Hausdorff dimension of rays with limsup/liminf N_ray^n/n^2 = a in a branching random walk) is open on 13 Nov 2026 - no paper computes any dimension. New nearby result: Skiredj-Berrada arXiv 2610.33897 (24 Oct 2026) answer AHS Open Question 1(ii): under the skip-free Thm 1.6(ii) hypotheses some ray has liminf N^k/k^2 >= kappa t/theta > 0 a.s. on survival, the optimal liminf constant L is deterministic, L <= t/(2 theta) (AHS), exact L open; for steps in {-1,0,1} a lower constant 4t/(sigma^2 j_{1,1}^2). So the liminf level set is nonempty for small a, empty for a > t/(2 theta); dimension unknown everywhere"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T16:02:43.945Z
---

P0359, rank 39 on the 200 list. Source: Aidekon, Hu and Shi, "Boundedness of discounted tree sums", arXiv
2409.01048, Open Question 3 (PDF pp.4-5). Under the hypotheses of their Theorem 1.6(ii) (quadratic growth of ray local
times), determine the Hausdorff dimension, in the generation ultrametric, of the rays with
limsup N_ray^n / n^2 = a, and of the rays with liminf N_ray^n / n^2 = a.

Status 13 Nov 2026: open. No paper found computes any dimension for these sets.
- Known:
  - Upper end. AHS Theorem 1.6(ii) gives limsup <= t/(2 theta) simultaneously for every ray, so every level set with
    a > t/(2 theta) is empty. Our first pass P0359-A001 (7 Sep, codex_20h) records the same point.
  - Liminf, new, by an outside group: Skiredj and Berrada, "Persistent occupation and critical marked sums on branching
    random walks", arXiv 2610.33897 (24 Oct 2026), the positivity theorem stated just before Proposition 2.2 (p.6), and Proposition 2.2.
    - Setting: the AHS Theorem 1.6(ii) hypotheses, with centred integer steps bounded above by 1.
    - Result: almost surely on survival some ray has liminf N^k / k^2 >= kappa t/theta, with kappa a universal
      constant. This answers AHS Open Question 1(ii).
    - The optimal constant L is deterministic on survival, and 0 < L <= t/(2 theta).
    - For steps in {-1,0,1}, Theorem 2.5 constructs one ray with lower constant 4t/(sigma^2 j_{1,1}^2) from an
      optimized profile energy quotient.
    - Still open in their paper: the exact L, and a general converse at negative drift.
  - Discounted sums by generic chaining: Zhang, arXiv 2602.18919 (Feb 2026). It extends the AHS boundedness result and
    does not touch local times or dimensions.
- Searches, 13 Nov:
  - arXiv: "discounted tree sum(s)", Aidekon's tree papers, "discounted branching random walk", and "branching random
    walk" + "local time" + "ray".
  - Full text of 2610.33897, all 46 pages, for "Hausdorff", "dimension" and "Question 3". The only hits for
    "dimension" are "one-dimensional ODE".
  - Full text of 2602.18919 for "Hausdorff" and "local time".
- What is missing for the spectrum (A001's obstruction still stands):
  - an upper cover estimate that turns local-time levels into generation depths;
  - a Frostman measure on rays that keep a prescribed quadratic occupation.
  The Skiredj-Berrada corridor construction builds one ray. A natural next step is to make it branch at a controlled
  rate, which would give a lower bound on the dimension of {liminf >= a} for a below their constant.

Related: [[p0343_beta_splitting_leaf_correlation_ours_posted_no_overlap_lit_check_2026_11_13]] (previous item in this
loop).
