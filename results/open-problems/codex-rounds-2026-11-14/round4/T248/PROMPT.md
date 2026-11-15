# Open problem T248: Edge universality for the conjugate kernel of a random network

Statement: Conjugate kernel of a one-layer random network: Y = sigma(W X / sqrt d), W m x d with iid N(0, 1) entries, X d x N with iid sub-Gaussian entries (or columns uniform on the sphere of radius sqrt d), m, d, N tending to infinity proportionally. Take sigma Lipschitz (or smooth), centred, with no linear part: E sigma(Z) = 0 and E Z sigma(Z) = 0 for Z ~ N(0, 1). Prove that lambda_max(Y Y^T / N) converges to the right edge of the limiting (Pennington-Worah) law, which is regular there, with Tracy-Widom (beta = 1) fluctuations on the n^(-2/3) scale. Then allow a linear component, which changes the bulk: state an explicit rule for any finite-rank spikes it or the input design creates and prove the same edge statement for the largest eigenvalue after them. For polynomial activations of degree at least 3 the top eigenvalue at widths below several thousand is an outlier made by the largest entry of Y, so the statement is asymptotic only.

Caveat: The global law is known; the edge and fluctuations are the open part. Outliers come from the mean and the linear Hermite component of sigma.

Source: L. Benigni and S. Péché, Eigenvalue distribution of nonlinear models of random matrices, arXiv:1904.03090 (2019); Z. Fan and Z. Wang, Spectra of the Conjugate Kernel and Neural Tangent Kernel for linear-width neural networks, arXiv:2005.11879 (2020)

Where it stands (checked by us, Nov 2026): Global laws proved. Benigni and Péché (arXiv:2201.04753) prove that the largest eigenvalue converges in probability to the same limit as for an information-plus-noise matrix, with a phase transition depending on the activation and the entry laws. Tracy-Widom fluctuations at the edge are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T248 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T248 (read it,
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
VERDICT: PROVED TW1 with deterministic finite-size centering for spherical inputs and Lipschitz activations of Hermite rank at least three, away from aspect ratio one

The earlier conditional application checks out. The new result completes its proposed next step for a precise subclass: independent spherical input columns; a fixed Lipschitz activation with Gaussian Hermite coefficients a_0=a_1=a_2=0 and variance v>0; N/d tending to a positive finite constant; and b_N=m/N tending to b in (0,infinity) with b!=1. For K=YY^T/N,

    [b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))] N^(2/3)
       [lambda_max(K)-v(1+sqrt(b_N))^2] => TW_1.

Consequently lambda_max(K) converges in probability to v(1+sqrt(b))^2. This is a special-case result, not a solution of the full original T248 statement.

The complete argument is in [PROOF.md](PROOF.md). Its new deterministic lemma bounds the covariance-edge displacement by

    C Tr((Sigma_X-vI)^2)/N,

when Sigma_X is near vI and Tr Sigma_X=Nv. Exact trace cancellation removes the linear perturbation term. For spherical inputs and Hermite rank at least three,

    E||Sigma_X-vI||_F^2
       <= 15 v^2 N(N-1)/[d(d+2)(d+4)] = O(d^-1).

The conditional covariance edge therefore differs from v(1+sqrt(N/m))^2 by O_p(d^-2), which is negligible at the TW scale. The proof verifies covariance regularity and gives a direct Gaussian rotation proof of the quadratic-form moment bounds. A deterministic bad-sequence argument justifies uniform conditional application and removal of conditioning.

The universality input is the already identified Corollary 1.4 of Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2). Its theorem is used as stated; it is not independently reproved here. The under-five-minute literature check reopened the cited papers and found no newer complete solution. No SOLVED_ELSEWHERE.md was created. The earlier folder contains no PROOF.md or research scripts to rerun.

Independent checks are recorded in [LOG.md](LOG.md). [verify_edge.py](verify_edge.py) checks 32 two-point population spectra using both derivative bisection and independent direct minimization of the edge function; they agree within 1.776e-15. The quadratic coefficient is also checked by finite differences, with maximum relative discrepancy 3.909e-08. The spherical sixth moment is checked through two exact formulas. The matrix-transposition scale agrees within relative error 2.220e-16. These are algebra checks; no numerical TW experiment is claimed.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_edge.py
```

The run exited successfully in under a second and used only the Python standard library. The sandbox rejected the nice priority adjustment with `setpriority: Operation not permitted`; the scalar script then ran. No further numerical program was launched. All task writes stayed inside this folder. No git or subagents were used.

What fails outside the subclass: a nonzero a_2 invalidates the Frobenius-small covariance argument; non-normalized inputs invalidate exact conditional centering and constant trace; the external theorem excludes aspect ratio one; and no proof is given for linear components, finite-rank supercritical outliers or the next eigenvalue below them, or non-Lipschitz polynomial activations. Replacing the exact aspect ratio by its limit also requires a convergence rate that is not assumed here.

Next worker: handle a nonzero second Hermite coefficient for spherical inputs in the strictly subcritical regime. First isolate its rank-one covariance component and prove a quantitative bound for the remainder; then check pole separation and the finite covariance-edge shift. Critical and supercritical spikes require an additional theorem and should be treated separately.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first clock reading 03:37:12 +04.
