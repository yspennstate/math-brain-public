# T264 work log

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 05:15 +04.

## Orientation

Read both predecessor folders' REPORT.md, LOG.md, PROOF.md and Python scripts. They remain read-only. Read startup memory/index and compute state (status warn, cpu_saturated, mode owner_away_open; free memory 54%). Computation will be short, sequential, standard-library only, one thread, below 1 GB, under nice -n 15. No git, subagents, or writes outside this folder. The folder-only instruction precludes invoking brain, checklist, or mesh commands that mutate their external stores; this log is the local task record.

## Bounded literature check, begun at 05:15 +04

Used the web search tool for ReLU / minimum norm / tempered overfitting / fixed dimension with 2025 and 2026, and opened the arXiv pages listed below. No complete resolution located so far.

- Ouns El Harzli, Yoonsoo Nam, Ilja Kuzborskij, Bernardo Cuenca Grau, Ard A. Louis, *Sufficient Conditions for Stability of Minimum-Norm Interpolating Deep ReLU Networks*, arXiv:2602.13910, https://arxiv.org/abs/2602.13910 . Sufficient architecture conditions for stability, rather than the fixed-dimensional noisy interpolation risk limit.
- Weizhao Li, Lei Shi, Hanfei Zhou, *Minimum-Norm Interpolation in Weighted Variation Spaces: Direct and Inverse Problems*, arXiv:2611.01105, https://arxiv.org/abs/2611.01105 . Direct and inverse approximation results for noiseless labels from a variation-space target.
- Junhyung Park, Patrick Bloebaum, Shiva Prasad Kasiviswanathan, *A Classical View on Benign Overfitting: The Role of Sample Size*, arXiv:2505.11621, https://arxiv.org/abs/2505.11621 and https://arxiv.org/html/2505.11621v1 . Studies arbitrarily small but nonzero training error; checking the assumptions in the opened full text.
- Guy Kornowski, Gilad Yehudai, Ohad Shamir, *From Tempered to Benign Overfitting in ReLU Neural Networks*, arXiv:2305.15141, https://arxiv.org/abs/2305.15141 . Classification, univariate and growing high dimension. Latest revision on the opened page: 21 March 2024.

## Earlier-result re-check: analytic part

For the round-3 positive-label formula, W dot x1 = W dot e2 = 1, W dot x2 = 1-2b > 0, while v dot x1 = 0, v dot x2 = 2ab, v dot e2 = -a. These recover labels (1,-1,1). For the negative-label formula, the atom-value columns are (1,cos(theta),b), (0,2ab,0), (0,0,a); substitution gives (1,-1,-1). Both costs equal the displayed dual objectives. Rechecked the activation-region dual inequalities in PROOF.md; they are valid for 0<theta<pi/3 and exclude off-plane equality directions. Independently, only the negative v coefficient is unbounded: theta C tends to 2, v tends to -e2, and every other coefficient stays bounded. Hence theta f converges uniformly to -2 sigma(-e2 dot x), giving theta^2 R -> 2/d using E[sigma(X2)^2] = 1/(2d). This confirms the main claim analytically. A fresh computation will follow before beginning the extension.

Literature check ended before 05:20 +04 (under five minutes). The opened full text of Park, Bloebaum and Kasiviswanathan explicitly distinguishes small nonzero training error from exact interpolation (introduction, lines 112–113 in the web rendering). No solution of the specified exact-interpolation limit found; no SOLVED_ELSEWHERE.md warranted. The bounded search is not a proof of absence.

## Proposed single extension

Prove that the same leading risk coefficient survives for third points in an open set, including out-of-plane locations in d>=3, and arbitrary uniformly bounded third labels. Approach: a competitor with cost 2/sin(theta)+O(1), combined with near equality in the close-pair dual bound, may force the scaled atomic mass into the two limiting directions +e2 and -e2. A third point with e2-coordinate bounded away from zero then removes one of these two leading coefficients. This avoids assuming that the earlier exact kink certificates persist under perturbation. Choice will be finalized after the independent numerical re-check.

## Independent numerical re-check completed

Created recheck_earlier.py. Unlike the earlier midpoint quadrature and kernel calculation, it splits the circle at every network activation kink and integrates the resulting (A cos(phi)+B sin(phi))^2 exactly by elementary antiderivatives. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_earlier.py > recheck_output.txt
```

Exit 0. Both labels and five angles (1e-5, .001, .1, .7, 1.047) passed interpolation, independently summed costs/dual values, and exact risk. Maximum relative risk discrepancy: 3.33e-16. At theta=1e-5, theta^2 R2 was 0.999989317008 (+ label) and 0.999996816919 (- label), consistent with 2/d = 1. Runtime 0.000252 seconds, RSS 13,434,880 bytes, inherited nice 20. nice reported permission denied trying to adjust priority, but the actual-priority assertion passed. The earlier main claim holds.

## Choice finalized before extension

Prove uniform convergence of theta f to -2 sigma(-e2 dot x) for z dot e2 >= delta > 0, and the reflected limit for z dot e2 <= -delta, uniformly over bounded third labels and over all minimum-Q interpolants. This is the proposed open-set extension, with the natural random-triple infinite-moment corollary if the proof succeeds. No exact optimizer formula is sought.

Key candidate competitor for q = z dot e2 >= delta: v=(b,-a),

    f0(x) = sigma(e1 dot x)/a - sigma(v dot x)/(ab)
            + r sigma(-v dot x),
    r = (tau - sigma(z dot e1)/a)/(a q - b (z dot e1)).

The correction vanishes at both close-pair samples. If theta <= delta/2, its denominator is >= delta/2, and cost <= 2/sin(theta)+K with K=2+2(H+2)/delta for |tau|<=H. This uniformly bounds the excess cost above the sharp pair dual optimum. Next: prove the mass-localization inequality, derive a uniform error bound, and try to falsify it with wrong-sign/off-plane atoms and explicit near-optimal networks.

## Proof written; first verification run

Wrote PROOF.md. The main inequality is ||u-t e2||^2 <= 4(1-a t g_theta(u)), where t is an atomic coefficient sign and g_theta is the normalized pair response difference. Pair interpolation sums the right side to 4(M-theta/b), where M is theta times total atomic mass. The competitor bounds M by 2theta/s+Ktheta, yielding a uniform O(sqrt(theta)) approximation by A sigma(e2 dot x)-B sigma(-e2 dot x), with A+B -> 2. The third observation forces A -> 0 on the positive cap. Reflection handles the negative cap. This proves the risk coefficient 2/d uniformly, and consequently infinite random-triple risk moments of orders r >= (d-1)/2.

Created verify_robust.py. First run of the command below exited before any mathematical checks because macOS rejected setting RLIMIT_AS to 900,000,000 (`ValueError: current limit exceeds maximum limit`). Investigating the existing limits and replacing the unsupported setting with a supported heap limit; the program uses only scalar standard-library operations and bounded small lists.

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_robust.py > verification_output.txt
```

