# Open problem T090: Kardar–Parisi–Zhang growth in 2+1 dimensions

Statement: Random surface growth in 2+1 dimensions in the isotropic KPZ class (the KPZ equation ∂_t h = Δh + λ|∇h|² + ξ in two space dimensions with spatially smoothed noise and fixed λ ≠ 0, or ballistic deposition and the Eden model) has nontrivial universal exponents: the height variance grows like t^{2β} with β ≈ 0.24, the roughness exponent is α ≈ 0.39, and the rescaled height has a non-Gaussian limit.

Caveat: The exponents are known only numerically. Isotropy matters: for anisotropic growth (AKPZ) fluctuations are predicted to be logarithmic (Wolf 1991).

Source: M. Kardar, G. Parisi and Y.-C. Zhang, Dynamic scaling of growing interfaces, Phys. Rev. Lett. 56 (1986); T. Halpin-Healy and Y.-C. Zhang, Kinetic roughening phenomena, stochastic growth, directed polymers and all that, Phys. Rep. 254 (1995)

Where it stands (checked by us, Nov 2026): When the coupling is sent to zero like 1/√log of the mollification scale, the limit is the Gaussian Edwards–Wilkinson equation (Chatterjee–Dunlap 2020; Caravenna–Sun–Zygouras, arXiv:1812.03911; Gu 2020), and at the critical coupling the critical 2D stochastic heat flow appears (Caravenna–Sun–Zygouras 2023; see also arXiv:2412.10311 and arXiv:2609.15832). Anisotropic models: logarithmic fluctuations for integrable AKPZ growth (Borodin–Ferrari 2014) and logarithmic superdiffusivity of the stationary AKPZ equation (Cannizzaro–Erhard–Toninelli, arXiv:2009.12934). In the isotropic strong-coupling regime nothing rigorous is known about the exponents, or even about the existence of a non-Gaussian universality class.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T090 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T090 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T090 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T090 (read it, never
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
VERDICT: PROVED first relative correction to the Gaussian second-moment weak-coupling asymptotic

The round-4 result holds. Its resolvent normalization, Gaussian finite constant, and spectral identification were independently rederived, and its numerical audit passed again. A bounded literature check found no newer solution of fixed-coupling T090. The already identified [critical-process result](https://arxiv.org/abs/2610.31614) remains outside that regime; complete source attribution is in LOG.md.

The new result is exactly the continuation named by round 4. For its flat-initial-data Itô SHE with diffusion coefficient 1/2 and Gaussian covariance R_s(x)=(4*pi*s)^(-1) exp(-|x|^2/(4s)),

\[
 \boxed{\gamma(b,s)=\frac{e^{-\gamma_{\rm E}}}{2s}e^{-4\pi/b^2}
 \left[1+\frac{\operatorname{Li}_2(1/4)}{4\pi}b^2+O(b^4)\right].}
\]

Here gamma is the long-time exponential rate of E[Z(t,0)^2]. The relative remainder is uniform over s>0. The ratio to the earlier renewal lower endpoint x_(b^2)/(2s) has the same bracket. Thus its first gap is positive, with coefficient

\[
 \frac{\operatorname{Li}_2(1/4)}{4\pi}
 =0.021299120270804\ldots.
\]

[PROOF.md](PROOF.md) gives every step. Retaining the next block term gives c=||(I-P)Av||^2=Li_2(1/4)/(16*pi^2). Two analytic calculations of that variance, and two algebraic derivations of its contribution to log gamma, agree. For diffusion coefficient d, the exponential constant is 8*pi*d and the relative correction is Li_2(1/4)*b^2/(8*pi*d). This calculation makes no claim of priority in the wider spectral literature.

Reproduce the audits with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_correction.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T090/check_prefactor.py
```

The new audit passed. Radial quadrature, a covariance double integral, and the positive dilogarithm series agree to about 1e-15. Nine special-function checks and five covariance scales passed. A separate zero-energy ODE diagnostic approaches the predicted coefficient; extrapolation from its last two couplings differs by 2.855e-8. These are floating-point checks, not certified enclosures or finite-coupling eigenvalues. Runtime was 0.245 seconds, peak RSS 12.031 MiB. The earlier audit also passed, in 0.112 seconds and 12.656 MiB. Commands and relevant output are in [LOG.md](LOG.md).

What failed: the sandbox rejected the requested incremental nice adjustment and Darwin address-space limiting. A direct query confirmed inherited niceness 20, already below the requested priority. Both audit scripts used one thread and a 60-second CPU limit. No mathematical failure was found.

Limits and uncertainty: this improves an annealed second-moment expansion for one Gaussian covariance. It does not estimate the variance of log Z, prove beta or alpha, or construct a fixed-coupling height limit. T090 remains open here. The status search was bounded, and wider novelty of the explicit coefficient was not investigated.

Next worker: a concrete continuation within this calculation is to retain the next Neumann term and evaluate the Gaussian quantity <h,QAQ h>, h=QAv, which controls the b^4 term in log gamma. A step toward T090 itself instead needs control of centered log Z; additional positive-moment coefficients alone do not provide it.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 08:12:26 +04; prompt receipt time unavailable.
