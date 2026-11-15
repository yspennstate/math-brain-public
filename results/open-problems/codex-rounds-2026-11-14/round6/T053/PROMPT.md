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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T053 (read it, never
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
VERDICT: PROVED stationary collision Palm law, finite positive collision intensity, and reciprocal-rate mean flight time at fixed density

The fixed-density CLT and planar recurrence remain unresolved. The bounded literature check found no solution elsewhere. No SOLVED_ELSEWHERE.md was created.

New beyond round 4: PROOF.md derives the collision ensemble from the stationary volume ensemble. Let theta be the probability that the origin belongs to unbounded vacancy, and let s_infinity be the mean exposed boundary area per unit spatial volume whose vacant side belongs to an unbounded component. With probability spherical velocity measure,
\[
 c_d=\frac{\kappa_{d-1}}{d\kappa_d},\qquad
 \gamma=\frac{c_ds_\infty}{\theta}.
\]
The expected number of collisions in any time interval of length T is exactly gamma*T. Given the boundary environment and outward obstacle normal n, the incoming velocity has law
\[
 \frac{(-v\cdot n)_+}{c_d}\,\sigma(dv).
\]
The full centered configuration is retained as a mark. The boundary environment marginal is its specific-area law normalized by s_infinity; it is not the origin-conditioned volume law.

Writing a=lambda*kappa_(d-1)*r^(d-1) and p0=exp(-lambda*kappa_d*r^d), the proof gives
\[
 \frac{(1-e^{-1})a}{1+\log(p_0/\theta)}
 \le \gamma \le \frac{a p_0}{\theta}<\infty.
\]
Positivity follows from a first-flight Poisson void bound, after establishing the exact expected-count formula. Under the collision Palm law, the mean time to the next collision is exactly 1/gamma. This uses the stationary marked time-count formula and exclusion of a collision-free subensemble, without assuming ergodicity or independent flights. No literature priority is claimed for these flux and Palm arguments.

The main technical step is an equality for the collision-history change of variables. Regular incoming tubes transfer the earlier phase-volume exceptional-set statement to surface flux. Spatial averaging then squeezes nonnegative marked collision counts between boundary integrals on cubes of radii R-T and R+T. This handles unbounded counts without taking a bounded-observable shell estimate beyond its scope.

Earlier result rechecked: the round-4 stationarity argument and almost-everywhere complete-flow construction hold. Section 8 of PROOF.md re-derives them. Both prior audit scripts were read and executed in memory, with no writes in their folders; both passed. The round-3 geometric exponent and the earliest logarithmic time-window witness also check.

Validation command:
~~~sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit_collision.py
~~~

Output: PASS. Independent hemisphere calculations agree within 4.86e-15; cosine-law second moments within 1.42e-14; all-vacancy rate normalizations within relative error 4.44e-16. The independent first-flight finite-difference check has relative error 5e-8, within its expected first-order error. Exact rational marked-count tests cover unequal periodic gaps and a nonergodic mixture, verifying the required event weighting and reciprocal-rate mean flight identity. Runtime was 0.027 seconds; peak resident memory 15,269,888 bytes; actual nice value 20. The script uses only bounded standard-library loops. LOG.md includes commands and full output for this and the earlier audits.

What failed or was corrected: no mathematical or numerical check failed. A draft overstatement about null exceptions at each fixed backward time was narrowed to the product flux-time nullity actually proved and needed. A command-string formatting issue and one JavaScript parse failure were corrected; the failed orchestration ran no shell command. The nice wrapper warned when attempting to raise inherited priority 20 to 15; the job remained at 20.

Limitations: no dynamical ergodicity, deterministic sample collision frequency, correlation decay, positive diffusivity, CLT, quenched limit, or recurrence estimate is proved. The mean flight identity concerns Palm sampling at collisions; the forward waiting time under volume sampling is different. The rate bounds are annealed and do not compute theta or s_infinity. The literature search was short, and the mathematical audit is internal.

Next worker: prove the invariance of the full boundary-mark law under the map taking one incoming collision state to the next, and derive a suspension identity relating the volume velocity correlation to collision marks and flight lengths. The collision sequence must retain its environment and variable flight times. A smaller check is the right derivative of the stationary velocity correlation at zero, using the proved cosine moment and an o(t) control of multiple-collision contributions. Neither calculation alone would control long-time correlations.

Opened primary sources for the bounded update: Karsten Matthies and Raphael Winter, [arXiv:2506.18539](https://arxiv.org/abs/2506.18539); Bálint Tóth, [arXiv:2501.00519](https://arxiv.org/abs/2501.00519); Yingxin Mu and Artem Sapozhnikov, [arXiv:2609.11690](https://arxiv.org/abs/2609.11690). Their abstract pages retain joint-limit or geometric-visibility scope. Also opened Patrick Charbonneau and Marcus Michelen, [arXiv:2611.07196](https://arxiv.org/abs/2611.07196); its abstract concerns high-dimensional void percolation, not billiard diffusion. None is a premise of the new proof.

Task: “Diffusion in the random Lorentz gas at fixed density” — 15 November 2026, 07:46 +04:00 (recorded session orientation).
