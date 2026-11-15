# Verify: has open problem T030 been settled by the OpenAI math release?

Our row: Rauch's hot spots conjecture for convex domains
Statement: For a bounded convex domain in R^2, every eigenfunction of the second Neumann eigenvalue of the Laplacian attains its maximum and minimum only on the boundary.
Where it stands (our note, Nov 2026, written before we knew of the release): Proved for obtuse triangles (Bañuelos–Burdzy 1999), lip domains (Atar–Burdzy 2004), convex domains with two axes of symmetry (Jerison–Nadirashvili 2000), all triangles (Judge–Mondal 2020) and further classes. Open for general convex planar domains.

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026  (title match score 36)
- https://github.com/openai/math/tree/main/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026  (title match score 22)
- https://github.com/openai/math/tree/main/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026  (title match score 13)

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
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T030 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/AV_T030 (read it,
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
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T030 (read it,
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
VERDICT: PROVED the bounded positive-kernel resolvent lemma used in the preprint audit, with a quantitative quadrature error estimate
New beyond the earlier report: PROOF.md independently derives the finite resolvent by Schur complements and proves its bounded continuous compact-support quadrature limit. The earlier smooth-boundary scope finding and regularization algebra survive independent rechecks; the literature verdict for the full T030 row remains PARTIAL-CLAIMED.
Command: OMP_NUM_THREADS=1 nice -n 15 python3 audit_resolvent.py. All 34 exact-rational elimination orders and 18 sharp scalar perturbation checks passed, including zero weights and coincident nodes; peak RSS 14,811,136 bytes, inherited priority 20.
What fails: negative updates can produce two positive reciprocal eigenvalues despite positive kernel entries; at the critical one-node weight the resolvent is singular. Both restrictions are present in the preprint, so these are not reported errors in it.
No later full strict convex-planar solution was found in the bounded literature search. The singular Green limit, boundary passage and eigenfunction argument remain unchecked here; no judgment of the complete proof is made. Next: check the epsilon-to-zero passage in prop:interior-reciprocal, especially the diagonal and off-diagonal L2 source bound.
Task: “Verify: has open problem T030 been settled by the OpenAI math release?” — 15 November 2026, about 00:50 Asia/Tbilisi.
