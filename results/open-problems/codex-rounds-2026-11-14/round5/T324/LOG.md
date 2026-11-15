# T324 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 09:09 +04 (Asia/Tbilisi). The prompt itself has no timestamp.

## 1. Orientation and bounded literature check

Read the startup memory, compute governor, and the reports, proofs, logs and verification scripts in the three predecessor folders. Those folders are read-only for this task. The current folder initially contained PROMPT.md, codex.log and run.pid. The governor reported status ok, mode owner_away_open; all computations here will nevertheless use one thread and nice 15 or lower priority. The specific folder-only order prevents writes to the shared brain, mesh and checklist, so those state-changing commands are not run. No git or subagents.

Within the first five minutes, searched the web for `"2410.23228" metastable clustering 2025 2026` and `"transformer" "metastability" "noise" clustering merging 2026`. Opened arXiv pages 2410.23228, 2312.10794, 2504.14697, 2509.25040, 2512.01868, 2608.08922 and 2610.08755, and the HTML of 2509.25040. The known multiscale follow-up has no new revision; the newer noise paper has hypotheses and a large-N limit distinct from the requested normalized-attention, large-beta problem. No later complete resolution was found in this limited check. See LITERATURE.md. This is not a novelty certification.

## 2. Independent recheck and choice

The round-4 velocity derivative is re-derived from the logarithmic derivative of the row weights: dV/dtheta = -E cos + beta Var(sin). On a narrow group this is at most -1+(beta+1/2)w^2+(beta+2)epsilon. Its internal mean-drift cancellation follows by exchanging the two integration variables, giving one half of the difference of reciprocal row sums. The signs, factors and final deterministic hitting-time sandwich agree with the earlier proof. An independent numerical recheck is being prepared using midpoint integration rather than RK4, as well as a local redirected rerun of the earlier script.

Chosen extension (before proving it): a stopped concentration theorem for two finite groups with independent angular Brownian noises, including the exact group-center variance and a quantitative error relative to the scalar drift. This is the missing estimate explicitly named in round 4. A finite time bound with its token-count and time-horizon factors is preferable to silently identifying each noisy group with an independently noisy atom. The basic mechanism will be pairwise contraction plus Brownian maximum bounds on unit time intervals. If these bounds suffice, derive persistence of the deterministic merging prefactor when the noise exponent exceeds the deterministic waiting exponent. No assertion about the noise-dominated regime is planned.

## 3. First recheck run

