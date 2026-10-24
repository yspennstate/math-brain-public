# account01/B17 independent end-to-end audit — fixed-multiplicity baseline

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Run: `20260924T133655Z-account01-B17-fixedmult-auto11`.

Pinned mathematical source read in full at repository head `ec8b5e4a2fe31c23e1eaa7aa0b51f2ef5833795e` before concurrent later commits. The manuscript blob is unchanged from the baseline:

- baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- manuscript size/line count reported by the pinned manifest and connector metadata: 47,883 bytes / 790 lines.

I read `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and all 790 source lines of `manuscript.tex`. I did not use earlier PASS reports as substitutes for the checks below.

## Overall verdict

**Mathematical baseline verdict: PASS.** I found no fatal gap in the written seventeen-eigenvalue theorem. The proof is internally self-contained at the stated constants and retains arbitrary independent one-dimensional densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine terms, arbitrary signature, dimension and remaining spectrum.

**Independent-validation status: NOT AWARDED.** This file is one actual independent review only. The owner requires two genuinely separate full reviews and reconciliation of any conflicts before a candidate is marked independently validated.

**Packaging/computation items not rerun locally in this invocation: UNCHECKED where stated below.** In particular I did not regenerate the PDF or independently recompute the manuscript SHA-256 byte hash from a local materialized copy. The Git blob and source contents read through the connector match the pinned source identity.

No fatal defect was found, so there is no fatal-defect notice to publish.

## End-to-end source audit

The ranges below are source lines in `manuscript.tex` and match the pinned `proof_map.csv`.

| Lines / label | Verdict | Independent check and reason | Downstream impact / next obligation |
| --- | --- | --- | --- |
| 1–46, preamble/abstract/conventions | PASS | Packages/macros are standard; abstract accurately states the 17-direction candidate, nonsymmetric interpolation role, fifth crossing volume, pivot treatment, and self-contained analytic ingredients. No theorem-strengthening claim appears here. | None. |
| 47–57 `thm:main` | PASS | Quantifiers are complete: arbitrary independent coordinate densities `<=K`, arbitrary symmetric `A`, arbitrary `b,c`, `s_17(A)>=s>0`, density bound `10^4 K^2/s`. | Main proof at 726–749 checked below. |
| 59–61 `cor:33` | PASS | Follows from monotonicity `s_17>=s_33`. | None. |
| 63–82 parameters/architecture | PASS | `eta=1/100`, `kappa=1/80^2`; pivot alternatives are exhaustive as used later. Counts `9=4*3-3`, `17=4*5-3` agree with Proposition `prop:volume`. No rotated-independence shortcut is asserted. | Threshold can be improved only by a new endpoint/structure; see improvement report for 9. |
| 84–120 `lem:fourier` | PASS | Plancherel normalization is consistent with `hat f(t)=int e^{itx}f(x)dx`. Gaussian inversion coefficient `1/(2 sqrt(pi v))` is correct. Approximate-identity and weak-limit steps are justified for rough laws. | Supports all inversion/smoothing uses. |
| 122–130 `lem:envelope` | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)`; Fourier inversion gives `ap/[pi(p-1)]`. | Order-five density constant checked. |
| 132–160 `lem:riesz` | PASS | Gamma representation and Tonelli are valid with extended values. The inner `v` integral equals `sqrt(2) Gamma(1/4)|t|^{-1/2}`, giving exactly `1/sqrt(2pi)`. The `3/4` envelope weighted integral is `12 sqrt(u)`. | Order-three half-potential constant checked. |
| 163–181 `lem:rank` | PASS | Eckart–Young approximation formula proves both nonsymmetric singular-value perturbation and the rank-shift inequality exactly as used. | Critical to `prop:volume`. |
| 183–207 `lem:schur` | PASS | For invertible `A`, `S^{-1}` is the complementary principal block of `A^{-1}`. Interlacing separately above `+1/t` and below `-1/t` gives `#(|eig S^{-1}|>1/t)<=n-N_A(t)`, i.e. `(n-k)-N_S(t)<=n-N_A(t)`. The singular approximation `A+eps I`, threshold `t-|eps|`, and limit preserve the non-strict `>=t` count. | Pivot branches retain the claimed spectral counts. |
| 209–217 `lem:dd` | PASS | Standard max-coordinate proof works for nonsymmetric matrices and strict row dominance. | Used only on `R[H,H]`. |
| 221–255 `thm:bl` | PASS | Heat equation normalization agrees with `g_t`; differentiating gives `partial_t F-Delta F=F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` by the frame contraction. Gaussian tail domination justifies differentiation/integration by parts; large-time scaling uses `sum c_i=d`; Fatou plus monotone truncation handles rough nonnegative integrable inputs. | No imported sharp BL theorem is needed. |
| 258–282 `lem:projection` | PASS | Orthogonal completion and Fubini give the marginal. With `b_i=|w_i|^2`, the normalized rows form the geometric frame. `f_i^{1/b_i}<=f_i` because `0<=f_i<=1`; `prod b_i^{-b_i/2}<=e^{d/2}` follows from `-b log b<=1-b` and `sum(1-b_i)=d`. Scalar scaling gives `sqrt(e)/|a|`. | Correctly avoids rotated independence. |
| 284–301 `lem:scalar-fourier` | PASS | For `m=floor(p/2)>=p/4`, `|hat f|^p<=|hat f|^{2m}`. The latter is the characteristic function of a sum of `m` independent differences; its zero-density is controlled by the preceding projection lemma with coefficient norm `sqrt(2m)`. Constants reduce to `2pi sqrt(2e)/sqrt(p)`. | Used in determinant theorem. |
| 303–324 `lem:decoupling` | PASS | First Cauchy–Schwarz duplicates only the `J` bank; integrating independent `I` coordinates produces the product Fourier factors. Squaring the nonnegative RHS gives the fourth-power form. Difference-coordinate densities are `f*tilde f<=1`. No moments required. | Correct powers 2 and 4. |
| 326–373 `thm:determinant` | PASS | `H=alpha I+a^2 M^TM`, `alpha=(2pi e)^2`; the frame weights satisfy `0<c_j<=1`, `0<=d_i<=1`, `sum d_i=sum(1-c_j)=theta`. The one-dimensional scaling factors in geometric BL are correct. Scalar Fourier powers give `(2pi sqrt(e d_i))^{d_i}` and cancel `d_i^{-d_i/2}`; `prod c_j^{-c_j/2}<=e^{theta/2}`. Factoring `alpha` leaves `(2pi e/sqrt(alpha))^theta=1`. Fourth roots yield exponent `-1/8` and coefficient `t^2/(pi^2 e^2)`. | Central Fourier bound PASS. |
| 375–400 crossing volumes and `cor:vol-fourier` | PASS | Cauchy–Binet gives `det(I+zM^TM)=sum z^k Z_k` and the elementary symmetric singular-value expression. Retaining one term yields exponent `k/4`. For `k=5`, envelope inversion gives `5e Z_5^{-1/10}`; for `k=3`, Riesz gives `12 sqrt((e/2) Z_3^{-1/6})`. | Constants checked exactly. |
| 404–414 `lem:square` | PASS | Two monotone branches give the exact square density bound; the interval preimage estimate `2 sqrt(2rho/|a|)` is correct after completing the square. | Scalar pivot profile valid. |
| 416–421 conditional profile | PASS | Measure domination follows by applying the conditional square density against nonnegative output test functions and Tonelli. No false independence is used. | Supports scalar pivot branches. |
| 423–434 `lem:definite` | PASS | Deterministic translation/orthogonal diagonalization is only a change of integration variables. Elliptic polar coordinates have Jacobian `1/(2 sqrt(det B))`; integrating the joint density cap gives `pi M/sqrt(|det B|)`. | Definite pair branch valid. |
| 437–482 `lem:hyperbola` | PASS | Hyperbolic parametrization has absolute Jacobian `1/(2sqrt D)`. In each branch `u,w` have common norm `sqrt(delta Lambda)/2`; a physical coordinate with `|u_i|>=|u|/sqrt2` exists. The cutoff `3/4 log2` makes one coordinate monotone with derivative `>=|coordinate|/3`. Cap-one/mass-one rearrangement gives each tail `<=3 log2`; middle length yields `<6+log_+(32/(delta Lambda))`. `Lambda>=2/sqrt D` converts this to the displayed `16 sqrt D/|z-v|`. Exceptional critical level is handled at the measure level. | Indefinite pair branch valid. |
| 485–525 `lem:quarter` | PASS | If a diagonal coefficient is large, conditional square small-ball gives `4 sqrt(rho/L)`. Otherwise zero-diagonal sign cutting yields a literal original-coordinate cross block with operator norm `>=L/4`. Determinant theorem gives the `|t|^{-1/4}` envelope. Gaussian smoothing at `v=1/8` yields the displayed coefficient `<16`. Layer cake gives `4+4log16`; atomlessness follows as `rho downarrow0`. | Log potential used in pivot branches is valid for arbitrary rough product laws. |
| 528–543 `def:pivot-volume`, small-entry estimate | PASS | No `eta` pivot gives `|a_ii|<eta` and `|a_ij|^2<eta^2+eta<2eta`, hence `|a_ij|<1/7`. Ordered-pair convention and empty-sum convention are explicit. | Entry bounds correct. |
| 545–564 `lem:sampling` | PASS | Weighted seed probability is normalized by `V_r`. For each off-diagonal `ell,m in L`, bordered elimination gives `det(child)^2=det(B)^2(A_lm-P_lm)^2`; sorting signs disappear after squaring. Any ordered child has at most `(r+1)^2` nonsingular parents, while singular parents may still have nonsingular children, so the required relation is an inequality. `P` has rank `<=r` and interpolates rows `S`/columns `T` exactly. | Sensitive ordered-minor step PASS. |
| 566–580 `lem:completion` | PASS | `E` is exactly the off-diagonal `LxL` residual; `D` is the diagonal residual on `L` and vanishes on `S union T`; `R_LL=P_LL`. `R-P` can be supported only in rows `T` or columns `S`, hence rank `<=2r`; adding `rank P<=r` gives global `rank R<=3r`, while `rank R_LL<=r`. No symmetry of `R,E` is needed. | Both different rank bounds and seed vanishing PASS. |
| 582–619 `prop:volume` | PASS | If `V_k<kappa^k`, a ratio `<kappa` occurs, including the first-zero case. At `r=0`, `||off A||_F<sqrt(kappa)=1/80` and `||diag A||<1/100`, contradicting `||A||>=1`. For `r>=1`, `eps<=(r+1)/80<=1/16`. With `m=4k-3>=4r+1`, rank perturbation forces at least `r+1` diagonal entries of `D` of magnitude `>=1-eps`; all lie in `L`. On their block, `|R_ii|>=371/400` and row off-diagonal sum is `<4(1/7+1/16)=23/28`, so strict diagonal dominance contradicts `rank R_LL<=r`. | Spectral-to-volume accounting PASS. |
| 621–630 `lem:cut` | PASS | Each ordered disjoint `(S,T)` is separated by a fair cut with probability `4^{-k}`; expectation identity and existence follow. | Product-preserving literal cross block obtained. |
| 632–645 `cor:no-pivot` | PASS | `V_k>=kappa^k` plus cut gives `Z_k^{-1/(2k)}<=2kappa^{-1/2}=160`. `k=3` gives `12sqrt(80e)<200`; `k=5` gives `800e<2400`. Affine/same-bank phases are covered by the cross-form theorem. | No-pivot branches valid. |
| 654–674 `lem:kernels` | PASS | Near part of `J(d)` is uniformly finite after scaling; far part uses `|x-d|>=|x|/2` and gives the logarithm. The second kernel is maximized at coincident interval superlevel sets; `2 int_0^1 x^{-1/2}log(1/x)dx=8`. | Constants safe, not sharp. |
| 676–714 `prop:pivot-H` | PASS | Scalar pivot: Schur leaves one unit spectral direction, quarter-power excludes an atom and controls the logarithm; `eta^{-1/2}(8+3L0)<600`. Definite pair gives `<160`. Indefinite pair integrates the hyperbolic envelope against the truncated half kernel; `sup D^{-1/2}log_+D=2/e` and `D>=eta` give `<444`. All are conditional measure-dominating bounds and average correctly. | Truncated half potential is genuinely uniform. |
| 716–724 `prop:nine` | PASS | With a pivot and `s_9>=1`, `prop:pivot-H` applies because at least two large eigenvalues are present. Without a pivot, the full half-potential bound `<200` applies. Tail outside radius 1 contributes at most 1, yielding 601. | Full vs truncated half-potential distinction correctly handled. |
| 726–749 proof of `thm:main` | PASS | No-pivot uses the 17-direction density branch. Scalar pivot leaves at least 16 directions, hence 9, and gives `6010`. Definite pair gives `<40`. Indefinite pair leaves at least 15 directions so the Schur remainder has operator norm at least one; hyperbolic plus log potential gives `<251`. Scaling `Y=KX`, `Q=(s/K^2)Qtilde` is exact and gives `K^2/s`. Interval/density equivalence is standard. | Baseline 17 theorem closes. |
| 751–773 threshold accounting/remarks | PASS | Correctly distinguishes order-five density from order-three half potential and does not claim the 3-eigenvalue theorem or global continuity. | Improvement requires a new analytic endpoint or structural input. |
| 775–790 acknowledgments/bibliography | PASS for mathematical dependency; bibliographic existence checked | Both cited works exist with the listed titles/authors/arXiv identifiers. The manuscript reproves the specific inequalities it uses, so no theorem depends on an unchecked imported citation. | Priority/novelty is not certified by this check. |

