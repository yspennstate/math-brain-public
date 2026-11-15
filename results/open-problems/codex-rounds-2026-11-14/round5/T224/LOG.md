# T224 working log

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 08:42 Asia/Tbilisi (first captured shell clock).

## Startup and literature check

Read the startup memory index and compute governor (warn, owner_away_open). All work is confined to this folder; the task-specific prohibition on outside writes overrides the global mesh/checklist/brain-writing routine. No agents, git, or external mutations are used. Programs will use one thread, nice 15, and standard-library-only small computations.

Opened https://arxiv.org/abs/2605.22010, https://arxiv.org/html/2605.22010v3, and https://arxiv.org/abs/1804.06561 with the web tool. The source remains v3, revised 11 November 2026, by Margalit Glasgow and Joan Bruna. Searched the exact title and arXiv number for later results; no later settlement found. The source's endpoint discussion and slower-decay open question remain in place. Check completed within five minutes. No SOLVED_ELSEWHERE.md is warranted.

Read the three prior REPORT.md, LOG.md, PROOF.md and audit scripts. The latest result is conditional on logarithmic integrated negative residual curvature, not on loss decay alone. Its deterministic comparison retains a negative output square before a Taylor estimate produces a quadratic parameter-error term. Independent verification follows before choosing an extension.

## Independent re-check of the latest result

Direct velocity subtraction, with e_i=w_i-v_i, y=average |e_i|^2, delta=f_m-f, zeta=average phi(v_i)-f, gives

    y'/2 = -average <r,(Dphi(w_i)-Dphi(v_i))e_i>
            -<average Dphi(w_i)e_i,delta>.

The first term is <=h y. Taylor expansion about w gives average Dphi(w_i)e_i=delta-zeta+R, ||R||<=My/2. Completing the output square yields y'<=2h y+eta^2+(M^2/4)y^2. The reciprocal comparison therefore gives y<=2 exp(2H(T))J_T when (M^2/4)S_T J_T<=1/2. Independently, this bad event is J_T>2/(M^2 S_T). Bounded differences for sqrt(J_T), with coordinate oscillation 2A sqrt(T)/m, give the reported tail exp(-m/(4M^2 A^2 T S_T)) provided m>=2M^2 A^2 T S_T. Multiplying the finite-time output estimate by four and adding 6L_T reproduces all constants in the latest theorem. The earlier claim holds in its stated bounded-feature Euclidean scope.

Reran both inherited audits from this folder, so their relative JSON outputs are local:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T224/audit_concentration.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T224/audit_cancellation.py
```

Both PASS, reproducing the previous numerical results: 488 exact concentration tails, 3,888 coordinate replacements, 300 concentration-constant checks, 21 exponent cases, 500 log-prefactor and 263 log-free-prefactor checks; 600 direct coupling identities (maximum error 7.11e-15), 300 exact cancellation cases and 300 Riccati checks. Actual nice 20 despite the wrapper's setpriority warning; peak RSS below 18 MB; both finish within a second. Full outputs: concentration_results.json, cancellation_results.json.

## Chosen extension, before proving it

Prove a loss-decay-only polynomial rate for the special case in which all feature outputs lie in one affine line in the output Hilbert space. This includes scalar output space (one effective input point), with arbitrary parameter dimension and nonlinear bounded smooth features. It is a new special case, rather than another refinement of the curvature assumption. In one output direction every neuron follows the same autonomous feature-gradient trajectory, with a common scalar clock. The feature average is monotone in that clock, so clock errors should satisfy a contractive scalar comparison without exp(H). Target: an all-time bound of order m^(-c/(c+2)) using a finite-time O((1+T)^2/m) estimate and loss monotonicity. No assertion of sharpness, no full-rank extension, and no counterexample is planned.

An initially tempting stronger claim, uniform O(1/m) for scalar outputs without any loss decay, is not justified: small changes of clock speed over a long nearly flat interval can produce a large timing difference at a later steep interval. The scalar clock comparison controls accumulated forcing, not a time-independent output error. The proof below will retain this time dependence explicitly.

## Proof saved

PROOF.md now proves the scalar-output theorem and its affine-line Hilbert-space version. Define Psi_s as gradient ascent of the scalar feature and F(s), F_m(s) as its population and empirical feature averages. Both are nondecreasing and B^2-Lipschitz. Physical dynamics are their scalar clocks tau'=gamma-F(tau), tau_m'=gamma-F_m(tau_m). For q=tau_m-tau and zeta=F_m(tau)-F(tau), q'=-(F_m(tau_m)-F_m(tau))-zeta, so |q|<=integral |zeta|. This is derived both by a regularized norm and by an integrating factor with a nonnegative bounded coefficient. At the deterministic mean-field clock E zeta^2<=A^2/m, giving E q^2<=A^2t^2/m. Minkowski then gives E output_error^2<=A^2(1+B^2t)^2/m. Loss monotonicity gives all-time bound 4A^2(1+B^2T)^2/m+6L_T. Choosing T=m^(1/(c+2))-1 proves exponent c/(c+2), with prefactor 4A^2 max(1,B^4)+6C, for every m>=1.

Also derived a source-admissible example: X=1, Y=pi/2, sigma=arctan, rho0=(delta_0+delta_1)/2. Its exact autonomous flow is Q(Psi_s(z))=s+Q(z), Q(w)=w+w^3/3. It gives L_t~1/(2 sqrt(t)), hence a genuinely nonintegrable sqrt loss and an O(m^-1/5) application. The previous global H(T) is exactly (3 sqrt(3)/8)tau(T)~(sqrt(6)/4)T^(3/4), so the previous global logarithmic-curvature hypothesis fails. This is an example covered by the new special-case theorem, not a counterexample to the general question or a weak-error lower bound. Along its actual nonnegative paths curvature has a favorable sign; this qualification is recorded in the proof.

Opened the source's Section 2 regularity assumption with the web tool to verify this example. The normalization E X^2=d holds at d=1; bounded labels and initial law satisfy the remaining data assumptions. The proof computes the activation total variations and bounded derivatives explicitly. Next: independent finite-flow/constant audit and a second derivation of the example's asymptotic constants.

## Independent audit

Saved audit_scalar_clock.py and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_scalar_clock.py
```

