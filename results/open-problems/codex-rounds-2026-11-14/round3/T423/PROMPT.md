# Open problem T423: Pathwise uniqueness for the SPDE of super-Brownian motion in one dimension

Statement: On R, let W be space-time white noise and let u0 be a deterministic nonnegative smooth function of compact support. Are any two adapted, nonnegative, continuous, tempered mild solutions with finite total mass of du=(1/2)u_xx dt+sqrt(u)dW, driven by this same W and initial value, indistinguishable? There is no immigration term.

Source: Burdzy-Mueller-Perkins, Non-uniqueness for non-negative solutions of parabolic stochastic partial differential equations (arXiv:1008.2126); Chen (arXiv:1308.5141).

Where it stands (checked by us, Nov 2026): Weak uniqueness does not give pathwise uniqueness. The nonuniqueness in 1308.5141 includes immigration; the strong-solution equation in 1203.4873 is a different, cumulative-distribution SPDE.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T423 (read it,
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
VERDICT: PARTIAL exact reduction to terminal-mass equality and a scalar occupation estimate

For any fixed pair of solutions driven by the same white noise and any
finite deterministic T, PROOF.md proves that equality of their terminal
total masses almost surely is equivalent to equality of the full fields
throughout [0,T]. Writing D for the mass difference and A for the spatial
integral of (sqrt(u)-sqrt(v))^2 gives

\[
\mathbb E D_T^2=\mathbb E\int_0^T A_s\,ds.
\]

The remaining condition is exactly

\[
\mathbb E\int_0^T
 \mathbf1_{\{|D_s|<\varepsilon\}}A_s\,ds=o(\varepsilon).
\]

The normalized occupation expression tends to E|D_T|, also the expected
symmetric local time at zero of D; its finite-width error is at most
epsilon/2. There is a quantitative consequence:

\[
\mathbb E\int_0^T\|u_s-v_s\|_1\,ds
 \leq2\sqrt{mT\,\mathbb E D_T^2}.
\]

In particular the unnormalized occupation integral equals
2*epsilon*E|D_T| with an error between -epsilon squared and zero.
It is always O(epsilon), while uniqueness requires o(epsilon).

The proof uses the known single-solution super-Brownian marginal law
only for continuous total mass and its first moment m. It then derives
the same-white-noise joint bracket directly. This is a reduction, with
no claim of novelty. It does not prove the required occupation estimate
or resolve pathwise uniqueness for nonzero initial mass.

Checks: the bracket identity is independently re-derived by expanding
the two-mass covariance; the local-time normalization is checked with
both a piecewise quadratic and a smooth convex approximation. The
spatial Cauchy--Schwarz constant is checked on proportional profiles.
The marginal second-moment coefficient is also checked by deriving the
Feller mass Laplace transform.
Zero mass, vanishing denominators, all-space cutoffs, endpoint times,
and the upgrade from almost-everywhere equality to indistinguishability
are treated explicitly.

What failed: equal masses do not algebraically control A. Disjoint
smooth profiles, and arbitrarily close equal-mass mixtures, demonstrate
the obstruction. These are tests of an inequality, not SPDE
counterexamples. Projecting the common white noise onto the two mass
processes gives scalar drivers with correlation C/sqrt(UV), which need
not be one. Applying scalar pathwise uniqueness with an assumed common
Brownian driver would therefore be invalid.

Literature search: approximately 2.3 minutes, within the ten-minute cap.
No verified resolution of this exact equation was found. Hao Wang's
[arXiv:1612.06055](https://arxiv.org/abs/1612.06055) was withdrawn because
of a gap in the main proof. The recent papers opened do not establish
the theorem asked for:

- Leonid Mytnik and Johanna Weinberger,
  [arXiv:2509.10984v3](https://arxiv.org/abs/2509.10984v3):
  weak existence and uniqueness with irregular drift.
- Jie Xiong and Wen Xu,
  [arXiv:2610.41400](https://arxiv.org/abs/2610.41400):
  catalytic systems with colored noise and inward-drift assumptions.
- Yi Han, [arXiv:2611.07310](https://arxiv.org/abs/2611.07310):
  weak uniqueness with uniformly nondegenerate diffusion.

The original distinctions are confirmed by Yu-Ting Chen,
[arXiv:1308.5141](https://arxiv.org/abs/1308.5141), and Jie Xiong,
[arXiv:1203.4873](https://arxiv.org/abs/1203.4873). The latter explicitly
explains why uniqueness for its distribution-function equation does not
transfer to the density equation. Search coverage is limited; absence
of a hit is not proof that no later result exists.

Commands and saved work: LOG.md records the search queries and local
commands. The proof is analytic; no simulation or numerical computation
supports its conclusions. Files were written with apply_patch and read
back with sed. Local commands were prefixed by OMP_NUM_THREADS=1 and
nice -n 15 after the initial negligible directory listing. The nice
wrapper warned because processes already inherit nice 20, confirmed by
Python's os.getpriority. No git, subagents, external writes, or heavy
computation were used.

Next worker: investigate the occupation estimate above using spatial
information specific to same-noise solution pairs. A useful estimate
must control cancellation between regions where u>v and u<v; arbitrary
profile inequalities cannot suffice. Check any proposed estimate against
the equal-mass examples in PROOF.md before attempting to close it.

Task: “push this problem forward by one checkable piece” — 14 November
2026, 22:14 Asia/Tbilisi session start.
