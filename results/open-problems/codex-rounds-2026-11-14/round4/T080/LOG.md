# T080 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Date: 2026-11-15. Exact receipt time unavailable. First retained clock reading: 04:41:23 Asia/Tbilisi (00:41:23 UTC).

## 1. Scope and reading

Read REPORT.md, LOG.md, PROOF.md, and every Python script in both earlier folders, ~/codex_op_1114/briefs/T080 and ~/codex_op_1114r3/briefs/T080. Both have one Python script, verify.py. Those folders remain read only. Read the startup memory index and compute governor state. The governor reported warn / owner_away_open, CPU saturation, and about 52 percent free memory. No heavy computation is needed.

The task's specific instruction forbids writes outside this folder. Thus no external mesh, checklist, recall logger, or brain writer is invoked. No git, subagents, background workers, or external publication. New computations use OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1, VECLIB_MAXIMUM_THREADS=1 and nice -n 15. The inherited nice setting is already low priority; the wrapper warns that it cannot adjust it further. Scripts check the actual setting.

## 2. Literature check, 00:41–00:42 UTC

Web searches: `"hard sphere" "phase transition" rigorous 2026 Euclidean`; `"hard disks" crystallization proof 2026`; `hard sphere crystallization rigorous proof September October November 2026 Euclidean Gibbs`.

Opened the following primary sources:

* Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, arXiv:2607.23873, https://arxiv.org/abs/2607.23873 and https://arxiv.org/html/2607.23873v1 . Its theorem is hyperbolic, and its abstract and introduction leave Euclidean freezing open.
* Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, arXiv:2606.28009, https://arxiv.org/abs/2606.28009 . It improves uniqueness bounds; it does not prove high-activity ordering.

No later Euclidean solution was found in this bounded search, completed within five minutes. This is a search outcome rather than an exhaustive exclusion. No SOLVED_ELSEWHERE.md is warranted.

## 3. Independent analytic re-check

The round-3 main claim holds. Let b_j be the volumes of disjoint, mutually compatible insertion regions protected from the exterior. Instead of labeled integration, start with an unordered configuration: choose an occupied subset J and independently choose one position in each selected region. The subset and all positions are recoverable uniquely. Its Gibbs weight integrates to product_(j in J)(z b_j), because the n! labelings of each unordered n-particle configuration cancel the specification's 1/n!. Summing J gives Z >= product_j(1+z b_j). Thus P(empty)=1/Z has the asserted upper bound, with no fixed-position atoms.

For the other direction, disjoint radius-1/2 balls around n centers in a rectangle fit in its coordinate expansion with side lengths L_i+1. Hence n <= floor[product_i(L_i+1)/(v_d/2^d)] = M. Each n-sector position integral is at most |S|^n, so Z <= E_M(z|S|). Independently, E_M(T)=exp(T) P(Poisson(T)<=M); applying exponential Markov to exp(-theta N), theta=log(T/M)>0 for T>M, gives log E_M(T)<=M[1+log(T/M)]. For T<=M, E_M(T)<=exp(T). These reproduce the previous cap and tilt with the correct direction.

The protected center margin is 1+a, and the center separation is 1+2a; subtracting the insertion radius once and twice respectively gives exclusion distance one. The round-3 constants for a=1/4, W=4, L=10 are m=12, M=70 in d=2 and m=72, M=1155 in d=3. The thin-row obstruction is also correct: 1/4+(4/5)^2=89/100<1. Conditioning and averaging extend the bounds to arbitrary surrounding volumes and DLR measures.

The first report's density formula also survives analytic re-check: the probability of a tagged nearest Poisson nucleus at radius r and no other nucleus before r+1 integrates to lambda d v_d integral r^(d-1) exp[-lambda v_d(r+1)^d] dr. Scaling gives q_d(t). The two-Lipschitz separation argument and the two-arrival local determination argument have the stated factors. The numerical re-check below will rerun the full round-3 audit from a local copy, never from the earlier folder.

## 4. Choice of one extension, before its proof

Extend the vacant-seam estimate to a uniform exponential bound for connected collections of boxes that contain a small but positive number of particles. For a union of n boxes, use m_0 protected insertion regions per box in the partition-function denominator and integrate all configurations with at most r n particles in the numerator. An exponential tilt bounds the latter without a volume-dependent prefactor. Then count connected sets of boxes by a deterministic tree traversal. The intended conclusion is an explicit high-activity bound on the size of connected regions of underoccupied boxes, valid for every hard-sphere Gibbs measure and every exterior.

Why this piece: it removes the previous lemma's exact-vacancy assumption for a class of particle-containing defects and includes the entropy of choosing the defect's shape. It is a restricted continuation of the interface program. A general orientation interface need not be underoccupied at this threshold; that missing geometric implication will remain explicit. No novelty claim or freezing claim is intended.

