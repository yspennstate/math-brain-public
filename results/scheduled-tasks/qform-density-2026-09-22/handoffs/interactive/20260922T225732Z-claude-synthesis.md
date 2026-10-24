# Newest-Claude synthesis: one remaining no-pivot density problem

Owner request: use the good results uploaded by the Claude agents to finish the full proof, and make all scheduled workers use the newest Claude work. Programme QFORM-DENSITY-3EIG-20260922. This is an interactive handoff, not a scheduled-worker sign-in. The full conjecture remains NOT PROVED by the checked synthesis.

## Actual newest sources consumed

Claude commits `e5f71d79eff325201dd0274053d20268ce65b837` (22:38:33Z) and `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926` (23:03:41Z), 22 September, in math-open-problems, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. Read FOURIER_ROUTE_REPORT.md, COUNTEREXAMPLE_SEARCH.md, the later GEOMETRIC_ROUTE_REPORT.md, and updated RESULTS.md. The final path-specific history read still showed 2f3340cd as the newest directory commit. Subsequent actual commits should be consumed at the next refresh. These contributions are not merely reports of work: they contain mathematical proofs. Their own full-target gaps remain explicit.

## Complete new supporting proofs, code, and executed results

Read `math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/README.md`.

All six mathematical proof/check files are present by `6dc1ce3ee7dba3621f83b49c961182fa2c4ab2ab`. The six Git blob hashes were read back and matched against local file bytes. The two full arguments are:

- GEOMETRIC_SYNTHESIS.md, blob `3812bec781d7878b5f11e174d4d30a4c725f7370`.
- REPORT.md, blob `6a5748aa1e93033b78d2c07d81e1468068ea4662`.

Independent end-to-end review is pending. The finite check scripts and their actual results are corroborating algebra, not universal proof certificates. No literature-wide novelty or native learned-memory ingestion claim is made.

### A. Use Claude's hyperbola lemma to remove the pair condition-number loss

For any actual original-coordinate indefinite 2x2 principal block B, D=|det B|, and s_3(A)>=s>0, the new synthesis proves

`||p_Q||_infinity <= D^(-1/2)[9.2+log_+(10000sqrt(D)/s)]`.

All other eigenvalues, couplings and affine terms are arbitrary. This combines Claude GEOMETRIC_ROUTE_REPORT Lemma 1.4 with the earlier arbitrary-rank quarter-power small-ball theorem at 742ac943440e41925fe09db9a8c02a96cbd83dbc. The Schur remainder has operator norm at least s_3(A), by a rank-two approximation. The resulting bound does not depend on sigma_min(B). At D>=3501/64000 and s>=1 it is below73. It does not assert that such a physical pair always exists.

### B. The logarithmic auxiliary theorem is already closed

For every nonzero symmetric S, R=Z^TSZ+b^TZ+c under the original law assumptions,

`sup_t E log_+(K/|R-t|) <=4+log_+(625K/||S||)`.

In particular ||S||>=1 gives a global constant `4+4log5<10.438` at K=1. This closes Claude's Hyp'_1 without a no-pivot restriction. Do not keep assigning that auxiliary problem as open.

### C. One remaining no-pivot statement suffices

Fix tau in (0,1]. Define N3(tau,C0) to be the original universal density statement restricted to actual matrices satisfying

`|A_ii|<tau`, `|det A[{i,j},{i,j}]|<tau` for every i,j,

while retaining three absolute eigenvalues at least one and arbitrary cap-one product inputs. GEOMETRIC_SYNTHESIS Theorem 5.1 proves that N3 implies the FULL conjecture with

`C_full <= tau^(-1/2) max{1+2exp(pi)C0, 1+3K_tau}`,
`K_tau=(2/sqrt(tau))[6.2+log_+(16sqrt(tau))]`.

No separate no-pivot half-Riesz hypothesis is needed. To see the essential bridge, append N>1/tau NEW independent coordinates with density exp(-pi x^2), and the rank-one block +/-J_N/N. These added blocks preserve the strict no-pivot class and supply one extra absolute eigenvalue1. Applying N3 to R+G^2 and R-G^2 controls the two one-sided half-Riesz potentials. The Gaussian variables are auxiliary in a reduction; the original input law remains arbitrary. The proof includes the affine regularization, lower-semicontinuity step, sign cases and all constant transfers. N3 ITSELF IS STILL UNPROVED.

### D. Close the actual finite-dimensional problem and finite-core dense-tail branch

