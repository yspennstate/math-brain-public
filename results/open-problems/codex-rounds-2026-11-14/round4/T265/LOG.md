# T265 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 06:26 Asia/Tbilisi.

## Orientation and bounded literature check

Read both earlier REPORT.md, LOG.md, PROOF.md, and all three earlier scripts (the original audit.py and round 3 audit.py/recheck.py). Read the startup memory index and compute governor: status warn, mode owner_away_open, CPU saturated, memory free 59%. Only small standard-library checks are planned. The task-specific rule restricts all writes to this folder, so global brain/mesh/checklist commands that write elsewhere are not run. No git, subagents, or training libraries.

The web literature check used three initial searches: `"benign overfitting" "ReLU" "n" "2026"`, `"2505.16204" Hashimoto`, and `"benign overfitting" "low dimensional" "two-layer"`; a follow-up searched the Park et al. title and path-norm question. Opened arXiv:2505.16204 abstract and v3 HTML, arXiv:2410.06191, arXiv:2505.11621, arXiv:2403.06903, and arXiv:2604.00505 abstracts. The check is closed, within five minutes of its first search. No verified whole-problem solution found. The Park abstracts concern approximate regression fitting; Hashimoto remains v3 (10 February 2026); Karhadkar et al. still state d=Omega(n); Lei and Xie give initialization-dependent generalization bounds, not this GD interpolation theorem. Exact references and scope will be in LITERATURE.md. No secondary site's mathematical claims are being used.

## Earlier result independently re-derived

For r=(v/u)-t, the centered second difference of |r| is 2(h-|r|)_+, giving H=|u|(1-|r|/h)_+. Disjoint slope intervals therefore give exact interpolation with six ReLUs per correction. The ratio change of variables has Jacobian |u|; integrating the centered absolute Gaussian bounds its density by [1/pi+s/sqrt(2pi)]/(1+t^2). Thus sum_i 2 C_s h_i <= 2 C_s/n^2 independently checks the localization bound. Also YX has the same law as F mu+sigma Z with Z independent standard Gaussian, so Cov(YX)=sigma^2 I+4 eta(1-eta)mu mu^T. For fixed v the excess risk is a[Phi(s)-Phi(s cos theta)], bounded by (a/sqrt(2pi))s(1-cos theta). The normalization inequality then recovers both round 3 baseline-risk bounds, including the factor sqrt(2/pi) V/(a s). The zero-vector and zero-signal cases in its proof are valid. The round 3 main result holds on this independent derivation. A newly written rational audit will check interpolation and numerical constants without running earlier scripts in their folders.

The original affine obstruction also holds: conditional on inputs, each affine prediction vector has probability of matching all labels at most product_i(1-q_i). Summing over at most 2 sum_{j<=d} binom(n-1,j) vectors and averaging iid inputs gives M(1-alpha)^n. The analogous conditional error coupling gives its binomial lower-tail bound.

## Chosen extension, recorded before proof work

Determine the minimum path norm over ALL finite bias-free ReLU representations of the earlier localized score, and compare it with a wider-cone interpolant of the same sample. More generally, for distinct unoriented unit normals u_k, analyze f(x)=v^T x+sum_k beta_k |u_k^T x|. Candidate formula:

    inf sum_j |a_j| ||w_j||
      = 2 sum_k |beta_k| + 2 dist(v, sum_k [-|beta_k|u_k, |beta_k|u_k]).

Gradient jumps across each hyperplane should force the absolute coefficients, while asymmetric pairs of ReLUs can absorb a linear term for free up to the displayed zonotope. Apply this formula to show that, for a fixed nondegenerate sample with a nonzero residual, sufficiently narrowing the earlier cones cannot minimize path norm even among interpolating scores. Supply an explicit finite-sample certificate. This is the earlier report's requested implicit-objective comparison, not a GD selection claim. Prove the formula and comparison fully, then audit the critical quantities a second way.

## Proof saved and independent recheck run

Saved PROOF.md with the exact norm formula, a lower bound allowing arbitrary extra hyperplanes, an attaining representation, a separate dual distance certificate, the conical specialization, a fixed-sample shrinking-width comparison, and an explicit sample with narrow intrinsic norm >=144 versus a wider interpolant of norm <=81. Also proved the equivalent minimum balanced parameter cost. The argument concerns global margin minima, not arbitrary KKT points or GD trajectories. Saved LITERATURE.md with opened primary references and bounded scope.

