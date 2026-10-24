SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-24T12:46:41Z.
attacking: end-to-end audit of the pinned 17-eigenvalue manuscript, then a product-preserving lower-threshold replacement and exact counterexamples to tempting shortcuts.

# account02/B17 independent fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and package state

The mathematical source audited here is the owner's pinned baseline:

- repository: `yspennstate/math-open-problems`
- branch: `master`
- initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- package-declared SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- manuscript length: 790 source lines.

I directly read the complete `manuscript.tex` at the pinned blob, plus the package `README.md` and `AUDIT.md`. I also re-fetched line 1 at the initial source commit and confirmed that it resolves to the same git blob. I did **not** independently recompute the SHA-256 from raw bytes, so that SHA-256 remains `UNCHECKED` as an independently recomputed digest; it is recorded as package/owner metadata, not as my own hash calculation.

At the current master snapshot used for package retrieval, direct root-path fetches for `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` returned 404. This conflicts with `README.md`/`AUDIT.md`, which say those supplementary files are present. I therefore record a **GAP (package/reproducibility, not a mathematical proof defect)** and mark the missing files `UNCHECKED`. The complete mathematical paper is nevertheless present in `manuscript.tex`, as the current objective states.

## Overall mathematical verdict

**PASS — pinned 17-eigenvalue theorem, in this independent end-to-end mathematical review.**

I found no fatal mathematical gap in the theorem

`independent real coordinate densities <= K`, `A=A^T`, `s_17(A)>=s>0`, arbitrary affine `b,c`

implying

`||p_(X^TAX+b^TX+c)||_infinity <= 10000 K^2/s`.

This report is an independent mathematical review, not a release certificate, formal verification, novelty determination, or claim about the unrestricted three-eigenvalue conjecture.

## Exhaustive line-coverage ledger

Every manuscript source line is assigned below. The ranges are contiguous and cover lines 1--790 exactly.

| source lines | status | independently checked content |
|---|---|---|
| 1--100 | PASS | document definitions; singular-value convention; theorem and corollary quantifiers; normalized parameters; architecture; Fourier convention; Gaussian regularization; statement of Plancherel/inversion |
| 101--200 | PASS | Plancherel/inversion proof and rough-law limiting step; power envelope; Riesz negative-half moment and constants; singular-value perturbation/rank; Schur spectral-count setup |
| 201--300 | PASS | Schur proof including singular matrices; strict diagonal dominance; geometric rank-one Brascamp--Lieb heat-flow proof; product-projection density; scalar Fourier-power argument |
| 301--400 | PASS | completion of scalar Fourier powers; quadratic cross-block decomposition; two/fourth-power decoupling; regularized determinant theorem including Jacobian/frame weights; crossing-volume/Cauchy--Binet identities |
| 401--500 | PASS | order-five density and order-three half-potential receivers; scalar square profile; conditional domination; definite pair; first part of hyperbolic pair envelope |
| 501--600 | PASS | hyperbolic tails and constants; quarter-power concentration/log potential; pivot/disjoint-volume definitions; no-pivot entry bounds; volume-sampled interpolation; completion and rank support; start of spectral-to-volume proposition |
| 601--700 | PASS | spectral-to-volume rank contradiction and exact constants; random cut identity; no-pivot 9/17 analytic consequences; truncated half potential; two kernel lemmas; start of pivot-half-potential proposition |
| 701--790 | PASS | completion of pivot-half-potential proposition; nine-eigenvalue full half potential; all three main-theorem pivot/no-pivot branches; `K,s` scaling; interval/density equivalence; threshold accounting, limitations, bibliography |

No source line in `manuscript.tex` is left `UNCHECKED` by this review. The only `UNCHECKED` items are the missing supplemental files and independent SHA-256 recomputation / attribution-only literature verification, neither of which is used as a premise of the proof.

## Lemma/hypothesis audit

### 1. Fourier normalization and negative half moments — PASS

The convention `hat f(t)=int e^{itx}f(x)dx` gives Plancherel factor `2pi`, inversion factor `1/(2pi)`, and the Gaussian identity used in the manuscript. The Riesz calculation is consistent:

`int_0^infinity v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^(-1/2)`.

The order-three envelope `min(1,(u/|t|)^(3/4))` gives the weighted integral `12 sqrt(u)`, hence the stated `12 sqrt(u/(2pi))` bound. Rough laws are handled by nonnegative Tonelli/Gaussian regularization rather than pointwise density selection.

### 2. Singular values, nonsymmetry, and Schur counts — PASS

