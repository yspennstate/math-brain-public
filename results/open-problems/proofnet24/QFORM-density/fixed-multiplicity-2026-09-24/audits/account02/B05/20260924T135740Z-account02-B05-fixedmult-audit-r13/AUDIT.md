# account02/B05 r13 — full fixed-multiplicity audit, product-projection and exceptional-slice lens

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T135740Z-account02-B05-fixedmult-audit-r13`  
Fresh master observed before delivery: `fb1c176f3e981f3e59465f58ce0d0c817e54244d`.  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**PASS for the complete written 17-eigenvalue baseline in this independent B05 reconstruction.** I found no mathematical `FALSE` item and no theorem-breaking `GAP`. Every source line 1--790 was read. The current package also contains `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`; the earlier missing-support-file reproducibility gap is therefore resolved at the current master. The support checker is correctly described as finite evidence, not proof.

This report does not claim formal verification, journal peer review, or the unrestricted three-eigenvalue QFORM theorem. The theorem audited here is exactly: independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0` imply `||p_Q||_infinity <= 10000 K^2/s`.

## Complete source ledger

Every range below is `PASS` unless explicitly stated otherwise. `Next obligation` is `none for the 17-direction baseline` except where the row itself names a lower-threshold task.

| Source lines | Label / content | Status | Independent check, impact, next obligation |
|---|---|---|---|
| 1--46 | preamble, abstract, conventions | PASS | Quantifiers in the abstract match the theorem; no hidden regularity, support, sign, or moment hypothesis. |
| 47--57 | `thm:main` | PASS | Statement is unambiguous; `s_17` means the seventeenth singular value; affine terms arbitrary. |
| 59--81 | `cor:33`, architecture, parameters | PASS | `s_17>=s_33`; pivot/no-pivot plan and counts `9=4*3-3`, `17=4*5-3` match later proofs. |
| 83--90 | Fourier conventions / Gaussian | PASS | Transform convention is used consistently with the `2pi` Plancherel and inversion constants. |
| 91--120 | `lem:fourier` | PASS | Gaussian regularization justifies Plancherel for `L1 cap L2`, inversion, and Gaussian identity; all Fubini steps have an integrable Gaussian or `L2` control. |
| 122--130 | `lem:envelope` | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)` and inversion gives the stated constant. |
| 132--160 | `lem:riesz` | PASS | Gamma representation, two Tonelli steps, and substitution give the coefficient `1/sqrt(2pi)`; the `3/4` envelope yields `12 sqrt(u/(2pi))`. |
| 161--168 | norm and spectral-count definitions | PASS | No ambiguity relevant downstream. |
| 169--181 | `lem:rank` | PASS | Approximation-number proof is valid for nonsymmetric matrices; rank shift direction used later is correct. |
| 183--207 | `lem:schur` | PASS | Invertible case via inverse principal compression is sound. Singular case uses `A+eps I` at threshold `t-|eps|` and eigenvalue continuity; this avoids a fixed-threshold discontinuity error. |
| 209--217 | `lem:dd` | PASS | Standard maximum-coordinate proof; symmetry is not needed. |
| 221--255 | `thm:bl` | PASS | Heat-flow derivative has the correct nonnegative quadratic form from the frame identity. Compact-support Gaussian domination justifies differentiation/integration by parts; large-time limit and small-time Fatou are valid; monotone truncation reaches arbitrary nonnegative integrable factors. |
| 258--282 | `lem:projection` | PASS | Reconstructed in detail below. It uses only the original product density plus Fubini and geometric BL, never rotated-coordinate independence. |
| 284--301 | `lem:scalar-fourier` | PASS | For `m=floor(p/2)`, `2m<=p` and `|hat f|<=1` give the correct comparison. The `m`-difference density at zero is bounded by the projection lemma after Fourier inversion supplies a continuous version. |
| 302--309 | cross-form setup | PASS | `F,G` only measurable/finite a.s.; affine terms are allowed. |
| 310--324 | `lem:decoupling` | PASS | Cauchy--Schwarz, independent copy, then integration in original independent coordinates produce the physical-coordinate Fourier product. No moment assumption. |
| 326--373 | `thm:determinant` | PASS | Frame weights `c_j,d_i`, trace identity, BL scales, scalar Fourier powers, entropy-like `-c log c` bound, and fourth-root exponent all check; final determinant exponent is `-1/8`. |
| 374--385 | crossing volumes / Cauchy--Binet | PASS | `Z_k` is the elementary symmetric polynomial in squared singular values and the determinant generating function is correct. |
| 386--400 | `cor:vol-fourier` | PASS | Retaining the order-`k` determinant term gives exponent `k/4`; order 5 is integrable and order 3 is exactly sufficient with the half-Riesz weight. |
| 404--414 | `lem:square` | PASS | Two inverse branches give the `|z-v|^-1/2` profile; interval-preimage length bound is correct. |
| 415--421 | conditional square profile | PASS | This is a **measure domination** statement obtained conditionally and then by Tonelli; it does not assert independence of the square and Schur remainder. |
| 423--434 | `lem:definite` | PASS | Completing the square and deterministic orthogonal diagonalization are inside a two-dimensional integral; the joint density cap, not post-rotation independence, is used. Jacobian gives `pi M/sqrt(|det B|)`. |
| 437--482 | `lem:hyperbola` | PASS | Reconstructed in detail below. The critical fiber really can be singular, but the proof uses an a.e. envelope plus nonnegative-test-function/Tonelli conditioning, which is sufficient. |
| 485--525 | `lem:quarter` | PASS | Diagonal branch and random-sign off-diagonal branch cover all cases. The determinant receiver gives the quarter-power characteristic bound; Gaussian smoothing and layer cake yield atomlessness and the logarithmic potential. |
| 528--544 | `def:pivot-volume`, no-pivot entry bound | PASS | Ordered disjoint-minor convention is consistent. No pivot gives `|a_ij|<1/7` from `eta=1/100`. |
| 545--564 | `lem:sampling` | PASS | Bordered determinant identity is exact. Singular seeds may have nonsingular extensions, hence the proof correctly uses an inequality rather than an equality in the counting step. |
| 566--580 | `lem:completion` | PASS | `D` vanishes on the seed; `E` has zero diagonal; `R-P` is supported on rows `T` or columns `S`; therefore global `rank R<=3r` while `rank R[L,L]<=r`. No symmetry of auxiliaries is assumed. |
| 582--619 | `prop:volume` | PASS | Telescoping ratio, `r=0` norm contradiction, nonsymmetric singular-value perturbation, and diagonal-dominance contradiction all check. With `r<=4`, `eps<=1/16`, diagonal `>=371/400`, row sum `<23/28`; restricted rank is contradicted. |
| 621--630 | `lem:cut` | PASS | Each ordered disjoint pair is separated in the prescribed orientation with probability `4^-k`; expectation identity is exact. |
| 632--645 | `cor:no-pivot` | PASS | `k=3` gives full half-potential `<200`; `k=5` gives density `<2400`; arbitrary affine terms remain inside the cross-form setup. |
| 646--653 | truncated half-potential definition | PASS | Atom convention and truncation are explicit. |
| 654--674 | `lem:kernels` | PASS | Both singular kernels are integrable at the relevant collisions. The logarithmic overlap rearrangement is valid. |
| 676--714 | `prop:pivot-H` | PASS | Scalar, definite-pair, and indefinite-pair branches each satisfy the exact pivot hypotheses. Scalar branch uses a surviving Schur eigenvalue only for the logarithmic potential. Indefinite branch averages a singular envelope without choosing exceptional slice values. |
| 716--724 | `prop:nine` | PASS | Pivot branch supplies truncated half-potential; no-pivot branch supplies full half-potential; the outside-unit tail contributes at most one. |
| 726--749 | proof of `thm:main` / scaling | PASS | Schur counts are 16 after scalar pivot and 15 after pair pivot. The scalar branch uses `prop:nine`; definite and indefinite pair branches are uniform in induced affine terms. Scaling `Y=KX` gives exactly `K^2/s`. |
| 750--790 | dependency table, limitations, remarks, bibliography | PASS | Limitations accurately state that multiplicity three is not proved and continuity is not claimed in pivot branches. |

No mathematical source range remains `UNCHECKED` in this run.

## B05 reconstruction: product-projection density

Let `U in R^{n x d}` have orthonormal columns and complete it to `(U,W)` orthogonal. With `w_i^T` the rows of `W`, Fubini gives, for a bounded-everywhere version of each original density,

`p(y)=int prod_i f_i((Uy)_i+w_i dot z) dz`.

Put `b_i=||w_i||^2=1-||U^T e_i||^2`. If `b_i=0`, the factor is at most one and may be discarded. Otherwise `v_i=w_i/sqrt(b_i)` and

`sum_i b_i v_i v_i^T=I_{n-d}`.

Apply the proved geometric BL inequality to

`h_i(t)=f_i((Uy)_i+sqrt(b_i)t)^(1/b_i)`.

Because `0<=f_i<=1` and `1/b_i>=1`, `f_i^(1/b_i)<=f_i`, so

`int h_i <= b_i^(-1/2)`.

Therefore

`p(y)<=prod_{b_i>0} b_i^(-b_i/2)`.

Using the continuous convention `-b log b=0` at `b=0` and `-b log b<=1-b`,

`log p(y)<=1/2 sum_i(1-b_i)=d/2`,

because `sum_i ||U^T e_i||^2=tr(U^TU)=d`. Hence `||p_{U^TX}||_infinity<=e^(d/2)`. For a full-row-rank linear map `L`, polar factorization gives the useful corollary

`||p_{LX}||_infinity <= e^(d/2)/sqrt(det(LL^T))`.

This corollary is the precise product-projection input used in the current nine-direction replacement review. It is a density statement for a linear image of the original product law; it is **not** a statement that the projected coordinates are independent.

## B05 reconstruction: exceptional slices in the hyperbolic pair

For an indefinite `2 x 2` quadratic part, the level-set parametrization has Jacobian `1/(2 sqrt D)`. On each hyperbolic branch, writing the physical-coordinate vector as `u e^t+w e^-t`, one original coordinate has `|u_i|>=rho_0/sqrt2`; after the stated cutoff it is monotone and its derivative is at least one third of its magnitude. The cap-one density and unit mass then make each tail integrable. The middle interval has finite length, giving

`p_q(v+delta)<=D^-1/2(6+log_+(16 sqrt D/|delta|))`

for a.e. `delta!=0`.

The critical level `delta=0` may have a true logarithmic singularity; the proof does not need a pointwise value there. Conditional applications are made against nonnegative output test functions and averaged by Tonelli, so conditioning-dependent critical values do not require a common exceptional set. The same measure-level reasoning validates the scalar square profile.

## Counterexamples to invalid shortcuts

These are cap-one product laws, so they stress exactly the theorem's admissible class.

1. **Unconditional projection cap does not survive conditioning.** Let `X1,X2` be independent uniform on `[-1/2,1/2]` and set `Y=(X1+X2)/sqrt2`, `Z=(X1-X2)/sqrt2`. The joint `(Y,Z)` density is one on a diamond. For `|y|<1/sqrt2`, `p_Y(y)=sqrt2-2|y|`, while `Z|Y=y` is uniform on an interval of that length and has density `1/(sqrt2-2|y|)`, which diverges at the boundary. Thus a proof may use the projection lemma for marginals, but may not manufacture conditional caps or rotated independence.

2. **The hyperbolic critical slice is genuinely singular.** If `W1,W2` are independent uniform on `[-1/2,1/2]`, then for `q=2W1W2`,

`p_q(z)=log(1/(2|z|))`, `0<|z|<1/2`.

Hence any uniform pointwise hyperbolic-fiber supremum is false; logarithmic integration/averaging is essential.

3. **A scalar square has a genuine square-root singularity.** For `Y` uniform on `[-1/2,1/2]`, `Y^2` has density `t^-1/2` on `(0,1/4)`. Thus the manuscript is right to combine the square profile with a half-potential of the Schur remainder rather than demand a bounded conditional square density.

These examples do not refute the manuscript; they rule out tempting stronger intermediate assertions.

## Support-package audit

`README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json` are present at the observed master. `SOURCE_MANIFEST.json` matches the manuscript blob/hash/size/line count above. `proof_map.csv` matches the statement/proof ranges used in this ledger. `verify.py` pins the same SHA-256 and checks the interpolation/rank/support identities plus finite Schur/graph diagnostics. `checks.json` records `PASS` with 534 exact interpolation seeds, 18 volume-sampling cases, 240 floating Schur-threshold cases, and 30 graph-weight cases. These are reproducibility checks only and were not used as substitutes for the analytic audit.

## Impact and next obligation

The 17-direction baseline is sound in this review. The useful current improvement is not another repair to the baseline: it is the separate nine-direction replacement audited in the sibling improvement artifact for this run. Multiplicity eight remains a different structural problem; no claim below nine is made here.
