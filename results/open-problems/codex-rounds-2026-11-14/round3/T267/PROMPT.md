# Open problem T267: Epoch-wise double descent

Statement: Epoch-wise double descent for networks. Fix a two-layer network of width m with a stated activation, trained by full-batch gradient flow from a stated initialization on n samples, Gaussian inputs in dimension d, labels from a teacher plus noise of variance s^2 (or labels flipped with probability p), in a stated limit: proportional (n, m, d tending to infinity at fixed ratios) or lazy (m much larger than n). Compute the limiting test risk R(t), the actual risk and not an upper bound, and prove that with probability tending to one R has two local minima and an interior local maximum in t, with the peak time to leading order. Feature learning (both layers trained) and the lazy or random-features regime are separate statements. Linear models with features learned at different speeds already show the effect (Heckel and Yilmaz; Pezeshki et al.) and do not answer the question.

Caveat: Linear models with features of very different scales show the effect (Heckel and Yilmaz 2020, to verify); the question is for networks.

Source: P. Nakkiran, G. Kaplun, Y. Bansal, T. Yang, B. Barak and I. Sutskever, Deep Double Descent: Where Bigger Models and More Data Hurt, arXiv:1912.02292 (2019)

Where it stands (checked by us, Nov 2026): Open for networks as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T267 (read it,
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
VERDICT: PARTIAL proved one-minimum property of the isotropic Marchenko--Pastur surrogate at every aspect ratio

`PROOF.md` proves that the explicit spectral risk curve used in prior T267 work cannot exhibit epoch-wise double descent, for every positive aspect ratio and every nonnegative ridge parameter. This removes the earlier requirement that the rate spectrum and its doubled spectrum be disjoint. If signal energy E>0 and s^2/4>Ec, there is exactly one nondegenerate interior minimum; otherwise the profile decreases throughout. Zero signal is handled separately.

The new step is an elementary density-ratio argument. The MP-weighted rate density is proportional to sqrt((b-k)(k-a))/k. Comparing it with its dilation by two proves that the signed density representing the risk derivative has exactly one sign change. Its Laplace transform consequently has exactly one zero. The proof includes an exact finite-sample surrogate-risk derivation, an independent ODE check of its derivative, and an independent initial-slope calculation. An exact two-atom counterexample in the audit shows that the conclusion fails for arbitrary spectral measures; the MP shape is essential. The singular critical-ratio case, zero ridge, null eigenvalues, zero signal, and zero noise are checked explicitly.

This is a theorem about the stated surrogate curve, not the nonlinear network asked for in T267. No feature-learning result, realized-sample high-probability shape theorem, network test-risk limit, or peak time is claimed. In particular, the prior note's conclusion that anisotropy is necessary for lazy-network double descent did not follow from its restricted proof and numerical search. The present result removes the spectral-profile gap but does not repair the separate network-limit gap.

The literature search took less than ten minutes. No opened reference supplied the full requested theorem. The closest prior work was Antoine Bodin and Nicolas Macris, *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, arXiv:2110.11805, NeurIPS 2021: https://arxiv.org/abs/2110.11805 . Their full paper explicitly leaves a concentration hypothesis unproved. Reinhard Heckel and Fatih Furkan Yilmaz, *Early Stopping in Deep Networks: Double Descent and How to Eliminate it*, arXiv:2007.10099, https://arxiv.org/abs/2007.10099 , give a network risk upper bound in Theorem 2. These are not a proof of the target statement. The other opened references and the search queries are recorded in `LOG.md`. A short search does not establish that the problem remains open.

Commands and artifacts: no numerical computation was required. The exact read-only orientation commands and web queries are recorded in `LOG.md`; edits used the file-edit tool. Review with `cat PROOF.md` and `cat LOG.md` from this folder. The attempt to invoke the startup recall under `OMP_NUM_THREADS=1 nice -n 15` reported that priority adjustment was not permitted, so no numerical experiment was launched. No git, subagents, or external publication was used.

What failed or remains uncertain: the network-to-surrogate reduction has not been established here. Constant/radial kernel modes, the actual initialization, and teacher/noise concentration require separate control. Compact-time convergence alone would not rule out extrema at times diverging with dimension. The result should not be cited as a solution to either the lazy-network or feature-learning version of T267.

Next worker: establish or refute the actual isotropic ReLU random-feature test-risk deterministic equivalent, with the constant and radial components retained and with enough derivative control to transfer a risk-shape statement. Alternatively, seek a network mechanism outside this isotropic MP profile. Do not repeat a scan of the old unresolved aspect-ratio interval; the profile question on that interval is now proved.

Task: "push this problem forward by one checkable piece" — 2026-11-14, approximately 22:09 Asia/Tbilisi.
