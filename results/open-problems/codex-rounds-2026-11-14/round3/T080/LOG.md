# T080 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received: 2026-11-15; exact receipt time was not supplied. First retained local clock reading: 2026-11-15 01:19:29 +04 (Asia/Tbilisi).

## 1. Scope and orientation

Read the earlier REPORT.md, LOG.md, PROOF.md, and the complete verify.py in ~/codex_op_1114/briefs/T080. Read the startup memory index, brain navigation index, and compute governor state. Governor reports warn / owner_away_open, with CPU saturation. Only short, single-threaded checks are planned.

The task specifically forbids writing outside this folder, so no mesh, checklist, recall logger, or brain writer that mutates external shared state is invoked. No git, subagents, or external publication. Earlier files are read only. New programs use OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1, VECLIB_MAXIMUM_THREADS=1 and nice -n 15. The wrapper currently reports `nice: setpriority: Operation not permitted`; the actual inherited priority will be checked inside the audit before computation.

## 2. Bounded literature check

Completed within the first five minutes. Searches: `"hard sphere" "phase transition" proof 2026 Euclidean freezing`; `"hard disks" crystallization proof 2026`; `"hard sphere" freezing rigorous proof November 2026`.

Opened and read:

* Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, arXiv:2607.23873v1, https://arxiv.org/html/2607.23873v1 . The introduction explicitly leaves finiteness of the Euclidean uniqueness threshold open in every dimension. The proved transition is hyperbolic.
* Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, arXiv:2606.28009, https://arxiv.org/abs/2606.28009 . The abstract proves improved uniqueness bounds, not high-activity ordering.
* Biman Bagchi, *From Freezing to Terminal Packing: A Puzzle and a Paradox*, arXiv:2608.29676, https://arxiv.org/abs/2608.29676 . The abstract concerns a density-functional bifurcation framework and a metastable continuation, not an infinite-volume hard-sphere Gibbs ordering theorem.

No later solution was found in this bounded check. This is not an exhaustive literature claim; no SOLVED_ELSEWHERE.md is warranted. References above are only to pages actually opened.

## 3. Independent re-check of the earlier result

The main claim holds. Here is a derivation using a tagged nucleus rather than conditioning on the nearest radius. At the origin, at most one nucleus y can satisfy `|z|-|y|>1` for every other nucleus z. The Poisson summation identity therefore gives

    P(origin retained) = lambda integral_R^d exp[-lambda v_d (|y|+1)^d] dy
                      = lambda d v_d integral_0^infinity r^(d-1) exp[-lambda v_d(r+1)^d] dr.

Scaling r by t=(lambda v_d)^(1/d) gives exactly the earlier q_d(t). Independent uniform phases multiply this retained volume fraction by rho_P. The summation identity follows directly by distinguishing one Poisson point in a bounded window and then taking increasing windows; the remaining process is Poisson. No contribution from ties occurs, since their probability at a fixed location is zero.

A second distributional derivation: condition on the second radial arrival S=R_2 in units with lambda v_d=1. Its density is d s^(2d-1) exp(-s^d). Conditional on S=s, the first radial volume is uniform on [0,s^d]. Therefore

    q_d(t) = d integral_t^infinity (s-t)^d s^(d-1) exp(-s^d) ds.

Integrating by parts, using d exp(-s^d)/ds = -d s^(d-1) exp(-s^d), recovers d integral_t^infinity (s-t)^(d-1) exp(-s^d) ds. The boundary terms vanish both at t and at infinity. This gives an independent formula for the numerical re-check.

The remaining geometric assertions survive audit: the distance difference is two-Lipschitz, so opposite gaps greater than one imply separation greater than one. Two nuclei in B(c,s) determine both nearest distances throughout B(c,a) from input in B(c,s+2a). The failure probability is (1+m)e^-m. Two disjoint truncations give covariance at most 8(1+m)e^-m for unit-bounded observables, with m=lambda v_d(R/4)^d and R>8a. The first derivative of q at zero is -(d-1)Gamma(1-1/d), from differentiating the second integral. Periodization with side L+1 leaves cross-copy separation greater than one. Exact contacts are null under every finite-activity DLR kernel. No correction to the earlier report is needed.

