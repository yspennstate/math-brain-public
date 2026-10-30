# fleet01/B05 r11 — full fixed-multiplicity audit

Run: `20260924T142555Z-fixed-multiplicity-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Starting lens: product-projection densities; deterministic orthogonal changes versus probabilistic independence; density versions and exceptional slices.

## Source pin and scope

Pinned mathematical source audited independently:

- repository: `yspennstate/math-open-problems`
- initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- owner-recorded SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- source length: 790 lines / 47,883 bytes.

I read all 790 source lines, plus current `README.md`, `DELIVERY_STATUS.md`, historical `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. The support package was read from current `master`; the mathematical proof was audited against the immutable initial source commit above. At final control refresh, `master` was observed at `0aa54bd634644b2922e9faecd003692d7f29e61e`; the baseline manuscript blob remained the pinned blob.

Exact theorem audited: independent real coordinate densities bounded by `K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; if `s_17(A)>=s>0`, then `Q=X^TAX+b^TX+c` has a Lebesgue density and `||p_Q||_infinity<=10000 K^2/s`. No continuity claim is part of the full theorem. The unrestricted three-eigenvalue conjecture is not claimed.

## Verdict

**Mathematical verdict on the complete pinned 17-direction proof: PASS in this B05 review.** I found no theorem-breaking `GAP` and no `FALSE` mathematical assertion. I did not infer this verdict from peer PASS labels; every proof dependency was reconstructed or checked directly.

`UNCHECKED` items in this run are non-proof items only: I did not independently verify bibliographic priority/metadata for the two classical antecedent citations, I did not recompute the stated SHA-256 from raw bytes in a local checkout, and I did not rerun the Python diagnostic suite. The Git blob/source identity was pinned through the repository; `verify.py` itself was inspected and `checks.json` was read. These omissions do not enter the theorem proof.

## Complete source ledger

Every source range below was read. Blank lines and section separators are absorbed into the adjacent range.

| Lines | Label/content | Status | Independent reasoning and downstream impact |
|---|---|---|---|
| 1–46 | Preamble, abstract, conventions | PASS | Abstract quantifiers match the theorem. No hidden support, moment, sign, smoothness, iid, log-concavity, or rotated-coordinate assumption. |
| 47–57 | `thm:main` | PASS | Exact `s_17`, arbitrary symmetric matrix, arbitrary affine terms, and essential-density formulation are unambiguous. |
| 59–81 | `cor:33`, architecture, parameters | PASS | Counts `9=4*3-3`, `17=4*5-3` agree with the later structural proposition. The text explicitly separates deterministic rotations from independence. |
| 83–90 | Fourier/Gaussian conventions | PASS | Fourier convention is consistent with every later `2pi` factor. |
| 91–120 | `lem:fourier` | PASS | Gaussian regularization proves Plancherel; `L^2` approximate identity is justified. `phi in L^1` gives a continuous density by uniform convergence of Gaussian-smoothed densities. Gaussian identity has the correct normalization. |
| 122–130 | `lem:envelope` | PASS | `int min(1,(a/|t|)^p)=2ap/(p-1)` and inversion gives the displayed constant. |
| 132–160 | `lem:riesz` | PASS | Gamma representation and two Tonelli steps are legitimate as nonnegative integrals. Substitution gives `sqrt(2) Gamma(1/4)|t|^-1/2`, hence coefficient `1/sqrt(2pi)`. The `3/4` power envelope integrates to `12 sqrt(u)`. |
| 161–181 | Spectral conventions, `lem:rank` | PASS | Approximation-number proof works for nonsymmetric auxiliaries. The rank-shift direction used later is correct. |
| 183–207 | `lem:schur` | PASS | Invertible case follows from inverse principal compression and positive/negative interlacing. Singular case correctly perturbs at threshold `t-|eps|`, avoiding a fixed-threshold discontinuity. |
| 209–217 | `lem:dd` | PASS | Strict row diagonal dominance proof is standard and does not need symmetry. |
| 221–255 | `thm:bl` | PASS | Heat-flow derivative is `F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` by the frame identity. Compact-support heat tails justify differentiation/integration by parts; large-time limit, small-time Fatou, and monotone truncation are sound. |
| 258–282 | `lem:projection` | PASS | Reconstructed below. The orthogonal completion is only a deterministic change of variables in the joint density; independence of projected coordinates is never asserted. |
| 284–301 | `lem:scalar-fourier` | PASS | With `m=floor(p/2)`, `2m<=p`; because `|hat f|<=1`, the comparison direction is correct. The `2m` power is the characteristic function of a sum of independent differences; inversion supplies the continuous value at zero before applying the projection cap. |
| 302–324 | Cross-form setup, `lem:decoupling` | PASS | Cauchy–Schwarz and one independent copy of the `J` bank give the physical-coordinate Fourier product. All pre-estimate integrands have modulus one, so no moment hypothesis is introduced. |
| 326–373 | `thm:determinant` | PASS | Checked frame weights, Jacobian, trace identity, BL scales, `p=2/d_i` Fourier powers, cancellation of all `d_i`, entropy bound on `c_j`, regularizer `alpha=(2pi e)^2`, and fourth root. Final exponent is exactly `-1/8`. |
| 374–400 | `Z_k`, Cauchy–Binet, `cor:vol-fourier` | PASS | `Z_k` is the elementary symmetric polynomial in squared singular values. Order 5 produces integrable exponent `5/4`; order 3 is used only against the half-Riesz weight. Constants `5e` and the stated order-3 bound check. |
| 404–421 | `lem:square`, conditional profile | PASS | Two monotone square branches give the square-root profile and interval-preimage length. The conditional statement is a measure-domination/Tonelli assertion; it does not assume the square and Schur remainder are independent. |
| 423–434 | `lem:definite` | PASS | Completing the square and orthogonally diagonalizing a deterministic 2D integral uses only the original joint density cap `M`; no post-rotation independence is invoked. Jacobian gives `pi M/sqrt(|det B|)`. |
| 437–482 | `lem:hyperbola` | PASS | Hyperbolic parameterization has Jacobian `1/(2sqrt D)`. Each tail is controlled by one original coordinate with monotone derivative `>=|coordinate|/3`; cap plus unit mass gives the logarithmic tail bound. The critical level may truly be singular, but only an a.e. density envelope is needed, and conditional applications are through nonnegative test functions/Tonelli. |
| 485–525 | `lem:quarter` | PASS | Diagonal and random-sign off-diagonal alternatives are exhaustive. The determinant theorem gives the `|t|^-1/4` bound; Gaussian smoothing yields the quarter-power small ball; layer cake gives `L_0=4+4 log16`. |
| 528–544 | Pivot-volume definition and no-pivot entry bound | PASS | Ordered disjoint-minor convention is consistent. No pivot implies `|a_ij|<1/7`. |
| 545–564 | `lem:sampling` | PASS | Bordered determinant identity is exact. An ordered `(r+1)` disjoint pair is counted at most `(r+1)^2`; singular seed extensions explain why the proof correctly claims an inequality, not equality. |
| 566–580 | `lem:completion` | PASS | `D` vanishes on seed coordinates; `E` has zero diagonal; `R_LL=P_LL` with rank at most `r`. Support of `R-P` lies in rows `T` or columns `S`, hence global rank at most `3r`. No symmetry of `R,E,P` is required. |
| 582–619 | `prop:volume` | PASS | `r=0` gives the norm contradiction. For `r>=1`, `eps<=(r+1)/80<=1/16`; rank subtraction forces `r+1` large diagonal entries in `L`. On such an `(r+1)` block, diagonal entries are at least `371/400`, each off-diagonal at most `1/7+1/16`, and the row sum is `<23/28`; strict diagonal dominance contradicts `rank R_LL<=r`. Exact slack is `297/2800>0`. |
| 621–630 | `lem:cut` | PASS | Every ordered disjoint row/column pair is separated in the specified orientation with probability `4^-k`; expectation identity is exact. |
| 632–645 | `cor:no-pivot` | PASS | `k=3` yields the full half-potential `<200`; `k=5` yields density `<2400`. All affine/same-bank terms stay inside the cross-form framework. |
| 646–674 | Truncated half potential, `lem:kernels` | PASS | Atom convention is explicit. Both singular kernels are integrable in the needed ranges; the logarithmic overlap estimate and constants are sufficient. |
| 676–714 | `prop:pivot-H` | PASS | Scalar, definite-pair, and indefinite-pair cases use exactly their pivot hypotheses. Scalar branch spends a surviving Schur direction only on the logarithmic potential. Indefinite branch averages the a.e. hyperbolic envelope and never selects conditioning-dependent exceptional values. |
| 716–724 | `prop:nine` | PASS | Pivot branch yields truncated half-potential; no-pivot branch yields the full half-potential; outside the unit neighborhood the kernel is at most one. |
| 726–749 | Main proof and scaling | PASS | No-pivot `<2400`; scalar pivot leaves 16 directions and gives `<6010`; definite pair `<40`; indefinite pair leaves 15 directions and gives `<251`. Scaling `Y=KX`, `A/s` yields exactly `K^2/s`. |
| 750–790 | Threshold accounting, dependency/limitations, bibliography | PASS for mathematical content; UNCHECKED for external bibliographic priority/metadata | The manuscript correctly states that 17 is not optimal and does not claim the full 3-direction theorem or global continuity. Classical citations are attribution only; no proof step depends on an unverified external theorem. |

No mathematical proof line remains `UNCHECKED` in this run.

## B05 lens reconstruction 1: product-projection density

Let `U in R^{n x d}` have orthonormal columns and complete it to an orthogonal matrix `(U,W)`. If `w_i^T` is row `i` of `W`, the original product density and the deterministic change of variables `x=Uy+Wz` give

`p(y)=int prod_i f_i((Uy)_i+w_i dot z) dz`.

Put `b_i=||w_i||^2=1-||U^T e_i||^2`. A factor with `b_i=0` is at most one and may be discarded. For `b_i>0`, `v_i=w_i/sqrt(b_i)` satisfies

`sum_i b_i v_i v_i^T=I_{n-d}`.

Apply the proved geometric BL theorem to

`h_i(t)=f_i((Uy)_i+sqrt(b_i)t)^(1/b_i)`.

Because `0<=f_i<=1` and `1/b_i>=1`,

`int h_i <= b_i^(-1/2)`.

Therefore

`p(y)<=prod b_i^(-b_i/2)`.

Using `-b log b<=1-b` and `sum_i(1-b_i)=sum_i||U^T e_i||^2=d`,

`||p_{U^T X}||_infinity<=e^(d/2)`.

This is a marginal-density statement for a deterministic linear image of the original product law. It says neither that the projected coordinates are independent nor that conditional densities after another projection inherit the same cap. For a full-row-rank deterministic map `L`, polar decomposition immediately gives the useful corollary

`||p_{LX}||_infinity <= e^(d/2)/sqrt(det(LL^T))`.

## B05 lens reconstruction 2: density versions and exceptional slices

The square profile and hyperbolic profile are deliberately a.e. statements. The critical square vertex can have a true `|z-v|^-1/2` singularity, and an indefinite pair can have a true logarithmic singularity at its critical value. A conditioning argument must therefore not choose one common pointwise version across conditioning parameters.

The manuscript uses the correct measure-level formulation: for almost every conditioning value, dominate the conditional output measure against every nonnegative output test function, then average with Tonelli. This produces an unconditional measure dominated by the averaged kernel and bypasses any need to synchronize null exceptional output slices. This also makes arbitrary rough input density versions harmless: choose bounded-everywhere representatives when convenient; changes on input null sets do not affect the pushforward law.

The deterministic orthogonal changes in `lem:definite` and the hyperbolic level-set parameterization are changes of integration variables only. The proof never treats the rotated coordinates as independent random variables. That distinction is essential and is respected throughout the source.

## Support-package audit

- `README.md`: PASS as a package map and scope statement. It accurately describes the 17-direction candidate and warns that independent worker reviews/release gate are separate.
- `DELIVERY_STATUS.md`: PASS as a delivery/status record; its peer-count claims were not used as proof evidence.
- historical `AUDIT.md`: read in full; treated only as author-side self-report, not as independent evidence.
- `proof_map.csv`: PASS; its statement/proof ranges match the source ranges used above.
- `SOURCE_MANIFEST.json`: PASS for internal consistency with the repository-visible commit/blob/size/line count. The listed SHA-256 was not independently recomputed from raw bytes in this run (`UNCHECKED` only for that recomputation).
- `verify.py`: PASS on code inspection. It pins the same SHA, exactly checks interpolation/rank/support identities on finite examples, and separately labels floating Schur/graph tests as diagnostics.
- `checks.json`: read; records PASS with 534 exact interpolation seeds, 18 volume comparisons, 240 floating Schur-threshold checks and 30 graph-weight checks. I did not rerun the suite in this invocation, so the execution is `UNCHECKED` here and is not used as proof.

## Threshold lowering checked in this run

After the baseline audit I independently reconstructed the current complete nine-direction replacement mechanism rather than accepting a peer verdict. It preserves every theorem hypothesis and gives

`||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s`

under `s_9(A)>=s`. The crucial new grouped product-Fourier compiler is compatible with the B05 projection proof: every density cap is applied to a deterministic linear image of an original product bank, and the rough-law `L^2` pushforward step uses mollification plus one independent copy of the literal `J` bank, not a conditional cap or rotated independence. The weighted-subset entropy inequality and the `E_3`/`E_2` promotion identities close the no-pivot and scalar-pivot branches respectively.

I record the full reconstruction and the remaining threshold-eight obstruction separately under this run's `improvements/fleet01/B05/.../IMPROVEMENT.md`. I do not assign owner-level release/independent-validation status here.

## Final statuses

- pinned 17-direction manuscript: **PASS** in this complete B05 audit;
- support-package mathematical dependencies: **PASS**; finite rerun and bibliographic priority only **UNCHECKED** as noted;
- complete 9-direction replacement: **PASS in this independent B05 reconstruction**, recorded separately;
- 8-direction `L^infinity` theorem: **OPEN**;
- unrestricted 3-direction conjecture: **OPEN / not claimed**;
- global continuity for the full fixed-multiplicity theorem: **not claimed**.

Model: GPT-5.6 Sol. Configured reasoning-effort/provider thinking counters: `UNKNOWN / NOT_EXPOSED`.