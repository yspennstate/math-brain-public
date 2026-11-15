# T248 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First clock: 15 November 2026, 03:37:12 +04 (2026-11-14 23:37:12 UTC).

## Orientation and literature check

All writes stay in this directory. No subagents, git, external messages, mesh/checklist/brain writes, or background processes. The task-specific folder restriction prevents the global shared-state write rituals. Read the startup memory, BRAIN_INDEX, T248 entries in TOPICS, and compute_state.json (warn/cpu_saturated, owner_away_open); no heavy computation is planned.

Read the previous REPORT.md, LOG.md, and SOLVED_ELSEWHERE.md at `~/codex_op_1114/briefs/T248`. A directory listing confirms there is no PROOF.md or research script there; the previous report explicitly says no computation was run.

Web search queries: `"Tracy–Widom law for sample covariance matrices under quadratic" Chen Lyu` and `random feature conjugate kernel Tracy Widom edge universality 2026`. Opened arXiv abstract pages and full HTML for 2610.41416v2 and 2609.09440v2. Chen–Lyu is still v2, revised 4 November 2026; Ma–Misiakiewicz is still v2, revised 11 September 2026. No later complete solution was identified. Literature search ended within five minutes of the first clock reading. The earlier general-covariance theorem is present with the hypotheses and normalization reported. This is not a reason to stop as solved: these are the same papers the predecessor already found, and the full original question is not covered.

## Independent recheck and selected extension

Re-derived conditional centering from exact unit Gaussian preactivation variances. Re-derived the sample-count normalization using the equality of nonzero squared singular values: H=Y^T Y/m and lambda_max(YY^T/N)=(m/N)lambda_max(H). Independently derive the required quadratic-form moment bound in PROOF.md from Gaussian Lp Poincare and concentration of ||Aq||; this does not rely on the predecessor's citation to Proposition 2.8. The earlier conditional application holds under its explicitly stated covariance hypotheses.

Selected ONE extension: prove deterministic finite-size centering and TW1 for independent spherical input columns and a nonzero Lipschitz activation of Hermite rank at least 3, with N/m tending to a positive limit other than 1. This is the predecessor's first requested next step. The covariance has exactly constant diagonal. Its squared Frobenius distance from vI has expectation at most v^2 N(N-1) 15/[d(d+2)(d+4)]. The vanishing trace cancels the first-order perturbation of the covariance edge. A deterministic edge lemma should then give an O_p(d^-2) centering error, rather than merely operator-norm closeness. Prove this lemma before invoking Chen–Lyu.

Sources actually opened:

- Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form concentration*, https://arxiv.org/html/2610.41416v2, Assumptions 1.1–1.2 and Corollary 1.4.
- Renyuan Ma and Theodor Misiakiewicz, *The anisotropic local law for sample covariance matrices under quadratic-form concentration*, https://arxiv.org/html/2609.09440v2. Background only; the new proof does not need its local-law theorem.

No SOLVED_ELSEWHERE.md is created: the original T248 statement remains unresolved.

## Proof completed and independent scalar checks

Wrote PROOF.md. The new theorem is TW1 for spherical inputs, a fixed Lipschitz activation with a_0=a_1=a_2=0 and variance v>0, and m/N tending to b in (0,infinity) other than one. The finite center is v(1+sqrt(m/N))^2. The multiplicative scale is N^(2/3)(m/N)^(1/6)/[v(1+sqrt(m/N))^(4/3)].

The deterministic edge lemma proves |E_X-e_0|+|gamma_X-gamma_0|<=C Tr((Sigma_X-vI)^2)/N when Sigma_X is near vI and has trace Nv. Its proof uses cancellation of the linear Taylor term in the population eigenvalues. With spherical input, the right side is O_p(d^-2). The leading edge-shift coefficient is (1+sqrt(r))^2/(v sqrt(r)), r=N/m. Its sign is independently checked using Jensen convexity. Gaussian quadratic-form concentration is proved directly by a Gaussian rotation argument, including its dimension-uniform fixed-p constants. Conditional-to-unconditional convergence is justified by a deterministic bad-sequence contradiction, rather than assuming unproved uniformity in the external theorem.