## 4. Choice of the extension, before its proof

Prove a finite-volume DLR estimate for an entirely vacant rectangular seam. Compare its zero-particle partition weight to the full conditional partition function, uniformly over admissible exterior configurations. Integrate continuum displacement variables by using independent insertion balls inside the seam. For the opposite inequality, bound the maximum number of seam centers geometrically, then use the truncated exponential partition sum. For seams of fixed width and growing area, the negative log empty-seam probability should lie between explicit positive multiples of area times log activity, at sufficiently large activity.

Why this piece: it is a checkable restricted case of the earlier report's requested interface partition-function estimate and uses the Gibbs specification essentially. It addresses a literal vacant guard region, not a general orientation defect. It does not justify removing arbitrary grain boundaries or prove freezing. The restrictions and the high-activity dependence will be explicit.

The seam must be thick enough for insertion balls protected from arbitrary exterior points. The general insertion lemma will also allow balls centered on a slightly dilated periodic packing, in any chosen orientation, using uniform phase to count available centers. A thin-strip blocking boundary will be checked explicitly rather than extending the estimate to all widths.

## 5. Proof written and first audit

Created PROOF.md. Main bound: m log(1+z b) <= -log P(S empty) <= log sum_{n=0}^M (z|S|)^n/n! <= U(z|S|,M). Here b=v_d a^d, h=1+2a, m is an explicit protected-ball grid count, M is the volume packing cap, and U is obtained by optimizing an exponential tilt. The proof checks the n! cancellation when continuum insertion positions are integrated. Conditioning on the rest of any larger sampling region gives a bound independent of that region. A periodic-packing variant provides protected slots in any selected orientation, with count at least floor[rho_P h^(-d) |S eroded by (1+a)|].

For fixed W>=2(1+a) and area A=L^(d-1), m/A tends to k(W,a)/h^(d-1)>0 and M/A tends to (W+1)/c_d. Both bounding functions grow proportionally to log z at high activity. An optional cap from periodization replaces the latter coefficient by rho_*(W+1).

Attempt to remove the width restriction fails: in d=2 an exterior unit-spaced row on y=0 blocks every point in a strip of width W<sqrt(3)/2, since the nearest row point is at distance squared at most 1/4+W^2<1. Then Z=1 and the empty probability is one. This counterexample is included in the proof. It concerns uniform boundary estimates, not the probability of this exact exterior under a Gibbs measure.

Next: run a new standard-library audit. It will not import or execute the earlier script, since that script writes beside its own source in the earlier folder. Compare the original density integral with the second-arrival integral from Section 3 of this log, verify exact rational grid thresholds and factorial cancellation, evaluate truncated-exponential bounds by a separate log-sum computation, and check the blocking example.

