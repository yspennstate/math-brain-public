# Open problem T427: The second-order term in the two-dimensional random matching problem

Statement: Let X1,...,Xn be iid uniform points in the unit square, mu_n=(1/n)sum_i delta_Xi, and let lambda be uniform probability measure on the square. Does c_square=lim_{n to infinity}[n E W_2(mu_n,lambda)^2-(log n)/(4 pi)] exist as a finite number, and what is its value?

Caveat: The two-empirical-sample problem has a different leading coefficient. No unchecked predicted numerical value is asserted.

Source: Ambrosio-Stra-Trevisan, A PDE approach to a 2-dimensional matching problem (arXiv:1611.04960); Ambrosio-Glaudo, Finer estimates (arXiv:1810.07002); Caracciolo et al. (arXiv:1402.6993).

Where it stands (checked by us, Nov 2026): The leading logarithmic term is proved. Finer error estimates and nonconstant-density leading asymptotics do not identify the finite semidiscrete next-order constant. The heuristic source does not constitute a proof of this limit.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T427 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T427 (read it,
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
VERDICT: PROVED an explicit convergent formula and truncation bound for the square spectral finite part h_Q

The earlier report's statement-level deduction from Yunzong Xu's [arXiv:2610.40509v1](https://arxiv.org/abs/2610.40509v1) holds: its theorem implies c_square=beta_sd+h_Q. No later result changing that picture was found in the literature check, completed within three minutes. The full matching proof remains unaudited.

New beyond that report: [PROOF.md](PROOF.md) evaluates the previously unevaluated geometric limit h_Q by an explicit positive, exponentially convergent series H_M. It proves

\[
0\leq h_Q-H_M\leq
\frac{4e^{-\pi(M+1)^2}}
{\pi^2(M+1)^2(1-e^{-\pi})(1-e^{-\pi(2M+3)})}.
\]

Already M=3 gives error below 10^(-21). Independent numerical formulas give

\[
h_Q\approx0.004022236572742278.
\]

The proof derives the formula from the Neumann heat trace, checks the heat-to-zeta finite-part conversion, and independently counts the square–torus boundary correction and omitted lattice shells. A second approximation uses the original quadrant eigenvalue sum with an explicit remainder. This is a new deliverable relative to the earlier folder, not a claim that the underlying spectral calculation is new in the literature.

Reproduce the numerical checks with

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_spectral.py
```

Both runs exited 0. H_3 has analytic tail bound 3.91564898356e-24; H_5 agrees with the independently corrected heat sum within its analytic error bound 1.39401977209e-46. The environment printed a priority-change warning, but the guard verified actual niceness 20 before computation. Measured peak resident memory was 19,562,496 bytes. Complete output is in [LOG.md](LOG.md).

What failed or remains uncertain: no mathematical counterexample was found. Full validation of Xu's subdivision proof and evaluation of beta_sd remain open in this work. Numerical rounding was checked by agreement, not certified by interval arithmetic; the exact series and its proved truncation bound are the rigorous result. No numerical value of c_square is asserted.

Next worker: focus on the equal-mass smoothing constant beta_sd=kappa_equal+log(2)/(4 pi), especially Theorem 4 and Appendix C of Xu's paper. The geometric spectral term now has a reproducible evaluator and need not be estimated again. A numerical estimate of kappa_equal would require a controlled semidiscrete solver and finite-size error analysis; the bipartite or Dirichlet constant cannot be substituted.

Task: “take the NEXT checkable step on this problem, building on that work.” Session clock: 15 November 2026, 03:52:56 Asia/Tbilisi (14 November 2026, 23:52:56 UTC).
