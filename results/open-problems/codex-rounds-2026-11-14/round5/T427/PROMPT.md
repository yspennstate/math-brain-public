# Open problem T427: The second-order term in the two-dimensional random matching problem

Statement: Let X1,...,Xn be iid uniform points in the unit square, mu_n=(1/n)sum_i delta_Xi, and let lambda be uniform probability measure on the square. Does c_square=lim_{n to infinity}[n E W_2(mu_n,lambda)^2-(log n)/(4 pi)] exist as a finite number, and what is its value?

Caveat: The two-empirical-sample problem has a different leading coefficient. No unchecked predicted numerical value is asserted.

Source: Ambrosio-Stra-Trevisan, A PDE approach to a 2-dimensional matching problem (arXiv:1611.04960); Ambrosio-Glaudo, Finer estimates (arXiv:1810.07002); Caracciolo et al. (arXiv:1402.6993).

Where it stands (checked by us, Nov 2026): The leading logarithmic term is proved. Finer error estimates and nonconstant-density leading asymptotics do not identify the finite semidiscrete next-order constant. The heuristic source does not constitute a proof of this limit.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T427 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T427 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T427 (read it,
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
VERDICT: PROVED a sharper equal-mass flat-grid subdivision bound O(n^(-1/60) log(en)^(11/10))

The earlier spectral result holds. An independent Dirichlet-beta Laurent expansion, checked numerically both by contour differentiation and a Gamma-function identity, gives h_Q approximately 0.004022236572742278. Its difference from the earlier H_5 is positive and below that formula's proved truncation bound. The earlier script also reran successfully. No update beyond the already cited preprint was found in the five-minute literature check.

New beyond round 3: [PROOF.md](PROOF.md) proves, for equal empirical masses on the unit square or flat torus, at t=n^(-5/6),

\[
\left|d_n^\Omega(t)-\mathbb E d_K^Q(m^2t)\right|
\le Cn^{-1/60}\log(en)^{11/10},
\qquad K\sim\operatorname{Bin}(n,m^{-2}),\quad m\in\{1,2,3\},
\]

where d_n^Omega(t)=n E W_{2,Omega}^2(P_t^Omega nu_n,nu_n) and d_0=0. A stronger bound for the expected absolute difference of the random global and cellwise costs is proved as well. This improves the equal-mass O(n^(-1/120) log n) estimate in Lemma 4.1 of Yunzong Xu, *Random Matching Between Distinct Distributions in Two Dimensions*, [arXiv:2610.40509v1](https://arxiv.org/html/2610.40509v1#S4.SS1). It refines that repair method; no claim of a new method is made.

The improvement comes from delta^2=A log(en)/(nt) and collar width r=(delta^2)^(1/5). The proof derives the rough expected cost directly, reconstructs the optimal-potential estimate, preserves each cell's mass during repair, and controls the replacement of global heat by cellwise heat. It uses basic quadratic transport facts, Gaussian heat kernels, iid covariance, and Bernstein concentration, without assuming a matching asymptotic theorem. The case m=1 includes the torus seam and hence the square–torus comparison.

Reproduction commands, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_zeta.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_scaling.py
```

Both exited 0. The numerical script took about 3.3 seconds and less than 20 MB peak RSS; the exact rational exponent check took below 0.1 seconds and less than 14 MB. The priority wrapper printed a warning, but both scripts checked actual niceness 20 before computation. All calculations used one thread, no GPU, and explicit CPU limits. [LOG.md](LOG.md) contains complete relevant output and the earlier-script command.

Attempts to break the argument checked the interpolation singularity at its atomic endpoint, covariance before event restriction, empty cells, small n, grid intersections, discontinuous cellwise densities, the m=1 seam, and exact conditional rescaling. All load-bearing exponents were obtained a second way. No mathematical counterexample was found. A draft Gamma-expression factor was corrected algebraically before execution; two small patch-context failures were corrected. A shortcut to t=n^(-2/3) was rejected because the global heat comparison would no longer decay by a power of n.

Limits and uncertainty: this proves subdivision, not the complete second-order matching theorem. The semidiscrete-to-smoothing reduction remains unaudited here, as do the curved-surface extensions. The numerical h_Q comparison is not interval arithmetic. No value of beta_sd or c_square is asserted. The cited preprint still states existence with c_square=beta_sd+h_Q, as the earlier reports recorded.

Next worker: audit the equal-mass semidiscrete-to-smoothing reduction in Proposition 3.1 and its Appendix B proof, especially the quantitative linearization error. The flat-grid repair now has a detailed derivation and a sharper bound. Evaluating beta_sd would still require additional analysis or a controlled semidiscrete computation with a finite-size error bound.

Task: “take the NEXT checkable step on this problem, building on that work.” Recorded session clock: 15 November 2026, 06:41:19 Asia/Tbilisi (02:41:19 UTC).
