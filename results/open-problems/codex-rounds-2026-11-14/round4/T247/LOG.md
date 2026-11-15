# T247 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 05:12 Asia/Tbilisi (01:12 UTC; exact tool time recorded below if different).

## Orientation and literature check

Read the startup memory and compute state (warn, owner_away_open). The task-specific restriction to writes inside this folder overrides global mesh, checklist and brain mutations: none of those external stores will be changed. No git, subagents, network posting or heavy computation. Numerical runs will use one thread, niceness at least 15, a short alarm and a peak-memory check below 1 GB.

Read both earlier REPORT.md, LOG.md, PROOF.md and their scripts without modifying those folders. The original result is an exact independent-gate moment formula. Round 3 supplies genuine dependent-gate conditional moment estimates and an accumulated bound after scalar normalization. Its constants were re-derived from the displayed gate bounds: (2*26+32)*16=1344, then 1344*(2Z+2)+144*(Z/2+3/2)=2760Z+2904. The directional linear term is bounded by completing (X-I+I/2)^2, giving 12Z+6.

Web queries: “deep neural network Jacobian joint depth width limit orthogonal tanh dynamical isometry rigorous 2025 2026”; “Collins Hayase Pastur Slavin Jacobian simultaneous depth width asymptotic freeness”. Opened arXiv pages 1711.04735, 2103.13466, 2503.07872 and 2506.08764, plus full HTML for the last and Collins–Hayase. The new nearby paper 2506.08764v3 explicitly states a fixed-depth infinite-width regime (introduction, lines 54, 59, 91–92 in the web rendering); it does not settle the requested joint limit. Hanin–Jiang treats independent i.i.d.-entry matrix products. No verified solution of the stated problem was found in this bounded check. Literature search ended within five minutes. Full citations will be saved in LITERATURE.md.

## Earlier-result recheck, before new work

Re-derive the accumulated recursion algebra independently and re-run the round-3 conditional Haar checks from a local copy. The earlier script writes relative results.json, so it must execute from this folder, never from the earlier folder. Also independently integrate the leading dependent-gate coefficients using exact spherical moments and check the closed-form independent-gate recurrence. Report the outcome before claiming an extension.

## Earlier-result recheck completed

