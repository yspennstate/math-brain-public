# Open problem T423: Pathwise uniqueness for the SPDE of super-Brownian motion in one dimension

Statement: On R, let W be space-time white noise and let u0 be a deterministic nonnegative smooth function of compact support. Are any two adapted, nonnegative, continuous, tempered mild solutions with finite total mass of du=(1/2)u_xx dt+sqrt(u)dW, driven by this same W and initial value, indistinguishable? There is no immigration term.

Source: Burdzy-Mueller-Perkins, Non-uniqueness for non-negative solutions of parabolic stochastic partial differential equations (arXiv:1008.2126); Chen (arXiv:1308.5141).

Where it stands (checked by us, Nov 2026): Weak uniqueness does not give pathwise uniqueness. The nonuniqueness in 1308.5141 includes immigration; the strong-solution equation in 1203.4873 is a different, cumulative-distribution SPDE.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T423 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T423 (read it,
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
VERDICT: PARTIAL terminal extinction synchrony and a natural-scale disagreement criterion

The earlier terminal-mass reduction holds. It was re-derived from the
mild equation using spatial heat-kernel testing, and checked by expanding
the two marginal variances and cross covariance. Averaging Tanaka's
formula over levels independently verifies its occupation normalization
and epsilon/2 error bound.

The new result replaces terminal mass equality by equality of one binary
observation. For a fixed same-noise pair and deterministic T>0,

\[
u=v\text{ on }[0,T]\times\mathbb R
\quad\Longleftrightarrow\quad
\mathbf1_{\{\int u_T=0\}}=\mathbf1_{\{\int v_T=0\}}
\text{ almost surely}.
\]

The proof derives, in the actual joint filtration,
\(\mathbb P(U_T=0\mid\mathcal F_t)=\exp(-2U_t/(T-t))\), where
\(U_t=\int u_t\) and \(V_t=\int v_t\). Equality of the terminal indicators
therefore forces equality of all earlier masses, then of the fields.
This uses the almost-sure equality of the events, not just equality of
their probabilities or their coincidence on a positive-probability set.

Write \(\delta_T\) for the probability that exactly one terminal mass is
zero. PROOF.md gives its exact white-noise energy identity and a stopped
bound on the unweighted discrepancy. Absorption at zero gives the further
criterion

\[
u,v\text{ indistinguishable for all times}
\quad\Longleftrightarrow\quad
\liminf_{T\to\infty}T\delta_T=0.
\]

Every pair satisfies \(\delta_T\leq4m/T\), where \(m=\int u_0\).
For every fixed t>0,

\[
\liminf_{T\to\infty}T\delta_T
\geq2\mathbb E[(U_t+V_t)
 \mathbf1_{\{\text{exactly one of }U_t,V_t\text{ is zero}\}}].
\]

Any pair that disagrees with positive probability before t has a strictly
positive right side. Thus nonuniqueness would force extinction disagreement
at the natural inverse-time scale. This is a new reduction beyond the
earlier report, with no claim of novelty in the literature. It does not
resolve T423: extinction synchrony and the required improvement over
the automatic O(1/T) estimate remain unproved.

Checks and commands: all substantive arguments and independent checks are
in PROOF.md; LOG.md records the steps. The small standard-library script
is run with

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py
```

It checks exact algebra, the occupation normalization, Bernoulli bounds,
a deterministic obstruction, tail scaling, and document consistency.
It is not a simulation or verification of the SPDE theorem. Processes
inherit nice 20, below the requested priority; the nice wrapper warns
when it attempts to change that value to 15. No heavy computation, git,
subagents, or writes outside this folder were used.

What failed: the new weighted energy does not bound the original spatial
discrepancy by an unconditional positive constant. The exact test
u=f, v=4f, integral f=1, q=log(2)/3 makes its weighted square-root
difference zero while the unweighted squared difference integrates to
one. The mass-capped inverse estimate is valid, but its constant grows
with the cap and cannot be sent to infinity to close the problem.
Equal-mass profile counterexamples from the preceding report remain
obstructions. None of these profiles constructs SPDE nonuniqueness.

Literature check: less than five minutes; no verified resolution found.
Only sources actually opened are cited here. Hao Wang's
[arXiv:1612.06055](https://arxiv.org/abs/1612.06055) remains withdrawn
because of a gap in the main proof. The opened recent records do not
prove the stated density-SPDE result:

- Leonid Mytnik and Johanna Weinberger,
  [arXiv:2509.10984v3](https://arxiv.org/abs/2509.10984v3): weak existence
  and uniqueness with irregular drift.
- Yi Han, [arXiv:2611.07310](https://arxiv.org/abs/2611.07310): weak
  uniqueness with uniformly nondegenerate diffusion.
- Jie Xiong and Wen Xu,
  [arXiv:2607.22220v2](https://arxiv.org/abs/2607.22220v2): cyclic
  catalytic finite-dimensional SDEs.

Yu-Ting Chen's [arXiv:1308.5141](https://arxiv.org/abs/1308.5141)
concerns nonuniqueness with immigration. Search coverage is limited;
absence of a hit is not proof of absence of a later solution.

Next worker: choose either the finite-horizon event criterion or the
large-time criterion as a target. A concrete sufficient estimate is
\(\delta_{T_j}=o(1/T_j)\) along some deterministic sequence
\(T_j\to\infty\), for every same-noise pair. The new proof shows why
the automatic eventual extinction of both populations does not suffice:
its rate of disagreement matters. Any attack must use spatial information
about the actual pair. Check proposed weighted-energy comparisons against
the explicit profile obstruction before using them. The conditional-law
and terminal-limit steps have been proved; the unresolved part is the
synchrony estimate itself.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 03:51 Asia/Tbilisi session start.
