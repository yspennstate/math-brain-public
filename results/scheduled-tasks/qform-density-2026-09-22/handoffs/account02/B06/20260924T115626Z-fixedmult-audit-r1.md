SIGNED IN - auditing the fixed-multiplicity quadratic-form density manuscript, account account02, slot B06, 2026-09-24T11:56:26Z.
attacking: graph determinant / Jacobian / weights / regularizer first, then a complete end-to-end audit and a threshold-lowering obstruction analysis.

# account02/B06 fixed-multiplicity audit handoff

Latest owner objective consumed: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`, which supersedes conflicting older instructions to spend this invocation primarily on the unstructured three-eigenvalue attack. The unrestricted three-eigenvalue conjecture remains OPEN.

Pinned manuscript audited: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, source SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Verdict: **PASS for the mathematical 17-eigenvalue baseline in this independent B06 audit; no fatal mathematical gap found.** This is not by itself the two-review independent-validation gate.

Canonical report: `yspennstate/math-open-problems@f45bbd7c0b67c165d45b6b73b0cae3d0cc6cb08c:proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account02/B06/20260924T115626Z-fixedmult-audit-r1/AUDIT.md`.

B06 primary check: the regularized crossing determinant is correct. With `a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2 M^T M`, weights `c_j=alpha e_j^T H^-1 e_j`, `d_i=a^2 m_i^T H^-1 m_i`, the geometric frame identity is exact. The scalar Fourier-power estimate cancels the `d_i` powers; `prod c_j^(-c_j/2)<=e^(theta/2)`; factoring `alpha^d` leaves `(2*pi*e/sqrt(alpha))^theta=1`. Fourth-root decoupling yields exactly

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

Every remaining manuscript dependency was read and reconstructed end to end: Fourier/Riesz normalization, heat-flow BL, product projections, scalar Fourier powers, decoupling, crossing volumes, scalar and two-coordinate kernels, quarter-power concentration, sampled nonsymmetric interpolation, global/restricted rank bounds, no-pivot spectral-to-volume conversion, random cut, half-potential bookkeeping, Schur spectral counts and final scaling.

Two nonfatal gaps were recorded. First, in the product-projection proof after `b_i=0` rows are omitted, the text should use `sum_{b_i>0}(1-b_i)<=d` rather than equality; this is the required direction and changes no result. Second, current root inspection found the README-named `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` absent; this is a reproducibility/package gap, not a symbolic-proof gap.

New route obstruction: retuning the scalar BL regularizer cannot improve the polynomial exponent. Before fixing alpha the fourth-power majorant is

`det(I+a^2 M^T M/alpha)^(-1/2) (2*pi*e/sqrt(alpha))^theta`.

For fixed rank r and `alpha/a^2->0`, each nonzero singular direction asymptotically contributes `2*pi*e/(|a| sigma)`, hence after the fourth root the exponent remains `r/4`. Comparable/larger alpha is no better. Thus the r=4 route remains the borderline `1/|t|` endpoint.

New source-valid counterexample to an abstract endpoint compiler: for independent cap-one `U,V~Uniform[-1/2,1/2]`,

`Q0=2UV`,

`p_Q0(q)=log(1/(2|q|)) 1_{|q|<1/2}` is unbounded, while `phi_Q0(t)=2 Si(t/2)/t=O(1/t)` and `sup_a E|Q0-a|^-1/2<infinity` (e.g. `p_Q0 in L^3` and Holder). Therefore `1/t` Fourier decay plus the manuscript's kind of half-potential bound cannot abstractly imply L-infinity. This refutes only that synthesis step; Q0 has only two large eigenvalues.

Threshold status: 17 certified in this audit; no 16 or 13 theorem proved. The first unpaid implication is `QFORM-FIXEDMULT-K4-STRUCTURED-ENDPOINT-v1`: exploit actual original-coordinate product/quadratic structure under `Z4(M)>=c` to obtain L-infinity, rather than combining only the two abstract endpoint estimates. A successful theorem would pair with the audited interpolation to lower 17 to 13.

Execution remains `WITHOUT_VERIFIED_BRAIN`. Model self-report: GPT-5.6 Sol. Reasoning effort: UNKNOWN. Provider reasoning-token/thinking-time telemetry: null/not exposed. No task identity, schedule, enabled state, quiet state, notification, email, account binding, permission, public-release setting, paid call, or remote workflow was changed.
