# Open problem T090: Kardar–Parisi–Zhang growth in 2+1 dimensions

Statement: Random surface growth in 2+1 dimensions in the isotropic KPZ class (the KPZ equation ∂_t h = Δh + λ|∇h|² + ξ in two space dimensions with spatially smoothed noise and fixed λ ≠ 0, or ballistic deposition and the Eden model) has nontrivial universal exponents: the height variance grows like t^{2β} with β ≈ 0.24, the roughness exponent is α ≈ 0.39, and the rescaled height has a non-Gaussian limit.

Caveat: The exponents are known only numerically. Isotropy matters: for anisotropic growth (AKPZ) fluctuations are predicted to be logarithmic (Wolf 1991).

Source: M. Kardar, G. Parisi and Y.-C. Zhang, Dynamic scaling of growing interfaces, Phys. Rev. Lett. 56 (1986); T. Halpin-Healy and Y.-C. Zhang, Kinetic roughening phenomena, stochastic growth, directed polymers and all that, Phys. Rep. 254 (1995)

Where it stands (checked by us, Nov 2026): When the coupling is sent to zero like 1/√log of the mollification scale, the limit is the Gaussian Edwards–Wilkinson equation (Chatterjee–Dunlap 2020; Caravenna–Sun–Zygouras, arXiv:1812.03911; Gu 2020), and at the critical coupling the critical 2D stochastic heat flow appears (Caravenna–Sun–Zygouras 2023; see also arXiv:2412.10311 and arXiv:2609.15832). Anisotropic models: logarithmic fluctuations for integrable AKPZ growth (Borodin–Ferrari 2014) and logarithmic superdiffusivity of the stationary AKPZ equation (Cannizzaro–Erhard–Toninelli, arXiv:2009.12934). In the isotropic strong-coupling regime nothing rigorous is known about the exponents, or even about the existence of a non-Gaussian universality class.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T090 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T090 (read it,
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
VERDICT: PARTIAL explicit Gaussian-covariance second-moment bounds; fixed-coupling KPZ exponents remain open

The earlier report's main claim holds: critical tuning sends the coupling to zero, so its cited theorem does not establish fixed-coupling KPZ scaling. Independently, the discrete tuning gives beta_N^2 log N -> pi, and the continuum tuning gives beta_epsilon^2 |log epsilon| -> 2*pi. A bounded literature check found no newer solution of T090. The critical result remains [The Critical 2D KPZ Process](https://arxiv.org/abs/2610.31614); full author names and the opened sources are recorded in LOG.md.

New beyond the earlier report is a proved fixed-coupling special-case estimate. For the flat-initial-data Itô equation

\[
 dZ=\tfrac12\Delta Z\,dt+bZ\,W_s(dt,x),\qquad
 R_s(x)=\frac{e^{-|x|^2/(4s)}}{4\pi s},\quad s>0,
\]

let x_g solve

\[
 \frac{g}{4\pi}e^{x_g}E_1(x_g)=1,\qquad g=b^2.
\]

Then the second-moment rate exists and satisfies

\[
 \frac{x_g}{2s}\le
 \lim_{t\to\infty}\frac1t\log\mathbb E[Z(t,0)^2]
 \le\frac{x_g}{s}.
\]

PROOF.md gives the stronger finite-time sandwich by scalar renewal functions, the Gaussian integration at every interaction, the rate-existence argument, and independent determinant identities. It also proves the weak-coupling logarithmic scale

\[
 b^2\log(s\gamma(b,s))\longrightarrow-4\pi.
\]

For diffusion coefficient 1 instead of 1/2, the corresponding constant is -8*pi. This normalization matters when relating the statement to the prompt. The Cole–Hopf conversion, including the deterministic Itô correction, is written out in PROOF.md.

This is a new calculation relative to the earlier folder, not a claimed new intermittency phenomenon. Second-moment intermittency in dimension two is established background; see Le Chen and Kunwoo Kim, [Nonlinear stochastic heat equation driven by spatially colored noise: moments and intermittency](https://arxiv.org/abs/1510.06046). Novelty of the particular explicit sandwich in the wider literature has not been checked.

Reproduce the audit with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_gaussian_renewal.py
```

The independent covariance-determinant calculation passed 515 cases, with maximum absolute log-product discrepancy 9.663e-13. Independent scalar integrals agreed to relative error 1.238e-12. Three closed-form two-interaction cases and four scaling checks also passed. For b=s=1 the two scalar rate endpoints are approximately 9.79026725e-7 and 1.95805345e-6. These decimal values are floating-point checks; the inequalities are proved analytically. Runtime was 0.051 seconds and peak RSS was 12.609 MiB.

What failed: the first script launch stopped at an unsupported address-space resource-limit operation, before doing calculations. The corrected script reports that limitation and installs a CPU limit. The sandbox denied changing nice priority on every invocation; the run was therefore at ordinary priority despite using the requested command. The computation was single-threaded and stayed far below 1 GB.

Limits and uncertainty: the proof uses a Gaussian covariance and flat initial data. These annealed exponential moments do not control the variance of the logarithm. LOG.md gives an explicit mean-one random-variable example with exponentially growing second moment and vanishing log variance. Thus no beta or alpha estimate, universal height law, or typical-height crossover time follows here. No counterexample to the stated special-case proposition was found.

Next worker: a concrete continuation is to prove or disprove asymptotic sharpness of the lower endpoint, namely gamma(b,s)/(x_{b^2}/(2s)) -> 1 as b -> 0, using a two-dimensional resolvent expansion. That would sharpen this moment estimate; it would still require a separate argument to reach the log-height fluctuations in T090.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 01:20:02 +04; prompt receipt time unavailable.
