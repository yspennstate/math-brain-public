# T265 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 03:40 Asia/Tbilisi (23:40 UTC on 14 November).

## 03:40–03:44 +04 — orientation, earlier work, bounded literature check

Read the earlier REPORT.md, LOG.md, PROOF.md, AUDIT.md, SOLVED_ELSEWHERE.md, and audit.py in `~/codex_op_1114/briefs/T265`; that directory remains read-only. Read the startup memory index and brain navigation index. The later task-specific instruction allows writes only here, so did not run global brain, mesh, or checklist commands that mutate outside this directory. No git or subagents. Governor read at start: status warn, mode owner_away_open, memory free 55%; only tiny standard-library computations planned, one thread, nice >=15, no training libraries.

Literature searches via the web tool included `"benign overfitting" "ReLU" "2026" "dimension"`, `"2505.16204" Hashimoto`, `"benign overfitting" "two-layer" "low-dimensional"`, and the Park et al. regression title. Opened Hashimoto arXiv:2505.16204v3 abstract and HTML, Karhadkar et al. arXiv:2403.06903 abstract, Park et al. arXiv:2410.06191 and arXiv:2505.11621 abstracts, and Xingyu Xu and Yuantao Gu's AISTATS 2023 paper PDF. Hashimoto still has version v3, revised 10 February 2026; Assumption 6.1(a) contains tr(Sigma)>=C n ||Sigma||_F, and (b) contains tr(Sigma)>=C n ||Sigma||. For nonzero covariance these imply d>=C^2 n^2 and d>=C n, respectively. No verified new whole-problem solution found in this bounded check. A separate literature note will preserve exact references and scope.

## Independent re-derivation of the earlier result

For a fixed input sample, let A be its set of affine prediction vectors and q_i the smaller label posterior. Every particular vector has conditional label probability at most product_i(1-q_i). Summing over |A|<=2 sum_{j<=min(d,n-1)} binom(n-1,j), and then averaging iid inputs, gives exactly M_(n,d)(1-alpha)^n. This independently obtains the earlier interpolation claim without stochastic coupling. For k errors, couple each vector's independent conditional errors above Bernoulli(q_i); the comparison tail is common to all vectors. Averaging that Poisson-binomial tail gives Bin(n,alpha), because the pairs (X_i,U_i) are iid. The affine arrangement count and its tie perturbation are valid. Thus the earlier main claim holds. An independently written script will check its numerical example and exact small cases, without importing or running the earlier script (which would write to its own folder).

## Chosen extension — recorded before proof work

Prove an explicit localization construction for *bias-free* two-layer ReLU networks on the same Gaussian mixture, in d>=3: exact real-valued interpolation of all noisy labels, while differing from the Bayes linear score only on a set with arbitrarily small population probability. Use a two-dimensional projection orthogonal to the signal and homogeneous triangular functions supported in narrow pairs of antipodal cones. Give the exact width, population bound, and parameter cost, and combine with the earlier affine obstruction.

Why: this is the representational portion of the earlier report's concrete localization target. It addresses the nonlinear gap without assuming a GD trajectory. It deliberately leaves GD selection unresolved. The construction must respect the identity f(x)-f(-x)=linear for every bias-free shallow ReLU network, so point-supported Euclidean tents are not available. Paired cones avoid that obstruction.

## Refinement of the same localization piece

Use a fixed coordinate plane instead of an oracle plane perpendicular to mu. A direct density calculation for the slope V/U of a two-dimensional shifted Gaussian gives f_T(t)<=C_s/(1+t^2), where C_s=1/pi+s/sqrt(2pi), s=||mu||/sigma. This will make the interpolation rule completely data-dependent: start with v_n=n^{-1}sum_i Y_i X_i, place paired conical triangular corrections at the observed slopes, and choose each slope half-width <=n^{-3} and <=one third of its nearest gap. The expected excess classification risk should then be at most sqrt(2/pi)*sqrt((d+4 eta(1-eta)s^2)/n)+2C_s/n^2. The proof and exact algebraic audit will verify every constant. This is still one localization extension, strengthened to an explicit consistent interpolating estimator; it is not a GD estimator.

## Independent numerical recheck completed

