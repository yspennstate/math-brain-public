# T090 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 04:47:12 +04 (00:47:12 UTC). Prompt receipt time unavailable.

## Orientation and literature check

Read both earlier REPORT.md and LOG.md files, the round-3 PROOF.md and its entire check_gaussian_renewal.py, the read-only memory index, and the compute governor state. The first folder has no PROOF.md or computation script. The governor reports warn / owner_away_open, CPU 100%; no heavy computation is planned. No subagents, git, external messages, or writes outside this folder. The task-specific write restriction supersedes the state-writing brain, checklist, and mesh utilities; they were not invoked.

Bounded status search began at approximately 04:47 +04 and finished within five minutes. Queries: `"2+1" "KPZ" "exponents" proof 2026`; `"The Critical 2D KPZ Process" 2610.31614`; `site.arxiv.org "KPZ" "November" "2026" "strong coupling" exponents proof`. Opened https://arxiv.org/abs/2610.31614 and https://arxiv.org/html/2610.31614v1. No newer fixed-coupling resolution found. The existing critical-process result concerns critical vanishing-coupling tuning, not the fixed-coupling long-time exponents. A bounded search is not a proof of absence.

Additional background opened for the chosen subproblem: Jussi Behrndt, Petr Siegl, Nicolas Weber, *Revisiting the Weak Coupling Phenomenon for Two-Dimensional Schrödinger Operators*, https://arxiv.org/abs/2604.19284 and https://arxiv.org/html/2604.19284v2; Sylwia Kondej, Vladimir Lotoreichik, *Weakly coupled bound state of 2D Schrödinger operator with potential-measure*, https://arxiv.org/abs/1402.3995. These establish that weakly coupled two-dimensional bound-state asymptotics are classical background. The Gaussian specialization below is intended as a new step relative to the earlier folder, not a new general spectral phenomenon.

## Independent algebraic recheck

For gaps u_i, one coordinate of the difference Brownian motion has covariance 2 C, C_ij=min(t_i,t_j). Direct multivariate Gaussian integration gives A_n=(4 pi s)^(-n)/det(I+C/s). Independently eliminating the covariance one observation at a time gives predicted variance w_i=v_(i-1)+2u_i, factor [2 pi(w_i+2s)]^(-1), and updated variance v_i=2s w_i/(w_i+2s). Since 0<=v_i<=2s, the round-3 finite-time renewal sandwich follows with denominators 4 pi(u_i+2s) and 4 pi(u_i+s). The scalar Laplace transform is g exp(ar) E1(ar)/(4 pi), giving endpoints x_g/(2s), x_g/s. The Markov-property subadditivity argument and the scalar renewal rate proof also check. The earlier main mathematical claim holds.

## Chosen extension (recorded before carrying it out)

Prove the next step named by round 3: asymptotic sharpness of the lower endpoint as g=b^2 decreases to zero. Use the rank-one logarithmic singularity of the two-dimensional free resolvent, prove its remainder estimate for the noncompact Gaussian potential, connect the spectral bound to the pointwise second-moment rate, and calculate the prefactor explicitly. Target: gamma(b,s)=[exp(-Euler)/(2s)] exp(-4 pi/b^2) [1+O(b^2)]. This would imply gamma/(x_(b^2)/(2s))->1. Independently audit the Gaussian logarithmic-distance integral and the Bessel/resolvent normalization. This remains an annealed moment statement and yields no KPZ fluctuation exponent.

