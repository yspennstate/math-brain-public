# T224 work log

Started: 2026-11-14 21:21 Asia/Tbilisi (UTC+04:00).
Task: “push this problem forward by one checkable piece.”

## Scope and startup

All writes stay in this folder; no git, external publication, subagents, or heavy computation. The task-specific folder restriction supersedes global instructions to write mesh/checklist/brain state elsewhere. Read the startup memory index and mesh protocol without changing them. Compute state: status ok, mode owner_away_open. Shell Python calls use OMP_NUM_THREADS=1 and nice -n 15; nice reports a priority-setting restriction, so no heavy computation will be attempted.

## Step 1: literature search (in progress)

Used the web search tool for the exact arXiv identifier, the title, slow convergence, and counterexamples. Opened https://arxiv.org/html/2605.22010v1 and https://arxiv.org/abs/1804.06561. The search returned a November 2026 source revision; inspecting the current version next. No conclusion of settlement yet.

### Literature outcome

The official source page https://arxiv.org/abs/2605.22010 lists Margalit Glasgow and Joan Bruna, v3 dated 11 November 2026. Opened its full HTML at https://arxiv.org/html/2605.22010v3. Remark 6 already treats c=2 by truncating the square-root-loss integral and gives a polynomial high-probability weak error bound. Section 6 still explicitly lists c<2 as open. Thus the original problem is not wholly settled. No SOLVED_ELSEWHERE.md claiming full settlement will be written. Also opened the arXiv page of Song Mei, Andrea Montanari, and Phan-Minh Nguyen, arXiv:1804.06561; no uninspected paper is used as evidence. Search queries included the exact identifier/title, Glasgow Bruna slow propagation 2026, and weak propagation nonintegrable neural. Literature phase ended within ten minutes.

## Step 2: chosen piece

Prove a quantitative uniform-in-time weak error bound for 0<c<2 in the subclass with globally bounded activation and three bounded derivatives. Target: a stretched-logarithmic rate using loss-dependent semiconvexity, rather than a polynomial-width assertion. This is a concrete partial result: bounded smooth activations are within the source's Euclidean regularity assumptions; the estimate would show how much the decay alone does yield without treating c=2 as new. First derive the deterministic stability inequality and identify whether its nonlinear remainder can be bootstrapped on a growing horizon. If that fails, retain only a fully justified logarithmic-rate theorem.

## Step 3: deterministic estimate derived

Let phi(w)=sigma(w dot X) in H=L2(P_X), with norms bounded by A, B, M for phi, Dphi, D2phi. For the mean residual r_t define h(t)=sup_w max(0,lambda_max(-<r_t,D2phi(w)>)) and H(T)=integral_0^T h(t)dt. The normalized empirical-risk Hessian splits into a positive semidefinite Jacobian-square term and a residual-curvature term. Along the segment between interacting particles and iid mean-field characteristics, the RMS parameter discrepancy q satisfies

q' <= [h(t)+M eta(t)+MB q] q+B eta(t),

where eta is the H norm of the iid sampling fluctuation, with E eta(t)^2 <= A^2/m. Thus E(integral_0^T eta)^2 <= A^2 T^2/m. A stopping argument at q=1/T, with a threshold on this integrated fluctuation, gives a deterministic-horizon expected output estimate K(1+T)^4 exp(2H(T))/m. Loss monotonicity extends it to all times with an added 6L_T. Next: write every step and independently check constants/signs and the logarithmic exponent.

This additionally identifies a sufficient stability hypothesis: H(T)<=h0+kappa log(1+T) gives a polynomial width exponent c/(c+4+2kappa). This is sufficient, not claimed necessary or sharp.

### Proof saved

Created PROOF.md with an explicit constant K, the normalized empirical-risk Hessian calculation, a stopping argument using only E Z_T^2, and the loss-monotonicity extension. The resulting master bound is 4K(1+T)^4 exp(2H(T))/m + 6L_T. Consequences are the stretched-logarithmic slow-decay bound and the sufficient logarithmic integrated-curvature condition for a polynomial rate. The latter exponent is c/(c+4+2kappa); no sharpness claim. Corrected two stray draft display fragments immediately after saving.

