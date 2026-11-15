# Open problem T224: Uniform-in-time weak mean-field rates when noiseless training converges slowly

Statement: In the two-layer mean-field gradient-flow model of arXiv:2605.22010, initialize m neurons iid from the same law as the limiting flow and use the paper’s regularity assumptions. Suppose its excess population MSE L_t<=C(1+t)^{-c}, with 0<c<=2, so that integral_0^infinity sqrt(L_t)dt need not be finite. Does this decay assumption alone imply sup_{t>=0} E||f_{rho_t^m}-f_{rho_t}||_{L^2(P_X)}^2<=poly(d)m^{-a(c)} for some a(c)>0? Determine the sharp exponent, or exhibit the missing stability hypothesis/counterexample.

Caveat: This is an output L^2 weak error, not Wasserstein distance between a discrete empirical measure and a continuous parameter law. The source theorem is not restated as an open problem.

Source: Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks (arXiv:2605.22010); Mei-Montanari-Nguyen (arXiv:1804.06561).

Where it stands (checked by us, Nov 2026): 2605.22010 already proves noiseless uniform-in-time weak propagation of chaos using quantitative convergence and an integrable square-root-loss condition. It does not give the proposed statement merely from a slow, possibly nonintegrable loss decay.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T224 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T224 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T224 (read it,
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
VERDICT: PARTIAL improved curvature-dependent uniform weak rates by concentration on iid trajectories

The round 3 result holds. An independent velocity subtraction recovers its energy inequality and constants; rerunning its audit reproduces its results. The new step replaces its Markov estimate on the time-integrated iid output fluctuation by concentration in trajectory Hilbert space. This improves the conditional width exponents under the same additional stability assumption.

In the same bounded-feature Euclidean population-flow setting, write \(A,B,M\) for uniform bounds on \(\phi,D\phi,D^2\phi\), \(L_t=\|f_t-g\|^2\), and

\[
 h(t)=\sup_{w,|u|=1}[-\langle f_t-g,D^2\phi(w)[u,u]\rangle]_+,
 \quad H(T)=\int_0^T h(t)dt,\quad S_T=\int_0^T e^{2H(s)}ds.
\]

PROOF.md establishes, for deterministic \(T\ge1\) and \(m\ge2M^2A^2 T S_T\),

\[
\begin{split}
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le {}&\frac{8A^2+16A^2B^2T e^{2H(T)}}m+6L_T\\
 &+16A^2\exp\!\left(-\frac{m}{4M^2A^2 T S_T}\right).
\end{split}
\]

If \(AM=0\), omit the exponential term and the width condition. This replaces the round 3 term of order \(T^2e^{2H(T)}/m\) by a term of order \(Te^{2H(T)}/m\) plus an exponentially small exceptional-event contribution.

Suppose additionally

\[
 L_t\le C(1+t)^{-c},\qquad H(T)\le h_0+\kappa\log(1+T).
\]

For \(0<c\le1\), the new rate is

\[
 O\!\left(\left(\frac{\log(em)}m\right)^{c/(2+2\kappa)}\right).
\]

For \(c>1\), the new rate is

\[
 O\!\left(m^{-c/(c+1+2\kappa)}\right).
\]

These improve the preceding exponent \(c/(c+2+2\kappa)\). For example, \(c=1,\kappa=0\) improves from \(m^{-1/3}\) to \(\sqrt{\log(em)/m}\); \(c=3/2,\kappa=0\) improves from \(m^{-3/7}\) to \(m^{-3/5}\). Explicit constants and width thresholds are in Corollaries 2 and 3 of PROOF.md. For each fixed \(c,\kappa\), the prefactors are polynomial in \(d\) when \(A,B,M,C\) are polynomial in \(d\), \(h_0=O(\log d)\), and \(\kappa\) is dimension independent. The log-free constant for \(c>1\) deteriorates as \(c\downarrow1\). No exponent or logarithmic factor is claimed sharp.

The key observation is that \(\sqrt{J_T}=\|m^{-1}\sum_i X_i-\mathbb EX_i\|_{L^2([0,T];\mathcal H)}\), where the entire mean-field paths \(X_i(t)=\phi(v_i(t))\) are iid and have norm at most \(A\sqrt T\). Changing one initial neuron changes this scalar norm by at most \(2A\sqrt T/m\). A self-contained bounded-difference proof controls the bad event without assuming temporal independence. The coupling cancellation and loss monotonicity then give the output estimate above. The result concerns the requested output norm with the supremum outside expectation, not a Wasserstein sampling rate.

Verification commands, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T224/audit_cancellation.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_concentration.py
```

Both passed. The new audit checks 48 exact trajectory variances, 488 exact finite-law concentration tails, 179 simplified tails, 3,888 coordinate replacements, 300 exact constant identities, 21 exact exponent cases, 500 logarithmic-rate prefactors, and 263 log-free prefactors. Four complete ordered-sample enumerations independently match the multinomial laws. A separate exact binomial tail agrees with Pascal recursion. The path laws include perfect temporal dependence and the zero case. These are concentration and algebra checks, not simulations of infinite-time neural convergence. Each script ran in under one second, actual nice 20, peak RSS below 17 MB. Full results: cancellation_results.json and concentration_results.json; derivations, commands and outputs: LOG.md.

The literature check, completed within five minutes, found no later settlement. The current source by Margalit Glasgow and Joan Bruna remains [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3), dated 11 November 2026. Remark 6 already handles \(c=2\); Section 6 leaves \(c<2\) open. No full-settlement SOLVED_ELSEWHERE.md was created. No literature-priority claim is made for the new bounds.

What failed or remains uncertain: concentration does not remove the exponential dependence on \(H(T)\). The slow-loss envelope alone still allows \(H(T)=O(T^{1-c/2})\) for \(c<2\), and this argument does not yield a polynomial width rate in that case. There is no admissible counterexample, no necessary stability condition, and no sharp exponent for the original problem. The scope remains bounded features, fixed output coefficients, Euclidean parameters, exact population flow and iid initialization; unbounded activations, sphere constraints, trained output coefficients, finite training data and discretization are not covered.

Next worker: address deterministic output stability rather than further improving iid tails. One concrete target is to retain the negative output square in (14)--(16) of PROOF.md and prove a coercivity estimate controlling the Taylor remainder through output discrepancy along the coupled trajectories. Such a bound would have to hold beyond a parameter-discrepancy stopping threshold and avoid the factor \(e^{2H(T)}\); otherwise this concentration improvement still leaves the decay-only obstruction intact. Alternatively, an admissible example must amplify sampling error in the output, not merely separate parameter trajectories.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 05:06 Asia/Tbilisi (first captured shell clock).