## Earlier computation rerun

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T090/check_gaussian_renewal.py` (read-only access to earlier script, bytecode disabled).

Output: all 515 determinant/recurrence cases, 3 closed-form cases, 4 scaling checks passed. Maximum absolute log-product discrepancy 9.663e-13; maximum independent scalar-integral relative error 1.238e-12. b=s=1 endpoints 9.79026725e-7 and 1.95805345e-6. Elapsed 0.051 seconds, peak RSS 12.406 MiB. Confirms the earlier calculation.

Resource detail: `nice` emits `setpriority: Operation not permitted`; Darwin address-space limit installation is unavailable, CPU limit 90 seconds succeeds. An attempt to inspect inherited niceness using `OMP_NUM_THREADS=1 nice -n 15 ps -o pid=,ni=,comm= -p $$` was denied (`ps: Operation not permitted`). Thus effective niceness is unverified; the warning alone does not establish ordinary priority. No substantial CPU load is being run.

## Resolvent derivation and proof audit

For V=R_s and v=sqrt(V), the Birman–Schwinger operator is K_E=v(E-Delta)^(-1)v. The heat kernel gives G_E(r)=(4 pi)^(-1) J(E r^2/4), J(a)=integral exp(-u-a/u) du/u. Splitting at sqrt(a) and substituting u->a/u in the lower half gives J(a)=2 integral_(sqrt(a))^infinity exp(-u-a/u) du/u. Its difference from 2 E1(sqrt(a)) has magnitude at most 2 sqrt(a). Therefore J(a)=-log(a)-2 Euler+O(sqrt(a)), with a global bound of that order after increasing the constant for a>=1. This derives the normalization directly without relying on a Bessel expansion.

Consequently K_E=t P+A+B_E, t=-log(E)/(4 pi), P=|v><v|, A(x,y)=v(x)v(y)[log(2)-Euler-log|x-y|]/(2 pi), and ||B_E||_HS=O_s(sqrt(E)). Gaussian second moments justify this norm bound on the whole plane; no compact-support assumption is slipped in. Block elimination with respect to P and I-P gives the top eigenvalue mu(E)=t+<v,Av>+O_s(1/t). The spectral threshold is mu(E)=1/g.

For independent X,Y with density R_s, X-Y has covariance 4s I and |X-Y|^2/(8s) is exponential of mean one. Thus E log|X-Y|=(log(8s)-Euler)/2 and <v,Av>=-[log(2s)+Euler]/(4 pi). Substitution yields the target prefactor. The remaining proof work is to spell out the spectral/pointwise rate identification and save the complete argument. The intended audit checks the same constant through angular averaging and through direct heat-kernel integration.

## Complete proof saved and numerical audit passed

Saved PROOF.md, including: a global resolvent remainder bound |R_E(r)|<=sqrt(E)*r/(2 pi); the explicit Hilbert–Schmidt bound ||B_E||^2<=2sE/pi^2; the variational proof of the spectral threshold; positive bounded eigenfunction lower bound; the Duhamel/L2 upper bound for the constant initial condition; block elimination for the eigenvalue; the exact Gaussian prefactor; comparison with x_g; spatial scaling; and diffusion normalization. A second analytic calculation of the Gaussian log-distance uses angular averaging and the maximum of two independent exponential variables.

Created check_prefactor.py and ran:

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_prefactor.py

Output:

```text
soft resource limit CPU seconds: 60
soft resource limit address space unavailable: current limit exceeds maximum limit
integral exp(-u) log(u): -0.57721566490153; expected -0.57721566490153
E log(max(U,V)): 0.11593151565844; expected 0.11593151565841
5 covariance scales: log-distance/prefactor checks PASS; max discrepancy 1.110e-14
s=1 prefactor: 0.28072974178344
heat resolvent: a, J(a)+log(a), error from -2*Euler
 1.0e-02 -1.09976247493176  5.467e-02
 1.0e-06 -1.15441666871983  1.466e-05
 1.0e-12 -1.15443132977451  2.855e-11
 1.0e-30 -1.15443132980307 -8.660e-15