First use arbitrary box length ell, insertion radius a, and 0<r<m_0. Give a fully explicit example ell=4, a=1/4, r=m_0/2 in d=2,3. If the argument supports it, state the same criterion using arbitrary protected insertion families; it should not require a prescribed crystalline orientation outside the boxes.

## 5. Reproduction of the previous computation

Copied the round-3 verify.py unchanged to prior_recheck/verify.py in this folder. Commands, all under `env OMP_NUM_THREADS=1 nice -n 15` for the directory/copy/read operations:

```sh
mkdir -p prior_recheck
cp ~/codex_op_1114r3/briefs/T080/verify.py prior_recheck/verify.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 prior_recheck/verify.py > prior_recheck/VERIFY_OUTPUT.txt 2>&1
```

Exit code 0. Complete captured output:

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
PASS; elapsed_seconds=0.030; peak_rss_mib=15.625
Wrote density_audit.csv, seam_bounds.csv, verification.json
```

The copied script writes beside its source, so all reproduced outputs are in prior_recheck/. The independent analytic derivation in Section 3 supplies the re-check by a second route. The previous result holds.

## 6. Proof and audit plan

Wrote PROOF.md. For n boxes, each with m_0 protected radius-a balls of volume b, and box volume v, the probability of at most rn centers is bounded by exp(-n tau), where tau=m_0 log(1+zb)-H_r(zv). The function H_r is the optimized Poisson lower-tail exponent. This includes all positive-particle sectors up to floor(rn). It recovers vacancy at r=0 and grows as (m_0-r) log z for r<m_0.

At most (2d)^(2(n-1)) connected n-box sets contain a fixed box: a canonical spanning-tree traversal encodes each by 2(n-1) signed coordinate steps. The event that an underoccupied component has at least n boxes supplies such an n-subset. A union bound proves P(component size>=n) <= q^n/(2d)^2, with q=(2d)^2 exp(-tau). This includes shape entropy and requires no independence or monotonicity of Gibbs occupations.

Explicit candidates: ell=4, a=1/4, m_0=2^d and r=m_0/2. The rational sufficient bounds should be q<=4/9 for d=2, z>=4096; q<=729/16384 for d=3, z>=65536. These follow from pi>3 and e<3 and will be checked independently with exact Fraction arithmetic. A periodic-slot corollary permits any fixed number-density threshold rho<rho_* after choosing sufficiently large boxes and then sufficiently large activity; the boxes and activity bound are not uniform near rho_*.

New verify.py will check the integrated low-count ratio on all 512 graphs with five weighted sites and two prescribed mutually compatible sites; compare finite exponential sums with two derivations of the tilt; enumerate anchored connected sets by growth and independently by closed walks; check tree-word injection; and audit all displayed scalar constants by both direct logarithms and exact rational bounds. These are algebraic and finite combinatorial checks, not a numerical proof of freezing.

## 7. New computation, 00:49 UTC

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
```

Exit code 0 on its first run. Complete captured output:

```text
nice: setpriority: Operation not permitted
Finite audits of integrated low-occupation and connected-set bounds.
nice_priority=20; thread_environment=1; CPU_limit_seconds=60
periodic_slots d=2: ell=100, rho=1/4, m_0=4225, r=2500, limiting_slot_density=4/9
periodic_slots d=3: ell=100, rho=1/4, m_0=274625, r=250000, limiting_slot_density=8/27
tilt_cases=150; all_finite_sums_below_exponent=PASS; independent_Poisson_derivation=PASS
weighted_graphs=512; exact_low_count_ratio_cases=3072; negative_controls=PASS
animals d=2: counts=[1, 4, 18, 76, 315]; independent_closed_walk_match=PASS
animals d=3: counts=[1, 6, 45, 344]; independent_closed_walk_match=PASS
d=2, z=4096: tau=3.97018440697, tau_lower=3.96521390452, q=0.301919249014
d=2, z=10000: tau=5.75239897971, tau_lower=5.75036231503, q=0.0508024723399
d=2, z=1000000: tau=14.9607230588, tau_lower=14.960702687, q=5.09050083408e-06
exact sufficient threshold d=2: z>=4096, exp(-tau)<=1/36, q<=4/9
d=3, z=10000: tau=-0.0485486301527, tau_lower=-0.0607624015223, q=37.7908711167
d=3, z=65536: tau=7.46116054602, tau_lower=7.45929566641, q=0.0206995854069
d=3, z=1000000: tau=18.3600405725, tau_lower=18.3599183424, q=3.82505947785e-07
exact sufficient threshold d=3: z>=65536, exp(-tau)<=81/65536, q<=729/16384
PASS; elapsed_seconds=0.271; peak_rss_mib=16.219
Wrote animal_counts.csv, contour_bounds.csv, verification.json
```

All 3,072 weighted-graph comparisons and the two stated rational threshold bounds use exact integer/Fraction arithmetic. The graph audit checks the partition-function algebra with arbitrary interactions among five sites; it does not claim arbitrary graphs can be realized geometrically by spheres. Connected-set counts are exact enumerations: growth gives 315 anchored five-cell sets in d=2 and 344 anchored four-cell sets in d=3, and independent exhaustive closed-walk enumeration gives exactly the same sets. The tree-word encoding is injective on every enumerated family.

