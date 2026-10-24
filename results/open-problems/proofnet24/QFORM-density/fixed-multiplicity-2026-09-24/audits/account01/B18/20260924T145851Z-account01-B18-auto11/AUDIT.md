# account01/B18 full audit — 2026-09-24T14:58:51Z

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer identity: `account01/B18`  
Status: **PASS mathematically for the pinned 17-eigenvalue theorem in this reconstruction; prior-art/bibliography presentation GAP; not an independent-validation certificate.**

## Source pin and scope

- Repository/branch: `yspennstate/math-open-problems@master`.
- Baseline commit named by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Manuscript path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
- Git blob actually read: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- SHA-256 recorded in `SOURCE_MANIFEST.json`: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Source length: 790 lines / 47,883 bytes.
- Also read in full this invocation: `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`.

This report is a fresh reconstruction by the same B18 slot. It must **not** be counted as a second genuinely independent complete review merely because B18 has performed earlier passes.

## Fatal defects first

**No fatal mathematical defect found.** The theorem as written is internally closed at the stated hypotheses and the conservative constant `10000 K^2/s`.

A previous B18 report had called the singular-`A` limit in `lem:schur` a gap. That was a false positive. The moving threshold is legitimate: if `m=N_A(t)-k>0`, the invertible regularizations give `s_m(S_epsilon)>=t-|epsilon|`; `S_epsilon -> S` and continuity of ordered singular values give `s_m(S)>=t`. If `m<=0` there is nothing to prove. Thus the baseline Schur proof needs no repair.

## End-to-end line/range audit

The ranges below are source line ranges from the pinned 790-line manuscript. `PASS` means I reconstructed the stated implication and checked all hypotheses used there. `GAP` below is only attribution/presentation unless explicitly described as mathematical.

