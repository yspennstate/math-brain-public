# Open problem T179: Uniqueness in law for the stochastic heat equation with non-degenerate Hölder noise coefficient below exponent 2/3

Statement: On the one-dimensional torus T consider ∂_t u = Δu + g(u)Ẇ with Ẇ space-time white noise, where g is uniformly elliptic (|g| bounded away from 0) and globally β-Hölder continuous. Weak uniqueness (uniqueness in law) is known for β > 2/3. Does it hold for every β ∈ (0, 2/3], or at least for β > 1/2?

Caveat: Without ellipticity uniqueness can fail: Mueller, Mytnik and Perkins constructed non-unique solutions for g(x) = |x|^γ with γ < 3/4, as described by Han, so the role of the condition |g| ≥ c > 0 is the whole question. Pathwise uniqueness for β > 3/4, without ellipticity, is due to Mytnik and Perkins. The finite-dimensional analogue (uniqueness in law for SDEs with uniformly elliptic continuous diffusion coefficient, Stroock–Varadhan) suggests that ellipticity alone might give uniqueness for every β > 0, and Han records that no counterexample is known for any β > 0.

Source: Y. Han, Stochastic heat equation with nondegenerate Hölder diffusion coefficient: uniqueness below the three-fourth threshold, arXiv:2608.01279 (2026)

Where it stands (checked by us, Nov 2026): Mytnik and Perkins (Probab. Theory Related Fields 149 (2011) 1–96) proved pathwise uniqueness for β > 3/4. Mueller, Mytnik and Perkins (Ann. Probab. 42 (2014) 2032–2112) gave non-uniqueness, both in law and pathwise, for the non-elliptic coefficient |u|^γ with γ < 3/4. Bass and Perkins proved uniqueness for elliptic coefficients 1/2 + ε-Hölder in an enhanced norm that does not cover pointwise coefficients. Han's generalized coupling method gave weak uniqueness for elliptic g with β > 3/4, and Han (arXiv:2608.01279) lowered this to β > 2/3. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T179 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T179 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T179 (read it,
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
VERDICT: PROVED measurable linear-growth drift extension for unbounded diffusion and arbitrary L2 initial states, conditional on the prior drift-free input

The round-3 result checks. Independently re-derived its ordered-gap mass
conservation, comparison limit, and martingale identification. Re-ran its
exact-arithmetic diagnostic successfully. No error was found in its main
claim. Its external input remains Yi Han's bounded-start theorem; the main
full-positive-Hölder argument in that preprint has not been audited here.

The new piece is weak existence and uniqueness for

    dU = (Delta U + b(t,x,U)) dt + g(U) dW,

with every deterministic u0 in L2(T), unbounded uniformly elliptic globally
beta-Hölder g, 0<beta<1, and Borel b satisfying
|b(t,x,z)| <= B_T(1+|z|) on each finite horizon. No bounded initial spatial
norm is assumed. PROOF.md gives the complete transfer from the prior
drift-free result, a canonical density determined by the state path, and
mutual absolute continuity of drifted and drift-free path laws.

It also proves the exact entropy identities

    Ent(mu_b | mu_0) = (1/2) E_mu_b integral ||b(U)/g(U)||_2^2 dt,
    Ent(mu_0 | mu_b) = (1/2) E_mu_0 integral ||b(U)/g(U)||_2^2 dt.

Both quantities are finite, with an explicit bound depending only on the
horizon, coefficient bounds, ellipticity constant and ||u0||_2. These
identities check the density's sign and the factor 1/2. They do not require
uniqueness of the joint state-noise law.

The transfer method is already Proposition 8.5 of Yi Han,
*Weak uniqueness for the stochastic heat equation with nondegenerate
diffusion: the full Hölder regime*,
[arXiv:2611.07310v1](https://arxiv.org/html/2611.07310v1).
The new scope comes from combining it with the round-3 L2 extension. This
is not an independent proof of the original full-Hölder uniqueness result.
The brief literature check found no later change to the residual
unbounded-diffusion, rough-initial-data case already isolated by the prior
workers. No new SOLVED_ELSEWHERE.md was written.

Commands run:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T179/check_estimates.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_transfer.py
```

Both exited 0. The new diagnostic checked 27 rational Volterra parameter
triples, four Fourier/Gaussian heat-trace comparisons, and 24 exact
Gaussian density/sign/entropy cases. Actual priority was nice 20; peak
RSS was 13.27 MiB, runtime 0.002s. The launcher warning reflects the
inherited priority, verified inside both scripts. Full output is in LOG.md.
These are arithmetic diagnostics, not numerical tests of uniqueness.

What failed: applying full Novikov directly is not valid. For g=1, u0=0,
b(z)=kz, the drift-free law has E exp(A/2)=infinity whenever k^2 T^2>=3;
PROOF.md derives this sufficient, non-sharp divergence condition two ways.
The stopped-energy proof still works. No calculation or diagnostic failed.
A clarification removes a possible circular explanation: weak-to-mild
conversion under changed measures is localized before applying moment bounds.

Uncertainty: the conclusion retains the same external bounded-start
uniqueness input as round 3. No unresolved estimate is assumed in the new
transfer proof. No pathwise uniqueness or initial-data contraction for the
drifted equation is claimed.

Next worker: audit the canonical predictable-integral construction and the
entropy change of integrator in Sections 6–7. If these check, a concrete
next extension is a nonanticipating H-valued drift B(t,path), with growth
bounded by C(1+||path_t||_2). The current moment and energy estimates suggest
this transfer, but its path-space predictability hypotheses and density
construction should be written out before claiming it.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 04:59 Asia/Tbilisi.
