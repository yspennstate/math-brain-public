---
name: t104_split45_lowers_proved_strat20_2026_11_13
description: "T104 split 4+5 proved with arbitrary lower components, every N>=9 (STRAT20, push 153 71574452); only connected 5+5 left (STRAT21 queued on mini1)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T18:08:33+02:00
  status: verified
  evidence: "push 153 71574452 (strat20 + strat20_check/strat20_myreplay.out 46/46 PASS, cmp20.out 106/106, mine_45_search.out)"
---

T104 (Alon Conj 1.5, Oliveira reduction): the disconnected D=2 split 4+5 - a connected four-vertex part and a connected five-vertex part - has T>=0 for every N>=9 and N->infinity, with isolates or arbitrary lower components; two connected top carriers give T>0; equality only at two equal edges plus isolates in the selected-projector closure; positive lower trace strict. Codex STRAT20 (mini1, ended 13 Nov 19:36 Mac, gpt-6.1-sol high, normal speed). How: every pair with a rank<=2 four-part or a rank<=3 five-part transferred from the proved 2+5 theorem at k=5 to k=7, five-part fixed (its trace-square and Y terms cancel; B5<=d5 pays the -8/35 change), extra T*>=1/100; the six four-tree x five-tree pairs by cleared numerators with only positive coefficients in seven fluxes and z=k-7 (23,715 to 38,574 terms), k=7 hardest; lowers by STRAT17 interpolation with S=k-8, F_k(k-8)>=F_7(0)+1/4, eighteen Bernstein controls. My audit: freeze 165 files, workstation copy and live tree both match; my replay 46/46 PASS (193 s, 136 MB), 106/106 receipt hash fields equal; my own SLSQP search (strat20_check/my_45_search.py, from the formula, not Codex code) finds no T<0: isolates minimiser K4+K5 at k=7,8,9,11,20,1e6 (99/2401 at N=9, 20/49 at infinity); with lowers K4+K5 at s=k-8 equals Codex's (k-3)(31k+22)/(20k^2)/M^2 at k=9,10,11,20 (301/4320 at k=9). The shifted-k transfer hint from 3+5 worked again. Pushed: push 153 71574452 (06_math_research/t104_alon_agent_2026_11_11/strat20 top-level files + strat20_check, 36 of 36 verified; inherited copies were pushed with earlier rounds). Left: connected 5+5 (STRAT21, queued on mini1 behind LO05_REF via heavy_lock_run.sh) - the last case for components of at most five vertices. Previous: [[t104_split35_lowers_proved_strat19_2026_11_13]].

