# account01/B07 independent full audit — fixed-multiplicity candidate

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T120614Z-account01-B07-fixedmult-audit-r11`  
Audited repository: `yspennstate/math-open-problems`, branch `master`  
Pinned manuscript commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Control/README supplied SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Current `master` manuscript blob at this run: `183ccd294763214e6a707e8d4749ff9a8cf7006d` (same source bytes by git blob identity).

## Verdict

**PASS for the mathematical 17-eigenvalue theorem in this independent B07 audit, with one nonfatal local proof-wording GAP and one repository-package GAP. No fatal mathematical gap was found.** This is one actual worker review, not a self-awarded independent-validation certificate, not formal verification, and not a proof of the unrestricted three-eigenvalue conjecture.

The theorem audited is exactly: independent real coordinate laws with densities `<=K`; arbitrary real symmetric `A`; arbitrary dimension, signature, remaining spectrum, affine `b,c`; if `s_17(A)>=s>0`, then `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity <= 10000 K^2/s`.

I read the entire 790-line `manuscript.tex` from the pinned commit, not just the B07 minor-selection section. The line-range table below covers all source lines. I separately read `README.md` and `AUDIT.md` on current master. `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` were requested directly on current master (and `proof_map.csv` also at the baseline commit) and returned Not Found; this is recorded below rather than inferred away.

## End-to-end line audit

| Source range / label | Verdict | Independent reasoning and downstream consequence |
|---|---|---|
| lines 1–60: preamble, abstract, `thm:main`, `cor:33` | **PASS** | Quantifiers are the advertised arbitrary-law/arbitrary-symmetric-matrix ones. No hidden moment, support, sign, diagonal, or rotational-independence hypothesis is introduced. `s_33>=s` implies `s_17>=s`, so the 33-direction corollary is immediate. |
| lines 61–80: architecture and parameters | **PASS** | `eta=1/100`, `kappa=1/80^2`; the proof explicitly separates pivot and no-pivot routes and correctly identifies the algebraic counts `9=4*3-3`, `17=4*5-3`. The claimed global conclusion is only essential boundedness, consistent with later pivot arguments. |
| lines 81–120: Fourier convention and `lem:fourier` | **PASS** | With `hat f(t)=int e^{itx}f(x)dx`, the Gaussian has transform `e^{-eps t^2}`; Plancherel is `2pi`; inversion is `1/(2pi)`; Gaussian inversion has coefficient `1/(2 sqrt(pi v))`. Approximate-identity, Fubini and dominated-convergence steps are legitimate under the stated integrability. |
| lines 121–160: `lem:envelope`, `lem:riesz` | **PASS** | The envelope has L1 mass `2ap/(p-1)`. The gamma representation with parameter `1/4`, followed by the Gaussian inversion and `v`-integration, yields the stated `1/sqrt(2pi)` Riesz factor. The weighted integral for exponent `3/4` is exactly `12 sqrt(u)`. |
| lines 161–181: singular-value conventions and `lem:rank` | **PASS** | Eckart–Young/SVD approximation gives both 1-Lipschitz singular values and the rank-shift inequality for nonsymmetric matrices. This is exactly the form needed later for `A-E` and nonsymmetric `R`. |
| lines 182–218: `lem:schur` | **PASS** | For invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}`; applying positive and negative interlacing separately gives the absolute-eigenvalue count. The singular case is recovered by `A+eps I` with threshold `t-|eps|` and continuity. No inertia-only shortcut is used. |
| lines 219–230: strict diagonal dominance | **PASS** | Standard maximum-coordinate argument works without symmetry and is later applied to the nonsymmetric `R_{H,H}` exactly as stated. |
| lines 231–264: geometric rank-one Brascamp–Lieb | **PASS** | Heat flow identity has nonnegative defect `sum c_i v_i^2 - |sum c_i u_i v_i|^2` by the frame contraction. Gaussian tail control justifies differentiation/integration by parts. The large-time limit uses `sum c_i=d`; Fatou and monotone truncation give the rough nonnegative case. |
| lines 265–283: `lem:projection` | **GAP (nonfatal local wording/indexing issue)** | After dropping rows with `b_i=0`, the manuscript writes `sum_i(1-b_i)=d`. If that displayed sum is interpreted only over retained positive-`b_i` rows, equality is false (e.g. `U=e_1` in `R^2`). The required estimate still holds: over positive rows the sum is `<=d`, or one may restore all rows on the RHS and use the continuous convention `-b log b=0` at `b=0`. Therefore `p<=e^{d/2}` and every later use remain valid. **Repair:** replace the equality by `<=d/2` at the logarithmic estimate, or explicitly state the RHS sum is over all rows. |
| lines 284–302: `lem:scalar-fourier` | **PASS** | `m=floor(p/2)>=p/4`; since `|hat f|<=1`, `|hat f|^p<=|hat f|^{2m}`. The latter is integrable and is the characteristic function of a sum of `m` independent differences; inversion at zero plus the scalar projection bound gives the stated constant. |
| lines 303–330: cross-form and `lem:decoupling` | **PASS** | Cauchy–Schwarz in `X_I`, expansion with an independent `X'_J`, and product Fourier integration in the original independent `X_i` give the square bound. Jensen gives the fourth-power version. Difference coordinates remain independent with cap-one densities. |
| lines 331–374: `thm:determinant` | **PASS** | `H=alpha I+a^2 M^TM` generates the exact geometric frame. The BL coordinate scales, `c_j,d_i`, trace identity, cap-one difference norms, scalar Fourier powers with `p=2/d_i`, cancellation of `d_i` powers, and entropy bound on `c_j` are consistent. With `alpha=(2pi e)^2`, taking fourth roots yields `det(I+t^2 M^TM/(pi^2 e^2))^{-1/8}`. No leverage/rank/sign assumption is smuggled in. |
| lines 375–414: `Z_k`, Cauchy–Binet, volume envelopes | **PASS** | The determinant polynomial coefficients are exactly sums of squared physical minors. Keeping the order-`k` term gives exponent `k/4`. For `k=5`, power `5/4>1` gives density `<=5e Z_5^{-1/10}`; for `k=3`, the `3/4` tail is used only after the Riesz weight and gives the stated half-potential bound. |
| lines 415–438: scalar square/profile and definite pair | **PASS** | The two inverse square branches give the `|a|^{-1/2}|z-v|^{-1/2}` domination and the interval preimage bound. Conditioning produces a measure-domination inequality, not an independence statement. The definite 2D integral has Jacobian `1/(2 sqrt(|det B|))` and yields `pi M/sqrt(|det B|)` without assuming independence after rotation. |
| lines 439–486: `lem:hyperbola` | **PASS** | Hyperbolic coordinates cover the two branches with Jacobian `1/(2sqrt D)`. The tail monotonicity/cutoff estimates use one original coordinate and only cap/mass of its density. The middle region gives the logarithm; `Lambda>=2/sqrt D` converts it to `16sqrt(D)/|z-v|`. Rough-law use is correctly formulated through nonnegative tests/Tonelli. |
| lines 487–529: `lem:quarter` | **PASS** | Large diagonal uses the scalar inverse-image estimate. Otherwise random-sign symmetrization of the off-diagonal part gives a physical crossing with norm `>=L/4`; retaining its top singular-value factor in the determinant theorem gives the quarter-power Fourier tail. Gaussian smoothing and the gamma integral give the stated constant `<16`; layer cake gives `L_0=4+4log16` and no atoms. |
| lines 530–545: `def:pivot-volume`, `eq:small-entry` | **PASS** | `V_r` is over **ordered disjoint** physical row/column sets. Absence of a principal 2x2 pivot gives `|a_ij|^2 <= |a_ii a_jj| + |a_ii a_jj-a_ij^2| < eta^2+eta <2eta`, hence `|a_ij|<1/7`. |
| lines 546–572: `lem:sampling` (B07 core) | **PASS** | Sampling nonsingular ordered disjoint seeds with weight `det(B)^2/V_r` is normalized. The bordered determinant after eliminating the last row is `±det(B)(A_lm-A_lT B^{-1}A_Sm)`; sorting signs disappear after squaring. Each ordered disjoint `(r+1)` extension has at most `(r+1)^2` removed-row/removed-column antecedents. Singular seeds can have nonsingular extensions, so the proof correctly uses **inequality, not equality**. `P` has rank `<=r` and interpolates rows `S` and columns `T`. |
| lines 573–595: `lem:completion` (B07 core) | **PASS** | `E` is exactly the off-diagonal `LxL` interpolation residual; `D` is diagonal and zero on `S union T`; hence `R_LL=P_LL` and has rank `<=r`. `R-P` vanishes on rows `S`, columns `T`, and `LxL`, so all remaining support is in rows `T` or columns `S`; decomposing these contributes ranks `r+r`, giving global `rank R<=3r`. Neither symmetry nor a nonexistent rank-`2r` improvement is assumed. |
| lines 596–635: `prop:volume` | **PASS** | If `V_k<kappa^k`, telescoping/first-zero yields a small consecutive ratio. At `r=0`, the off-diagonal Frobenius norm plus diagonal bound gives `||A||<1`. For `1<=r<=4`, `||E||<=1/16`; the global rank `3r` shifts the `m=4k-3` singular index and produces at least `r+1` large diagonal `D` entries. These lie in `L` because `D` vanishes on the seed. On an `(r+1)`-set, diagonal entries of `R` exceed `371/400`, while the worst off-diagonal row sum is `<23/28`; strict diagonal dominance contradicts `rank R_LL<=r`. The nonsymmetric singular-value use is valid. |
| lines 636–648: `lem:cut` (B07 core) | **PASS** | Each ordered disjoint `(S,T)` of size `k` contributes to `Z_k(A_{I,J})` exactly when `S subset I`, `T subset J`, with probability `2^{-2k}=4^{-k}`. Linearity gives the exact expectation, hence one physical cut at least the mean. |
| lines 649–666: `cor:no-pivot` | **PASS** | From `Z_k>=4^{-k}kappa^k`, `Z_k^{-1/(2k)}<=2 kappa^{-1/2}=160`. The `k=3` full half-potential is `12sqrt(80e)=176.959...<200`; the `k=5` density is `800e=2174.625...<2400`. |
| lines 667–688: `lem:kernels` | **PASS** | Near the two square-root singularities, rescaling gives a fixed finite integral `<8`; away from them, `|x-d|>=|x|/2` produces the logarithmic term. The logarithmic-kernel integral is maximized by centered interval superlevel overlap and equals at most 8. |
| lines 689–720: `prop:pivot-H` | **PASS** | Scalar pivot: Schur leaves one large direction, profile + `J` + quarter-power log control gives `532.71...<600`. Definite pair gives `4pi eta^{-1/2}=125.66...`. Indefinite pair gives `432.38...<600`; `sup D^{-1/2}log_+D=2/e` is correct. The pivot alternatives are exhaustive. |
| lines 721–727: `prop:nine` | **PASS** | Pivot branch uses the preceding truncated bound; no-pivot branch has the stronger full half-potential `<200`. Outside `|Q-a|<=1`, the kernel is `<=1`, yielding the full `<=601` bound. |
| lines 728–759: proof of `thm:main` | **PASS** | No pivot uses the 17-direction density branch. Scalar pivot loses one Schur direction, leaving 16 and hence the nine-direction half-potential, giving `6010`. Definite pair gives `<40`. Indefinite pair loses two directions, leaving 15 and at least one, so the critical-value logarithmic potential is controlled; the resulting bound is `238.998...`. Conditioning is handled by test functions/Tonelli. Scaling `Y=KX` and `Q=(s/K^2) Qtilde` gives exactly `10000 K^2/s`. |
| lines 760–790: threshold accounting, limitations, acknowledgments, bibliography | **PASS (mathematics)** | The paper accurately distinguishes the global `3r` rank from the restricted `r` rank, the order-5 density exponent from the order-3 half-potential exponent, and explicitly does **not** claim `s_3` or continuity in all branches. Bibliographic references are attribution only and are not used as unproved dependencies. |

