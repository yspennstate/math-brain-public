# Open problem T090: Kardar–Parisi–Zhang growth in 2+1 dimensions

Statement: Random surface growth in 2+1 dimensions in the isotropic KPZ class (the KPZ equation ∂_t h = Δh + λ|∇h|² + ξ in two space dimensions with spatially smoothed noise and fixed λ ≠ 0, or ballistic deposition and the Eden model) has nontrivial universal exponents: the height variance grows like t^{2β} with β ≈ 0.24, the roughness exponent is α ≈ 0.39, and the rescaled height has a non-Gaussian limit.

Caveat: The exponents are known only numerically. Isotropy matters: for anisotropic growth (AKPZ) fluctuations are predicted to be logarithmic (Wolf 1991).

Source: M. Kardar, G. Parisi and Y.-C. Zhang, Dynamic scaling of growing interfaces, Phys. Rev. Lett. 56 (1986); T. Halpin-Healy and Y.-C. Zhang, Kinetic roughening phenomena, stochastic growth, directed polymers and all that, Phys. Rep. 254 (1995)

Where it stands (checked by us, Nov 2026): When the coupling is sent to zero like 1/√log of the mollification scale, the limit is the Gaussian Edwards–Wilkinson equation (Chatterjee–Dunlap 2020; Caravenna–Sun–Zygouras, arXiv:1812.03911; Gu 2020), and at the critical coupling the critical 2D stochastic heat flow appears (Caravenna–Sun–Zygouras 2023; see also arXiv:2412.10311 and arXiv:2609.15832). Anisotropic models: logarithmic fluctuations for integrable AKPZ growth (Borodin–Ferrari 2014) and logarithmic superdiffusivity of the stationary AKPZ equation (Cannizzaro–Erhard–Toninelli, arXiv:2009.12934). In the isotropic strong-coupling regime nothing rigorous is known about the exponents, or even about the existence of a non-Gaussian universality class.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T090 (read it,
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
VERDICT: PARTIAL omitted critical-regime advance identified; fixed-coupling T090 remains open

The literature check found [arXiv:2610.31614v1](https://arxiv.org/abs/2610.31614v1), submitted 22 October 2026. Theorem-level scope, complete authors, and reference are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). This is an omitted advance beyond the results listed in the prompt, not a discovery published after November 2026.

Following step 1's stopping rule, no new proof or computation was attempted. Search queries, opened primary sources, and checks are recorded in [LOG.md](LOG.md). Reproduce the check with the web search query `"Critical 2D KPZ Process"`, then open `https://arxiv.org/html/2610.31614v1` and `https://arxiv.org/pdf/2610.31614`.

Audit: compared the abstract with Theorems 1.2 and 1.6 in both HTML and PDF, checked the hypotheses, and derived the vanishing-disorder scale directly from equations (1.5)–(1.6). The failed extension was interpreting critical convergence as a fixed-coupling theorem. No numerical exponent was obtained. The preprint's full proof was not independently audited.

Next worker: retain T090 as open, update its critical-regime background, and choose a separate fixed-coupling subproblem. Avoid replacing the long-time point-height question by the critical random-distribution limit.

Task: “push this problem forward by one checkable piece.” First recorded clock: 14 November 2026, 21:57:51 +04; prompt receipt time unavailable.
