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
VERDICT: PARTIAL proved an all-time test-risk reduction for very wide uncentered ReLU random-feature networks

The preceding sine-network theorem checks out. The new piece proves the ReLU test-operator estimate that the previous report left open, retains the radial mode explicitly, and applies the estimate to the actual finite-width output-layer gradient flow. The model has standard Gaussian inputs and first-layer weights, zero output initialization, a Gaussian random linear teacher of energy E, independent Gaussian noise of variance s^2, d/n tending to a fixed positive ratio, and m/n^2 tending to infinity. The first layer is fixed.

Write K_m for the original nonlinear training kernel and b_m(t)=integral_0^t exp(-u*K_m)y du. Equation (6) of PROOF.md proves

\[
 \sup_{t\geq0}\left|R_m(t)-s^2-
 \left\|X^Tb_m(t)/(4d)-\beta\right\|^2\right|
 \longrightarrow0\quad\text{in probability}.
\]

This concerns actual realized-sample risk. It also holds for the infinite-width ReLU kernel flow. It is not a deterministic limiting risk formula: the nonlinear training matrix remains inside b_m(t). No two-minimum theorem, peak time, or feature-learning result is proved.

The main lemma controls the test-prediction operator and is valid for every fixed nonzero design. The infinite-width test kernel is exactly its linear part Xx/(4d), plus a rank-one radial part mu_d*a*a(x), plus an orthogonal even remainder. Here a_i=||x_i||/sqrt(d), a(x)=||x||/sqrt(d), and

\[
 \mu_d=d\left[\frac{\Gamma(d/2)}{2\sqrt\pi\Gamma((d+1)/2)}\right]^2
 =\frac1{2\pi}+\frac1{4\pi d}+O(d^{-2}).
\]

The remainder has test-operator norm O_P(1/d). The centered quadratic component is controlled by an exact spherical covariance and Schur contraction; a Hilbert--Schmidt estimate would lose the necessary factor. Equation (4) gives the explicit deterministic bound. Equation (17) gives an exact orthogonal decomposition of the infinite-width realized risk for arbitrary coefficients.

To apply the lemma along the full flow, the proof uses the positive fourth-order ReLU kernel coefficient 1/(48*pi) to establish a fixed bulk spectral gap without discarding the quadratic training term. Finite-width Gaussian moment estimates then suffice under m/n^2 tending to infinity. A rank-one inverse identity and a Gaussian grid argument show that the radial prediction is uniformly O_P(sqrt(log(n)/n)). Risk derivatives are not controlled.

Verification was analytic. Independently re-derived the predecessor's sine constants, noise scaling, risk derivative and density-dilation argument. For the new result, independently checked the ReLU coefficients, exact radial mean, spherical fourth/eighth moments, finite-width moment constants, inverse-vector scale, and both ends of the time-uniform argument. The adversarial checks show why deleting the radial term at operator level is false and why radial labels y=a would invalidate its disappearance along the flow. Zero signal/noise and every fixed positive aspect ratio are covered. No numerical program or simulation was run.

The literature check closed within five minutes. The opened paper by Antoine Bodin and Nicolas Macris, *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, arXiv:2110.11805, retains an unproved concentration hypothesis ([paper](https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf), Section 2.3). The other opened sources and exact queries are in LOG.md. No inspected source establishes the requested theorem; this short search does not certify that it remains open.

Commands and artifacts: read both predecessor folders' REPORT.md, LOG.md and PROOF.md and the four ancestral Python scripts read-only. No scripts occur in the predecessor folders themselves. All derivations, checks and the failed shortcuts are in PROOF.md and LOG.md. Review with `cat PROOF.md`, `cat LOG.md`, and `cat REPORT.md` from this folder. All writes stayed here. No git, subagents, publication or external messages.

What failed or remains uncertain: deleting the constant/radial kernel term before controlling the flow is invalid; estimating the quadratic test component only in Hilbert--Schmidt norm is insufficient. The result retains the degree-two nonlinear training matrix. It does not prove a training-kernel deterministic equivalent, risk-derivative convergence, a sharper width threshold, proportional-width behavior, or either positive double-descent statement in T267.

Next worker: prove the operator approximation for the centered quadratic **training** Gram matrix, retaining its diagonal and radial rank-one terms. Then control the large radial eigenvalue in the coefficient dynamics and replace K_m inside the linear predictor of (6). The test-side estimate, bulk gap and radial-prediction control here can be reused. Uniform derivative statements need separate treatment of the initial time layer caused by the radial eigenvalue of order n. Do not assume (6) already implies the earlier MP risk formula.

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 06:30 Asia/Tbilisi.
