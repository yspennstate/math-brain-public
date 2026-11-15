# Open problem T267: Epoch-wise double descent

Statement: Epoch-wise double descent for networks. Fix a two-layer network of width m with a stated activation, trained by full-batch gradient flow from a stated initialization on n samples, Gaussian inputs in dimension d, labels from a teacher plus noise of variance s^2 (or labels flipped with probability p), in a stated limit: proportional (n, m, d tending to infinity at fixed ratios) or lazy (m much larger than n). Compute the limiting test risk R(t), the actual risk and not an upper bound, and prove that with probability tending to one R has two local minima and an interior local maximum in t, with the peak time to leading order. Feature learning (both layers trained) and the lazy or random-features regime are separate statements. Linear models with features learned at different speeds already show the effect (Heckel and Yilmaz; Pezeshki et al.) and do not answer the question.

Caveat: Linear models with features of very different scales show the effect (Heckel and Yilmaz 2020, to verify); the question is for networks.

Source: P. Nakkiran, G. Kaplun, Y. Bansal, T. Yang, B. Barak and I. Sutskever, Deep Double Descent: Where Bigger Models and More Data Hurt, arXiv:1912.02292 (2019)

Where it stands (checked by us, Nov 2026): Open for networks as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T267 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T267 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T267 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T267 (read it, never
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
VERDICT: PARTIAL proved the centered quadratic training-Gram approximation and the ReLU training-kernel reduction with its radial spike retained

The round 4 ReLU test-risk reduction checks out. The new piece is the training-side lemma that report requested. For independent uniform directions, let B have zero diagonal and off-diagonal entries `(u_i.u_j)^2-1/d`. Equation (3) of PROOF.md gives the exact fourth-trace identity

\[
 \mathbb E\operatorname{tr}B^4
 =(n)_4D\lambda^4+2(n)_3(\lambda r)^2+(n)_2\kappa_4,
\]

where `D=(d-1)(d+2)/2`, `lambda=2/[d(d+2)]`, `r=1-1/d`, and the explicit fourth centered moment kappa4 is in equation (2). If `d/n -> gamma>0`, then `d*E tr(B^4) -> 8/gamma^3`. Therefore `||B||_op=O_P(d^(-1/4)) -> 0`. The rate is not asserted sharp.

For standard Gaussian inputs, uncentered ReLU features and independent standard Gaussian first-layer weights, this proves

\[
 K_m=\frac{XX^T}{4d}+\mu_d aa^T+cI+o_{\mathbb P}(1)
\]

in operator norm, provided `m/n^2 -> infinity`. Here `a_i=||x_i||/sqrt(d)`, `c=1/4-1/(2*pi)`, and `mu_d=1/(2*pi)+1/(4*pi*d)+O(d^(-2))` is the exact radial mean from round 4. Equation (6) also gives a comparison preserving the diagonal exactly. The total finite-width operator error is `O_P(d^(-1/4)+n/sqrt(m))`.

An important failed simplification is now quantified: replacing mu_d by `1/(2*pi)` alone leaves operator error tending to `1/(4*pi*gamma)`. Keeping the quadratic radial correction is necessary for this operator approximation. Also `||B||_F^2 -> 2/gamma^2` in probability, so the elementary Frobenius shortcut fails despite operator convergence.

Equation (26), using the previous test-risk theorem and the new training lemma, replaces the original nonlinear training matrix inside its all-time realized-risk reduction by the displayed linear-plus-radial matrix. The network has only its output layer trained from zero, a Gaussian random linear teacher of energy E and independent Gaussian label noise of variance s^2. The radial spike is retained in H_t. This is not a deterministic limiting risk formula, a proof of two minima, or a peak-time calculation. Neither layer-learning dynamics nor proportional width is covered.

Verification was analytic. Re-enumerated the fourth trace by squaring B^2; checked n=2 and n=3; derived kappa4 both from raw spherical moments and a centered beta-moment recurrence; checked d=2 by angular integration; independently checked the covariance, eighth moment, ReLU constants, exact diagonal and all-time filter perturbation. No numerical program was run: the sandbox refuses the requested nice adjustment. No error in the stated new lemma was found.

The literature check closed within five minutes. The inspected [paper by Antoine Bodin and Nicolas Macris](https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf), *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, arXiv:2110.11805, still leaves a concentration hypothesis unproved. The opened recent diagnostic work and exact search queries are recorded in LOG.md. No inspected source supplied the requested theorem; this short check does not certify openness. No novelty claim over existing general kernel-linearization theorems is made for the training approximation itself; the contribution here is a self-contained proof closing this sequence's specific gap.

Commands and artifacts: read all three predecessor REPORT.md, LOG.md and PROOF.md files and all four ancestral Python scripts read-only. Text inspection used `rg --files`, `cat`, `sed` and `tail`; shell commands were prefixed with `nice -n 15 env OMP_NUM_THREADS=1` after initial discovery, and priority failure was recorded. Writes used the file-edit tool. Review `PROOF.md`, `LOG.md` and `REPORT.md` in this folder. No scripts, git, subagents, outside writes, publication or external messages.

What remains uncertain: the order-n radial spike cannot be deleted by a small operator perturbation. Its dynamical effect on the linear prediction still needs proof. The new rate and width condition may be improved, but neither supplies a positive double-descent example. No risk-derivative convergence or control of late finite-sample extrema is claimed.

Next worker: with `A=XX^T/(4d)+cI`, prove or refute

\[
 \sup_{t\geq0}\left\|\frac{X^T}{4d}
 [H_t(A+\mu_d aa^T)-H_t(A)]y\right\|\to0
 \quad\text{in probability}
\]

for the stated centered Gaussian teacher/noise law. A separate argument is needed for time derivatives near the initial order-1/n layer. If spike removal holds, use Gaussian quadratic-form concentration and the standard sample-covariance spectral law to derive the actual ReLU risk limit; the earlier isotropic MP profile has only one minimum. A positive double-descent construction must use a mechanism beyond that particular profile.

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 09:03 Asia/Tbilisi.