| Range / label | Verdict | Reconstruction and exact reason |
|---|---|---|
| 1–39 preamble, notation declarations, title metadata | PASS | LaTeX/theorem setup is coherent. Identity/affiliation metadata are not mathematical dependencies. |
| 40–86 abstract; `thm:main` 47–57; `cor:33` 59–61; architecture and parameters | PASS | Quantifiers are arbitrary independent real coordinate densities `<=K`, arbitrary symmetric `A`, arbitrary affine `b,c`; `s_17(A)>=s`. Scaling target `K^2/s` is dimensionally correct. `s_17>=s_33` proves the corollary. No continuity claim is smuggled into the theorem. |
| 87–120 `lem:fourier` | PASS | Gaussian regularization, Plancherel normalization `2pi`, inversion factor `1/(2pi)`, and Gaussian identity were rederived. Approximate-identity and dominated/Fatou uses are legitimate for the stated integrability. |
| 122–130 `lem:envelope` | PASS | Integral of `min(1,(a/|t|)^p)` is exactly `2ap/(p-1)`; Fourier inversion yields `ap/[pi(p-1)]`. |
| 132–160 `lem:riesz` | PASS | Gamma representation and Gaussian inversion produce coefficient `1/sqrt(2pi)`; the weighted envelope integral is `12 sqrt(u)`, giving the stated bound. Tonelli is applied only to nonnegative majorants. |
| 161–181 singular-value conventions and `lem:rank` | PASS | Eckart–Young approximation formula yields the Lipschitz and rank-shift inequalities for nonsymmetric matrices as used later. |
| 183–207 `lem:schur` | PASS | Invertible case follows from inverse principal compression and positive/negative spectral counts. Singular case is valid via `A+epsilon I`, threshold `t-|epsilon|`, and continuity. Earlier B18 GAP is withdrawn. |
| 209–217 strict diagonal dominance | PASS | Standard max-coordinate proof works without symmetry. |
| 221–255 geometric rank-one BL theorem | PASS | Heat-flow sign is correct: frame identity makes `sum c_i v_i^2-|sum c_i u_i v_i|^2>=0`. Integration by parts is justified after heat smoothing; large-time normalization uses `sum c_i=d`; small-time Fatou plus monotone truncation closes rough inputs. |
| 258–282 `lem:projection` | PASS + attribution GAP | Deterministic marginal formula and geometric-BL application give `exp(d/2)`. It does not use rotational independence. The proof is self-contained. **Presentation GAP:** Livshyts–Paouris–Pivovarov (Israel J. Math. 216 (2016), 877–889, DOI 10.1007/s11856-016-1431-5) proves the sharper `2^{d/2}` product-marginal density bound and should be cited as directly relevant prior art. This omission does not affect proof correctness. |
| 284–301 scalar Fourier powers | PASS | `g=f*tilde f<=1`; Fourier inversion at zero after integrability is legitimate. `m=floor(p/2)>=p/4` and the projection cap give the displayed `2pi sqrt(2e)/sqrt p`. |
| 302–324 cross-form definition and `lem:decoupling` | PASS | Conditioning/Cauchy–Schwarz, independent copy, and product Fourier factors are correct. Difference coordinates remain independent and each convolution density is `<=1`. Arbitrary same-bank phases `F,G` survive exactly. |
| 326–373 `thm:determinant` | PASS + prior-art scope GAP | Frame vectors sum to identity; `c_j,d_i` are in `[0,1]`; the BL Jacobian and scalar Fourier norms cancel at `alpha=(2pi e)^2`; fourth root gives exponent `-1/8` and coefficient `t^2/(pi^2 e^2)`. **Presentation GAP:** Banks–Garza Vargas–Kulkarni–Srivastava, Ann. IHP Probab. Stat. 60(4) (2024), 2736–2766, DOI 10.1214/23-AIHP1400, contains Theorem 2.1 explicitly titled “Density of Quadratic Forms” and Corollary 2.4 with a scalar geometric-mean singular-value refinement for bilinear-affine forms. It should be discussed. It does *not* subsume this theorem because it lacks arbitrary same-bank phases `F(X_I)+G(X_J)`. |
| 374–400 `Z_k`, Cauchy–Binet, `cor:vol-fourier` | PASS | `det(I+zM^TM)` coefficients are `Z_k`; retaining one term gives exponent `k/4`. For `k=5`, Lemma envelope gives `5e Z_5^{-1/10}`. For `k=3`, Riesz gives the stated half-potential estimate. |
| 404–414 square profile | PASS | Two inverse branches give the density profile; completing the square gives the interval preimage length bound. Conditional use later is measure domination, not independence. |
| 423–434 definite pair | PASS | Completing square/orthogonal diagonalization is deterministic; polar Jacobian in `(delta,theta)` is `1/(2 sqrt(det B))`; joint density cap is the only probabilistic input. |
| 437–482 hyperbolic pair | PASS | Parametrization and Jacobian were checked; tail monotonicity starts after the stated cutoff; bathtub bound on `1/|y|` is valid for a cap-one density of mass at most one on a half-line. The proof actually yields the sharper constant `(15/2) log 2` before it is rounded to `6`; this is used in the separate improvement artifact. |
| 485–525 quarter-power concentration | PASS | Diagonal alternative follows from square inverse length. Offdiagonal random-sign split gives a physical cross block of norm `>=L/4`; determinant theorem then gives `|t|^{-1/4}`. Gaussian smoothing and the gamma integral yield the quarter-power concentration; layer cake gives `L_0=4+4 log16`. No rotated-coordinate independence is asserted. |
| 528–535 pivot/volume definitions and no-pivot entry estimate | PASS | From `|a_ii|<eta` and `|a_ii a_jj-a_ij^2|<eta`, the stated `|a_ij|^2<eta^2+eta` follows. |
| 545–564 `lem:sampling` | PASS | Bordered determinant identity is exact after squaring. The `(r+1)^2` multiplicity is an upper bound because singular seeds can have nonsingular extensions. Weighted averaging therefore gives existence of a good nonsingular seed. |
| 566–580 `lem:completion` | PASS | `E` is supported on the `LxL` offdiagonal residual; `D` is diagonal and vanishes on seed indices. `R-P` can be decomposed into rows `T` plus remaining columns `S`, so global rank `<=3r`; on `LxL`, `R=P`, hence restricted rank `<=r`. Nonsymmetry is harmless because later perturbation uses singular values. |
| 582–619 `prop:volume` | PASS | Telescoping/first-zero selection of `r` is exhaustive. `r=0` contradicts `s_m(A)>=1` via operator norm. For `1<=r<=4`, rank shift forces `r+1` large diagonal entries of `D` in `L`; strict diagonal dominance of `R[H,H]` contradicts restricted rank `<=r`. Every numerical inequality at the baseline parameters checks. |
| 621–630 random cut | PASS | Each ordered disjoint `(S,T)` survives the fair cut with probability `4^{-k}`. This is a physical original-coordinate partition. |
| 632–645 no-pivot consequences | PASS | `Z_k^{-1/(2k)}<=2 kappa^{-1/2}=160`; substitution into the order-three/order-five analytic bounds gives `<200` and `800e<2400`. |
| 654–674 kernel integrals | PASS, sharpenable | Baseline `J(d)<=8+3 log_+(1/|d|)` and log-kernel `<=8` are valid. I found a self-contained stronger `J(d)<=8+2 log_+(1/|d|)`; proof is in the improvement artifact. |
| 676–714 `prop:pivot-H` | PASS, sharpenable | Scalar pivot uses Schur + quarter-power log control; definite and indefinite pair bounds are uniform under conditioning. `D^{-1/2} log_+ D<=2/e` is correct. Sharper kernel/hyperbola constants reduce this branch materially; see improvement. |
| 716–724 `prop:nine` | PASS | Pivot/no-pivot dichotomy gives truncated half-potential bound; outside unit distance the kernel is `<=1`, hence full half-potential `<=601`. |
| 726–749 main theorem proof | PASS | No-pivot density, scalar pivot via Schur leaving 16 modes (hence 9), definite pair, and indefinite pair exhaust cases. Conditional exceptional slices are avoided through measure domination/Tonelli. General scaling `Y=KX`, `Q=(s/K^2) Qtilde` gives exactly `K^2/s`. |
| 750–780 threshold accounting/limitations | PASS | It correctly distinguishes order-five integrable exponent `5/4` from order-three half-potential use and explicitly does not claim the 3-eigenvalue conjecture or continuity in pivot branches. |
| bibliography, final lines | GAP (presentation only) | BCCT and RV are legitimate provenance, but bibliographic records should use the published versions and add LPP and Banks et al. Herry–Malicet–Poly is also relevant contrast literature but materially narrower (iid inputs with a smooth Gaussian-field representation). Search absence is not used as a novelty claim. |

