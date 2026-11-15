# Verify: has open problem T137 been settled by the OpenAI math release?

Our row: The Parisi formula for diluted spin glasses
Statement: For the Viana–Bray model, N Ising spins in which each pair interacts, independently with probability c/N, through an independent coupling with the symmetric law ±1 (or the standard Gaussian law), prove that lim (1/N) E log Z_N(β) equals the Mézard–Parisi variational formula at every β > 0, with full replica symmetry breaking where the model needs it. The same question is posed for the diluted K-spin model with K even and for random K-SAT at positive temperature.
Where it stands (our note, Nov 2026, written before we knew of the release): The formula is an upper bound for the diluted K-spin model with K even, which includes Viana–Bray, and for random K-SAT (Franz–Leone 2003; Panchenko–Talagrand 2004), and it is proved in replica-symmetric regimes such as high temperature (for Viana–Bray, Guerra–Toninelli, J. Stat. Phys. 115 (2004)). Panchenko showed that 1-RSB asymptotic Gibbs measures of the diluted p-spin models satisfy the Mézard–Parisi ansatz (arXiv:1308.1944), and that after a small modification of the Hamiltonian so do all finite-RSB ones (arXiv:1406.4702); the full-RSB case and the removal of the modification are missing. The satisfiability threshold of random K-SAT at large K is proved to be the one-step value (Ding–Sly–Sun 2015), but that is a zero-temperature statement, not the free energy. The formula at every temperature is open.

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026  (title match score 56)
- https://github.com/openai/math/tree/main/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026  (title match score 29)
- https://github.com/openai/math/tree/main/preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026  (title match score 15)

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
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T137 (read it,
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
VERDICT: PARTIAL-CLAIMED Viana–Bray and diluted even-K spin glasses at every positive temperature; positive-temperature random K-SAT only for even K
OpenAI's “The Mézard–Parisi formula for diluted spin glasses” (September 23, 2026) claims equality with the infimum over all finite hierarchy depths, without a finite-RSB restriction; its arity hypothesis explicitly excludes odd-K SAT.
The other two candidates concern Haar-orthogonal interaction matrices and representation-theoretic Spin groups, respectively, and do not cover T137's sparse models. No correctness judgment is made here.
A separate later paper by Dmitry Panchenko, “The Mézard-Parisi formula” (arXiv:2610.39545, October 29, 2026), claims the full row, including random K-SAT for every K >= 2; it does not verify OpenAI's different argument.