## 6. First audit run: resource-limit setup failed

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
```

Exit code 1, before any mathematical computation. This Mac rejected setting RLIMIT_AS to 768 MiB with `ValueError: current limit exceeds maximum limit`. The usual nice wrapper warning also appeared. Inspect the inherited limits and use the applicable memory limit without trying to raise a pre-existing hard limit. This is a harness/resource-setting failure, not a failed estimate.

Read-only inspection: inherited AS, RSS, and DATA limits are all `(9223372036854775807, 9223372036854775807)`; actual nice priority is 20; a minimal interpreter's peak RSS is 11,485,184 bytes. A second run preserving the inherited hard limits also failed before computation: both AS and DATA soft-limit changes were rejected with the same ValueError. Removed those unsupported limit changes. The calculation uses fixed small lists (the largest partition-sum list has 1,156 entries), reports peak RSS, rejects a measured peak above 768 MiB, and retains its working 60-second CPU limit. No memory-intensive libraries or allocations are used. A measured peak check is not claimed as an enforced address-space cap.

## 7. Successful independent audit (01:25 +04)

Repeated the command in Section 6 after removing the unsupported memory-limit changes. Exit code 0. Complete output:

```text
nice: setpriority: Operation not permitted
Standard-library independent audit; floating-point checks support the proof.
nice_priority=20; thread_environment=1; memory_check=peak RSS <768 MiB; cpu_limit_seconds=60
Earlier density formula: original integral vs conditional second-arrival integral
density_pairs=24; maximum_absolute_error=3.33e-16
d=2: loss_constant=1.77245385091; two_integral_errors=4.44e-16,4.44e-16
d=3: loss_constant=2.70823587885; two_integral_errors=8.88e-16,8.88e-16
d=4: loss_constant=3.6762501074; two_integral_errors=4.44e-16,4.44e-16
d=8: loss_constant=7.62756650196; two_integral_errors=8.88e-16,0
exact_grid_threshold_checks=81; rational_margin_and_pair_distance_checks=PASS
exact_n_factorial_cancellation=PASS; missing_factorial_negative_control=detected
truncated_exponential_and_tilt_cases=48; all_bounds=PASS
Seam example: a=1/4, W=4, L=10; lower <= exact truncated-sum upper <= tilt upper
d=2, z=1, m=12, M=70: 2.15129845 <= 39.9999939 <= 40
d=2, z=100, m=12, M=70: 36.3238373 <= 350.162082 <= 353.188808
d=2, z=1e+06, m=12, M=70: 146.251882 <= 994.868259 <= 997.912634
d=3, z=1, m=72, M=1155: 4.56459131 <= 400 <= 400
d=3, z=100, m=72, M=1155: 145.503581 <= 5244.80423 <= 5249.21987
d=3, z=1e+06, m=72, M=1155: 798.411939 <= 15882.7181 <= 15887.163
surface d=2: alpha=1.33333333333, m/A=1.3332; kappa=6.36619772368, M/A=6.3668
surface d=3: alpha=0.888888888889, m/A=0.88871112; kappa=9.54929658551, M/A=9.55120654
thin_strip W=4/5: maximum_distance_squared_bound=89/100<1, so Z=1
wider_strip W=9/10: (x,y)=(1/2,89/100) is allowed by that exterior row
PASS; elapsed_seconds=0.030; peak_rss_mib=15.188
Wrote density_audit.csv, seam_bounds.csv, verification.json
```

The density audit uses a newly implemented 24-point composite Gauss–Legendre quadrature, not the earlier adaptive Simpson routine or its incomplete-gamma implementation. Its nodes and weights pass 41 polynomial moment checks. It compares two integral representations with different integrands in dimensions 2, 3, 4, and 8 and also checks erfc in dimension two. The largest density discrepancy is 3.3306690738754696e-16. The integrals stop at eight: the first tail is at most exp(-8^d), and for the second tail it is at most (8^d+1)exp(-8^d), by replacing (s-t)^d with s^d and substituting s^d. Thus tails are negligible on the numerical error scale. These checks use floating point, not certified interval arithmetic.

The new lemma's thresholds, guard margins, pair separations, and factorial identity have exact Fraction checks. The wrong expression that omits 1/n! is a negative control and is detected. Forty-eight truncated exponential sums are independently evaluated by log-sum-exp and bounded by the optimized tilt. The constants in the seam example are independently hand-checked below. CSV files preserve all 24 density comparisons and six seam-bound examples; verification.json records resource use and results.

## 8. Attempts to break the result and second derivations

1. **Factorial and independence.** In n distinct insertion balls, labeled positions have n! assignments. This exactly cancels the Gibbs 1/n!, giving a product over optional occupied balls. A second derivation assigns each ball independent occupancy with weights 1 and z b_j, then maps that product measure to unordered configurations. Balls are disjoint, so the occupied subset and its positions are uniquely recoverable. Its total unnormalized Gibbs weight is exactly product_j(1+z b_j). No displacement is frozen, and an individual exact packing receives zero weight as it should.
2. **Width-one versus radius-one.** Exterior centers can lie on the region boundary. A radius-a insertion ball needs its center at least 1+a from that boundary. Taking only 1/2+a would fail. The lower count explicitly removes 1+a from each face. Between insertion centers, the required spacing is 1+2a. This is independently checked from the distance between two open balls, as well as by squared rational grid distances.
3. **Upper cap.** Each inside center has a disjoint radius-1/2 ball. All those balls lie in the coordinate-expanded box with side lengths L_i+1; its volume yields M. Independently, repeating the inside configuration with coordinate periods L_i+1 proves n<=rho_* product_i(L_i+1), giving the optional sharper cap. These are upper bounds on the maximum particle number, not equality claims.
4. **Upper tilt, second route.** If N is Poisson with mean T, E_M(T)=exp(T)P(N<=M). For T>M, the exponential Markov bound with theta=log(T/M)>0 gives log P(N<=M)<=theta M+T(exp(-theta)-1). Adding T yields M[1+log(T/M)]. For T<=M, the bound E_M(T)<=exp(T) applies. This independently reproduces U with the same sign and constants.
5. **Numbers in the seam example.** With a=1/4, h=3/2, W=4, L=10, the long-direction count is 1+floor[(10-5/2)/(3/2)]=6 and the width count is 1+floor[(4-5/2)/(3/2)]=2. Hence m=12 in d=2 and 72 in d=3. In d=2, c_2=pi/4, so M=floor(55/(pi/4))=70. In d=3, c_3=pi/6, so M=floor(605/(pi/6))=1155. The ball volumes are pi/16 and pi/48 respectively. Substituting these exact expressions gives the displayed lower costs. The limiting coefficients are alpha=2/(3/2)^(d-1) and kappa=(W+1)/c_d, reproducing the numerical values by a separate expression.
6. **Surface limit and quantifiers.** Only bounding functions have limits. No surface-tension limit is proved. The lower and upper area coefficients are independent of the exterior; averaging conditional probabilities preserves both inequalities. At fixed admissible width, log(1+zb)/log z tends to one and U(zWA,M)/[A log z] has leading upper coefficient kappa after the large-area limit. This is an area-times-log-z estimate, not an area-times-z estimate. Constants are not claimed sharp.
7. **Periodic slots.** Dilation by h changes density by h^(-d), and only erosion by 1+a protects the full insertion ball from the exterior. Uniform phase supplies a phase with enough sites, not an assertion that every phase has that many. The square-grid count and periodic count are alternative families and cannot be added. Rotating the candidate sites preserves their separation and their mean count, but does not rotate or assume order in the boundary configuration.
8. **Thin seams.** For W=4/5 the squared-distance bound is exactly 89/100, so every inside point is blocked. For W=9/10 the point (1/2,89/100) is allowed by that row, since 1/4+(89/100)^2>1. This checks the direction and scale of the obstruction. It invalidates a width-uniform positive bound, not the proved thick-seam bound.
9. **Actual orientation interfaces.** A seam of zero or small free width, strain, dislocations, and changes of displacement volume outside a chosen strip are not covered. An arbitrary boundary between two crystal orientations need not contain the vacant box of the theorem. The earlier random construction therefore cannot simply be assigned the cost (6) at each of its grain faces.

The result is a restricted Gibbs lemma with explicit constants, not a solution of freezing. Its novelty relative to general Gibbs insertion estimates has not been established.

## 9. Final artifact audit

Ran a separate read-only Python check under the same single-thread environment and nice -n 15. It verifies the eight deliverables are nonempty, the REPORT.md verdict matches exactly, the complete successful VERIFY_OUTPUT.txt is present in this log, both CSV tables match verification.json, all six saved bound comparisons have the right ordering, resource records meet the task limits, and the proof/report retain the thin-seam restriction and unresolved freezing gap. Output:

```text
nice: setpriority: Operation not permitted
PASS: eight deliverables present; verdict, output log, CSV rows, analytic scope, and resource record consistent.
No SOLVED_ELSEWHERE.md: no Euclidean solution found in bounded literature check.
```

Only this folder was written. The earlier folder was read but neither its script nor any of its files was executed in a way that could write there. No git, subagents, external messages, accounts, or background processes were used. Completed the requested one-piece extension; T080 remains open.
