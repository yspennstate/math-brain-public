# fleet02/B07 full fixed-multiplicity audit — 2026-09-24 run

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`

## Source pin and scope

- Repository/branch: `yspennstate/math-open-problems`, `master`.
- Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Source git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Source length: 47,883 bytes, 790 lines.
- Fresh master observed during this run: `d3299af8809b11f51e3d6dd1273c54913c197989`; the manuscript blob at that commit is still exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Read in full: `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`.

Verdict on the written theorem: **PASS_WITH_NONFATAL_PROJECTION_WORDING_GAP**. I found no fatal mathematical defect. This is an fleet02/B07 audit, not formal verification, peer review, priority verification, or a claim that 17 is optimal. The unrestricted three-eigenvalue QFORM conjecture is not claimed solved.

## Complete source-line audit

The following ranges cover every line of `manuscript.tex`.

| Lines | Object | Status | Reason / repair / impact |
|---|---|---|---|
| 1–46 | LaTeX setup, abstract, global definitions | PASS | Statement in abstract matches the theorem; no hidden support, moment, log-concavity or post-rotation-independence assumption is introduced. |
| 47–61 | `thm:main`, `cor:33` | PASS | Quantifiers are arbitrary independent coordinate densities `<=K`, arbitrary real symmetric `A`, arbitrary affine `b,c`; singular-value hypothesis and scaling target are coherent. |
| 62–90 | architecture, parameters `eta=1/100`, `kappa=1/80^2` | PASS | Later branches use exactly these constants; 9 and 17 are `4k-3` at `k=3,5`. |
| 91–120 | `lem:fourier` | PASS | Plancherel, Gaussian regularization, inversion and weak-limit argument are valid at the stated hypotheses. |
| 121–130 | `lem:envelope` | PASS | Envelope integral is `2ap/(p-1)` and inversion gives the displayed constant. |
| 131–160 | `lem:riesz` | PASS | Gamma representation and the `sqrt(2) Gamma(1/4)|t|^{-1/2}` integral give the stated normalization; the `3/4` envelope integral is `12 sqrt(u)`. |
| 161–182 | singular-value conventions and `lem:rank` | PASS | Approximation-number proof works for nonsymmetric matrices, as later required. |
| 183–207 | `lem:schur` | PASS | Invertible case follows from the complementary principal block of `A^{-1}` plus positive/negative interlacing; the singular limiting argument preserves the `>=t` count. |
| 208–220 | `lem:dd`, transition | PASS | Strict row diagonal dominance proves invertibility without symmetry. |
| 221–257 | `thm:bl` | PASS | Heat-flow sign, frame contraction, large-time Gaussian limit, small-time Fatou step and rough-function monotone approximation are consistent. |
| 258–282 | `lem:projection` | **GAP (wording only)** | After factors with `b_i=0` are dropped, the proof writes `(1/2) sum_i(1-b_i)=d/2`. For the retained positive-`b_i` indices the correct statement is `sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`. This is exactly sufficient for `p(y)<=e^{d/2}`; no theorem or constant changes. |
| 283–309 | `lem:scalar-fourier` and cross-form setup | PASS | `m=floor(p/2)>=p/4`, Fourier inversion at zero, and projection scaling give the displayed `2pi sqrt(2e)/sqrt(p)` bound. |
| 310–324 | `lem:decoupling` | PASS | Cauchy–Schwarz, independent copy, product Fourier factors and Jensen powers are correct; no moment assumption is used. |
| 325–385 | `thm:determinant`, `Z_k` and determinant expansion | PASS | Frame weights satisfy `sum d_i=sum(1-c_j)`; scalar Fourier powers cancel the `d_i`; `alpha=(2pi e)^2` cancels the entropy factor; fourth root gives exponent `-1/8`. Cauchy–Binet normalization is correct. |
| 386–400 | `cor:vol-fourier` | PASS | Retaining the order-`k` determinant term gives exponent `k/4`; constants for `k=5` density and `k=3` half-potential are correct. |
| 401–422 | `lem:square`, conditional profile | PASS | Two inverse branches and interval-preimage estimate are valid; the conditional profile is measure domination, not an independence assertion. |
| 423–436 | `lem:definite` | PASS | Completing the square and deterministic polar coordinates give `pi M/sqrt(|det B|)` without rotating the product law. |
| 437–482 | `lem:hyperbola` | PASS | Hyperbolic parameterization, Jacobian, tail coordinate selection, `1/|y|` rearrangement, middle interval length and final AM–GM substitution check out. |
| 483–527 | `lem:quarter` | PASS | Large diagonal and off-diagonal random-cut alternatives are exhaustive; determinant decay and Gaussian smoothing give the quarter-power bound; layer cake gives `4+4 log16`. |
| 528–544 | `def:pivot-volume`, no-pivot entry bound | PASS | `V_r` is explicitly over **ordered disjoint** pairs with sorted submatrices. No-pivot gives `|a_ij|<1/7`. |
| 545–564 | `lem:sampling` | PASS | See B07 exact audit below. The `off` in `F=off(A_LL-P_LL)`, the condition `ell != m`, sorting signs, ordered child multiplicity and existential seed quantifier are all essential and correctly stated. |
| 565–581 | `lem:completion` | PASS | Diagonal residual is put in `D`; `E` has zero diagonal; `R-P` support is rows `T` or columns `S`, yielding global rank `<=3r`, while `R_LL=P_LL` gives restricted rank `<=r`. |
| 582–620 | `prop:volume` | PASS | Telescoping/first-zero cases cover all possibilities. For `r=0`, operator norm is `<1`; for `1<=r<=4`, `||E||<=1/16`, rank perturbation forces `r+1` large diagonal entries in `L`, and exact diagonal-dominance slack is `297/2800>0`. |
| 621–645 | `lem:cut`, `cor:no-pivot` | PASS | A fixed ordered disjoint `(S,T)` survives the oriented fair cut with probability `4^{-k}`. The resulting `Z_k^{-1/(2k)}<=160`; constants `<200` and `<2400` follow. |
| 646–675 | truncated half potential and `lem:kernels` | PASS | Both singular integrals and the centered-overlap argument have the stated constants. |
| 676–715 | `prop:pivot-H` | PASS | Scalar Schur remainder has a surviving eigenvalue; definite and indefinite pair branches average valid conditional domination bounds; `sup D^{-1/2} log_+D=2/e` is used with the right coefficient. |
| 716–725 | `prop:nine` | PASS | Pivot/no-pivot alternatives give `H<=600`; the outside kernel contributes at most one. |
| 726–749 | proof of `thm:main` | PASS | Scalar pivot leaves >=16 unit eigenvalues, pair pivot leaves >=15; normalized branch constants are below `10^4`; general `K,s` scaling is exact. |
| 750–790 | threshold accounting, limitations, acknowledgments, bibliography | PASS for internal mathematical claims; **UNCHECKED only for comprehensive literature/priority status** | The text explicitly does not claim the 3-eigenvalue theorem or optimality. Classical references are attribution only; this run did not perform an exhaustive prior-art review. |

## B07 exact audit: ordered minors, signs and multiplicities

For increasing `S,T` and `ell,m` outside `S union T`, `ell != m`, define

`p_S(ell)=#{s in S:s>ell}`, `p_T(m)=#{t in T:t>m}`.

