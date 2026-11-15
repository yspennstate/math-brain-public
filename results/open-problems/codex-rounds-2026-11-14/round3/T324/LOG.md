# T324 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded session clock: 15 November 2026, 03:47 +04 (Asia/Tbilisi).

## 1. Orientation and literature check

Read the previous REPORT.md, LOG.md, PROOF.md, verify.py and LITERATURE.md in ~/codex_op_1114/briefs/T324. That folder remains read-only. The current folder initially contained PROMPT.md. Read the compute state: status warn, CPU saturated, owner_away_open. Only short, single-threaded standard-library calculations will be run. A startup brain recall was attempted under nice -n 15; its initial output reported inability to persist a telemetry identifier and the execution session disappeared before results could be retrieved. No further semantic recall is needed for the mathematical task. The folder-only instruction supersedes the general instructions to mutate the shared checklist, mesh or memory; no such writes are authorized here. No git or subagents.

Literature search completed in less than five minutes. Queries: `"metastable" "transformer" clustering merging 2026 2025`; `"Emergence of meta-stable clustering" Bruno Pasqualotto Agazzi`; `transformer clustering "merging" "November" "2026" metastability`; `"A multiscale analysis of mean-field transformers"`. Opened arXiv pages 2410.23228, 2509.25040, 2610.08755 and the HTML of 2509.25040v1. An attempted conference-PDF opening returned a browser challenge, so it supplied no theorem evidence. No post-report resolution was found. The multiscale follow-up and the conditional noisy result were already covered in the earlier report. This short search does not establish novelty. Details and exact references will be in LITERATURE.md.

## 2. Independent re-derivation of the earlier result

For equal masses, compute the cosine derivative directly from the projected vector equation: c'=2(1-c^2)/(1+exp(beta(1-c))). Consequently T=(1/2) integral_[cos(x),cos(delta)] (1+exp(beta(1-c)))/(1-c^2) dc. Endpoint Laplace asymptotics give exp(beta(1-cos(x)))/(2 beta sin(x)^2), agreeing with the earlier claim.

For independent angular noises sqrt(2 nu), the difference generator is 2 nu d^2/ds^2-h(s)d/ds. The first derivative p=u' of the killed mean hitting time satisfies 2 nu p'-hp=-1 and p(pi)=0; integrating from pi gives precisely the earlier positive, decaying double-integral kernel. Restricting it near x yields the lower exponent min{a(x),r}. A positive lower drift bound on each short interval [y,y+eta] yields the upper bound 1/b+pi/(2nu) exp(-eta b/(2nu)); the outward term is superexponentially small if a(x+eta)<r. This independently validates both the exponent and the sign of the excursion estimate. A numerical check will use a separate boundary-value solve and angular/cosine quadratures without running the old write-producing script in its source folder.

## 3. Choice, recorded before extending the proof

One extension: determine the dependence of the scalar merging law on unequal two-atom masses. In addition to fixed unequal masses, permit a beta-dependent mass ratio rho_beta=min(p_beta/(1-p_beta),(1-p_beta)/p_beta) with -log(rho_beta)/beta -> kappa. This is the same two-atom reduction, but probes a singular case missed by a fixed-mass estimate. Proposed deterministic exponent: max{1-cos(x)-kappa,0}. Proposed mean hitting exponent under independent atom noises: min{max{1-cos(x)-kappa,0},r}. For fixed masses the proposed deterministic prefactor is 1/[(p/q+q/p) beta sin(x)^2]. This does not model independent noises within multi-token groups. The mass-dependent denominator and all diffusion factors must be checked separately, and the zero-exponent and threshold cases must be retained.

## 4. Proof and first analytic audit

Wrote PROOF.md and LITERATURE.md. The mass-dependent drift is sin(s) times [1/(1+rho exp(beta a(s)))+rho/(exp(beta a(s))+rho)]. Its second summand is between zero and the first. This gives bounds uniform in the masses and proves the proposed positive-part exponent. The noisy proof uses the exact killed mean formula; a fixed positive minimum of sin(s) on [delta,x+eta] supplies the lower drift bound, avoiding any unjustified monotonicity assumption. It controls outward excursions even when the small-mass drift is order one.

Independent checks: the vector cosine equation yields c'=(w1+w2)(1-c^2), and rational simplification yields h/sin=(C E+2)/(E^2+C E+1), with C=p/q+q/p. Both give the same fixed-mass prefactor. The angular generator separately confirms 2nu in the gap diffusion. A logarithmic primitive gives an additional check of the potential sign and mass dependence.

Adversarial case found: the fixed-mass prefactor cannot be substituted with exponentially vanishing masses. If rho=exp(-kappa beta) and kappa>a(x), that substitution would predict T->0, whereas the exact drift tends uniformly to sin(s), giving a positive finite limit. The positive part in the new exponent is essential. No failure of the earlier equal-mass theorem was found.