No mathematical line remains `UNCHECKED` in this B18 pass. The external factual question of publication priority is not “proved” by a finite search; the report therefore makes no novelty assertion from a search miss.

## Primary-source attribution / scope audit

1. **Bennett–Carbery–Christ–Tao.** The geometric Brascamp–Lieb method is appropriate provenance. Published form: *Geom. Funct. Anal.* 17, 1343–1415 (2008), DOI `10.1007/s00039-007-0619-6`. The manuscript proves the exact geometric rank-one inequality it needs, so this is attribution rather than a delegated dependency.
2. **Rudelson–Vershynin.** *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, *IMRN* 2015(19), 9594–9617, DOI `10.1093/imrn/rnu243`. Relevant hypotheses are independent coordinates with one-dimensional concentration/density control. Again, the manuscript re-proves the weaker projection estimate it actually uses.
3. **Livshyts–Paouris–Pivovarov.** *On sharp bounds for marginal densities of product measures*, *Israel J. Math.* 216 (2016), 877–889, DOI `10.1007/s11856-016-1431-5`. Their cap-one product hypothesis matches the normalized projection setting and gives the sharper marginal cap `2^{d/2}`. Add as prior art; not required for correctness of the weaker in-manuscript proof.
4. **Banks–Garza Vargas–Kulkarni–Srivastava.** *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, *Ann. IHP Probab. Stat.* 60(4) (2024), 2736–2766, DOI `10.1214/23-AIHP1400`. Section 2 contains Theorem 2.1 “Density of Quadratic Forms” for the bilinear-affine form `X^T ZY+X^T U+V^T Y+W`; Corollary 2.4 gives a scalar geometric-mean singular-value refinement. It does not retain arbitrary same-bank phases, so it is related prior art rather than an exact prior solution of this manuscript's theorem.
5. **Herry–Malicet–Poly.** *Regularity of laws via Dirichlet forms — Application to quadratic forms in independent and identically distributed random variables*, *Probability Theory and Related Fields* 191 (2025), 523–567, DOI `10.1007/s00440-024-01332-x`. Their iid/smooth-Gaussian-field representation assumptions are materially narrower than arbitrary non-iid density-capped inputs.
6. **de la Peña–Montgomery-Smith decoupling literature.** Classical U-statistic/quadratic-form decoupling compares tail distributions/norms of coupled and decoupled chaoses. It does not directly transfer the local `L^infinity` density problem with arbitrary same-bank phases, so it cannot be cited as closing the `s_16` endpoint without an additional local-concentration argument.

