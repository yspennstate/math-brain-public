# account01/B03 end-to-end audit — run 20260924T134617Z-account01-B03-fixed-multiplicity-audit-r12

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and package

- Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Baseline path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
- Git blob read at that commit: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Owner/source-manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Source length: 790 lines, 47,883 bytes as recorded in `SOURCE_MANIFEST.json`; the connector read returned the pinned blob above.
- Fresh package files read in this run: `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and `manuscript.tex` lines 1–790 in full.

## Verdict

**PASS for the mathematical 17-eigenvalue theorem in this independent B03 reconstruction.** I found no fatal mathematical gap and no mathematical `UNCHECKED` source range in the 790-line manuscript. The exact theorem audited is

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent real coordinate densities bounded by `K`.

This audit is one worker report, not a self-awarded independent-validation certificate. The unrestricted three-eigenvalue theorem is not proved here. The manuscript claims only an essentially bounded density globally; continuity is proved only in the no-pivot Fourier-inversion branch.

## B03 lens: decoupling, copies, conditional independence, and exponents

### Lines 302–324 (`lem:decoupling`): PASS

For

\[
Z=F(X_I)+2X_I^TMX_J+G(X_J)
\]

with original-coordinate product banks, integrating first in `X_J` and applying Cauchy--Schwarz in the law of `X_I` gives

\[
|\phi_Z(t)|^2\le
\mathbb E_{X_I}
\left|\mathbb E_{X_J}e^{itG(X_J)+2itX_I^TMX_J}\right|^2.
\]

Expanding this square uses one genuinely independent copy `X'_J`. With `D=X_J-X'_J`, integration over the independent original coordinates `X_i`, `i in I`, gives

\[
|\phi_Z(t)|^2\le
\mathbb E_D\prod_{i\in I}|\widehat f_i(2t(MD)_i)|.
\]

The coordinate pairs `(X_j,X'_j)` are independent across `j`, hence the `D_j` are independent. Their densities are `f_j*\widetilde f_j<=1`; no conditioning on `X_j+X'_j` occurs and no false independence between a sum and difference is used. Jensen on the nonnegative right-hand side gives

\[
|\phi_Z(t)|^4\le
\mathbb E_D\prod_i|\widehat f_i(2t(MD)_i)|^2.
\]

All pre-estimate integrands have modulus at most one, so Fubini requires no moment assumption.

### Lines 283–301 (`lem:scalar-fourier`): PASS

For `p>=2`, taking `m=floor(p/2)` gives `2m<=p`, hence `|fhat|^p<=|fhat|^{2m}` because `|fhat|<=1`. The even power is integrable because it is bounded by `|fhat|^2`. It is the characteristic function of a sum of `m` independent differences; Fourier inversion at zero is legitimate and the manuscript's product-projection lemma gives the density cap `sqrt(e)/sqrt(2m)`. Therefore

\[
\int|\widehat f|^p\le 2\pi\sqrt{2e}/\sqrt p.
\]

The proof uses only original signed coordinates and deterministic coefficient norms, not independence after rotation.

### Lines 325–373 (`thm:determinant`): PASS

With `a=2t`, `alpha=(2*pi*e)^2` and `H=alpha I+a^2M^TM`, the vectors

\[
\sqrt\alpha H^{-1/2}e_j,
\qquad aH^{-1/2}m_i
\]

form the exact rank-one frame. The weights

\[
c_j=\alpha e_j^TH^{-1}e_j,
\qquad d_i=a^2m_i^TH^{-1}m_i
\]

lie in `[0,1]` and satisfy `sum d_i=sum(1-c_j)=theta`. The BL change-of-variables factors are correct. Since each difference density is cap one, `||g_j||_{1/c_j}<=1`. Applying the scalar Fourier-power lemma with `p=2/d_i` yields

\[
\|h_i\|_{1/d_i}\le(2\pi\sqrt{e d_i})^{d_i},
\]

which cancels the `d_i^{-d_i/2}` Jacobian factor. The coordinate entropy satisfies `prod c_j^{-c_j/2}<=e^{theta/2}`. With the chosen regularizer the residual scalar multiplier is exactly one. Taking fourth roots gives

\[
|\phi_Z(t)|\le
\det\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

The power bookkeeping is exact: an order-`k` crossing term therefore supplies the tail exponent `k/4`; `k=5` is directly `L^1_t`, while `k=3` is not and is used only after multiplication by `|t|^{-1/2}` in the Riesz estimate.

### Lines 374–400 (`Z_k`, `cor:vol-fourier`): PASS

Cauchy--Binet gives the stated coefficient identity. Retaining the `k`-th coefficient yields

\[
|\phi_Z(t)|\le\min\{1,(u_k/|t|)^{k/4}\},
\quad
u_k=\pi e Z_k(M)^{-1/(2k)}.
\]

For `k=5`, the power-envelope lemma gives `5e Z_5^{-1/10}`. For `k=3`, the Riesz-weighted integral gives the displayed negative-half-moment bound. The manuscript does **not** turn the order-three envelope into an `L^infinity` density claim.

## Complete line ledger

| Source range | Status | Independent check |
|---|---|---|
| 1–46 | PASS | notation, environments, abstract and scope agree with theorem; no hidden hypotheses. |
| 47–80 | PASS | theorem/corollary quantifiers, normalization architecture, pivot definition preview, and `9=4*3-3`, `17=4*5-3` accounting are consistent. |
| 81–120 | PASS | Fourier convention, Plancherel `2pi`, inversion `1/(2pi)`, Gaussian inversion, approximate-identity and weak-identification steps are correct for rough laws. |
| 121–160 | PASS | power envelope and Riesz half-potential constants/exponents reconstructed; Tonelli is applied only to nonnegative majorants. |
| 161–181 | PASS | approximation-number proof gives perturbation and rank inequalities for nonsymmetric matrices as used later. |
| 182–207 | PASS | Schur spectral-count lemma is sound. In the singular case, applying the invertible statement at threshold `t-|eps|` gives an ordered singular-value inequality for `S_eps`; continuity yields the endpoint `t` with no loss. |
| 208–217 | PASS | strict row diagonal dominance implies invertibility without symmetry. |
| 218–255 | PASS | geometric rank-one BL heat-flow sign, differentiation/integration by parts, large-time scaling, Lebesgue-point/Fatou limit and truncation are all closed. |
| 256–282 | PASS | projection density proof rotates only deterministic integration variables; no rotated independence. Zero frame weights are safely dropped and the entropy estimate gives `e^(d/2)`. |
| 283–301 | PASS | scalar Fourier powers and difference-density cap checked; see detailed B03 lens above. |
| 302–324 | PASS | decoupling/copies/conditional independence checked in detail above. |
| 325–373 | PASS | regularized determinant, frame weights, scalar powers, Jacobians and fourth-root exponent checked in detail above. |
| 374–400 | PASS | crossing-volume determinant expansion and order-5/order-3 conclusions checked. |
| 401–422 | PASS | square profile, interval preimage estimate and conditional measure domination are valid; no square/remainder independence is asserted. |
| 423–434 | PASS | definite two-coordinate coarea calculation yields `pi M/sqrt(|det B|)` after deterministic diagonalization only. |
| 435–482 | PASS | hyperbolic branches, Jacobian `1/(2sqrt D)`, original-coordinate tail monotonicity, bathtub estimate, middle interval and `Lambda>=2/sqrt D` give the displayed logarithmic envelope; exceptional critical level is handled in test-function form. |
| 483–525 | PASS | quarter-power concentration: diagonal case, random-sign cross block, determinant tail, Gaussian smoothing, Gamma integral and layer-cake logarithmic potential all check. |
| 526–544 | PASS | ordered disjoint volume definition and no-pivot entry bound are correct. |
| 545–564 | PASS | bordered-minor identity, `(r+1)^2` extension multiplicity, singular-seed inequality, rank and interpolation properties check. |
| 565–580 | PASS | `A=D+R+E`, support of `R-P`, global rank `<=3r`, restricted rank `<=r`, zero diagonal of `E`, and vanishing of `D` on the seed are exact. |
| 581–619 | PASS | ratio-drop alternative exhaustive; perturbation gives `r+1` large diagonal entries in the complement; numerical diagonal-dominance margins are strict; restricted-rank contradiction is valid. |
| 620–645 | PASS | fair-cut factor `4^-k`, order-3 full half-potential `<200` and order-5 density `<=800e<2400` follow with `Z_k^-1/(2k)<=160`. |
| 646–674 | PASS | full/truncated half-potential distinction is maintained; both singular-kernel bounds are Tonelli-safe. |
| 675–714 | PASS | scalar, definite-pair and indefinite-pair pivot alternatives all satisfy exact hypotheses; Schur survivor counts and logarithmic averaging are valid. |
| 715–724 | PASS | nine-eigenvalue proposition combines truncated pivot control or full no-pivot control correctly, then pays at most one outside `|Q-a|<=1`. |
| 725–749 | PASS | normalized main proof exhausts no-pivot/scalar/definite/indefinite cases; scalar pivot leaves 16 directions, indefinite pair leaves 15; scaling back gives exactly `K^2/s`. |
| 750–779 | PASS | threshold accounting and continuity limitations accurately describe what was proved. |
| 780–790 | PASS for theorem / attribution not re-audited | acknowledgment and bibliography are not proof dependencies because all specialized inputs used are reproved in the paper. No priority/novelty claim is validated by this audit. |

## Audit-package statuses

- `README.md`: **PASS** as a description of the current package and candidate scope.
- `proof_map.csv`: **PASS**; the listed statement/proof ranges match the source labels read in this run.
- `SOURCE_MANIFEST.json`: **PASS for internal consistency** with the connector-visible source blob and package paths. The SHA-256 value was read from the manifest/checker record; I did not independently recompute raw-file SHA-256 in this connector-only invocation.
- `verify.py`: **PASS for checker logic**. I audited the source-pin guard, exact interpolation identities, volume inequality, rank/support assertions, and the distinction between symbolic checks and floating diagnostics.
- `checks.json`: **RECORDED PASS / independent re-execution UNCHECKED in this run**. It records 534 exact interpolation seeds, 18 volume-sampling cases, 240 floating Schur-threshold cases and 30 graph-weight cases against the pinned SHA. This invocation did not rerun the script in the recorded Python/numpy/sympy environment. The analytic proof does not depend on those finite tests.
- Compiled PDF/build/render claims in the delivery metadata: **UNCHECKED in this run**; this audit is of the pinned LaTeX mathematics, not a reproduction of the binary build.

## Threshold-lowering status from the B03 lens

The previous B03 run proved that merely changing the leverage-free Jensen/copy power cannot make order four directly integrable: the best uniform scalar-Fourier input occurs at the manuscript's fourth-power choice, giving exactly the `|t|^{-1}` order-four endpoint. In this run I changed mechanism rather than repeating that barrier. The new improvement artifact for this run proves (i) a shared-environment split-row determinant estimate that can add crossing orders from two disjoint physical row packets without conditional recapping, and (ii) an unconditional order-four `L^r` endpoint/near-linear interval bound under the no-pivot `s_13` branch. Neither yet yields a universal `L^infinity` bound, so the unconditional fixed-multiplicity theorem remains at 17 after this B03 run.

## Review status

No fatal mathematical issue found. No manuscript mathematical range remains `UNCHECKED` in this B03 audit. Package execution/build claims explicitly marked above remain unrerun. This report does not claim that the owner's two-separate-end-to-end-review release gate has been formally discharged; peer artifacts must be reconciled by the designated release process.
