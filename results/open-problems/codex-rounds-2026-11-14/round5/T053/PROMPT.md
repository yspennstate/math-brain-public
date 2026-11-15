# Open problem T053: Diffusion in the random Lorentz gas at fixed density

Statement: A point particle moving at unit speed with specular reflection among fixed hard balls of radius r centred at the points of a Poisson process in R^d (d ≥ 2, fixed density and radius below the threshold at which the vacant set stops percolating, the particle started with a random direction in the unbounded component of the vacant set) behaves diffusively: X_t/√t converges to a non-degenerate Gaussian. In d = 2 the motion is recurrent.

Caveat: Started anywhere outside the balls the statement is false: with positive probability the origin lies in a bounded vacant cavity and the particle stays bounded (w672 audit, 14 Oct). Annealed or quenched limit to be fixed.

Source: H. A. Lorentz, The motion of electrons in metallic bodies, Proc. Amsterdam Acad. 7 (1905); H. Spohn, Large Scale Dynamics of Interacting Particles (Springer, 1991)

Where it stands (checked by us, Nov 2026): In the Boltzmann–Grad limit the motion becomes a Markov flight process (Gallavotti 1969; Spohn 1978; Boldrighini–Bunimovich–Sinai 1983); diffusion under a joint Boltzmann–Grad and diffusive scaling, past the kinetic time scale (Lutsko–Tóth, arXiv:1812.11325). Periodic scatterers: CLT with finite horizon (Bunimovich–Sinai 1981), √(t log t) with infinite horizon (Szász–Varjú 2007). Open at fixed density, including recurrence in d = 2.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T053 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T053 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T053 (read it,
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
VERDICT: PROVED invariance of the conditioned environment-and-velocity law at fixed density

The fixed-density diffusion and planar recurrence problems remain open. No solution elsewhere was found in the literature update, which ended within five minutes. No SOLVED_ELSEWHERE.md was created.

New beyond round 3: PROOF.md proves the proposed stationarity lemma. Let H be the event that the origin lies in an unbounded open vacant component, theta=P(H)>0, Q=P(.|H), and sigma uniform probability measure on the velocity sphere. For the billiard started at the origin with law Q tensor sigma,

\[
(\tau_{X_t}\omega,V_t)\ \stackrel{\mathrm{law}}=\ Q\otimes\sigma
\]

at every deterministic time t. The resulting environment process is stationary. No ergodicity or uniqueness of the unbounded component is assumed. The proof uses Liouville measure and finite-speed spatial averaging, with an explicit error supported in a shell of relative volume [(1+|t|/R)^d-(1-|t|/R)^d]. It covers bounded measurable observables of the entire environment.

The well-posedness justification is included: for almost every initial phase point, the billiard has a two-sided regular trajectory with locally finite collisions, even though obstacle balls overlap. Finite singular encounters are null by dimension counting. A local collision-flux bound excludes finite-time accumulation without assuming global existence first. Translation invariance and Tonelli then transfer the spatial almost-everywhere assertion to the fixed origin under Q tensor sigma. This removes round 3's regular-trajectory caveat for this initial law, while retaining exceptional directions.

A direct consequence is the exact finite-time identity

\[
\mathbb E[X_tX_t^{\mathsf T}]
 =\frac{2I_d}{d}\int_0^t(t-s)\mathbb E[V_0\cdot V_s],ds.
\]

The infinite-time formula is stated only under an additional, unproved absolute-integrability hypothesis on the velocity correlation. Neither positive diffusivity nor a CLT follows from stationarity alone. These elementary invariant-measure arguments are new relative to the supplied folders; no literature priority is claimed.

Earlier result rechecked: the independent cell exponent is (d-ac) log R-log log R+O(1), and the net exponent is (d-bc) log R+(d-1) log log R+O(1), with b increasing to a. They confirm the earlier maximum-segment constant d/a, its dyadic almost-sure argument, and its trajectory corollary with the stated component caveat. The unmodified earlier audit was also executed in memory and passed. Its maximum sausage-volume discrepancy was 7.83e-15. The earliest logarithmic time-window witness checks as well.

Validation command from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit_stationarity.py
```

Output: PASS. Hemisphere projection and independent angular integration agree within 4.63e-14; tube Jacobians within 8.88e-16; shell formulas within 1.78e-15. The time-square, triangle, and closed-form checks confirm the covariance factors, with finite-grid error at most 2.5e-7. Runtime was 0.004 seconds and peak resident memory 12,795,904 bytes. Actual nice value was 20. LOG.md records the complete output and the in-memory earlier-audit command. All code uses bounded standard-library loops and one thread.

What failed or remains uncertain: no mathematical check failed. The nice wrapper warned when trying to raise inherited priority 20 to 15; the actual process remained at the lower priority 20. No decay, mixing, ergodicity, quenched limit, positive diffusivity, or recurrence estimate has been obtained. The literature search was bounded, and the proof has only the internal independent checks recorded here.

Next worker: derive the stationary collision Palm law from the flux construction. Normalize incoming velocity by |v dot n| on exposed boundary patches adjacent to unbounded vacancy, and express the mean collision rate through that boundary's mean area per unit volume. Establish finiteness and the normalization without assuming ergodicity. After that, the missing dynamical issue is quantitative control of velocity correlations or a suitable martingale approximation; neither follows from the geometric flight bound.

Opened primary sources confirming scope: Karsten Matthies and Raphael Winter, [arXiv:2506.18539v2](https://arxiv.org/html/2506.18539v2); Bálint Tóth, [arXiv:2501.00519v2](https://arxiv.org/abs/2501.00519v2); Yingxin Mu and Artem Sapozhnikov, [arXiv:2609.11690v1](https://arxiv.org/html/2609.11690v1). Their joint-limit and visibility results do not supply fixed-density diffusion.

Task: “Diffusion in the random Lorentz gas at fixed density” — 15 November 2026, 04:25 +04:00 (session orientation time).