Command: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck.py > recheck_output.txt 2>&1`.

The earlier script passed unchanged, with its output redirected to this folder by setting its ROOT global before calling main. It reproduced the full six-token time 159.656205 at beta=14, derivative bounds -0.863807204, -0.959970992, -0.95999 at beta=500,1000,2000, and kernel/BVP discrepancy 2.019e-8. Its run took 4.088 seconds and 17.75 MiB RSS, effective nice 20. The independent explicit-midpoint solve then passed agreement with RK4 at its finer step but failed its own .02/.01 refinement threshold 2e-6. This is a numerical resolution failure, not a contradiction to the earlier theorem. Refined both steps to .01/.005 and kept both tolerances. The nice warning is inherited from an effective priority already lower than requested; the program checks nice>=15 before computing.

## 4. Recheck holds; stochastic estimates derived

The same command with refined midpoint steps exited 0. Full output is in recheck_output.txt. At beta=10, midpoint time 19.2480286659063 versus earlier RK4 19.2480316478517, relative error 1.5492209559653247e-7. At beta=14, midpoint 159.6562185450334 versus RK4 159.6562045570337, relative error 8.761325465123093e-8. The refined run took 4.709 seconds overall, peak RSS 17.563 MiB. The earlier analytic result and computation hold.

For a pair in one group, D satisfies dD=c_t D dt+sqrt(4 nu)dB with c_t<=-1/2 while the groups stay in a separated narrow tube. Integration by parts on a unit interval bounds its stochastic response by twice the Brownian maximum on that interval. Iteration gives W(t)<=w_0 exp(-t/2)+K u, K=2+2/(1-exp(-1/2)), except with probability at most 4 M ceil(T) exp(-u^2/(8 nu)), where M is the number of within-group unordered pairs. This is a stopped estimate; it does not assume independent pair differences.

For equal token weights, the group-center gap martingale has quadratic variation 2 nu(1/n_A+1/n_B)t, derived by summing the original independent Brownian motions. Pointwise symmetrization and the current gap s give a sharper residual bound |R|<=C[beta w^3+(beta+1)w h_beta(s)] when beta w<=1. Using only a fixed coarse cross-attention bound would not suffice for this relative estimate; retaining its dependence on the current separation is essential.

These estimates support the following additional conclusion within the same noisy-group extension: for fixed group sizes, initial widths satisfying the earlier hypotheses, and -log(nu_beta)/beta->r>1-cos(x), the deterministic merging prefactor survives in probability. The proof will subtract the center Brownian path and compare the remaining absolutely continuous gap with the scalar drift. No mean-time assertion follows without control of exceptional-event tails.

## 5. Proof saved

Saved PROOF.md, with every step of the concentration bound, exact center-noise calculation, current-gap-dependent internal drift estimate, and the weak-noise merging theorem. The theorem uses the slightly wider auxiliary tube 1/(3 sqrt(beta)), which contains all initial widths allowed by round 4; the sufficient derivative bound still has a fixed margin. The initial width hypothesis itself is unchanged. A first-exit argument controls the transient until 4 beta, then subtracting the center martingale produces an absolutely continuous gap and a scalar hitting-time sandwich. This avoids using an exponentially growing global Lipschitz error bound and avoids an unjustified scalar Markov assumption.

The full prefactor holds in probability under beta^2 w_beta^3->0 and liminf[-log(nu_beta)/beta]>1-cos(x). Without the extra width condition, the same proof gives only log(tau)/beta->1-cos(x) in probability. The statement includes arbitrarily fast-decaying positive noise. It does not transfer the earlier two-atom mean-time law to groups.

Analytic checks so far: the pair noise has variance rate 4 nu; the center noise has variance rate 2 nu(1/n_A+1/n_B), verified again by the original N-angle generator. The pair block response factor is 2, its geometric accumulation is K=2+2/(1-exp(-1/2)), and its reflection denominator is 8 nu. The center reflection denominator is 4 nu chi T. The three exponent inequalities needed for the weak-noise theorem are 2 kappa<r_0, 3 kappa>1-cos(L), and H+2 gamma<r_0; their simultaneous feasibility is proved in Section 5.

## 6. New numerical verification passed

Command:

~~~sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1
~~~

Exit 0, elapsed 2.493 seconds, peak RSS 14.969 MiB, effective nice 20. Full output is in verification_output.txt and all data in verification.json. No external packages, subprocess workers, GPU or large arrays. The script enforces a 120-second CPU limit.

All six check groups passed: exact center coefficient norms plus Gaussian sampling; 81 pointwise drift-residual cases; exact kicked contraction equations with adapted damping; 15 feasible parameter choices including gaps .001 and 3.13 and a noise-rate margin .01 percent; 12 finite-time noisy five-token paths satisfying the explicit high-beta contraction condition; and eight full merging paths with coupled coarse/fine Brownian increments.

Output that matters:

~~~text
K: 7.082988165073597
Maximum center variance relative sampling error: 0.013389679320400694
Maximum exact drift residual / explicit bound: 0.032599929830756824
High-beta width check: beta=500, nu=1e-9, dt=.01, T=20, trials=12,
  sufficient derivative bound=-0.851415411290588,
  theoretical block-event failure bound=8.579212376901801e-12,
  maximum measured width=.001994674389177664,
  maximum grid pair increment=.000261615431506573, u=.0005.
~~~

The theoretical failure bound is from (7), not an estimate from 12 samples. Discrete Brownian grids miss bridge maxima and do not certify the continuous-time event. The stochastic paths are consistency checks only. At beta=10 the four full token/scalar time ratios range from .9661034 to 1.0089001; at beta=14 from 1.0058669 to 1.0106339. The largest coupled .04/.02 time-step discrepancy is 2.9473791626877244e-5. These moderate-beta paths do not verify an exponential-time limit or its sufficient high-beta contraction hypotheses; the proof supplies the asymptotic result.

The new verification script passed on its first run. The only computational failure in this session was the earlier independent midpoint recheck at insufficient resolution, recorded in Section 3.

## 7. Independent analytic audit and final run

Added Section 9 of PROOF.md as a second concentration argument. For a stopped within-group pair D, Itô's formula for F(D)=exp(D^2/(16 nu)) gives LF<=(1/4-D^2/(32 nu))F<=1/4. The last inequality follows by differentiating (1/4-z/32)exp(z/16), which is decreasing for z>=0. Optional stopping and a union bound give the independent exit bound (39), with exponential denominator 16 nu. This checks the variance factor and long-horizon concentration without the unit-block argument. It does not replace the transient envelope used for merging.

Added a separate numerical check of this generator identity and reran the same verify.py command because this was new validation. Exit 0; final run elapsed 2.253666875 seconds, peak RSS 15.3125 MiB, nice 20. The alternative-generator algebra agreed within 5.4569682106375694e-12 over 3003 points; maximum LF was .25. All earlier checks still passed. Final resources in verification.json and verification_output.txt supersede the first run's resource measurements.

The scalar prefactor was re-derived a second way: for two atoms put c=cos(s). Direct projection gives c'=(1-c^2)(f_A+f_B), and f_A+f_B~(p/q+q/p)exp[-beta(1-c)] on a fixed gap interval. Endpoint integration in c gives exp[beta(1-cos(x))]/[(p/q+q/p)beta(1-cos(x)^2)], the same prefactor and sign as the angular integral. The two singleton noise coefficients also recover exactly 4 nu for the gap variance, while equal n-token groups give 4 nu/n.

Searched for missing cases: within-group token crossings do not invalidate the common-field derivative argument; simultaneous gap and width exits are included in the Lyapunov bound; a negative sine lower factor in the cross comparison is handled by positivity; beta w may be large during the initial relaxation, so only the rough bound (21) is used there; the sharp residual (9) is used only after contraction. No global fixed-arc invariance under Brownian noise is assumed. The upper gap boundary is excluded only after subtracting the center martingale. At r=1-cos(x), the exponential horizon choices fail, so that case is explicitly outside the theorem. No upgrade from probability to mean is made.

## 8. Final artifact audit

Wrote REPORT.md with the required first-line verdict and the next missing step. Under the same thread/nice launcher, a short standard-library heredoc read the saved artifacts, compiled both scripts without writing bytecode, checked the verdict, checked balanced mathematical delimiters, and checked that all 39 equation tags are consecutive and unique. Exit 0. It read back the final resource data, the largest full stochastic coupled-step error 2.9473791626877244e-5, and the largest independent predecessor error 1.5492209559653247e-7. All eleven report, proof, log, literature, script, data and output files exist here.

The result remains PARTIAL relative to T324. The noisy concentration estimate and weak-noise merging theorem are proved; the generic cluster-count problem and the noise-dominated/mean-time extensions remain open within this work. All writes were confined to this folder.