The data-heap rlimit was rejected with the same exception, including an independent soft-limit-only probe. Both memory-limit attempts failed before the verifier's computation. Removed those unsupported calls; the final script has bounded small lists, a CPU limit, a wall alarm, and a peak-RSS assertion. No limit increase or special permissions were requested. The mathematical assertions and constants were unchanged. The next run of the same command exited 0; full output is in verification_output.txt.

## Verification output and independent audits

```text
PASS: localization inequality, 18102 signed directions; max violation 0
PASS: 162 feasible perturbed networks in d=2,3,7, both caps, labels -2.5,0,2.5
Maximum interpolation error 4.44e-16; sampled error/proved bound 0.0519
d=2 theta=5e-06: theta^2 R=0.999998407806, limit=1
d=3 theta=5e-06: theta^2 R=0.666665605417, limit=0.666666666667
d=7 theta=5e-06: theta^2 R=0.285713817797, limit=0.285714285714
PASS: out-of-plane S^2 integration scaled risk=0.662466247785, kernel=0.662453416353
PASS: dropping fixed delta fails: theta^2 R2=0.500000000417, expected 1/2, not 1
d=2: alpha=0.5, tail liminf lower bound=0.159154943092
d=3: alpha=1, tail liminf lower bound=0.0833333333333
d=4: alpha=1.5, tail liminf lower bound=0.0375131798399
d=5: alpha=2, tail liminf lower bound=0.015
d=6: alpha=2.5, tail liminf lower bound=0.00544522365849
d=7: alpha=3, tail liminf lower bound=0.0018221574344
PASS: angular normalizers, lower-tail constants, endpoint exponent
All assertions passed.
Resources: {'seconds': 0.2874981249915436, 'peak_rss_bytes': 16285696, 'nice': 20, 'threads': 1}
```

The 162 networks are explicit competitors with a random ridge plus three compensating atoms that preserve all interpolation constraints; they are not numerical minimizers. Their costs satisfy the theorem's cost hypothesis. This checks the broader cost-bounded statement, including off-plane weights, both cap signs, and bounded non-Rademacher labels. No optimizer or discretized dictionary supplies a proof step.

Load-bearing coefficient 2/d was recovered from the hemisphere limit and separately from its orthogonal odd/even parts, each contributing 1/d. The direct S^2 surface integral independently checks the spherical kernel normalization on a network with a genuinely out-of-plane atom. Angular normalizers were checked by a sine-integral recurrence independently of the gamma expression. Tail constants simplify separately to 1/(2*pi), 1/12, and 3/200 for d=2,3,5. The moment endpoint was checked both from the angle integral and from integration of the lower tail; equality gives logarithmic divergence.

Added a genuine counterexample to dropping the fixed-delta hypothesis: z_theta=(-cos(3theta/2),sin(3theta/2)), tau=+1, and the old two-point minimum. Its third response is exactly 1 since u dot z=sin(theta), v dot z=-sin(2theta)<0. The pair dual still certifies minimum cost 2/sin(theta), so this is an exact three-point minimum with theta^2 R -> 1/d, while z_theta dot e2 -> 0. The third point approaches the antipode of the pair midpoint, not the pair itself. Every step is in Section 7 of PROOF.md; the independent verifier confirms it numerically. Thus no unproved robustness at the equator has entered the theorem.

Checked existence for random triples: pairwise nonparallel inputs have atomic response vectors spanning R^3, by the independent derivative jumps across their distinct activation hyperplanes. Three units therefore suffice for interpolation, and compactness gives a minimum. This closes a potential gap in the fixed-width random-triple corollary.

## Completion, 05:27 +04

Wrote REPORT.md with the required verdict line, theorem and model restrictions, commands and resources, failed memory-limit attempts, the exact equatorial counterexample, unresolved questions, and the next fourth-point step. Audited the report against equations (4), (17), (19), (22), (23), and (25) of PROOF.md and the saved verification output. The tail factor includes the opposite-label probability 1/2 and both third-point caps; it counts only one designated pair. No upper tail or lower-order moment finiteness is claimed. The fixed n=3 infinite expectation is not described as an n-to-infinity classification. All files written are in this folder; predecessor folders remain unchanged.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 05:15 +04.
