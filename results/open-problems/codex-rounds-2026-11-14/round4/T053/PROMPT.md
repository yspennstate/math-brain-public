# Open problem T053: Diffusion in the random Lorentz gas at fixed density

Statement: A point particle moving at unit speed with specular reflection among fixed hard balls of radius r centred at the points of a Poisson process in R^d (d ≥ 2, fixed density and radius below the threshold at which the vacant set stops percolating, the particle started with a random direction in the unbounded component of the vacant set) behaves diffusively: X_t/√t converges to a non-degenerate Gaussian. In d = 2 the motion is recurrent.

Caveat: Started anywhere outside the balls the statement is false: with positive probability the origin lies in a bounded vacant cavity and the particle stays bounded (w672 audit, 14 Oct). Annealed or quenched limit to be fixed.

Source: H. A. Lorentz, The motion of electrons in metallic bodies, Proc. Amsterdam Acad. 7 (1905); H. Spohn, Large Scale Dynamics of Interacting Particles (Springer, 1991)

Where it stands (checked by us, Nov 2026): In the Boltzmann–Grad limit the motion becomes a Markov flight process (Gallavotti 1969; Spohn 1978; Boldrighini–Bunimovich–Sinai 1983); diffusion under a joint Boltzmann–Grad and diffusive scaling, past the kinetic time scale (Lutsko–Tóth, arXiv:1812.11325). Periodic scatterers: CLT with finite horizon (Bunimovich–Sinai 1981), √(t log t) with infinite horizon (Szász–Varjú 2007). Open at fixed density, including recurrence in d = 2.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T053 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T053 (read it,
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
VERDICT: PARTIAL fixed-density geometric flight bounds proved; diffusion and planar recurrence remain open

The earlier logarithmic time-window comparison holds. No fixed-density solution was found in the five-minute literature update. Matthies–Winter and Tóth still require simultaneous small-radius and long-time limits; neither gives the requested fixed-density CLT. No SOLVED_ELSEWHERE.md was created.

New beyond the earlier report: PROOF.md gives a self-contained fixed-density geometric lemma, explicit finite-scale probability bounds, and a billiard consequence. For Poisson intensity lambda>0, radius r>0, and d>=2, let M_R be the supremum of lengths of vacant straight segments with endpoints in the ball of radius R. With a=lambda*kappa_(d-1)*r^(d-1),

\[
\frac{M_R}{\log R}\longrightarrow\frac d a
\quad\text{almost surely}.
\]

The upper estimate uses deterministic position and direction nets with a reduced obstacle radius. The lower estimate uses independent empty sausages in disjoint cells. It gives the explicit bound

\[
\mathbb P(M_R<L)\le
\exp\{-N(R,L)e^{-\lambda\kappa_dr^d-aL}\},
\]

where N(R,L)=floor((2R/sqrt(d))/(L+3r))*floor((2R/sqrt(d))/(3r))^(d-1). The corresponding explicit upper bound is equation (2) in PROOF.md.

For every regular unit-speed billiard path starting at the origin, the longest collision-free portion G(T) before time T satisfies limsup G(T)/log T <= d/a. If its collisions are locally finite, its collision count satisfies liminf N_X(T)log T/T >= a/d. These statements hold simultaneously for all such paths in a probability-one set of environments, and survive conditioning on the origin being in an unbounded vacant component of positive probability. The lower bound for M_R does not locate its segments in that component.

The maximum-segment asymptotic is already covered by Yingxin Mu and Artem Sapozhnikov, *On the maximum visibility in a ball through the vacant set of Poissonian obstacles*, [arXiv:2609.11690v1](https://arxiv.org/abs/2609.11690v1), Theorem 1.1 and Remark 1.2. Their fixed-radius deviation bounds also imply almost-sure convergence by dyadic Borel--Cantelli. This session supplies an elementary proof and the trajectory corollary; no new literature theorem is claimed.

Validation command, from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit_geometry.py
```

Output: PASS; independent cap integration and volume formulas agree to relative error 7.83e-15; exact cell margins are r/2; the leading coefficient agrees with radius-one rescaling. Special cases are d/a=1/(lambda*r) in d=2 and 3/(lambda*pi*r^2) in d=3. The earlier scale witness was independently recomputed. Runtime was 0.006 seconds, peak resident memory 14,712,832 bytes, inherited nice priority 20. The script uses only the standard library and small bounded loops. Full command output and adversarial checks are in LOG.md.

What failed: two initial audit launches failed before computation because setrlimit rejected attempts to set address-space and data limits; their cause was not established. Those calls were removed, and the successful run reported its resident memory. A final file audit also needed its text-search sentinel corrected to the actual component caveat. No mathematical check failed. No diffusion simulation was attempted.

Limits and uncertainties: the result controls straight flights, including environment-dependent directions. It supplies no velocity decorrelation estimate and proves neither positive diffusivity nor recurrence. Global existence through singular billiard configurations is not proved; the trajectory corollary assumes regular locally finite collisions. The literature search was bounded and does not prove absence of a solution.

The formulation for future work is fixed explicitly in LOG.md: condition the Poisson environment on the origin lying in an unbounded open vacant component and choose an independent uniform initial direction. Annealed convergence averages the environment and direction; quenched convergence fixes almost every conditioned environment and averages direction only.

Next worker: establish invariance of this conditioned environment-and-velocity law under the environment seen from the billiard particle, using spatial averaging and Liouville measure. Do not assume ergodicity. This is a separate fixed-density lemma needed before using stationary velocity correlations; the present geometric bound cannot justify a Green--Kubo or regeneration argument.

Opened sources verifying the earlier work: Karsten Matthies and Raphael Winter, [arXiv:2506.18539v2, Theorem 3.1](https://arxiv.org/html/2506.18539v2#S3); Bálint Tóth, [arXiv:2501.00519v2, Theorems 2--3](https://arxiv.org/html/2501.00519v2); Christopher Lutsko and Bálint Tóth, [arXiv:1812.11325](https://arxiv.org/abs/1812.11325). Search queries and opened URLs are recorded in LOG.md.

Task: “Diffusion in the random Lorentz gas at fixed density” — 15 November 2026, 01:01 +04:00 (recorded session orientation time).