The arXiv PDF of 2509.25040 was successfully opened after the conference link failed. Read the startup and identity memories directly; no further shared-state operations were performed.

## 5. Verification implementation and launch correction

Added verify.py. It independently checks drift algebra in three representations, angular and cosine adaptive quadratures, and the noisy mean using direct two-dimensional quadrature of the explicit primitive, a separate central-difference boundary-value solve, and exact constant-drift cell transfers. A short table tests beta-dependent mass ratios, including the positive-part threshold and equal noisy/deterministic exponents. All loops are single-threaded, with arrays only in the small BVP solve.

Command: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py`

First launch exited immediately: `nice: setpriority: Operation not permitted`, followed by `ValueError: current limit exceeds maximum limit` when trying to set RLIMIT_AS to 768 MiB. Removed the unsupported address-space hard-limit call. The script instead measures peak RSS and asserts it is below 1 GiB; the actual data structures are far smaller. It checks effective nice >=15 and all four thread settings before any computation. This is a launcher correction, not a change to a mathematical claim.

The next run failed the deterministic relative-coordinate assertion at p=.01, beta=320. A diagnostic using the same launcher and a Python heredoc independently evaluated both adaptive quadratures at absolute tolerances 2e-11 and 1e-15. With the loose tolerance, the scaled integral is only 3.642913e-5 and the coordinate relative discrepancy was 1.089027e-7; at 1e-15 it was 2.446932e-13. Tightened the adaptive absolute tolerance to 1e-15, retaining the original relative assertion. No formula or acceptance threshold was relaxed.

## 6. Sharper deterministic audit

Rational division gives an additional finite-parameter estimate uniform over all masses: max{B,J_beta/C_beta} <= T_beta <= B+J_beta/C_beta, where B=integral_delta^x csc(s) ds and J_beta=integral_delta^x exp(beta a(s)) csc(s) ds. Indeed (E^2+CE+1)/(CE+2)-E/C lies between zero and one, and the first quotient is at least one. Added the full derivation to PROOF.md. Consequently the mass-dependent prefactor is valid for all sequences with exp(beta a(x))/(C_beta beta)->infinity, including all kappa<a(x), rather than only fixed masses. This is part of the same unequal-mass extension. It also identifies an order-one crossover more sharply than the logarithmic exponent does.

The third verification launch reached the noisy quadrature and failed its coarse/refined assertion for beta=12, p=.2, nu=.002: the 256/512 uniform two-dimensional Simpson discrepancy was 6.360962e-6, above 5e-6. A separate diagnostic using the same launcher compared an adaptive inner integral against the central-difference BVP: means 140.555473609 and 140.555466503, a relative difference 5.055751e-8. Changed the direct two-dimensional calculation to adaptive integration in z (absolute tolerance 1e-12) while retaining the 256/512 outer-mesh comparison and all original assertions. The discrepancy was a resolved sharp inner layer, not evidence against the exact formula. Also added checks of the uniform deterministic comparison and critical mass sequences L_beta=beta a(x) +/- sqrt(beta).

The fourth launch passed the earlier quadrature checks but exhausted adaptive recursion in the mass-scaling table. The global 1e-15 absolute tolerance was subdividing below floating-point roundoff when the function was of order one. Added a local stopping floor of 128 machine epsilons times the absolute cell integrals, alongside the requested quadrature tolerance. External coordinate, BVP, mesh-refinement and comparison assertions remain unchanged. These calculations are floating-point consistency checks, not interval certificates; the proof is analytic.

## 7. Successful check and final sharpening

The fifth run of the recorded command passed in 2.893 seconds, peak RSS 18.17 MiB, effective nice 20. Drift representations agreed within 2.998e-15; angular/cosine deterministic integrals within 3.152e-12. For equal masses at beta=4, nu=.03, the direct-kernel and BVP means were 6.952670870 and 6.952670897, confirming the earlier noisy formula independently. The table's largest 32768/65536 cell-mesh discrepancy was 2.047e-5. Full final output is recorded below after the final run.

A second polynomial division sharpens the uniform mass estimate to an additive error at most B/(C_beta exp(beta a(delta))): T_beta=J_beta/C_beta+(1-2/C_beta^2)B minus a nonnegative remainder within that bound. This proves a finite limiting constant at the critical scale L_beta=beta a(x)-log(beta)+b+o(1): T_beta->B+exp(-b)/sin(x)^2. Added the identity, its proof, and numerical cases b=-1,0,1. The sqrt(beta) critical perturbations independently illustrate why a zero exponent does not imply a bounded time. Corrected the scope paragraph to make the divergence condition for the mass-dependent prefactor explicit. The original proposed mass-dependent noisy exponent is unchanged.

## 8. Final verification output

Command, from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
```

Exit code 0. Combined output (the nice warning preceded the script output):

