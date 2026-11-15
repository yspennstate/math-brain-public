# Open problem T305: Metropolized HMC under operator-norm Hessian regularity

Statement: Let pi be proportional to exp(-V) on R^d, with mI<=Hessian V<=LI, bounded L/m, and ||Hessian V(x)-Hessian V(y)||op<=M||x-y||, with m,L,M independent of d. From an M0-warm start, determine whether leapfrog Metropolized HMC reaches total-variation error epsilon in O-tilde(d^{1/4} polylog(M0/epsilon)) gradient evaluations uniformly over this class, or construct a counterexample requiring a larger dimension exponent. No dimension-independent Frobenius-norm Hessian bound is assumed.

Caveat: The warm-start factor is explicit. A stronger-regularity theorem does not settle the stated uniform class.

Source: Chen-Gatmiry-Jiang, When does Metropolized Hamiltonian Monte Carlo provably outperform Metropolis-adjusted Langevin algorithm? (arXiv:2304.04724).

Where it stands (checked by us, Nov 2026): The source gives the desired dimension exponent under its stronger Frobenius-Lipschitz regularity and warm-start assumptions. Operator-norm Lipschitzness alone can cost a factor sqrt(d) on conversion and is a distinct class.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T305 (read it,
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
VERDICT: PARTIAL explicit warm-start concentration of the leading leapfrog energy-error coefficient

For every C2 potential with `mI <= Hessian V <= LI`, define

\[
 A(x,p)=\frac1{12}p^T\nabla^2V(x)p-\frac1{24}|\nabla V(x)|^2,
 \qquad \rho=\pi\otimes N(0,I),\quad\kappa=L/m.
\]

[PROOF.md](PROOF.md) proves the exact identity

\[
576\operatorname{Var}_\rho(A)
=12E\operatorname{tr}((\nabla^2V)^2)
-4E[\nabla V^T\nabla^2V\nabla V]
+\operatorname{Var}_\pi(|\nabla V|^2),
\]

and consequently

\[
\frac{E\operatorname{tr}((\nabla^2V)^2)}{72}
\le\operatorname{Var}_\rho(A)
\le\frac{E\operatorname{tr}((\nabla^2V)^2)}{48}
\le\frac{L^2d}{48}.
\]

More strongly, for each deterministic exact Hamiltonian trajectory time T,
an M0-warm position start with fresh standard Gaussian momentum satisfies,
with probability at least `1-delta`,

\[
 |A(Z)-A(\Phi_TZ)|
 \le2L\left\{\sqrt{\kappa d\log(12M_0/\delta)}
              +\kappa\log(12M_0/\delta)\right\}.
\]

No Hessian-Lipschitz constant, in either operator or Frobenius norm, is
needed for these bounds. They apply to the full class in T305. For fixed
C4 potentials, the proof also derives directly that `A(Z)-A(Phi_T Z)`
is the limit of the kick–drift–kick leapfrog energy error divided by h²,
as h=T/n tends to zero. This identification is a fixed-problem statement.

The remaining problem is uniform finite-step control. With

\[
 R_{h,T}(z)=\mathcal H(\Psi_h^{T/h}z)-\mathcal H(z)
 -h^2[A(z)-A(\Phi_Tz)],
\]

the explicitly subtracted leading term has the desired dimension and
logarithmic warm-start scales. A bound on R at h of order d^(-1/4),
uniform over operator-norm Lipschitz Hessians, has not been proved.
The compact-set Taylor argument does not give it. No finite-step acceptance
bound, mixing theorem, or counterexample to T305 is claimed.

The next worker should try to bound this R in probability under a warm
start, or find a dimension-dependent potential for which R is large at
that step size. Numerical endpoint laws cannot be replaced by exact-flow
stationarity. A subsequent mixing argument must also supply proposal
overlap or another route to conductance.

Validation used exact rational polynomial algebra, a direct Gaussian
invariant calculation, deterministic quadrature on a coupled asymmetric
two-dimensional target, and a separate RK4/leapfrog convergence comparison.
The two variance derivations agree; the numerical identity residual is at
most 6.939e-18. Gaussian coordinates give `5 lambda^2/288`, inside the
proved bounds. The finite-grid calculations are checks, not rigorous
numerical proofs. No literature priority claim is made for these lemmas.

Reproduce with:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py > audit_output.txt 2>&1
```

The run took 0.209 seconds and used about 17.5 MB maximum RSS, with one
Python thread. The `nice` wrapper warns because the inherited priority is
already nice 20; the script verifies it. Exact output is in
[audit_output.txt](audit_output.txt), data in [audit_data.json](audit_data.json),
and the derivation/audit history in [LOG.md](LOG.md).

The literature check, completed in less than ten minutes on 14 November
2026, did not locate a full settlement. Papers actually opened:

- Yuansi Chen, Khashayar Gatmiry, and Minhui Jiang,
  *When does Metropolized Hamiltonian Monte Carlo provably outperform
  Metropolis-adjusted Langevin algorithm?*,
  [arXiv:2304.04724v3](https://arxiv.org/html/2304.04724v3),
  11 February 2026. Section 2.4 requires Frobenius Hessian regularity;
  Table 1 retains that extra assumption for the d^(1/4) guarantee.
- Fan Chen, Sinho Chewi, Alexander Rakhlin, and Matthew S. Zhang,
  *Exact simulation of diffusions and improved algorithms for log-concave
  sampling*, [arXiv:2608.05022](https://arxiv.org/html/2608.05022v1),
  5 August 2026. It uses path-space rejection sampling. Its improved
  higher-order bound assumes Frobenius-Lipschitz Hessians explicitly in
  Assumption 1, and does not settle leapfrog HMC for this operator-norm class.
- Siddharth Mitra, Vishwak Srinivasan, Xiuyuan Wang, and Andre Wibisono,
  *Accelerated Mixing Time of Randomized Hamiltonian Monte Carlo*,
  [arXiv:2607.12902](https://arxiv.org/abs/2607.12902), 14 July 2026.
  Its abstract gives exact-flow total-integration-time guarantees;
  these do not establish the stated discretized gradient complexity.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:30 Asia/Tbilisi.
