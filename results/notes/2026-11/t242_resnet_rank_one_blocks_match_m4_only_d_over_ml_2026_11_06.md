---
name: t242_resnet_rank_one_blocks_match_m4_only_d_over_ml_2026_11_06
description: "[PROVISIONAL] T242 depth/width commute: with M=1 (rank-one blocks, constraints ii+iii of 2603.18168 broken) the trained ResNet output gap to M=D falls 0.0148->0.0055 over D=64..128, same as M=4; only D/(ML)->0 shows"
metadata:
  type: project
  created: 2026-11-06
  created_at: 2026-11-06T01:36:06+02:00
  status: provisional
  evidence: ""
---

Frontier row T242 target (a), arm G (an agent, 6 Nov 2026). Model and statistic of resnet_dm.py (tanh ResNet, GD k=8, eta 0.5, N=4, coupled RMS output gap against arm A M=D, L=4 sqrt D at the same seed). Arm G: M=1, L=round(4 D^1.5), so D/(ML)=1/(4 sqrt D) as arm A, while log L ~ 9M and D/M=D. Gap A-G: D=64 0.0148 (0.016 0.012 0.017), D=128 0.0055 (0.006 0.006 0.004). Arm F (M=4, same D/(ML)): 0.0189, 0.0056. Arm B (M=sqrt D, L=D): 0.0211, 0.0130. Control C (D/(ML)=1): 0.066, 0.090. Reading: the output limit sees D/(ML) alone down to a single hidden unit per block; constraints (ii) log L=O(M) and (iii) D=O(M) of Theorem 1.1 are invisible here. Size of doubt: three seeds, one data set, outputs only (not hidden states), k=8; per-D means carry about 30 pct. D=256 (L=16384) was running at landing and goes into rows/T242/DOSSIER.md. Files: rows/T242/resnet_dm_g.py, resnet_dm_run4_G.txt, DOSSIER.md (arm G section), moves.jsonl. Status provisional; would change if D=256 levels off above 0.003 or if hidden states disagree. Related [[compaction_agent_20261106T012158]].


**6 Nov 01:59, D = 256 in.** A-G 0.0071 (seeds 0.0067, 0.0108, 0.0040) against A-F 0.0053; F-G is 0.0083, as large as either gap to A. Both arms stop falling after D = 128 and swap order seed by seed, so D = 256 sits at a common floor set by the reference arm's own finite size. Read the claim as: M = 1 tracks M = 4 wherever the test resolves (D = 64, 128); past that the reference must improve (Richardson over arm A at 128/256/512) before anything finer can be said. Would change it: a better reference showing G's gap stuck while F's keeps falling.


**6 Nov 02:3x, the noise split (supersedes the 01:59 'floor from arm A' reading).** Redrawing only the block weights (same embeddings) measures block noise directly: at D = 256 the redraw spread is A 0.0039, F 0.0073, G 0.0054. Averaged over draws per seed, A-F is 0.0013 and A-G 0.0021, against residual noise of about 0.002. So the single-draw gaps were block noise, and M = 1 matches arm A's output limit at D = 256 to about 0.002. At D = 64 and 128 the one-draw gaps were inside A's own redraw spread (0.0158, 0.0114), so those columns never resolved anything. Method lesson for any coupled-gap test: measure each arm's redraw spread before reading a gap as a systematic effect. Would change it: draw-mean gaps that stay above the residual noise as draws are added.
