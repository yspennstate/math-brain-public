---
name: t104_split35_lowers_proved_strat19_2026_11_13
description: "[VERIFIED] T104 split 3+5 proved with arbitrary lower components, every N>=8 (STRAT19, push 151 d64510f1); next 4+5 (STRAT20 queued on mini1 behind the heavy lock)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T16:52:51+02:00
  status: provisional
  evidence: ""
---

T104 (Alon Conj 1.5, Oliveira reduction): the disconnected D=2 split 3+5 - a connected triangle-part and a connected five-vertex part - has T>=0 for every N>=8 and N->infinity, with isolates or arbitrary lower components; equality only two equal edges plus isolates; positive lower trace strict. Codex STRAT19 (mini1, 13 Nov 18:16-18:32 Mac, gpt-6.1-sol high, normal speed). How: rank(A5)<=3 five-parts transferred from the proved 2+5 theorem at k=5 to 3+5 at k=6 with B5<=d5 paying the -2/15 coefficient change (margins 1/20 path corner, 73/675 balanced triangle, plus inherited 1/400000) - no new SOS; six triangle-corner x five-tree numerators with only positive coefficients in fluxes and z=k-6; lowers by STRAT17 interpolation, F_k(k-7)>=F_6(0)+1/4. My audit: replay on mini1 framework python 39/39 PASS (103 s, 100 MB), 87/87 receipt hashes equal, live tree == freeze (132 files); my own SLSQP search (my_35_search.py, written from the formula, not Codex code) finds no T<0, K3+K5 = 56/1215 at N=8 and 4/9 at infinity, and with lowers K3+K5 at s=k-7 equals Codex's 2(k-3)(11k+7)/(15k^2)/M^2 at k=8,9,10,20; no uniform margin as N->infinity (T* ~22/15, T ~ 1/M^2). Files: 06_math_research/t104_alon_agent_2026_11_11/strat19 and strat19_check. Hint for 4+5/5+5: try the same shifted-k transfer from a proved smaller split before new SOS. Scar the same day: I launched STRAT20 on mini1 without reading ~/.claude/compute/heavy_job.lock while the BTC stretch held it; stopped it after 3 min and requeued via ~/brain/porting/heavy_lock_run.sh with a foreground run.sh - launch Codex on mini1 only that way. Previous: [[t104_split44_lowers_proved_strat18_2026_11_13]]; scar: [[codex_launch_during_btc_heavy_phase_killed_stretch_lock_gate_added_2026_11_13]].
