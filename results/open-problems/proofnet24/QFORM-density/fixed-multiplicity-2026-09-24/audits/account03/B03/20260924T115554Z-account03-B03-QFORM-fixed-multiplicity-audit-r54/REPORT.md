SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-24T11:55:54Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924, with B03 focus on decoupling, copies, conditional independence, Fourier exponents, and the order-four endpoint.

# account03/B03 independent end-to-end audit of the fixed-multiplicity manuscript

Run: `20260924T115554Z-account03-B03-QFORM-fixed-multiplicity-audit-r54`
Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Audited source repository: `yspennstate/math-open-problems`
Audited source commit named by the owner objective: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
Audited source git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
Audited source SHA-256 (owner manifest): `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
Current-master readback used for the full 790-line read had the same source blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent B03 audit, with one nonfatal wording repair and one repository-package reproducibility gap.** I found no fatal mathematical error in the source after an end-to-end read of `manuscript.tex`. This report is an independent scheduled-worker audit, not formal verification, peer review, or a self-awarded release certificate. The unrestricted three-large-eigenvalue conjecture remains OPEN.

The theorem actually audited is exactly: independent real coordinate densities bounded by `K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; if `s_17(A)>=s>0`, then `X^T A X+b^T X+c` has an essentially bounded density with

`||p||_infinity <= 10000 K^2/s`.

No continuity claim is made globally. The no-pivot Fourier branch is continuous; pivot branches are established as essential-density domination statements.

## End-to-end audit ledger

### 1. Theorem quantifiers, scaling, and architecture — PASS (source lines 1–100)

The statement retains arbitrary dimension, arbitrary signatures and remaining spectrum, arbitrary affine terms, and arbitrary rough product laws subject only to `0<=f_i<=K`. The normalization `Y=KX`, `A -> A/s`, together with `Q=(s/K^2)\widetilde Q`, gives the stated `K^2/s` density scaling. The paper does not insert a hidden moment, support, centering, Gaussianity, log-concavity, or post-rotation independence assumption.

### 2. Fourier normalization, inversion, power envelopes, and Riesz half-potential — PASS (lines 90–170)

Under the convention `\widehat f(t)=int e^{itx}f(x)dx`, the Plancherel constant `2pi`, Gaussian inversion, and density inversion constant `1/(2pi)` are mutually consistent. The Riesz calculation gives

`E|Z-a|^{-1/2} <= (2pi)^(-1/2) int |t|^(-1/2)|phi_Z(t)| dt`.

For the `3/4` power envelope the weighted integral is exactly `12 sqrt(u)`, hence `12 sqrt(u/(2pi))`. Extended-value/Tonelli usage is legitimate.

### 3. Singular-value perturbation and Schur spectral count — PASS (lines 160–220)

The rank perturbation statement is valid for nonsymmetric matrices because it is formulated for singular values. The principal-pivot Schur count

`N_S(t) >= N_A(t)-k`

is correctly obtained from the complementary principal block `S^{-1}` of `A^{-1}` and positive/negative interlacing, followed by the stated `A+epsilon I` limiting argument in the singular case. This is the exact count needed later after scalar and pair pivots.

### 4. Geometric Brascamp--Lieb heat flow — PASS (lines 220–275)

The frame identity makes the column operator a contraction, so the heat-flow derivative has the correct nonnegative sign. The large-time Gaussian limit yields the product of masses. The passage from bounded compactly supported functions to general nonnegative integrable functions is valid by monotone truncation, Fatou, and the stated Lebesgue-point/Fubini argument.

### 5. Product-projection density — PASS WITH LOCAL WORDING REPAIR (lines 270–300)

The proof of `||p_{U^T X}||_infinity <= e^{d/2}` is mathematically sound. There is one wording ambiguity after rows with `b_i=0` are dropped. If the later sum is read only over `b_i>0`, the manuscript's displayed equality

`sum_i (1-b_i)=d`

should be `sum_{b_i>0}(1-b_i)<=d`. Alternatively, retain the sum over all rows, in which case equality is correct and the omitted zero-`b_i` rows merely add nonnegative terms on the upper-bound side. Either local edit leaves the lemma and every downstream constant unchanged.

Status: **GAP (wording only), repaired locally by replacing `=` with `<=` under the restricted-index reading. Downstream theorem unaffected.**

### 6. Integrated scalar Fourier powers — PASS (lines 285–305)

For `p>=2`, `m=floor(p/2)>=p/4`, and `|\widehat f|<=1` gives the comparison to the `2m` power. That power is integrable because it is dominated by the `L^2` power, and Fourier inversion at zero identifies it with the density of a sum of independent signed differences. The product-projection lemma gives the stated `2pi sqrt(2e)/sqrt(p)` constant. The difference density is indeed bounded by one by convolution with a cap-one density.

## B03 deep audit: decoupling and crossing determinant (lines 301–400)

### 7. Two-copy decoupling — PASS

For

`Z=F(X_I)+2 X_I^T M X_J+G(X_J)`

