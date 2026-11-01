# B20 independent release-gate audit — nine-eigenvalue / constant-400 candidate

Run: `20260924T152240Z-fleet01-B20-fixedmult-r11`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Audited source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
Pinned source commit from manifest/objective: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
Pinned source blob actually fetched on master: `19fb119877426b640b2c0dae19ec2f78a399fe11`
Pinned SHA-256 from manifest: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
Length: 955 lines.

## Verdict

**PASS (mathematical reconstruction).** I found no fatal mathematical gap in the 955-line source. The theorem proved by this source is, with the exact stated scope,

\[
s_9(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 400K^2/s,
\]

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, and arbitrary affine terms. No moment, iid, compact-support, log-concavity, exact-rank, or rotated-independence hypothesis is introduced.

This is **one independent end-to-end review of this exact revision**, not an independent-validation certificate. The source's own audit is not independent. Earlier B16/B19 review folders that predate the 14:54Z source revision do not certify this revision. A genuinely separate second complete reconstruction of the same blob is still required before independent-validation status.

The theorem asserts existence and an essential-supremum density bound. I do not upgrade the full theorem to global continuity; the no-pivot Fourier branch is continuous, while the pivot assembly only needs absolute continuity and the essential bound.

## End-to-end audit map

Every labeled definition/equation in `proof_map.csv` and all intervening proof text was checked. Status below is for the exact source ranges.

| Lines | Content | Status | Reconstruction / issue check |
|---|---|---|---|
| 1–80 | quantifiers, theorem, normalization, parameters | PASS | `s_9`, arbitrary affine terms and arbitrary product laws are preserved. Scaling later returns exactly `K^2/s`. The Borel representative convention repairs pointwise-cap uses. |
| 81–158 | Fourier/Plancherel/inversion, Gaussian smoothing, power envelope, Riesz half-potential | PASS | Fourier normalization gives the stated `2π` factors. The Gaussian identity and Riesz constant are consistent. For the `3/4` envelope the weighted integral is exactly `12 sqrt(u)`. |
| 159–213 | singular-value perturbation, Schur spectral counts, diagonal dominance | PASS | Rank perturbation is valid for nonsymmetric auxiliaries. The singular-Schur limiting argument preserves the threshold. No eigenvalue claim is made for nonsymmetric matrices. |
| 214–297 | heat-flow geometric BL, product projections, scalar Fourier powers | PASS | Heat-flow sign and large-/small-time limits are correct. Projection density is `<=e^{d/2}` without rotated independence. The positive-weight entropy sum is handled correctly. |
| 298–396 | decoupling, graph BL determinant estimate, crossing volumes | PASS | Difference coordinates remain independent cap-one. The regularized determinant normalization `α=(2πe)^2` and fourth-root exponent `-1/8` are correct. Cauchy–Binet volume identities are used with the right ordered/disjoint conventions. |
| 397–527 | grouped mollified-L2 receiver, row promotion, terminal hub, `E_3`/`E_2` receivers | PASS | Jensen is applied to mollified `L^2` norms before the limit; the pure `J` phase is discarded only after original `I` integration. Weighted Hölder is valid for the finite non-normalized kernel measure because the weights sum to one. The joint map density uses its exact Gram determinant. Hub variables are literal original coordinates; all hub-to-left couplings are retained. Constants independently reduce to `C3=3√2 e(9/2)^(1/6)<15` and `C2=8√e 2^(-1/8)<14`. |
| 528–662 | scalar square, definite pair, hyperbolic pair, quarter-power concentration | PASS | Coarea/Jacobian factors and output scaling were reconstructed. The indefinite pair tails use an original coordinate and no symmetry of the input laws. The quarter-power cut gives `||M||>=L/4`, and the Gaussian-smoothed coefficient is genuinely `<5`; layer cake gives `L0=4+4 log 5`. |
| 663–766 | disjoint volumes, volume-sampled interpolation, completion, spectral-to-volume, random cut | PASS | Border count is an inequality because singular seeds are excluded. `P` may be nonsymmetric. Completion has **global rank `<=3r`** but **restricted `L×L` rank `<=r`**; `D` is zero on the seed and `E` has zero diagonal. For `r=1,2` the exact diagonal-dominance margins are `1131/2200` and `51/2200`. This is the step producing `4k-3`, hence nine at `k=3`. |
| 767–860 | full-vs-truncated half potentials, pair potential, five-eigenvalue half potential, main theorem | PASS | The pair estimate scales as `D^(-1/4)`, not `D^(-1/2)`. The scalar-pivot argument distinguishes the truncated square-profile convolution from the full half potential and adds the far tail `<=1`. Main normalized branch bounds are `<375`, `<280`, `<320`, `<383`, `<80`, `<392.5`. General scaling is exactly `Q=(s/K^2) Q_tilde`. |
| 861–925 | overlap-one spectral-tail theorem and `s_8` corollary | PASS | `D` diagonal and `E` zero-diagonal are Frobenius-orthogonal. The best rank-`3r` tail inequality is valid for nonsymmetric matrices. Same-index bordered determinants give the exact `W/V_r` diagonal-error expectation. Singular seeds are not silently added. Thus `W_{2,1}^× >= 2V_2-9V_3` under `s_8>=1`. |
| 926–955 | threshold accounting, limitations, references | PASS for theorem scope; UNCHECKED for novelty | The text correctly says eight and three are not proved. The bibliography is not a proof dependency. I did not perform an exhaustive novelty/priority search in this run. |

## Specific mandatory stress checks

- **Nonsymmetric interpolation support — PASS.** The bordered determinant identity uses the ordered row/column seed, not symmetry. `P=A_{·,T}B^{-1}A_{S,·}` is allowed to be nonsymmetric.
- **Global rank `<=3r` versus restricted rank `<=r` — PASS.** The proof uses global `3r` only for the singular-value shift and restricted `r` only for the final `H subset L` invertibility contradiction.
- **`D` vanishing on the seed — PASS.** `D_{ii}=0` on `S∪T`; therefore all large `D` coordinates forced by the rank argument lie in `L`, where the restricted-rank contradiction is legitimate.
- **Spectral-to-volume conversion — PASS.** The exact parameter inequalities survive at `r=2`; the small positive `51/2200` margin is real.
- **Fourier normalization — PASS.** All `π`, `2π`, scale-`2t`, fourth-root and inversion constants are consistent.
- **Heat-flow / rough-law limits — PASS.** Compact-support heat-flow is extended by monotone approximation. Rough conditional laws are handled through domination, mollification, Tonelli and nonnegative test functions rather than exceptional point evaluation.
- **Schur counts — PASS.** A scalar pivot loses at most one target-scale eigenvalue and a two-coordinate pivot at most two; the singular matrix case is treated by a fixed-threshold perturbation.
- **Full versus truncated half potentials — PASS.** The pair potential is full. The scalar-pivot square profile is integrated on `|Q-a|<=1` and the complementary contribution `<=1` is explicitly restored.

## Constant checks

The repository checker records exact finite constants and 96 exact interpolation seeds plus eight exact aggregate-overlap comparisons. I independently reconstructed the identities used in the proof; the finite checker is supporting evidence, not proof. In particular:

- `p+d^2 = 13/1600 < 1/121`;
- `r=1` margin `=1131/2200`;
- `r=2` margin `=51/2200`;
- `C3 = 14.818337...`, hence no-pivot density `25 C3 = 370.458... <375`;
- scalar/scalar branch `=360.847... <383`;
- indefinite pair branch `=384.574... <392.5 <400`;
- pair full half-potential unit-scale estimate `12+5 log 2 =15.4657...<16`.

## Release status

Mathematics of the candidate: **PASS in this review**.

Independent-validation gate: **OPEN** until a second genuinely separate full review of blob `19fb119877426b640b2c0dae19ec2f78a399fe11` is verified. Do not use older-version PASS labels to fill this requirement.

Eight-eigenvalue theorem: **OPEN**. The overlap theorem is valid supporting algebra, not an analytic receiver for the shared original coordinate.

Three-eigenvalue theorem: **OPEN**.

Global continuity of the assembled nine-eigenvalue theorem: **not claimed**.