## B07 focused audit: ordered minors, bordered determinants, zero minors, multiplicities, random cuts

The critical combinatorial chain is sound.

1. **Ordered minors.** `V_r` counts ordered pairs `(S,T)` with `S cap T=empty`; this is exactly the object sampled in `lem:sampling`. No hidden factor `2` from swapping `S,T` is lost because the expectation and extension counting use the same ordered convention.
2. **Bordered identity.** For a fixed nonsingular seed `B=A_{S,T}` and `ell,m in L`, row elimination gives `det A_{S+ell,T+m}=±det(B)(A_{ell m}-A_{ell,T}B^{-1}A_{S,m})`. Only a sign can be introduced by re-sorting; squaring removes it.
3. **Zero/singular seeds.** They have zero sampling weight. A singular seed can nevertheless have a nonsingular extension; therefore the extension sum is bounded **above** by the full `(r+1)` volume with multiplicity `(r+1)^2`. The manuscript explicitly uses an inequality, so no missing-extension equality is assumed.
4. **Multiplicity.** For each ordered disjoint extension `(S',T')` of size `r+1`, there are exactly `(r+1)^2` choices of deleted row and deleted column before imposing seed nonsingularity; hence there are at most `(r+1)^2` sampled antecedents. This proves the expected Frobenius bound.
5. **Random cut.** A fixed ordered disjoint `(S,T)` of size `k` has `2k` distinct physical coordinates; the probability all rows land in `I` and all columns in `J` is exactly `2^{-2k}=4^{-k}`. No binomial or unordered multiplicity is missing.

