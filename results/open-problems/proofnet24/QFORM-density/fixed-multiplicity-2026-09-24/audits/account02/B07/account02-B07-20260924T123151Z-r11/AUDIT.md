# account02/B07 end-to-end audit — fixed multiplicity 17

Run: `account02-B07-20260924T123151Z-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Starting lens: ordered minors, bordered determinants, sampling multiplicities; account02 counterexample emphasis.

## Source pin and package inventory

I audited the immutable manuscript content with git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, reported SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`. Its initial source commit is `7c0d6e60946b19423e6400a12d34b473cf0591e2`; the same blob remained present at master commits `c86b275521a4acad3df614a0e2a12d24f8cb7909` and final pre-write refresh `bf8c7ffa35c063180f10ce989cd1f7bfe530eb7e`.

Package inventory at the final pre-write refresh:

- `README.md`: **PASS / READ**.
- `manuscript.tex`: **PASS / READ IN FULL**, all 790 source lines covered below.
- `AUDIT.md`: **PASS / READ**, treated only as author self-audit, not validation.
- `SOURCE_MANIFEST.json`: **UNCHECKED / MISSING** from package root.
- `proof_map.csv`: **UNCHECKED / MISSING** from package root.
- `verify.py`: **UNCHECKED / MISSING** from package root.
- `checks.json`: **UNCHECKED / MISSING** from package root.

The README and self-audit describe the four missing files as package members. This is a **GAP (reproducibility/package, nonfatal to the symbolic theorem)**. Repair: restore those files at the stated source pin or amend README/AUDIT to say they are not repository-resident. Until then, their claimed finite-check output is not independently reproducible from this package.

## Overall verdict

**Mathematical 17-eigenvalue baseline: PASS in this audit, with one local wording GAP and no fatal mathematical defect found.** The theorem audited is exactly: independent real coordinates with densities bounded by `K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; if `s_17(A)>=s>0`, then `X^TAX+b^TX+c` has an essentially bounded density at most `10000 K^2/s`.

This is one scheduled-worker audit, not a peer-review certificate or formal verification. I do not claim the unrestricted three-eigenvalue QFORM conjecture is solved, and I do not lower 17 in this run.

## Complete source-line coverage

Every line of `manuscript.tex` was read. Status by contiguous source range and dependency:

- **Lines 1–179: PASS.** Definitions and theorem quantifiers; normalized parameters; Fourier convention; Gaussian regularization/inversion; power envelope; Riesz negative-half-moment formula; singular-value perturbation setup. Scaling and constants are dimensionally consistent.
- **Lines 180–259: PASS.** Nonsymmetric singular-value rank perturbation; Schur spectral count including singular limit; strict diagonal dominance; geometric rank-one Brascamp–Lieb heat-flow argument and limiting passage.
- **Lines 260–284: GAP, locally repairable.** `lem:projection` is mathematically correct, but after indices with `b_i=0` are dropped the entropy line writes `sum_i(1-b_i)=d`. For the remaining positive-`b_i` indices the exact statement is `sum_{b_i>0}(1-b_i) <= d`; omitted zero-`b_i` indices would each contribute one to the all-index sum. The proof only needs the inequality, so `||p_{U^T X}||_infty <= e^{d/2}` and all downstream constants remain valid. Repair this equality sign/quantifier only.
- **Lines 285–519: PASS.** Integrated scalar Fourier powers; two-copy decoupling; regularized crossing determinant; crossing-volume expansion; order-5 density and order-3 half-potential envelopes; square/definite/hyperbolic pivot estimates; quarter-power concentration. Hypotheses are invoked with original-coordinate independence only; deterministic rotations do not assert rotated independence.
- **Lines 520–620: PASS, B07 detailed audit below.** `V_r`, no-pivot entry bound, volume-sampled interpolation, completion with global/restricted ranks, and spectral-to-volume contradiction.
- **Lines 621–790: PASS.** Random-cut multiplicity; no-pivot analytic consequences; truncated/full half-potential distinction; kernel bounds; pivot half-potential; nine-eigenvalue bound; main case split, Schur counts, normalization/scaling; threshold limitations and continuity scope.

No line remains mathematically UNCHECKED in the manuscript itself. The absent supplementary files remain UNCHECKED as files.

## Statement-level dependency audit

### Fourier and measure inputs — PASS

`lem:fourier`, `lem:envelope`, and `lem:riesz` have consistent transform normalization. The weighted `|t|^{-1/2}` Riesz integral is used with the order-three `|t|^{-3/4}` envelope; the manuscript never promotes that envelope to direct `L^1` inversion. Gaussian regularization and Tonelli are applied to nonnegative or integrably dominated expressions.

### Spectral and Schur inputs — PASS

`lem:rank` is valid for nonsymmetric auxiliaries by singular-value approximation. `lem:schur` correctly loses at most the pivot dimension: for invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`, and positive/negative interlacing applied to `A^{-1}` gives the absolute-value count; the singular case follows by an `A+epsilon I` limit while retaining the pivot. `lem:dd` needs no symmetry and is used in precisely that scope.

