# fleet01/B07 r13 — full fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Actual run: `20260924T140521Z-fleet01-B07-fixedmult-audit-r13`  
Pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`  
Source length: 790 lines.

## Verdict

**PASS — no mathematical FALSE item or fatal/unrepaired GAP found in the 790-line seventeen-eigenvalue argument in this B07 reconstruction.** The theorem as written has the stated arbitrary-product-law, arbitrary symmetric-matrix, arbitrary-affine scope and the normalized constant is safely below `10^4`.

This is one worker audit, not formal verification or journal peer review. The unrestricted three-eigenvalue theorem is not proved by this manuscript.

I also checked the recently raised concern about the singular-matrix paragraph of `lem:schur`. My verdict is **PASS, no repair is mathematically necessary**: for `tau_e=t-|e|`, the invertible case gives `N_{S_e}(tau_e)>=N_{A+eI}(tau_e)-k>=N_A(t)-k`; if the right side is `q`, continuity of the ordered absolute eigenvalues of `S_e` and `tau_e -> t` gives `s_q(S)>=t`, hence `N_S(t)>=q`. A fixed-`delta` rewrite would be a clarity improvement, but the moving-threshold argument already closes.

The product-projection line `sum_i(1-b_i)=d` is also mathematically sound provided the displayed sum is read over all rows after extending `-b log b` by zero at `b=0`; more explicitly one may write `sum_{b_i>0}(1-b_i)<=sum_i(1-b_i)=d`. This is a wording clarification, not a proof gap.

## Complete source-range audit

The following ranges partition the mathematical source and cover every statement/proof line. `PASS` means I independently checked the displayed statement against the proof and downstream use.

| Lines / label | Verdict | Independent check and downstream consequence |
|---|---|---|
| 1–46 preamble/abstract/architecture | PASS | Definitions and claimed scope match the theorem proved later. No hidden moment, support, sign, iid, or rotated-independence assumption appears. |
| 47–61 `thm:main`, `cor:33` | PASS | Quantifiers are exactly independent densities `<=K`, arbitrary symmetric `A`, arbitrary `b,c`; scaling at lines 742–749 matches `K^2/s`. |
| 62–88 architecture/parameters | PASS | `eta=1/100`, `kappa=1/80^2`; counts `9=4*3-3`, `17=4*5-3` match later spectral-to-volume use. |
| 89–120 `lem:fourier` | PASS | Plancherel normalization is `2pi`; Gaussian inversion and weak-limit density argument are correct under the stated hypotheses. |
| 122–130 `lem:envelope` | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)` and inversion gives `ap/[pi(p-1)]`. |
| 132–160 `lem:riesz` | PASS | Gamma representation, Gaussian inversion, Tonelli and the `|t|^{-1/2}` constant are consistent; the `3/4` envelope gives `12 sqrt(u/(2pi))`. |
| 162–181 norms and `lem:rank` | PASS | SVD approximation formula yields both perturbation and rank-shift inequalities for nonsymmetric matrices, exactly what the interpolation proof requires. |
| 183–207 `lem:schur` | PASS | Invertible case via inverse principal compression is correct. Singular case with threshold `t-|e|` is valid by continuity of ordered absolute eigenvalues; no loss at equality `|lambda|=t`. |
| 209–217 `lem:dd` | PASS | Standard max-coordinate proof of strict row diagonal dominance. |
| 219–255 `thm:bl` | PASS | Heat-flow derivative has nonnegative defect by the Parseval-frame contraction; integration by parts and large-time Gaussian limit are justified by the compact-support approximation, then monotone convergence. |
| 257–282 `lem:projection` | PASS | Original-coordinate product density is integrated along the orthogonal complement, not declared independent after rotation. BL frame weights are `b_i`; `sum_i(1-b_i)=d`. Optional clarity: explicitly insert `sum_{b_i>0}(1-b_i)<=d`. |
| 284–301 `lem:scalar-fourier` | PASS | `g=f*tilde f<=1`; Plancherel plus projection density for the `2m` signed coordinates gives the displayed `p>=2` power integral. |
| 303–324 cross-form and `lem:decoupling` | PASS | Cauchy–Schwarz is applied before independent-copy expansion; same-bank phases have modulus one; the difference coordinates remain independent with cap-one densities. |
| 326–373 `thm:determinant` | PASS | Graph/BL regularizer `alpha=(2pi e)^2`, frame weights, Jacobian, scalar Fourier powers and fourth-root exponent `-1/8` all check. No leverage or rank assumption is inserted. |
| 375–400 `Z_k`, Cauchy–Binet, `cor:vol-fourier` | PASS | `Z_k=e_k(sigma^2)`. Retaining the order-`k` determinant term gives exponent `k/4`; `k=5` gives density, `k=3` gives the half-Riesz bound only. |
| 402–414 `lem:square` and profile setup | PASS | Two inverse branches give the square-root envelope; conditional use is measure domination via Tonelli, not independence of the square term and Schur remainder. |
| 423–434 `lem:definite` | PASS | Deterministic two-dimensional diagonalization and polar Jacobian yield `pi M/sqrt(|det B|)`; no rotated-coordinate independence is used. |
| 436–482 `lem:hyperbola` | PASS | Hyperbolic coordinates have Jacobian `1/(2 sqrt D)`; original-coordinate tail integration uses only cap/mass and the middle interval gives the logarithm. Constants are safe. |
| 484–525 `lem:quarter` | PASS | Random sign cut produces a literal physical cross block with norm at least `L/4`; one singular factor plus Gaussian smoothing gives quarter-power concentration. Layer cake yields `4+4 log16`. |
| 528–543 `def:pivot-volume`, no-pivot entry bound | PASS | `V_r` is over **ordered disjoint** row/column sets. No-pivot principal `2x2` inequality correctly implies `|a_ij|<1/7`. |
| 545–564 `lem:sampling` | PASS | Bordering identity is exact up to sorting sign, removed by squaring. Each ordered `(r+1)` disjoint minor has at most `(r+1)^2` nonsingular seed deletions. Singular seeds have zero sampling weight but may have nonsingular extensions, hence the proof correctly uses `<=`, not equality. |
| 566–580 `lem:completion` | PASS | `E` is only off-diagonal on `LxL`, `D` is diagonal and vanishes on `S union T`, `R[L,L]=P[L,L]`. Support of `R-P` is rows `T` or columns `S`, so `rank R<=3r`; restricted rank is `<=r`. Nonsymmetry is harmless because later perturbation uses singular values. |
| 582–619 `prop:volume` | PASS | Telescoping/first-zero argument produces a bad ratio. `r=0` is paid by the off-diagonal Frobenius norm. For `r>=1`, global rank loss gives at least `r+1` large diagonal entries in `L`; entry bounds make the corresponding `R[H,H]` strictly diagonally dominant, contradicting restricted rank `<=r`. The count `m>=4r+1` is exact. |
| 621–630 `lem:cut` | PASS | Every ordered disjoint `(S,T)` survives the fair physical cut with probability exactly `2^{-2k}=4^{-k}`. Linearity of expectation produces a literal original-coordinate crossing. |
| 632–645 `cor:no-pivot` | PASS | `Z_k^{-1/(2k)}<=160`; order 3 is used only for full half potential, order 5 for bounded density. Constants `<200` and `<2400` are safe. |
| 647–674 `H`, `lem:kernels` | PASS | Truncation is explicit. The two singular-integral bounds are sufficient and the centered-interval overlap argument for the logarithmic kernel is valid. |
| 676–714 `prop:pivot-H` | PASS | Scalar pivot invokes Schur count and one surviving unit direction; definite pair is direct; indefinite pair uses the hyperbolic envelope plus the log potential. All are conditional measure bounds uniform in outside variables. |
| 716–724 `prop:nine` | PASS | Pivot branch needs only two large directions; no-pivot branch uses the already proved `s9` half-potential. Adding the outside-unit tail costs at most one. |
| 726–749 main proof | PASS | No-pivot `s17` branch uses order five. Scalar pivot leaves 16 Schur directions and invokes `prop:nine`; pair pivots are direct/one-direction log. Scaling `Y=KX` and output scaling yield `10^4 K^2/s`. |
| 751–790 accounting/remarks/bibliography | PASS | Limitations accurately distinguish continuous no-pivot branch from global essential boundedness; no claim of the three-eigenvalue theorem or optimality is made. Classical citations are attribution, not hidden dependencies. |

