# account01/B01 complete audit — QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

Run: `20260924T120640Z-account01-B01-FIXMULT-auto11`  
Reviewer: `account01/B01`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256 (owner manifest/objective): `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Current `master` observed during this review: `95e6c5265050f3f3fd418733517b6e126838164a`; the manuscript blob on that snapshot is still exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**PASS on the complete 790-line mathematical proof of the 17-eigenvalue candidate.** I found no fatal mathematical defect and no theorem-changing gap. This is one complete independent B01 review; it is not a self-awarded independent-validation certificate and it does not solve the unrestricted three-eigenvalue conjecture.

The precise theorem audited is: for independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A`, arbitrary `b,c`, and `s_17(A)>=s>0`, the law of `X^T A X+b^T X+c` has an essentially bounded density with

`||p||_infinity <= 10000 K^2/s`.

The global conclusion in this manuscript is **essential boundedness**, not continuity. The no-pivot Fourier branch produces a continuous density because its characteristic function is integrable; the pivot branches are proved by domination of measures/densities and do not establish continuity for arbitrary rough input densities.

## End-to-end line audit

| Source lines / statement | Status | Independent check and exact reasoning | Downstream impact |
|---|---|---|---|
| 1–83: definitions, theorem, corollary, normalization architecture | PASS | Quantifiers retain arbitrary independent cap-`K` densities, arbitrary dimension/signature/remaining spectrum, symmetric `A`, and arbitrary affine `b,c`. For `n<17`, `s_17=0` by the stated zero-padding convention, so the hypothesis is simply unavailable. The proof correctly distinguishes essential density from continuity. | Main statement is internally coherent and has the advertised scope. |
| 84–151: Fourier convention, Gaussian inversion, power envelope, Riesz half-potential | PASS | With `hat f(t)=int exp(itx)f(x)dx`, Plancherel has factor `2pi`, inversion has `1/(2pi)`, and the Gaussian formula is consistent. The gamma/Gaussian calculation gives the coefficient `(2pi)^(-1/2)` in the half-potential inequality. The envelope integral is `2ap/(p-1)`. | All Fourier constants used downstream are normalized consistently. |
| 152–220: singular-value perturbation, Schur spectral count, diagonal dominance | PASS | The approximation-number proof works for nonsymmetric auxiliaries. For an invertible pivot, the complementary block of `A^{-1}` is `S^{-1}`; positive and negative principal-compression interlacing gives the absolute-eigenvalue count, and the `A+eps I` limit correctly covers singular `A`. Strict row diagonal dominance needs no symmetry. | All later Schur spectral counts and nonsymmetric rank arguments have valid inputs. |
| 221–300: geometric rank-one BL, product projections, scalar Fourier powers | PASS | Heat flow has `partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` by the frame contraction. Trace gives `sum c_i=d`; the large-time Gaussian normalization is correct. Product projection uses an orthogonal deterministic change only inside an integral and never asserts rotated independence. The scalar Fourier-power argument uses a genuine sum of independent differences and the continuous Fourier-inversion version at zero. | The projection and scalar `L^p` bounds are proved inside the manuscript; no external theorem is needed for the constants used. |
| 301–400: decoupling, regularized crossing determinant, crossing volumes | PASS | Both independent-copy inequalities preserve product provenance. In the graph-BL step the weights form the exact regularized frame, the one-dimensional scale factors are correct, and `alpha=(2pi e)^2` cancels the nondeterminant multiplier. Taking the fourth root gives determinant exponent `-1/8`. Retaining order `k` gives `|t|^{-k/4}`; `k=5` is integrable and `k=3` is used only with the Riesz `|t|^{-1/2}` weight. | The no-pivot density and half-potential receivers are supported exactly at the stated crossing orders. |
| 401–500: scalar square, definite pair, hyperbolic pair | PASS | Scalar change of variables gives the `|z-v|^{-1/2}` profile and the interval-preimage bound. Definite-pair polar coordinates give `pi M/sqrt(|det B|)`. For the indefinite pair, the hyperbolic level-set Jacobian is `1/(2sqrt D)`; on each tail a physical coordinate is monotone after the stated cutoff, and the cap-one/mass-one bound controls the `1/|y|` integral. The final logarithmic envelope and `16sqrt D` scale are in the correct direction. | Pair pivots are controlled without any post-rotation independence assumption. |
| 501–535: quarter-power concentration | PASS | If no large diagonal exists, the random sign cut extracts a physical cross block with norm at least `L/4`; retaining its largest singular factor in the determinant theorem gives the required `|t|^{-1/4}` envelope. Gaussian smoothing gives the `rho^{1/4}` small-ball estimate, then layer cake gives the log potential. | The one-surviving-direction logarithmic input used in pivot branches is valid for rough laws. |
| 536–600: `V_r`, no-pivot entry bounds, sampled interpolation, completion | PASS | The no-pivot `|a_ij|<1/7` estimate follows from the principal determinant bound. Volume sampling uses the bordered determinant identity; each ordered disjoint `(r+1)` pair is counted at most `(r+1)^2`, with singular seeds only lowering the count. For `P=A[:,T]B^{-1}A[S,:]`, one has exactly `P[S,:]=A[S,:]` and `P[:,T]=A[:,T]`. With the defined `D,E,R`, `R[L,L]=P[L,L]`; `R-P` is supported only in rows `T` or columns `S`, so `rank R<=3r`, while `rank R[L,L]<=r`. `D` vanishes on the seed and `diag E=0`. | The most sensitive nonsymmetric interpolation/support claims pass. |
| 601–630: spectral-to-volume proposition | PASS | A bad ratio gives `eps<= (r+1)/80<=1/16`. With `m=4k-3` and `r<=k-1`, `m>=4r+1`; after the global rank-`3r` loss, at least `r+1` entries of `D` have modulus `>=1-eps`, all in `L`. On those coordinates, `|R_ii|>=371/400` while each off-diagonal is `<1/7+1/16`; for `r<=4`, the row sum is `<23/28`. The exact dominance slack is `371/400-23/28=297/2800>0`, so `R[H,H]` has rank `r+1`, contradicting `rank R[L,L]<=r`. The `r=0` branch also contradicts `||A||>=1`. | The conversion `4k-3` spectral directions -> order-`k` disjoint volume is sound for `k<=5`. |
| 631–660: random cut and no-pivot consequences | PASS | Each ordered disjoint minor survives a fair cut with probability `4^{-k}`. Combining with the volume envelope gives `12sqrt(80e)<200` for `k=3` and `800e<2400` for `k=5`. | The nine-direction full half-potential and seventeen-direction no-pivot density branches close. |
| 661–730: truncated potential, singular kernels, pivot-H | PASS | The two singular-kernel estimates are valid by the displayed region split/layer-cake argument. Scalar pivot uses the Schur remainder's surviving direction and integrates the exact square profile. Definite and indefinite pairs are conditioned only on original coordinates. The truncated/full distinction is kept explicit, and the stated numerical ceilings are conservative. | The pivot branch gets a uniform truncated half-potential bound `<=600`. |
| 731–790: nine-direction proposition, main theorem, scaling, limitations | PASS | Pivot vs no-pivot is exhaustive. A scalar pivot under `s_17>=1` leaves at least 16 Schur directions and therefore enough for the proved nine-direction half-potential bound, yielding `6010`. A definite pair gives `<40`. An indefinite pair leaves at least 15 directions, while only one surviving direction is needed for the logarithmic potential, yielding `<251`. For general `K,s`, setting `Y=KX` makes every density cap at most one, applying the normalized theorem to `A/s`, and using `Q=(s/K^2) Qtilde` gives exactly `10000 K^2/s`. | The complete candidate theorem closes with the advertised constant. |
| Bibliography metadata / classical antecedent wording | PASS for metadata; UNCHECKED for priority completeness | The two cited titles/authors/arXiv identifiers match the stated BCCT and Rudelson–Vershynin sources. I did not conduct a comprehensive novelty/priority search. These citations are attribution only, not proof dependencies. | No mathematical dependency impact. |
| `README.md` and `AUDIT.md` theorem/source descriptions | PASS with package GAP below | Their mathematical description matches the pinned manuscript and source hash. | Documentation is broadly consistent with the proof. |
| `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json` advertised in README/objective | **GAP (missing package artifacts)** | At the pinned source commit the manuscript root contains only `manuscript.tex`; on current `master` the root contains `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, `improvements/`. Direct fetches of all four advertised files returned not found. Thus the finite-check claims cannot be rerun from the currently published root. | Reproducibility/release-package gap only. It does **not** open a mathematical dependency gap because the specialized proof is self-contained in `manuscript.tex`. |

No source line of the 790-line manuscript is left mathematically UNCHECKED in this review. The only UNCHECKED item relevant to the package is the advertised external finite-check execution, because its scripts/results are absent from the repository root.

## B01 lens: theorem quantifiers, scaling, and dependency closure

The normalized proof is genuinely dimension-free and law-uniform under only the density cap. No moments, bounded support, log-concavity, connected support, identical laws, Gaussianity, or independence after a deterministic rotation are introduced. Every conditioning step is on original coordinate blocks. The nonsymmetric matrices `P,R,E` are deterministic algebraic auxiliaries used only in singular-value/rank estimates; they are never substituted as quadratic coefficient matrices for the random form.

The scaling is exact. If `f_X<=K`, then `Y=KX` has coordinate densities bounded by one. Define

`Qtilde = Y^T(A/s)Y + (K/s)b^T Y + (K^2/s)c`.

Then `s_17(A/s)>=1` and `Q=(s/K^2)Qtilde`. Therefore a normalized density cap `10^4` becomes `10^4 K^2/s`, with no hidden dependence on `n`, `b`, `c`, signature, or the remaining spectrum.

The specialized dependency chain is closed inside the manuscript:

`Fourier/Gaussian/Riesz -> geometric BL + product projection + scalar Fourier powers -> decoupling/determinant -> crossing-volume envelopes -> sampled interpolation/rank contradiction -> no-pivot receivers`,

and independently

`scalar/definite/hyperbolic coordinate changes + one-direction concentration -> pivot half-potential -> nine-direction half-potential -> main scalar-pivot branch`.

The two bibliographic citations are explanatory antecedents only; none of their theorems is invoked as an unproved black box at a required constant.

## Threshold-lowering audit

No valid full-theorem reduction below 17 is established in this run.

Within the manuscript's present mechanism, 17 is the first closed threshold. The fourth-power decoupling/determinant receiver gives order-`k` decay `|t|^{-k/4}`, so direct absolute Fourier inversion requires `k>4`, hence `k=5`. In the bad-volume interpolation branch, the worst seed order is `r=k-1`; the global rank loss is `3r`, while the restricted block has rank at most `r`, so the contradiction needs at least `r+1` large diagonal directions after the global loss. This requires

`m >= 3r+(r+1)=4r+1=4k-3`.

At `k=5`, this is `m>=17`.

The exact obstruction to `s_16` occurs at the terminal `r=4` chamber. Global rank `<=12` can leave only four large diagonal directions; a diagonally dominant `4x4` block has rank four, which is compatible with the restricted bound `rank R[L,L]<=4`. No choice of smaller `eta` or `kappa` changes this rank saturation. Thus a `17 -> 16` theorem cannot be obtained by numerical tightening of the existing contradiction.

There is also no automatic rescue from the factorization on a saturated four-set `H`:

`P[H,H] = A[H,T] B^{-1} A[S,H]`,

so when all three square matrices are invertible,

`det P[H,H] = det A[H,T] det A[S,H] / det B`.

This identity gives invertibility of the two physical cross matrices, but not a dimension-free lower bound on either determinant because the sampled seed determinant `det B` may be arbitrarily small. Hence it does not by itself provide the quantitative cross-volume currency needed for a 16-eigenvalue full theorem.

The next genuine threshold obligation is therefore: close the `r=4` terminal saturation chamber with a new quantitative structural input, or obtain an endpoint receiver strong enough to turn order-four aggregate crossing volume into a bounded-density estimate without adding hypotheses.

## Review status and scope

- Mathematical candidate `s_17`: **PASS in this complete B01 review**.
- Fatal mathematical defects found: **none**.
- Package/reproducibility defect: **GAP — four advertised supplementary files are absent**.
- Threshold lowered below 17 in this run: **no**.
- Full three-eigenvalue conjecture: **OPEN / not addressed by this candidate theorem**.
- Independent-validation gate: **not self-awarded**; owner requires two genuinely separate full reviews plus release synthesis.
- Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**; repository transport/readback is not evidence of native learned-memory ingestion.

## Privacy / write scope

Only the authorized mathematical manuscript, its audit artifacts, and the current objective/protocol were read. This review contains no credentials, scheduler IDs, unrelated personal/company/financial material, or private-source excerpts beyond the scoped mathematical proof. No repository-local privacy checker was exposed through the connector; I therefore performed a manual changed-file scope review before writing this artifact. No task, schedule, notification, permission, visibility, account binding, or public-release state was changed.
