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
VERDICT: PROVED TW1 with deterministic finite-size centering for spherical inputs and a strictly subcritical quadratic Hermite component

The round 3 result holds on independent rechecking. This session extends it
from a_0=a_1=a_2=0 to a_0=a_1=0, allowing q=a_2^2>0 under the explicit strict
condition

    q alpha sqrt(b)<v,
    alpha=lim N/d,    b=lim m/N !=1,    v=E sigma(Z)^2>0.

The other hypotheses remain: independent spherical input columns of radius
sqrt(d), independent standard Gaussian W, a fixed Lipschitz activation, and
positive finite proportional limits. For K=YY^T/N and b_N=m/N,

    [b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))] N^(2/3)
      [lambda_max(K)-v(1+sqrt(b_N))^2] => TW_1.

Thus the largest eigenvalue converges in probability to v(1+sqrt(b))^2.
This is a further special case of T248. The full problem remains open.

The complete proof is in [PROOF.md](PROOF.md). Its new covariance decomposition is

    Sigma=(v-q/d)I+(q/d)11^T+qB+R,
    B_jk=rho_jk^2-1/d (j!=k),    B_jj=0,
    ||B||_op=O_p(d^-1/4),    ||R||_F=O_p(d^-1/2).

The operator-norm bound follows from an exact fourth-trace identity proved
by centered traceless tensor contractions and closed-walk counting. It
isolates one population eigenvalue v+q alpha+o_p(1). The condition above is
exactly positive separation of its pole from the scalar MP stationary point.
A strengthened deterministic edge lemma allows this nonvanishing subcritical
population spike. Exact trace cancellation and E Tr((Sigma-vI)^2)=O(1) give
an O_p(N^-1) conditional edge shift, negligible at the TW scale.

The universality input remains Corollary 1.4 of Guangchen Chen and Xing Lyu,
*Tracy–Widom law for sample covariance matrices under quadratic form
concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2).
Its hypotheses are verified conditionally, with uniform constants. The theorem
is used as stated, not independently reproved. The five-minute literature
check found no newer full solution; no SOLVED_ELSEWHERE.md was created.

Independent verification is in [verify_subcritical.py](verify_subcritical.py),
with the command and complete relevant output in [LOG.md](LOG.md):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B verify_subcritical.py
```

All checks passed. Coordinate-polynomial integration independently reproduced
the pair, star and cycle expectations exactly at d=2,3; exhaustive enumeration
verified all fourth-trace walk counts for N=2,...,7. The two covariance-edge
solvers agreed within 1.776e-15. The script also checked the predecessor's
rational trace cancellation, spherical moments, the threshold on both sides
of criticality, first-order finite-rank edge shifts, and normalization in both
rectangular orientations. These are algebra checks, not numerical TW evidence.
The scalar script used the standard library and finished in 0.018 seconds.

The launcher printed a priority-adjustment warning, but the script's effective
priority guard passed. A separate diagnostic measured nice value 20, already
at least the required 15. No computation ran at an unverified higher priority.
All task writes stayed in this folder; no git, subagents or external writes.

What fails or remains uncertain: covariance closeness to vI alone fails for
q>0, which is why the spike was separated. At criticality pole separation
vanishes, and above it the scalar MP stationary point is across the pole;
the cited regular-rightmost-edge theorem does not supply the desired bulk-edge
fluctuation result there. No sample outlier fluctuation law or law for the
next eigenvalue below an outlier is proved. Linear components, random column
norms, non-Lipschitz polynomials and b=1 remain outside this result. Replacing
the exact finite aspect ratio by its limit still requires an extra rate.

Next worker: use the same decomposition to prove TW1 for the explicitly
projected kernel Y(I-ee^T)Y^T/N, e=(1,...,1)^T/sqrt(N), even when q is supercritical.
Then identify the additional comparison needed to transfer that result to
the second eigenvalue of the original kernel. Interlacing alone does not
identify its fluctuations, so do not equate these two conclusions.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first clock reading 05:13:02 +04.
