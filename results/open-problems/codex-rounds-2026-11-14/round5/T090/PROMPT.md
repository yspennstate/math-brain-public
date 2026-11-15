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
VERDICT: PROVED asymptotic sharpness of the Gaussian second-moment renewal lower endpoint at weak coupling

The round-3 result holds. Its Gaussian recursion was independently re-derived through a covariance determinant, its scalar renewal roots and rate argument check, and its script passed all 515 determinant cases again. A bounded literature check found no newer solution of the fixed-coupling KPZ problem. T090's growth exponents and height limit remain unresolved here.

The new result answers exactly the next question named in the round-3 report. For its flat-initial-data Itô SHE with diffusion coefficient 1/2, Gaussian covariance R_s(x)=(4 pi s)^(-1) exp(-|x|^2/(4s)), and g=b^2, write

\[
 \gamma(b,s)=\lim_{t\to\infty}t^{-1}\log\mathbb E[Z(t,0)^2].
\]

Then

\[
 \boxed{\gamma(b,s)=\frac{e^{-\gamma_{\rm E}}}{2s}
          e^{-4\pi/b^2}\bigl(1+O(b^2)\bigr)}.
\]

Here gamma_E is Euler's constant. Consequently, for the earlier root defined by g exp(x_g) E1(x_g)/(4 pi)=1,

\[
 \frac{\gamma(b,s)}{x_{b^2}/(2s)}=1+O(b^2)\longrightarrow1.
\]

The relative error can be chosen independent of s>0 by exact spatial scaling. For the prompt's diffusion coefficient 1, the corresponding formula is gamma_1(b,s)=(exp(-gamma_E)/s) exp(-8 pi/b^2)(1+O(b^2)).

[PROOF.md](PROOF.md) supplies the whole argument. It derives the free-resolvent constant from the heat kernel, controls the Gaussian tails by an explicit Hilbert–Schmidt remainder bound, proves the equality of the pointwise moment rate and the spectral threshold, and performs the rank-one eigenvalue expansion. The Gaussian finite constant is calculated twice, using the difference distribution and angular averaging. This is a step beyond the earlier folder, not a claim of a new general weak-bound-state phenomenon. Relevant existing spectral background is Jussi Behrndt, Petr Siegl, Nicolas Weber, [arXiv:2604.19284](https://arxiv.org/abs/2604.19284), and Sylwia Kondej, Vladimir Lotoreichik, [arXiv:1402.3995](https://arxiv.org/abs/1402.3995); the proof does not import a compact-support result for the Gaussian potential.

Reproduce the independent audits with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_prefactor.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T090/check_gaussian_renewal.py
```

The new audit passed. At s=1 the prefactor is approximately 0.28072974178344. Independent logarithmic-distance calculations across five covariance scales differed by at most 1.110e-14. Direct heat-resolvent quadrature recovered the finite constant -2 gamma_E. An additional zero-energy radial-ODE diagnostic agreed under step halving to 6.040e-13 and approached the independently predicted constant. Those ODE outputs are not finite-coupling eigenvalues. Runtime was 0.076 seconds and peak RSS 11.828 MiB. The earlier script took 0.051 seconds and used 12.406 MiB. These are floating-point checks; the theorem does not depend on them. Commands and full relevant output are in [LOG.md](LOG.md).

What failed: the sandbox rejected additional nice priority adjustment and Darwin address-space limiting. A separate Python priority query established inherited niceness 20, already lower priority than requested; the nice warning did not mean ordinary priority. Both calculations used one thread, a CPU limit, tiny fixed-size storage, and measured memory far below 1 GB. One log patch failed on a wrong anchor and changed nothing. No mathematical failure was found. No git, subagents, external messages, or writes outside this folder were used.

Limits and uncertainty: this is an annealed second-moment asymptotic for one mollifier. It does not control variance of log Z, establish beta or alpha, or produce a fixed-coupling height law. The bounded search is not an exhaustive literature review, and wider novelty of the explicit Gaussian prefactor is unassessed.

Next worker: retain the distinction between annealed moments and typical height. A concrete continuation of this calculation is to retain the next block-elimination term and prove a first relative correction, evaluating ||(I-P)Av||_2^2 for the Gaussian. The present O(b^2) bound does not identify that coefficient. Reaching T090 itself still requires control of centered log Z rather than its positive moments.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 04:47:12 +04; prompt receipt time unavailable.
