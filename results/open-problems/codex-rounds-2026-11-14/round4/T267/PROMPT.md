# Open problem T267: Epoch-wise double descent

Statement: Epoch-wise double descent for networks. Fix a two-layer network of width m with a stated activation, trained by full-batch gradient flow from a stated initialization on n samples, Gaussian inputs in dimension d, labels from a teacher plus noise of variance s^2 (or labels flipped with probability p), in a stated limit: proportional (n, m, d tending to infinity at fixed ratios) or lazy (m much larger than n). Compute the limiting test risk R(t), the actual risk and not an upper bound, and prove that with probability tending to one R has two local minima and an interior local maximum in t, with the peak time to leading order. Feature learning (both layers trained) and the lazy or random-features regime are separate statements. Linear models with features learned at different speeds already show the effect (Heckel and Yilmaz; Pezeshki et al.) and do not answer the question.

Caveat: Linear models with features of very different scales show the effect (Heckel and Yilmaz 2020, to verify); the question is for networks.

Source: P. Nakkiran, G. Kaplun, Y. Bansal, T. Yang, B. Barak and I. Sutskever, Deep Double Descent: Where Bigger Models and More Data Hurt, arXiv:1912.02292 (2019)

Where it stands (checked by us, Nov 2026): Open for networks as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T267 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T267 (read it,
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
VERDICT: PARTIAL proved the actual all-time test-risk limit and one-minimum property for very wide sine random-feature networks

The earlier Marchenko--Pastur surrogate theorem checks out. The new result establishes a network-to-surrogate passage for the genuinely nonlinear activation `sin`, with independent standard Gaussian inputs and first-layer weights, a Gaussian random linear teacher of energy E, independent Gaussian label noise of variance s^2, zero output initialization, and only the output layer trained. The limit is `d/n -> gamma in (0,infinity)` and `m/n^2 -> infinity`. The width condition is sufficient, not asserted sharp. No explicit regularization is added to the network.

`PROOF.md`, equation (8), gives an explicit integral for the limiting **actual realized-sample test risk**. Equation (9) proves convergence in probability uniformly over every training time `t>=0`, for the risk and its first two derivatives. The constants are `q=exp(-1)` and `c=(1-exp(-2))/2-exp(-1)>0`; the spectral law is the correctly scaled Marchenko--Pastur law. The noise coefficient in the risk is `q*s^2`. Time is for the half-sum squared loss; for the averaged loss, divide its training time by n.

The limit is strictly decreasing when `E>0` and `q*s^2<=E*c`. When `E>0` and `q*s^2>E*c`, it has exactly one nondegenerate interior minimum. The zero-signal cases are treated separately. Thus this limiting nonlinear random-feature network has no double descent. The unique minimum transfers to the finite network on any fixed interval containing it, with probability tending to one. The all-time absolute convergence does not exclude extra finite-sample extrema whose times diverge.

What is new beyond the earlier report: its conclusion concerned an explicitly postulated spectral curve. This result derives such a curve from an actual finite-width nonlinear network, proves concentration for realized teacher/noise samples, controls the test prediction in the needed operator norm, and controls all training times. It changes the activation to make the missing reduction tractable. It does not validate the ReLU reduction left open in that report. No claim of priority over the general kernel-regression literature is made.

The proof uses the exact sine covariance kernel, an elementary cubic-remainder estimate, bounded-feature sampling estimates, Gaussian quadratic-form concentration, and the standard Gaussian sample-covariance limit. The latter is the classical theorem of V. A. Marchenko and L. A. Pastur, *Distribution of eigenvalues for some sets of random matrices*, Math. USSR-Sb. 1:4 (1967), 457--483 ([paper](https://www.mathnet.ru/eng/sm4101)). The previous density-ratio proof is reproduced with the new scaling, rather than assumed to apply unchanged.

The five-minute literature check found no opened source establishing the requested double-descent theorem. Antoine Bodin and Nicolas Macris, *Model, sample, and epoch-wise descents: exact solution of gradient flow in the random feature model*, arXiv:2110.11805, explicitly leave a concentration hypothesis unproved ([paper](https://proceedings.neurips.cc/paper/2021/file/b4f8e5c5fb53f5ba81072451531d5460-Paper.pdf), Section 2.3). Reinhard Heckel and Fatih Furkan Yilmaz, *Early Stopping in Deep Networks: Double Descent and How to Eliminate it*, arXiv:2007.10099, give a network risk upper bound in Theorem 2 ([paper](https://arxiv.org/pdf/2007.10099)). This search is not a proof that the full problem remains open.

Verification was analytic. Independently re-derived the earlier derivative and dilation Jacobian; checked the sine constants using Gaussian integration by parts and feature variance; checked first and second risk derivatives from the parameter ODE and the spectral formula; checked spectral moments using exact Gaussian matrix traces; checked sixth moments using conditioning and a moment generating function; checked the radial test estimate using a Lipschitz bound and an exact chi-square Laplace transform. Singular aspect ratio, spectral null space, zero noise, zero signal, and the threshold equality are included. No numerical program, simulation, or empirical curve is asserted. The startup recall command reported that lowering priority was not permitted; no numerical experiment followed.

Commands and artifacts: read-only `rg --files`, `cat` of the earlier REPORT.md, LOG.md, PROOF.md, and ancestral scripts; web queries and opened sources are in `LOG.md`. Files were written with the file-edit tool. Review from this folder with `cat REPORT.md`, `cat PROOF.md`, and `cat LOG.md`. No git, subagents, or external publication was used.

What failed or remains uncertain: a naive Hilbert--Schmidt estimate for the full radial test error is too weak; rotational invariance supplies the stronger operator bound used in the proof. The cubic argument does not cover ReLU's constant and quadratic components. The theorem does not cover proportional width, the full condition `m/n -> infinity` alone, nonzero output initialization, feature learning, or arbitrary teacher distributions. No positive double-descent construction or peak time is proved. Potential late finite-sample extrema remain uncontrolled in relative size and sign.

Next worker: use Sections 3--6 as a checklist for the actual ReLU reduction, retaining its constant/radial and quadratic components and proving a test-operator estimate rather than just a training-kernel approximation. Alternatively, for a positive lazy-network construction, move to proportional width or a different teacher/spectrum and prove three strict derivative sign changes; another scan of this isotropic sine/MP model cannot produce the target limiting peak. Improving the sufficient width condition here is possible work, but it would not by itself construct double descent.

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15, approximately 03:43 Asia/Tbilisi.
