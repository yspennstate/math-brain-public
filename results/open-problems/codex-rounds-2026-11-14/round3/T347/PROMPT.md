# Open problem T347: The Amit–Gutfreund–Sompolinsky capacity of the Hopfield model

Statement: In the Hopfield model with N neurons and M = alpha·N iid uniform ±1 patterns xi^mu, with energy H(sigma) = −(1/(2N)) Σ_mu (Σ_i xi_i^mu sigma_i)², prove that at zero temperature there are, with high probability, local minima of H (fixed points of the zero-temperature dynamics) with overlap close to 1 with each pattern if and only if alpha < alpha_c, where alpha_c ≈ 0.138 is the replica-symmetric value of Amit, Gutfreund and Sompolinsky; and prove the replica-symmetric free energy in the retrieval phase.

Caveat: Retrieval states are proved to exist for small alpha (Newman: alpha < 0.056; Loukianova: alpha < 0.071; to verify Talagrand's bounds; Feng, Shcherbina and Tirozzi, arXiv:math-ph/0012038, state that a stable fixed point exists with probability tending to one for alpha <= 0.113, with retrieval errors matching the replica prediction at small alpha, to verify); the replica-symmetric formula is proved at high temperature or small alpha (Talagrand; Bovier and Gayrard). The threshold 0.138 is not proved.

Source: D. J. Amit, H. Gutfreund and H. Sompolinsky, Storing infinite numbers of patterns in a spin-glass model of neural networks, Phys. Rev. Lett. 55 (1985) 1530; M. Talagrand, Rigorous results for the Hopfield model with many patterns, Probab. Theory Related Fields 110 (1998) 177-276

Where it stands (checked by us, Nov 2026): Open (the 0.138 threshold).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T347 (read it,
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
VERDICT: PARTIAL substantial 2026 free-energy advance located; exact T347 remains unverified

The literature stop condition applies. References, theorem numbers, identifiers, and scope are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). No new proof or computation is claimed.

The opened Bernoulli-pattern theorem goes beyond the high-temperature/small-load free-energy results listed in the prompt. The separate capacity claim remains an unaudited preprint with a different success criterion. Neither is recorded here as a proof of the stated AGS threshold or replica symmetry throughout retrieval.

Checks: compared model normalization with the prompt; checked theorem statements against abstracts; distinguished Gaussian from Bernoulli disorder, equilibrium from constrained profiles, and barriers from an exclusion of individual minima. The reported capacity endpoints agree between the abstract and Theorem 1.4(c); their certificates were not rerun.

Commands and web operations are recorded in [LOG.md](LOG.md). No mathematical computation was run. The first PDF request failed; following the PDF link succeeded. The nice warning was checked: inherited priority is already 20.

Next worker: audit the new variational theorem and the capacity preprint, especially the uniform strict merging inequality and numerical certificates; specify an overlap/error criterion and the relation between wells and single-spin local minima before claiming the requested equivalence.

Task: “push this problem forward by one checkable piece.” Start: 14 November 2026, 22:14 +04.
