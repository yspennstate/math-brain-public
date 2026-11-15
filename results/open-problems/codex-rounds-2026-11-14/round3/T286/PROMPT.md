# Open problem T286: Bayes-optimal learning of extensive-width networks with quadratically many samples

Statement: Learn a two-layer teacher network with width m proportional to the input dimension d from n = alpha·d² samples. Maillard, Troiani, Martin, Krzakala and Zdeborová obtain the Bayes-optimal error for quadratic activation by mapping to extensive-rank matrix denoising, and conjecture a formula for general activations. Prove the Bayes-optimal error for a general activation (e.g. ReLU or tanh) in this regime, and decide whether gradient descent achieves it.

Caveat: For quadratic activation the formula rests on a matrix-denoising reduction (rigorous status to verify); the general case is conjectural.

Source: A. Maillard, E. Troiani, S. Martin, F. Krzakala and L. Zdeborová, Bayes-optimal learning of an extensive-width neural network from quadratically many samples, arXiv:2408.03733 (2024)

Where it stands (checked by us, Nov 2026): Open beyond quadratic activation as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T286 (read it,
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
VERDICT: PARTIAL literature status corrected; substantial follow-ups found, general theorem still open

The bounded literature search found a rigorous restricted quadratic follow-up and developed general-activation predictions. References, exact theorem locations and restrictions are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). Its filename is required by the prompt's stopping branch and does not mean the general problem is solved.

The key rigorous reference is Yizhou Xu, Antoine Maillard, Lenka Zdeborová, Florent Krzakala, [arXiv:2503.14121](https://arxiv.org/abs/2503.14121), Theorem 2.10. The principal general-activation follow-up is Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore, Rudy Skerk, [arXiv:2510.24616](https://arxiv.org/abs/2510.24616), whose Remark 4 retains explicit conjectures.

No new theorem or computation was attempted after the substantial-advance finding, following instruction 1. These advances predate the supplied November 2026 status date; the search did not uncover a subsequent rigorous solution. The assertion that the general case remains open survives this check, while the quadratic caveat can be sharpened.

Verification: compared abstracts against full-text theorem statements and caveats; checked the sample scaling directly in equation (4) of 2510.24616; distinguished ADAM experiments from gradient-descent theorems, and fresh-sample online SGD from reuse of a fixed dataset. No load-bearing numerical estimates were made. Published proofs were not independently reconstructed in full.

Commands and web queries are recorded in [LOG.md](LOG.md). Shell work consisted of reading local orientation files, checking time and writing these documents. No numerical program, git operation or external write was run. Two guessed HTML version URLs returned 404; correct versions were subsequently opened.

Next worker: start with Appendix B.6 of 2510.24616v5, audit its interpolation remainder and concentration assumptions, and isolate one lemma for activations with μ₀=μ₁=μ₂=0. Keep the ReLU case separate because its second Hermite coefficient is nonzero. Neither optimizer experiments nor online-SGD timescale predictions settle the fixed-dataset gradient-descent question.

Task: “push this problem forward by one checkable piece” — session logged 14 November 2026, 22:09 Asia/Tbilisi.
