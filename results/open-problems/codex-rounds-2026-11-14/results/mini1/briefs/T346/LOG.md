# T346 work log

Task received: “push this problem forward by one checkable piece.” Session start: 2026-11-14 18:13 UTC (22:13 Asia/Tbilisi).

## 1. Orientation and literature search started

Read PROMPT.md, the startup memory, compute_state.json, and the existing task checklist. The latest task confines all writes to this folder, so the global mesh/checklist/brain commands that write elsewhere are not being run. No subagents, git, or external publication.

Shell commands are prefixed with OMP_NUM_THREADS=1 and nice -n 15. The sandbox prints `nice: setpriority: Operation not permitted` but executes the command. No substantial computation has been launched; the governor reports CPU saturation. Any verification will be tiny and single-threaded.

Initial web queries:

- `randomized smoothing optimal distributions l infinity curse dimensionality non product input dependent 2025 2026`
- `randomized smoothing l p p greater 2 optimal noise distribution lower bound Yang 2020 2024`

Found leads: Yang et al., Randomized Smoothing of All Shapes and Sizes (2020); Wu et al., Completing the Picture (2021); Intriguing Properties of Input-dependent Randomized Smoothing (2021); Rethinking Randomized Smoothing from the Perspective of ... (recent). These are search leads only until opened and checked. Literature-search deadline: 18:23 UTC.

## 2. Literature check and choice (18:17 UTC)

Opened the arXiv pages for 1902.02918, 2002.03517, 2002.08118, 2110.05365, 2312.12608, 2206.01715, and 2512.01782; opened the Blum PDF, Yang PMLR PDF, Wu PMLR PDF, and the ICLR 2026 Dual Randomized Smoothing proceedings page. Search included 2025/2026, November 2026, optimal distributions, full covariance, input dependence, and local/minimax bounds. No located paper settles the problem as worded. The 2026 dual-smoothing work improves adaptive variance selection, not the universal dimension exponent. Its arXiv page lists revision 31 October 2026, before the brief's November 2026 status. The search ended within five minutes, below the ten-minute cap.

Important correction to the caveat: Blum's additive-noise second-moment theorem does not assume product noise. Yang's Theorem 7.3 / Corollary 7.4 even allows a family q_x, subject to their universal useful-smoothing assumptions. Those assumptions are stronger than empirical fixed clean accuracy. Thus neither arbitrary non-product noise nor input dependence is automatically an uncovered escape route.

Failed access: the OpenReview survey PDF redirected to a browser challenge; the newer Lipschitz-standard-deviation PDF returned 404. Neither is used as a technical source. Search-result snippets are not treated as proof.

**Chosen piece, before beginning proof:** Determine the exact minimax *infinitesimal class-probability loss* among Gaussian kernels N(x, Sigma(x)) with an arbitrary C1 positive-definite covariance field, under the local budget tr Sigma(x) <= d sigma^2, for every p>2 including infinity and every nominal class probability a in (0,1). Prove a sharp constant and an attaining kernel. This addresses a precise input-dependent, non-product special case without claiming a finite-radius theorem at fixed dataset accuracy. The idea to check is that two reflected halfspaces and both attack signs prevent a covariance derivative from canceling the mean-shift loss.

Planned independent checks: derive halfspace derivatives from exact univariate Gaussian CDFs and from density scores; derive the covariance bound both by random signs plus eigenvalues and by averaging covariance quadratic forms plus matrix Cauchy-Schwarz. Check a=1/2, p=infinity, correlated noise, and variable covariance explicitly.

## 3. Proof saved

Wrote PROOF.md. The result is the exact local minimax loss constant phi(Phi^{-1}(a)) d^{1/2-1/p}/sigma for C1 full-covariance Gaussian kernels under a local trace budget. The proof uses uniform L1 differentiability of the Gaussian density, reflected halfspaces, and a sign-vector argument. A constant-covariance likelihood-ratio calculation independently gives an exact finite transfer formula, including the usual Gaussian radius and optimality of isotropic covariance within that class.

Load-bearing steps have already been derived twice on paper: halfspace derivatives by CDF differentiation and conditional score integration; the trace bound by eigenvalue Cauchy-Schwarz and by a selected sign vector plus matrix Cauchy-Schwarz. A variable-covariance field is covered only infinitesimally; no finite-radius conclusion is inferred from this derivative.

