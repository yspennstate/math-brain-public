# Open problem T248: Edge universality for the conjugate kernel of a random network

Statement: Conjugate kernel of a one-layer random network: Y = sigma(W X / sqrt d), W m x d with iid N(0, 1) entries, X d x N with iid sub-Gaussian entries (or columns uniform on the sphere of radius sqrt d), m, d, N tending to infinity proportionally. Take sigma Lipschitz (or smooth), centred, with no linear part: E sigma(Z) = 0 and E Z sigma(Z) = 0 for Z ~ N(0, 1). Prove that lambda_max(Y Y^T / N) converges to the right edge of the limiting (Pennington-Worah) law, which is regular there, with Tracy-Widom (beta = 1) fluctuations on the n^(-2/3) scale. Then allow a linear component, which changes the bulk: state an explicit rule for any finite-rank spikes it or the input design creates and prove the same edge statement for the largest eigenvalue after them. For polynomial activations of degree at least 3 the top eigenvalue at widths below several thousand is an outlier made by the largest entry of Y, so the statement is asymptotic only.

Caveat: The global law is known; the edge and fluctuations are the open part. Outliers come from the mean and the linear Hermite component of sigma.

Source: L. Benigni and S. Péché, Eigenvalue distribution of nonlinear models of random matrices, arXiv:1904.03090 (2019); Z. Fan and Z. Wang, Spectra of the Conjugate Kernel and Neural Tangent Kernel for linear-width neural networks, arXiv:2005.11879 (2020)

Where it stands (checked by us, Nov 2026): Global laws proved. Benigni and Péché (arXiv:2201.04753) prove that the largest eigenvalue converges in probability to the same limit as for an information-plus-noise matrix, with a phase transition depending on the activation and the entry laws. Tracy-Widom fluctuations at the edge are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T248 (read it,
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
VERDICT: PARTIAL found a new edge-universality theorem relevant to T248; full statement not verified

The literature check found Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form concentration*, [arXiv:2610.41416v2](https://arxiv.org/abs/2610.41416v2), revised 4 November 2026. Theorem 1.3 and Corollary 1.4 establish TW1 edge fluctuations for independent centered vectors with dependent coordinates under quadratic-form concentration and uniform covariance-edge regularity. This substantially advances the status supplied in the prompt. As instructed, the session stops at the literature stage.

[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) records the exact hypotheses, normalization, and conditional random-feature application. For fixed spherical-norm designs, centered Lipschitz activations give independent centered feature rows conditional on X, and bounded input operator norm gives the needed concentration. The remaining requirements concern the conditional covariance. The relevant sample count after transposing Y is m, not N; translating the theorem back multiplies eigenvalues by m/N.

Also opened: Renyuan Ma and Theodor Misiakiewicz, *The anisotropic local law for sample covariance matrices under quadratic-form concentration*, [arXiv:2609.09440v2](https://arxiv.org/abs/2609.09440v2). Its Proposition 2.8 and Example 2.11 explicitly support the concentration route for Lipschitz random features. Benigni–Péché arXiv:2201.04753v1 and Fan–Wang arXiv:2005.11879 were opened for context.

Checks against overclaiming: inspected the full theorem statements, rather than relying on abstracts; independently checked the Gram-matrix rescaling by singular values and by the identity YᵀY/N=(m/N)(YᵀY/m); checked the fixed-norm Gaussian marginals needed for exact conditional centering; distinguished dimension-uniform moment concentration from stochastic domination with a growing loss. The explicit exceptions and unresolved steps are listed in SOLVED_ELSEWHERE.md.

What was not proved: the full T248 assertion; deterministic edge centering for random designs at the TW scale; edge universality after arbitrary finite-rank outliers; the polynomial-activation extension; or aspect ratio one under the newly found theorem. The new papers were inspected for their statements and applicability, not independently re-proved or fully refereed.

Commands and search queries are in [LOG.md](LOG.md). No numerical experiment was run and no computation data file was produced. One tiny file-writing command used `OMP_NUM_THREADS=1 nice -n 15 python3`; the sandbox printed `nice: setpriority: Operation not permitted` but continued the file write. No further Python or numerical programs were launched. Subsequent document writes used the patch tool.

Next worker: first exploit the conditional theorem for spherical inputs and Lipschitz activations with the first three Hermite coefficients zero. Verify covariance regularity and control its finite-size edge, then address a nonzero second coefficient, critical/supercritical spikes, and conditional means for non-normalized designs. Do not label the complete original problem solved on the strength of the covariance theorem alone.

Task: “push this problem forward by one checkable piece” — 14 November 2026, first session clock reading 22:08:29 +04.
