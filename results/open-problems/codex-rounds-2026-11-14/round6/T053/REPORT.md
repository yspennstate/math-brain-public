VERDICT: PROVED invariant collision map and exact suspension and velocity-correlation representations at fixed density

The fixed-density Gaussian limit and planar recurrence remain unresolved. The bounded literature check found no solution elsewhere; no SOLVED_ELSEWHERE.md was created.

New beyond round 5: PROOF.md proves that the full incoming collision-mark law nu is invariant under the next-collision map S. The proof uses a bounded endpoint cancellation in a finite time window and the earlier marked Campbell identity, without an ergodic theorem. The mark retains the full centered configuration, normal and incoming velocity.

The stationary time law is recovered as the variable-roof suspension
\[
 \widehat\mu(dM,ds)=\gamma\nu(dM)1_{\{0\le s<\ell(M)\}}ds.
\]
Its current-flight mark law is gamma*ell*nu, with uniform age within that flight. Following the interior state backwards to its most recent collision supplies the inverse identification. Thus this represents the entire stationary flow, including variable flight times.

With outgoing flight velocities w_n, lengths ell_n, cumulative times L_n, and overlap weights
\[
 A_n(t,M)=\bigl|[0,\ell_0)\cap[L_n-t,L_{n+1}-t)\bigr|,
\]
the stationary correlation is exactly
\[
 C(t)=\gamma\sum_{n\ge0}\nu[(w_0\cdot w_n)A_n(t,M)].
\]
The absolute majorant is gamma*nu(ell)=1. Equation (14) of PROOF.md gives an explicit collision series for its Laplace transform at every real z>0, with a finite-index tail bound. A pointwise telescoping calculation controls the entire absolute majorant by 1/z; no second flight-time moment is assumed. These are elementary Palm and suspension identities, with no literature-priority claim.

Earlier result rechecked: the round-5 marked collision law, positive finite rate and reciprocal-rate mean flight time hold. The independent analytic audit checks the collision-history Jacobian, spatial count squeeze, hemisphere normalization, unconditioned Poisson insertion, exclusion of a collision-free subensemble, and partition into complete flight intervals. All three earlier audit scripts were rerun unmodified in memory, with no writes in their folders, and passed. Earlier stationarity and geometric constants also check.

Commands:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit_suspension.py
```

Earlier audit command: `OMP_NUM_THREADS=1 nice -n 15 python3 -`, reading each prior script and executing `exec(compile(old.read_text(), str(old), 'exec'), {'__name__':'__main__'})` under stdout capture. LOG.md records commands and output.

Validation: 24 exact rational correlation comparisons between direct time-phase integration and collision overlaps, plus 16 exact nonergodic mixture comparisons, passed. Event-shift, length bias, age moments, residual waiting and finite-window endpoint cancellation checks passed. The Laplace series agrees with an independent piecewise-linear time integral within 1.78e-15. Constant velocity recovers 1/z within 1.78e-15. All 27 finite-index tail checks passed. Deliberately wrong event weights and an incorrect first intervening roof were detected. Final runtime was 0.056 seconds; peak resident memory 15,990,784 bytes; actual nice value 20. The script uses bounded standard-library loops and one thread; it does not simulate Lorentz diffusion.

What failed or was corrected: no mathematical check failed. One accidental zero-width BOM at a display delimiter was removed. Large combined reading displays truncated and were followed by bounded reads of the affected material. The nice wrapper warns because inherited priority 20 cannot be raised to 15; actual execution remains at 20.

Limitations and uncertainty: neither ergodicity, quantitative mixing, integrable velocity correlation, positive diffusivity, a CLT, a quenched limit nor planar recurrence is proved. The Laplace convergence is for positive z, with no bound uniform as z decreases to zero. The periodic examples audit the identities only. Literature checking was short, and the proof has internal checks rather than external review.

Next worker: a bounded local step is to establish the o(t) multiple-collision estimate and derive C'(0+)=-4*gamma/(d+1) from the cosine jump moment. For long-time progress, estimate the weighted multi-collision terms in equations (12) or (14); stationarity alone gives no cancellation. Retain all intervening roofs and the environment. The proposed derivative is not proved in this session.

Opened primary sources in the bounded update: Karsten Matthies and Raphael Winter, [arXiv:2506.18539](https://arxiv.org/abs/2506.18539), still a joint small-radius/long-time limit; Bálint Tóth, [arXiv:2501.00519](https://arxiv.org/abs/2501.00519), a joint-limit result along extractor sequences; Patrick Charbonneau and Marcus Michelen, [arXiv:2611.07196](https://arxiv.org/abs/2611.07196), a high-dimensional void-percolation threshold result. None supplies a fixed-density billiard CLT or is a premise of the proof here.

Task: “Diffusion in the random Lorentz gas at fixed density” — 15 November 2026, 10:09 +04:00 (session orientation).
