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