Priority diagnostic command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B -c 'import os; print("inherited_nice", os.getpriority(os.PRIO_PROCESS, 0)); print("OMP_NUM_THREADS", os.environ["OMP_NUM_THREADS"])'
```

Output: `nice: setpriority: Operation not permitted`, then `inherited_nice 20` and `OMP_NUM_THREADS 1`. The process is already at priority 20, at least as low as requested; the sandbox rejects the attempted nice change. The verification will assert this inherited priority before computing.

## 4. First numerical audit

Command (wall time approximately 0.12 seconds):

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify.py
```

Output:

```text
nice: setpriority: Operation not permitted
{
  "matrix_cases": 21,
  "halfspace_cases": 420,
  "max_cdf_derivative_error": 4.948756959777256e-10,
  "max_score_integral_error": 3.630606926208202e-11,
  "max_sign_average_identity_error": 0.0,
  "min_sign_bound_ratio": 0.9999999999999998,
  "nice": 20,
  "OMP_NUM_THREADS": "1"
}
PASS: all assertions; audit_data.json written
```

Data saved in audit_data.json. Tested dimensions 1 through 7; isotropic, unequal diagonal, and correlated covariances; p=2.01,3,4,infinity; a=0.1,0.5,0.75,0.9,0.99. Exact halfspace-CDF finite differences and numerical integration of the conditional score independently agree with the derivative constants. All sign vectors were enumerated in each matrix case. These finite checks audit the proof and do not replace it.

Potential missed case found during audit: a covariance derivative can cancel the loss of ONE selected halfspace. The reflected halfspace and attack-sign supremum in the proof are essential. Adding an explicit cancellation test before finalizing.

## 5. Strengthening found during the adversarial audit (18:20 UTC)

The chosen Gaussian special case admits a finite-radius strengthening, so it would be wasteful to stop at the local statement. For the halfspace P_x(A)=a>1/2, moving the mean exactly to its boundary makes its probability 1/2 under ANY nondegenerate Gaussian covariance at the endpoint. Moving slightly farther makes it less than 1/2. Thus the upper bound z/M_p(Sigma(x)) holds at finite radius for arbitrary input-dependent Gaussian covariance fields, without any continuity assumption. Constant covariance attains it, and isotropic covariance optimizes it under the trace budget. This strengthens the same Gaussian minimax piece; it does not settle arbitrary non-Gaussian smoothing or fixed dataset accuracy.

The explicit single-halfspace cancellation test passed: derivatives [0.0, 0.3509966638649736] at a=0.9, s=1, lambda=-2/Phi^{-1}(0.9). It confirms why a one-halfspace local argument alone would have failed. Final run of `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify.py` before the finite strengthening took approximately 0.14 seconds; other metrics were unchanged.

## 6. Finite-radius audit and final report

Added a second derivation of the halfspace boundary distance using p/q norm duality. Added explicit finite-radius checks with endpoint projected standard deviations 0.01, 0.3, 2, and 100, independent of the nominal covariance. At 0.99 times the boundary distance the halfspace probability is above 1/2; at the boundary it equals 1/2; at 1.01 times the boundary distance it is below 1/2. The proof uses the exact formula and does not rely on these checks.

Final command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify.py
```

Final output (exit 0, approximately 0.16 seconds):

```text
nice: setpriority: Operation not permitted
{
  "matrix_cases": 21,
  "halfspace_cases": 420,
  "finite_radius_cases": 1008,
  "max_boundary_probability_error": 1.7708057242771247e-14,
  "max_cdf_derivative_error": 4.948756959777256e-10,
  "max_score_integral_error": 3.630606926208202e-11,
  "max_sign_average_identity_error": 0.0,
  "min_sign_bound_ratio": 0.9999999999999998,
  "cancellation_halfspace_derivatives": [
    0.0,
    0.3509966638649736
  ],
  "nice": 20,
  "OMP_NUM_THREADS": "1"
}
PASS: all assertions; audit_data.json written
```

Saved REPORT.md with the exact Gaussian special-case verdict, precise scope, literature corrections, failures, and next steps. No files outside this folder were modified. No git, subagents, heavy computation, or external publication. The broad all-distribution/fixed-clean-accuracy question remains open in this session; the Gaussian special case is proved.

Final artifact check: a read-only Python command printed the required first line of REPORT.md, parsed audit_data.json (420 rows), and confirmed LOG.md, PROOF.md, REPORT.md, verify.py, and audit_data.json are present alongside the original PROMPT.md. The finite theorem's covariance quantifiers, strict-majority boundary convention, and distinction between a and dataset clean accuracy were checked explicitly.
