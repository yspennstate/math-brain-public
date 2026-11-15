# Open problem T224: Uniform-in-time weak mean-field rates when noiseless training converges slowly

Statement: In the two-layer mean-field gradient-flow model of arXiv:2605.22010, initialize m neurons iid from the same law as the limiting flow and use the paper’s regularity assumptions. Suppose its excess population MSE L_t<=C(1+t)^{-c}, with 0<c<=2, so that integral_0^infinity sqrt(L_t)dt need not be finite. Does this decay assumption alone imply sup_{t>=0} E||f_{rho_t^m}-f_{rho_t}||_{L^2(P_X)}^2<=poly(d)m^{-a(c)} for some a(c)>0? Determine the sharp exponent, or exhibit the missing stability hypothesis/counterexample.

Caveat: This is an output L^2 weak error, not Wasserstein distance between a discrete empirical measure and a continuous parameter law. The source theorem is not restated as an open problem.

Source: Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks (arXiv:2605.22010); Mei-Montanari-Nguyen (arXiv:1804.06561).

Where it stands (checked by us, Nov 2026): 2605.22010 already proves noiseless uniform-in-time weak propagation of chaos using quantitative convergence and an integrable square-root-loss condition. It does not give the proposed statement merely from a slow, possibly nonintegrable loss decay.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T224 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T224 (read it,
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
VERDICT: PARTIAL improved curvature-dependent polynomial weak rate using an output cancellation

The earlier bounded-feature Euclidean result holds. An independent direct coupling derivation recovers its main inequality, and rerunning its audit reproduces its results.

The new result improves its finite-horizon factor from \((1+T)^4\) to \((1+T)^2\). With exactly the same notation and assumptions—bounded smooth features \(\phi\), bounded first and second derivatives with constants \(A,B,M\), fixed output coefficients, population gradient flow, and iid initialization—PROOF.md establishes

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le \frac{4K_*(1+T)^2e^{2H(T)}}m+6L_T,
 \qquad K_*=2A^2+4A^2B^2+2M^2A^4.
\]

Here \(H\) is the integrated positive part of the worst negative mean-residual curvature, as defined precisely in PROOF.md. Thus, if

\[
 L_t\le C(1+t)^{-c},\qquad H(T)\le h_0+\kappa\log(1+T),
\]

then for \(m\ge2^{c+2+2\kappa}\),

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le (4K_*e^{2h_0}+6C)m^{-c/(c+2+2\kappa)}.
\]

The previous exponent was \(c/(c+4+2\kappa)\). For example, \(c=1,\kappa=0\) improves from \(1/5\) to \(1/3\). The new constant is polynomial in the feature bounds; the old constant included an exponential in those bounds. Consequently the prefactor is polynomial in \(d\) if \(A,B,M,C\) are, \(h_0=O(\log d)\), and \(\kappa\) is dimension independent. Neither exponent is claimed sharp.

The new step keeps the negative output-error square in the exact paired-particle energy identity. For squared RMS parameter discrepancy \(y\), iid output fluctuation norm \(\eta_t\), and residual-curvature bound \(h(t)\), completing the square gives

\[
 y'\le2h(t)y+\eta_t^2+\frac{M^2}{4}y^2.
\]

A reciprocal Riccati comparison, a first-moment bound on \(\int_0^T\eta_t^2dt\), and the bounded output cap control the exceptional initializations. Population-loss monotonicity handles all later times. The conclusion is the requested output norm with the supremum outside expectation, and makes no empirical-measure Wasserstein claim.

Verification commands, run from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114/briefs/T224/audit.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_cancellation.py
```

Both passed. The new audit checks 600 bounded-feature vector-field identities, 300 exact rational cancellation cases, 300 exact scalar Riccati solutions, 300 exact constant cases, and 18 exact exponent balances. Maximum direct-identity error was \(7.11\times10^{-15}\); maximum completed-square error was \(3.55\times10^{-15}\). An exact local equality case independently checks the Riccati coefficient. These supplement the proof, rather than simulate infinite-time convergence. Actual nice was 20, peak RSS below 17 MB, and each audit finished in under one second. Outputs are audit_results.json and cancellation_results.json; commands and details are in LOG.md.

The literature check took under five minutes and found no later settlement. Margalit Glasgow and Joan Bruna, *Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks*, [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3), remains the current source revision, dated 11 November 2026. Remark 6 covers \(c=2\); Section 6 still leaves \(c<2\) open. No full-settlement SOLVED_ELSEWHERE.md was created.

What failed or remains uncertain: inserting only the slow loss envelope into this improved estimate still yields the earlier logarithmic rate \((\log m)^{-2c/(2-c)}\), rather than a polynomial width rate. The extra curvature hypothesis remains sufficient, with no necessity claim. There is no counterexample and no sharp exponent for the original problem. The proof retains the earlier limitations: unbounded activations, sphere constraints, trained output coefficients, finite training data, and discretization are not covered. No literature-priority claim is made for the improved bound.

Next worker: exploit the same exact identity before discarding the negative output square, to seek an estimate on output error that avoids controlling the global parameter discrepancy on rare initializations. A concrete alternative is to replace Markov's exceptional-event estimate with a concentration bound for the time-integrated iid fluctuation; that may sharpen the conditional polynomial rate, but would not by itself remove the exponential dependence on \(H(T)\). To settle decay alone, a further output-level stability estimate or an admissible output-error counterexample is still needed.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 03:32 Asia/Tbilisi (recorded shell clock).
