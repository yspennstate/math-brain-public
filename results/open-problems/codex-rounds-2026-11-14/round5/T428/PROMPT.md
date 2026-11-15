# Open problem T428: The critical two-dimensional stochastic heat flow and the two-dimensional KPZ equation at criticality

Statement: Prove Conjecture 1.17 of arXiv:2609.15832: retain the other hypotheses and critical tuning of Theorems 1.9 and 1.15, but replace nonnegativity and uniform compact support of the spatial kernels zeta_N by |zeta_N(x)|<=C exp(-a|x|), uniformly in N, for some C,a>0. Do the discrete and continuum measure-valued flows still converge in finite-dimensional distributions to the critical two-dimensional stochastic heat flow, with the same critical-tuning coefficients Lambda_N?

Caveat: This is a named remaining conjecture; no undefined logarithm of a singular flow is called a solution of critical KPZ.

Source: A universality result for the critical 2d stochastic heat flow (arXiv:2609.15832); Caravenna-Sun-Zygouras (arXiv:2109.03766).

Where it stands (checked by us, Nov 2026): 2609.15832 proves universality for a substantial class of linear flows, including correlated polymers and mollified Gaussian SPDEs. It explicitly leaves the signed, exponentially decaying spatial-kernel extension as Conjecture 1.17.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T428 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T428 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T428 (read it,
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
VERDICT: PARTIAL Time-resolved Brownian signed pair-renewal limit with unchanged critical tuning

The earlier spectral and Laplace-transform results hold on independent
re-derivation. The new result upgrades the fixed-profile Brownian signed
pair limit from Laplace transforms to locally uniform convergence in
positive time, in operator norm.

Let f be fixed, real, |f(x)|<=C exp(-a|x|), with m=integral f>0.
Set u=sqrt(|f|), v=sgn(f)u, P=u tensor v/m, L=log N, and
Q(t)=M_u exp(t Delta)M_v. Retain the earlier sharp-time eigenvalue
Lambda_N and exactly the same tuning

    alpha_N L Lambda_N=1+(theta+epsilon_N)/L,   epsilon_N -> 0.

For the signed series R_N=sum_{k>=1} alpha_N^k Q^{*k}, the theorem is

    sup_{delta<=t<=T} ||N R_N(Nt)/L - g_theta(t)P|| -> 0

for every 0<delta<T<infinity, where

    z_*=exp(theta-gamma),
    g_theta(t)=integral_0^infinity z_*^s t^(s-1)/Gamma(s) ds.

Its Laplace transform is 1/(log z+gamma-theta) for real z>z_*.
There is also operator-norm convergence against every continuous time
test having a finite limit at infinity, with damping exp(-bt), b>z_*.
The full proof, including a fresh derivation of the preceding transform
input, is in [PROOF.md](PROOF.md).

The new ingredient is operator order. With the unitary sign multiplier
J=sgn(f), taking J=1 on {f=0},

    [N R_N(Nt)/L]J
        =(N alpha_N/L) M_u exp(t N(Delta+alpha_N f)) M_u.

This is positive as a Hilbert-space operator. After multiplication by
exp(-bt), it decreases in operator order, because the preceding spectral
argument bounds the top of N(Delta+alpha_N f) below b. Polynomial
approximation in exp(-t) gives norm convergence against continuous time
tests; before/after averages then squeeze each positive time. A finite
partition yields local uniformity. The signed potential remains f
throughout. No replacement by |f| and no change in Lambda_N is made.

The earlier claim was independently checked by a Schur complement with
respect to the nonorthogonal projection P. Its scalar denominator is
(log z+gamma-theta-epsilon_N)/L+O(L^-2). The signed self-adjoint form
argument justifying the actual Laplace integral was also re-derived.
A new compactified rational-overlap quadrature independently recovered
4 pi I_f=log(81/32). No defect was found in the earlier work.

Reproduce the scalar checks with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py
```

Exit 0; 40-digit precision; 0.645 seconds; peak RSS 25,706,496 bytes;
all four thread settings equal one. The wrapper's extra nice increment
was refused, while libc measured inherited nice 20 with errno zero.
The program uses a 120-second CPU cap and scalar quadrature only.
Results are in [verification.json](verification.json); the command,
output that matters and adversarial audit are in [LOG.md](LOG.md).
Twelve gamma-integral versus pole/branch density checks agree to better
than 1.5e-39, and three independent branch-transform checks agree to
better than 9.2e-41. These check constants, not an operator theorem.

No numerical assertion failed. A vertical-line resolvent estimate was
not needed: semigroup order provides the positive-time reconstruction.
The audit checks the sign convention at zeros of f, the pole residue
z_* in the independent density representation, and the distinction
between a norm bound on a positive operator-valued total mass and an
integral of operator norms. The latter is not inferred.

A web-tool literature check under five minutes found no later resolution.
The opened current record of Hindy Drillick, Jonathan Hou and Shalin
Parekh, *A universality result for the critical 2d stochastic heat flow*,
[arXiv:2609.15832](https://arxiv.org/abs/2609.15832), still lists only
v1; its [HTML](https://arxiv.org/html/2609.15832v1) retains Conjecture 1.17.
This bounded search does not establish absence of all other work.
Novelty of the pair theorem is not claimed.

What remains unproved: Conjecture 1.17 in both discrete and continuum
form; time estimates uniform down to zero; any rate for the new time
limit; diffusive spatial endpoints; arbitrary N-dependent profiles and
gap processes; and third/fourth moment convergence. The proof relies on
a self-adjoint Brownian generator and strictly positive mass. It neither
constructs a KPZ field nor takes a logarithm of the singular flow.

The next worker should first make this time theorem uniform for
N-dependent real profiles with a common exponential envelope and
integrals bounded below by a positive constant. The precise target is
||N R_N(Nt)/L-g_theta(t)P_N|| -> 0 uniformly on [delta,T], retaining
each profile's original sharp-time Lambda_N and moving projection P_N.
The spatial moment and spectral-gap estimates appear uniform under
these assumptions, and the order proof only needs a uniform bound on
||P_N J_N||. That uniformity must be written out, not assumed from
the fixed-profile statement. General nonsymmetric gap processes still
require a different argument.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 06:41 +04 (Asia/Tbilisi;
first recorded local clock reading).