Moving the newly added row/column from sorted position to the last block position gives the unsquared identity

`det A[S+ell,T+m] = (-1)^(p_S(ell)+p_T(m)) det(B) (a_ell,m - A[ell,T] B^{-1} A[S,m])`.

Thus the manuscript's squared identity is correct for sorted child sets. I independently checked this exact sign formula on **3,204** bordered extensions from symmetric integer matrices in dimensions 4–6 at seed orders 1–2; every case passed.

There is also an exact aggregate identity. For an ordered disjoint child `(U,V)` of size `r+1`, let

`c(U,V)=#{(ell,m) in U x V : det A[U\{ell},V\{m}] != 0}`.

Then

`sum_(nonsingular ordered seeds S,T) det(A_ST)^2 ||F_ST||_F^2
 = sum_(ordered disjoint children U,V) c(U,V) det(A_UV)^2`.

This follows by the bordered identity term-by-term; every off-diagonal residual corresponds to one deleted-row/deleted-column parent. Hence `0<=c(U,V)<=(r+1)^2`, which is exactly the manuscript's sampling inequality. I independently checked this coefficient identity in 30 exact random-matrix/order cases, in addition to the package checker.

The coefficient `(r+1)^2` is genuinely attained even inside the no-pivot regime. Take the symmetric Cauchy matrix

