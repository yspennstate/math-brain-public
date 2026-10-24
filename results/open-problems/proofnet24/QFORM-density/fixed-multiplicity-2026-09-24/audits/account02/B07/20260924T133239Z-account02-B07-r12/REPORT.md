# account02/B07 end-to-end audit — fixed-multiplicity manuscript

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`

Run: `account02-B07-20260924T133239Z-r12`

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`

Current master observed before audit: `15082841edd324c5a29c7fb4d9ceb2f81726f107`; pre-write master refresh: `34697881037374b1294bc0d41410d672eb6acc7a`.

The manuscript blob at both observations is unchanged: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Manifested source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**PASS for the complete written 17-eigenvalue theorem, with one nonfatal local wording GAP in `lem:projection`; no fatal mathematical defect found.** The unrestricted three-eigenvalue QFORM conjecture is not claimed solved. I found no complete replacement proof lowering 17 in this run.

The previously reported package reproducibility gap is now closed at the repository level: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are present and were read. The compiled PDF binary itself was not available in the package root and its hash/render claims remain UNCHECKED by this run, exactly as documented.

## Full source-range audit

Every manuscript line 1--790 was read from the pinned unchanged blob. Each specialized lemma invocation was checked against its stated hypotheses.

| Source range / label | Verdict | Reasoning / repair / impact / next obligation |
|---|---|---|
| 1--46 preamble and abstract | PASS | Scope matches the theorem: arbitrary independent real coordinate laws with density cap, arbitrary symmetric matrix/signature/remainder spectrum and affine terms. No continuity or optimality claim is smuggled into the theorem. |
| 47--85 `thm:main`, `cor:33`, architecture | PASS | `s_17(A)>=s` and scaling target are stated correctly; 33 is a monotone corollary. The proof architecture distinguishes the density-producing order-five branch from the order-three half-potential branch. |
| 86--121 `lem:fourier` | PASS | Fourier convention, Plancherel factor `2pi`, Gaussian inversion factor and weak-limit density identification are consistent. |
| 122--131 `lem:envelope` | PASS | Envelope integral is `2ap/(p-1)` and inversion contributes `1/(2pi)`. |
| 132--160 `lem:riesz` | PASS | Gamma/Tonelli derivation and the weighted Fourier integral yield the displayed `1/sqrt(2pi)` normalization; the power envelope gives `12 sqrt(u/(2pi))`. |
| 161--181 `lem:rank` | PASS | SVD approximation formula proves both perturbation and rank-shift inequalities without symmetry. |
| 182--208 `lem:schur` | PASS | For invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive/negative interlacing gives the absolute-value spectral count. The moving threshold for `A+eps I` is sufficient in the singular limit. |
| 209--217 `lem:dd` | PASS | Maximal-coordinate proof establishes invertibility for nonsymmetric strictly row-diagonally-dominant matrices. |
| 218--255 `thm:bl` | PASS | Heat-flow sign, frame contraction, integration by parts, large-time Gaussian limit, small-time Fatou and monotone truncation are consistent. |
| 256--283 `lem:projection` | **GAP, local/nonfatal** | After factors with `b_i=0` are dropped, the proof writes `sum_i(1-b_i)=d` as though the entropy sum still included those rows. Correct chain: `sum_{b_i>0}(-b_i log b_i) <= sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`. The stated `e^{d/2}` bound and every downstream constant remain unchanged. Next obligation: patch this one inequality in prose. |
| 284--301 `lem:scalar-fourier` | PASS | `m=floor(p/2)>=p/4`; `|hat f|^{2m}` is integrable and is the characteristic function of a sum of `m` independent differences. The projection bound at zero gives the stated constant. |
| 302--325 `lem:decoupling` | PASS | Cauchy--Schwarz and one independent `J` copy yield the product Fourier factors over original `I` coordinates; Jensen gives the fourth-power bound. Difference-coordinate densities stay <=1. |
| 326--373 `thm:determinant` | PASS | The regularized graph vectors form the identity frame. BL Jacobian factors, `c_j,d_i` exponents, scalar Fourier powers and entropy factor cancel at `alpha=(2pi e)^2`; taking fourth roots gives determinant exponent `-1/8`. |
| 374--400 crossing volumes and `cor:vol-fourier` | PASS | Cauchy--Binet coefficient is exactly the squared-minor volume; retaining the order-k term gives exponent `k/4`. k=5 gives direct density, k=3 gives only the weighted half-potential. |
| 401--422 square profile and conditional profile | PASS | Two inverse branches give the square-root envelope and interval-preimage bound. Conditional measure domination is legitimate without independence between the completed square and its Schur critical value. |
| 423--436 `lem:definite` | PASS | Two-dimensional quadratic polar coordinates have Jacobian `1/(2 sqrt(det B))`; joint density cap is used before deterministic rotation. |
| 437--484 `lem:hyperbola` | PASS | Hyperbolic Jacobian, original-coordinate tail choice, monotonic tail maps, filling bound, branch constant and `Lambda>=2/sqrt(D)` all check. Exceptional critical level is handled in the measure-domination formulation. |
| 485--525 `lem:quarter` | PASS | Large diagonal gives square small-ball control; otherwise the random-sign physical crossing has norm >=L/4. Determinant decay plus Gaussian smoothing gives the quarter-power estimate, and layer cake yields the logarithmic potential. |
| 526--544 `def:pivot-volume`, no-pivot entry estimate | PASS | `V_r` is explicitly over ordered disjoint pairs, with sorted row/column order inside each minor. No pivot implies `|a_ij|<1/7`. |
| 545--565 `lem:sampling` | PASS | Bordering a nonsingular seed gives `det(sorted child)= +/- det(B)(a_lm-P_lm)`; the sign is exactly the product of the row/column sorting permutation signs and is removed by squaring. Each ordered child has at most `(r+1)^2` deleted parent pairs. Singular parents have zero sampling weight, so only `<=` is valid. Existence follows from the weighted average; the proof does not claim all seeds are good. |
| 566--581 `lem:completion` | PASS | `E` is the off-diagonal LxL defect, `D` the diagonal defect on L and vanishes on the seed. `R-P` is supported in rows T or columns S outside the regions where interpolation is exact, giving global rank <=3r; `R[L,L]=P[L,L]` gives restricted rank <=r. |
| 582--620 `prop:volume` | PASS | Telescoping/first-zero logic produces a small successive ratio. The r=0 case contradicts operator norm >=1. For 1<=r<=4, global rank loss plus perturbation forces r+1 large diagonal entries in L; the exact diagonal-dominance slack is `371/400-23/28=297/2800>0`, contradicting restricted rank. |
| 621--631 `lem:cut` | PASS | Each fixed ordered disjoint pair survives the fair cut in its prescribed orientation with probability exactly `2^{-2k}=4^{-k}`. This is an exact expectation identity, not a selection heuristic. |
| 632--645 `cor:no-pivot` | PASS | `Z_k^{-1/(2k)}<=160`; k=3 gives full half-potential <200 and k=5 gives density `800e<2400`. |
| 646--675 H and `lem:kernels` | PASS | Near/far split for J(d) and the interval-overlap layer-cake proof for the log kernel are valid at the stated constants. |
| 676--715 `prop:pivot-H` | PASS | Scalar, definite-pair and indefinite-pair alternatives exhaust the pivot definition. Each branch uses the correct surviving spectral hypothesis and keeps arbitrary affine terms. |
| 716--725 `prop:nine` | PASS | Pivot branch controls the truncated half-potential; no-pivot order-three branch controls the full half-potential. The tail outside distance one contributes at most one. |
| 726--749 proof of `thm:main` | PASS | No-pivot s17 closes directly. A scalar pivot leaves at least 16 Schur directions, hence >=9; pair pivot leaves >=15. The normalization `Y=KX`, `Q=(s/K^2) Qtilde` yields exactly `10000 K^2/s`. |
| 750--781 threshold accounting and remarks | PASS | Correctly states what is and is not proved and separates continuous no-pivot density from essential density in pivot branches. |
| 782--789 bibliography | UNCHECKED for exhaustive prior-art/priority only | Citations are attribution, not proof dependencies. No literature-priority audit was performed here. |
| 790 end | PASS | Source terminates normally. |

