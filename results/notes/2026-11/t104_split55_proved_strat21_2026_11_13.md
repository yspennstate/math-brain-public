---
name: t104_split55_proved_strat21_2026_11_13
description: "[VERIFIED] T104 split 5+5 proved with arbitrary lower components, every N>=10 (STRAT21, push 156): closes disconnected D=2 with components of at most five vertices"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T19:51:21+02:00
  status: provisional
  evidence: ""
---

T104 (Alon Conj 1.5, Oliveira reduction): the disconnected D=2 split 5+5 - two connected five-vertex top carriers - has T>=0 for every N>=10 and N->infinity, with isolates or arbitrary lower components; both connected gives T>0; equality only at two equal edges plus isolates in the selected-projector closure; positive lower trace strict. With STRAT15's full-cover theorem kept as a premise this closes disconnected D=2 when every component has at most five vertices. Codex STRAT21 (mini1, exit 0 13 Nov 21:10 Mac, gpt-6.1-sol high, normal speed). How: R5 and tree-vs-rank<=3 pairs transferred from the edge+five theorem at k=5 to k=8 (second five-part fixed, trace-square and Y terms cancel), extra T*>=1/100; the rank-three zero-edge endpoint Z5 by a matrix SOS (Gram entries integer/8e10), F25>=1/5; last pair T*>=11/50 at k=8; lowers with trace cap k-9 from k=10. My audit: freeze 202 files, workstation copy matches; replay 54/54 PASS (393 s, 423 MB), 145/145 hash fields equal Codex's; my own SLSQP search (strat21_check/my_55_search.py) finds no T<0: K5+K5 is the minimiser at k=8..1e6 (9/256 at N=10, 3/8 at infinity), with lowers at s=k-9 equal to 2(k-3)(4k+3)/(5k^2)/M^2. Scar from this round: my freeze excluded every file named codex.log, but Codex hashes inherited20/codex.log as a proof input, so the first replay stopped at once - freeze by top-level name, not by basename anywhere. Also .npz is gitignored in the brain repo; rank3_discovery.npz is a replay input, pushed with ALLOW_IGNORED=1. Pushed: push 156 64e509ad (06_math_research/t104_alon_agent_2026_11_11/strat21 + strat21_check, 43 of 43). Left: D>2 top multiplicity outside the closure; carriers of six or more vertices. Previous: [[t104_split45_lowers_proved_strat20_2026_11_13]].