### Geometric BL / projections — PASS with the local projection wording GAP above

The heat-flow derivative has the correct sign from the Parseval-frame contraction. The large-time Gaussian limit and the monotone approximation to rough nonnegative inputs are legitimate. The product-projection proof uses only original coordinate product structure. Replacing `=` by `<=` in the entropy sum closes the only local wording gap I found.

### Decoupling / determinant / crossing volumes — PASS

The `|phi|^2` decoupling expands one independent copy of `X_J`; Jensen gives the fourth power. In the determinant theorem the frame weights `c_j,d_i`, determinant Jacobian, `d_i` cancellation, entropy factor, and regularizer `alpha=(2 pi e)^2` yield exactly

`det(I + t^2 M^T M/(pi^2 e^2))^(-1/8)`.

Cauchy–Binet gives the stated `Z_k`; retaining the order-`k` term gives exponent `k/4`. Thus `k=5` is integrable and gives density; `k=3` is used only with the half-potential Fourier weight.

### Pivot kernels and rough laws — PASS

Scalar completion gives a conditional density domination, not an independence claim. Definite and indefinite two-coordinate changes of variables are deterministic. The hyperbolic tail estimate uses only cap-one coordinate densities and their mass. The quarter-power lemma either conditions on an original scalar pivot or creates an original-coordinate bipartite cut; no forbidden post-rotation independence occurs.

## B07 audit: ordered minors, borders, multiplicities

### `V_r` definition and ordered-pair convention — PASS

`V_r` sums over **ordered** pairs `(S,T)` of disjoint `r`-sets, while rows and columns inside each minor are written in increasing order. Therefore `(S,T)` and `(T,S)` are distinct summands unless literally identical (which disjoint positive-size sets cannot be). This convention is consistent in the sampling lemma and random-cut lemma.

### Bordered determinant identity — PASS

For a nonsingular seed `B=A_{S,T}` and `ell,m` outside the seed, Schur row elimination gives, before sorting,

`det [[B, A_{S,m}],[A_{ell,T},a_{ell m}]] = det(B)(a_{ell m}-A_{ell,T}B^{-1}A_{S,m})`.

Sorting `S union {ell}` and `T union {m}` into increasing order may contribute independent row and column permutation signs. Squaring removes their product exactly. There is no missing absolute sign in the squared identity used by the proof.

### Sampling multiplicity `(r+1)^2` — PASS and sharp as a worst-case count

Fix an ordered disjoint extension `(S',T')` with `|S'|=|T'|=r+1`. It can arise by choosing one removed row `ell in S'` and one removed column `m in T'`, at most `(r+1)^2` choices. Each choice determines the child seed `(S'\{ell},T'\{m})`. If that child determinant is singular it has zero sampling weight, so the aggregate relation is an **inequality**, not equality. If all child seeds are nonsingular, all `(r+1)^2` choices can contribute; hence the manuscript's coefficient is the correct uniform combinatorial bound.

### Seed-selection quantifier — PASS

Sampling probability is `det(B)^2/V_r` over nonsingular disjoint seeds. The weights sum to one because singular seeds contribute zero to `V_r`. The expectation bound therefore implies existence of at least one nonsingular seed satisfying the Frobenius estimate. No universally good individual `(r+1)` minor is inferred.

### Completion support and rank — PASS

With `E_{L,L}=off(A_{L,L}-P_{L,L})` and zero elsewhere, `D` is diagonal and vanishes on `S union T`, while `R_{L,L}=P_{L,L}` has rank at most `r`. Globally `R-P` vanishes on rows `S`, columns `T`, and `L x L`; the remaining support is contained in rows `T` or columns `S`. Splitting those two pieces gives global `rank R <= r+r+r=3r`.

The factor `3r` cannot simply be replaced by `2r`. An exact `r=1` witness is

`A0 = [[-2,-2,-2],[-2,-2,-1],[-2,-1,-2]]`, seed `S={1}`, `T={2}` (1-based first/second coordinates). Its completion has `rank R=3`. Scaling by `1/250` gives

`A = [[-1/125,-1/125,-1/125],[-1/125,-1/125,-1/250],[-1/125,-1/250,-1/125]]`.

This scaled witness also satisfies the manuscript's no-pivot entry-size conditions (`|a_ii|=1/125<1/100`, and every principal 2x2 determinant has modulus below `1/100`) while preserving rank 3. It is an algebraic counterexample to any blanket `rank R<=2r` repair. It is not a counterexample to the theorem, because it does not satisfy the large-spectrum hypothesis.

### Spectral-to-volume conversion — PASS

