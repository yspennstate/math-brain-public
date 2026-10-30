# fleet01/B11 r12 — full fixed-multiplicity audit and Schur adjudication

Run: `20260924T131124Z-fleet01-B11-fixedmult-r12`  
Objective acknowledged: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Worker: `fleet01/B11`

## Source pin

- Baseline source commit required by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Fresh master observed immediately before publication: `d11ccbed9e8d0f45b0f42b519564641bdfb9f1bc`.
- `manuscript.tex` at that fresh master still has git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, exactly the baseline mathematical source.
- Manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines.

I read the complete 790-line manuscript in source order and the current `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md`. I did not use previous PASS reports as premises for the mathematical verdict below.

## Verdict

**Mathematical theorem: PASS.** I found no fatal defect and no unrepaired proof gap in the written 17-eigenvalue theorem. The theorem proved by the pinned manuscript is exactly:

> independent real coordinate densities `<=K`, arbitrary real symmetric `A`, arbitrary `b,c`, and `s_17(A)>=s>0` imply that `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity<=10000 K^2/s`.

No Gaussianity, log-concavity, moments, bounded support, identical laws, sign restriction, diagonal-basis assumption, or independence after rotation is used.

Two peer comments required explicit adjudication in this run:

1. **Singular Schur limit:** PASS as written. A prior B18 audit called the moving-threshold limit a gap. It is not a gap once the count is written as an ordered singular-value inequality; the proof below makes this explicit. The B18 fixed-`delta` repair is also valid but unnecessary.
2. **Product-projection `b_i=0` line:** PASS as written, though a recent B02 note suggests a tighter wording. The manuscript's sum `sum_i(1-b_i)=d` is over all indices after extending `-b log b` by zero at `b=0`, so the displayed upper bound is valid. A tighter intermediate bound is `(d-z)/2` when `z=#{i:b_i=0}`, but no correction is needed for the advertised `e^{d/2}` constant.

The current support package is complete. Earlier reports that `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` were missing describe older snapshots and are no longer current.

## B11 lens: complete Schur-complement proof

Write

`A=[[B,C],[C^T,D]]`, `det B != 0`, `S=D-C^T B^{-1} C`, with `B` of order `k`, and define `N_T(t)=#{j:|lambda_j(T)|>=t}` for symmetric `T`.

### Invertible ambient matrix

Block elimination gives `S^{-1}` as the complementary principal compression of `A^{-1}`. For a Hermitian principal compression, separately on the positive and negative tails,

`#{lambda(S^{-1})>1/t} <= #{lambda(A^{-1})>1/t}`

and

`#{lambda(S^{-1})<-1/t} <= #{lambda(A^{-1})<-1/t}`.

Adding gives

`#{|lambda(S^{-1})|>1/t} <= #{|lambda(A^{-1})|>1/t}`.

Because `A,S` are invertible,

`#{|lambda(A^{-1})|>1/t}=n-N_A(t)`

and

`#{|lambda(S^{-1})|>1/t}=(n-k)-N_S(t)`.

Hence `N_S(t)>=N_A(t)-k`.

### Singular ambient matrix and the strict/non-strict endpoint

Take a sequence `epsilon_m -> 0` such that `A_e=A+eI` is invertible. Since `B` itself is invertible, `B+eI` is invertible for all sufficiently small `e`; its Schur complement

`S_e=D+eI-C^T(B+eI)^{-1}C`

converges to `S`.

For `|e|<t`, every eigenvalue of `A` with modulus at least `t` gives an eigenvalue of `A+eI` with modulus at least `t-|e|`, so

`N_{A_e}(t-|e|)>=N_A(t)`.

Applying the already-proved invertible case at threshold `t-|e|` yields

`N_{S_e}(t-|e|)>=m`, where `m=N_A(t)-k`.

If `m<=0` there is nothing to prove. If `m>=1`, this count is exactly the ordered-modulus statement

`s_m(S_e)>=t-|e|`.

Ordered eigenvalue moduli (equivalently singular values for symmetric matrices) are continuous in the matrix entries. Letting `e->0` therefore gives

`s_m(S)>=t`,

which is equivalent to `N_S(t)>=m=N_A(t)-k`.

This directly resolves the apparent moving-threshold concern: a count at a moving threshold converging upward to `t` is safe because the `m`-th ordered modulus itself is bounded below by that moving threshold. No eigenvalue-tracking choice is needed. A fixed-`delta` proof is an equivalent longer repair, not a missing ingredient.