For any actual A with s_3(A)>=sigma, arbitrary rank and affine terms, REPORT Theorem 3.1 proves

`||p_Q||_infinity <=(2sqrt(2pi)/sigma) sum_i ||P_E e_i|| <=2sqrt(6pi n)/sigma`,

where E spans any three substantial eigendirections. This uses a projected-gradient identity, physical-coordinate slicing, and the cap-two 2D product-marginal theorem. It uses E, NOT range(A), and hence improves the general dimensional loss. It is not a dimension-free bound.

For an m-coordinate physical principal block `A_HH=U_H Lambda U_H^T+T_H` with `U_H^T U_H>=aI`, `sigma_min(Lambda)>=s`, and `||T_H||<=epsilon<as`,

`||p_Q||_infinity <=2sqrt(6pi m)/(as-epsilon)`.

Arbitrary outside blocks and dense/nonseparable tails are retained exactly. The example m<=30,a>=.8,s>=1,epsilon<=.1 gives <68 independently of ambient n. A large rank-three component plus an arbitrarily cancelling diagonal is NOT an actual spectral condition. The fully localized branch is controlled; the one-/two-localized-direction hybrid is not covered by this argument.

### E. Correct the combined rank-three map

Semidefinite exact-rank-three forms were already proved with constant3e by account02/B18 in `20260922T123541Z-account02-B18-QFORM-r11/REPORT.md`, read at math-open-problems commit f8b6f4d6763094eedf3b23b845dce57e28279c55. REPORT Section6 reproduces the short compatible proof; it is not a new theorem. Do not leave this case open in the merged map.

Claude's ruled one-sheet estimate is justified for rough input laws in REPORT Section7 by smooth cap-one product approximation and interval domination. It remains a ONE-SIDED exact-rank-three estimate, not the full indefinite case or a continuity theorem. The localized/hybrid indefinite two-sheet side and additional-spectrum no-pivot class still need work.

## Specific next use by existing workers

Existing account02/B19 and account03/B12 independently check the new synthesis end to end: the logarithmic layer cake, determinant-only pair averaging, class-preserving Gaussian padding, affine limiting step, Schur count and constant transfer. No review is predeclared passed. Existing account02/B05 and account03/B15 check the projected-gradient/rough-ruling proof and then APPLY it; keep the reviews mathematical and bounded. Earlier reviews do not approve these new arguments.

B01-B04 apply D', D5, weighted volume and averaged-frequency methods directly to N3, preserving source dependence. B07-B12 combine the finite-core and determinant-only pair payments with the hub/one-factor/dense-tail survivor inside N3. B13-B16 retain rough-law limits, actual affine terms and product-source marginal geometry. B17 targets valid adversarial constructions in the uncovered class; B18 checks primary inputs needed at the live gap. B19/B20 assemble one noncircular proof of N3 and the completed implication to the full theorem. Do not reprove the globally controlled logarithmic potential, semidefinite rank-three case, or finite-dimensional statement as though those finish the target.

## Native rollout and real work

All twenty account04 native prompts were updated successfully, prompt fields only, between23:04:14Z and23:08:21Z under lease7eaf6f61b293dc66b6830962a118e1b61306d3be. The exact sanitized evidence is at brain commit9f04824830186e7c48f847ce52c143702ac046e6, `scheduled_tasks/work/shared/qform-density-2026-09-22/events/interactive/20260922T225732Z-claude-synthesis/NATIVE_SOURCE_REFRESH.json`.

Their required mutable newest-Claude directive will now point to this synthesis and the later2f source. Other account B20 coordinators must perform their own lease/inventory-authorized native source refresh; no direct other-account mutation or later adoption is claimed here. Preserve all differentiated roles and the exclusive full QFORM target.

Each actual worker signs in at the real time, saves only its own canonical login/run receipt, pushes useful partial mathematics before ending, and provides a read-back commit and path. Configuration, actual invocation, sign-in, mathematical progress, successful push and independent correctness are different evidence classes. Reconcile missing pushes with genuine artifacts or actual error/incomplete reports; no fabricated acknowledgements, speculative restarts, backdating or permission bypasses.

Latest control read: brain3be802acd8880e828362a43d547073f2bf4f14ef, revision2026-09-22.15. Later owner/platform changes and stops prevail. Preserve hourly schedules, identities, states and quiet delivery. No other research, new tasks, notifications, paid calls, remote workflows, public release, cross-account authentication or production-store mutation. Repository delivery is not native memory ingestion.
