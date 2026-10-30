# fleet01/B01 fixed-multiplicity audit continuation — r13

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `fleet01/B01`  
Run: `20260924T133745Z-fleet01-B01-fixedmult-r13`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Declared SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh repository head seen before publication: `afb8a72698c7367670a6cd19dd98a3135ee4835b`.

The current-hour B01 sign-in already existed when this invocation began, so it was read and preserved rather than overwritten. Fresh `AGENTS.md`, `scheduled_tasks/CURRENT_OBJECTIVE.md`, and the sign-in/privacy protocol were read before work.

## Executive verdict

I reread the complete 790-line pinned manuscript and all requested support files in this invocation. The literal baseline source still has one repairable proof gap: the singular-ambient limiting sentence in `lem:schur` (source line 205). I found no second mathematical defect in the baseline source. A new rank-only proof below repairs `lem:schur` using only the manuscript's already-proved singular-value rank lemma; after that repair, the advertised 17-eigenvalue theorem is PASS in this reconstruction with all quantifiers and scaling unchanged.

The strongest complete lower-threshold theorem currently supported by full replacement arguments I inspected is the nine-eigenvalue candidate. Separate workers have now posted genuinely distinct full PASS reconstructions of that candidate (including fleet01/B07 and fleet02/B09); release/independent-validation status remains an owner/B20 synthesis decision and is not self-awarded here. The eight-eigenvalue theorem is still open.

I also audited the new fleet03/B16 overlap-one structural theorem for the `s_8` endpoint. Its main lower bound is correct, but one displayed intermediate statement is FALSE as written: equation (2.11) calls a weighted-seed identity exact while its `W_{2,1}` also includes singular order-two seeds, which the sampling law omits. The repair is favorable and actually yields a stronger theorem supported entirely on invertible seeds; see the improvement artifact from this run.

## End-to-end baseline status

| Source range / dependency | Status | Reasoning / downstream impact |
|---|---|---|
| 1–83 theorem, quantifiers, normalization architecture | PASS | Arbitrary independent real cap-`K` coordinate laws, arbitrary symmetric `A`, arbitrary affine `b,c`, all signatures/dimensions/remaining spectrum. No hidden moment/support/log-concavity/Gaussian/exact-rank assumption. |
| 84–168 Fourier/Gaussian/Riesz preliminaries | PASS | Fourier convention, Plancherel, Gaussian inversion, envelope and half-Riesz constants are mutually consistent; Tonelli/approximate-identity passages are valid for rough laws. |
| 169–181 singular-value perturbation/rank | PASS | Approximation-number proof covers nonsymmetric auxiliaries and is sufficient for every later rank loss. |
| 183–204 `lem:schur` statement + invertible proof | PASS | The invertible case is sound. |
| 205 singular-ambient limit in `lem:schur` | GAP, repairable | A moving threshold `t-|epsilon|` cannot be passed to the endpoint by continuity alone when an eigenvalue lands exactly at `t`. The rank-only proof in the companion improvement repairs the lemma without approximation or new input. |
| 209–301 diagonal dominance, geometric BL, product projection, scalar Fourier powers | PASS | Heat-flow/frame contraction and limits close; deterministic rotations occur only inside integrals; scalar Fourier power uses original independent copies. |
| 302–400 decoupling, determinant compiler, crossing volumes | PASS | Copies and product provenance are correct; graph weights/Jacobians and `alpha=(2*pi*e)^2` cancellation check; `k=5` is used for density and `k=3` only with the half-Riesz weight. |
| 401–525 square/definite/hyperbolic pivots and quarter concentration | PASS | Conditional statements are measure dominations, not independence assertions; hyperbolic tail is controlled in an original coordinate; log potential follows by layer cake. |
| 526–645 disjoint volumes, sampled interpolation, completion, spectral-to-volume, cut | PASS | Bordered-minor sampling is an inequality because singular seeds can have nonsingular extensions; `rank R<=3r`, `rank R[L,L]<=r`, zero diagonal of `E`, and `D=0` on the seed are correct. Diagonal-dominance slack is `297/2800`. |
| 646–724 kernel integrals, pivot half potential, nine-half-potential baseline proposition | PASS after Schur repair | Truncated versus full half-potential bookkeeping is correct. |
| 726–790 main theorem/scaling/limitations | PASS after Schur repair | Normalized branches close; with `Y=KX`, `Q=(s/K^2) Qtilde`, so the density cap scales by `K^2/s`. Global continuity is not claimed by the manuscript and is not proved by pivot branches. |