Equivalent useful form:

` s_j(S) >= s_{j+k}(A) `

whenever the right side is interpreted within the available dimensions.

## Exhaustive source-line audit

| Source range | Status | Independent reasoning / exact issue | Downstream impact |
|---|---|---|---|
| 1–45 | PASS | Preamble, macros, abstract and metadata introduce no mathematical hypothesis beyond the theorem. | None. |
| 46–83 | PASS | Singular-value convention, theorem quantifiers, normalization `eta=1/100`, `kappa=1/80^2`, and pivot/no-pivot architecture match the proof. No continuity is overclaimed. | Scope correct. |
| 84–160 | PASS | Fourier convention, Gaussian transform, Plancherel constant `2pi`, inversion, Gaussian inversion, power envelope and Riesz half-potential constants re-derived. Tonelli/dominated convergence are used in valid directions for rough laws. | Fourier and half-potential inputs valid. |
| 161–181 | PASS | Approximation-number characterization proves both nonsymmetric singular-value perturbation and rank-shift inequalities. | Used safely for nonsymmetric auxiliaries. |
| 183–207 (`lem:schur`) | PASS | Inverse-compression proof valid for invertible `A`; singular case valid by the ordered-modulus argument above. Strict inverse threshold `>1/t` matches original non-strict count `>=t`. | All scalar/pair Schur invocations valid with no change. |
| 209–217 | PASS | Strict row diagonal dominance proof does not need symmetry. | Interpolation contradiction valid. |
| 221–255 | PASS | Heat-flow Brascamp--Lieb derivative identity, frame contraction, integration by parts, large-time limit, Lebesgue-point/Fatou limit and monotone truncation checked. | Geometric integral inequality valid. |
| 258–282 (`lem:projection`) | PASS | Deterministic orthogonal fiber integration only; no rotated independence. If `Z={i:b_i=0}`, one can write `sum_{b_i>0}(1-b_i)=d-|Z|<=d`; equivalently, as the manuscript does, extend `-b log b` by zero and sum `-b log b<=1-b` over all `i`, obtaining `sum_i(1-b_i)=d`. | Bound `e^{d/2}` valid. |
| 284–301 | PASS | Difference density cap `<=1`, Plancherel integrability, inversion at zero and coefficient norm `sqrt(2m)` give the stated scalar Fourier-power bound. | Fourier powers valid. |
| 310–324 | PASS | Two- and four-power decoupling checked. Difference coordinates stay independent cap-one; same-bank phases disappear only under Cauchy--Schwarz/modulus. | No hidden independence/moment assumption. |
| 326–400 | PASS | Regularized frame, weights `c_j,d_i`, determinant Jacobian, `L^p` factors, entropy cancellation at `alpha=(2pi e)^2`, fourth-root exponent `-1/8`, Cauchy--Binet expansion, order-3/order-5 consequences all check. | Determinant engine valid. |
| 404–434 | PASS | Scalar-square profile and interval preimage bound correct; conditional use is measure domination. Definite-pair polar Jacobian gives `pi M/sqrt(|det B|)`. | Pivot inputs valid. |
| 437–482 | PASS | Hyperbolic two-branch parametrization, Jacobian, original-coordinate tail monotonicity, mass/cap bathtub estimate, middle interval and `Lambda>=2/sqrt D` checked. | Indefinite-pair envelope valid. |
| 485–525 | PASS | Random sign cut gives a physical cross block of norm `>=L/4`; determinant envelope, Gaussian smoothing and Gamma power give the quarter concentration; layer cake gives `L0=4+4 log16`. | One spectral direction controls logarithm. |
| 528–580 | PASS | Ordered disjoint volumes, no-pivot entry estimate, bordered determinants, sampling multiplicity, nonsymmetric interpolation support and completion checked. `rank R<=3r`, while `rank R[L,L]<=r`, and `D=0` on seed. | Sensitive structural step valid. |
| 582–619 | PASS | Bad ratio selection handles first vanishing volume without division by zero. Rank perturbation forces `r+1` large diagonals for `m=4k-3`; they lie in `L`; constants `371/400` vs `<23/28` give strict diagonal dominance contradiction. | Spectral-to-volume proposition valid. |
| 621–645 | PASS | Fair cut includes each ordered disjoint pair with probability `4^{-k}`; `k=3,5` constants yield full half-potential `<200` and density `<2400`. | No-pivot consequences valid. |
| 654–674 | PASS | Both singular kernel integrals re-derived; Tonelli and interval-overlap argument valid. | Pivot half-potential convolution valid. |
| 676–714 | PASS | Scalar, definite and indefinite pivot alternatives checked. Scalar branch exact bound is `200+120 log16`; pair bounds are smaller. | `H(Q)<=600` valid and conservative. |
| 716–724 | PASS | Pivot case gives truncated half-potential; no-pivot case gives full half-potential; adding at most one outside the unit window gives full `<=601`. | Full/truncated distinction correct. |
| 726–774 | PASS | Main case split exhaustive. Scalar pivot leaves at least 16 directions; pair pivot leaves at least 15. Constants and scaling `Y=KX`, `Q=(s/K^2) Qtilde` checked. | Main 17 theorem closes. |
| 775–790 | PASS for theorem scope; UNCHECKED for exhaustive priority | Threshold accounting and continuity limitation accurately stated. Bibliographic citations are antecedent/attribution only; I did not perform an exhaustive novelty/priority search in this B11 run. | No theorem dependency unchecked. |

