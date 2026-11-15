# T265 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 09:02 Asia/Tbilisi.

## Orientation and literature check — 09:02–09:04 +04

Read the three prior REPORT.md, LOG.md, PROOF.md files and their Python scripts. Read the startup memory index and compute governor: status ok, mode owner_away_open. Only small standard-library computations are planned, with single-thread environment variables, nice -n 15, and resource guards. The specific instruction allowing writes only in this folder overrides global brain/mesh/checklist writes; those commands are not run. No git or subagents.

The web check used searches for benign overfitting, ReLU, non-orthogonality, n >= d, and 2026, and for arXiv:2505.16204. Opened Ichiro Hashimoto's abstract and full v3 HTML (last revised 10 February 2026), and the arXiv abstract of Kedar Karhadkar, Erin George, Michael Murray, Guido Montúfar, Deanna Needell, arXiv:2403.06903. Hashimoto's probabilistic conditions still include trace-versus-n covariance restrictions; Karhadkar et al. explicitly require d=Omega(n). No verified solution of the full ReLU/GD many-samples question was found. Search is closed after approximately two minutes. Only opened primary sources will be cited in LITERATURE.md.

## Independent re-derivation of the earlier result

The round 4 intrinsic norm formula holds. For an arbitrary finite representation, aggregate coefficients b+ and b- on each unoriented hyperplane. Its score is gamma |u.x| + t u.x, where gamma=(b++b-)/2 and t=(b+-b-)/2; its cost is at least 2 max(|gamma|,|t|). Local gradient jumps force gamma=beta on the listed hyperplanes and gamma=0 elsewhere. Clipping t to [-|beta|,|beta|] leaves a vector in the zonotope; the triangle inequality bounds the remaining linear cost below by twice its distance to v. A nearest-point allocation and one linear pair attain the bound. This independently checks the main universal lower bound, including extra hyperplanes and cancellations.

For the explicit sample X1=(1,0), X2=(1,3), labels +1,-1, the baseline is (0,-3/2), residual amplitudes 1,7/2. The narrow lower bound is 4(9/2)/(1/8)=144. The wider upper bound is 8+70+3=81. These agree with the earlier report without using its code. The displayed balanced-realization descent also holds: differentiating the correction cost after z=1/h gives a strictly negative width derivative, and center hyperplanes have zero tangent preactivation. A new independent script will verify the numerical norm values and identities in this folder.

## Chosen extension, before proof work

Determine whether the earlier localized score can satisfy the generalized unit-margin parameter KKT conditions in ANY finite bias-free two-layer ReLU representation with both layers trainable. The previous report excludes only its displayed balanced realization. The target is a necessary condition on the score's forced hyperplanes derived directly from the per-neuron KKT equations, allowing extra directions, coefficient splitting, cancellation, and arbitrary derivatives at zero. If a universal statement is false or requires a width restriction, retain the exact condition and identify a checkable special case rather than infer GD selection.

## Candidate representation-independent obstruction — 09:09 +04

For a KKT multiplier vector define D(u)=sum lambda_i Y_i rho(u.X_i). Per-neuron stationarity gives balance and D(u)=sign(a) at every used unit direction. At an endpoint normal u_e, no sample preactivation vanishes; its active-sample vector must equal sign(a) u_e. The center direction u_c lies in the closure of that same activation cell. Thus D(u_c)=sign(a) u_e.u_c, whose absolute value is strictly less than one. No neuron on that oriented center can occur. A nonzero center kink is forced by equality of scores, so it must use the opposite orientation. Both endpoints must then use the same other orientation, with coefficient sign sign(A). Computing D at the center from both adjacent cells forces u_left.u_c=u_right.u_c. For slope-symmetric edges q(t-h), q(t+h), this angular-bisector identity holds only when t=0. This would exclude every finite representation whenever one nonzero cone has t!=0, with no bound on width or norm and regardless of extra hyperplanes. Need to check all zero-neuron, splitting, subgradient, and degenerate cases before finalizing.

## Proof saved; first resource guard rejected

