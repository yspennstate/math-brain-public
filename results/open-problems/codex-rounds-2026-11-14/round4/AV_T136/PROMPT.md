# Verify: has open problem T136 been settled by the OpenAI math release?

Our row: Free-energy and ground-state fluctuations of the Sherrington–Kirkpatrick model at low temperature
Statement: For the Ising SK model H_N(σ) = N^{−1/2} Σ_{i<j} g_ij σ_i σ_j with iid standard Gaussian couplings, determine the order and the limiting law of the fluctuations of log Z_N(β) at each fixed β > 1, and of the ground-state energy max_σ H_N(σ). Physics predicts a standard deviation of order N^{1/6}.
Where it stands (our note, Nov 2026, written before we knew of the release): For β < 1 the fluctuations are of order one and Gaussian (Aizenman–Lebowitz–Ruelle 1987). For β > 1 superconcentration gives variance O(N/log N) (Chatterjee, arXiv:0907.3381, at zero external field). Aronow and Lopatto (arXiv:2609.09103, 2026) prove that at zero external field and every fixed β > 1 the variance of log Z_N(β) lies between the orders N^{4/15} and N^{7/15}, with the same exponents for the ground-state energy; the predicted standard deviation N^{1/6}, a variance of order N^{1/3}, lies inside that range. The competing predictions are surveyed by Collins-Woodfin and Le (arXiv:2510.26960). The exponent and the limit law are open.

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026  (title match score 63)
- https://github.com/openai/math/tree/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026  (title match score 48)
- https://github.com/openai/math/tree/main/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026  (title match score 31)

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
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T136 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/AV_T136 (read it,
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
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T136 (read it,
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
VERDICT: PROVED bare-system exponential augmentation lemma for Gaussian zero-field SK, for every exponential rate 0<a<=1.
New beyond the earlier report: PROOF.md gives a finite-dimensional density proof for completed and uncompleted log Z, plus an explicit uniform exponential-moment bound conditional on bounded n^(-1/3) variance. This verifies one supporting lemma at bare endpoints; it does not verify hierarchical paths, the stopped pressure increment, or the SK fluctuation theorem.
The earlier literature verdict survives independent rechecking: PARTIAL-CLAIMED for fixed finite beta>1 (scale, positive variance equivalent and moment-characterized law); ground-state fluctuations remain outside the three candidates. The brief follow-up search found no change; the later formalization reports exponent results, excluding the prefactor and limiting law.
Checks passed: five exact quotations, seven fresh-source comparisons, 336 exact covariance cases and the earlier smoothing exponents. Reproduce with `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit.py`; output is in audit.txt. Niceness and an attempted data-limit change were denied; no Lean replay was run. Next check: extend the gauge-density argument to every physical hierarchical path in Section 4, checking preservation of the initial continuation law and its negative convex coefficient.
Task: “Verify: has open problem T136 been settled by the OpenAI math release?” Continuation began 15 November 2026, about 00:57 Asia/Tbilisi; the ask has no separate timestamp in the supplied prompt.