## Support-file audit

### `proof_map.csv` — PASS

The labels and source ranges agree with the 790-line manuscript as read. In particular the sensitive ranges are correctly mapped: `lem:sampling` 545–564, `lem:completion` 566–580, `prop:volume` 582–619, `prop:pivot-H` 676–714, `prop:nine` 716–724, and main proof 726–749.

### `verify.py` / `checks.json` — PASS in their explicitly limited scope

The checker reads the pinned manuscript SHA-256, verifies the exact diagonal-dominance slack `297/2800`, the parameter relations, exact interpolation/rank/volume identities on its finite seeded examples, and floating Schur/graph-weight diagnostics. `checks.json` records PASS with 534 exact interpolation seeds, 18 exact volume cases, 240 floating Schur threshold cases and 30 graph-weight cases. This code is correctly labelled as finite diagnostics, not a proof certificate. The floating checks include tolerance and therefore are not promoted to exact proof evidence.

The historical counts in `AUDIT.md` differ from the newer delivery checker counts; `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, and `checks.json` explicitly disclose that they are different suites. **No contradiction** results.

### `SOURCE_MANIFEST.json` — PASS for repository identity; UNCHECKED for local rehash/build

The connector shows the manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d` unchanged at the pinned source read. The manifest's reported SHA-256/size/line count are consistent with the control files. I did not materialize the bytes locally and independently recompute the SHA-256 in this invocation, and I did not rebuild/render the PDF. Those two packaging claims remain **UNCHECKED by this reviewer**, not mathematical gaps.