Saved PROOF.md with the necessary angular-bisector identity, its contradiction for every nonzero center slope, and the almost-sure Gaussian consequence. Also found and proved an exact three-neuron KKT example at center slope zero, with norm and multiplier sum both 10. This counterexample shows that the nonzero-slope restriction cannot simply be dropped for arbitrary baselines. It does not use the sample-mean baseline and does not contradict the Gaussian statement.

Created recheck.py and audit.py, both standard-library-only, with CPU and wall limits of 60 seconds and inherited-priority checks. First command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck.py
```

Exit 1 before mathematical computation: macOS rejected setting RLIMIT_AS to 768 MB with `ValueError: current limit exceeds maximum limit`. Removed that unsupported virtual-address-space guard from both scripts; these fixed-size small checks will instead report measured peak RSS. CPU and wall guards remain. The wrapper also printed the earlier sessions' `nice: setpriority: Operation not permitted`; the priority guard passed before the resource error, so inherited niceness already met the requirement.

## Independent round 4 recheck passed

Reran the same command after removing only the unsupported resource guard. Exit 0, under one second. The new code used a different baseline-absorbing representation at each width, evaluated its path cost, and independently summed forced gradient-jump norms using 70-digit Decimal square roots. Narrow norm 386.3134673380746; wide norm 49.221478356835924. Exact rational baseline allocations attain both lower bounds. Verified 294 exact score identities, twelve exact gradient jumps, the integer bounds 144>81, and fifteen derivative comparisons between direct per-neuron differentiation and the closed cost formula. Actual niceness 20; peak RSS 16,515,072 bytes. Results saved in recheck_results.json. The earlier result holds.

## New theorem audit passed

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

Exit 0, wall time 0.23 seconds. Enumerated all 27 nonempty orientation-support triples; 25 are incompatible with the endpoint/center restriction and exactly two survive, each with both edges opposite the center. Verified 432 exact activation-cell closure identities across dimensions 2,3,5, both input signs and both orientations; 1,296 exact zero-derivative identities; 35 high-precision geometry cases, including tiny widths; 28 independent trigonometric comparisons (maximum discrepancy 3.89e-16). Five zero-center cases passed the angular equality, as expected.

Verified twelve exact KKT counterexamples at zero center: 36 full stationarity vector identities, 36 unit margins, 192 exact score identities. Their positive multiplier sums and balanced objectives are exactly 10,12,...,32. The displayed k=5 certificate gives h=5/12, center derivative 13/48, multipliers (10/13,288/65,24/5), and J=sum lambda=10. These are exact rational checks; no numerical optimizer was used. Actual niceness 20; peak RSS 16,187,392 bytes. Results saved in audit_results.json. The wrapper's denied nice adjustment was harmless because the inherited-priority guard passed.

## Adversarial review and source audit

Re-read PROOF.md against the equations. The argument does not assume that a representation minimizes path norm: it uses necessary neuron stationarity and forced gradient jumps. New directions and orientation cancellation do not evade it; same-orientation cancellation is impossible by D(u)=sign(a). All center derivatives disappear from score evaluations, so independent subgradient freedom cannot repair the angular mismatch. The determinant proof and the independent arctangent computation agree on the load-bearing identity. The zero-center counterexamples prevent an overbroad conclusion.

The almost-sure residual assertion was checked separately: for each fixed label vector, Y1-n^(-1)sum_j Yj Xj.X1 is a nonzero polynomial (value Y1 at all zero inputs), so its zero set has measure zero. Joint input/label measures are absolutely continuous in the input coordinates. No independence of the residual and slopes is needed.

Reopened the already-read Hashimoto Assumption 6.1 to verify the exact covariance terms, without any new search; its dimension restrictions remain as stated. Saved LITERATURE.md and AUDIT.md. No claim about GD convergence, approximate stationarity, or risk of other interpolants is inferred from the new theorem.

## Handoff complete

Saved REPORT.md with the required PARTIAL verdict, the representation-independent theorem and almost-sure Gaussian consequence, the exact KKT exception, all commands, failed guard and false overgeneralization, and limitations. The next target is angularly symmetric localization and compatibility of shared multipliers across many centers. All authored files and computation outputs stayed in this folder. Earlier folders remained read-only. No git, subagents, external messages, account creation, GPU, or training libraries were used. T265's main GD benign-overfitting question remains open in this work.
