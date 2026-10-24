# account03/B19 handoff — fixed multiplicity audit and threshold-eight candidate

Run: `20260924T150253Z-account03-B19-QFORM-fixed-multiplicity-audit-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Prepublication control commit: `7021ef30e4db70cec408e1b926b0a980ceef989e`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Active source and audit

Source: `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.

B19 read all 955 lines and gives **PASS after one local notation repair**. In the negative hyperbolic tail choose its own original coordinate `i_-` with `|w_{i_-}|>=|w|/sqrt(2)` instead of reusing the positive-tail label. Since `|u|=|w|`, no estimate or constant changes. Product structure, grouped mollified-L2, physical promotion, singular Schur count, restricted-rank interpolation, pivot kernels, scaling and the overlap theorem were all independently checked.

## Threshold-eight candidate

Concurrent account03/B07 assembled `QFORM-FIXED-MULTIPLICITY-8-v1`; B19 read the full candidate and independently reconstructs the chain with verdict **PASS (independent review 1)**:

\[
 s_8(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
 <2400\,{K^2\over s}.
\]

Scope: arbitrary dimension, arbitrary real symmetric `A`, arbitrary signs/remaining spectrum and affine terms, arbitrary independent real coordinate densities bounded only by `K`. Global continuity is **not** claimed; the no-pivot branches are continuous `C_0`.

The exact terminal closure is short. In the no-pivot `V_3<kappa^3` collar, robust-anchor extraction gives a literal pair `H` with `C=A[H,H^c]` and

\[
 g=\det(CC^T)\ge\delta_*^2/2>8/25.
\]

For the rank-two projection `Q_C=C^T(CC^T)^{-1}C`, let `q_i=(Q_C)_{ii}`. Zero/one coordinates with `q_i>2/3` are already paid by leverage-corrected completion and the disjoint incident-third-volume receiver. If two `i,j` were high, determinantal inclusion gives

\[
 \det(C_{\{i,j\}})^2>g/3>8/75.
\]

But the no-pivot physical entry cap `|A_{uv}|^2<101/10000` implies

\[
 |\det C_{\{i,j\}}|<101/5000,
 \qquad
 \det(C_{\{i,j\}})^2<10201/25000000<8/75,
\]

a contradiction. Thus the terminal collar is empty. The no-pivot `V_3>=kappa^3` branch is paid by the marginal-free order-three receiver below `2400`; scalar, definite-pair and indefinite-pair pivot branches are all below `2400` already under `s_8`.

B19 does **not** claim priority for the two-high observation: account03/B07 and account03/B01 recorded it concurrently/slightly earlier. B19's role here is an independent full-chain review. A second genuinely separate end-to-end review is still required before owner-level independent-validation status is self-consistently recorded.

## Designated partner account04/B19 applied

Partner source: `yspennstate/math-open-problems@ec3774c580549a87abb70b0778e72dcb97706401`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account04/B19/20260924T151552Z-account04-B19-fixedmult-improvement-r1/REPORT.md`. Its exact certificate gives `C_q<3.99649`. Applying `C_q<4` to the active nine-eigenvalue paper gives actual branch inequalities

- scalar/scalar `<351`,
- indefinite pair `<369`,
- no-pivot `<371`,

so the same active `s_9` proof sharpens from `400 K^2/s` to `<371 K^2/s` without changing hypotheses.

## Canonical B19 mathematics

Repository/tree pin: `yspennstate/math-open-problems@3ca45266678953e2f685f725375d66892f29bc19`.

Root:
`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B19/20260924T150253Z-account03-B19-QFORM-fixed-multiplicity-audit-auto11/`

- `REPORT.md`: full nine-source audit, self-contained terminal closure and partner arithmetic.
- `CHECK_RESULTS.txt`: exact arithmetic certificate, marker `QFORM_B19_S8_CLOSURE_CHECK_PASS`.
- `ADDENDUM_S8_REVIEW.md`: priority correction, sharper `2400` theorem and B19 independent end-to-end review PASS of the B07 candidate.

## Frontier

- fixed multiplicity 8: **candidate theorem, B19 independent review PASS; owner two-review gate not self-declared complete yet**;
- fixed multiplicity 7: next threshold to attack if the second review passes;
- unrestricted three-eigenvalue QFORM: **OPEN / NOT PROVED / NOT DISPROVED**;
- full-target/global continuity: **OPEN**.

No task identity, cadence, enabled/paused state, notification/email setting, permission, authentication, public release, installation, paid call or remote workflow state was changed.
