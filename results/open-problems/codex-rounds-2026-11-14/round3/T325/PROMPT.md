# Open problem T325: Do trained transformers learn in-context regression by gradient descent?

Statement: Pretrain a transformer on prompts (x_1, y_1, ..., x_N, y_N, x_query) with x_i ~ N(0, I_d), y_i = <w, x_i> and w ~ N(0, I_d). Zhang, Frei and Bartlett prove that gradient flow on a one-layer linear self-attention model from a suitable initialization converges to a predictor implementing one step of preconditioned gradient descent. Prove that gradient-based training of a multi-layer softmax transformer (or of a linear transformer with L ≥ 2 layers from a random initialization) converges to a predictor whose in-context risk approaches that of the Bayes-optimal ridge predictor as N → ∞, and identify the algorithm it implements.

Caveat: Constructions show transformers can implement gradient descent and ridge regression in context (von Oswald et al.; Akyürek et al.); stationary points of multi-layer linear models are characterized (Ahn et al.). Convergence of training beyond one layer is the open part.

Source: R. Zhang, S. Frei and P. L. Bartlett, Trained Transformers Learn Linear Models In-Context, arXiv:2306.09927 (2023); J. von Oswald et al., Transformers learn in-context by gradient descent, arXiv:2212.07677 (2022); E. Akyürek et al., What learning algorithm is in-context learning? Investigations with linear models, arXiv:2211.15661 (2022); K. Ahn, X. Cheng, H. Daneshmand and S. Sra, Transformers learn to implement preconditioned gradient descent for in-context learning, arXiv:2306.00297 (2023); S. Garg, D. Tsipras, P. Liang and G. Valiant, What Can Transformers Learn In-Context? A Case Study of Simple Function Classes, arXiv:2208.01066 (2022)

Where it stands (checked by us, Nov 2026): Open beyond one layer / linear attention as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T325 (read it,
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
VERDICT: PARTIAL identified substantial restricted training-convergence advances omitted from the supplied status

Created [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) with three opened primary references, exact authors, arXiv identifiers, theorem locations, and restrictions. The literature search took less than ten minutes. The papers are from 2024–October 2026; no claim is made to have found work published after the supplied November 2026 check.

The full T325 statement remains unproved here. The existing results justify the requested substantial-advance stop branch, interpreted to include relevant older work omitted from the supplied status. No new training experiment or unconditional convergence proof was attempted.

Commands and web queries are recorded in [LOG.md](LOG.md). No numerical workload was run. The only Python invocation read orientation files and listed the workspace; its nice wrapper reported a priority-setting failure. A subsequent process-priority inspection was denied. All deliverables were written inside this folder, without git or external mutations.

Audit: checked theorem assumptions against architecture and objective definitions; distinguished weight sharing, fixed blocks, structured initialization, and CoT supervision from the requested setting. Independently integrated the scalar gradient-dominance comparison equation and checked it by differentiation. Found a sign/prefactor discrepancy in one displayed comparison argument and a dimension-factor mismatch in another reported bound. Details are in LOG.md. These checks do not certify the full proofs of the cited papers or refute their qualitative results.

Next worker: begin with the restricted looped-model theorem, verify its loss identity and matrix domain, and resolve the recorded bound discrepancies before importing numerical rates. A concrete subsequent target is stability of its training trajectory under small nonzero perturbations to the prescribed zero blocks and under untying two layers. Neither stability statement is established here.

Task: “push this problem forward by one checkable piece” — 14 November 2026, 22:13 Asia/Tbilisi.
