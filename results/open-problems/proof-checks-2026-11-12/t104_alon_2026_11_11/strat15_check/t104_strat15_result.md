# T104 (Alon Conj. 1.5): the 5+1 class for every N >= 7 — STRAT15 result

13 Nov 2026, 14:01 +04. an agent. Run on Mac mini 1, ~/agent_run/STRAT15 (Codex pid 94630, normal speed).

## What is proved

PROVED (STRAT15/replay_all.py, replay_summary.json sha256 8dd01bec..., label "all required exact replays passed", 3452 s):
T_N >= 0 for every graph with exactly one connected five-vertex component that carries both top Laplacian eigenvalues
(lambda of multiplicity exactly two) and N-5 isolated vertices, for every N >= 7 and in the limit N -> infinity.
With STRAT13 (N = 6) and STRAT14 (connected n = 5) this closes the 5+1 class for every N >= 6.

The ten replay stages, all PASS: unchanged STRAT14 (699 s), unchanged STRAT13 (1364 s), all-N premises
(verify_allN_ratio, verify_allN_cells, verify_analytic, verify_summary), verify_target, verify_padding, check_spawn,
verify_new (1310 s: the full canonical root for real q >= 1 including infinity; new controls and collar pullbacks).
789 source files unchanged. The first verify_new attempt died on a spawn/import assertion (archived as
failed_replay_1.json); after check_spawn.py was added the resumed run passed with no mismatch.

How all N is handled: C_N(q) = c0 + c1 q + c2 q^2 with q = N - 6; certified c2 >= 0, d1 = c1 + 2c2 >= 0 and
C1 = c0 + c1 + c2 >= 0 on every leaf, which gives C_N >= 0 for all q >= 1 and c2 >= 0 covers N -> infinity.
Corner and the nine equality limits: local_uniform.py, a degree-2 Bernstein form in v = 1/(N-2) in [0, 1/5], with chart
bound T_N >= ||h||_1/12 on matrix balls of radius 1/4000 (edges) and 1/12900 (triangle).

Region list: 8,366 non-all-N leaves (250 STRAT10, 48 STRAT11, 7,702 STRAT12, 366 STRAT13) + 1,004 exclusions that do not
transfer under the weaker all-N premises = 9,370 boxes; 9,357 certified at once, 13 refined into 18 leaves by 5 bisections.
Final ledger 9,289 positive leaves + 86 exclusions; 17 collar boxes kept; STRAT11 corner ball at 15 permutations.

## My independent checks (all PASS, same bank: certificates.json 60441b5e..., refinements.json 8ab45400...)

1. check1a/1b: 7,267 of 7,267 weaker-Farkas transfers re-verified with my own polynomial and Bernstein code.
2. cs_cross / cs_cross2: c0 - c1 + c2 = 1/4 x the STRAT8 face numerator; 8(c0, c1, c2) = the STRAT10 numerator by power of q.
3. check4: the 9,370 inputs each appear once with identical boxes; refinement trees partition their roots exactly; no open
   leaf; 174 of 174 sampled certificates (all 18 refinement leaves + 40 random) re-verify.
4. check5: 176 in-scope rational points in the 17 collar boxes, exact C_N/(q+1)^2 at N = 7, 8, 10, 20, 100, 10^6 and c2:
   no negative value; minima 0.724 (N=7) down to 0.193 (N=10^6). Corroboration, not proof. The corner ball was not sampled.
Files: brain repo 06_math_research/t104_alon_agent_2026_11_11/strat15_check/ (push 144, commit bcbccc601392).

## What is NOT proved

OPEN (RESULT.md, Codex's own reading of STRAT7/RESULT.md): every disconnected graph at D = 2 with components of at most five
vertices does NOT follow. STRAT7 padding covers adding isolates only. Still open:
- a four-vertex double carrier with lower nontrivial components other than one edge; a five-vertex double carrier with any
  nontrivial lower component;
- split simple top carriers 2+3, 2+4, 3+3 with an extra nontrivial lower component;
- split simple top carriers 2+5, 3+4, 3+5, 4+4, 4+5, 5+5, with or without lower components.
Covered already: triangle double carrier and two-edge carriers with arbitrary lower components (S5 = 0); four-vertex double
carrier with at most one lower edge; split pairs 2+3, 2+4, 3+3 with isolates only; now the five-vertex double carrier with
isolates.

## Hashes (Mac mini 1, 14:00:47 +04)
see strat15_check/strat15_final_hashes.txt. Final RESULT.md is 7b470e74... (re-hashed after Codex exited: unchanged).
Its first line reads PROVED for the entire 5+1 class for every integer N >= 7, T_infinity >= 0, zero OPEN leaves, no
counterexample; line 124 keeps the broader disconnected statement OPEN. Tarball STRAT15_final.tgz (24,906,588 bytes,
sha256 554e13fe140a2069f49dc407aa0d5314e7f7b2edef4e6505b5e35ca6d6ceb492, nested STRAT14 excluded on unpack) is on Mac
mini 1 at ~/agent_run/; its 52 top-level files are pushed under strat15/.

## Next for T104
The split carriers 2+5 ... 5+5 and the double carriers with lower components are the next region; each needs its own chart.