## Reproducibility support files

`verify.py` pins the SHA-256 and performs exact finite checks of interpolation identities plus floating diagnostics for Schur counts and graph weights. `checks.json` reports PASS with 534 exact interpolation seeds, 18 volume-sampling cases, 240 numerical Schur threshold cases, and 30 graph-weight cases. These are consistent with the source but are not proof certificates. The older historical self-audit counts in `AUDIT.md` are explicitly a different suite and should not be conflated with this checker.

## Threshold reduction audit

I rechecked the current `17 -> 16` endpoint rather than claiming an unsupported reduction. Under normalized no-pivot `s_16(A)>=1`, existing pinned improvements rigorously reduce an unpaid survivor to a near-rank-four physical crossing with order-four exterior volume, plus same-bank mass transverse to its top-four left carrier. A subsequent mixed-exterior identity pays the branch where at least half of the forced four-plus-one energy is physically disjoint. The remaining survivor is trapped in explicit row-leverage/self-coordinate overlap functionals. Those results are genuine progress, but they do **not** yet yield an order-five physical crossing or a local-density receiver for every survivor.

The present architecture itself has two exact barriers at 16:

- algebraically, at `r=4` the global rank loss is `3r=12`, so `s_16` transfers only four large diagonal entries, while restricted rank `<=4` needs five for the diagonal-dominance contradiction;
- analytically, order-four crossing volume gives only the endpoint characteristic envelope `O(|t|^{-1})`, not an `L^1` envelope.

I found no source-valid theorem in the audited literature that preserves the arbitrary same-bank phases and removes both endpoint barriers. Therefore **no 16-eigenvalue theorem is claimed in this run**.

## Final B18 verdict

- Pinned 17-eigenvalue proof: **PASS** in this reconstruction.
- Fatal mathematical gaps: **none found**.
- Unchecked mathematical source ranges: **none**.
- Prior-art/bibliography: **GAP, nonfatal**; add LPP and Banks et al., update BCCT/RV publication metadata, optionally mention Herry–Malicet–Poly as narrower-scope contrast.
- `17 -> 16`: **not proved**; current surviving endpoint is explicitly localized, not closed.
- Independent-validation status: **unchanged**; this is one B18 review and cannot self-award the required separate review certificate.
- Full three-eigenvalue conjecture: **not claimed solved**.