Created recheck.py independently. It uses a three-hinge identity, rather than the earlier six-neuron code: the linear second difference vanishes, so [rho(q(t-h)^T x)-2rho(q(t)^T x)+rho(q(t+h)^T x)]/h equals H. This identity provides an additional representation check with the same path cost. No earlier scripts were executed or imported.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck.py
```

Exit 0, wall time 0.16 seconds. Output: earlier_result_holds=true; 96 rational samples; 528 exact interpolations; 9,504 three-hinge identities; 528 exact support checks; 16 direct Cartesian ratio-density integrals. Bayes risk=0.11820010555854385; localization bound=2.2323888939733122e-8; expected excess bound=0.0010691876353647793; affine log probability bound=-1115.3559280520174. These agree with both earlier reports. Actual niceness=20, max RSS=15,204,352 bytes. The wrapper printed `nice: setpriority: Operation not permitted`, but the script checks inherited niceness >=15 before any computation and passed. Results are in recheck_results.json. The script has 60-second CPU and wall guards and only uses the standard library.

## Exact norm audit completed

Created audit.py and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

Exit 0, wall time 0.24 seconds. Output: 180 exact primal/dual certificates (including dimension three and linear parts outside the span of the kink normals); 72 independent exact distances to convex-hull polygon edges; 3,564 rational score identities; 720 rescaled/split representation checks; six degenerate-zonotope cases; two duplicate-normal cases correctly rejected; twelve exact gradient jumps; four exact sample interpolations; thirty monotonicity checks. Formula evaluation, sum of gradient-jump norms, and the cost of a separate baseline-absorbing representation independently agree. Narrow intrinsic norm=386.3134673380746, wide intrinsic norm=49.22147835683593. Exact rational bounds remain 144>81, with certified shrinking-width threshold 2/9. Actual niceness=20, max RSS=16,465,920 bytes. Same priority-wrapper warning as before, with the inherited-priority guard passing. Results are in audit_results.json. Both scripts finished within one second and use only the standard library.

## Adversarial review

The broad possible failure was a cheaper representation using new hyperplanes or cancellation. The proof groups every possible representation and forces the even coefficient by a local gradient jump; extra groups have zero even coefficient and can supply only linear terms at cost at least twice their Euclidean norm. Clipping the listed groups' odd coefficients proves the lower bound even in this case. The upper bound is attained with finite width, not just approached.

The naive formula “correction cost plus twice baseline norm” fails: x_1+|x_1|=2 rho(x_1) has norm 2, not 4. The zonotope distance repairs precisely this issue. Opposite or repeated normals must be merged before applying the formula: |x_1|-|x_1| has zero norm; the unmerged sum would be wrong. Audit includes both sign and duplication cases, rank-one and zero-dimensional sets, zero distance, and nonzero perpendicular residuals. These were rejected overgeneralizations, not failures of the final statement. No mathematical assertion or program run failed.

The explicit comparison is also derived with coarse exact integers, independently of all square roots: S_A=9/2 and h=1/8 give 4 S_A/h=144; the wide upper bound is 8+70+3=81. The numerical exact norms are optional stronger evaluations. The fixed-sample comparison does not control the random nearest-gap dependence of the wide competitor as n grows. It therefore does not exclude the prescribed n^(-3) rule with high probability for all n, and says nothing about global-minimum-norm risk. KKT points and GD trajectories are not excluded.

## Refinement of the same objective comparison, before writing it

The correction-cost monotonicity supplies a local feasible parameter path: slightly widen one nonzero cone while keeping every fitted score fixed. Balance each displayed neuron by positive rescaling, so its half-squared parameter norm equals its path cost. The derivative of C along this path is strictly negative. At a center neuron's zero preactivation, the weight derivative is parallel to its current weight, hence its inner product with that training input is zero. Thus every allowable ReLU subgradient has the same zero constraint derivative on the path. Check and add the resulting exclusion of generalized margin KKT stationarity for this particular balanced displayed realization. This refines the chosen norm-objective piece, not a new trajectory claim. Alternative parameterizations of the same score are not covered by that local argument.

## Local descent refinement proved and audited

Added Proposition 4 to PROOF.md. It gives a strictly feasible norm-descent direction for the displayed balanced realization whenever some residual is nonzero, and excludes generalized KKT stationarity by taking the stationarity equation's inner product with that direction. The kink at each center does not obstruct the argument: its preactivation stays zero along the path and every allowed ReLU derivative has zero product with the weight tangent. Unbalanced positive neuron rescalings instead have a rescaling direction with nonzero objective derivative and zero score derivatives. Thus those realizations are also excluded. This sharpens the earlier log's global-only conclusion; alternative realizations and GD trajectories remain unresolved.

Extended audit.py and reran exactly the command above. Exit 0, wall time 0.26 seconds. All prior counts passed unchanged. New counts: balanced_feasible_descent_cases=10; exact_tangent_subgradient_checks=78; exact_widened_interpolations=26. Tangent constraint derivatives are exactly rational zero, including every affected neuron's zero preactivation separately. The negative balanced-objective derivative agrees with differentiating the norm formula independently. Final niceness=20; max RSS=16,941,056 bytes. audit_results.json now contains this final run. No failed run.

## Handoff complete

Saved REPORT.md with the required PARTIAL verdict, exact formula, strict finite-sample comparison, local KKT refinement, commands, failed overgeneralizations, and remaining scope. The next target is stationarity across alternative parameterizations of the same score. All authored files and generated outputs remain in this folder; both earlier folders stayed read-only. No git, subagents, external messages, accounts, or shared-state writes were used. The main GD/ReLU benign-overfitting problem remains unresolved by this work.