## Step 4: independent audit

Saved audit.py and ran exactly:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit.py
```

Output (complete structured data is in audit_results.json):

```json
{
  "seed": 224,
  "hessian_and_coupling_cases": 200,
  "max_hessian_risk_second_difference_error": 7.273956076359056e-08,
  "max_hessian_gradient_difference_error": 1.5019611665501031e-09,
  "max_coupling_inequality_violation": -0.012888690525113832,
  "min_jacobian_square_term": 0.0012489718140441487,
  "max_constant_ratio": 0.8649849541759318,
  "max_stopping_bound_times_T": 0.37489679051053576,
  "linear_psd_sign_check": true,
  "status": "PASS",
  "scope": "Algebra and finite-difference audit only; not evidence of the infinite-time theorem by simulation."
}
```

The script independently checks the empirical-risk Hessian by second differences of the scalar risk and by differences of its vector gradient, in 200 seeded cases. It also directly computes the coupled vector fields for a bounded feature map (sin w, cos w), checks the one-sided coupling inequality, the PSD sign on a linear feature, 200 instances of the explicit constant and stopping threshold, and 15 exact rational exponent balances. These are algebraic checks, not numerical evidence for an infinite-time assertion.

Analytic attempts to break the proof:

- Temporal dependence: (10) uses Cauchy--Schwarz and Tonelli, with no independence across times.
- Norm order: the proof establishes sup_t E error^2. It does not claim E sup_t error^2, because eta_t is only controlled in expectation at each fixed t.
- Parameter/output distinction: q is a paired characteristic discrepancy used inside the proof. The theorem bounds output L2 error; it never equates q with Wasserstein sampling error.
- Nonlinear coupling: the MBq^2 term is retained and controlled by a first-hitting-time argument. Dropping it would be unjustified.
- Rare initializations: bounded features give the 4A^2 output cap used on the bad event. This is where unbounded activations fall outside the theorem.
- Long-time control: (22)--(24) require exact population gradient flow and a common target g, and use loss monotonicity. The proof does not extend itself to finite training data or discrete steps.
- Curvature sign and normalization: checked the positive Jacobian-square term, normalized m-inner product, and factor 2 in both dissipation identities.
- Tail constants: 2 E L_T^m+2L_T <=4 E error_T^2+6L_T. An independent expansion of the two squared triangle inequalities reproduces 4 and 6.
- Exponents: p=1-c/2, c/p=2c/(2-c). For the stability condition, balance (1+T)^(4+2kappa)/m with (1+T)^(-c), giving a=c/(c+4+2kappa). The audit checks both identities with exact fractions.
- Degenerate cases: B=0 gives identical constant outputs; M=0 leaves the estimates valid; C=0 leaves only the first term of (26). The chosen D includes 1 so horizon selection never divides by zero.
- Near c=2: constants and the threshold deteriorate as p approaches zero. No estimate uniform in c up to 2 is claimed. The endpoint is already in the source.

No gap found in the stated bounded-feature Euclidean theorem. No proof of polynomial convergence from loss decay alone, no sharp exponent, and no counterexample were obtained.

## Step 5: report and final artifact audit

Created REPORT.md with verdict PARTIAL, theorem and consequences, exact verification command, limitations, and next action. Created SOLVED_ELSEWHERE.md to record partial endpoint coverage in the source; its first paragraph expressly says the whole problem is not settled. This supplements the earlier literature entry: the filename records an advanced special case, not a full-settlement claim.

Resource check: a tiny standard-library Python process read its actual priority using os.getpriority as 20; its maximum RSS was 14,565,376 bytes. Thus the nice wrapper warning reflected inherited lower priority rather than a heavy process running at normal priority. No heavy program, network shell command, git operation, subagent, or write outside this folder was used.

Read back the entire PROOF.md. All 38 display-math delimiters are paired, and no draft display fragments remain. Rechecked the theorem's target, the all-time loss extension, and the caveat about unbounded activations. The finite-difference audit is explicitly distinguished from proof.

Final check: all six required/result artifacts exist, REPORT.md begins with VERDICT: PARTIAL, audit_results.json has status PASS, and the proof displays remain balanced. Work complete for this session.
