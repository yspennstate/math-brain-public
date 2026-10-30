# fleet01/B08 auto11 — full fixed-multiplicity manuscript audit

Run: `20260924T144535Z-fleet01-B08-fixedmult-audit-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `fleet01/B08`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source pin and verdict

Fresh owner control was read before selecting work from `yspennstate/math-research-brain/main/AGENTS.md` and `scheduled_tasks/CURRENT_OBJECTIVE.md`; this run explicitly acknowledges `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Fresh `master` observed immediately before publication: `4335ca25ed47bbaf02045553f59b8d52d9322228`.  
Current `manuscript.tex` Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`, unchanged from the baseline.  
Manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Manifest size/length: 47,883 bytes, 790 lines.

I read all 790 lines in this invocation, together with current `README.md`, `DELIVERY_STATUS.md`, historical `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`.

**Verdict on the exact current mathematical source: PASS.** I found no mathematical FALSE item and no unresolved mathematical GAP in the 17-eigenvalue theorem. The theorem under audit is only

` s_17(A)>=s>0  =>  ||p_(X^TAX+b^TX+c)||_infinity <=10000 K^2/s `

for arbitrary real symmetric `A`, arbitrary independent coordinate densities bounded by `K`, and arbitrary affine `b,c`. Nothing here proves the unrestricted three-eigenvalue conjecture, and the manuscript does not claim global continuity.

### Correction of my own preceding B08 r12 report

My r12 audit labeled the singular paragraph of `lem:schur` a repairable GAP. That diagnosis was incorrect and is superseded by this report. The manuscript's moving-threshold argument is valid as written. If

`q=N_A(t)-k>0`,

choose admissible `epsilon ->0`. The manuscript gives

`N_(A+epsilon I)(t-|epsilon|)>=N_A(t)`

and the invertible case gives

`N_(S_epsilon)(t-|epsilon|)>=q`.

Equivalently the q-th largest eigenvalue modulus of `S_epsilon` is at least `t-|epsilon|`. Since `S_epsilon -> S` and ordered eigenvalue moduli are continuous for symmetric matrices,

`s_q(S)>=lim (t-|epsilon|)=t`,

hence `N_S(t)>=q`. No fixed-delta repair is needed. The earlier objection that an eigenvalue might approach `t` at a different rate is irrelevant, because the proved lower threshold itself converges to `t`.

## Complete line/range audit

Every mathematical source line 1–790 is covered below. `UNCHECKED` is used only for matters outside the written mathematical proof or for an execution I did not independently rerun.

| Source range / label | Verdict | Independent reconstruction |
|---|---|---|
| 1–35 | **PASS** | Preamble, notation and macros only; no hidden mathematical premise. |
| 36–83, abstract, `thm:main`, `cor:33`, architecture | **PASS** | Quantifiers are exactly arbitrary dimension/signature/remaining spectrum, arbitrary affine terms, non-iid independent rough densities capped by `K`. The main theorem asserts essential boundedness, not continuity. |
| 84–120, `lem:fourier` | **PASS** | Fourier convention, Gaussian inversion and density-by-smoothing constants are consistent with `hat f(t)=int e^{itx}f(x)dx`; measure domination is used rather than pointwise density assumptions. |
| 122–160, `lem:envelope`, `lem:riesz` | **PASS** | Power-envelope integral and negative-half-moment normalization have the stated constants and exponents; positive cutoffs justify the rough-law Riesz passage. |
| 169–181, `lem:rank` | **PASS** | Approximation-number proof gives the nonsymmetric rank-shift and operator perturbation inequalities used later; symmetry is not required. |
| 183–207, `lem:schur` | **PASS** | In the invertible case, `S^{-1}` is the complementary principal compression of `A^{-1}` and positive/negative min-max counts yield the absolute-value count. The singular limiting paragraph is valid for the reason proved above. |
| 209–217, `lem:dd` | **PASS** | Strict row diagonal dominance implies nonsingularity by the maximal-coordinate kernel-vector argument; no symmetry assumption is needed. |
| 221–255, `thm:bl` | **PASS** | Heat-flow derivative has the correct nonnegative sign by the frame contraction; integration by parts, Gaussian large-time normalization, truncation/Fatou and monotone approximation close the rough-law endpoint. |
| 258–282, `lem:projection` | **PASS** | Deterministic orthogonal projection only; no rotated-coordinate independence is asserted. Zero row norms may be retained by the limiting convention `-b log b=0`; the entropy bound gives the stated `e^{d/2}` cap. |
| 284–301, `lem:scalar-fourier` | **PASS** | Difference variables remain independent with density cap one. Projection density plus inversion at zero yields the even-power estimate; interpolation to general powers is in the correct direction. |
| 310–324, `lem:decoupling` | **PASS** | Two-copy and four-copy Cauchy–Schwarz identities use independence only between original banks; same-bank phases cancel before modulus. |
| 326–373, `thm:determinant` | **PASS** | With `H=alpha I+a^2M^TM`, the graph Jacobian, weights `c_j,d_i`, trace identity and scalar Fourier exponents cancel exactly at `alpha=(2*pi*e)^2`; fourth root gives determinant exponent `-1/8`. |
| 386–400, `cor:vol-fourier` | **PASS** | Cauchy–Binet identifies the crossing volume. Order five gives an integrable `|t|^{-5/4}` density envelope; order three gives only the weighted half-Riesz endpoint, exactly as later used. |
| 404–414, `lem:square` | **PASS** | Completing one original scalar square gives the stated inverse-square-root measure profile for arbitrary translated cap-one input laws. |
| 423–434, `lem:definite` | **PASS** | The two-dimensional definite quadratic change of variables has Jacobian and area constant `pi/sqrt(det B)`; deterministic diagonalization is only an integration device. |
| 437–482, `lem:hyperbola` | **PASS** | Both hyperbola branches, tail coordinate choice, monotonicity, middle-interval length and `Lambda>=2/sqrt(D)` reconstruct. The resulting logarithmic envelope is a measure domination statement and tolerates arbitrary translations. |
| 485–525, `lem:quarter` | **PASS** | Random signs create a literal original-coordinate crossing of norm at least `L/4`; determinant Fourier control plus Gaussian inversion gives the quarter-power small-ball estimate and the logarithmic-potential bound. |
| 528–535, pivot-volume definition and no-pivot entry bound | **PASS** | Scalar and principal-pair pivot exclusions imply the displayed diagonal/off-diagonal coefficient bounds. |
| 545–564, `lem:sampling` | **PASS** | For invertible seed `B=A[S,T]`, the bordered determinant identity is exact. Singular seeds correctly enter only through an inequality. Each extension is counted at most `(r+1)^2` times, giving the weighted residual estimate. |
| 566–580, `lem:completion` — B08 lens | **PASS** | Independently reconstructed below. `P` may be nonsymmetric; `E` has zero diagonal; `D` vanishes on `S union T`; `rank R[L,L]<=r`; support of `R-P` gives global `rank R<=3r`. |
| 582–619, `prop:volume` | **PASS** | A bad volume ratio gives `||E||_F<=(r+1)/80<=1/16`. With `m=4k-3>=4r+1`, global rank subtraction forces `r+1` large diagonal coordinates of `D`, all in `L`; strict diagonal dominance contradicts restricted rank `<=r`. The exact slack is `297/2800>0`. |
| 621–645, `lem:cut`, `cor:no-pivot` | **PASS** | Each ordered disjoint `k`-minor survives a fair physical cut with probability `4^{-k}`. The order-five and order-three analytic conclusions are used at their proper exponents. |
| 654–674, `lem:kernels` | **PASS** | Both elementary singular-integral bounds are correct; the coarse constants are sufficient. |
| 676–714, `prop:pivot-H` | **PASS** | Scalar, definite-pair and indefinite-pair pivot cases are exhaustive; square/hyperbolic kernels are averaged through Tonelli without assuming a conditional density cap for the Schur law. |
| 716–724, `prop:nine` | **PASS** | Pivot branch invokes `prop:pivot-H`; no-pivot branch invokes the full order-three half potential, not merely the truncated one. The outside tail contributes at most one. |
| 726–749, proof of `thm:main` | **PASS** | No-pivot `<2400`; scalar pivot leaves at least sixteen spectral directions and hence the nine-direction half-potential input; definite pair is direct; indefinite pair leaves at least fifteen. Scaling `Y=KX` gives exactly `K^2/s`. |
| 750–790, threshold accounting, limitations, bibliography | **PASS mathematically / UNCHECKED priority** | Threshold accounting accurately distinguishes global `3r` from restricted `r` and order-five from order-three endpoints. Bibliographic priority/novelty was not comprehensively re-searched in this run and is **UNCHECKED**, but no citation is a proof premise. |

## B08 interpolation reconstruction

Order coordinates as `S,T,L`, with `|S|=|T|=r`, and write

```
A = [ C    B    G
      B^T  F    H
      G^T  H^T  J ],              B=A[S,T] invertible.