Commands (both exit 0):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 recheck_independent.py > recheck_independent_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 recheck_dependent.py > recheck_dependent_output.txt 2>&1
```

Local copies were made by pathlib reads/writes; the only change to the dependent script is its output filename, prior_results.json. The 20 exact rational independent-gate checks, 15 residual O(2) integrations, eight full O(3) quadratures and actual depth-30 networks all passed. Maximum quadrature error 2.49e-14; derivative error 1.4e-8. Peak RSS 124.4 MiB, runtime .99 seconds, inherited niceness 20. The nice warning reports an attempted priority adjustment; actual niceness is already below the required priority. Independent algebra re-derivation of the accumulated recursion also agrees. Earlier main claim holds.

## Chosen extension, before derivation

Prove that the random scalar normalization can be removed in a concrete genuine tanh network with one deterministic gain at all layers. Take a small target preactivation variance a_n, choose the spherical backward-critical gain g_n^2=1/mu_n(a_n), and initialize the radius so q_1=a_n. Seek a high-probability forward-radius envelope and S_L->1 when L a_n^2 + L a_n/n ->0, with n,L->infinity. This uses the previous theorem at its own scaling and addresses its stated next obstruction. It is a zero-bias, vanishing-variance critical sequence, not a theorem at fixed nonzero stationary variance or a full density formula.

Method to test: compare log scalar gain to the telescoping forward log-radius. Both have leading decrement -2q; the spherical fourth moment introduces a q/n correction. Control the radius by the restoring sign of the mean radial map, and control the remaining fluctuations by a martingale. The proof must allow L a_n to diverge; a simple accumulated absolute-error estimate would miss that regime.

## Scalar and forward-radius estimates derived

For u uniform on the sphere, put M4=n sum u_i^4 and M6=n^2 sum u_i^6. Exact moments give E M4=3n/(n+2), E M4^2=n^2(9n+96)/((n+2)(n+4)(n+6))<=9, and E M6<=15. For the exact forward ratio F(q,u)=sum tanh^2(sqrt(nq)u_i)/(nq), the global scalar inequalities give -log F<=2q M4 and |log F+(2/3)q M4|<=q^2((17/45)M6+2M4^2). Consequently E log F=-(2n/(n+2))q+rho, |rho|<=24q^2, and Var(log F)<=36q^2. These bounds do not require every coordinate to be small.

On the stopped interval q in [a/2,2a], the log-radius martingale has quadratic mean at most 144 L a^2. The drift restores the radius toward a within a log band r=8/n+222a. A last-crossing argument yields max |log(q_l/a)|<=8/n+238a+2 delta except on an event of probability at most 144 L a^2/delta^2, provided the right side stays below log 2.

The comparison to the scalar normalizer yields |log S_L|<=8/n+238a+8La/(n+2)+156La^2+3 delta on that same event. This would remove S_L in exactly the previous sufficient regime La^2+La/n->0. The argument actually requires only |log(g^2)-2a|<=15a^2. Both the spherical critical gain and the conventional Gaussian critical gain g^2=1/E sech^4(sqrt(a)G) satisfy this by the same global scalar bound. Include the Gaussian choice in the theorem. The gain stays deterministic and identical across layers; the forward network is not normalized adaptively.

Checks still required: prove the global tanh lower bound used for the logarithm; write out the discrete last-crossing argument with stopping indices; verify every spherical-moment constant independently; test finite-width actual products and a regime with La growing. No theorem is yet declared complete.

## Proof saved; verification started

Saved PROOF.md with a self-contained proof, including the preceding round's one-layer dependent-gate estimate. The theorem covers any deterministic identical-layer gain satisfying |log(g^2)-2a|<=15a^2; in particular g^2=1/mu_G(a) and g^2=1/mu_n(a). Initial input satisfies g^2||h_0||^2/n=a. Both the high-probability radius envelope and S_L->1 are proved under La^2+La/n->0. Freezing the normalized Gram process after radius exit makes the old almost-sure-envelope estimate applicable; on the good event this process equals the actual normalized Jacobian.

Finite bounds: for n>=64, 0<a<=1/4096, 0<delta<=1/8, the radius/scalar exceptional probability is at most 144La^2/delta^2. The stopped distortion has expectation at most B exp(A), A=24La/(n+2)+11040La^2, B=12La/(n+2)+11616La^2. Equation (37) states a finite probability bound for the actual unnormalized empirical W2 distance.

The global lower tanh bound follows by differentiating (1+x^2)sinh x-x cosh x. It handles rare large coordinates and avoids a hidden condition nq<<1. The exact moment bound E M4^2<=9 follows from the positive difference 12n^2+396n+432 after clearing denominators. The last-crossing argument explicitly includes the exit step, so no overshoot is omitted.

Started the verification command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 verify_critical.py > verification_output.txt 2>&1
```

The script has a 180-second alarm, one-thread environment, peak RSS check below 10^9 bytes, and no BLAS matrix multiplications. Planned independent checks include 110-digit global scalar inequalities, Dirichlet rising-factorial moments, deterministic sphere quadrature for the -4/(n+2) scalar/radius mismatch, randomized last-crossing tests, forward-radius simulations, and actual full Jacobian products at n=64.

## First verification completed; adversarial audit

The command exited 0. Exact moment checks passed in eight dimensions including n=1,2 and n=10000; 110-digit checks covered x up to 100 and q from 1e-12 to 10, including a fully concentrated coordinate. Sphere quadrature changed by 4.44e-16 when doubled. Its extrapolated scalar/radius mismatch coefficient is -0.7999999996 at n=3, versus exact -4/5. All 100000 randomized last-crossing checks passed.