with disjoint original-coordinate banks, integrating first in `X_J`, applying Cauchy--Schwarz only in the probability law of `X_I`, and expanding with an independent copy `X'_J` gives

`|phi_Z(t)|^2 <= E_D prod_{i in I} |\widehat f_i(2t(MD)_i)|`,

where `D=X_J-X'_J`. The coordinates of `D` are independent because the original coordinate pairs are independent; each difference density is cap one. Jensen then gives

`|phi_Z(t)|^4 <= E_D prod_i |\widehat f_i(2t(MD)_i)|^2`.

No step treats `X_j+X'_j` as independent of `X_j-X'_j`; in fact no conjugate sum is introduced. The arbitrary same-bank phases `F,G` are retained until their unit moduli are harmless. This is exactly dependence-safe decoupling.

### 8. Regularized crossing determinant — PASS

With `a=2t`, `alpha=(2pi e)^2`, `H=alpha I+a^2 M^T M`, and

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`,

the normalized coordinate vectors and row vectors form an exact geometric Brascamp--Lieb frame. The change of variables contributes `det(H)^(-1/2)`. The difference-density factors have the required `L^{1/c_j}` norms at most one, while

`|| |\widehat f_i|^2 ||_{1/d_i} <= (2pi sqrt(e d_i))^{d_i}`.

The `d_i` powers cancel their one-dimensional Jacobian factors. The entropy estimate on the `c_j` factors costs `e^{theta/2}`, and the choice `alpha=(2pi e)^2` cancels the remaining scalar factor exactly. Taking the fourth root gives

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

The determinant exponent and every use of independence check out.

### 9. Crossing-volume exponents — PASS

Cauchy--Binet gives the exact polynomial expansion in `Z_k(M)`. Keeping only the `k`th term yields

`|phi_Z(t)| <= min(1,(u_k/|t|)^(k/4))`, `u_k=pi e Z_k^(-1/(2k))`.

Thus `k=5` gives exponent `5/4>1` and an `L^1` characteristic function, while `k=3` gives exponent `3/4`, which is used only after the Riesz weight `|t|^{-1/2}`. The paper never promotes the `k=3` estimate directly to bounded density.

## 10. Coordinate pivots and singular kernels — PASS (lines 401–500)

The scalar-square profile is a measure-domination statement after conditioning on original coordinates, not an independence assertion. The definite pair calculation uses a deterministic two-dimensional change of variables and does not assume independence after diagonalization. The hyperbolic-pair proof keeps the original-coordinate product density on the parametrized level set; the logarithmic envelope and the critical-level exceptional set are correctly handled via nonnegative test functions and Tonelli.

The quarter-power concentration lemma is also consistent: when no diagonal coefficient carries the norm, a sign partition exposes an original-coordinate cross block with norm at least `L/4`; retaining one determinant factor gives `|t|^{-1/4}` and Gaussian smoothing gives the stated `rho^{1/4}` small-ball estimate. It does not use the refuted law-uniform pointwise quadratic-phase decay.

## 11. Nonsymmetric interpolation, support, and both rank bounds — PASS (lines 501–620)

For a nonsingular disjoint seed `B=A_{S,T}`, the interpolant

`P=A_{.,T} B^{-1} A_{S,.}`

has rank at most `r`, interpolates rows `S` and columns `T`, and need not be symmetric. The bordered-minor identity is exact. Omitting singular seeds makes the sampling count an inequality, in the correct direction.

In `A=D+R+E`, the construction has: `D` diagonal and zero on `S union T`; `E` zero-diagonal and supported only on `L x L`; `R_{L,L}=P_{L,L}` with rank at most `r`; globally `R-P` is supported in rows `T` or columns `S`, hence `rank R<=3r`. This is the precise distinction used later.

## 12. No-pivot spectral-to-volume conversion — PASS (lines 560–650)

If `V_k<kappa^k`, telescoping produces a ratio `V_{r+1}/V_r<kappa` or the first vanishing volume. The `r=0` branch contradicts `||A||>=1`. For `1<=r<=4`, `||E||<=1/16`. Rank perturbation by global rank at most `3r` forces at least `r+1` large diagonal entries of `D` when `m=4k-3>=4r+1`; these entries lie in `L` because `D` vanishes on the seed. On the resulting `(r+1)`-set, the displayed diagonal and off-diagonal estimates give strict row diagonal dominance of `R_{H,H}`, contradicting `rank R_{L,L}<=r`. The arithmetic is strict and the nonsymmetry is harmless because the diagonal-dominance lemma itself is nonsymmetric.

The fair random coordinate cut retains each ordered disjoint `k`-minor with probability `4^{-k}`, so `E Z_k(A_{I,J})=4^{-k}V_k(A)` exactly.

## 13. Full versus truncated half potentials and final theorem — PASS (lines 620–790)

The manuscript carefully separates the truncated potential `H(Q)` from the full half potential. Scalar and pair pivot envelopes give `H(Q)<=600` under two large directions; under nine large directions either this pivot estimate applies or the no-pivot `k=3` estimate controls the full half potential. Adding at most one outside the truncation yields `sup_a E|Q-a|^{-1/2}<=601`.

The main scalar-pivot branch leaves at least sixteen large directions in the Schur complement, hence enough for the nine-direction theorem, and gives `6010<10000`. Definite and indefinite pair branches are smaller. The no-pivot branch uses the `k=5` crossing estimate and gives `<2400`. The final scaling to arbitrary `K,s` is correct.

## Order-four endpoint: exact obstruction to an envelope-only 17 -> 13 reduction

The same algebraic scheme at `k=4` would need only `4k-3=13` large singular directions, but the determinant theorem yields only the borderline envelope `|phi(t)| <= C/|t|`. An envelope of this strength by itself cannot imply an `L^infinity` density.

A fully explicit witness is `W=UV` for independent `U,V ~ Uniform[-1,1]` (their input densities are `1/2<=1`). Its density is

`p_W(w)=(1/2) log(1/|w|) 1_{0<|w|<1}`,

which is unbounded. Its characteristic function is

`phi_W(t)=Si(t)/t`, `Si(t)=int_0^t sin(s)/s ds`.

For `|t|<=1`, `|Si(t)|<=|t|`; for `|t|>=1`, splitting at one and one integration by parts gives the crude uniform bound `|Si(t)|<=4`. Hence

`|phi_W(t)| <= min(1,4/|t|)`

although `p_W` is unbounded. Moreover the B03 negative-half collision resource is finite:

`int |t|^(-1/2)|phi_W(t)|^2 dt <= 32/3`.

Therefore neither the borderline `1/|t|` envelope nor finiteness of the whole-copy negative-half weighted integral alone can close the `k=4` density endpoint. This does **not** refute a genuine order-four QFORM endpoint theorem: it proves that such a theorem must use additional product/quadratic structure beyond the scalar Fourier envelope.

Status: **proved route obstruction, not a counterexample to the manuscript or to the QFORM conjecture.**

## Actual application of the designated account04/B03 result

I read `account04/B03` commit `da1d4e5510082c67ee7b34bbe70fde2060451518`, theorem `QFORM-B03-PAIR-IN-HUB-PLANCHEREL-v1`. For its concrete six-coordinate quadratic form

`Q_*=2RV+2RU_1+2VU_2+2U_1Y_1+2U_2Y_2`

with all six variables mutually independent and cap one, the theorem applies with `k=2`, `L=N=K=1`, `beta=1`, and therefore gives the actual inequalities

`||p_{Q_*}||_infinity <= 3`,

`int |t|^(-1/2)|phi_{Q_*}(t)|^2 dt <= (24/5)sqrt(pi) = 8.5077784843...`.

The coefficient matrix is the adjacency matrix of `P_6`, whose eigenvalues are `2 cos(j pi/7)`, so four eigenvalues have modulus greater than one. This is a real order-four/full-target chamber in which a second genuine physical Plancherel resource upgrades past the borderline `1/t` obstruction. It does **not** imply that every `Z_4>0` crossing arising in the fixed-multiplicity proof has the required pair-in-hub source decomposition; that structural implication remains unproved.

## Package/reproducibility GAP

At the master snapshot inspected during this run, the manuscript root contained `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/`. The README names `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but those files were not present in the root listing; a direct fetch of `proof_map.csv` returned 404.

