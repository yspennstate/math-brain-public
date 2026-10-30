# fleet03/B12 independent audit — scalar pivots, kernels, and end-to-end closure

Run: `20260924T124631Z-fleet03-B12-fixedmult-audit-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `fleet03/B12`  
Starting lens: scalar pivots; square and logarithmic kernel integrability.  
Review status: independent mathematical reading by this worker; **not** a fleet-wide validation certificate.

## Source pin and package state

- Owner-pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Owner-pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Owner-pinned / fresh-read manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Fresh `master` immediately before publication: `5d43209b89cb8889811e0dbf6ff55d284b539cc4`; `manuscript.tex` still had the same blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- `README.md`, `AUDIT.md`, and all 790 source lines of `manuscript.tex` were read.
- At the fresh tree I obtained `404 Not Found` for `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`. This is a **package/reproducibility GAP**, not by itself a mathematical gap in the self-contained manuscript. The paper's proof does not depend on those files, but the finite-check claims in the README/self-audit cannot be independently rerun from the currently committed root until those files are restored or their absence is documented.

## Overall verdict

**PASS for the written 17-eigenvalue theorem, subject to the package GAP above.** I did not identify a fatal mathematical defect in the self-contained proof after an end-to-end line-by-line reading. In particular, the B12-sensitive square-profile, logarithmic-kernel, scalar-pivot, and moving-critical-value steps are valid as measure-dominating statements and do not smuggle in independence after a rotation.

This is one independent review only. It does not make the candidate globally `INDEPENDENTLY_VALIDATED`; the owner objective requires two genuinely separate complete reviews. It also does not prove the unrestricted three-eigenvalue conjecture.

The manuscript itself proves essential boundedness. Continuity is proved on the no-pivot Fourier-inversion branch, but the pivot branches are only handled by density domination; I therefore mark a continuous representative for the entire 17-eigenvalue theorem **UNCHECKED / NOT PROVED BY THIS MANUSCRIPT**.

## End-to-end audit ledger

| Source lines | Statement / dependency | Verdict | Independent check |
|---|---|---|---|
| 1–80 | theorem quantifiers, architecture, normalization parameters | PASS | The theorem has the required rough product-law quantifiers, arbitrary signs/dimension/affine terms, and states only essential boundedness. The later scaling gives the advertised `K^2/s` homogeneity. |
| 81–160 | Fourier normalization, Gaussian inversion, power envelope, negative half moment | PASS | With `hat f(t)=∫e^{itx}f(x)dx`, Plancherel has factor `2π`, inversion has `1/(2π)`, and the Gaussian identity is consistent. The Riesz calculation gives the stated `1/sqrt(2π)` coefficient and weighted integral `12 sqrt(u)`. |
| 161–209 | singular-value perturbation and Schur spectral count | PASS | The rank perturbation statement follows from best low-rank approximation. For an invertible symmetric block matrix, `S^{-1}` is the complementary principal block of `A^{-1}`; positive and negative Cauchy interlacing separately imply the absolute spectral count. The `A+εI` limiting argument covers singular `A`. |
| 210–269 | geometric rank-one Brascamp–Lieb heat-flow proof | PASS | The frame identity makes the velocity quadratic form nonnegative, heat tails justify integration by parts, and the `t→∞` scaling uses `Σc_i=d` and `Σc_i(u_i·z)^2=|z|^2`. Fatou at `t↓0` has the correct direction. |
| 270–320 | product projection density and scalar integrated Fourier powers | PASS | The BL scaling gives `∏b_i^{-b_i/2}≤e^{d/2}` without asserting rotated independence. For scalar Fourier powers, `|hat f|^{2m}` is integrable because `|hat f|≤1` and `hat f∈L^2`; inversion at zero plus the projection cap yields the stated constant. |
| 321–400 | decoupling, regularized determinant, crossing-volume envelopes | PASS | Both decoupling powers retain only original-coordinate independence. In the graph BL step, `α=(2πe)^2` exactly cancels the entropy factors; taking the fourth root gives determinant exponent `-1/8`. Keeping the order-`k` determinant term gives exponent `k/4`; `k=5` is integrable and `k=3` becomes integrable only after the `|t|^{-1/2}` Riesz weight. |
| 401–432 | scalar square profile and conditional profile | PASS | Completing the square gives two inverse branches and density at most `1/sqrt(|a||z-v|)`. The interval inverse length is at most `2 sqrt(2ρ/|a|)`. Conditioning on the other **original** coordinates and integrating the conditional domination by Tonelli justifies `p_Q(z)≤|a|^{-1/2} E|z-R|^{-1/2}`; no independence of the square and `R` is claimed or needed. |
| 433–481 | definite pair and hyperbolic pair | PASS | The definite Jacobian is `1/(2 sqrt(det B))`, so angular integration gives `πM/sqrt(|det B|)`. For the indefinite pair, each hyperbolic branch has Jacobian `1/(2√D)`; the exponential tails are paid by one original marginal at a time and the middle interval has logarithmic length. `Λ≥2/√D` converts the final logarithm to the displayed `16√D/|z-v|` scale. |
| 482–526 | quarter-power concentration and logarithmic moment | PASS | If no diagonal carries half the norm, random sign splitting produces a physical cross block with norm at least `L/4`. The determinant theorem then gives `|φ_R(t)|≤(4πe/(L|t|))^{1/4}`. Gaussian smoothing with `v=1/8` has exact coefficient `2^(5/8) π^(-1/4) e^(3/8) Γ(3/8)=3.99525936158...<16`. Layer cake yields exactly `4+4 log 16`. |
| 527–576 | disjoint volume, sampled nonsymmetric interpolation | PASS | Bordered determinants give the squared residual entry exactly. Sorting signs disappear after squaring. An extension can be counted at most `(r+1)^2` times; singular seeds being omitted changes equality only to the required inequality. `P` need not be symmetric and is never substituted as a random quadratic form. |
| 577–640 | completion, global/restricted ranks, spectral-to-volume contradiction, random cut | PASS | `R-P` is supported in rows `T` or columns `S`, giving global rank `≤3r`; on `L×L`, `R=P`, so restricted rank `≤r`; `D` vanishes on the seed. With `m=4k-3≥4r+1`, rank perturbation forces `r+1` large diagonal entries in `L`. The resulting `(r+1)×(r+1)` block of `R` is strictly diagonally dominant, contradicting restricted rank. The cut identity has probability `4^{-k}` per ordered disjoint minor. |
| 641–646 | no-pivot analytic consequences | PASS | The cut volume gives `Z_k^{-1/(2k)}≤160`; inserting `k=3,5` into the proved volume envelopes yields the stated `<200` half-potential and `<2400` density bounds. |
| 647–681 | square/logarithmic kernel integrals | PASS | Detailed derivation below. Both singular integrals are finite uniformly at the exact strengths used later. |
| 682–720 | pivot controls truncated half-potential | PASS | Scalar pivot uses the Schur count plus the one-direction logarithmic bound; definite pair is immediate; indefinite pair combines the moving log singularity with the uniform log-kernel integral. All three are integrated conditionally against original variables. |
| 721–790 | nine-direction half potential, main 17-direction proof, scaling, limitations | PASS | The full half-potential is at most `H+1`. A scalar pivot loses one spectral direction and still leaves nine for the `s_17` theorem; an indefinite pair loses two and leaves at least one for the log moment. The no-pivot branch uses order five. Scaling `Y=KX`, `A→A/s`, and `Q=(s/K^2) Qtilde` yields `10000 K^2/s`. The manuscript correctly does not claim the three-eigenvalue theorem or global continuity. |

## B12 focal derivations

### 1. Scalar square/profile is a valid measure inequality

For fixed conditioning variables, write

`Q = a (X_i-m)^2 + R`,  `a=A_ii !=0`.

If `r=sqrt(|z-R|/|a|)` is on the permitted side, the two inverse branches have derivatives of modulus `2|a|r`; hence

`p_{Q | X_-i}(z) = [f_i(m+r)+f_i(m-r)]/(2 sqrt(|a||z-R|))`

and therefore

`p_{Q | X_-i}(z) <= |a|^{-1/2}|z-R|^{-1/2}`.

Integrating this inequality against a nonnegative output test function and then using Tonelli gives the unconditional domination. This avoids any claim that `a(X_i-m)^2` is independent of the random remainder `R`.

### 2. Exact check of `J(d)`

For

`J(d)=∫_{-1}^1 |x|^{-1/2}|x-d|^{-1/2} dx`,

split into `|x|<=2|d|` and its complement. On the near part, after `x=|d|u`, reflection reduces to

`∫_{-2}^2 |u|^{-1/2}|u-1|^{-1/2} du`

which equals

`2 asinh(sqrt 2) + π + 2 acosh(sqrt 2) = 7.196771497190056... < 8`.

On the far part, `|x-d| >= |x|/2`, so the integrand is at most `sqrt(2)/|x|`; both tails contribute at most

`2 sqrt(2) log_+(1/(2|d|)) <= 3 log_+(1/|d|)`.

Thus the displayed `8+3 log_+(1/|d|)` bound is valid.

### 3. Exact check of the logarithmic kernel

Represent both nonnegative factors in

`∫_{-1}^1 |x|^{-1/2} log_+(1/|x-a|) dx`

by layer cake. Every superlevel set is an interval, centered at `0` for the first factor and at `a` for the second. For each pair of thresholds, the overlap is no greater than the overlap when the centers agree. Tonelli therefore reduces the supremum to `a=0`, where

`2∫_0^1 x^{-1/2} log(1/x) dx = 8`.

This proves the exact uniform kernel constant used by the hyperbolic-pivot branch.

### 4. Quarter-power coefficient and logarithmic layer cake

In the non-diagonal branch of Lemma `quarter`, the Gaussian smoothing integral with `v=1/8` has coefficient

`2^(5/8) π^(-1/4) e^(3/8) Γ(3/8) = 3.995259361581614...`,

so the manuscript's coarse constant `16` is safe. Integrating `min(1,16 e^{-u/4})` over `u>=0` gives exactly

`L0 = 4 + 4 log 16 = 15.09035488895912...`.

The resulting scalar-pivot truncated-half-potential bound is actually

`10(8+3L0)=532.7106466687737... < 560 < 600`,

and the indefinite-pair truncated bound is at most

`10(32+4 log16)+4/e = 432.3750666542770... < 444`.

The final indefinite-pair density constant in the normalized main proof is

`10(10+5 log16)+1/e = 238.9973155531605... < 251`.

## Exact multiplicity accounting inside the pivot branches

The published `17` is governed by the no-pivot order-five endpoint, not by the pivot analysis.

1. **Scalar pivot:** if `|A_ii|>=1/100` and already `s_10(A)>=1`, the one-coordinate Schur complement retains at least nine eigenvalues of modulus at least one. Proposition `nine` therefore applies, and

   `||p_Q||_∞ <= 10*601 = 6010`.

   Thus the scalar-pivot branch needs only ten large spectral directions.

2. **Definite pair pivot:** a definite physical pair with `|det B|>=1/100` directly gives conditional density at most `10π`; no extra spectral multiplicity is needed once that pivot exists.

3. **Indefinite pair pivot:** if `s_3(A)>=1` and an indefinite physical pair has determinant modulus at least `1/100`, its two-coordinate Schur complement retains at least one eigenvalue of modulus at least one. The quarter/log estimate therefore gives the normalized bound `<251`.

These are genuine lower-multiplicity branch theorems under the manuscript's full rough-law/affine hypotheses. They **do not lower the unconditional 17-eigenvalue theorem**, because the no-pivot branch remains.

## Why the present no-pivot architecture stops at 17

The algebraic proposition at order `k` needs `4k-3` large singular values. Taking `k=4` would reduce the spectral count to `13`, and the same random-cut argument would produce positive fourth crossing volume. But the determinant receiver then gives only

`|phi_Q(t)| <= min(1, u_4/|t|)`.

Its absolute Fourier integral diverges logarithmically. Therefore the current sequence

`no pivot -> V_4 -> random cut -> regularized determinant -> L1 Fourier inversion`

cannot prove a bounded density at multiplicity 13. This is an **architecture obstruction**, not a counterexample to a 13-eigenvalue theorem. Lowering the global threshold below 17 requires at least one genuinely new ingredient: an endpoint improvement beyond the pointwise `1/|t|` determinant envelope, an integrated cancellation estimate at order four, or a structural reduction which forces a pivot/other already-controlled branch before the no-pivot order-five receiver is needed.

## Package GAP

The root README and self-audit describe `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but direct reads of all four at fresh master returned 404. Consequently:

- the manuscript proof remains self-contained and was auditable;
- the numerical/reproducibility bundle advertised by the README is presently incomplete in the committed root;
- finite-check totals quoted by the self-audit were **not** treated as proof and were not independently reproduced from missing scripts in this run.

Recommended repair: restore those exact supplementary files with hashes matching the documented baseline, or amend README/AUDIT to state that they are intentionally external. Do not alter the pinned manuscript baseline merely to repair packaging.

## Final status

- 17-eigenvalue theorem: **PASS in this independent review**.
- Scalar-pivot branch: **PASS; closes already at multiplicity 10**.
- Definite-pair branch: **PASS once pivot exists**.
- Indefinite-pair branch: **PASS; closes already at multiplicity 3**.
- Full manuscript continuity: **UNCHECKED / not established by the pivot branches**.
- Supplementary reproducibility files: **GAP (missing from current root)**.
- Unrestricted three-eigenvalue QFORM conjecture: **OPEN**.
- Global independent-validation status: **not self-awarded; requires the owner-specified separate complete reviews**.

Next proof obligation for this slot: attack the order-four no-pivot endpoint (`s_13`) by an integrated/log-cancellation mechanism rather than trying to improve constants in the already-correct square/log pivot lemmas.