Forward simulations: n=64,L=10000,a=.0002 (La=2), maximum observed |log(q/a)| .0375334 and mean S .910903; n=256,L=2000,a=.0002, maximum .00702258 and mean S .998071. The n=64 value is deliberately retained: at fixed finite width and a horizon with La/n=.03125, S need not be especially close to 1. The theorem needs this quantity to vanish; its bound is conservative and does not claim every simulated finite scalar is near one.

Actual full dependent critical-gain network: n=64,L=120,24 samples,a=.0002. Mean unnormalized distortion .000158672, mean normalized distortion .000158685, stopped expectation bound .0639479. All simulated radii remained in [a/2,2a]. Runtime 2.11 seconds, peak RSS 78.8 MiB, inherited niceness 20; thread settings all one. No floating-point warnings or numerical assertion failures.

Audit of possible missing cases: rare coordinates with nq large are covered by the global logarithmic bound, not by a coordinate Taylor assumption; the radius stopping time is predictable before each active matrix step; its final crossing step is included in the last-crossing inequality. Empirical W2 control does not imply a bound on every singular value. The Gaussian gain is critical for the derivative mean at the target a, while zero-bias forward stationarity at a is not assumed. The theorem concerns a->0 and explicitly does not settle fixed positive stationary variance with bias.

Added independent arithmetic checks for 144,222,238,39,156 and an additional extrapolated forward-log-radius derivative check (-6/5 at n=3). Rerun required after this verification-only addition.

## Final verification and report

Reran the unchanged verification command after those additions. Exit 0. Exact saved output:

```text
nice: setpriority: Operation not permitted
Exact spherical moment cases: 8; all constant checks passed
110-digit global scalar inequalities: 10 points; forward log inequalities: 15 cases
Sphere O(3) scalar quadrature difference: 4.44e-16
Normalizer/radius linear coefficient: -0.7999999996, predicted -0.8
Forward log-radius linear coefficient: -1.2, predicted -1.2
Discrete last-crossing inequalities: 100000 passed
Radius n=64, L=10000, La=2: max |log(q/a)|=0.0375334, mean S=0.910903
Radius n=256, L=2000, La=0.4: max |log(q/a)|=0.00702258, mean S=0.998071
Actual critical tanh n=64, L=120: mean Z=0.000158672, mean normalized Z=0.000158685, bound=0.0639479
Niceness 20; peak RSS 60.3 MiB; runtime 1.71 s
All critical-gain verification checks passed
```

Saved REPORT.md with the partial verdict, precise theorem and gain/input choices, what is new beyond round 3, commands, limitations and next mathematical target. All formulas in the proof were re-audited: the radial coefficient is 2n/(n+2); its difference from the derivative coefficient 2 is 4/(n+2); the global forward remainder is (17/45)*15+2*9=71/3<24; stopped variance is 36*(2a)^2 per step; the scalar remainder is 15+24=39; its envelope contribution is 39*(2a)^2=156a^2. All gain choices are deterministic; none of the Jacobians differentiates an adaptive normalization.

What did not work: summing absolute scalar increments would only cover La->0. The logarithmic radius comparison handles the wider stated regime. No attempted verification or mathematical assertion failed in this session. What is not established is explicit in REPORT.md: positive stationary variance with bias, the full density, spectral edges, operator isometry and necessity of the scaling. Only in-probability empirical isometry is asserted, rather than expected unnormalized distortion convergence.

Final stdlib-only artifact audit, run with the same one-thread nice environment, exited 0: “Final artifact audit passed: theorem, stopping bounds, reports, scripts, exact checks, numerical output and resource limits agree.” It checked all 12 supporting files, Python syntax without creating bytecode, all 37 numbered proof equations, report scope, earlier exact checks, both new leading coefficients, stopping/envelope data and resource limits. No writes outside this folder were requested or performed. Work completed at approximately 05:26 Asia/Tbilisi, 15 November 2026.