Status: **GAP (repository packaging, not mathematical proof).** The manuscript itself is complete and was read in full; no finite-check claim from the missing checker files is treated here as independent proof evidence.

## Threshold result of this run

No rigorous global reduction below 17 is claimed. The current algebra would produce a `k=4` crossing under thirteen directions, but the scalar determinant envelope is exactly at the nonintegrable `1/t` endpoint. The explicit product witness above proves that an envelope-only or negative-half-collision-only argument cannot bridge that endpoint. The partner theorem shows one concrete mechanism that *can* bridge it when an additional source-disjoint physical Plancherel structure is available.

The next precise proof obligation for `17 -> 13` is therefore:

> Starting from the order-four crossing supplied by the manuscript's no-pivot interpolation/random-cut step, prove a product-coordinate structural refinement that supplies an additional source-disjoint Plancherel/smoothing resource (or another translation-uniform endpoint estimate), without assuming a conditional projection-density cap or deleting same-bank quadratic terms.

Until that implication is proved, 17 remains the lowest multiplicity certified by this audit.

## Status summary

- Mathematical 17-eigenvalue baseline: **PASS in this audit**.
- Fatal mathematical gap: **none found**.
- Local wording repair: product-projection sum after omitted zero rows (`=` -> `<=` if restricted to positive rows).
- Repository package: **GAP**, missing files named by README.
- Multiplicity reduction proved here: **none**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **OPEN**; no-pivot branch continuous, full theorem only essentially bounded.
- Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**; repository retrieval/writeback is separate from native learned-memory receiver use.