Command (one standard-library-only scalar run, under a second, no arrays or numerical libraries):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_edge.py
```

The sandbox printed `nice: setpriority: Operation not permitted` and then ran the script successfully, exit 0. Thus the requested priority was attempted but not applied. No more Python or numerical programs will be launched in this session. This run uses negligible memory and does no matrix simulation.

Output that matters:

```text
Two-point populations t=v+-epsilon; trace perturbation exactly zero
v r eps/v edge_shift/s2 predicted relative_error minimizer_disagreement
0.7 0.25 0.003 6.428094190 6.428571429 7.424e-05 0.000e+00
0.7 0.50 0.003 5.887342394 5.887600491 4.384e-05 4.441e-16
0.7 2.00 0.003 5.887497928 5.887600491 1.742e-05 0.000e+00
0.7 4.00 0.003 6.428495493 6.428571429 1.181e-05 0.000e+00
1.3 0.25 0.003 3.461281487 3.461538462 7.424e-05 4.441e-16
1.3 0.50 0.003 3.170107443 3.170246418 4.384e-05 0.000e+00
1.3 2.00 0.003 3.170191192 3.170246418 1.742e-05 8.882e-16
1.3 4.00 0.003 3.461497573 3.461538462 1.181e-05 1.776e-15
max edge disagreement: 1.776e-15
spherical sixth-moment identities: exact agreement at d=2,3,10,100,1000
coefficient finite-difference max relative error: 3.909e-08
transposition scale max relative error: 2.220e-16
activation sin(t)-exp(3/2)sin(2t)/2: a1=0.000e+00, a3=0.742845315, variance=1.607934850
PASS: scalar checks only; the TW conclusion uses the cited theorem.
```

The run checks 32 two-point populations: v=0.7,1.3; r=0.25,0.5,2,4; epsilon/v=0.1,0.03,0.01,0.003. It solves stationarity by bisection and independently minimizes f by golden-section search. The printed excerpt keeps the smallest perturbation for each v,r; the script regenerates the complete table. Both sides of the rectangular regime are tested. The coefficient is separately checked by finite differences of the scalar kernel. The spherical sixth moment is re-derived by radial Gaussian moments and Beta moments, with exact rational agreement. The normalization is checked by direct scalar evaluation for four dimension pairs in both orientations. These computations check algebra, not TW numerics.

## Attempts to break the result

- Nonzero a_2: squared correlations have nonzero mean 1/d; the Frobenius-small covariance argument fails. This is an actual scope restriction, not a removable error term.
- Random Gaussian column norms: exact conditional centering and exact trace Nv no longer follow. This theorem does not apply to that branch of T248.
- Aspect ratio one: excluded by the external theorem even though the covariance-edge lemma itself is valid there. Transposition does not repair the exclusion.
- Fixed limiting-aspect centering: replacing m/N by its limit without a rate is unjustified on the TW scale. The theorem retains the exact ratio.
- Non-Lipschitz activation, zero variance, or an added linear coefficient: explicitly excluded; no concentration or spike conclusion is claimed.
- Uniform conditional application: checked by selecting a deterministic bad design sequence if uniformity were to fail; uniform constants and regularity hold for every such sequence.
- No entrywise independence of Y is assumed anywhere. Conditional independence is across feature rows, and the covariance-edge theorem is applied with sample count m.

The only unavailable infrastructure step was the nice priority adjustment. The complete original problem remains open in the omitted cases. No empirical TW claim or new local-law proof is made.

## Final artifact audit

Read back the complete PROOF.md and checked the exact report verdict, assumptions, source attribution, and finite-aspect normalization. Commands: `sed -n '1,280p' PROOF.md`, `wc -l LOG.md PROOF.md REPORT.md verify_edge.py`, `head -1 REPORT.md`, targeted `rg -n` checks, and `ls -l` on the four artifacts. All four files exist. The proof covers both rectangular orientations while retaining the external theorem's exclusion of ratio one. REPORT.md states what is new, the computational checks and priority failure, the unproved cases, and the proposed next step. No later numerical run or outside-folder write was performed.