PASS. Full output is scalar_clock_results.json. The audit checks 500 autonomous-flow implicit/group/derivative identities, six exact ordered-sample variances, 6,000 constant-coefficient comparison intervals evaluated by their analytic solutions, 95 raw finite-neuron flow cases with 401 time points each, 500 exact rational horizon/triangle-constant checks, and six exact exponent balances (each compared with 501 rational horizon scales). Maximum implicit-flow error 7.11e-15, group error 1.34e-15, feature-clock derivative error 6.94e-11. Raw particle ODEs and independently integrated clock equations agree within 4.99e-11; no violation of the integrated-forcing comparison was observed. Full binomial enumeration over widths 1,2,4,8 verifies finite-time expected output bounds, with maximum error/bound ratio 0.06346. These deliberately loose bounds are not a sharpness test.

The flow cases use five targets, including pi/8, where the mean-field output is stationary at the target but finite clocks initially go in opposite directions depending on the sample. This checks that no unnoticed common residual-sign assumption is needed. The endpoints +/-pi/2 test clocks running to opposite infinities. No infinite-time conclusion is inferred from the finite RK4 comparisons. Exact scalar-comparison formulas also include zero damping, alternating forcing signs, and long intervals.

Four evaluations at autonomous clock s=1e3,1e6,1e9,1e12 give the residual/asymptotic ratios 1.0029854, 1.0000318, 1.00000032, 1.0000000032. These support arithmetic of the closed form only; asymptotics are proved in PROOF.md. Actual nice 20, peak RSS 17,006,592 bytes, elapsed 0.42 seconds. The wrapper's setpriority warning does not change the independently checked low priority.

## Attempts to break the result and second derivations

- Re-derived the clock error once by differentiating sqrt(q^2+epsilon^2), and again by solving q'=-k_t q-zeta with k_t in [0,B^2]. Both give |q|<=integral |zeta|, including q=0 and stationary or reversed clocks.
- Re-derived the output estimate with separate L2 norms: ||D+zeta||_L2<=B^2||q||_L2+||zeta||_L2, giving exactly A(1+B^2t)/sqrt(m). Squaring after this step avoids an extra factor two.
- Recomputed all-time constants from 2 E L_T^m+2L_T<=4 E error_T^2+6L_T. This uses population-loss monotonicity only, never assumes convergence of the finite system, and also handles T=0, hence m=1 in the optimized bound.
- Independently balanced T^2/m against T^-c: 2/(c+2)-1=-c/(c+2). Exact arithmetic verifies the prefactor 1+B^2(u-1)<=max(1,B^2)u, including B=0. There is no division by A, B, M or C. A=0 or B=0 gives constant features and zero true output discrepancy.
- Confirmed iid variance is only evaluated at the deterministic clock tau(t), not the empirical clock. Temporal dependence is retained in the time Cauchy--Schwarz estimate. The empirical law is never treated as iid after interaction.
- Scalar output here means one-dimensional span in L2(P_X). Ordinary scalar-valued regression on many inputs need not have this property. The affine-line statement explicitly forces the target into the same closed line by loss convergence. This is the main scope restriction, not a solution to the general problem.
- Re-derived the arctan asymptotic constants without the clock-time integral: Q(w1)-Q(w0)=4/3 gives w1/w0->1, so w0*residual->1 and (w0^4)'->4. Hence sqrt(t)L_t->1/2, tau/t^(3/4)->2sqrt(2)/3, and H/t^(3/4)->sqrt(6)/4. This independent derivation is also in PROOF.md.
- Checked total variations: TV(arctan)=pi, TV(sigma')=2, TV(sigma'')=4*(3sqrt(3)/8)=3sqrt(3)/2. Maximizing 2x/(1+x^2)^2 over x>=0 gives x=1/sqrt(3), confirming the curvature coefficient separately. The exact relation H=(3sqrt(3)/8)tau also immediately proves nonintegrability of sqrt loss.
- The example violates the previous *global* H condition, but its realized nonnegative paths have favorable curvature. It is not an output-instability counterexample and does not prove that the new method is necessary. The exponent c/(c+2) is not asserted sharp.

No gap found in the stated scalar/affine-line theorem. The unrestricted slow-loss problem still lacks a polynomial bound or a counterexample.

## Final artifacts

Saved REPORT.md with the required PARTIAL verdict, the special-case theorem, source-admissible slow example, all verification commands, limitations, and the next two-direction/commutator lemma. Read back PROOF.md and checked its 38 paired display environments. A final small nice-wrapped standard-library check confirms all three audit JSON files say PASS, their recorded priorities and memory satisfy the limits, the required artifacts exist, and REPORT.md begins correctly. Final check PASS, actual nice 20. No additional computation is needed after these checks.

The new result is the one-output-direction theorem, not a settlement of general T224. All substantive writes stayed in this folder; earlier folders were read only. No git, agents, outside coordination mutations, or external publication was used.
