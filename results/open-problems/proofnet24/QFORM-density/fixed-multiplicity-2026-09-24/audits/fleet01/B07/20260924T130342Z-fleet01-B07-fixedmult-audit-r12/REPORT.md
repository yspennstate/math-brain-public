# fleet01/B07 complete audit — QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

Run: `20260924T130342Z-fleet01-B07-fixedmult-audit-r12`  
Reviewer: `fleet01/B07`  
Starting lens: ordered disjoint minors, bordered determinant identities, singular deleted seeds, volume-sampling multiplicities, and random-cut expectations.  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and verdict

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Advertised and manifest source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Current `master` immediately before publication: `1b6a5a125347f5d07c79332ac9ab535d106de5fa`; the manuscript blob is unchanged from the baseline.

**Mathematical verdict: PASS for the written seventeen-eigenvalue theorem in this independent B07 review. Fatal mathematical gaps found: none.** I read all 790 source lines and reconstructed the full dependency chain rather than adopting the authoring self-audit or another worker verdict. The theorem reviewed is

`||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s`

for arbitrary dimension, arbitrary real symmetric `A` with `s_17(A)>=s>0`, arbitrary affine `b,c`, and independent arbitrary real coordinate laws with densities bounded by `K`.

This is one worker review. It is not a formal-verification certificate, not by itself an independent-validation release decision, and not the unrestricted three-eigenvalue theorem.

## Complete line-by-line audit map

