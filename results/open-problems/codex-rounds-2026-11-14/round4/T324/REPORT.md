VERDICT: PARTIAL deterministic concentration and merging asymptotics for two groups of nonzero width

The earlier two-atom result holds. Its rational drift and uniform time identity were re-derived independently; angular/cosine quadratures agree to 6.704e-13 relative error, and the noisy kernel agrees with a separate boundary-value solve to 2.019e-8. The brief web update found no later resolution. Opened references and the limits of that check are in LITERATURE.md; publication priority is not established.

The new theorem closes the deterministic concentration gap named by the earlier report. Consider normalized identity-matrix attention on the circle, including self-attention, with two labelled groups of fixed positive masses p,q. Their initial arithmetic center gap is fixed x, and merging means first entrance of that center gap into a fixed delta, where 0<delta<x<pi. Suppose both initial group diameters are at most w_beta<=1/(4 sqrt(beta)). For sufficiently large beta:

- Each group diameter is at most w_beta exp(-t/2) until the merging threshold.
- The merging time satisfies log(tau_beta)/beta -> 1-cos(x).
- If beta^2 w_beta^3 -> 0, then tau_beta ~ exp(beta(1-cos(x)))/[(p/q+q/p) beta sin(x)^2]. This includes initial diameters O(1/beta).

The estimates are uniform in the number of tokens and their individual positive weights. The proof also covers compactly supported mean-field groups. PROOF.md supplies all steps, including the attention-velocity derivative, cancellation of internal mean motion, and an explicit scalar hitting-time sandwich after time 4 beta. The accumulated initial center displacement is O(beta w_beta^3) plus an exponentially small term; controlling it to o(1/beta) is what preserves the prefactor.

Verification command, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
```

The final run exited 0 in 3.817 seconds, peak RSS 16.28 MiB, inherited effective nice 20. It uses one thread and only the Python standard library. The launcher prints a setpriority warning because the inherited priority is already lower than requested. The script checks derivative and symmetrization identities, two time-step resolutions of a six-token system with unequal weights, and finite-time contraction cases satisfying the explicit sufficient condition. At beta=18 the full-token/scalar time ratio is 0.999994235. Numerical values are consistency checks, not proof certificates; full output and commands are in LOG.md and data in verification.json.

What failed: an initial numerical assertion extrapolated the contraction bound to beta=6, where the proof's sufficient condition fails. The measured width excess was about .00551. The final script retains that out-of-regime datum and checks contraction separately at beta=500,1000,2000. An isolated skew-group experiment also shows why small initial width alone does not justify transferring the prefactor without controlling center displacement. No counterexample within the theorem's asymptotic hypotheses was found.

Limits and uncertainties: this does not prove a generic cluster count, formation of the two groups, successive mergers, a noisy concentration theorem, or general attention matrices. Group masses are fixed, unlike the previous report's singular atom-mass regime. The stopping event is a center-gap threshold, not exact collision. The prefactor width condition is sufficient and has not been shown necessary. The numerical checks do not simulate exponentially long waiting at large beta; the analytic sandwich supplies that conclusion.

Next worker: prove a stopped concentration estimate for independently noisy tokens in these two narrow groups. For equal token weights, derive the exact group-mean martingale variance (which depends on group size) before comparing to a scalar noisy gap. Control the internal drift residual and the probability of width excursions over the relevant merging interval; replacing each group by the earlier independently noisy atom is not justified without these estimates.

Task: T324, “take the NEXT checkable step on this problem, building on that work.” First recorded session clock: 15 November 2026, 06:31 +04 (Asia/Tbilisi); the prompt's own timestamp was not supplied.