As a finite regression only (not proof), I also checked the bordered identity/completion ranks on random exact rational symmetric examples and enumerated every fair cut for a random rational 6x6 matrix at `k=1,2,3`; the random-cut expectation discrepancy was exactly zero. The symbolic proof above, not these tests, is the basis of the verdict.

## Nonfatal GAP 1: projection proof indexing

**Location:** `lem:projection`, lines 265–283, specifically the step after `p(y)<=prod_{b_i>0}b_i^{-b_i/2}`.  
**Status:** `GAP`, locally repairable; theorem statement and downstream results remain correct.  
**Reason:** rows with `b_i=0` were dropped from the product. If the next displayed `sum_i(1-b_i)=d` is read over only retained rows, equality need not hold. For `U=e_1 in R^2`, the sole positive `b` is `1`, so that restricted sum is `0`, while `d=1`.  
**Repair:** write
`log p(y) <= (1/2) sum_{b_i>0}(1-b_i) <= d/2`,
or explicitly restore all rows on the right and define the `b=0` entropy contribution to be zero.  
**Downstream consequence:** none after this repair; the asserted `e^{d/2}` bound is unchanged and all scalar-Fourier/determinant constants remain valid.

## Repository-package GAP / still-UNCHECKED material

The current repository README says the root contains `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. Direct fetches on current `master` returned **Not Found** for all four; `proof_map.csv` was also absent at the pinned baseline commit. Therefore:

- **GAP (reproducibility/package):** the repository inventory claimed by README/AUDIT does not match what is presently accessible at the root.
- **UNCHECKED:** the claimed `verify.py` finite-check implementation and `checks.json` recorded results cannot be independently rerun/read from this repository state.
- **UNCHECKED:** the claimed `proof_map.csv` label/range map and `SOURCE_MANIFEST.json` cannot be audited.
- **UNCHECKED:** the compiled PDF hashes/visual rendering claims in the self-audit were not independently reproduced in this run; the proof audit was performed against the complete 790-line LaTeX source.
- **UNCHECKED:** I did not independently recompute the supplied SHA-256 from raw bytes. I did independently verify that the baseline and current-master `manuscript.tex` have the same git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, and the baseline commit exists with the expected 790-line manuscript addition.

These package gaps do **not** create a mathematical dependency gap because every specialized theorem used by the 17-direction proof is proved inside `manuscript.tex`. They should nevertheless be repaired before calling the repository bundle reproducible.

## Threshold-lowering audit outcome

No unconditional reduction below 17 is proved in this B07 run. The current B07 algebraic skeleton has a genuine sharp bookkeeping barrier: its global `rank R<=3r` estimate cannot simply be replaced by `2r`, and deleting the seed rows/columns before applying the restricted `rank<=r` estimate costs the same total `3r` spectral indices. I record the proof and an explicit rank-saturating example separately in the immutable improvement artifact for this run.

A separately completed leverage-conditional receiver in the repository shows that an order-three physical crossing with maximum row leverage `<=1/2` would already yield a bounded continuous density and, combined with the baseline `s_9` volume bound, a `9`-direction branch. But the baseline random-cut argument controls `Z_3`, not leverage, so this does not lower the theorem unconditionally. The missing structural implication is a product-coordinate-safe low-leverage crossing or a complete high-leverage route.

## Release status

- Mathematical 17-eigenvalue baseline: **PASS in this review**, subject to the local projection-proof wording repair above.
- Fatal mathematical issue: **none found**.
- Full-three-eigenvalue theorem: **not proved**.
- Independent-validation gate: **not self-awarded by this worker**; this report is one complete independent audit artifact and must be evaluated alongside genuinely separate complete reviews under the owner release protocol.
- Companion package completeness: **GAP / partially UNCHECKED** because the four README-listed files are absent from the accessible root.
