# Verify: has open problem T304 been settled by the OpenAI math release?

Our row: The query complexity of sampling from strongly log-concave distributions
Statement: For targets pi ∝ exp(−f) on R^d with f m-strongly convex and L-smooth (condition number kappa = L/m), determine the minimal number of gradient (or value) queries needed to output a sample within total variation epsilon (or Wasserstein epsilon·sqrt(d/m)), as a function of d and kappa. In particular decide whether the d^{1/3} dimension dependence of the randomized midpoint method and the d^{1/2} of MALA from a warm start are optimal in their respective accuracy regimes.
Where it stands (our note, Nov 2026, written before we knew of the release): Open (gap between upper and lower bounds in general dimension). Zhou and Suzuki (arXiv:2611.05813) prove that any randomized first-order sampler needs exp(Omega(log^(1/3) d)) queries for strongly log-concave targets with condition number 2, even from a warm start, which rules out polylogarithmic dimension dependence; the gap to the known upper bounds remains.

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026  (title match score 53)
- https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026  (title match score 28)
- https://github.com/openai/math/tree/main/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026  (title match score 22)

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

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/AV_T304 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/AV_T304 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/AV_T304 (read it, never
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
VERDICT: PROVED one-factor R improvement in Lemma 6.2's harmonic and angle error bounds, conditional on the stated spatial and probability-circuit inputs
New beyond round 4: PROOF.md derives stationary harmonic derivative bounds with R^{-(2m-1)}, giving angle error delta^{2tm-3t} and harmonic truncation delta^{2tm+t}; the source's respective bounds are delta^{2tm-4t} and delta^{2tm}. This is a local implication, not certification of the complete sampler; T304 remains open in full, with literature verdict PARTIAL-CLAIMED.
Recheck: the inherited cancellation, Hermite endpoint weights, scale identities and exponent margins hold. The previous script passes; a new nodal-polynomial construction independently reproduces its endpoint weights. Nine reopened original source snapshots match, and the three main theorem quotations remain verbatim. No later settlement was located in the bounded update search.
Commands: nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -I -B audit_round5.py; the same prefix with sources/round4/audit_round4.py. All exact checks pass, including weighted-divergence identities, translated quadratic examples, stencil moments and independent exponent propagation.
Failure checks: correlated harmonic anchors destroy stationarity; weakening the source's actual R^{-(j-1)} spatial input to R^{-j} loses the gain. Neither is a defect in the stated construction. An initial source-hash mismatch was only terminal-newline normalization and was resolved by direct text comparison. The sandbox refuses nice's priority adjustment; only negligible single-threaded standard-library checks ran.
Uncertainty and next step: the jet, spatial transport and probability-circuit accuracy estimates remain inputs. Check Lemma 6.3's endpoint quadrature error and its probability-time derivative inputs in Lemma 5.1/Section 4 next; later centering integration, compiler query cap, sampling reductions and the complete Lean import graph remain unaudited.
Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026; exact request time was not supplied, first logged clock reading 07:34:55 +04.