```text
nice: setpriority: Operation not permitted
effective nice=20; peak RSS=17.70 MiB
Drift algebra max relative error: 2.998e-15
Deterministic coordinate max relative error: 3.152e-12
Fixed masses: p, beta, exact/asymptotic
0.50, 20, 1.053957161
0.50, 80, 1.011037476
0.50, 320, 1.002643594
0.20, 20, 1.054125400
0.20, 80, 1.011037476
0.20, 320, 1.002643594
0.01, 20, 1.059947996
0.01, 80, 1.011037476
0.01, 320, 1.002643594
Noisy direct quadrature / BVP / cell transfer: beta, p, three means
4, 0.5, 6.95267087, 6.952670897, 6.952670863
4, 0.2, 3.827278835, 3.827278754, 3.827278833
12, 0.2, 140.5554736, 140.5554665, 140.5554724
Mass scaling: kappa, beta, log(T)/beta, predicted limit, T/sine-limit if available
0.000000000, 20, 0.462863916, 0.637642246, None
0.000000000, 80, 0.576099299, 0.637642246, None
0.000000000, 320, 0.617898286, 0.637642246, None
0.250000000, 20, 0.247944776, 0.387642246, None
0.250000000, 80, 0.334763638, 0.387642246, None
0.250000000, 320, 0.370064371, 0.387642246, None
0.637642246, 20, 0.012227277, 0.000000000, 1.0498687839132048
0.637642246, 80, 0.002597120, 0.000000000, 1.0119602226361164
0.637642246, 320, 0.000621379, 0.000000000, 1.0029652314827013
0.900000000, 20, 0.009807137, 0.000000000, 1.0002624328983216
0.900000000, 80, 0.002448504, 0.000000000, 1.0000000000091724
0.900000000, 320, 0.000612126, 0.000000000, 0.9999999999999997
Noise crossover: kappa, r, beta, log(mean)/beta, predicted limit
0.000000000, 0.300000000, 40, 0.286240568, 0.300000000
0.000000000, 0.300000000, 160, 0.295431170, 0.300000000
0.000000000, 0.300000000, 320, 0.297579055, 0.300000000
0.250000000, 0.200000000, 40, 0.173822580, 0.200000000
0.250000000, 0.200000000, 160, 0.191567818, 0.200000000
0.250000000, 0.200000000, 320, 0.195548185, 0.200000000
0.250000000, 0.387642246, 40, 0.331453347, 0.387642246
0.250000000, 0.387642246, 160, 0.366587595, 0.387642246
0.250000000, 0.387642246, 320, 0.375313795, 0.387642246
0.250000000, 0.800000000, 40, 0.299519013, 0.387642246
0.250000000, 0.800000000, 160, 0.356835610, 0.387642246
0.250000000, 0.800000000, 320, 0.370064411, 0.387642246
0.637642246, 0.400000000, 40, 0.005495144, 0.000000000
0.637642246, 0.400000000, 160, 0.001261308, 0.000000000
0.637642246, 0.400000000, 320, 0.000621379, 0.000000000
0.900000000, 0.400000000, 40, 0.004897013, 0.000000000
0.900000000, 0.400000000, 160, 0.001224252, 0.000000000
0.900000000, 0.400000000, 320, 0.000612126, 0.000000000
Critical mass corrections: sign, beta, time, sine limit, mass-dependent asymptotic
-1, 40, 17.654707, 1.21638135, 16.0616898
-1, 160, 2254.27912, 1.21638135, 2241.04573
-1, 320, 211849.146, 1.21638135, 211289.367
1, 40, 1.21643412, 1.21638135, 5.15646747e-05
1, 160, 1.21638137, 1.21638135, 2.30979169e-08
1, 320, 1.21638135, 1.21638135, 6.12471523e-11
Critical constants: b, beta, time, predicted limit
-1, 80, 4.38006817, 4.34553026
-1, 320, 4.35380246, 4.34553026
0, 80, 2.38023669, 2.3675309
0, 320, 2.37057407, 2.3675309
1, 80, 1.6445398, 1.6398656
1, 320, 1.64098512, 1.6398656
Maximum crossover mesh discrepancy: 2.047e-05
All checks passed in 3.093 seconds; wrote verification.json.
```

Reading verification.json with a short standard-library command under the same launcher gave max noisy BVP discrepancy 5.055750662563696e-08, max noisy cell discrepancy 8.919518235117607e-09, and a(x)=0.6376422455233264. Both the old equal-mass theorem and the new formulas passed the independent checks. The critical constants were derived again using the cosine endpoint asymptotic and C_beta~exp(L_beta), giving the same exp(-b)/sin(x)^2 term.

## 9. Completion

Wrote REPORT.md. The result is partial relative to T324: the unequal-mass two-atom extension is proved, including a uniform deterministic comparison and the critical constant, but no generic cluster count or finite-width noisy reduction. All new artifacts are in this folder; no file in the earlier worker's folder was edited. No further calculations are needed after the passing check.