```

The manuscript interpolant is

`P=A[:,T] B^{-1} A[S,:]`.

Therefore

`P[S,:]=A[S,:]`, `P[:,T]=A[:,T]`, and `P[L,L]=H^T B^{-1}G`.

Define `E[L,L]=off(A[L,L]-P[L,L])`, zero elsewhere, and let `D` be the diagonal of `A-P-E`. Then:

1. `diag E=0`.
2. `D=0` on `S union T`, because `P` already interpolates every row in `S` and every column in `T`, including those diagonal positions.
3. For `R=A-D-E`, `R[L,L]=P[L,L]`, hence `rank R[L,L]<=r`.
4. `R-P` vanishes on rows `S`, columns `T`, and all of `L x L`. Its support is contained in the union of rows `T` and columns `S`. Splitting those two supports gives `rank(R-P)<=2r` and therefore `rank R<=rank P+2r<=3r`.

There is also an exact normal form:

```
R = [ C    B    G
      B^T  F    H
      G^T  H^T  H^T B^{-1}G ].
```

After a column permutation and exact elimination using invertible `B`,

`rank R = r + rank K`,

where

```
K = [ B^T-FB^{-1}C       H-FB^{-1}G
      G^T-H^TB^{-1}C     0          ].
```

The remaining block row and block column each have rank at most `r`, so `rank K<=2r`. This explains the global `3r` and restricted `r` estimates simultaneously.

Both estimates are sharp in the present algebraic class. Take the direct sum of `r` copies of

```
(1/200) [0 1 1
         1 0 1
         1 1 1]
