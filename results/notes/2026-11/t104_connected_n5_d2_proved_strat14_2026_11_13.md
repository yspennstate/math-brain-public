---
name: t104_connected_n5_d2_proved_strat14_2026_11_13
description: "T104 connected five-vertex graphs at D=2 proved 13 Nov (Codex STRAT14 + my exact checks): STRAT8 residual closed by porting the STRAT11-13 chain; push 141 3dae1e7d"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T10:37:30+02:00
  status: verified
  evidence: "06_math_research/t104_alon_agent_2026_11_11/t104_strat14_result.md"
---

T104 (Alon Conj. 1.5), connected five-vertex graphs at D = 2: proved on 13 Nov 2026. T >= 0 for every connected
five-vertex weighted graph whose top Laplacian eigenvalue has multiplicity exactly 2. Still open in T104: the 5+1 class
for N >= 7, and connected carriers with n >= 6.

How it closed (Codex STRAT14 on Mac mini 1, 34 minutes from launch to a passing replay):
- The n = 5 target is the STRAT10 all-N polynomial at N = 5: C_N(-1) = 2 Cface. N = 6 positivity gives no sign for
  N = 5, so certificates were recomputed against Cface, but every tool transferred: the STRAT8 chart and constraints,
  Bernstein + Farkas certificates (STRAT12), and the STRAT13 collar chart at the two disconnected equality types.
- Collars: edges T5 >= ||h||_1/20 on ||h||_1 <= 1/520, triangle T5 >= ||h||_1/12 on ||h||_1 <= 1/600; nine zero
  witnesses (Q(sqrt5), Q(sqrt15)) in STRAT8 OPEN leaves 12437 12643 13871 14683 14814 17328 17952 18124 18548.
- 5,272 STRAT8 OPEN leaves -> 8,227 positivity, 3,729 exclusion, 14 collar leaves, depth <= 73, 0 OPEN.
  Global ledger 32,929 pos / 13,937 excl / 14 collars / 46,879 splits, volume 1152. replay_all.py 17/17 PASS, 606 s.

Lesson (method reuse): once a chain (cover -> Bernstein/Farkas -> collars at infimum-zero limits) closed one stratum,
porting it to a sibling stratum on the same chart took one Codex run, because the obstruction points were again the
disconnected equality limits. Before attacking a new residual, ask which finished chain shares its chart and its
equality types; see [[t104_region11_n6_proved_collars_strat13_2026_11_13]] and
[[t104_region11_infimum_zero_at_corner_box_splitting_cannot_close_2026_11_13]].

Check point that mattered: a new premise (scale14, a > 103/200) is only valid as the complement of a region proved
elsewhere (STRAT6), and only where its guard 103D - 200tau >= 0 holds on the whole box. Read every constraint a
certificate uses against the prior stratum's necessary() before trusting the certificate count.

Evidence: brain repo 06_math_research/t104_alon_agent_2026_11_11/ (strat14/, strat14_check/,
t104_strat14_result.md), push 141 3dae1e7d (43 of 43 verified). Tarball sha 6c8af48a...f9d7 on both machines.
My checks: target and all 25 constraints equal STRAT8's formulas exactly; 5,272/5,272 partitions exact; 140/140
sampled Bernstein leaves (20 deepest included); collars sampled, 239 feasible points all positive (corroboration, not
a replacement for verify_local.py).

