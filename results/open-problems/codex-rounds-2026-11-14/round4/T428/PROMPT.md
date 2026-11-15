# Open problem T428: The critical two-dimensional stochastic heat flow and the two-dimensional KPZ equation at criticality

Statement: Prove Conjecture 1.17 of arXiv:2609.15832: retain the other hypotheses and critical tuning of Theorems 1.9 and 1.15, but replace nonnegativity and uniform compact support of the spatial kernels zeta_N by |zeta_N(x)|<=C exp(-a|x|), uniformly in N, for some C,a>0. Do the discrete and continuum measure-valued flows still converge in finite-dimensional distributions to the critical two-dimensional stochastic heat flow, with the same critical-tuning coefficients Lambda_N?

Caveat: This is a named remaining conjecture; no undefined logarithm of a singular flow is called a solution of critical KPZ.

Source: A universality result for the critical 2d stochastic heat flow (arXiv:2609.15832); Caravenna-Sun-Zygouras (arXiv:2109.03766).

Where it stands (checked by us, Nov 2026): 2609.15832 proves universality for a substantial class of linear flows, including correlated polymers and mollified Gaussian SPDEs. It explicitly leaves the signed, exponentially decaying spatial-kernel extension as Conjecture 1.17.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T428 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T428 (read it,
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
VERDICT: PARTIAL Brownian signed pair-renewal Laplace limit with unchanged critical tuning

The earlier Brownian spectral lemma holds. Its operator expansion was
re-derived, and the signed Gaussian example's correction
4 pi I(f)=log(81/32) was independently recomputed by finite-interval
Gaussian-log quadrature. No defect was found in the earlier result.

The new result is a Laplace-transform limit for an actual signed pair
renewal density, for the same fixed real Brownian profile satisfying
|f(x)|<=C exp(-a|x|) and m=integral f>0. With L=log N, use the earlier
sharp-time eigenvalue Lambda_N and tune

    alpha_N L Lambda_N = 1+(theta+epsilon_N)/L,   epsilon_N -> 0.

Here alpha_N is the earlier beta_N^2. Set

    u=sqrt(|f|),   v=sgn(f)u,   P=u tensor v/m,
    Q(t)=M_u exp(t Delta) M_v,
    R_N(t)=sum_{k>=1} alpha_N^k Q^{*k}(t).

For Re z>exp(theta-gamma), the theorem proves

    integral_0^infinity exp(-zt) [N/L R_N(Nt)] dt
        -> P/(log z+gamma-theta)

in operator norm, locally uniformly in z, with error
O_K(1/L+|epsilon_N|). The algebraic resolvent limit also holds on compact
subsets of Re z>0 away from exp(theta-gamma).

The two new ingredients in [PROOF.md](PROOF.md) are:

- A direct heat-kernel comparison between exponential time damping and
  the sharp cutoff. Its finite part is -gamma-log z and its weighted
  operator remainder is O(N^-1/2). The signed leading projection is
  retained throughout.
- Identification of the finite-time renewal series with
  alpha_N M_u exp(t(Delta+alpha_N f)) M_v. A self-adjoint quadratic-form
  argument justifies its critical-scale Laplace integral. Finite-time
  absolute convergence alone would not justify that integral.

This extends the earlier spatially integrated spectral calculation to
a genuine renewal transform. It does not replace f by |f| or change
the sharp-time coefficient Lambda_N. Novelty is not claimed.

Reproduce the scalar checks with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py
```

Exit 0; 45-digit precision; 0.614 seconds; peak RSS 24,592,384 bytes;
one thread. The shell refused a further nice increment, but libc reported
inherited nice 20 with errno zero. Results are in
[verification.json](verification.json), and the command, numerical output
that matters, independent Schur-complement derivation and adversarial
audit are in [LOG.md](LOG.md). These are scalar checks, not a numerical
operator proof. All exact scalar identities tested agree to better than
1e-34. No numerical assertion failed.

A web-tool literature check of less than five minutes found no later
resolution. The current record of Hindy Drillick, Jonathan Hou and Shalin
Parekh, *A universality result for the critical 2d stochastic heat flow*,
[arXiv:2609.15832](https://arxiv.org/abs/2609.15832), still lists v1,
whose HTML states Conjecture 1.17. The check also opened Quentin Berger,
Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu,
Shuta Nakajima, Rongfeng Sun, Li-Cheng Tsai, Zuodi Xie and Nikos Zygouras,
*The Critical 2D KPZ Process*,
[arXiv:2610.31614](https://arxiv.org/abs/2610.31614). Its stated result
concerns a renormalized Cole–Hopf construction; it is not a stated
resolution of the signed-kernel conjecture and predates the earlier
report. This bounded search does not establish absence of other work.

What remains uncertain or unproved: Conjecture 1.17 in both its discrete
and continuum forms; inverse Laplace estimates on unbounded vertical
lines; pointwise time-resolved renewal estimates; diffusive spatial
endpoints; arbitrary N-dependent profiles and gap processes; and third
and fourth moments. The result requires positive total mass. It does not
construct a KPZ field or take an undefined logarithm of the singular flow.

The next worker should try to prove a uniform vertical-line resolvent
bound strong enough for time inversion, or first derive a precise weak
time-integrated pair limit from this transform theorem. The semigroup
representation may help control signed matrix elements. Compact-set
Laplace convergence alone must not be presented as pointwise time
convergence.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 03:53 +04 (Asia/Tbilisi;
first recorded local clock reading).