Portions still mathematically UNCHECKED in the pinned 790-line manuscript: **none**.

## Support-package audit

- `README.md`: PASS as current delivery/status metadata.
- `DELIVERY_STATUS.md`: PASS as delivery/status metadata; correctly separates activity from validation.
- `proof_map.csv`: PASS; statement/proof ranges match the manuscript.
- `SOURCE_MANIFEST.json`: PASS for repository-internal metadata consistency with blob `183ccd...`, 790 lines and 47,883 bytes.
- `verify.py`: PASS as a finite diagnostic script only. It checks exact interpolation identities/constants plus numerical Schur/graph cases, but is not a proof certificate.
- `checks.json`: PASS as the recorded output of that suite: 534 exact interpolation seeds, 18 volume comparisons, 9 strict-sampling cases, 240 numerical Schur-threshold cases and 30 graph-weight cases.
- historical root `AUDIT.md`: GAP as a validation verdict because it missed the line-205 limiting issue; useful as historical self-audit evidence only.

## Audit of the new eight-direction overlap-one structural result

Source inspected: fleet03/B16, `improvements/fleet03/B16/20260924T132036Z-fleet03-B16-FIXEDMULT-r48/REPORT.md`, blob `0e99f86ed86e36794e1512aa1e8bb8f7052e6c53`.

The theorem claims, for `s_8(A)>=s>0` and `V_2(A)>0`,

`W_{2,1}(A) >= 2 s^2 V_2(A) - 12 s sqrt(V_2(A)V_3(A))`.

The rank-six step is correct: for each nonsingular order-two seed, `A=D+R+E`, `rank R<=6`, and therefore `s_2(D)>=s_8(A-E)>=(s-epsilon)_+`. Hence

`sum_h D_hh^2 >= 2(s-epsilon)_+^2 >= 2s^2-4s epsilon`.

The sampled off-diagonal error still obeys `E epsilon^2 <=9 V_3/V_2`, so `E epsilon <=3 sqrt(V_3/V_2)`.

### Exact defect in equation (2.11)

The report writes

`W_{2,1}/V_2 = E_seed sum_h D_hh^2`

as an exact identity. This is **FALSE** for the stated `W_{2,1}`, because its definition sums overlap-one extensions of *all* ordered disjoint two-seeds, whereas determinant-squared sampling assigns zero mass to singular seeds. A singular two-seed can have a nonsingular same-index bordered extension.

Explicit symmetric five-coordinate example, with `S={1,2}`, `T={3,4}`, `h=5`:

```
A = [[0,0,1,0,0],
     [0,0,0,0,1],
     [1,0,0,0,0],
     [0,0,0,0,1],
     [0,1,0,1,0]].
```

Then

`A[S,T]=[[1,0],[0,0]]`, so `det A[S,T]=0`, while

`A[S union {h}, T union {h}] = [[1,0,0],[0,0,1],[0,1,0]]`

has determinant `-1`. Thus this overlap-one term belongs to `W_{2,1}` but not to the weighted expectation.

This defect does **not** invalidate the lower bound. Replacing equality by `>=` is enough. Better, define the invertible-seed overlap volume `W^x_{2,1}` by restricting the sum to `det A[S,T] != 0`. Then the exact identity holds with `W^x`, and the entire lower bound is carried by invertible seeds. The companion improvement proves this strengthened form.

Downstream status of fleet03/B16's structural conclusion: **PASS after local repair**. Its claimed eight-eigenvalue bounded-density theorem was already explicitly left OPEN; this review does not change that.

## Threshold status

- Repaired 17-eigenvalue baseline: PASS in this reconstruction.
- Nine-eigenvalue full theorem: complete candidate with multiple separate PASS reconstructions now present in the repository; owner/B20 release synthesis remains separate. A currently posted sharpening reaches a constant below 2582, but this run did not re-audit every arithmetic step of that newest constant optimization and therefore does not certify that sharpening.
- Eight eigenvalues: OPEN. The corrected overlap-one theorem gives a strong structural certificate but still lacks a product-preserving analytic receiver for the shared physical anchor.
- Full three-eigenvalue conjecture: OPEN.
- General continuity: OPEN; only branches with integrable characteristic-function control automatically give continuous densities.

Model self-report: GPT-5.6 Sol. Reasoning effort/counters: UNKNOWN / not exposed. Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval occurred, but no native learned-memory receiver use was observed.
