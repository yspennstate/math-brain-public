# fleet01/B09 repeated end-to-end audit — fixed multiplicity 17

Run: `20260924T124412Z-fleet01-B09-FIXMULT-auto11`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
Declared source SHA-256 from objective: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
Fresh master before publication: `5d43209b89cb8889811e0dbf6ff55d284b539cc4`; canonical manuscript blob remains exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**PASS for the mathematical 17-eigenvalue theorem, with one nonfatal local wording/indexing GAP and one repository-package UNCHECKED/GAP.** I re-read the entire 790-line baseline source in this invocation and independently re-derived the B09-sensitive rank/spectral/diagonal-dominance chain before consulting newer peer improvements.

The theorem supported by the manuscript is exactly

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary dimension, arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, and arbitrary affine `b,c`.

This is a repeat review by the same fleet01/B09 worker and is **not** a new independent reviewer identity. It must not be counted as a second independent end-to-end review. The unrestricted three-eigenvalue problem remains open. Global continuity is not proved; the theorem gives an essentially bounded density, while the no-pivot Fourier branch separately gives continuity.

## Source ledger: every manuscript block

### Lines 1–100 — theorem, quantifiers, normalization plan, Fourier conventions: PASS

- `thm:main` states the correct product-law, matrix, affine and scaling quantifiers.
- The architecture distinguishes the nine-direction half-potential subproblem from the seventeen-direction density subproblem.
- No moment, support, log-concavity, Gaussian, diagonal-basis or rotated-independence hypothesis is inserted.
- The Fourier convention and Gaussian regularization are mutually consistent.

### Lines 101–200 — Plancherel/inversion, power envelope, Riesz half potential, singular-value perturbation, start of Schur count: PASS

- The Gaussian approximate-identity argument proves Plancherel at the stated normalization.
- `lem:envelope` integrates the power envelope correctly.
- `lem:riesz` has the correct constant `(2*pi)^(-1/2)` after the Gaussian integral; the `3/4` characteristic-function exponent is used only after multiplication by `|t|^{-1/2}`.
- `lem:rank` is correctly formulated for nonsymmetric matrices. The approximation-number identity gives both `|s_j(T)-s_j(U)|<=||T-U||` and the rank-shift inequality.

### Lines 201–300 — singular Schur count, strict diagonal dominance, geometric BL, product projection: PASS except GAP-PROJECTION-WORDING