The perturbation/rank inequalities are singular-value statements and are valid for the nonsymmetric auxiliaries later used. In the Schur lemma, for invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`. Counting positive and negative inverse eigenvalues separately gives `N_S(t)>=N_A(t)-k`; the singular case is recovered by `A+epsilon I` and continuity. No false assertion about absolute-value interlacing of a principal compression is made.

### 3. Geometric Brascamp--Lieb and product projections — PASS

The heat-flow sign is correct: the frame identity makes

`sum c_i v_i^2 - |sum c_i u_i v_i|^2 >=0`.

The large-time Gaussian normalization and the `t downarrow 0` Fatou step are compatible with the stated truncation/monotone limit. In the projection lemma, rows with complementary leverage `b_i=0` may be discarded because their factors are bounded by one. The entropy estimate `-b log b <=1-b` yields `e^(d/2)`. No post-rotation independence is used.

### 4. Scalar Fourier powers — PASS

For `p>=2`, `m=floor(p/2)>=p/4`; because `|hat f|<=1`, the `2m` power dominates the `p` power in the needed direction. The sum of `m` independent differences is a one-dimensional projection of `2m` original independent cap-one variables; the projection lemma plus scaling gives the stated `2pi sqrt(2e)/sqrt(p)`. The density value at zero is legitimate because the integrable characteristic function furnishes a continuous inversion version.

### 5. Decoupling and regularized crossing determinant — PASS

The `|phi|^2` identity duplicates only the `J` bank after Cauchy--Schwarz in `I`; all same-bank phases have modulus one after expansion and integration over the original independent `I` coordinates gives the product of physical Fourier factors. Jensen gives the fourth-power version.

For the determinant theorem, the vectors

`sqrt(alpha) H^(-1/2)e_j`, `a H^(-1/2)m_i`

form an exact geometric frame. The one-dimensional Jacobians in the Brascamp--Lieb step are correct; `p=2/d_i>=2` matches the scalar Fourier lemma; the powers of `d_i` cancel; `prod c_j^(-c_j/2)<=e^(theta/2)`; with `alpha=(2pi e)^2` the residual entropy factor is exactly one. The fourth root produces exponent `-1/8` and coefficient `t^2/(pi^2 e^2)` as stated.

### 6. Crossing volumes and Fourier receivers — PASS

Cauchy--Binet gives the full elementary-symmetric expansion of `det(I+zM^TM)`. Retaining the `k`th term gives the `k/4` characteristic-function exponent. For `k=5`, inversion gives `5e Z_5^(-1/10)`; for `k=3`, the Riesz calculation gives `12 sqrt((e/2) Z_3^(-1/6))`. The manuscript correctly does **not** claim order three alone yields an integrable characteristic function.

### 7. Scalar/definite/hyperbolic pivots — PASS

The square-root profile is a conditional measure domination, not an independence statement. The definite pair uses only the joint cap after conditioning original coordinates. In the indefinite pair, the hyperbolic parameterization has Jacobian `1/(2 sqrt(D))`; the two tails are controlled by a one-dimensional cap-one bathtub against `1/|y|`; the middle interval has the stated logarithmic length; `Lambda>=2/sqrt(D)` converts the final scale. Exceptional critical levels are safely avoided by the test-function/Tonelli formulation.

### 8. Quarter-power concentration — PASS

If a diagonal pivot of the residual spectral direction is unavailable, the random-sign split extracts a literal cross block with operator norm at least `L/4`. Retaining one singular factor in the determinant theorem gives the `|t|^(-1/4)` envelope. Gaussian smoothing with `v=1/8` gives the stated quarter-power small-ball inequality; letting the radius decrease to zero excludes atoms. Layer cake then gives `L_0=4+4 log16` when `L>=1`.

### 9. Volume-sampled nonsymmetric interpolation — PASS

For an invertible disjoint seed `B=A[S,T]`, the interpolant

`P=A[:,T] B^(-1) A[S,:]`

is correctly left nonsymmetric. The bordered determinant identity is exact. An ordered disjoint `(r+1)`-minor can be generated by at most `(r+1)^2` deleted row/column choices; singular seeds can possess nonsingular extensions, so the manuscript correctly uses an inequality rather than equality. The completion has

`rank R<=3r`, `R[L,L]=P[L,L]`, `rank R[L,L]<=r`,

while `D` vanishes on the seed and `E` has zero diagonal. The support argument for `R-P` (rows `T` or columns `S`) is correct.

### 10. Spectral-to-volume conversion — PASS

For a bad ratio at seed order `r`, `||E||<=||E||_F<=(r+1)sqrt(kappa)`. Rank subtraction from `D+R=A-E` uses the **global** `rank R<=3r`, forcing at least `r+1` large diagonal entries when `m>=4r+1`. Because `D=0` on `S union T`, these entries lie in `L`, where the **restricted** rank bound `rank R[L,L]<=r` applies. With the manuscript constants,

`|R_ii|>=371/400`,

while for `r<=4` the off-diagonal row sum is `<23/28`; strict diagonal dominance forces an `(r+1)`-rank subblock and contradicts restricted rank. This is the central new 17-threshold mechanism and it checks out.

### 11. Random cut and no-pivot endpoints — PASS

Each ordered disjoint `k`-minor crosses a fair cut in the required orientation with probability `4^(-k)`, giving exact expectation `4^(-k)V_k`. For `k=3` and `k=5`, the resulting `Z_k^(-1/(2k))<=160` constants are correct. The nine-direction no-pivot branch yields the **full** half potential `<200`; the seventeen-direction branch yields a bounded continuous density `<800e<2400`.

### 12. Full versus truncated half potentials — PASS

The pivot proposition proves only the truncated potential `H(Q)<=600`; the no-pivot nine-direction estimate is a full potential. Proposition `prop:nine` correctly adds at most one for the tail `|Q-a|>1`, obtaining `<=601`. The main scalar pivot invokes this full half potential only after its Schur complement has at least nine surviving large eigenvalues. There is no hidden replacement of truncated by full potential.

### 13. Main theorem dependency closure and scaling — PASS

- no pivot + `s_17>=1`: direct density `<2400`;
- scalar pivot: Schur count `>=16`, hence `>=9`, square profile times full half potential `<=6010`;
- definite pair: conditional density `<40`;
- indefinite pair: Schur count `>=15`, only one surviving spectral direction is needed for the logarithmic potential, giving `<251`.

For general cap `K` and scale `s`, `Y=KX` has coordinate densities at most one and

`Q=(s/K^2) Qtilde`, `Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`,

so the density scales by `K^2/s`. This preserves arbitrary affine terms and all remaining spectrum.

## Exact adversarial checks against shortcuts

These are counterexamples to proof shortcuts, **not** counterexamples to the fixed-multiplicity theorem or to unrestricted QFORM.

### A. Absolute spectral count does not interlace under arbitrary principal compression

Take

`A=diag(1,-1)`.

Compress to the line spanned by `(1,1)/sqrt(2)`. The compression is `[0]`: the full matrix has two eigenvalues of modulus one, but the codimension-one compression has none. Thus a threshold reduction may not replace the Schur-complement inverse argument by naive absolute-value principal interlacing.

### B. Symmetrizing the interpolation can double rank and destroys the exact one-sided support bookkeeping

For `P=e_1 e_2^T`, `rank P=1`, while

`(P+P^T)/2`

has rank two. The baseline's nonsymmetric interpolation is therefore substantive; a shortcut that symmetrizes it before the rank count can lose exactly the gain being used.

### C. The `m=8` endpoint is not closed by the existing rank count

With a seed of order `r=2`, let the seed occupy coordinates `1,2,3,4`, `L={5,6,7,8}`, and set

`D=diag(0,0,0,0,1,1,0,0)`,

`R=diag(1,1,1,1,0,0,1,1)`, `E=0`.

Then `rank R=6=3r`, `rank R[L,L]=2=r`, `D` vanishes on the seed, and `D+R=I_8` has eight singular values equal to one. Only two large diagonal entries of `D` are forced, and a `2x2` diagonally-dominant restricted block is perfectly compatible with restricted rank two. This exact algebraic example shows why the baseline information alone cannot turn `8` into `9` by tighter constants. It is **not** asserted to arise from a no-pivot interpolated symmetric `A`; its purpose is to refute the rank-count shortcut itself.

### D. A two-direction density endpoint is genuinely dangerous

Let `U,V` be independent with density `1` on `[-1/2,1/2]`. Then the density of `U^2` is `h(s)=s^(-1/2)` on `(0,1/4)`, and therefore the density of `U^2-V^2` at zero contains

`int_0^(1/4) h(s)^2 ds = int_0^(1/4) ds/s = infinity`.

Thus an order-two/indefinite endpoint cannot simply be promoted from a half-potential or `|t|^(-1)` envelope to a bounded-density receiver. This is a source-valid rank-two obstruction, not an eight-eigenvalue QFORM counterexample.

## Package/reproducibility issues

| item | status | reason | impact / repair |
|---|---|---|---|
| `manuscript.tex` | PASS | full 790 lines read at pinned git blob | mathematical audit completed |
| `README.md` | PASS | read; theorem/source metadata consistent with manuscript | none |
| `AUDIT.md` | PASS as self-audit metadata | read in full; not used as proof evidence | none |
| `SOURCE_MANIFEST.json` | GAP / UNCHECKED | root-path fetch returned 404 at current master | restore/add file or correct README path; no theorem implication |
| `proof_map.csv` | GAP / UNCHECKED | root-path fetch returned 404 | restore/add; this review supplies independent contiguous line coverage meanwhile |
| `verify.py` | GAP / UNCHECKED | root-path fetch returned 404 | restore/add before claiming reproducible checker delivery |
| `checks.json` | GAP / UNCHECKED | root-path fetch returned 404 | restore/add before claiming recorded finite checks are repository-reproducible |
| package SHA-256 | UNCHECKED independently | metadata read, but raw-byte digest not independently recomputed in this connector run | git blob was independently pinned; digest should be recomputed once raw bytes are available |
| BCCT/RV attribution | UNCHECKED as prior-art attribution | no external literature audit in this B17 run | no dependency impact because specialized inequalities are reproved in manuscript |

## Baseline conclusion and next obligation

The **17-eigenvalue baseline passes this independent mathematical audit**. The reproducibility supplement is incomplete at the advertised root and should be repaired separately. The mathematical threshold can be lowered: my independent replacement proof is in the sibling B17 improvement artifact. It reaches **nine** eigenvalues with an explicit integer constant `5338 K^2/s`, while the eight-direction endpoint is reduced to a precise overlap-one/rank-two-triangle chamber rather than falsely declared solved.

The unrestricted three-eigenvalue QFORM conjecture remains OPEN; nothing in this audit asserts otherwise.
