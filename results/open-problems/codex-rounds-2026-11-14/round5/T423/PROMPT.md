# Open problem T423: Pathwise uniqueness for the SPDE of super-Brownian motion in one dimension

Statement: On R, let W be space-time white noise and let u0 be a deterministic nonnegative smooth function of compact support. Are any two adapted, nonnegative, continuous, tempered mild solutions with finite total mass of du=(1/2)u_xx dt+sqrt(u)dW, driven by this same W and initial value, indistinguishable? There is no immigration term.

Source: Burdzy-Mueller-Perkins, Non-uniqueness for non-negative solutions of parabolic stochastic partial differential equations (arXiv:1008.2126); Chen (arXiv:1308.5141).

Where it stands (checked by us, Nov 2026): Weak uniqueness does not give pathwise uniqueness. The nonuniqueness in 1308.5141 includes immigration; the strong-solution equation in 1203.4873 is a different, cumulative-distribution SPDE.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T423 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T423 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T423 (read it,
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
VERDICT: PARTIAL exact inverse-time extinction-disagreement coefficient

For every fixed same-noise pair in T423, let U,V be the two total
masses, let delta_T be the probability that exactly one is zero at T,
and let L be symmetric local time at zero of U-V, normalized by Tanaka's
formula with coefficient one. Then

\[
\lim_{T\to\infty}T\delta_T
=2\mathbb E L_\infty
=2\lim_{t\to\infty}\mathbb E|U_t-V_t|\in[0,4m],
\qquad m=\int u_0.
\]

This improves round 3's liminf criterion to an existing limit with an
exact coefficient. Both predecessor main reductions hold on independent
re-derivation. The result does not solve pathwise uniqueness: proving
this coefficient is zero for actual same-noise spatial pairs remains open.
No novelty in the literature is claimed.

The new identity behind the limit is, for theta>0 and
b_s=theta/(1+(T-s)theta/2),

\[
\mathbb E|e^{-\theta U_T}-e^{-\theta V_T}|
=\mathbb E\int_0^T b_se^{-b_sU_s}\,dL_s.
\]

With theta=lambda/T, multiplication by T gives a kernel bounded by
lambda. Dominated convergence against the finite measure E dL proves
that its limit is (2lambda/(lambda+2))*E L_infinity. An explicit marginal
Laplace calculation approximates T*delta_T with error at most
8m/(lambda+2), uniformly in T. Letting lambda increase to infinity
proves the displayed result. PROOF.md supplies every step and the
integrability and endpoint justifications.

Checks: conditional Jensen independently gives the matching lower
bound; local-time transformation checks the min/max Tanaka factor;
independent and partially common Feller masses check coefficients 4m
and 4b against expected local times 2m and 2b. The standard-library
script audit.py checks the finite-parameter algebra, approximation
constant, scalar examples and document consistency. Run:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py
```

LOG.md records its output. These checks do not simulate the SPDE or
establish uniqueness. All writes are confined to this folder; no git,
subagents, global registrations or heavy computation were used.

What failed: the singular extinction kernel cannot be passed directly
through the large-time limit by dominated convergence. Finiteness of
expected total local time alone does not supply that domination. The
finite-parameter identity and uniform approximation avoid this problem.
The exact coefficient still does not bound local time by zero using
spatial information. No convergence rate or SPDE counterexample is claimed.

Literature check: less than five minutes, no verified resolution found.
Hao Wang's [arXiv:1612.06055](https://arxiv.org/abs/1612.06055) remains
withdrawn because of a gap in the main proof. The opened records for
Leonid Mytnik and Johanna Weinberger,
[arXiv:2509.10984](https://arxiv.org/abs/2509.10984), and Yi Han,
[arXiv:2611.07310](https://arxiv.org/abs/2611.07310), concern weak
uniqueness; the latter assumes uniformly nondegenerate diffusion.
Yu-Ting Chen's [arXiv:1308.5141](https://arxiv.org/abs/1308.5141)
concerns immigration. These records do not resolve the stated problem;
the bounded search is not a proof that no later resolution exists.

Next worker: target the local-time creation mechanism. It suffices to
prove E L_t=0 on each finite horizon, equivalently the small-occupation
estimate from the first report. The new formula identifies exactly how
any positive expected local time would persist as an inverse-time
extinction mismatch. Estimates involving arbitrary profiles or eventual
extinction alone still cannot give zero. A useful next spatial lemma
would rule out positive local time of U-V at equal total masses, despite
possible cancellation between regions with u>v and regions with u<v.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 06:39 Asia/Tbilisi session start.
