# fleet01/B12 complete fixed-multiplicity audit — 20260924T141340Z

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `fleet01/B12`  
Pinned owner source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned/current manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256 from the current objective/manifest: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Source: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, 790 lines.

## Overall verdict

**PASS on the entire 790-line mathematical manuscript.** I independently reread every definition, displayed equation, lemma/proposition/theorem statement, proof, scaling step, and limitation statement. I found **no FALSE mathematical claim and no theorem-changing GAP** in the candidate theorem

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
\le 10^4K^2/s
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary affine terms, and independent arbitrary real coordinate laws having densities at most `K`.

The proof establishes an essentially bounded density globally. Continuity is proved in the Fourier/no-pivot branches where the characteristic function is integrable; it is not asserted for all pivot branches. The unrestricted three-large-eigenvalue conjecture is not claimed solved.

## Exact line/range audit

The ranges below use the canonical 790-line source and the current `proof_map.csv`.

| Lines | Item | Verdict | Independent reasoning |
|---|---|---|---|
| 1–46 | Preamble, notation, abstract | PASS | Definitions of singular values, density norm, symmetry, affine scope, and the claimed 17-direction theorem are consistent. No hidden smoothness, moment, support, sign, or rotated-independence assumption appears. |
| 47–57 | Theorem 1 (main) | PASS | Quantifiers exactly match the advertised fixed-multiplicity theorem. The interval formulation is equivalent once the bounded density is constructed. |
| 58–83 | Corollary, normalization, architecture | PASS | `s_33<=s_17`; `eta=1/100`, `kappa=80^{-2}` and the counts `9=4*3-3`, `17=4*5-3` are used consistently. Essential boundedness rather than continuity is correctly stated as the global conclusion. |
| 84–120 | Fourier conventions, Gaussian regularization, inversion | PASS | Fourier normalization gives Plancherel factor `2pi`, inversion factor `1/(2pi)`, and the displayed Gaussian identity. Approximate-identity and weak convergence arguments establish a genuine density when `phi in L1`. |
| 122–130 | Power envelope | PASS | The envelope integral is `2ap/(p-1)`; inversion gives `ap/[pi(p-1)]`. |
| 132–160 | Negative-half-moment/Riesz estimate | PASS | Gamma representation plus Gaussian inversion/Tonelli yields coefficient `1/sqrt(2pi)`. For the `3/4` envelope the weighted integral is exactly `12 sqrt(u)`. |
| 161–181 | Norm conventions; perturbation/rank lemma | PASS | Approximation numbers prove the nonsymmetric singular-value perturbation and rank-shift inequalities used later. |
| 183–207 | Schur-complement spectral count | PASS | For invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`. Positive and negative principal-compression interlacing separately imply the absolute spectral count. The `A+eps I` argument correctly handles singular `A` with strict/inclusive thresholds converging in the right direction. |
| 209–217 | Strict diagonal dominance | PASS | Standard maximum-coordinate proof; symmetry is not required. |
| 221–255 | Geometric rank-one Brascamp–Lieb | PASS | The heat-flow identity has the correct sign because the rank-one frame is a contraction. Trace gives `sum c_i=d`; Gaussian tails justify differentiation/integration by parts; the large-time normalization and small-time Fatou argument are correct. |
| 258–282 | Product-projection density | PASS | The deterministic orthogonal change is used only inside an integral. For `b_i>0`, BL gives the stated product and `f_i^{1/b_i}<=f_i`. Extending the entropy sum by zero terms at `b_i=0` gives `sum(-b_i log b_i)<=sum(1-b_i)=d`; no rotated independence is asserted. |
| 284–301 | Integrated scalar Fourier powers | PASS | `m=floor(p/2)>=p/4`; `|fhat|<=1`; the `2m`-power is the characteristic function of a genuine sum of independent differences. Product projection bounds its continuous inversion density at zero and produces the stated constant. |
| 303–324 | Cross form and decoupling | PASS | Conditioning/Cauchy–Schwarz is on original independent blocks. Expanding an independent copy gives exactly the two displayed powers; difference coordinates remain independent and cap-one. |
| 326–373 | Regularized crossing determinant theorem | PASS | The regularized vectors form the exact frame. The BL scale factors, `d_i` Fourier powers, entropy factor, and `alpha=(2pi e)^2` cancellation are all correct. Taking the fourth root yields exponent `-1/8` and scale `t^2/(pi^2 e^2)`. |
| 375–400 | Crossing volumes and volume envelopes | PASS | Cauchy–Binet gives the determinant polynomial and `Z_k`. Retaining order `k` produces `|t|^{-k/4}`; `k=5` is directly integrable and `k=3` is used only with the half-Riesz weight. Constants `5e` and the displayed half-potential bound check. |
| 404–414 | Scalar square profile | PASS | Two monotone inverse branches give the density and interval-preimage bounds; conditional use is through nonnegative test functions/Tonelli, not a false independence claim. |
| 423–434 | Definite two-coordinate pair | PASS | Completing the square and deterministic elliptic coordinates give Jacobian `1/(2 sqrt(det B))`, hence `pi M/sqrt(|det B|)`. Rotation is only a deterministic integration coordinate change. |
| 437–482 | Hyperbolic pair/log envelope | PASS | Hyperbolic charts have Jacobian `1/(2sqrt D)`. The positive and negative tails are controlled by a genuine original coordinate after the stated cutoffs; the cap-one/mass-one bathtub step is valid. The middle interval and `Lambda>=2/sqrt D` produce the stated logarithmic envelope. Critical fibers are null and downstream conditioning is handled measure-theoretically. |
| 485–525 | Quarter-power concentration/log potential | PASS | Either a physical diagonal is large or a random sign cut gives a physical cross block with norm at least `L/4`. Retaining one singular factor in the determinant theorem and Gaussian smoothing yields the `rho^{1/4}` small-ball estimate. Layer cake gives `4+4 log 16`; atoms are excluded. |
| 528–535 | Pivot/volume definition and no-pivot entry bound | PASS | From `|a_ii|<eta` and the principal `2x2` determinant bound, `|a_ij|^2<eta+eta^2<1/49`, hence the manuscript's `<1/7` bound is valid. |
| 545–564 | Volume-sampled interpolation | PASS | Bordering an invertible disjoint seed gives exactly `det(B)^2(A_lm-P_lm)^2`. Each order-`r+1` ordered disjoint pair has at most `(r+1)^2` predecessors; singular seeds only reduce the sum. Exact row/column interpolation and rank `<=r` are correct. |
| 566–580 | Diagonal + interpolation completion | PASS | With the stated `D,E`, one has `R[L,L]=P[L,L]`. `R-P` is supported only in rows `T` or columns `S`; adding the rank-`r` matrix `P` gives `rank R<=3r`, while the restricted rank is `<=r`. Nonsymmetry is explicitly allowed and used only algebraically. |
| 582–619 | No-pivot spectral-to-volume proposition | PASS | A bad ratio gives `eps<=(r+1)/80<=1/16`. With `m=4k-3` and `r<=k-1`, `m>=4r+1`; after rank loss `3r`, at least `r+1` large diagonal entries remain in `L`. On that set `|R_ii|>=371/400`, off-diagonal row sum is `<23/28`, leaving exact positive slack `297/2800`. This contradicts `rank R[L,L]<=r`. The `r=0` norm contradiction is also valid. |
| 621–630 | Random coordinate cut | PASS | Each ordered disjoint `(S,T)` survives a fair cut with probability `4^{-k}`. |
| 632–645 | No-pivot analytic consequences | PASS | `Z_k^{-1/(2k)}<=160`; substitution into the order-three/order-five receivers gives `<200` full half-potential and `<2400` density, respectively. |
| 654–674 | Singular kernels | PASS | Region splitting proves the square-root kernel convolution bound; layer-cake/superlevel overlap proves the log-kernel bound, with the centered case extremal. |
| 676–714 | Pivot controls truncated half-potential | PASS | Scalar pivot uses the exact square profile and one Schur-surviving direction; definite pair is direct; indefinite pair combines the hyperbolic envelope with the log-kernel estimate. Constants and `sup D^{-1/2} log_+ D=2/e` are correct. |
| 716–724 | Nine-eigenvalue half-potential | PASS | Pivot branch uses the preceding truncated estimate; no-pivot branch has the stronger full half-potential bound. The tail outside distance one contributes at most one, giving `<=601`. |
| 726–758 | Main proof, all pivot branches and scaling | PASS | No-pivot gives `<2400`. Scalar pivot under `s_17>=1` leaves at least 16 Schur directions, hence nine suffice, giving `6010`. Definite pair gives `<40`. Indefinite pair leaves at least 15 directions but only one is needed for the logarithmic potential, giving `<251`. For general `K,s`, `Y=KX` has cap-one densities and `Q=(s/K^2) Qtilde`, producing exactly `10^4 K^2/s`. |
| 760–790 | Threshold accounting, limitations, acknowledgement, bibliography | PASS for mathematical statements; UNCHECKED for exhaustive priority | The rank bookkeeping and analytic exponents accurately explain why the present proof closes at 17. The continuity limitation is correctly separated. Bibliographic metadata is not a proof dependency; I did not perform an exhaustive priority/novelty search. |

### Manuscript summary by verdict

- **PASS:** lines 1–790, all mathematical definitions/equations/proofs.
- **GAP:** none found in the mathematical manuscript.
- **FALSE:** none found.
- **UNCHECKED:** exhaustive novelty/priority of the two antecedent citations only; this has no proof impact.

## Package/support-file audit on current `master`

The support-file situation has changed since my preceding B12 run. The advertised files are now present on current `master`.

| Artifact | Verdict | Reason |
|---|---|---|
| `README.md` | PASS | Correctly identifies the pinned theorem/source and now points to `DELIVERY_STATUS.md`; descriptions match the manuscript. |
| `AUDIT.md` | PASS for mathematical descriptions; UNCHECKED for historical execution provenance | The self-audit's proof descriptions are consistent with this independent review. Its historical checker counts are records of a past run and were not independently reproduced here. |
| `proof_map.csv` | PASS | The mapped labels/ranges agree with the canonical source and were used for the line audit above. |
| `SOURCE_MANIFEST.json` | PASS for text/source hashes; UNCHECKED for compiled-PDF binary claims | It records the same manuscript blob/SHA-256/line count and hashes for the support files. I did not independently obtain/visually inspect the compiled PDF binary. |
| `verify.py` | PASS as code audit | The script checks the pinned source hash, exact arithmetic/slack, exact interpolation identities on a finite deterministic suite, and numerical Schur/graph diagnostics. Its own comments correctly state that these are finite checks rather than a universal proof. |
| `checks.json` | PASS as a repository execution record; UNCHECKED as an independently rerun execution | It records `PASS`, 534 exact interpolation seeds, 18 exact volume comparisons, 240 numerical Schur cases, and 30 graph-weight cases, consistent with the current delivery status. I did not rerun the Python process in this invocation, so execution provenance is not independently certified by this review. |
| `DELIVERY_STATUS.md` | PASS as status metadata | It explicitly distinguishes the current checker suite from the historical self-audit suite and does not elevate finite tests to proof. |

Thus the prior B12 **package GAP is resolved on current `master`**. Remaining UNCHECKED package items are only independent rerun/compiled-binary provenance, not mathematical dependencies.

## B12 lens: scalar pivot, square branches, singular kernels, nine-direction closure

The scalar-pivot chain is internally complete. Conditional square inversion produces the one-sided `|z-R|^{-1/2}` profile without assuming independence from the Schur remainder. The manuscript correctly needs a half-potential of `R`; the nine-direction theorem supplies it by an exhaustive pivot/no-pivot split. The truncated/full distinction is handled explicitly: pivot control supplies `H(R)<=600`, no-pivot supplies the stronger full half-potential `<200`, and the tail outside distance one costs at most one.

The logarithmic branch is likewise complete. The hyperbolic two-coordinate envelope has the correct logarithmic singularity, and the quarter-power small-ball estimate supplies a uniform logarithmic potential as soon as one Schur eigenvalue survives. The final indefinite-pair branch therefore needs only `s_3` locally; the large global multiplicity is not spent there.

As proved in my preceding B12 improvement and rechecked here, the current local multiplicity ledger is:

- scalar pivot: `s_10(A)>=1` suffices for `||p_Q||_infty<=6010`;
- definite `2x2` pivot: no spectral multiplicity beyond the pivot is needed, `||p_Q||_infty<=10pi`;
- indefinite `2x2` pivot: `s_3(A)>=1` suffices for `||p_Q||_infty<251`.

Therefore every obstruction to lowering the **global** 17 threshold lies in the no-pivot branch.

## Threshold-lowering status after this audit

No unconditional replacement of 17 by 16 is validated here. The exact `s_16` obstruction remains the terminal `r=4` saturation chamber. My earlier B12 reduction and the newer B09/B20 improvements show that the chamber is much more structured than the baseline proof records, but a new analytic/aggregate receiver is still required. The companion improvement from this run proves two additional structural/analytic facts: an exact-rank crossing Plancherel receiver and a quantitative double-leverage polarization of every low-residual terminal seed. Those results are saved separately under this run's `improvements/` directory.

## Independent-review gate

This B12 artifact is one complete end-to-end review. Other repository workers have separately recorded complete PASS audits of the same pinned 790-line source. I do **not** infer or self-award owner-level validation from their existence, and I do not alter release status. Any replacement theorem below 17 still requires its own full proof plus the owner's required two genuinely separate end-to-end reviews.

## Privacy/write scope

Only the authorized QFORM manuscript, its support/audit artifacts, relevant QFORM mathematical predecessor reports, and current brain objective/control were read. No task/cadence, email/push, permission, account-binding, repository-visibility, paid-model/API, public-release, or remote-workflow state was changed.