| Source lines / label | Status | Independent reasoning | Downstream consequence |
|---|---|---|---|
| 1–83: preamble, `thm:main`, `cor:33`, architecture | PASS | Quantifiers preserve arbitrary dimension, signs, remaining spectrum, affine terms, and rough product densities. Singular values are zero-padded. The theorem asks only for an essentially bounded density. | Scope is coherent; 33 is an immediate stronger-hypothesis corollary. |
| 84–120: Fourier convention, Gaussian regularization, Plancherel/inversion | PASS | The `e^{itx}` convention gives the stated `2 pi` Plancherel factor and `1/(2 pi)` inversion factor. Gaussian smoothing and approximate-identity limits are legitimate. | Normalizations used later are consistent. |
| 121–160: power envelope and Riesz half-potential | PASS | The envelope integral is `2ap/(p-1)`. The gamma/Gaussian computation gives the stated `(2 pi)^(-1/2)` factor; for exponent `3/4` the weighted integral is exactly `12 sqrt(u)`. | Negative-half-moment branch is normalized correctly. |
| 161–217: perturbation/rank, Schur spectral count, diagonal dominance | PASS | Approximation numbers give both nonsymmetric singular-value inequalities. For invertible `A`, `S^{-1}` is the complementary principal block of `A^{-1}`; positive/negative compression bounds give the absolute-value count. The `A+epsilon I` passage handles singular `A`. Row diagonal dominance does not require symmetry. | Schur losses and nonsymmetric rank steps are valid. |
| 218–255: geometric rank-one Brascamp–Lieb | PASS | Heat-flow differentiation has the correct sign by the Parseval-frame contraction. Gaussian tails justify integration by parts; `sum c_i=d` gives the correct large-time normalization. Fatou and monotone truncation close rough nonnegative inputs. | The determinant theorem has a self-contained geometric input. |
| 256–282: product projections | PASS | The orthogonal completion is used only as a deterministic integration coordinate system. With `b_i=|w_i|^2`, the frame is exact. After dropping factors with `b_i=0`, `-b log b <= 1-b`; summing the RHS over all original rows gives `sum_i(1-b_i)=d`. Zero-`b` rows have zero contribution on the logarithmic LHS and only enlarge this RHS. | Bound `e^{d/2}` is valid; no rotated independence is asserted. |
| 283–301: scalar Fourier powers | PASS | `|hat f|<=1`, Plancherel gives integrability of all even powers used, and the density at zero is evaluated only after inversion yields a continuous version. Product-projection scaling with coefficient norm `sqrt(2m)` gives the stated constant. | Integrated Fourier input is valid for arbitrary cap-one densities. |
| 302–324: cross-block decoupling | PASS | Cauchy–Schwarz first removes the `I`-side phase; expansion with an independent `J` copy gives independent coordinate differences. Jensen produces the fourth-power version. No moments are used. | Arbitrary same-bank phases and affine terms are retained. |
| 325–373: regularized crossing determinant | PASS | The regularized vectors form an exact frame. The `d_i^{-d_i/2}` scaling cancels the `sqrt(d_i)` from the scalar Fourier-power estimate. `prod c_j^{-c_j/2}<=e^(theta/2)` and `alpha=(2 pi e)^2` cancel the remaining multiplier. Fourth roots give exponent `-1/8`. | Determinant characteristic-function bound is sound without rank/sign/leverage assumptions. |
| 374–400: crossing volumes and volume envelopes | PASS | Cauchy–Binet gives the coefficient `Z_k`. Retaining the order-`k` term gives exponent `k/4`; `k=5` is integrable and `k=3` is used only with the Riesz weight. | Fifth volume gives density; third volume gives half-potential, not direct density. |
| 401–434: scalar square and definite pair | PASS | The square map gives the inverse-square-root profile and interval preimage bound. The definite two-dimensional integral may be orthogonally parameterized because this is a deterministic coarea calculation, not a probabilistic independence claim. | Scalar and definite pivot receivers are valid. |
| 435–482: hyperbolic pair | PASS | The two level-set branches and Jacobian `1/(2 sqrt D)` are correct. The `(3/4) log 2` tail cutoff yields monotonicity; the density-cap/mass-one bathtub bound controls each tail; the middle length and `Lambda>=2/sqrt D` have the stated directions. | Indefinite pair logarithmic envelope is valid for rough independent coordinates. |
| 483–525: quarter-power concentration | PASS | If no diagonal is large, random signs produce a literal coordinate crossing with norm at least `L/4`. One singular factor in the determinant theorem gives `|t|^{-1/4}`; Gaussian smoothing gives the `rho^(1/4)` small-ball bound and layer cake gives `L0=4+4 log16`. | One surviving spectral direction pays the logarithmic singularity. |
| 526–544: ordered-disjoint volume and no-pivot entry bounds | PASS | `V_r` uses ordered disjoint `(S,T)` with increasing internal order. Under no pivot, `a_ij^2<eta^2+eta<1/49`, hence `|a_ij|<1/7`. | Correct bookkeeping currency and entry scale. |
| 545–564: `lem:sampling` | PASS | For nonsingular `B=A[S,T]`, row elimination gives `det A[S∪{ell},T∪{m}] = ±det(B)(A_lm-P_lm)`. Squaring removes sorting signs. A fixed ordered disjoint `(r+1)` extension has at most `(r+1)^2` deleted disjoint seeds. Singular deleted seeds have zero sampling weight even when the extension is nonsingular, so the aggregate relation is an inequality, exactly as stated. | The sampling estimate is valid; replacing it by an unconditional equality would be false. |
| 565–580: `lem:completion` | PASS | `P` matches all rows in `S` and columns in `T`; `E` is only the off-diagonal `L x L` residual; `D` is the residual diagonal on `L` and vanishes on the seed. `R-P` is supported in rows `T` or columns `S`, giving global rank `<=3r`, while `R[L,L]=P[L,L]` has rank `<=r`. | The two distinct rank bounds are both valid. |
| 581–619: `prop:volume` | PASS | The telescoping/first-zero argument finds a bad ratio. At `r=0`, `||off A||_F<1/80` contradicts `||A||>=1`. For `1<=r<=4`, `epsilon<=1/16`; after global rank loss `3r`, `m=4k-3>=4r+1` leaves `r+1` large diagonal entries of `D`, all in `L`. There `|R_ii|>=371/400`, each off-diagonal `<23/112`, and the worst row sum is `<23/28`; exact slack is `297/2800>0`. This contradicts `rank R[L,L]<=r`. | Spectral-to-volume conversion is sound. |
| 620–630: random coordinate cut | PASS | Each ordered disjoint `(S,T)` survives exactly when all `S` coordinates land in `I` and all `T` coordinates in `J`, probability `2^{-2k}=4^{-k}`. Linearity gives the exact expectation. | No missing orientation or multiplicity factor. |
| 631–645: no-pivot analytic consequences | PASS | `Z_k^{-1/(2k)}<=160`; the `k=3` half-potential constant is `12 sqrt(80e)<200`, while `k=5` gives density `800e<2400`. | Nine no-pivot directions pay a full half-potential; seventeen no-pivot directions pay density. |
| 646–674: truncated potential and kernel integrals | PASS | The near piece of `J(d)` is a scale-free beta/hyperbolic integral and the far piece is logarithmic. The log-kernel rearrangement is maximized by centered intervals and Tonelli gives `8`. | Pivot singularity averaging is justified. |
| 675–714: `prop:pivot-H` | PASS | Scalar pivot: Schur leaves one direction and the quarter-power logarithmic bound pays `J`. Definite pair: conditional density cap is uniform. Indefinite pair: hyperbolic envelope plus log-kernel and `sup D^{-1/2} log_+D=2/e` gives a uniform conditional bound. All are applied by nonnegative test functions/Tonelli. | Truncated half potential `<=600` is sound. |
| 715–724: `prop:nine` | PASS | Pivot/no-pivot is exhaustive. Outside distance one, the half-kernel is `<=1`, so the truncated bound becomes a full bound `<=601`. | Nine-direction full half-potential theorem closes. |
| 725–749: main theorem and scaling | PASS | No-pivot uses fifth volume. Scalar pivot loses one Schur direction, leaving more than the nine needed. Definite pair is immediate. Indefinite pair loses two but only one residual direction is needed for logarithms. For general `K,s`, `Y=KX` has cap-one coordinate densities and `Q=(s/K^2) Qtilde`; the density rescales exactly by `K^2/s`. | Candidate seventeen-direction theorem closes. |
| 750–790: threshold discussion, continuity scope, references | PASS mathematically; priority UNCHECKED | The rank accounting accurately describes the proof. Only the no-pivot Fourier branch is asserted continuous; the full theorem asserts essential boundedness. The two references are not used as black-box proof dependencies. | Comprehensive literature priority/novelty remains outside this mathematical audit. |

