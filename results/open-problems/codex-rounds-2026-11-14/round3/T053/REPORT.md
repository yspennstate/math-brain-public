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
