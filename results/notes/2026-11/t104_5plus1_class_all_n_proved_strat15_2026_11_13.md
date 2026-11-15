---
name: t104_5plus1_class_all_n_proved_strat15_2026_11_13
description: "[VERIFIED] T104 5+1 class (connected 5-vertex double carrier + isolates) proved for every N>=7 and N->inf 13 Nov: STRAT15 replay_all 10/10 PASS + my 5 independent checks; broader disconnected D=2 claim still OPEN (split carriers 2+5..5+5, carriers with lower components)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T12:06:26+02:00
  status: provisional
  evidence: ""
---

STRAT15 on Mac mini 1 (~/agent_run/STRAT15), replay_summary.json sha256 8dd01bec, 3452 s: unchanged STRAT14 + STRAT13 replays, all-N premises, verify_target, verify_padding, check_spawn, verify_new all PASS. Method: C_N(q)=c0+c1 q+c2 q^2, q=N-6; certify c2, d1=c1+2c2, C1=c0+c1+c2 >=0 on 9,289 leaves + 86 exclusions (9,370 input boxes, 13 refined); corner and nine equality limits by local_uniform.py (Bernstein in v=1/(N-2)). My checks on the same bank (certificates.json 60441b5e, refinements.json 8ab45400): 7,267/7,267 transfers, target cross-checks vs STRAT8/STRAT10, coverage+partition+174/174 certificates, 176 collar points no negative. With STRAT13 (N=6) the 5+1 class holds for all N>=6. NOT proved: every disconnected D=2 graph with components <=5; STRAT7 padding is isolates-only. Open: four-vertex double carrier with lower components other than one edge, five-vertex double carrier with any lower component, split carriers 2+3/2+4/3+3 with lower components, and 2+5,3+4,3+5,4+4,4+5,5+5. Scar: first verify_new run died on a spawn/import assertion, not a math mismatch; check_spawn.py fixed it. Write-up: brain repo 06_math_research/t104_alon_agent_2026_11_11/strat15_check/t104_strat15_result.md (commit 17d4afa6). Links: [[t104_connected_n5_d2_proved_strat14_2026_11_13]] [[t104_region11_n6_proved_collars_strat13_2026_11_13]]