**No mathematical source line remains UNCHECKED in this B07 review.**

## Companion-file audit

The root now contains all requested textual support artifacts. `proof_map.csv` matches the theorem/lemma ranges in the 790-line source. `SOURCE_MANIFEST.json` pins the same baseline blob/SHA and explicitly states that the compiled PDF binary is not stored in this root. `verify.py` guards the pinned source SHA, checks the exact rank/support/bordered-minor and sampling identities on finite rational examples, and runs floating Schur/graph diagnostics. `checks.json` reports PASS with 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, exact diagonal-dominance slack `297/2800`, 240 floating Schur-threshold cases, and 30 graph-weight cases.

Status labels for these companions:

- `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`: **PASS as present/read metadata and review aids; they are not proof certificates.**
- `verify.py`: **PASS by code inspection as a finite diagnostic suite; its finite scope does not establish the theorem.**
- `checks.json`: **PASS as a recorded result matching the current suite/schema/source hash; actual re-execution of the suite in this connector-only run is UNCHECKED.**
- Compiled 16-page PDF hash/render claim in the manifest: **UNCHECKED in this run**, because the manifest states that binary is not stored in this GitHub root.
- Comprehensive novelty/priority search: **UNCHECKED** and not needed for correctness of the self-contained proof.

The root companion files were absent when an earlier B07 run queried them, but they are present now; this report supersedes that earlier repository-package observation. The mathematical manuscript blob itself has not changed.

## B07 focal reconstruction

For `lem:sampling`, fix ordered disjoint `r`-sets `S,T`, `B=A[S,T]` invertible, and `P=A[:,T]B^{-1}A[S,:]`. For `ell notin S`, `m notin T`, row elimination in the bordered matrix gives

`det A[S∪{ell},T∪{m}] = ± det(B)(A_lm-P_lm)`.

For the manuscript's disjoint `(r+1)` extensions, every fixed extension can arise from at most `(r+1)^2` row/column deletions. Crucially, a nonsingular extension may have singular deleted seeds; those seeds carry zero volume-sampling probability, so only `<=` is valid. This verifies both the sign convention and the zero-minor treatment.

The random-cut identity is exactly

`E Z_k(A[I,J]) = 4^{-k} V_k(A)`

because disjointness makes the `2k` color requirements independent. There is no extra factor for swapping `S,T`: `V_k` is already an ordered-pair sum and `Z_k(A[I,J])` uses that orientation.

## Review status

- Seventeen-eigenvalue candidate: **PASS in this complete fleet01/B07 review.**
- Fatal mathematical GAP/FALSE statements found: **none.**
- Mathematical UNCHECKED source lines: **none.**
- Companion computation re-execution and compiled binary render: **UNCHECKED as described above.**
- Full three-eigenvalue conjecture: **OPEN / not solved by this manuscript.**
- Independent-validation status: **not self-awarded**; the owner requires two genuinely separate complete reviews and a release synthesis.

A separate improvement artifact from this run gives a new exact overlap-multiplicity extension of `lem:sampling` and a nine-direction no-pivot funnel. It does not yet constitute an unconditional lowering of the theorem from seventeen to nine.
