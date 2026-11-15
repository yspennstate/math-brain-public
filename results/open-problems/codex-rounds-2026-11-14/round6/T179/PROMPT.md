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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T179 (read it, never
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
VERDICT: PROVED nonanticipating H-valued linear-growth drift extension, conditional on the prior drift-free input

The round-4 result checks. Independently reconstructed its canonical
predictable integral, its change of integrator, and both entropy identities.
Re-ran its arithmetic diagnostic and the round-3 diagnostic successfully.
No error was found. The full-positive-Hölder bounded-start uniqueness
theorem remains an external input.

The new piece replaces the pointwise drift b(t,x,u) by any jointly Borel
nonanticipating map

    B: [0,T] x C([0,T];L2(T)) -> L2(T),
    ||B(t,path)||_2 <= K(1+||path_t||_2).

PROOF.md establishes weak existence and uniqueness of the state-path law
for this equation, allowing unbounded elliptic globally beta-Hölder g,
0<beta<1, and every deterministic L2 initial state. It also establishes
equivalence with the drift-free law and the two finite entropy identities

    Ent(mu_B | mu_0) = (1/2) E_mu_B A_B,
    Ent(mu_0 | mu_B) = (1/2) E_mu_0 A_B,
    A_B = integral ||B(t,path)/g(path_t)||_2^2 dt.

The additional technical step is a predictable representative defined on
canonical path space independently of the probability law. One-sided
Bochner time averages converge to B for almost every time on every path;
their predictable limit preserves the current-norm growth bound. This
allows the stopped Girsanov proof to handle arbitrary spatial nonlocality
and history dependence. A running-threshold drift gives an explicit
example. No Markov assumption on the drifted state is needed.

The transfer method builds on Section 8.2 of Yi Han,
*Weak uniqueness for the stochastic heat equation with nondegenerate
diffusion: the full Hölder regime*,
[arXiv:2611.07310v1](https://arxiv.org/html/2611.07310v1).
Its Proposition 8.1 is the bounded-start input used by round 3. The brief
literature check found the same version and scope; no later result changed
the earlier picture. This is an extension of the prior reports, not an
independent proof of Han's main theorem. No new SOLVED_ELSEWHERE.md was
written.

Commands, all exiting 0:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T179/check_transfer.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T179/check_estimates.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_history.py
```

The new diagnostic checked 54 two-stage history-dependent Gaussian laws
by one-dimensional quadrature. It checks normalization and both entropy
directions, including cases where they differ. The largest residual was
9.83e-11. Four exact piecewise-polynomial calculations also checked causal
time-average errors. Actual nice was 20, runtime 0.284s, peak RSS 13.02 MiB.
The launcher warning concerns inherited priority, verified inside the
scripts. Full outputs are in LOG.md. These are arithmetic diagnostics,
not simulations or numerical tests of SPDE uniqueness.

What failed: ordinary left-endpoint sampling cannot approximate arbitrary
Borel time dependence. For B(t,path)=1_Q(t)e, all rational left-endpoint
sums equal Te although the time integral is zero. The proof uses causal
averages instead. No diagnostic failed. One log patch failed context
matching and was reapplied.

Uncertainty and limits: the same external drift-free uniqueness input
remains unaudited in full. No unresolved estimate is assumed in the new
transfer proof. Growth in the running path supremum is not covered by its
current-norm estimate. No pathwise uniqueness or beta=0 result is claimed.

Next worker: audit the universal predictable representative and the
weighted approximation under equivalent measures in Sections 1 and 5.
If those check, extend the growth hypothesis to
`||B(t,path)|| <= K(1+sup_(r<=t)||path_r||)` by proving a uniform stopped
maximal-moment estimate. This would include unbounded delay drifts; the
present fixed-time moment estimate alone does not justify that extension.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 08:32 Asia/Tbilisi.
