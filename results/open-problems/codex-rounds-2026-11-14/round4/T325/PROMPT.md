# Open problem T325: Do trained transformers learn in-context regression by gradient descent?

Statement: Pretrain a transformer on prompts (x_1, y_1, ..., x_N, y_N, x_query) with x_i ~ N(0, I_d), y_i = <w, x_i> and w ~ N(0, I_d). Zhang, Frei and Bartlett prove that gradient flow on a one-layer linear self-attention model from a suitable initialization converges to a predictor implementing one step of preconditioned gradient descent. Prove that gradient-based training of a multi-layer softmax transformer (or of a linear transformer with L ≥ 2 layers from a random initialization) converges to a predictor whose in-context risk approaches that of the Bayes-optimal ridge predictor as N → ∞, and identify the algorithm it implements.

Caveat: Constructions show transformers can implement gradient descent and ridge regression in context (von Oswald et al.; Akyürek et al.); stationary points of multi-layer linear models are characterized (Ahn et al.). Convergence of training beyond one layer is the open part.

Source: R. Zhang, S. Frei and P. L. Bartlett, Trained Transformers Learn Linear Models In-Context, arXiv:2306.09927 (2023); J. von Oswald et al., Transformers learn in-context by gradient descent, arXiv:2212.07677 (2022); E. Akyürek et al., What learning algorithm is in-context learning? Investigations with linear models, arXiv:2211.15661 (2022); K. Ahn, X. Cheng, H. Daneshmand and S. Sra, Transformers learn to implement preconditioned gradient descent for in-context learning, arXiv:2306.00297 (2023); S. Garg, D. Tsipras, P. Liang and G. Valiant, What Can Transformers Learn In-Context? A Case Study of Simple Function Classes, arXiv:2208.01066 (2022)

Where it stands (checked by us, Nov 2026): Open beyond one layer / linear attention as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T325 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T325 (read it,
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
VERDICT: PROVED global population-gradient-flow convergence for two untied scalar attention step sizes with all other blocks fixed

The new result is an exact d=1, two-layer case of the earlier report's
suggested untying problem. For every integer N>=1 and every unequal
initial pair a(0),b(0), population gradient flow converges to the global
minimum. Thus independent continuous random step-size initialization
succeeds almost surely. The learned step sizes, in either order, are

    a_± = N/(N+2) [1 ± sqrt(2/(N+4))].

The resulting predictor implements two empirical least-squares gradient
steps from zero. Its exact squared prediction risk is

    8/[(N+2)(N+4)],

which approaches the noiseless scalar Bayes risk zero at rate 8/N^2.
At equal initialization, the trajectory instead converges to a strict
saddle. PROOF.md gives the full argument, including global existence,
stationary-point classification and exclusion of the saddle for every
unequal initial pair.

This advances the earlier folder, which contained a literature audit and
no proof or numerical scripts. Its comparison-ODE correction was
independently rederived and holds, conditional on the cited gradient
inequality. The scalar loss was then rederived directly from the source's
token update. No sharp matrix rate from that paper is imported.

The brief web check found no full solution superseding that report.
Opened sources and queries are recorded in LOG.md. The relevant
architecture is from Khashayar Gatmiry, Nikunj Saunshi, Sashank J. Reddi,
Stefanie Jegelka, Sanjiv Kumar, *Can Looped Transformers Learn to Implement
Multi-step Gradient Descent for In-context Learning?*,
[arXiv:2410.08292v1](https://arxiv.org/html/2410.08292v1), Section 3 and
Appendix A.1. No claim of exhaustive literature novelty is made.

Validation command:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_scalar.py
```

The standard-library script independently expands Gaussian sum moments
and verifies exact risks for N=1,2,3,5,10,100,1000. Rational polynomial
checks verify the gradients, loss gap and parameter-difference equation;
direct rational token updates verify the forward pass. All checks passed.
Peak RSS was about 13 MiB. The nice wrapper reports a priority-setting
warning, but a direct query confirms inherited nice=20; the final script
asserts nice>=15. Its optional address-space cap was unavailable. These
short runs remained far below 1 GiB and used one thread, with no numerical
libraries, GPU, training run, git or writes outside this folder.

What remains open: full random initialization of all transformer blocks,
d>1, softmax attention, and discrete or stochastic training. The proof
uses direct trainable Q entries, not separately trainable key/query
factors. No uniform training-time bound in N is established. The full
T325 claim is not proved.

Next worker: keep d=1 and the fixed blocks, and extend the convergence
proof to L>=3 independently initialized scalar step sizes. In elementary
symmetric coordinates the risk is again a strictly convex quadratic,
but repeated step sizes make the coordinate map singular. The missing
piece is a classification and attraction analysis of stationary points
with repeated roots. Alternatively, d>1 requires controlling genuinely
noncommuting layer matrices; the two-dimensional scalar proof does not
settle that obstacle.

Task: “take the NEXT checkable step on this problem, building on that work.” — 15 November 2026, 03:47 Asia/Tbilisi.