`A_ij = delta/(x_i+x_j)`, `delta=1/100`, `x_i=i`.

The Cauchy determinant formula makes **every square minor nonzero**, so every disjoint child has all `(r+1)^2` nonsingular parents. The matrix is no-pivot: `|A_ii|<=1/200<1/100`, and every principal two-coordinate determinant is `<delta^2/4<1/100`. Therefore no reduction of the parent-count factor can come from symmetry, no-pivot assumptions, ordering conventions or sorting signs alone.

## New adversarial finite obstruction: why `off` is mandatory

A tempting but false variant would bound the **full** Schur residual `A_LL-P_LL` by `V_{r+1}/V_r`, allowing `ell=m`. This fails because `V_{r+1}` only counts disjoint row/column sets.

Take

`A = [[0,1/20,0],[1/20,0,0],[0,0,1/200]]`, `r=1`, `S={1}`, `T={2}`.

This matrix is no-pivot: diagonal magnitudes are `<1/100` and every principal `2x2` determinant has modulus `<1/100`. Here `V_1=1/200>0` but `V_2=0` because three coordinates cannot contain two disjoint 2-sets. For the chosen seed, `P_33=0`, so the full residual has diagonal entry `1/200` even though the right side of a putative full-residual sampling bound is zero. Correspondingly,

`det A[{1,3},{2,3}] = 1/4000 != 0`,

but this bordered minor has overlapping row/column sets at coordinate 3 and therefore is correctly absent from `V_2`. The manuscript avoids the false inference by defining `F=off(...)` and absorbing the diagonal residual into `D` in the completion lemma. This is a substantive PASS of the exact quantifier/definition as written and a counterexample to a natural misreading.

## Package/support-file audit

- `README.md`: PASS; theorem scope, source pin, build instructions and release cautions match the source.
- `DELIVERY_STATUS.md`: PASS as delivery metadata; correctly distinguishes source from an uncommitted conversation PDF.
- `SOURCE_MANIFEST.json`: PASS for repository metadata; source blob/hash/length agree with the pinned package. The separate compiled PDF binary itself is **UNCHECKED by this run** because it is not in the GitHub root.
- `AUDIT.md`: READ/PASS as a historical self-report, not used as proof of correctness.
- `proof_map.csv`: PASS; statement/proof ranges align with the manuscript labels used in this audit.
- `verify.py`: PASS as a finite diagnostic program, with correctly scoped limitations.
- `checks.json`: PASS and independently reproduced for its mathematical diagnostics: 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict cases, slack `297/2800`, 240 Schur threshold diagnostics and 30 graph-weight diagnostics. These computations are diagnostics, not proof certificates.

## Threshold-improvement status

No unconditional reduction below 17 is claimed. The current order-five architecture can land at the `r=4` ratio. With only 16 unit-scale singular values, the global rank loss `3r=12` forces only four large diagonal directions, while `R_LL` is allowed rank four; strict diagonal dominance needs a fifth row. The exact counting identity above shows that ordered-minor multiplicity/sign conventions do not supply the missing direction. Moving to order four leaves the present determinant envelope at the non-`L^1` endpoint `|t|^{-1}`. A valid lower threshold therefore still requires a new saturated-`r=4` structural argument or a genuinely stronger endpoint/cancellation theorem, with arbitrary rough product laws and affine terms retained.

## Final status and next obligation

- Mathematical baseline: **PASS_WITH_NONFATAL_PROJECTION_WORDING_GAP**.
- Fatal gap: none found.
- Threshold reduction: none proved.
- New B07 obstruction: full-residual/`ell=m` sampling is false even in a no-pivot matrix; `off` and the diagonal completion are essential.
- Next obligation: attack the saturated `r=4`, sixteen-direction case without changing the ordered-disjoint volume quantifiers, or prove an order-four endpoint density theorem strong enough to replace the order-five `L^1` step.