If `V_k<kappa^k`, telescoping (or first vanishing volume) gives `V_{r+1}<kappa V_r` for some `0<=r<=k-1`. For `r>=1`, sampling/completion gives `||E||<=1/16`, global rank at most `3r`, and restricted rank at most `r`. With `m=4k-3>=4r+1`, rank perturbation forces at least `r+1` diagonal entries of `D` of modulus at least `1-epsilon`. They lie in `L` because `D` vanishes on the seed. On such an `(r+1)`-set,

`|R_ii| >= 371/400`, while each off-diagonal `|R_ij|<1/7+1/16`; for `r<=4`, the row sum is `<23/28`. The strict slack is

`371/400 - 23/28 = 297/2800 > 0`.

So `R_HH` is invertible of rank `r+1`, contradicting `rank R_LL<=r`. The `r=0` branch is independently closed by the Frobenius norm of `off A`.

### Random coordinate cut — PASS and exact

For a fixed ordered disjoint `(S,T)` with `|S|=|T|=k`, the event `S subset I` and `T subset J` prescribes all `2k` independent fair labels, hence has probability `2^{-2k}=4^{-k}`. Therefore `E Z_k(A_{I,J})=4^{-k}V_k(A)` exactly.

Sharp `k=1` diagnostic: for `A=[[0,7],[7,0]]`, `V_1=98`, while averaging `Z_1` over all four fair cuts gives `49/2=V_1/4`. Thus the factor cannot be replaced by `1/2` under this ordered convention.

## Adversarial finite diagnostics (diagnostic only)

Using exact rational/integer arithmetic independent of the absent package checker:

- 4,708 bordered squared-determinant identities checked on random symmetric integer matrices (`n=4,5,6`, `r=1,2`), including seeds where sorted extension indices induce signs: all passed.
- 48 exact aggregate sampling-expectation inequalities checked: all passed.
- 45 exact random-cut expectation identities checked by enumerating all `2^n` cuts for `n=2,...,6` and admissible `k<=3`: all passed.
- The `r=1` completion witness above attains global rank `3r`, falsifying the tempting `2r` shortcut.

Numerical constant recomputation (not a proof substitute): quarter-power coefficient `3.99525936158<16`; hyperbolic near-region constant `7.19677149719<8`; no-pivot half-potential `176.959336187<200`; no-pivot density `2174.62546277<2400`; diagonal-dominance slack `297/2800`; scalar-pivot main bound `6010<10000`.

## Threshold reduction audit

No complete lower-threshold replacement theorem is proved here. The natural same-architecture attempt at `k=4` would combine the algebraic count `4k-3=13` with the determinant envelope exponent `k/4=1`. That gives only a crude `|t|^{-1}` characteristic-function envelope, which is borderline nonintegrable and does **not** yield an `L^infty` density by absolute Fourier inversion. Therefore a claimed `17 -> 13` improvement based only on substituting `k=4` is **FALSE as a proof step**.

Likewise, replacing the global interpolation rank `3r` by `2r` to lower the spectral count is **FALSE in general**, as the explicit scaled no-pivot witness above shows.

A genuine improvement must supply either (i) an endpoint order-four density/small-ball theorem that survives arbitrary same-side curvature, affine terms and cap-one product laws, or (ii) a different structural decomposition with a proved smaller global rank while retaining the needed restricted rank. Until such a complete replacement is supplied, 17 is the lowest multiplicity certified by this audit.

## Final ledger

- Theorem quantifiers/scaling: **PASS**.
- Fourier normalization/inversion/Riesz: **PASS**.
- Schur spectral count and nonsymmetric singular-value use: **PASS**.
- Geometric BL heat flow/rough limit: **PASS**.
- Product projection: **GAP (local wording only)**; replace the positive-`b_i` entropy equality by `<= d`.
- Scalar Fourier powers: **PASS**.
- Decoupling and regularized determinant: **PASS**.
- Crossing-volume expansion/exponents: **PASS**.
- Scalar/definite/hyperbolic pivots and quarter concentration: **PASS**.
- Ordered-minor definition: **PASS**.
- Bordered determinant signs: **PASS**.
- Sampling multiplicity and seed quantifier: **PASS**.
- Completion support/global rank/restricted rank/seed vanishing: **PASS**.
- No-pivot spectral-to-volume contradiction: **PASS**.
- Random-cut multiplicity `4^{-k}`: **PASS**.
- Truncated vs full half-potential chain: **PASS**.
- Main 17-eigenvalue proof: **PASS**.
- `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`: **UNCHECKED / MISSING**, package reproducibility GAP.
- Complete reduction below 17: **UNCHECKED / NOT ESTABLISHED**; no improvement claimed.
- Unrestricted three-eigenvalue QFORM: **OPEN; not claimed solved**.

Next obligation: prove a true `k=4` endpoint receiver (or a different complete structural replacement) before asserting multiplicity 13 or lower; separately restore/correct the missing reproducibility package files and apply the local projection-line repair.