### `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md` — PASS as status documents

They consistently distinguish a complete written candidate from independent validation, distinguish the committed LaTeX source from the uncommitted binary PDF, and distinguish current reproducibility checks from the historical self-audit suite.

## Independent arithmetic and adversarial checks performed in this run

I independently recomputed the decisive constants:

- `sqrt(kappa)=1/80`;
- worst interpolation error at `r=4`: `(r+1)/80=1/16`;
- diagonal lower bound `1-1/16-1/100=371/400`;
- off-diagonal row sum `4(1/7+1/16)=23/28`, with strict slack `371/400-23/28=297/2800>0`;
- no-pivot `k=3` half potential constant `12 sqrt(80e)<200`;
- no-pivot `k=5` density constant `800e<2400`;
- scalar-pivot main constant `10*601=6010<10000`.

I also reconstructed the canonical interpolation/completion on the exact symmetric block

```
A0=[[-2,-2,-2],
    [-2,-2,-1],
    [-2,-1,-2]]
```

with seed `S={1}, T={2}`. The canonical completion has `E=0`, `rank R=3` and `rank R[L,L]=1`; direct sums give simultaneous equalities `rank R=3r`, `rank R[L,L]=r` for `r=1,2,3,4`. Scaling by `1/250` places this example in the manuscript's no-pivot regime (`max |a_ii|=1/125`, max principal `2x2` determinant magnitude `3/62500`). Thus the two rank constants are not artifacts of a loose proof and cannot simply be replaced by `2r/r` or `3r/(r-1)` from symmetry/no-pivot alone.

## Remaining UNCHECKED items after this complete mathematical reading

1. Fresh local SHA-256 recomputation of `manuscript.tex` bytes: **UNCHECKED** in this run; connector git-blob identity was pinned.
2. Fresh LaTeX compilation and visual inspection of the 16-page PDF: **UNCHECKED** in this run; not a mathematical dependency.
3. Comprehensive literature priority/novelty search: **UNCHECKED**; the two bibliography entries themselves were verified to exist.
4. Independent validation by a second reviewer: **UNCHECKED / required by owner policy**. This report does not self-award it.

## Baseline conclusion

**PASS:** the pinned 17-eigenvalue proof is complete as written at the mathematical level I checked. No definition, equation, lemma invocation or branch in lines 1–790 produced a fatal gap. The next mathematical obligation is therefore a genuine threshold reduction rather than baseline repair. My separate improvement report for this same run reconstructs a full-scope **nine-eigenvalue** replacement theorem and records why the present interpolation rank mechanism alone does not pass below nine.