No mathematical source line is unreviewed.

## Labeled statement audit

PASS: `thm:main`, `cor:33`, `lem:fourier`, `lem:envelope`, `lem:riesz`, `lem:rank`, `lem:schur`, `lem:dd`, `thm:bl`, `lem:projection`, `lem:scalar-fourier`, `lem:decoupling`, `thm:determinant`, `cor:vol-fourier`, `lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter`, `def:pivot-volume`, `lem:sampling`, `lem:completion`, `prop:volume`, `lem:cut`, `cor:no-pivot`, `lem:kernels`, `prop:pivot-H`, `prop:nine`, and the final theorem proof.

I also checked all displayed formulas used downstream, including every formula named in `proof_map.csv`; no formula was left UNCHECKED.

## Package audit

| Artifact | Status | Reason |
|---|---|---|
| `README.md` | PASS | Correctly describes the current baseline and distinguishes proof from review status. |
| `AUDIT.md` | PASS as historical self-report, not proof evidence | Its older finite-test counts are explicitly historical. |
| `proof_map.csv` | PASS | Line ranges agree with the 790-line source and cover all labeled statements. |
| `SOURCE_MANIFEST.json` | PASS for repository metadata; UNCHECKED for independent SHA-256 recomputation | Git blob, byte count and line count agree with the retrieved source. I did not locally recompute every listed SHA-256. |
| `verify.py` | PASS as a finite diagnostic program | The assertions correspond to the stated interpolation, Schur and graph-weight diagnostics. It is not a proof certificate. |
| `checks.json` | PASS for internal consistency; UNCHECKED for independent rerun in this invocation | It records PASS on 534 exact interpolation seeds, 18 exact volume comparisons, 240 numerical Schur threshold cases and 30 graph-weight cases against the pinned source hash. |
| `DELIVERY_STATUS.md` | PASS | Correctly records that the formerly missing support files have now been added and that the new finite suite does not reproduce the historical self-audit counts. |

## Exact constant already available from the written pivot proof

The scalar-pivot half-potential estimate is not merely `<600`; the proof gives

`H <= 10(8+3(4+4 log16)) = 200+120 log16`.

Adding the tail gives full half-potential `<=201+120 log16`, and multiplying by the outer worst scalar-pivot factor `eta^{-1/2}=10` gives

`2010+1200 log16 = 5337.106466687737...`.

Thus even the baseline 17-direction theorem can replace `10000` by this constant without changing hypotheses. More importantly, the separate improvement report for this run combines the newly source-matched order-three/order-two product-Fourier receiver with this exact bookkeeping and lowers the complete theorem from 17 directions to 9.

## Review-state conclusion

- Pinned 17-eigenvalue manuscript: **PASS in this complete B11 review**.
- Singular-Schur concern from the B18 snapshot: **resolved as PASS for the original text**, not a theorem gap.
- Product-projection endpoint comment from the recent B02 note: **stated bound remains PASS**; the note supplies a tighter intermediate inequality only.
- Full three-eigenvalue conjecture: **not solved here**.
- Global continuity: **not claimed/proved for the full fixed-multiplicity theorem**.
- Model: GPT-5.6 Sol. Configured reasoning effort/provider thinking counters: `UNKNOWN / NOT_EXPOSED`.
