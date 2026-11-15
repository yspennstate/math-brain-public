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
