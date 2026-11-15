# Open problem T247: The singular-value spectrum of deep network Jacobians in the joint depth-width limit (dynamical isometry)

Statement: Pennington, Schoenholz and Ganguli compute, via free probability, the limiting singular-value distribution of the input-output Jacobian J = Π D_l W_l of a depth-L network with orthogonal or Gaussian weights, assuming asymptotic freeness of the diagonal derivative matrices D_l and the weights W_l, and find 'dynamical isometry' at criticality for orthogonal weights and sigmoid-like activations. Prove the formula and the isometry claim when depth and width tend to infinity jointly (L = L(n) → ∞), not only at fixed depth.

Caveat: At fixed depth asymptotic freeness of the layer Jacobians has been proved (Pastur and Slavin; Collins and Hayase, to verify). The joint limit needs control of errors accumulated over L layers.

Source: J. Pennington, S. S. Schoenholz and S. Ganguli, Resurrecting the sigmoid in deep learning through dynamical isometry: theory and practice, arXiv:1711.04735 (2017)

Where it stands (checked by us, Nov 2026): Fixed-depth freeness proved; joint limit open as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T247 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T247 (read it,
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
VERDICT: PARTIAL exact dependent-gate trace identities and a joint-limit scalar-normalized empirical isometry theorem for orthogonal tanh networks

The earlier independent-gate result holds. An independent invariant-tensor calculation passed 20 exact rational product checks, including width one, zero depth, zero variance and inhomogeneous variances. The earlier folder was read without modification.

The new result treats gates computed from the same Haar matrix as the actual forward layer. [PROOF.md](PROOF.md) gives exact conditional formulas for the first two trace moments at every n>=3. They retain the forward-direction energies alpha=e^T X e and gamma=e^T X^2 e, which the independent-gate calculation does not contain. For a spherically mean-normalized tanh squared derivative, the leading errors are

\[
 E\operatorname{Tr}X'-\operatorname{Tr}X
 =-\frac{4q}{n+2}(n\alpha-\operatorname{Tr}X)+R_1,
\]

\[
 E\operatorname{Tr}((X')^2)-\operatorname{Tr}X^2
 =-\frac{8q}{n+2}(n\gamma-\operatorname{Tr}X^2)+R_2,
\]

with explicit dimension-uniform bounds in Theorem 2. In particular, dependence can contribute at order q, whereas independent-gate variance begins at order q^2.

Combining the corrections gives an accumulated bound for an ordinary zero-bias tanh network with deterministic gains g_l. Define its actual conditional forward variance q_l=g_l^2||h_(l-1)||^2/n and

\[
 \mu_n(q)=E_{u\text{ uniform sphere}}\operatorname{sech}^4(\sqrt{nq}\,u_1),\qquad
 S_L=\prod_{l=1}^L g_l^2\mu_n(q_l).
\]

If deterministic envelopes q_l<=epsilon_l<=1/4 hold almost surely, Theorem 3 proves

\[
 E\frac1n\operatorname{Tr}\left(\frac{J_LJ_L^T}{S_L}-I\right)^2
 \leq B_L e^{A_L},
\]

\[
 A_L=\sum_l\left(\frac{12\epsilon_l}{n+2}+2760\epsilon_l^2\right),\qquad
 B_L=\sum_l\left(\frac{6\epsilon_l}{n+2}+2904\epsilon_l^2\right).
\]

Thus the empirical squared-singular-value distribution of J_L/sqrt(S_L) tends to delta_1 in W_2 in probability whenever

\[
 \sum_l\epsilon_l^2+\frac1n\sum_l\epsilon_l\to0.
\]

For a constant envelope these conditions are L epsilon_n^2->0 and L epsilon_n/n->0. They are sufficient, without a necessity claim. This is a theorem for the genuine dependent network after an explicit scalar normalization. If additionally S_L->1 in probability, it proves empirical isometry for the original Jacobian. For gain-one tanh, epsilon_n=||h_0||^2/n is a deterministic envelope, so the normalized-spectrum conclusion already has an unconditional special case.

Verification commands, run here:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 recheck_earlier.py > recheck_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 verify_dependent.py > verification_output.txt 2>&1
```

Both exited 0. New verification includes 15 exact rational residual-Haar integrations, direct full-Haar O(3) tanh quadrature at eight q values with maximum discrepancy 2.49e-14, independent finite-difference checks of the linear coefficients to 1.4e-8, higher-dimensional residual-Haar simulations within 1.064 standard errors, and actual depth-30 tanh products at widths 4,8,16. The latter had mean normalized distortions .00118727, .00101426, .000742813, below the proved bounds .135098, .118380, .107635. Final runtime was .92 seconds, peak RSS 91.8 MiB, niceness 20, with all thread settings one. Exact parameters and outputs are in [results.json](results.json), [verification_output.txt](verification_output.txt), and [LOG.md](LOG.md).

What failed or remains uncertain: the initial NumPy BLAS reductions/products emitted spurious-looking floating-point warnings on finite arrays; one exception-enabled run stopped. Their cause was not established. The final verification avoids those operations with explicit weighted sums and non-BLAS einsum while keeping floating-point exceptions enabled. The nice command emitted its inherited-priority warning; actual niceness was verified as 20. Mathematically, scalar normalization cannot be omitted: even the simulations have S_L near .943. No proof of S_L->1 at a fixed critical initialization, no forward-radius concentration theorem for that initialization, no full limiting density, and no spectral-edge or operator-isometry bound is supplied. The small-q accumulated theorem assumes zero bias. No novelty claim is made for the finite-dimensional identities.

The literature check stopped within five minutes and found no verified new resolution; papers actually opened and their scope are in [LITERATURE.md](LITERATURE.md). No SOLVED_ELSEWHERE.md was created.

Next worker: use the explicit scalar factor S_L to isolate what remains at critical initialization. Prove a high-probability forward-radius envelope and control sum_l log(g_l^2 mu_n(q_l)); extend the small-q estimates to the biases used to maintain a nonzero stationary variance. A stopped-process version could replace the almost-sure envelope by a high-probability one. The exact identities are available for this work without invoking freeness.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 03:34 Asia/Tbilisi.