## Support-file audit

- `README.md`: PASS as a delivery/index document; it correctly distinguishes source from PDF binary and finite checks from proof.
- `AUDIT.md`: PASS as a historical authoring-agent self-audit, **not** independent evidence.
- `proof_map.csv`: PASS; labels and line ranges match the source I read.
- `SOURCE_MANIFEST.json`: PASS as metadata; it matches the source blob/SHA/line count.
- `verify.py`: PASS by code inspection for the exact assertions it makes. It checks interpolation/support/rank identities, weighted sampling inequality, diagonal-dominance arithmetic, and floating diagnostics. It is not a proof certificate.
- `checks.json`: PASS as the recorded output of that scoped suite (`534` exact interpolation seeds, `18` volume-sampling cases, `9` strict cases, `240` floating Schur threshold cases, `30` graph-weight cases).

### Still UNCHECKED in this run

1. **UNCHECKED:** I did not independently execute `verify.py`; I inspected the code and recorded output only. Downstream consequence: none for the analytic proof, because no theorem step depends on these finite diagnostics.
2. **UNCHECKED:** I did not independently rebuild/render the 16-page compiled PDF binary. Downstream consequence: none for mathematical correctness of the source; this is a presentation/reproducibility item.
3. **UNCHECKED:** exhaustive literature priority/novelty beyond the cited classical antecedents. Downstream consequence: no bearing on internal proof validity, but no novelty/priority claim should be inferred from this audit.
4. **UNCHECKED:** formal proof-assistant verification. No such certificate is claimed.

## Threshold lowering status checked in this run

The repository now contains two genuinely separate complete reconstructions of the **nine-eigenvalue** replacement with safe constant `6010 K^2/s`: fleet01/B16 at commit `54ec2a651d854563f8db0d92c4c3426f76551786` and fleet02/B09 at commit `51022fbf2819704f220b1dc6d5f1889f979ca77b`. I read the B16 review and the B09 commit proof rather than relying only on a keeper label. Their grouped product-Fourier compiler, marginal-free `E_3` density receiver, marginal-free `E_2` half-potential receiver, and final pivot/no-pivot assembly are mathematically consistent with the audited baseline. Thus **9 is presently the lowest complete, two-review fixed multiplicity I can support in this run**.

The threshold-eight structural collar is sound but not yet a density theorem. A separate improvement file from this run gives a new three-bank averaging consequence of that collar and pays its generic `E_3`-rich branch.

## Final status

- Literal 17-eigenvalue mathematical argument: **PASS in this B07 review**.
- Threshold 9 replacement: **supported as complete with two separate prior full reviews; safe constant 6010**.
- Threshold 8: **OPEN**, but structurally sharpened in the companion B07 improvement.
- Full threshold 3 conjecture: **OPEN**.
- Full global continuity at threshold 9: **OPEN**; no-pivot `E_3` branch is continuous.
