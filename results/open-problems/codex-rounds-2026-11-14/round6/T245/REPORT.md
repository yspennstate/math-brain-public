VERDICT: PARTIAL finite Taylor-jet approximation with a uniform error bound for the structured model's first learning-rate correction

The round-5 result holds on independent recheck. The new result replaces its evolving depth field by finitely many symmetric matrices, with a proved truncation error. For every fixed training interval and rho>1, the endpoint and full NTK approximation has error

\[
O_T(\eta^2+\eta\rho^{-m}).
\]

Thus m=O(log(1/eta)) suffices to retain the preceding O(eta^2) accuracy. This is a controlled finite approximation, not an exact closure at fixed m. The original independent-Gaussian/ReLU joint-limit training-law problem remains unresolved.

The setting remains the fully trainable deep-linear model with scalar-identity initialization and fixed active dimension d. Conditional on S>0, put H=P^TP/S^2 and K=log H along the already known balanced endpoint flow. Expand the round-5 memory as J(tau,z)=sum_q j_q(tau)z^q. Its coefficients satisfy

\[
\dot j_q=\sum_{a=1}^q(r_a^Tj_{q-a}+j_{q-a}r_a)-tn_q,
\qquad j_q(0)=0,
\]
\[
r_a=-t(-1)^{a-1}\operatorname{ad}_K^{a-1}(vg^T)/a!,
\qquad v=P^Te.
\]

The source coefficients n_q are explicit finite products of K,v,g, given in [PROOF.md](PROOF.md), equations (12)--(14). Each equation uses only lower j's. Every truncated system therefore computes its retained Taylor coefficients exactly; discarded coefficients do not feed back into them.

The field J is entire in complex depth. A uniform disk bound and Cauchy's formula give

\[
\sup_{\tau\le T,\,z\in[0,1]}\|J-J_m\|_F
\le M_\rho\rho^{-m}/(\rho-1).
\]

The proof supplies an explicit M_rho, a uniform bound for the forced-Gram inverse, and propagation through the endpoint sensitivity and both kernel coefficients. The full kernel includes its perpendicular-input term. The evolving state has

\[
2(d^2+1)+(m+1)d(d+1)/2
\]

real coordinates. The boundary solve and kernel integrals are instantaneous functions of that state. The proof also constructs the polynomial-source boundary solve by a finite matrix exponential and linear solve.

The size limit is taken first, then eta tends to zero on a fixed training interval. All randomness remains S=exp(mu t+sigma sqrt(t) Z). Constants depend on S; no uniform lognormal-tail moment claim is made. No novelty claim is made for Taylor approximation of analytic ODEs. The contribution here is its explicit triangular form and full-NTK error estimate for this particular correction.

Independent checks and commands, run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 recheck.py > recheck_output.txt 2>&1
OMP_NUM_THREADS=1 T245_GRID=128 nice -n 15 python3 recheck.py > recheck_refined_output.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1
```

[recheck.py](recheck.py) integrates the first Euler-error equation in the original nonlinear profile, without using J or its reconstruction. Its full sensitivity agrees with round 5 within 4.64e-8 at depth grid 128; grid doubling reduces the discrepancy by a factor 4.0006. The previous two commutators and the mandatory memory constants -1/24 and -1/48 pass exact rational checks.

[verify.py](verify.py) checks the new coefficient formulas by independent exact multiplication of exponential series through degree 8. It also checks repeated eigenvalues with a nonzero source, exact independence of retained coefficients from truncation order, and an independent spectral evaluation of the transport R. The wrong commutator sign fails with error 1.085, so the sign check is consequential.

At (t,S,T)=(2,1.3,1.2), the following discrepancies are relative to the preceding field implementation at the same quadrature settings:

| Degree m | Maximum memory-field discrepancy | Maximum full first-correction discrepancy |
| --- | ---: | ---: |
| 0 | 3.215e-2 | 2.397e-2 |
| 2 | 4.581e-3 | 9.214e-4 |
| 4 | 2.652e-4 | 1.952e-5 |
| 6 | 7.123e-5 | 3.674e-6 |
| 8 | 4.202e-6 | 1.533e-7 |
| 12 | 2.461e-9 | 8.093e-11 |

Degree 12 uses 39 symmetric memory coordinates, or 49 evolving coordinates including endpoint and sensitivity. Refining depth evaluation and training integration changes the degree-8 full correction by 6.42e-10. The smallest same-grid discrepancy above is below this refinement difference; it is not a certified absolute integration error.

With degree 6 at time .4, halving eta from .04 down to .005 reduces full-state errors against the original nonlinear discrete profile by factors between 4.014 and 4.104 in the three earlier cases t=.5,1,2. At eta=.005 the errors are 3.50e-7, 1.59e-6, and 1.46e-5 respectively. These numerical diagnostics support, but do not replace, the proof. The main verification took 72.18 seconds, used 21.9 MB peak RSS, one thread, and priority 20. All scripts use only the standard library. The macOS nice warning reflects inherited priority 20, checked directly inside each script.

[audit.py](audit.py) uses a separate, exactly solvable frozen-coefficient memory equation. Its Taylor coefficients are nonzero at every order, and its closed exponential solution verifies the factorials and the Cauchy tail estimate. This is a manufactured test, not a reachable-training or impossibility theorem. It also recomputes the saved convergence ratios. Full commands, failures, outputs, and resource measurements are in [LOG.md](LOG.md), [verification_data.json](verification_data.json), and the output files.

What failed: the first recheck used an overstrict flow tolerance; depth refinement identified the raw solver's depth error. The general worst-case analytic constant is too pessimistic to certify the small practical degrees used in the numerical examples. Fixed degree does not reproduce the full memory exactly: degree 6 has a visible truncation error on the longer interval. No assertion in the final verification failed.

What remains uncertain: exact finite compression for the actual two-example training trajectory, a useful certified stopping rule for m, fixed-positive-eta closure, Gaussian matrix initialization, ReLU gate changes, simultaneous size/step limits, and infinite training time. The bounded literature check found no whole-problem solution; opened papers and their distinct scopes are recorded in the log.

Next worker: obtain a useful path-dependent analytic tail bound for (15), and use it to certify a degree for the mandatory two-example benchmark at a specified eta. The present global bound proves convergence but is generally too large for that purpose. Preserve the exact coefficient-prefix identities, the two commutators, and the -1/24 and -1/48 kernel slopes as checks.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 11:27 Asia/Tbilisi (session receipt, minute precision).
