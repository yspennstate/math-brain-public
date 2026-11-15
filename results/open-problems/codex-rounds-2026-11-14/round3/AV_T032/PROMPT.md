# Verify: has open problem T032 been settled by the OpenAI math release?

Our row: Bose–Einstein condensation for interacting bosons in three dimensions
Statement: The interacting Bose gas in three dimensions (for example with a repulsive pair potential), in the thermodynamic limit at fixed density, condenses at low temperature: the one-body density matrix has off-diagonal long-range order.
Where it stands (our note, Nov 2026, written before we knew of the release): Proved for the ideal gas and for interactions that do not couple cycles (Süto 1993, 2002); ground-state and trapped-gas results in dilute limits (Lieb–Seiringer 2002 and later); macroscopic cycles in spatial random permutation models with special interactions (Betz–Ueltschi, arXiv:0711.1188). Open for the interacting gas at positive temperature.

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026  (title match score 43)
- https://github.com/openai/math/tree/main/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026  (title match score 17)
- https://github.com/openai/math/tree/main/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026  (title match score 17)

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
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T032 (read it,
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
VERDICT: PARTIAL-CLAIMED macroscopic constant-orbital condensation for three-dimensional dilute hard spheres at fixed density and low positive temperature in the thermodynamic limit
The model is restricted to hard spheres at sufficiently small fixed gas parameter; main Theorem 1.1 gives one positive temperature, and scaled Theorem 2.1 also yields a low-temperature interval.
The conclusion is a positive liminf of the constant-orbital occupation fraction, without a stated pointwise infinite-distance kernel limit; the other candidates concern zero-temperature ground states.
The documented Lean result covers ground-state condensation only. Later expert literature describes the announcement as under review; this report does not judge the proofs correct.
