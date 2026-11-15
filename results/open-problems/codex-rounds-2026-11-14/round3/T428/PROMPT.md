# Open problem T428: The critical two-dimensional stochastic heat flow and the two-dimensional KPZ equation at criticality

Statement: Prove Conjecture 1.17 of arXiv:2609.15832: retain the other hypotheses and critical tuning of Theorems 1.9 and 1.15, but replace nonnegativity and uniform compact support of the spatial kernels zeta_N by |zeta_N(x)|<=C exp(-a|x|), uniformly in N, for some C,a>0. Do the discrete and continuum measure-valued flows still converge in finite-dimensional distributions to the critical two-dimensional stochastic heat flow, with the same critical-tuning coefficients Lambda_N?

Caveat: This is a named remaining conjecture; no undefined logarithm of a singular flow is called a solution of critical KPZ.

Source: A universality result for the critical 2d stochastic heat flow (arXiv:2609.15832); Caravenna-Sun-Zygouras (arXiv:2109.03766).

Where it stands (checked by us, Nov 2026): 2609.15832 proves universality for a substantial class of linear flows, including correlated polymers and mollified Gaussian SPDEs. It explicitly leaves the signed, exponentially decaying spatial-kernel extension as Conjecture 1.17.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T428 (read it,
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
VERDICT: PARTIAL Brownian signed-kernel tuning eigenvalue and cutoff stability

For the gap of two independent planar Brownian motions, let f be a fixed
real profile with |f(x)|<=C exp(-a|x|) and m=integral f>0. The coefficient
defined by the integrated gap kernel has a unique dominant positive
simple eigenvalue for large N, even if f changes sign. The proof gives

    Lambda_N(f) = m/(4 pi) + I(f)/(m log N) + O(1/log^2 N),
    I(f) = integral integral f(x)f(y)
                 [log 4-gamma-2 log|x-y|]/(4 pi) dx dy.

It also controls normalized powers of the weighted operator uniformly
in the number of factors. This is a signed spatial-operator counterpart
of the spectral step; it is not a time-resolved renewal theorem.

Cutting f off at R_N=kappa log log N, with kappa>1/a, changes Lambda_N(f)
by o(1/log N). Therefore the same beta_N preserves the critical parameter
theta when beta_N^2 f is replaced by beta_N^2 f_{R_N}. The tuning is

    beta_N^2 = 4 pi/(m log N)
        * [1+(theta-4 pi I(f)/m^2)/log N+o(1/log N)].

The complete argument is in [PROOF.md](PROOF.md). For the signed
positive-definite example f=2 phi_1-phi_2, with phi_s the centered planar
Gaussian density of covariance s Id, m=1 and

    4 pi I(f)=log(81/32)=0.92871325187271221849482034039921997821.

This constant was derived independently from Gaussian logarithmic moments
and a rational heat-overlap integral. Scalar quadrature at 45-digit
precision agrees with the closed formula to better than 1e-36.
The heat-kernel normalization and remainder were likewise checked by
two analytic derivations and direct integration. These numerical checks
do not substitute for the operator proof.

Reproduce the checks from this folder with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py
```

The successful run exited 0, used 21,512,192 bytes peak RSS and about
0.1 seconds of quadrature time. Results are in
[verification.json](verification.json); commands, output and the
adversarial audit are in [LOG.md](LOG.md). The sandbox rejected a
further nice increment, but the measured inherited nice value was
already 20. An earlier run failed before computation because macOS
rejected the attempted address-space limit; that unsupported limit was
removed. A 90-second CPU limit remains in the script.

The literature search took approximately three minutes. No later
resolution of the particular conjecture was located. The current
[arXiv record for 2609.15832](https://arxiv.org/abs/2609.15832) lists v1.
[Xue-Mei Li and Te-Chun Wang, arXiv:2611.03191](https://arxiv.org/abs/2611.03191)
concerns moment growth and ground-state energy bounds; it does not
announce this signed-kernel extension. The earlier
[Sudheesh Surendranath, arXiv:2608.11603](https://arxiv.org/abs/2608.11603)
is already discussed in the target paper as supporting evidence. This
bounded search is not a guarantee that no relevant work exists.

What remains unproved:

- Conjecture 1.17, in either its general discrete or continuum form.
- Time-resolved signed renewal estimates and higher-moment convergence.
- An analogue for general N-dependent gap processes under the paper's
  assumptions; the proof uses the explicit Brownian kernel.
- The zero-mass case and arbitrary N-dependent profiles. The isolated
  rank-one eigenvalue used here disappears when m=0.
- Construction of approximating stochastic flows from the cutoffs.
  Increasing support radii violate uniform compact support, and cutting
  off a covariance can destroy positive definiteness.

No counterexample to the stated lemma was found. Its novelty is not
claimed. The next useful step is a time-resolved signed pair-resolvent
estimate in the same Brownian, fixed-profile, positive-mass setting,
using the dominant spectral projection to retain cancellations.
Replacing f by |f| generally changes its mass and critical scale, so
absolute-value domination alone does not supply that estimate.

Task: “push this problem forward by one checkable piece” — 14 November
2026, approximately 22:15 +04 (Asia/Tbilisi).