zero-energy ODE diagnostic (not finite-g eigenvalues)
g        A/B+4*pi/g         residual from Euler-log(2)    step discrepancy
2       -0.071084665165  0.044846850494 1.679e-13
1       -0.094086324111  0.021845191548 1.208e-13
0.5     -0.105147360766  0.010784154893 6.040e-13
0.25    -0.110573322116  0.005358193543 7.816e-14
0.125   -0.113260801344  0.002670714314 8.527e-14
max RK4 step discrepancy: 6.040e-13
elapsed seconds: 0.076; peak RSS MiB: 11.828
PASS: floating-point audits only; the theorem is proved analytically in PROOF.md
```

All computations are deterministic, standard-library only, single-threaded, with constant-size state and a 60-second CPU limit. The sandbox again rejected nice priority adjustment and the address-space limit; measured RSS was far below 1 GB. The ODE rows are explicitly diagnostics of a zero-energy equation, not numerical estimates or certified enclosures of the finite-g moment exponent. No scattering-length theorem is used in PROOF.md.

A subsequent attempted log patch used an anchor from PROOF.md by mistake and failed verification without changing a file; the correct append is this entry.

## Attempts to break the result

1. **Diffusion and interaction factors.** Re-derived the closed second-moment PDE directly by Itô multiplication. Pair covariance contributes gR_s exactly once, and the difference process has generator Delta, not (1/2)Delta. Independently, time rescaling for diffusion d gives gamma_d=(d exp(-Euler)/s) exp(-8 pi d/b^2)(1+O(b^2/d)). At d=1/2 this returns the theorem. The constant 1/2 in the Gaussian prefactor is also recovered by the angular-maximum calculation, which does not use the Gaussian difference density.
2. **Gaussian support and resolvent tails.** No compact-support theorem from the cited background is applied. The proof actually has the global bound |J(a)+log(a)+2 Euler|<=4 sqrt(a) for all a>0, since (9)'s integral is at most sqrt(a) and the split-integral error is at most 2 sqrt(a). Thus the earlier note's proposed large-a case split is unnecessary. Multiplication by the two Gaussian weights gives a finite explicit Hilbert–Schmidt error <=sqrt(2sE)/pi. The logarithmic diagonal singularity is square integrable in two dimensions.
3. **Constant initial data not in L2.** A direct appeal to an L2 spectral limit would leave a gap. Instead, the proof bounds T_t 1 above using 1+g integral T_u V du, where V is in L2 and a one-unit kernel smooths evaluation at zero. The bounded strictly positive top eigenfunction gives the reverse bound. Thus the spectral threshold is indeed the pointwise moment rate.
4. **Existence and choice of eigenvalue.** The compact positive Birman–Schwinger operator has a continuous strictly decreasing top eigenvalue from infinity to zero. Its unique crossing at 1/g is an upper spectral bound by the quadratic form and an attained eigenvalue by the resolvent construction. There is no assumption of a unique bound state, or of isolation from an unexamined essential spectrum, in the rate argument.
5. **Perturbation error.** Block elimination bounds the correction by C_s^2/(ell-2C_s), rather than discarding the off-diagonal block. At the crossing ell=1/g+O(1), so the log-eigenvalue error is O(g), producing relative error O(g). The heat-kernel remainder is exponentially smaller there. This establishes the claimed relative convergence, not merely the previously known limit g log(s gamma)=-4 pi.
6. **Excluded boundaries and scope.** b=0 has Z=1 and rate zero; the positive root description excludes it, consistently with the limiting formula. Negative b gives the same g. s=0 is excluded; all s>0 are related by exact scaling. The result requires the specified Gaussian covariance and flat initial condition. No claim about logarithmic height variance or KPZ exponents follows. The zero-energy ODE calculation is labelled only as a diagnostic; it is not used to estimate the finite-g eigenvalue or justify the proof.

No counterexample or mathematical gap in the stated Gaussian asymptotic was found. The general weak-bound-state mechanism is established background, and novelty of this particular Gaussian formula in the wider literature has not been checked.

Source attribution for the status check: Quentin Berger, Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu, Shuta Nakajima, Rongfeng Sun, Li-Cheng Tsai, Zuodi Xie, Nikos Zygouras, *The Critical 2D KPZ Process*, https://arxiv.org/abs/2610.31614 and https://arxiv.org/html/2610.31614v1. These were opened, not inferred from search snippets.

Two early directory-listing calls inadvertently listed the entire large memory directory and yielded oversized output. Both have completed with exit code 0; their output was truncated and not used as evidence for any mathematical claim. Subsequent orientation reads used exact filenames. Neither command mutated files.

## Final resource and artifact audit

Resolved the remaining priority uncertainty with a read-only Python API query:

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B -c 'import os; print("effective process niceness:", os.getpriority(os.PRIO_PROCESS, 0))'

Output: `nice: setpriority: Operation not permitted`, followed by `effective process niceness: 20`. Thus these shell-launched processes inherit niceness 20, already more polite than 15. The warning concerns an attempted further increment. It does not mean ordinary priority. This also corrects the earlier report's unsupported interpretation of that warning, while leaving its mathematical results intact. REPORT.md has been updated accordingly.

At 2026-11-15 04:55:22 +04, checked `head -1 REPORT.md`, `wc -lc REPORT.md PROOF.md LOG.md check_prefactor.py`, and targeted `rg` matches for verdict, theorem, normalization, limitations, failures, next worker, and task clock, all with `OMP_NUM_THREADS=1 nice -n 15`. Confirmed the exact required verdict prefix, the complete 22-equation proof, and all four nonempty deliverables. Files totaled approximately 36 KB before this final log entry. The selected continuation is proved; the original KPZ exponent problem remains open here. No SOLVED_ELSEWHERE.md was created because no solution of the stated fixed-coupling problem was found.