The 150 truncated-exponential comparisons use floating point with tolerance 2e-10. The largest positive rounding excess over the analytic bound was 8.526512829121202e-14. These are supporting checks, not interval certificates. The proof of the tilt is analytic and also derived independently through Poisson exponential Markov. The six floating-point scalar examples agree with the independent logarithmic expression, with exact difference m_0 log(1+1/(zb)). Tables and full-precision resource records are saved in the CSV and JSON files.

No new computation failed. The d=3, z=10000 example deliberately shows failure of the sufficient criterion: tau<0 and q>1, so the probability bound is only the trivial bound one. It is not evidence for a transition or for a large underoccupied component at that activity.

## 8. Attempts to break the result

* The component bound must exclude arbitrary exterior boxes in a finite-volume law. If exterior boxes were included, an empty fixed exterior could itself create an infinite underoccupied component. Clarified PROOF.md: the full-lattice component assertion concerns infinite-volume Gibbs measures, while finite-volume components use the induced graph of boxes wholly inside the sampling region. Every candidate set in the latter graph satisfies the hypotheses of the finite-volume conditional bound.
* A positive-particle event cannot be charged the empty-event cost. For two independent slots, P(N<=1)=(1+2zb)/(1+zb)^2 exceeds P(N=0)=1/(1+zb)^2. The audit explicitly detects this incorrect shortcut. The numerator E_floor(rn) is necessary.
* The strict gap r<m_0 is necessary for the displayed log-z gain. In the same independent-slot model N<=m_0 holds with probability one. At r>=m_0 no positive log-z penalty follows merely from m_0 slots.
* Factorials and displacement volumes were checked again on the weighted graphs: every sector is a sum over unordered occupied subsets. Its labeled-coordinate representation has exactly s! copies, canceling 1/s!. Removing all particles outside the selected insertion balls is a restriction of the denominator, not a conditional claim that existing particles already occupy those balls.
* For a union of boxes, insertion slots must remain mutually compatible across box faces. Each open ball is protected from its own full box complement by distance greater than one, so every point in every other box is compatible. Direct rational checks give center spacing 3/2 within a box and minimum center spacing 5/2 across adjacent boxes in the explicit example.
* Shape entropy is counted once, with an anchor. The tree traversal has exactly 2(n-1) steps and reconstructs the entire visited set. No translation factor or factorial is missing. A component of size at least n supplies a connected subset of exactly n containing its root; no extra sum over larger sizes is required. Independence of neighboring occupations is not available and is not used.
* Re-derived the constants directly from tau: in d=2 the logarithmic lower bound is 2 log[z pi^2/(2048e)], and in d=3 it is 4 log[z pi^2/(36864e)]. With pi>3 and e<3, z=4096 gives e^-tau<=1/36; z=65536 gives e^-tau<=(3/16)^4=81/65536. Multiplying by 16 and 36 gives 4/9 and 729/16384 respectively. Exact Fraction calculations independently reproduce each value.
* The periodic-slot corollary needs strict slack twice: choose rho_P/(1+2a)^d>rho, and then ell large enough that the boundary erosion and integer floor still leave m_0>rho ell^d. The order is rho, P, a, ell, then z. No assertion is uniform as rho approaches rho_*. A square/cubic-lattice example with ell=100 gives m_0=4225 and 274625, respectively, exceeding rho ell^d for rho=1/4 without numerical integration.
* Underoccupied components are connected by face adjacency. No conclusion about percolation of their complements, closed separating surfaces, or interfaces follows just from their absence. In particular the theorem does not show that orientation defects cause low occupation at this threshold. That remains the missing step.

The result is an elementary Gibbs estimate with integrated positions and a connected-shape count. Its novelty in the literature has not been established. It does not prove freezing.

## 9. Report and final artifact audit

Wrote REPORT.md with the required PARTIAL verdict, the new probability and component bounds, exact sufficient constants, reproduction commands, the finite-volume correction, limitations, opened references, and the next geometric test.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_artifacts.py > ARTIFACT_AUDIT.txt 2>&1
```

Exit code 0. Complete output:

```text
nice: setpriority: Operation not permitted
PASS: report, full output logs, unchanged previous source copy, two data tables, exact thresholds, resource records, and finite-volume scope agree.
```

The read-only artifact check confirms the prior script copy is byte-for-byte unchanged, both mathematical audit outputs appear completely in this log, saved CSV rows equal the JSON records, all stated rational constants match, the report retains the open freezing gap, and no SOLVED_ELSEWHERE.md was created. All new files are in this folder, including prior_recheck/. Earlier folders were never written. No git, subagents, external messages, accounts, GPU work, or background processes were used.

Completed the one-piece extension. T080 remains open.
