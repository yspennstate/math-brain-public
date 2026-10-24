# account01/B15 r13 — full fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Actual invocation start: `2026-09-24T14:03:06Z`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned `manuscript.tex` blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Source size/length from `SOURCE_MANIFEST.json`: 47,883 bytes / 790 lines.

I read the fresh owner controls and then all 790 lines of `manuscript.tex`, plus `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` in this invocation. The historical test counts in `AUDIT.md` are not reproduced by the newer checker and are treated separately below.

## Fatal defects first

**No fatal defect found. No FALSE mathematical claim found in the pinned manuscript.**

My exact-source verdict is **PASS**, including the singular case of Lemma `lem:schur` at lines 205–207. Several later peer artifacts label those three lines a repairable GAP because the threshold `t-|epsilon|` moves with `epsilon`; I rechecked that objection and it does not create a gap. The manuscript's limiting sentence is short, but the argument is valid as written. A detailed reconstruction is in the improvement artifact for this run.

The fixed-multiplicity theorem proved by the pinned manuscript therefore remains mathematically sound on this B15 audit:

` s_17(A)>=s>0  =>  ||p_(X^TAX+b^TX+c)||_infinity <= 10000 K^2/s `

for arbitrary real symmetric `A`, arbitrary affine terms, and arbitrary independent real coordinate laws with densities bounded by `K`. This says nothing about optimality and does not prove the unrestricted three-eigenvalue conjecture.

## Line-by-line coverage ledger

Every source line 1–790 is covered. `PASS` means I reconstructed the mathematical step or checked that it is nonmathematical metadata. `UNCHECKED` is reserved for claims external to the written proof or for an execution I did not independently rerun.

