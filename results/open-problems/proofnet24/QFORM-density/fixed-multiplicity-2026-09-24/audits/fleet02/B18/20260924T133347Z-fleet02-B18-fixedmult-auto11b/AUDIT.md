# fleet02/B18 full fixed-multiplicity audit — auto11b

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Pins and verdict

I reread the complete fixed-multiplicity package and the full 790-line manuscript. The mathematical baseline audited is immutable source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`. At the pre-write refresh, `master` was `6f66b0489379ff8a5f183465eaf465571c427a66`; `manuscript.tex` still had the same immutable source content. The current package files `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md` were also read.

**Baseline mathematical verdict: PASS.** I found no FALSE manuscript statement and no unresolved mathematical GAP in the pinned 17-direction theorem. This is an independent worker review, not formal verification or a release certificate. The unrestricted three-eigenvalue QFORM conjecture is not claimed solved.

**Package/reproducibility verdict: PASS with one explicitly historical item.** The current `verify.py/checks.json` suite is a new delivery suite and does not reproduce the older test counts quoted in the historical author self-audit. The package now says so explicitly. The compiled PDF binary and its visual-inspection claim remain **UNCHECKED in this run** because the binary is not stored in this GitHub root; neither is a premise of the proof.

## Complete source-line coverage

Every manuscript line 1--790 was read. The following ledger is exhaustive at source-range level; the proof-map labels are only navigation aids, not substitutes for reading.

| Lines | Object | Status | Independent check / impact |
|---|---|---|---|
| 1--46 | preamble, abstract, definitions | PASS | theorem scope and terminology agree with the later proof; no hidden regularity assumption |
| 47--61 | `thm:main`, `cor:33` | PASS | exact quantifiers are arbitrary independent density caps, arbitrary symmetric `A`, arbitrary affine terms; corollary follows from singular-value monotonicity |
| 62--90 | architecture, parameters, conventions | PASS | `eta=1/100`, `kappa=1/6400`; no post-rotation independence asserted |
| 91--160 | `lem:fourier`, `lem:envelope`, `lem:riesz` | PASS | Fourier factors `2pi`, `1/(2pi)`, Gaussian normalization and half-Riesz constant rederived |
| 161--217 | `lem:rank`, `lem:schur`, `lem:dd` | PASS | nonsymmetric singular-value perturbation is valid; Schur count checked also in singular limit; strict diagonal dominance use correct |
| 218--282 | `thm:bl`, `lem:projection` | PASS | heat-flow sign/frame identity and rough-law limiting step valid; projection argument uses deterministic orthogonal geometry only |
| 283--301 | `lem:scalar-fourier` | PASS | even-power inversion and `2pi sqrt(2e/p)` constant checked |
| 302--324 | `lem:decoupling` | PASS | independent copy introduced only on original product coordinates; phase terms removed only after modulus |
| 325--400 | `thm:determinant`, `cor:vol-fourier` | PASS | regularizer `alpha=(2pi e)^2`, graph weights, entropy factors, determinant exponent `-1/8`, Cauchy--Binet and order-3/order-5 exponents checked |
| 401--525 | `lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter` | PASS | inverse branches, hyperbolic Jacobian/tails, random coordinate cut and quarter-power constant checked; no rotated-law independence |
| 526--645 | pivot-volume definition, `lem:sampling`, `lem:completion`, `prop:volume`, `lem:cut`, `cor:no-pivot` | PASS | bordered-minor identity, nonsymmetric interpolation, global rank `<=3r`, restricted rank `<=r`, zero seed diagonal, diagonal-dominance contradiction and fair-cut factor all checked |
| 646--724 | `lem:kernels`, `prop:pivot-H`, `prop:nine` | PASS | singular kernels integrable with stated constants; full versus truncated half potentials kept distinct |
| 725--749 | main proof | PASS | all four branches close; largest branch `6010<10000`; Schur-remnant hypotheses match invoked lemmas |
| 750--790 | threshold discussion, remarks, bibliography | PASS | correctly avoids optimality/novelty/full-three claims; cited works are antecedents, not hidden proof dependencies |

No manuscript range remains UNCHECKED mathematically.

## Sensitive points rederived

1. **Nonsymmetric interpolation.** For sampled disjoint `S,T`, `P=A[:,T] A[S,T]^{-1} A[S,:]` has rank at most `r` and exactly interpolates rows `S` and columns `T`. In `A=D+R+E`, `R[L,L]=P[L,L]` has rank at most `r`, whereas globally `R-P` is supported in rows `T` or columns `S`, so `rank R<=3r`. `D` vanishes on the seed and `E` has zero diagonal. No symmetry of `P,R,E` is needed or claimed.

2. **Spectral-to-volume conversion.** If a sampled ratio is small, `||E||_F<=1/16`. Nonsymmetric rank perturbation plus `rank R<=3r` forces at least `r+1` large diagonal entries of `D`; because `D` vanishes on the seed these lie in `L`. Their `(r+1)` block contradicts `rank R[L,L]<=r` by strict diagonal dominance. The arithmetic slack is `371/400-23/28=297/2800>0`.

3. **Fourier endpoint distinction.** Order five gives exponent `5/4>1` and direct density inversion. Order three gives exponent `3/4`; it is used with the additional `|t|^{-1/2}` Riesz weight and is never misreported as an `L^1` characteristic-function bound.

4. **Pivots.** Completing a scalar or two-coordinate pivot is conditional on literal original coordinates. Deterministic rotations appear only in level-set integration. The definite-pair lemma needs only a joint density cap; the hyperbolic proof evaluates the original product density and uses a literal coordinate cap for its tail.

5. **Scaling.** For `Y=KX` and the normalized polynomial `Qtilde`, `Q=(s/K^2)Qtilde`; hence any normalized constant `C` rescales to `C K^2/s` exactly.

## Primary-source prior-art verification

The manuscript cites Bennett--Carbery--Christ--Tao and Rudelson--Vershynin as classical antecedents but proves all constants it actually needs.

* Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492 / IMRN 2015, works with independent real coordinates and bounded one-dimensional densities. Its scalar theorem uses only that density cap and gives the sharp `sqrt(2)K` normalized linear-form bound; its projection theorem gives an absolute-constant `d`-dimensional projection-density bound. No moments, bounded support, iid, centering, symmetry or log-concavity are assumed. The manuscript does **not** import RV's unspecified multidimensional constant: its explicit `e^{d/2}` projection bound is proved internally.
* Bennett--Carbery--Christ--Tao, arXiv:math/0505065, proves the geometric Brascamp--Lieb inequality and explicitly describes heat-flow/monotonicity methods; the paper itself identifies the geometric inequality as Ball's antecedent. This matches the manuscript's broad historical sentence. The specialized rank-one constant-one inequality used here is nevertheless proved inside the manuscript, so no external hypothesis is silently imported.

A targeted literature search also located special-law/special-form quadratic-density work, but nothing searched was used as a novelty certificate. Search misses are not evidence of priority.

## Package files

- `README.md`: **PASS** for theorem scope, pins and cautionary release language.
- `SOURCE_MANIFEST.json`: **PASS** for source blob/hash/size and explicit distinction between current and historical finite suites; PDF binary assertions **UNCHECKED** here.
- root `AUDIT.md`: **PASS as historical self-report**, not independent evidence. Its old finite-test counts are not reproduced by the current checker and the package now says so.
- `proof_map.csv`: **PASS** as a correct navigation map for all labeled statements/proofs.
- `verify.py`: **PASS on static inspection**; it pins the source hash and checks the sensitive interpolation/rank identities while explicitly disclaiming proof status.
- `checks.json`: **PASS for consistency with the current checker schema/result**. Exact dynamic re-execution of the repository script was not performed in this connector-only run; the mathematical identities and key constants above were recomputed independently.

## Baseline consequence

The pinned manuscript's 17-eigenvalue theorem is mathematically PASS in this review. The live repository now also contains a complete lower-threshold candidate at nine spectral directions; that improvement is audited separately in this run rather than being folded into or misrepresented as the unchanged 17-direction manuscript.
