# account01/B06 complete audit — fixed-multiplicity theorem

Run: `20260924T140420Z-account01-B06-fixedmult-audit-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Source: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, 790 lines.

## Verdict

**PASS for the mathematical 17-eigenvalue theorem, with one nonfatal local wording/indexing GAP in the proof of the product-projection lemma.** I found no FALSE statement and no theorem-breaking GAP. Every manuscript line was read in this invocation. There is no source range left UNCHECKED for mathematical correctness in this review.

The audited conclusion is exactly

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, arbitrary affine `b,c`, and independent arbitrary real coordinate laws with densities bounded by `K`. This review does **not** establish the unrestricted three-eigenvalue conjecture. It is a repeated review by the same `account01/B06` worker identity and is not a second independent reviewer.

## Complete source ledger

### Lines 1–90 — front matter, theorem, quantifiers, architecture: PASS

- The theorem has the intended quantifiers and only the stated density-cap hypothesis.
- The normalization plan separates the order-three half-potential argument from the order-five density argument.
- No Gaussianity, moments, support, log-concavity, diagonal-basis assumption, spectral truncation, or rotated-coordinate independence is inserted.
- The text correctly promises only an essentially bounded density globally; continuity is later asserted only where Fourier integrability proves it.

### Lines 91–160 — Fourier identities, power envelope, negative half moments: PASS

- The Gaussian regularization and Fourier normalization are consistent: Plancherel has factor `2*pi`, inversion factor `1/(2*pi)`, and the Gaussian identity has the stated prefactor.
- The approximate-identity limit is justified in `L^2`; the inversion argument identifies the limiting continuous density when `phi in L^1`.
- The power-envelope integral is exact.
- The Riesz representation and the `|t|^{-1/2}` Fourier weight give the displayed constant. The order-three characteristic exponent is never misused as a direct `L^1` Fourier bound.

### Lines 161–217 — singular values, Schur spectral count, diagonal dominance: PASS

- The singular-value approximation formula proves both perturbation and rank-shift inequalities for nonsymmetric matrices.
- For an invertible principal pivot, the complementary block of `A^{-1}` is `S^{-1}`; positive/negative compression interlacing yields `N_S(t)>=N_A(t)-k`.
- The `A+epsilon I` limiting argument handles singular `A` while the fixed pivot remains invertible for small epsilon and the Schur complement converges.
- Strict diagonal dominance is used in a form valid without symmetry.

### Lines 221–257 — geometric rank-one Brascamp--Lieb: PASS

- The heat-flow derivative has the correct sign because the weighted frame map is a contraction/Parseval operator.
- Differentiation and integration by parts are justified first for compactly supported bounded data; the large-time Gaussian limit uses `sum c_i=d`; Fatou and monotone truncation correctly pass to rough nonnegative integrable inputs.

### Lines 258–282 — product projections: **GAP (nonfatal wording/indexing only)**

The proof is mathematically repairable without changing the statement or constant. After rows with `b_i=0` are dropped, the argument obtains

\[
\log p(y)\le\frac12\sum_{b_i>0}(1-b_i).
\]

The manuscript then writes this sum as `d/2`. If the displayed sum is read as still restricted to `b_i>0`, equality is not generally true. The correct line is

\[
\frac12\sum_{b_i>0}(1-b_i)
\le \frac12\sum_i(1-b_i)=\frac d2,
\]

because `b_i=1-|U^T e_i|^2` and `sum_i |U^T e_i|^2=d`. Equivalently, one may explicitly reinsert the omitted nonnegative zero-`b_i` terms before using equality. This is a one-symbol/indexing repair; `||p_{U^TX}||_infty<=e^{d/2}` and every downstream result are unchanged.

### Lines 284–301 — integrated scalar Fourier powers: PASS

- `|fhat|^{2m}` is integrable by Plancherel and `|fhat|<=1`; Fourier inversion therefore legitimately evaluates the convolution density at zero.
- The product-projection scalar bound is applied to original independent signed coordinates with coefficient norm `sqrt(2m)`.

### Lines 303–400 — decoupling, graph determinant, crossing volumes: PASS

The B06-sensitive determinant calculation was independently rederived. With

\[
a=2t,\qquad \alpha=(2\pi e)^2,\qquad H=\alpha I+a^2M^TM,
\]

and

\[
c_j=\alpha e_j^TH^{-1}e_j,\qquad d_i=a^2m_i^TH^{-1}m_i,
\]

the graph vectors form a Parseval frame and

\[
\theta=\sum_i d_i=\sum_j(1-c_j).
\]

The substitution `x=H^{-1/2}z` contributes exactly `det(H)^(-1/2)`. Geometric BL contributes the one-dimensional scaling factors `alpha^(c_j/2)c_j^(-c_j/2)` and `d_i^(-d_i/2)`. The scalar Fourier-power lemma contributes `(2*pi*sqrt(e*d_i))^(d_i)`, so the powers of `d_i` cancel. The entropy estimate contributes at most `e^(theta/2)`, and

\[
(2\pi e/\sqrt\alpha)^\theta=1.
\]

Thus the fourth-power decoupling gives

\[
|\phi_Z(t)|^4\le
\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/2},
\]

and the fourth root is exactly exponent `-1/8`. There is no missing Jacobian, factor two, trace term, or post-rotation independence claim. Cauchy--Binet and the order-three/order-five consequences have the correct exponents and constants.

### Lines 404–525 — scalar square, definite pair, hyperbolic pair, quarter-power concentration: PASS

- The scalar square formula and interval-preimage length are correct after conditioning on original coordinates.
- The definite pair argument is a deterministic change of variables in a two-dimensional integral; it does not rotate independent random variables and then assume independence.
- The hyperbolic parametrization has Jacobian `1/(2*sqrt(D))`; both tails spend an original-coordinate density and total mass, and the critical level is handled in measure-domination/Tonelli form.
- The sign-splitting argument produces an original-coordinate crossing with operator norm at least `L/4`; the Gaussian-smoothed Fourier estimate yields the stated quarter-power concentration and logarithmic moment bound.

### Lines 528–645 — disjoint-minor sampling, nonsymmetric completion, spectral-to-volume conversion, random cut: PASS

- The bordered determinant identity is exact up to sorting signs, removed by squaring. Singular seeds have zero sampling weight and are the reason the aggregate relation is an inequality rather than an equality.
- In the completion, `E_LL=off(A_LL-P_LL)`, `D` is diagonal and vanishes on `S union T`, `R_LL=P_LL`, `rank R_LL<=r`, and the support of `R-P` gives `rank R<=3r`.
- For a bad ratio at `r<=4`, `||E||_F<=(r+1)sqrt(kappa)<=1/16`. With `m=4k-3`, perturbation and the global rank bound force at least `r+1` large diagonal entries of `D`; they lie in `L`. The strict diagonal-dominance margin is positive, contradicting `rank R_LL<=r`.
- The `r=0` case and the fair-cut factor `4^{-k}` are correct.
- The no-pivot order-three bound is used only for the half potential; order five gives the density bound.

### Lines 650–724 — singular kernels, pivot half potential, nine-direction bound: PASS

- Both singular-kernel inequalities are used in their stated truncated/full roles.
- Scalar, definite-pair, and indefinite-pair pivot alternatives exhaust the pivot definition and preserve original-coordinate conditioning.
- The Schur complement hypotheses invoked in each pivot branch match the needed spectral count.
- `prop:nine` correctly upgrades the truncated `<=600` estimate to a full half potential `<=601` by bounding the outer kernel by one.

### Lines 726–790 — main theorem, scaling, threshold accounting, limitations and references: PASS

- No-pivot branch: `<2400`.
- Scalar pivot: the one-coordinate Schur complement retains at least sixteen unit-scale eigenvalues, hence the nine-direction half-potential theorem applies and gives `6010`.
- Definite pair: `<40`.
- Indefinite pair: the two-coordinate Schur complement retains at least fifteen directions; one is enough for the logarithmic potential, giving `<251`.
- Scaling `Y=KX`, `A->A/s`, and `Q=(s/K^2) Qtilde` yields exactly the factor `K^2/s`.
- The final limitations correctly state that the three-eigenvalue theorem and global continuity are not proved.
- The two bibliography entries are attribution/background only; no mathematical step depends on importing an unstated result.

## Support package audit

`README.md`, historical `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` were all present and read in this invocation. The manifest matches the pinned source blob/hash/size/line count. `verify.py` pins the same SHA-256 and its reported `checks.json` counts are internally consistent with the currently supplied checker: 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict cases, 240 Schur diagnostics, and 30 graph-weight diagnostics. These checks are correctly labelled finite diagnostics rather than proof.

The older historical `AUDIT.md` lists a different, larger test suite. `README.md`, `SOURCE_MANIFEST.json`, and `DELIVERY_STATUS.md` explicitly say the new checker is a newly supplied scoped suite and does not reproduce the historical counts. That difference is therefore **not** evidence of a mathematical failure; the historical counts themselves were not rerun by the present checker.

## Lower-threshold status after this audit

The baseline interpolation proof cannot simply replace 17 by 16. In the terminal `r=4` chamber, `s_16` forces four large diagonal coordinates after the global rank-12 loss, while `rank R_LL` is allowed to equal four. The contradiction used at 17 genuinely disappears. Separate repository examples show the `3r` global rank and `r` restricted rank can both be sharp for this construction.

A companion improvement from this run gives a new direct three-bank density receiver in the exact terminal `s_16` collar by combining the already-proved exact-rank physical-crossing theorem with the quantitative determinant transfer. It materially weakens the reciprocal determinant cost but does **not** yet remove it. Therefore the same-scope unconditional fixed multiplicity remains **17** in this run.

## Classification summary

- Mathematical 17-eigenvalue theorem: **PASS**.
- Fatal defect: **none found**.
- FALSE source statement: **none found**.
- Nonfatal GAP: **product-projection proof, lines 258–282; replace a displayed equality by an inequality/reinsert zero-`b_i` terms**.
- Manuscript mathematical source ranges UNCHECKED: **none**.
- Supplementary files requested by the owner: **all present and read**.
- Unconditional multiplicity proved here: **17**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **not proved; essential bounded density is the audited conclusion**.