## Supplementary package audit

- `README.md`: PASS for package description and mathematical scope.
- `DELIVERY_STATUS.md`: PASS as a status document; scheduler statements were not used as mathematical evidence.
- `AUDIT.md`: PASS as a historical authoring self-report, not independent validation. Its old finite-test counts remain historical and are explicitly distinguished from the new checker.
- `proof_map.csv`: PASS. Statement/proof ranges are consistent with the source read here.
- `SOURCE_MANIFEST.json`: PASS for source blob/line/byte metadata consistency with the package. UNCHECKED: compiled-PDF binary SHA/render claim was not independently reproduced in this run; support-file SHA-256 strings were not independently recomputed from raw bytes.
- `verify.py` / `checks.json`: PASS for code-to-result consistency. I independently reran the mathematical body of the checker (omitting only its repository-file SHA gate) and reproduced exactly: 534 interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, diagonal-dominance slack 297/2800, 240 floating Schur-threshold cases, and 30 graph-weight cases. These remain diagnostics, not proof certificates.

## New B07 adversarial findings

Three exact finite constructions sharpen the minor/rank quantifiers. Full details are in `ADVERSARIAL_MINOR_CHECKS.md` in this immutable run folder.

1. **The `(r+1)^2` child multiplicity is combinatorially sharp for every relevant r=1,2,3,4, even inside the no-pivot regime.** Scaled symmetric Cauchy bipartite blocks make every one of the `(r+1)^2` deleted r-seeds nonsingular for a fixed child.
2. **The sampled-seed conclusion is genuinely existential, not universal.** A no-pivot 4x4 rational matrix has one nonsingular r=1 seed with `||F||_F^2` more than fifteen times the theorem's average threshold, while another seed is below it; the weighted mean equals the stated bound exactly.
3. **The global `3r` and restricted `r` ranks in `lem:completion` can be attained simultaneously for every relevant r=1,2,3,4 under no-pivot scaling.** A direct sum of r explicit 3x3 blocks gives `rank R=3r` and `rank R[L,L]=r` with `E=0`.

These results block three tempting threshold shortcuts: dividing the child multiplicity by symmetry, choosing an arbitrary seed instead of sampling, or replacing global `3r` by `2r` using only symmetry/no-pivot. They do not prove that 17 is optimal, and they are not counterexamples to a lower-multiplicity density theorem.

## Threshold reduction status

No unconditional multiplicity below 17 is certified by this run. The current order-five determinant envelope has exponent `5/4>1`; order four is the nonintegrable endpoint `|t|^{-1}` for this leverage-free mechanism. The rank bookkeeping can genuinely lose `3r`, and the worst small-ratio index for k=5 is r=4, where `16-3r=4` does not force five large diagonal directions against a restricted rank-four block. A reduction therefore needs a new analytic endpoint/cancellation theorem or genuinely new structural routing, not a multiplicity/sign/counting correction.

## Final status

Mathematical baseline: PASS with one nonfatal projection wording GAP.

Fatal defects found: none.

Unrestricted three-eigenvalue QFORM: OPEN / not claimed solved.
