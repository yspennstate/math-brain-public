# Verify: has open problem T083 been settled by the OpenAI math release?

Our row: Pointwise convergence of multiple ergodic averages
Statement: For a measure-preserving system (X, μ, T), k ≥ 3 and f_1, …, f_k ∈ L^∞(μ), the averages (1/N) Σ_{n<N} f_1(T^n x) f_2(T^{2n} x) ⋯ f_k(T^{kn} x) converge for μ-almost every x.
Where it stands (our note, Nov 2026, written before we knew of the release): k = 2 (Bourgain 1990). Norm convergence for every k (Host–Kra 2005; Ziegler 2007) and for commuting transformations (Tao, arXiv:0707.1117, ETDS 2008). Pointwise results for nilsystems (Leibman 2005) and distal systems (Huang–Shao–Ye, arXiv:1406.5930), and for the bilinear averages f(T^n x) g(T^{P(n)} x) with deg P ≥ 2 (Krause–Mirek–Tao, arXiv:2008.00857, Ann. Math. 2022). Open for k = 3.

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026  (title match score 42)
- https://github.com/openai/math/tree/main/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026  (title match score 40)
- https://github.com/openai/math/tree/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026  (title match score 40)

Your job (a literature verification, not a new proof):
1. For each candidate, open the preprint itself (the folder holds paper.tex or build/paper.tex or paper.pdf; raw files are
   at https://raw.githubusercontent.com/openai/math/main/preprints/<folder>/...). Copy its main theorem statement exactly.
2. Compare it with OUR statement word by word: same model, same dimension or range, same quantity, same strength (a
   bound vs an asymptotic, a special case vs the general one). Say precisely what is covered and what is not.
3. Search for anything after the preprint: an arXiv version or exposition, a refutation, an error report, a referee or
   expert comment, a Lean formalisation (the repository's lean/ folder and docs). Record what you opened.
4. Write VERIFY.md with: the theorem quoted, the comparison, the follow-ups found, and a recommended new "where it stands"
   sentence for our row, in plain words, at most three sentences, naming the preprint by its title and date.
5. Write REPORT.md whose first line is exactly one of:
   VERDICT: SOLVED-CLAIMED <the whole statement is claimed>  |  VERDICT: PARTIAL-CLAIMED <which part>  |
   VERDICT: NOT-THIS <the preprint is about something else>  |  VERDICT: UNREADABLE <why>
   Then two or three lines of reasons. Do not judge the preprint's proof correct; you may note a step that looks wrong.
If time remains after REPORT.md, pick the single most load-bearing lemma of the preprint and check it carefully; append what
you found to VERIFY.md under "Spot check".

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/AV_T083 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/AV_T083 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/AV_T083 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.




----- earlier REPORT.md -----
VERDICT: PROVED the smooth-row estimate under its stated Bessel hypotheses with catalog loss 140(log_2(2d))^(3/2)
New beyond round 4: PROOF.md verifies the smooth-row application in the separated-scale lemma and improves its bound from 760(B_H+A)(log_2(2d))^2 to 140(B_H+A)(log_2(2d))^(3/2), times |R|^(1/2), where d=2+#carriers. Disjoint residue-class output coordinates give the improvement.
Recheck: round-4 check_rows.py passed all 4,240 stopping and 8,480 Abel checks; independent weak-tail and Abel rederivation agrees. Commands: OMP_NUM_THREADS=1 nice -n 15 python3 -B check_smooth_rows.py; the same launcher ran the earlier script read-only. Exact bump, Bessel, residue and constant checks passed; final counts are in LOG.md.
No mathematical check failed. The five-minute literature refresh found no later settlement; VERIFY.md quotes and compares all three main theorems. The full T083 statement and the candidate proofs remain unverified.
Next: check base.tex lines 553–569 against H's “A scale sum for one separated term”, especially the ordinary selected-array Bessel bound, fixed complete carriers and catalog count. Those scalar premises, projected-input compression and the full separated-scale lemma are still uncertain.
Task: “Verify: has open problem T083 been settled by the OpenAI math release?” — 15 November 2026, first clock 07:23:33 +04; exact receipt time unavailable.