| Source range / item | Verdict | Reason |
|---|---|---|
| 1–35 | **PASS** | LaTeX macros, metadata and theorem setup; no hidden mathematical premise. |
| 36–83, abstract/main statement/architecture | **PASS** | Quantifiers and scaling target are explicit: arbitrary dimension, signature, affine terms and rough non-iid product laws. Main conclusion is essential `L^infinity`, not continuity. |
| 84–90, Fourier convention/setup | **PASS** | Convention `hat f(t)=int e^{itx}f(x)dx` is used consistently downstream. |
| 91–120, `lem:fourier` | **PASS** | Plancherel/inversion normalization is consistent. Gaussian identity coefficient is `1/(2 sqrt(pi v))`; the regularized inversion argument is valid for probability measures without prior density. |
| 121–130, `lem:envelope` | **PASS** | Direct split at the balancing frequency gives the stated power-envelope `L^1` integral and density cap. |
| 131–160, `lem:riesz` | **PASS** | The Gaussian/Mellin representation of `|x|^{-1/2}` and Tonelli give the factor `1/sqrt(2pi)`. For `min(1,(u/|t|)^(3/4))`, the weighted integral is exactly `12 sqrt(u)`. |
| 161–168, norms and spectral-count notation | **PASS** | Definitions are standard and used consistently. |
| 169–181, `lem:rank` | **PASS** | Approximation-number characterization gives both Lipschitz singular-value perturbation and the rank shift for nonsymmetric auxiliaries. |
| 183–207, `lem:schur` | **PASS** | Invertible case: `S^{-1}` is the complementary principal compression of `A^{-1}`; positive/negative min-max counts give the modulus count. Singular case is valid as written; see the explicit moving-threshold argument below. |
| 209–217, `lem:dd` | **PASS** | Kernel-vector proof of strict row diagonal dominance; no symmetry required. |
| 218–255, geometric Brascamp–Lieb | **PASS** | Heat-flow derivative has the correct sign because the frame map is a contraction; large-time Gaussian normalization and small-time Fatou/truncation steps are legitimate. |
| 256–282, `lem:projection` | **PASS** | Only deterministic orthogonal changes of integration variables occur. `sum_i(1-b_i)=d` and `-b log b<=1-b` give the `e^(d/2)` cap. No rotated random coordinates are asserted independent. |
| 284–301, `lem:scalar-fourier` | **PASS** | Difference density cap, even-power inversion at zero, and `floor(p/2)>=p/4` yield the stated constant. |
| 302–324, cross form / `lem:decoupling` | **PASS** | Two-copy Cauchy–Schwarz uses literal independent coordinate banks; same-bank phases cancel before modulus. |
| 326–373, `thm:determinant` | **PASS** | Regularizer, graph weights, Jacobian and fourth-root exponent reconstruct. Determinant exponent `-1/8` is correct; no product structure is claimed after rotation. |
| 374–400, volume Fourier corollary | **PASS** | Cauchy–Binet gives the crossing volumes. Crucial scope is correct: order three gives `|t|^{-3/4}` and only a negative-half-potential after the Riesz weight; order five gives `|t|^{-5/4}` and hence direct `L^1` inversion/continuous density. |
| 401–414, square profile | **PASS** | One-dimensional inverse-branch measure domination; rough densities are handled as measures rather than pointwise exceptional slices. |
| 415–434, definite pair | **PASS** | Two-dimensional polar/elliptic calculation has Jacobian `1/(2 sqrt(det B))` and yields `pi/sqrt(det B)` uniformly over induced affine terms. |
| 435–482, hyperbolic pair | **PASS** | Original-coordinate branch parametrization, monotonic-tail changes of variables, determinant scaling and logarithmic envelope are valid. Exceptional critical level is handled by nonnegative test functions/Tonelli. |
| 483–525, quarter-power concentration | **PASS** | Random sign cut produces a physical crossing of norm at least `L/4`; Fourier/Gaussian small-ball calculation and layer cake give the stated constants and no-atom/log-potential conclusion. |
| 526–544, pivot/volume definitions and no-pivot entry bounds | **PASS** | Failure of scalar and principal-pair pivots yields the displayed entry estimates. |
| 545–564, `lem:sampling` | **PASS** | Bordering determinant identity is exact. Singular seeds correctly make the aggregate extension count an inequality, not a false equality. |
| 566–580, `lem:completion` | **PASS** | `E` has zero diagonal; `D` vanishes on the seed; `R[L,L]=P[L,L]` has rank at most `r`; support of `R-P` gives global rank at most `3r`. Nonsymmetry is explicitly allowed and correctly handled. |
| 582–619, `prop:volume` | **PASS** | A bad volume ratio yields `||E||_F<=(r+1)/80<=1/16`; `4r+1` spectral directions force `r+1` large diagonal residuals, contradicting the restricted rank via strict diagonal dominance. Numerical slack is positive. |
| 621–630, random cut | **PASS** | Each ordered disjoint `k`-minor survives with probability `4^{-k}`. |
| 632–645, no-pivot consequences | **PASS** | At `k=3`, Riesz-weighted order-three decay gives full half-potential `<200`; at `k=5`, order-five decay is integrable and yields density `<2400`. These conclusions are deliberately different. |
| 646–674, singular kernels | **PASS** | `J(d)` and the logarithmic kernel are bounded by direct splitting/layer-cake rearrangement at the constants used. |
| 676–714, `prop:pivot-H` | **PASS** | Scalar, definite-pair and indefinite-pair alternatives exhaust pivots. Scalar branch uses one surviving Schur direction only through the quarter-power/log bound; pair branches are measure domination statements. |
| 716–724, `prop:nine` | **PASS** | Pivot/no-pivot dichotomy is exhaustive; outside the unit window the half kernel is at most one, giving full half-potential `<=601`. |
| 726–749, main proof | **PASS** | No-pivot `<2400`; scalar pivot uses the nine-direction half-potential and costs `eta^-1/2=10`; pair branches are cheaper. No forbidden independence or continuity shortcut is used. |
| 750–773, scaling/corollary/equivalent interval formulation | **PASS** | With `Y=KX`, `Q=(s/K^2) Qtilde`; scalar density scaling yields exactly `K^2/s`. Interval domination is equivalent to the essential density cap. |
| 774–790, threshold limitations/remarks/bibliography | **PASS mathematically / UNCHECKED priority** | The manuscript accurately separates order-three and order-five thresholds and explicitly declines the three-eigenvalue theorem/global continuity shortcut. Bibliographic priority/exhaustive novelty is not a proof premise and was not independently exhaustively searched here. |

## The purported singular-Schur gap is not a gap

Let `q=N_A(t)-k`. If `q<=0` there is nothing to prove. For a sequence `epsilon_m->0` avoiding the finitely many bad shifts and with `|epsilon_m|<t`, the manuscript has

