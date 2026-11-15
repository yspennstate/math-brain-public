# Open problem T248: Edge universality for the conjugate kernel of a random network

Statement: Conjugate kernel of a one-layer random network: Y = sigma(W X / sqrt d), W m x d with iid N(0, 1) entries, X d x N with iid sub-Gaussian entries (or columns uniform on the sphere of radius sqrt d), m, d, N tending to infinity proportionally. Take sigma Lipschitz (or smooth), centred, with no linear part: E sigma(Z) = 0 and E Z sigma(Z) = 0 for Z ~ N(0, 1). Prove that lambda_max(Y Y^T / N) converges to the right edge of the limiting (Pennington-Worah) law, which is regular there, with Tracy-Widom (beta = 1) fluctuations on the n^(-2/3) scale. Then allow a linear component, which changes the bulk: state an explicit rule for any finite-rank spikes it or the input design creates and prove the same edge statement for the largest eigenvalue after them. For polynomial activations of degree at least 3 the top eigenvalue at widths below several thousand is an outlier made by the largest entry of Y, so the statement is asymptotic only.

Caveat: The global law is known; the edge and fluctuations are the open part. Outliers come from the mean and the linear Hermite component of sigma.

Source: L. Benigni and S. Péché, Eigenvalue distribution of nonlinear models of random matrices, arXiv:1904.03090 (2019); Z. Fan and Z. Wang, Spectra of the Conjugate Kernel and Neural Tangent Kernel for linear-width neural networks, arXiv:2005.11879 (2020)

Where it stands (checked by us, Nov 2026): Global laws proved. Benigni and Péché (arXiv:2201.04753) prove that the largest eigenvalue converges in probability to the same limit as for an information-plus-noise matrix, with a phase transition depending on the activation and the entry laws. Tracy-Widom fluctuations at the edge are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T248 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T248 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T248 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T248 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PROVED TW1 with deterministic finite-size centering for the projected spherical kernel with arbitrary quadratic Hermite coefficient

The round 4 result holds on independent rechecking. This session proves
its proposed next step. Assume independent spherical input columns of
radius sqrt(d), independent standard Gaussian weights, a fixed Lipschitz
activation with a_0=a_1=0 and variance v>0, N/d tending to a positive finite
limit, and b_N=m/N tending to b in (0,infinity), b!=1. For

    K_P=Y(I-ee^T)Y^T/N,    e=(1,...,1)^T/sqrt(N),

the conclusion is

    [b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))] N^(2/3)
       [lambda_max(K_P)-v(1+sqrt(b_N))^2] => TW_1.

Thus lambda_max(K_P) converges in probability to v(1+sqrt(b))^2. There
is no restriction on q=a_2^2. In particular this includes the critical
and supercritical quadratic-spike regimes excluded by round 4. This is
a theorem for an explicitly projected kernel; the full T248 problem
remains open.

The complete proof is in [PROOF.md](PROOF.md). In dimension M=N-1, the
conditional covariance is

    T=(v-q/d)I_M+q Q^T B Q+Q^T R Q,

where Q is any deterministic orthonormal basis of e^perp. The constant
quadratic spike disappears, so ||T-vI||_op=o_p(1) for every q. Projection
loses exact trace cancellation: the trace defect is

    Tr(T-vI)=-q(N-1)/d+o_p(1).

The new deterministic edge lemma retains this bounded trace defect and
the bounded squared Hilbert–Schmidt defect. It gives an O_p(N^-1)
conditional edge displacement, negligible at the TW scale. The proof
handles the singular ambient projection by working on e^perp, verifies
uniform concentration and edge regularity, and removes conditioning.

The universality input remains Corollary 1.4 of Guangchen Chen and Xing
Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form
concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2).
It is used as stated, not independently reproved. The five-minute web
search found no newer full solution; no SOLVED_ELSEWHERE.md was created.

Commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T248/verify_subcritical.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B verify_projection.py
```

All checks passed. The new [verification script](verify_projection.py)
checks exact rational projection, trace and Frobenius identities;
independently checks the predecessor's circle moments by Fourier
integration; checks a bounded cosine activation's covariance two ways;
and checks the nonzero-trace edge lemma with two independent scalar
solvers. The solvers agree within 1.776e-15. Three normalization formulas
agree within relative error 2.220e-16 for the scale and absolute error
3.553e-15 for the center, in both rectangular orientations. These are
algebra checks, not numerical evidence of a TW limit. The new script
took 0.026 seconds and used 13.8 MiB peak RSS. Full output is in
[LOG.md](LOG.md).

What failed or remains uncertain: replacing the projected trace defect
by zero would be wrong. The general covariance-edge lemma must allow
negative edge corrections; no sign is claimed for the network's correction.
Interlacing cannot transfer this result to lambda_2(YY^T/N); the script
exhibits an order-one gap in a deterministic rank-one example. No sample
outlier law or original-model eigenvalue sticking estimate is proved.
Linear components, random column norms, non-Lipschitz polynomials and
b=1 remain outside the result. Replacing b_N by b in the center still
requires an additional convergence rate. There is no unresolved proof
gap identified within the stated projected model, conditional on the
cited universality theorem.

The launcher printed a priority-adjustment warning. Both numerical runs
passed their effective-priority guards; the new run measured nice value
20. Thus all computations ran at the requested low effective priority.
All writes stayed in this folder. No git, subagents or external writes.

Next worker: in the strictly supercritical regime q alpha sqrt(b)>v,
prove edge sticking between lambda_2(YY^T/N) and lambda_1(K_P), ideally
their difference being o_p(N^-2/3). Start from the exact rank-one identity
K=K_P+aa^T, a=Ye/sqrt(N), and its secular equation. The missing estimate
must control the dependence of a on K_P and the secular denominator near
the bulk edge. A rank-one interlacing argument or population covariance
norm estimate alone is insufficient. Treat a critical spike separately.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first clock reading 08:52:40 +04.
