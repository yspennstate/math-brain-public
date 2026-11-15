# Verify: has open problem T095 been settled by the OpenAI math release?

Our row: Differentiability of the limit shape in first-passage percolation
Statement: For first-passage percolation on Z^2 with iid nonnegative edge weights whose law is continuous and satisfies E min(τ_1, …, τ_4)² < ∞ (the Cox–Durrett condition for the shape theorem; τ_1, …, τ_4 are independent copies), the boundary of the limit shape is differentiable at every point.
Where it stands (our note, Nov 2026, written before we knew of the release): The shape is compact and convex (Cox–Durrett 1981). Flat edges occur for atoms at the infimum (Durrett–Liggett 1981), with differentiability at the endpoints of the flat segment (Auffinger–Damron 2013; Auffinger–Damron–Hanson, arXiv:1511.03262, Theorem 2.25). No continuous weight distribution is known to give a differentiable boundary; strict convexity is open too (T050).

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026  (title match score 55)
- https://github.com/openai/math/tree/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026  (title match score 31)
- https://github.com/openai/math/tree/main/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026  (title match score 17)

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

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T095 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/AV_T095 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/AV_T095 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T095 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/AV_T095 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T095 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PARTIAL rare-fast crossing input checked from the fixed-Gamma uniform shape theorem
New beyond round 3: PROOF.md derives df:cr:rare-fast and its local-travel prerequisites, checks the noncircular dependence radius, and gives the sufficient bad-site bound 2^(-48(2k+1)^2). No gap was found in this section under its stated shape-theorem input; the full preprint is unverified, and its Gamma-only claims do not settle general T095.
Recheck: the earlier audit passes unchanged. `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py` passes 2,307 contour cases, 1,536 rational strip placements, 1,734 dependence-coordinate cases, source/theorem checks, and two exact contour-sum evaluations giving 181/48000. Actual nice is 20; measured peak RSS is 15,974,400 bytes. Both attempted memory-limit setters were rejected before mathematical checks; the bounded audit then completed in 0.307 seconds.
No new full continuous-law result or specific refutation was located. Next: inspect the transverse-witness argument and its use of the endpoint estimates; retain the Gamma-specific change of measure as a limitation. Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 04:16 Asia/Tbilisi.
