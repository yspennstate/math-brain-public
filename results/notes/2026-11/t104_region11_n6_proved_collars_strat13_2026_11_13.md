---
name: t104_region11_n6_proved_collars_strat13_2026_11_13
description: "[VERIFIED] T104 5+1 region (11) at N=6 proved: STRAT10 cover + STRAT11 corner ball + STRAT12 Bernstein + STRAT13 collars at nine infimum-zero limits; exact replay passed, push 139 1d4a76e2"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T09:47:51+02:00
  status: verified
  evidence: "brain repo 06_math_research/t104_alon_agent_2026_11_11; push 139 1d4a76e2 verified 32 of 32"
  supersedes: t104_region11_infimum_zero_at_corner_box_splitting_cannot_close_2026_11_13
---

T104 (Alon Conj. 1.5), 5+1 class, STRAT9 region (11) at N = 6: proved on 13 Nov 2026. T6 > 0 at every feasible connected point,
for a five-vertex connected carrier plus one isolate under the original (11) hypotheses. N >= 7 and larger carriers are still open.

The chain, each step replayed exactly (Fractions or rational Bernstein coefficients, no floats in any proof step):
- STRAT10 cover of the canonical root (40,177 splits): every leaf excluded or positive, except the ones near the corner.
- STRAT11 corner ball: T6 >= ||S-S0||/120 for 0 < ||S-S0|| <= 1/20800. 13,368 boxes left open.
- STRAT12 Bernstein certificates with Farkas multipliers on the STRAT10 constraints: 13,359 closed. Nine left, each containing a
  point of the closure where the connected constraint vanishes (two edges of weight 1/2 with coordinates in Q(sqrt5), or a
  triangle of weights 1/3 with coordinates in Q(sqrt15)). No strict certificate exists on a box that contains such a point.
- STRAT13 collars: a chart h=(x,y,k,p,q,v,z) on the rank-two zero-sum manifold that removes the eigenframe rotation at the repeated
  eigenvalue; active edge weights omega_ij = lambda/5 + S_ij; Farkas multipliers give T >= ||h||_1/6 - M||h||_1^2/2, so
  T >= ||h||_1/12 for ||h||_1 <= 1/384 (edges, M=32) or 1/648 (triangle, M=54); physically T6 >= ||S-S_P||max/24 on balls of
  radius 1/15360 and 1/27864. The rest of the nine boxes is split again: 366 positivity, 216 exclusion, 17 collar leaves.
- Final ledger: 32,925 positive, 20,277 exclusions, 17 collar leaves, 53,218 splits, no open leaf. The radial identity
  T6(a,ar) = (1-t^2) 9/80 + a(1-t) L6 + t^2 T6(E,rE), with L6 >= 3(1+r)/32, carries the endpoint to every inward scale.

Lesson: when the open leaves stop shrinking under splitting, look for an infimum-zero limit in the closure (here, infeasible
points with a disconnected carrier). Splitting cannot close a box that contains one, but a local chart at the limit with Farkas
multipliers on the active constraints gives a linear lower bound, and a collar of that radius closes it. See
[[t104_region11_infimum_zero_at_corner_box_splitting_cannot_close_2026_11_13]].

Audit scar: Codex rebuilt collar_cover.json between my first check and its final replay (211 KB -> 281 KB, 12 -> 17 collar
leaves). My first check had run on the old cover. Before pushing, compare the sha256 of the files a check read with the final
tarball, and rerun the check if they differ. Here the rerun on the final cover passed 425 of 425.

Evidence: brain repo 06_math_research/t104_alon_agent_2026_11_11/ (strat11, strat12, strat13, *_check,
t104_strat11_12_result.md); push 138 d8faceb3 (83 of 83 files verified), push 139 1d4a76e2 (32 of 32). Codex replay_all.py: all
18 stages passed, 1,093 s on Mac mini 1. My checks: strat13_check/my_collar_check.out (425 of 425 on the final cover),
my_chart_stress.out (600 of 600 per type, worst ratio 0.201 and 0.245 against 1/12).