`N_(A+epsilon_m I)(t-|epsilon_m|) >= N_A(t)`.

The already-proved invertible case at that positive threshold gives

`N_(S_epsilon_m)(t-|epsilon_m|) >= q`.

Equivalently, the `q`-th largest eigenvalue modulus of the symmetric Schur complement satisfies

`s_q(S_epsilon_m) >= t-|epsilon_m|`.

Because the original pivot `B` is invertible, `(B+epsilon I)^(-1)->B^(-1)`, hence `S_epsilon_m->S` in operator norm. Ordered eigenvalue moduli are continuous for symmetric matrices, so

`s_q(S)=lim_m s_q(S_epsilon_m) >= lim_m (t-|epsilon_m|)=t`.

Therefore `N_S(t)>=q=N_A(t)-k`. The fact that the threshold moves is harmless because its limit is exactly `t` and the inequality is a lower bound on an ordered modulus. A hypothetical eigenvalue `t-sqrt(|epsilon|)` would simply violate the already-established inequality `s_q(S_epsilon)>=t-|epsilon|` for small `epsilon`; it is not a counterexample to the limit step.

Thus no source edit is mathematically required at lines 205–207, although expanding those three lines with the preceding ordered-modulus sentence would prevent the recurring false alarm.

## Support-package audit

- `README.md`: **PASS** for current source pin/delivery description.
- `DELIVERY_STATUS.md`: **PASS as a status snapshot**, not mathematical evidence by itself.
- `proof_map.csv`: **PASS**; ranges agree with the 790-line source.
- `SOURCE_MANIFEST.json`: **PASS** for source/blob/SHA/size consistency.
- `verify.py`: **PASS source review**; it pins the manuscript SHA and tests the interpolation identities, rank bounds, exact dominance slack, plus floating diagnostics. It is explicitly not a proof certificate.
- `checks.json`: **PASS recorded output/readback**: status PASS, 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, exact slack `297/2800`, 240 Schur-threshold diagnostics and 30 graph-weight diagnostics.
- independent re-execution of `verify.py` in this invocation: **UNCHECKED**. I read the code and its recorded output but did not claim a fresh Python execution.
- historical finite counts in `AUDIT.md`: **UNCHECKED historical provenance**. The manifest explicitly states that the current checker is a different suite and does not reproduce those counts.

## Multiplicity reduction after baseline audit

The strongest complete replacement theorem I can support from current source-pinned repository evidence is **nine eigenvalues**, not seventeen:

` s_9(A)>=s>0  =>  ||p_Q||_infinity <= 6010 K^2/s `

with all original hypotheses retained. The grouped original-coordinate product-Fourier compiler supplies a marginal-free order-three density receiver and order-two half-potential receiver; the rough-law endpoint has an explicit mollification/Fourier-Fatou proof. Multiple genuinely separate full reconstructions are present, and the current release-gate synthesis records two independent full PASS reviews for the conservative `6010` theorem. I do not claim any theorem below nine.

Multiplicity eight remains open. Current terminal work shows a two-sided/overlap collar and a literal `E_2` packet, but order-two control is a half-potential endpoint rather than a linear interval/density endpoint. A zero middle pair can already carry collar mass at the guaranteed scale, so the missing step must be a product-preserving overlap receiver rather than extraction of a conventional principal-pair pivot.

The improvement artifact from this B15 run gives one new analytic sharpening of that frontier: the half-potential of the Schur critical value cancels the entire determinant singularity in the **logarithmic** portion of the indefinite-pair envelope; only the nonlogarithmic hyperbolic tail term remains determinant-singular. This isolates the endpoint debt more sharply but does not prove multiplicity eight.

## Final verdict

- literal pinned 17-eigenvalue source: **PASS** in this B15 audit;
- fatal mathematical defects: **none found**;
- source ranges left mathematically UNCHECKED: **none**;
- external novelty/priority and independent rerun of the finite checker: **UNCHECKED**;
- strongest complete fixed-multiplicity density theorem supported here: **9 eigenvalues**, conservative reviewed constant `6010 K^2/s`;
- multiplicity 8: **OPEN**;
- unrestricted 3-eigenvalue conjecture: **OPEN**;
- global continuity is a separate conclusion and is not needed for the height proof.