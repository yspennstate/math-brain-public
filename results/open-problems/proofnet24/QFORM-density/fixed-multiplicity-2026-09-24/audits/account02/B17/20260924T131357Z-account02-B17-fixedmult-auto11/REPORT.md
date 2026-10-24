SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-24T13:13:57Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924 — independent end-to-end audit of the pinned 17-eigenvalue manuscript, then a complete lower-threshold replacement and adversarial shortcut search.

# account02/B17 full fixed-multiplicity audit — auto11

Run: `20260924T131357Z-account02-B17-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and package coverage

Mathematical baseline audited:

- repository: `yspennstate/math-open-problems`
- initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- package-declared SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- source length: 47,883 bytes / 790 lines according to the manifest and checker.

I read the entire 790-line manuscript from the pinned blob in contiguous ranges, including a second fetch of the previously response-truncated 426--510 range. I also read `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json` from master. On the latest master observation before this write, `manuscript.tex` still resolved to git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

The SHA-256 above is pinned by `SOURCE_MANIFEST.json` and is rechecked internally by `verify.py`/`checks.json`; I did not independently hash raw bytes outside the connector, so an independent recomputation of SHA-256 is `UNCHECKED`. This is provenance metadata, not a proof premise.

A prior B17 report from an earlier run recorded the support files as missing. That package-only gap is now **repaired**: all requested support files are present and were read in this run. The historical larger finite-check counts in `AUDIT.md` are not reproduced by the current delivery suite; `SOURCE_MANIFEST.json` explicitly labels the current suite as new. Those historical counts remain `UNCHECKED` by this run and have no mathematical-proof role.

## Overall verdict

**PASS — literal pinned 17-eigenvalue mathematical theorem.** I find no fatal mathematical gap in the statement

`independent real coordinate densities <= K`, `A=A^T`, `s_17(A)>=s>0`, arbitrary affine `b,c`

implying

`||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s`.

This is an independent mathematical audit by this slot, not formal verification, novelty review, or a claim that the unrestricted three-eigenvalue QFORM problem is solved. Global continuity is not asserted by the theorem.

### Schur-limit reconciliation: PASS, not GAP

The only live conflicting audit label I found concerns `lem:schur`, lines 183--207. The manuscript's moving-threshold singular-matrix limit is valid as written. Let `m=N_A(t)-k>0` and choose `epsilon->0` avoiding the finitely many singular values of `A+epsilon I` and of the pivot `B+epsilon I`. Its Schur complement `S_epsilon` converges to `S`. Since every eigenvalue `lambda` with `|lambda|>=t` satisfies `|lambda+epsilon|>=t-|epsilon|`,

`N_(A+epsilon I)(t-|epsilon|)>=N_A(t)`.

The invertible case at threshold `t-|epsilon|` gives

`N_(S_epsilon)(t-|epsilon|)>=m`,

equivalently the ordered `m`th singular value obeys

`s_m(S_epsilon)>=t-|epsilon|`.

Singular values are continuous under operator-norm convergence, hence `s_m(S)>=t`, i.e. `N_S(t)>=N_A(t)-k`. Therefore no fixed-delta repair is required. The moving threshold loses nothing because the proof follows the ordered singular value.

## Exhaustive source-line ledger

Every manuscript source line is covered below. `PASS` means I reconstructed the mathematical dependency rather than inheriting the author self-audit. `UNCHECKED` below is attribution-only and does not feed the theorem.

| lines | status | audit finding |
|---|---|---|
| 1--46 | PASS | notation, theorem environments, metadata and abstract match the later mathematical statement; no hidden support/moment/smoothness assumption is introduced. |
| 47--80 | PASS | `thm:main`, `cor:33`, singular-value convention, normalization `eta=1/100`, `kappa=1/80^2`, pivot/no-pivot architecture and scaling target are mutually consistent. |
| 81--160 | PASS | Fourier convention, Gaussian regularization, Plancherel/inversion, power envelope and Riesz negative-half-moment formula have the displayed constants; rough laws are handled by Gaussian regularization/Tonelli. |
| 161--217 | PASS | nonsymmetric singular-value perturbation/rank inequalities, principal Schur spectral count including singular `A`, and strict diagonal dominance all hold under the stated hypotheses. |
| 218--301 | PASS | geometric rank-one Brascamp--Lieb heat-flow proof, product-projection density bound and integrated scalar Fourier powers close with the stated constants and no rotated-product independence. |
| 302--400 | PASS | literal product-bank decoupling, fourth-power step, regularized crossing determinant, Cauchy--Binet crossing volumes, order-five density receiver and order-three half-potential receiver are consistent. |
| 401--525 | PASS | scalar-square domination, definite pair, full hyperbolic-pair envelope, quarter-power concentration and log-potential estimate are valid as measure-dominating statements for rough laws. |
| 526--645 | PASS | pivot/volume definitions, no-pivot entry bound, ordered disjoint-minor sampling, nonsymmetric completion, global/restricted rank bounds, spectral-to-volume contradiction, random cut and no-pivot consequences are valid. |
| 646--724 | PASS | singular-kernel integrals, pivot truncated-half-potential compiler, distinction between truncated and full half potentials, and the nine-direction full half-potential proposition close with the stated constants. |
| 725--790 | PASS mathematically; attribution-only UNCHECKED | all main-theorem branches, scaling to general `K,s`, interval/density equivalence, threshold accounting and limitations are valid. Bibliographic priority/completeness is not independently audited here and is not used as a proof premise. |

## Label-by-label hypothesis audit

- `thm:main` / `cor:33` (47--61): **PASS**. All quantifiers and scaling are explicit; `s_17(A)>=s` means seventeen absolute eigenvalues at scale `s` because `A` is symmetric.
- `lem:fourier` (91--120): **PASS**. The convention gives Plancherel factor `2pi`, inversion `1/(2pi)`, and the displayed Gaussian identity.
- `lem:envelope` (122--130): **PASS**. The envelope mass is exactly `2ap/(p-1)`.
- `lem:riesz` (132--160): **PASS**. The Gamma/Tonelli calculation yields coefficient `1/sqrt(2pi)`; the `3/4` power envelope gives weighted integral `12 sqrt(u)`.
- `lem:rank` (169--181): **PASS**. Approximation-number proof applies to nonsymmetric auxiliaries.
- `lem:schur` (183--207): **PASS**, including the moving-threshold singular case, by the ordered-singular-value argument above.
- `lem:dd` (209--217): **PASS**, symmetry not needed.
- `thm:bl` (221--255): **PASS**. The frame contraction gives the heat-flow sign, large-time Gaussian normalization is correct, and Fatou plus monotone truncation treats rough inputs.
- `lem:projection` (258--282): **PASS**. Only deterministic orthogonal coordinates are used; factors with complementary leverage zero are safely dropped; `-b log b<=1-b` gives `e^(d/2)`.
- `lem:scalar-fourier` (284--301): **PASS**. `m=floor(p/2)>=p/4`, the even power is integrable, and the signed projection has coefficient norm `sqrt(2m)`.
- `lem:decoupling` (310--324): **PASS**. The copy is introduced only in a literal independent product bank; same-bank phases are modulus one and arbitrary affine terms remain allowed.
- `thm:determinant` (326--373): **PASS**. The regularized graph vectors form an exact frame; `c_j,d_i` lie in `[0,1]`; scalar Fourier powers use `p=2/d_i`; `alpha=(2pi e)^2` cancels the entropy factor; fourth root gives exponent `-1/8` and coefficient `t^2/(pi^2 e^2)`.
- `cor:vol-fourier` (386--400): **PASS**. Retaining order `k` gives exponent `k/4`; order five is `L1`, while order three is used only with the Riesz weight.
- `lem:square` / conditional profile (404--422): **PASS**. This is conditional measure domination, not independence of the square and Schur remainder.
- `lem:definite` (423--434): **PASS**. The deterministic two-dimensional polar change has Jacobian `1/(2sqrt(|det B|))`; no random-variable rotation is invoked.
- `lem:hyperbola` (437--482): **PASS**. Branch Jacobian, tail monotonicity/bathtub bound, middle logarithmic length and `Lambda>=2/sqrt(D)` give the stated envelope.
- `lem:quarter` (485--525): **PASS**. If no large diagonal exists, a physical sign cut extracts a literal cross block of norm at least `L/4`; determinant decay plus Gaussian smoothing gives the quarter-power small-ball bound and hence finite log potential.
- `def:pivot-volume` (528--535): **PASS**. Ordered disjoint pairs and empty-sum convention match every subsequent counting identity.
- `lem:sampling` (545--564): **PASS**. Bordered determinants, sorting signs removed by squaring, and at-most `(r+1)^2` parent multiplicity give the expected Frobenius residual; only an existential good seed is claimed.
- `lem:completion` (566--580): **PASS**. `D` vanishes on `S union T`; `E` has zero diagonal; `R-P` is supported in rows `T` or columns `S`; therefore `rank R<=3r`, while exactly `R[L,L]=P[L,L]` gives restricted rank `<=r`.
- `prop:volume` (582--619): **PASS**. At a bad ratio, `||E||<=1/16`. Rank perturbation forces `r+1` large diagonal entries in `L` because `m=4k-3>=4r+1`. Their `R`-diagonal is at least `371/400`, while four off-diagonal terms cost `<23/28`; strict diagonal dominance contradicts restricted rank `r`.
- `lem:cut` / `cor:no-pivot` (621--645): **PASS**. Each ordered disjoint `k,k` pair crosses a fair cut with probability `4^-k`; the constants `160`, `<200`, and `<2400` follow.
- `lem:kernels` (654--674): **PASS**. Both singular integrals are locally integrable and the displayed coarse constants suffice.
- `prop:pivot-H` (676--714): **PASS**. Scalar pivot uses one surviving Schur eigenvalue only for the logarithmic potential; definite/indefinite pair branches are uniformly conditionable in original coordinates. This proposition controls the **truncated** half potential.
- `prop:nine` (716--724): **PASS**. No-pivot supplies a full half potential; pivot supplies truncated `<=600`, and the outside kernel is `<=1`, so the full half potential is `<=601`.
- proof of `thm:main` (726--749): **PASS**. No-pivot uses order five; scalar pivot leaves sixteen Schur directions and invokes `prop:nine`; definite pair is direct; indefinite pair leaves at least one Schur direction for the logarithmic receiver. Scaling gives exactly `10000 K^2/s`.

## Package/checker audit

`proof_map.csv` agrees with the source labels/ranges used above. `verify.py` first checks the pinned SHA-256 and then performs exact symbolic interpolation/rank/volume assertions plus separate floating diagnostics. `checks.json` records `PASS`: 534 exact interpolation seeds, 18 exact volume-sampling comparisons, 9 strict-sampling cases, exact diagonal-dominance slack `297/2800`, 240 numerical Schur-threshold cases and 30 numerical graph-weight cases. I audited the checker logic but did **not** independently execute this suite in this connector-only run; the recorded execution is therefore supporting evidence, not my proof certificate.

## Impact and next obligation

The 17-eigenvalue baseline is mathematically sound in this audit. The next obligation is not another baseline rewrite but a genuine lower-threshold replacement. This run supplies a complete threshold-nine replacement separately in the paired improvement artifact. Multiplicity eight is not proved here; exact no-pivot `s_8=1` examples and rank-count saturation show that two tempting structural shortcuts fail.

No claim is made that the unrestricted three-eigenvalue QFORM conjecture is solved.