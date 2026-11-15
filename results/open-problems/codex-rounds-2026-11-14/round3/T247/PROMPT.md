# Open problem T247: The singular-value spectrum of deep network Jacobians in the joint depth-width limit (dynamical isometry)

Statement: Pennington, Schoenholz and Ganguli compute, via free probability, the limiting singular-value distribution of the input-output Jacobian J = Π D_l W_l of a depth-L network with orthogonal or Gaussian weights, assuming asymptotic freeness of the diagonal derivative matrices D_l and the weights W_l, and find 'dynamical isometry' at criticality for orthogonal weights and sigmoid-like activations. Prove the formula and the isometry claim when depth and width tend to infinity jointly (L = L(n) → ∞), not only at fixed depth.

Caveat: At fixed depth asymptotic freeness of the layer Jacobians has been proved (Pastur and Slavin; Collins and Hayase, to verify). The joint limit needs control of errors accumulated over L layers.

Source: J. Pennington, S. S. Schoenholz and S. Ganguli, Resurrecting the sigmoid in deep learning through dynamical isometry: theory and practice, arXiv:1711.04735 (2017)

Where it stands (checked by us, Nov 2026): Fixed-depth freeness proved; joint limit open as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T247 (read it,
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
VERDICT: PARTIAL exact finite-width second moments and joint-limit empirical isometry for independent gates with Haar orthogonal weights

The full nonlinear-network problem remains open in this work. The completed piece is a proof for the independent-gate surrogate, with explicit accumulated width error, in [PROOF.md](PROOF.md). No asymptotic freeness assumption is used in that proof.

Let J = D_L O_L ... D_1 O_1, with independent real Haar O_l and independent diagonal gates. Assume the squared gate entries in layer l are i.i.d., nonnegative, have mean 1, and have variance v_l. Put V = sum_l v_l and Z = Tr((JJ^top-I)^2)/n. The exact formula is

\[
\mathbb E Z=\frac{n+2}{3}
\left[\prod_{l=1}^L\left(1+\frac{3v_l}{n+2}\right)-1\right].
\]

Also E Tr(JJ^top)/n = 1, and the variance of that empirical mean is E Z/n. The deviation from the free second-moment prediction is bounded by

\[
0\leq\mathbb E Z-V
\leq \frac{3V^2}{2(n+2)}e^{3V/(n+2)}.
\]

This gives the following consequences.

- For any joint sequence n,L(n) -> infinity, expected empirical squared distortion tends to zero if and only if V -> 0. In that regime the empirical measure of squared singular values converges in W_2, in probability, to the point mass at 1.
- For fixed homogeneous v > 0, the absolute error of the free second moment vanishes exactly when L^2/n -> 0; the relative error in the spread vanishes exactly when L/n -> 0. These are moment thresholds, not a full spectral convergence theorem.
- For independent normalized tanh derivative gates, a = sech^4(sqrt(q) G)/E sech^4(sqrt(q) G), the gate variance is 8q^2 + o(q^2). For q -> 0, the expected empirical isometry criterion is Lq^2 -> 0, without a further restriction on L/n.
- Empirical isometry does not imply control of every singular value. For Bernoulli gates with survival probability p_n = 1-1/n and L_n = floor(sqrt(n)), E Z -> 0, but P(J invertible) = p_n^(n L_n) <= exp(-L_n) -> 0. A sufficient condition for operator-norm isometry in this surrogate is the stronger nV -> 0; its necessity is not claimed.

Verification used the exact command

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 check_moments.py > verification_output.txt 2>&1
```

The script passed 95 rational cases including accumulated-error bounds, and an independent exact integration of the n=2, L=2 Bernoulli model gave second trace moment 15/4 and squared trace-mean moment 19/8. Three matrix-product simulations agreed within 1.045 estimated standard errors. Independent Gaussian quadrature gave v(q)/q^2 = 7.992008098 at q=0.0001, consistent with the rigorously derived limit 8. The proof also re-derives the product factor by following the fourth moment of a single vector norm. Boundary checks include n=1, L=0, zero gate variance, and inhomogeneous layers.

Data and all numerical parameters are in [results.json](results.json); exact stdout/stderr is in [verification_output.txt](verification_output.txt); commands and work record are in [LOG.md](LOG.md). The final run took 2.81 seconds and used 36.5 MiB peak RSS. NumPy thread settings were all one. The inherited niceness was 20; `nice -n 15` emitted a priority warning because the process was already at that lower priority, and execution completed successfully.

The literature check stayed within ten minutes. References actually opened and their scopes are in [LITERATURE.md](LITERATURE.md). In particular, Boris Hanin and Tianze Jiang, [arXiv:2503.07872](https://arxiv.org/abs/2503.07872), prove an any-relative-rate joint spectral limit for linear i.i.d.-entry products on the depth-root scale. That does not establish the requested nonlinear orthogonal-gate result. No solution of that result was verified, so SOLVED_ELSEWHERE.md was not created. This search is not an exhaustive absence claim.

What failed or remains uncertain: upgrading empirical isometry to uniform isometry is false without additional assumptions, as the explicit kernel example shows. The actual forward-network gates are dependent on the weights and earlier layers, so the conditional gate averaging in the proof does not apply to them. No higher-moment bounds, spectral-edge limits, full limiting density, or novelty claim for the moment calculation is supplied. The 2026 Haas et al. proceedings abstract was opened, but its PDF could not be fetched, so its scope is reported only at abstract level.

The next worker should quantify the error in the two conditional trace identities (5) of PROOF.md for actual orthogonal tanh networks, including the forward-variance drift. Showing that these errors stay negligible after accumulation in a regime such as Lq^2 -> 0 would transfer this empirical isometry argument to the dependent model. A full density or spectral-edge theorem requires further work beyond those identities.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 22:08 Asia/Tbilisi.