- `lem:schur`: for invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`; positive and negative eigenvalue interlacing yields `N_S(t)>=N_A(t)-k`. The `A+epsilon I` limiting argument handles singular `A` without changing the pivot in the limit.
- `lem:dd` is the standard maximum-coordinate proof and does not require symmetry.
- `thm:bl`: the heat-flow sign is correct because the weighted frame operator is the identity. The compact-support heat-flow limit and monotone truncation are adequate.
- `lem:projection`: deterministic rotation is used only inside a marginal integral, not as an independence claim.

**GAP-PROJECTION-WORDING (nonfatal), source approximately lines 270–282, statement `lem:projection`.** After factors with `b_i=0` are dropped, the manuscript writes

`log p(y) <= (1/2) sum_i (1-b_i) = d/2`.

If the displayed sum is read as being only over retained indices `b_i>0`, equality need not hold. The correct statement is

\[
\sum_{b_i>0}(1-b_i)\le d,
\]

or, equivalently, equality holds if the sum is taken over all physical rows before the zero-`b_i` rows are dropped. Since only an upper bound is needed, changing `=` to `<=` repairs the line with no change in the theorem or constant `e^{d/2}`.

Downstream impact: none after this one-symbol/indexing repair. No theorem statement or later constant changes.

### Lines 301–400 — scalar Fourier powers, decoupling, regularized determinant, crossing volumes: PASS

- `lem:scalar-fourier` is not circular: `|fhat|^{2m}` is integrable by Plancherel plus `|fhat|<=1`, so inversion legitimately evaluates the convolution density at zero.
- `lem:decoupling` uses copies only within original coordinate banks; both powers two and four are correct.
- `thm:determinant`: the graph-frame identity is exact. The factors from BL, scalar Fourier powers and the entropy inequality cancel at `alpha=(2*pi*e)^2`, leaving
  `det(I+t^2 M^T M/(pi^2 e^2))^{-1/8}` after the fourth root.
- Cauchy–Binet gives the `Z_k` expansion. Retaining the order-`k` term produces exponent `k/4`, so `k=5` is integrable and `k=3` is suitable for the Riesz half potential.

### Lines 401–500 — scalar-square, definite-pair, hyperbolic-pair and beginning quarter-power concentration: PASS

- Scalar square profile and interval-preimage estimate are valid after conditioning on original coordinates.
- Definite pair uses a deterministic two-dimensional integral and never assumes independence after orthogonal diagonalization.
- Hyperbolic pair parametrization has Jacobian `1/(2 sqrt(|det B|))`; the tail estimate spends only one original-coordinate density cap and total mass. The critical level is handled through measure domination/Tonelli.
- The quarter-power concentration split correctly isolates a large diagonal or a large original-coordinate cross block.

### Lines 501–600 — quarter-power completion, disjoint-minor sampling, nonsymmetric completion: PASS

- The sign cut gives an original-coordinate cross block `M` with `||M||>=||S||/4`, and the determinant theorem supplies the `|t|^{-1/4}` envelope used under Gaussian smoothing.
- `lem:sampling`: the bordered determinant identity is correct up to sorting signs, removed by squaring. Singular seeds carry zero sampling weight; extensions of singular seeds are why the aggregate count is an inequality rather than an equality.
- `lem:completion`: with `E_LL=off(A_LL-P_LL)`, `D_ii=A_ii-P_ii` on `L` and zero on `S union T`, one has exactly `R_LL=P_LL` and hence `rank R_LL<=r`. The support of `R-P` lies in rows `T` or columns `S`, so `rank R<=rank P+2r<=3r`. Nonsymmetry causes no problem because only singular values and ranks are used.

### Lines 601–700 — B09 core: spectral-to-volume contradiction, random cut, no-pivot analytic consequences, singular kernels and pivot half-potential: PASS

For a bad ratio at order `r<=4`, the completion gives

\[
\|E\|_F\le(r+1)\sqrt\kappa\le1/16,
\qquad \operatorname{rank}R\le3r,
\qquad \operatorname{rank}R_{L,L}\le r,
\qquad D|_{S\cup T}=0.
\]

Let `m=4k-3`. Since `s_m(A)>=1`, nonsymmetric singular-value perturbation gives

\[
s_m(D+R)=s_m(A-E)\ge1-\varepsilon,
\]

and the rank shift gives

\[
s_{m-3r}(D)\ge1-\varepsilon.
\]

Because `m>=4r+1`, there are at least `r+1` diagonal entries of `D` of modulus at least `1-epsilon`. They lie in `L` because `D` vanishes on the seed coordinates. On `H subset L`, `|H|=r+1`,

\[
|R_{ii}|\ge1-1/16-1/100=371/400,
\]

while the no-pivot entry estimate and `||E||_F<=1/16` give

\[
|R_{ij}|<1/7+1/16\quad(i\ne j).
\]

As `r<=4`, the row off-diagonal sum is `<23/28`, and

\[
371/400-23/28=297/2800>0.
\]

Thus `R_HH` is strictly diagonally dominant and invertible of rank `r+1`, contradicting `rank R_LL<=r`. This checks the precise nonsymmetric rank perturbation, spectral count, seed-location and strict diagonal-dominance chain requested for B09.

The `r=0` case is also valid: `V_1=||off A||_F^2<kappa` and the no-pivot diagonal bound imply `||A||<1`. The fair-cut identity retains each ordered disjoint `k`-minor with probability `4^{-k}`. The resulting `k=3` and `k=5` analytic estimates have the stated roles.

The two singular kernel inequalities are used in the correct truncated/full roles. `prop:pivot-H` handles scalar, definite-pair and indefinite-pair pivots without assuming independence of the Schur remainder.

### Lines 701–790 — nine-direction half potential, main theorem, scaling, threshold accounting, regularity: PASS

- `prop:nine` combines pivot truncated half potential `<=600` with the no-pivot full half potential `<200`; the tail outside distance one is `<=1`, giving full half potential `<=601`.
- Main no-pivot branch: density `<2400`.
- Main scalar-pivot branch: the one-coordinate Schur complement retains at least sixteen large eigenvalues, hence enough for `prop:nine`; the density bound is `6010`.
- Main definite-pair branch: `<40`.
- Main indefinite-pair branch: two-coordinate Schur complement retains at least fifteen large eigenvalues; only one is needed for the logarithmic potential, giving `<251`.
- All branches are below `10000`.
- For general `K,s`, `Y=KX` has cap-one coordinate densities and `Q=(s/K^2) Qtilde`, giving exactly `K^2/s` after density scaling.
- The manuscript correctly does not claim global continuity. Only the no-pivot branch has an integrable characteristic function and therefore a continuous density.

## Supplementary package status

**UNCHECKED / repository-package GAP, nonmathematical.** At the fresh root listing during this invocation, only `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/` were present. The README-named `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` were not present. Therefore I could not independently read the manifest/proof map or rerun the advertised finite checker from the repository package. The compiled PDF is likewise not a repository blob according to the README. This does not create a mathematical dependency gap because the specialized proof is self-contained in `manuscript.tex`.

## Multiplicity reduction status

No unconditional reduction from 17 is proved by this audit. The exact existing B09 mechanism requires `m>=4r+1`; at the terminal order-five ratio `r=4`, `m=17` supplies five complement diagonal directions against restricted rank four. With `m=16`, it supplies only four, so the old contradiction saturates rather than closes.

A new quantitative terminal-r=4 determinant-escalation lemma was proved in the companion improvement for this run. It materially narrows the `s_16` survivor but does **not** yet prove a 16-eigenvalue density theorem because the low-residual volume-sampled seed need not be a globally maximal determinant seed and an iteration needs dimension-free control of seed multiplicities/weights.

## Final classification

- 17-eigenvalue mathematical theorem: **PASS** in this repeated fleet01/B09 audit.
- Fatal mathematical gap: **none found**.
- Local mathematical gap: **one nonfatal indexing/wording repair** in `lem:projection`.
- Supplementary reproducibility package: **UNCHECKED/GAP because the four README-named files are absent from the repository root**.
- Lower multiplicity theorem proved here: **none**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **not proved**; essential bounded density is the audited conclusion.

Next obligation: exploit the terminal `s_16`, `r=4` determinant-escalation geometry without a dimension-dependent seed-selection loss, or replace the order-five absolute-Fourier step by a genuine order-four endpoint `O(|I|)` theorem retaining arbitrary rough product laws and original-coordinate provenance.