Created recheck.py independently; did not import or execute the earlier script. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck.py
```

Exit 0. Exact enumeration checked all 512 label vectors with nine distinct nonconstant posteriors and all ten lower-tail thresholds. Gaussian tail was independently integrated by Simpson quadrature. log M was evaluated both by exact integer binomial sums and lgamma/log-sum-exp. Output: alpha=0.1182001055585434, log M=142.5453296114031, log interpolation bound=-1115.3559280519955, 99% lower error=0.032424089156115624. These agree with the earlier report to displayed precision. Actual niceness=20, peak RSS=15,138,816 bytes; wall time <1 second. The wrapper warned `nice: setpriority: Operation not permitted`; the script verifies inherited niceness >=15 before calculating, so the completed run meets the priority rule. Results saved in recheck_results.json. The earlier main result holds.

The literature check is closed; exact opened references and limitations are in LITERATURE.md. The fixed-plane construction also works in d=2; no perpendicular-to-mu plane is needed after the slope-density lemma.

## Proof and first construction audit

Saved PROOF.md. The interpolation rule uses six bias-free ReLU neurons per paired cone, plus two for the baseline v_n^T x. The risk argument combines an explicit bound on the shifted-Gaussian slope density with a direct second-moment bound for v_n. It covers d>=2 and contains no GD claim.

Created audit.py using only the standard library and exact rational arithmetic for network evaluations. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

Exit 0, wall time about 0.15 seconds. Output: 360 exact triangular identities, 139 exact network evaluations, 107 exact support checks, 14 endpoint/norm checks, 3 rejected degenerate inputs; 42 shifted-Gaussian density checks against Cartesian quadrature, 6 independent projective-angle normalization integrals, 18 cone-mass checks by Cartesian and polar integration; 32 exact moment atoms and 1,024 exact two-sample pairs; 72 baseline-risk inequalities. Maximum relative density discrepancy was 6.51e-13. Actual niceness=20 and peak RSS=16,285,696 bytes. The same harmless `nice` adjustment warning appeared; the inherited priority guard passed.

Example n=10000,d=20,s=2,eta=0.1: width<=60002, Bayes risk=0.11820010555854338, population score-disagreement bound=2.2323888939733122e-8, expected excess-risk bound=0.03694474849632246. These are rigorous formula evaluations, not trained-network measurements. A deliberately nearly degenerate rational sample had displayed path norm about 2.56e26, confirming that small disagreement probability does not control parameter norm or numerical conditioning.

## Adversarial review in progress

Independently derived the slope-density constant through projective polar coordinates, and the baseline second moment through Cov(YX)=sigma^2 I+4 eta(1-eta)mu mu^T. Checked the Gaussian zero-signal and baseline zero-vector cases explicitly. Paired cones respect f(x)-f(-x)=linear; ignoring this identity would invalidate a one-sided spike construction. Exact antipodal or repeated projected directions are excluded only on a Gaussian null event. The construction needs d>=2 and real-valued coefficients; finite precision and GD selection are not established. A second nearly antipodal case in the audit currently has a baseline that already fits its labels; change its labels to force nonzero corrections before the final run.

The review also gives a sharper risk estimate within this same construction: s(1-cos(theta))=(s/2)||v/||v||-mu/||mu||||^2. Combining this identity with the already proved normalization inequality replaces the baseline square-root bound by sqrt(2/pi)*V/((1-2eta)s) when s>0, where V=(d+4eta(1-eta)s^2)/n. Take the minimum of the two bounds. This yields order d/n for fixed positive signal and fixed eta<1/2. Add the full derivation and audit both pointwise bounds before the final run.

## Final audit after the sharper estimate and forced corrections

Reran the same `nice -n 15 python3 -B audit.py` command with the four one-thread environment variables. Exit 0; wall time about 0.14 seconds. Final output counts: algebra_cases=360, exact_network_points=139, exact_support_checks=107, endpoint_norm_checks=14, rejected_degeneracies=3, density_checks=42, density_normalizations=6, cone_mass_checks=18, exact_moment_atoms=32, exact_sample_mean_pairs=1024, baseline_risk_checks=72. Maximum density relative discrepancy=6.509928519596081e-13. Both pointwise baseline-risk estimates passed, including v=0 and reversed directions.

The revised nearly antipodal sample now has nonzero corrections and path norm 32000.66355687642. All 14 interpolation endpoints remain exact. The sharpened example gives expected_excess_bound=0.0010691876353647793; the earlier square-root bound remains 0.03694474849632246. Independently, its variance/((1-2eta)s) factor is exactly 67/50000; multiplying by 2/sqrt(2pi) and adding the localization term agrees. Localization bound=2.2323888939733122e-8, width=60002. Final actual niceness=20, peak RSS=15,728,640 bytes. All scripts have 60-second CPU and wall guards. Final JSON is audit_results.json.

## Handoff

Saved REPORT.md with verdict PARTIAL, the explicit estimator, risk bound, evidence, limitations and next target; saved AUDIT.md with independent derivations and attempted counterexamples. The main GD question remains open in this work. No global task/checklist/mesh/brain state was modified because this task explicitly limits all writes to this directory. No git, subagents, external messages, accounts, GPU or numerical/training libraries were used. Earlier files were read only.