```

and choose the first coordinate of each block in `S`, the second in `T`, the third in `L`. Then `B=(1/200)I_r`, `D=E=0`, `rank R=3r`, and `rank R[L,L]=r`, while all scalar and principal-pair coefficients stay inside the manuscript's no-pivot regime. Thus symmetry of `A` does not permit a generic bookkeeping replacement `3r ->2r`.

## Supplementary package audit

The current root contains all requested support files.

- `README.md` and `DELIVERY_STATUS.md`: **PASS/read**. They distinguish manuscript source, compiled conversation PDF, finite diagnostics, worker activity and mathematical validation.
- `proof_map.csv`: **PASS/read**. The statement/proof ranges agree with the pinned source labels used in this review.
- `SOURCE_MANIFEST.json`: **PASS/read**. Source blob/hash/size/line count agree with the current manuscript.
- `verify.py`: **PASS code inspection** for its stated finite scope. Its exact interpolation tests exercise the support/rank/zero-diagonal identities and the exact diagonal-dominance slack; floating Schur/graph checks are explicitly diagnostic only.
- `checks.json`: **PASS recorded-output consistency**. It records source hash match, 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, slack `297/2800`, 240 floating Schur threshold checks and 30 graph-weight checks.
- Independent rerun of `verify.py` in this connector-only invocation: **UNCHECKED**. I did not execute a second local Python copy of that suite; this does not affect the analytic proof audit.
- Historical `AUDIT.md`: **PASS as historical self-report**, not as independent validation. Its historical statement that independent reviews were pending is intentionally time-stamped history and is not a current mathematical claim.

## End-to-end review 1 — direct dependency walk

Starting from the theorem statement, I traced every invoked dependency in proof order: main theorem -> no-pivot volume/Fourier or physical pivot -> nine-half-potential -> pivot-H/no-pivot order-three -> square/hyperbola/quarter -> Schur count -> sampling/completion -> nonsymmetric rank bounds -> determinant Fourier -> product projection/BL/scalar Fourier. Every invocation meets its stated hypotheses after conditioning on original coordinates only. No hidden Gaussian, moment, support, sign, connected-support, diagonal-basis, or post-rotation-independence hypothesis enters.

## End-to-end review 2 — reverse obstruction walk

Independently, I started from each potential failure mode and traced it forward: singular `A` in the Schur step; singular seeds in volume sampling; nonsymmetric `P,R,E`; zero projection rows; rough densities without pointwise versions; dependence of the hyperbolic critical value on conditioned coordinates; and the distinction between truncated and full half potentials. Each is explicitly handled in the source. The only non-proof items left `UNCHECKED` are the external priority search and my own rerun of the finite diagnostic script.

## Final baseline status

- Exact pinned/current `manuscript.tex`: **PASS** in this B08 full audit.
- Fatal defects: **none found**.
- Unresolved mathematical GAP/FALSE item: **none found**.
- Global continuity: **not claimed / not established by the baseline theorem**.
- Full three-eigenvalue conjecture: **OPEN / not addressed by this validation result**.

A separate improvement report from this same run gives an independent replacement proof at multiplicity nine and records the current multiplicity-eight obstruction.