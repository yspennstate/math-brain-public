# Open problem T224: Uniform-in-time weak mean-field rates when noiseless training converges slowly

Statement: In the two-layer mean-field gradient-flow model of arXiv:2605.22010, initialize m neurons iid from the same law as the limiting flow and use the paper’s regularity assumptions. Suppose its excess population MSE L_t<=C(1+t)^{-c}, with 0<c<=2, so that integral_0^infinity sqrt(L_t)dt need not be finite. Does this decay assumption alone imply sup_{t>=0} E||f_{rho_t^m}-f_{rho_t}||_{L^2(P_X)}^2<=poly(d)m^{-a(c)} for some a(c)>0? Determine the sharp exponent, or exhibit the missing stability hypothesis/counterexample.

Caveat: This is an output L^2 weak error, not Wasserstein distance between a discrete empirical measure and a continuous parameter law. The source theorem is not restated as an open problem.

Source: Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks (arXiv:2605.22010); Mei-Montanari-Nguyen (arXiv:1804.06561).

Where it stands (checked by us, Nov 2026): 2605.22010 already proves noiseless uniform-in-time weak propagation of chaos using quantitative convergence and an integrable square-root-loss condition. It does not give the proposed statement merely from a slow, possibly nonintegrable loss decay.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T224 (read it,
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
VERDICT: PARTIAL uniform weak logarithmic rate and a sufficient curvature condition for polynomial rates

For Euclidean population gradient flow with fixed second-layer coefficients and bounded smooth features, PROOF.md proves

\[
\sup_{t\ge0}\mathbb E\|f_t^m-f_t\|_{L^2(P_X)}^2
\le \frac{4K(1+T)^4e^{2H(T)}}m+6L_T\qquad(T\ge1).
\]

Here the feature map and its first two derivatives have uniform bounds A, B, M, the explicit K is given in (4), and H(T) is the integrated positive part of the worst negative residual curvature, defined in (3). The initialization is iid from the mean-field initial law.

Consequently, for 0<c<2, the loss envelope alone gives

\[
\sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
=O_{A,B,M,C,c}\big((\log m)^{-2c/(2-c)}\big).
\]

A concrete sufficient extra hypothesis is

\[
H(T)\le h_0+\kappa\log(1+T).
\]

It gives an explicit polynomial bound with exponent c/(c+4+2kappa). If h0=O(log d), kappa is dimension independent, and the feature derivative bounds are dimension independent, the prefactor is polynomial in d (also allowing a polynomial loss-envelope constant C). Neither this exponent nor the logarithmic exponent is claimed sharp.

The proof retains the positive Jacobian-square term in the empirical-risk Hessian, controls the nonlinear coupling remainder by stopping at RMS discrepancy 1/T, and bounds the bad event using an integrated iid output fluctuation. Monotonicity of both population losses then controls all later times. The result is sup_t E error squared, not E sup_t error squared.

The source's Euclidean bounded-total-variation activation assumptions give bounded features and derivatives, so this includes that subclass. It does not include the population-data relaxation to unbounded activations, sphere-constrained dynamics, trained second-layer coefficients, sample error, or time discretization.

Literature check: the November 11 source revision already treats c=2 in Remark 6; see SOLVED_ELSEWHERE.md. The source authors are Margalit Glasgow and Joan Bruna, arXiv:2605.22010. The full problem was not found settled, so the session continued for c<2. This is a correction to endpoint coverage in the supplied status, not a claim that the source theorem is a new open problem.

Verification command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit.py
```

Output and data: audit_results.json; exact command and output summary: LOG.md. The audit passed 200 independent Hessian/coupling cases, 200 checks of the constant/stopping threshold, and 15 exact rational exponent balances. Maximum Hessian errors were 7.28e-8 from scalar-risk second differences and 1.51e-9 from gradient differences. These checks supplement the written proof; they are not an infinite-time simulation. The program uses only the Python standard library, runs in well under one second, and has negligible memory use. The inherited process priority was independently read as nice 20, despite the wrapper's harmless setpriority warning.

What failed or remains uncertain: no counterexample was constructed, and no polynomial rate was derived from slow loss decay alone. The curvature condition is sufficient and can be stronger than necessary. The constants and horizon threshold deteriorate as c approaches 2. There is no sharpness or necessity claim and no uniform estimate in c at that endpoint. The qualitative mechanism resembles truncation arguments already present in the source; no claim of literature novelty is made for this rate without a wider search.

Next worker: seek output-level cancellations beyond the global residual-curvature bound. Alternatively, build an admissible bounded smooth example with polynomial loss decay and enough accumulated negative curvature to amplify iid initialization fluctuations into output error larger than every inverse power of m. Parameter separation alone would not give the needed counterexample. A useful intermediate task is to replace the global supremum in h(t) by a rigorously controlled quantity along the sampled trajectories without introducing m-dependent constants.

Task: “push this problem forward by one checkable piece” — 2026-11-14 21:21 Asia/Tbilisi.
