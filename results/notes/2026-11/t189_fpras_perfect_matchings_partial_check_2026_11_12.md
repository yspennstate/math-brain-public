---
name: t189_fpras_perfect_matchings_partial_check_2026_11_12
description: "FPRAS for counting perfect matchings in general graphs (OpenAI 23 Sep 2026; Liu-Meng arXiv 2610.26803): Sections 3-5 of the simplified proof verified by hand, the two-matching restricted Poincare inequality tested on K_6 and K_8 (best constant bounded for ultrametric weights, 1/t for a heavy cycle), its proof read not verified; do not work the row as open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T03:00:18+02:00
  status: provisional
  evidence: "06_math_research/t189_fpras_matchings_agent_2026_11_12/T189_CHECK.md, t189_check.out; push d560ad19ff15dc560bda4e4c1f71d7a9f0d33b4b"
---

Row T189 of the top-200 list (an FPRAS for counting perfect matchings in general graphs) is reported solved and the report holds up to a partial check. Sources: OpenAI, "A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs", 23 Sep 2026, 45 pages, public repository openai/math (preprints folder; not on arXiv); Liu and Meng, arXiv 2610.26803 (19 Oct 2026), 20 pages, an independent simplified proof with the same architecture.

What I did (12 Nov 2026), on the Liu-Meng version: verified by hand every step of Sections 3, 4, 5 and the final assembly of Section 2.4 (capped levels, the replication lemma 3.1 and the gap 3/(8J), hole-ratio inequalities (4.2)-(4.7), the completion bound Z_mu/Z_lambda <= e^0.001, the marked law and its three means, the dyadic balancing pass, Hoeffding and the final product). Not verified: the proof of Theorem 2.1 (two-matching restricted Poincare inequality, Var(f) <= (10n)^80 r^9 E(f(M1)+g(M2)) for weights within a factor r of an ultrametric), which is the core; I read it and followed the telescoping but did not check the cell comparisons or the encoding. No Lean formalization of this theorem in the repository.

Computer tests (t189_check.py, brute force on K_4, K_6, K_8): (4.2), (4.4), (4.5) hold to rounding on 360 weight matrices; g(U) B_ij / n is at most 0.284 on 290 balanced instances (the lemma allows 1e5); 2 Var <= S holds. The best constant in Theorem 2.1, computed exactly, stays bounded as the spread of an ultrametric goes to infinity (limit 1/18 at n = 6, 1/36 at n = 8, the rate of one two-edge switch) and decays like 1/t for a heavy chordless 6-cycle with light chords, where r = t.

How to use: do not work T189 as open. Open next to it: a practical running time (q = 32 (10n)^80 (D+1)^9 matchings per level, D = 1e8 (n+1)^4); the true order of the two-matching constant (numerics suggest about n^2); a deterministic scheme. Reusable: the replication lemma (additive two-coordinate Poincare inequality plus q independent guide coordinates gives a gap for all functions, cost factor 1 - 4C/q); completion by the bottleneck ultrametric; marking a sample to read several partition-function ratios from one batch. When a theorem's constant is beyond experiment, compute the best constant exactly on small cases and watch how it moves with the parameter the hypothesis controls, and include one case outside the hypothesis.

What would change this: an error found in Liu-Meng Sections 2.2-2.4 or in the original Sections 5-6; a third independent write-up or a formalization would raise the check from partial to full.

