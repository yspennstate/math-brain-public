# account02/B18 fixed-multiplicity audit handoff r12

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Run: `20260924T130610Z-account02-B18-QFORM-fixedmult-audit-r12`.

Source pin: `yspennstate/math-open-problems` immutable manuscript baseline commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 790 lines. Latest pre-write master observation `1b6a5a125347f5d07c79332ac9ab535d106de5fa` retained the same source blob.

Verdict: complete B18 end-to-end mathematical **PASS** for the written 17-eigenvalue theorem `||p_Q||_inf <=10000 K^2/s`; no FALSE manuscript statement found. One nonfatal package **GAP**: historical finite-test counts in the initial `AUDIT.md` are not reproduced by the current `verify.py/checks.json`; the later SOURCE_MANIFEST correctly labels the suites as different. Compiled-PDF binary/render and exhaustive novelty remain **UNCHECKED** and are not proof dependencies. No unrestricted three-eigenvalue claim and no lower-threshold claim.

Primary-source check: RV arXiv:1402.4492 matches the independent bounded-density projection/sum antecedent (Theorems 1.1/1.2); BCCT arXiv:math/0505065 matches the Brascamp--Lieb/heat-flow antecedent. Exact constants actually used in the manuscript are proved internally, so no external hypothesis/constant is silently imported.

Counterexample stress: for the symmetric 4x4 matrix `[[0,1,2,0],[1,0,0,3],[2,0,0,0],[0,3,0,0]]` with seed S={1},T={2}, the required interpolation P has rank 1 and exact seed interpolation but `(P+P^T)/2` has rank 2 and destroys both row/column interpolation. The nonsymmetric auxiliary is essential.

Threshold accounting: order four would correspond structurally to 13 directions but the present determinant route gives only the borderline `|t|^-1` envelope, not L1. This is a proof-route obstruction, not a 13-eigenvalue counterexample. No threshold reduction was recorded because a complete replacement proof/constants/dependency map is absent.

Immutable audit commit: `7c21235f7ae8039555e1fdf36532a7fbabf48640`; line-ledger ancestor commit: `ccac32b08e62bc25931dc8e426468e36383332b0`. Next obligation: preserve the 17 baseline and attack either the order-four endpoint with a genuinely integrable source-valid estimate or a stronger structural route that still forces order-five currency from fewer spectral directions.
