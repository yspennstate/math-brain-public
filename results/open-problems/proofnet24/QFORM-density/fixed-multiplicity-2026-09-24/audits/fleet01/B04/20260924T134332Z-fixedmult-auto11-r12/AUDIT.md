# fleet01/B04 r12 — full fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T134332Z-fixedmult-auto11-r12`  
Role lens: geometric Brascamp--Lieb heat flow, derivative signs, integration by parts, Gaussian domination, and approximation limits; followed by an independent end-to-end read.

## Source pin

- Repository: `yspennstate/math-open-problems`
- Branch read: `master`
- Manuscript path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- Latest commit touching the manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- Bytes/lines: `47883 / 790`
- Master head observed during the run: `afb8a72698c7367670a6cd19dd98a3135ee4835b`; the manuscript blob itself is unchanged from the pinned baseline.

I read the complete 790-line `manuscript.tex`, plus `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. The support files that were missing in an earlier B04 run are now present. The new checker is explicitly a different reproducibility suite from the historical counts in `AUDIT.md`; this provenance difference is documented in `DELIVERY_STATUS.md` and `SOURCE_MANIFEST.json` and is not treated as a mathematical contradiction.

## Overall verdict

**PASS as a mathematical audit of the written 17-eigenvalue candidate.** I found no FALSE statement and no GAP in the 790-line proof. I do **not** upgrade the candidate to independently validated status: this report is one worker review, finite checks are not proofs, and the owner requires two genuinely separate complete reviews and reconciliation of conflicting findings before validation.

The full three-eigenvalue conjecture is not proved by this manuscript. The theorem audited here is exactly the arbitrary-law, arbitrary-dimension statement with `s_17(A)>=s>0`, arbitrary signs/remaining spectrum/affine terms, and density bound `10000 K^2/s`.

## Line-by-line / statement-by-statement audit

The line ranges below are the source ranges in the pinned 790-line manuscript (using the repository `proof_map.csv` for labeled statements).

| Source range | Label / content | Verdict | Independent reasoning in this run |
|---|---|---|---|
| 1--90 | Preamble, theorem statement, scaling architecture, conventions | PASS | Quantifiers and singular-value convention match the claimed theorem. The normalization `K=s=1` and final rescaling are dimensionally consistent. No continuity is claimed for the full theorem. |
| 91--120 | `lem:fourier` Fourier identities | PASS | Gaussian regularization gives the stated Plancherel normalization `2 pi`; approximate identity convergence in `L^2`, monotone convergence, weak convergence of `mu*g_eps`, and dominated convergence under `phi in L^1` justify inversion. Gaussian inversion constant `1/(2 sqrt(pi v))` is correct. |
| 122--130 | `lem:envelope` power envelope | PASS | Direct integration gives `2ap/(p-1)` and Fourier inversion gives `ap/[pi(p-1)]`. |
| 132--160 | `lem:riesz` negative half moments | PASS | Gamma representation and Tonelli are nonnegative. The substitution `w=t^2/(4v)` gives `sqrt(2) Gamma(1/4)|t|^{-1/2}`; the `3/4` envelope weighted integral is `12 sqrt(u)`. Constants and extended-value handling are correct. |
| 161--168 | Norm and spectral-count conventions | PASS | Used consistently downstream. |
| 169--181 | `lem:rank` perturbation and rank | PASS | Best low-rank approximation formula proves both Lipschitz singular-value inequality and the rank-shift inequality without symmetry. |
| 183--207 | `lem:schur` spectral count under a principal pivot | PASS | Invertible case follows from the inverse principal compression and positive/negative min-max counts. The singular-ambient `A+eps I` passage is terse but valid: apply at `t-|eps|`, use convergence of the Schur complements and continuity of ordered absolute eigenvalues, then let `eps->0`. |
| 209--217 | `lem:dd` diagonal dominance | PASS | Standard maximum-coordinate proof works for nonsymmetric matrices. |
| 221--255 | `thm:bl` geometric rank-one Brascamp--Lieb | **PASS** | Re-derived the full heat-flow proof. For `F=prod f_i(t,u_i.x)^{c_i}` and `v_i=(log f_i)'`, direct differentiation gives `(partial_t-Delta)F = F[sum c_i v_i^2 - |sum c_i u_i v_i|^2]`. The sign is nonnegative because the matrix with columns `sqrt(c_i)u_i` has `WW^T=I`, hence operator norm one. On every compact positive-time interval, compact support of the initial data gives Gaussian tails for `f_i` and derivatives and at-most-polynomial logarithmic derivatives; the frame identity turns the product into an integrable Gaussian majorant, so differentiation under the integral and integration by parts are justified. As `t->infty`, `sum c_i=d`, the rescaling `x=sqrt(t)z` gives the correct `(4 pi)^(-d/2)` Gaussian and dominated convergence to `prod M_i^{c_i}`. As `t downarrow 0`, inverse images of one-dimensional exceptional Lebesgue-point sets are null by rotation/Fubini, so Fatou gives the desired inequality. Monotone truncation handles arbitrary nonnegative integrable `h_i`; zero-mass factors are harmless. |
| 258--282 | `lem:projection` product projections | PASS | Orthogonal completion is used only in a deterministic integral. The row weights `b_i=1-|U^T e_i|^2` form a geometric BL frame in the orthogonal complement. The one-dimensional scaling and `f_i^{1/b_i}<=f_i` give the product bound, and `-b log b<=1-b` gives `e^{d/2}`. No rotated-independence claim occurs. |
| 284--301 | `lem:scalar-fourier` scalar Fourier powers | PASS | `m=floor(p/2)>=p/4`, `|hat f|<=1`, Plancherel/inversion for the `2m`-power, and the scalar projection bound yield the stated `2 pi sqrt(2e)/sqrt(p)` constant. Difference densities remain cap one by convolution. |
| 302--309 | Cross-form setup | PASS | Every quadratic polynomial across an original-coordinate cut has the stated form; affine terms stay inside `F,G`. |
| 310--324 | `lem:decoupling` | PASS | Cauchy--Schwarz in the `X_I` law, an independent `X'_J`, Fubini for modulus-one integrands, and Jensen give exactly the second- and fourth-power inequalities. The difference coordinates are independent and cap one. |
| 326--373 | `thm:determinant` regularized crossing determinant | PASS | Checked the regularized frame `H=alpha I+a^2 M^T M`, weights `c_j,d_i`, trace identity, BL scalings, `L^{1/c_j}` cap-one bound, scalar Fourier input at exponent `2/d_i`, cancellation of the `d_i` powers, entropy factor for the `c_j`, and the choice `alpha=(2 pi e)^2`. Taking fourth roots produces exactly exponent `-1/8` and coefficient `t^2/(pi^2 e^2)`. Rows with `d_i=0` are legitimately omitted. |
| 374--385 | `Z_k` and Cauchy--Binet expansion | PASS | Both physical-minor and singular-value formulas are standard Cauchy--Binet identities and are used with the correct ordered/unordered conventions. |
| 386--400 | `cor:vol-fourier` | PASS | Keeping the order-`k` determinant term gives exponent `k/4`; `k=5` is integrable and gives `5e Z_5^{-1/10}`, while `k=3` is used only with the Riesz half-potential weight. |
| 404--414 | `lem:square` scalar square profile | PASS | Monotone-branch change of variables and the interval-preimage estimate are correct for arbitrary cap-one rough densities. |
| 415--422 | Conditional scalar profile | PASS | Completing the square conditionally gives a domination of measures. Tonelli, not an independence claim between the square and residual, justifies the displayed profile. |
| 423--434 | `lem:definite` definite pair | PASS | Deterministic orthogonal diagonalization is applied only inside the two-dimensional integral. Jacobian is `1/(2 sqrt(det B))`, so integration over `theta` gives `pi M/sqrt(|det B|)`. |
| 437--482 | `lem:hyperbola` indefinite pair | PASS | Rechecked the hyperbolic parametrization, Jacobian, exponential tail monotonicity, the rearrangement bound for `1/|y|`, the middle interval length, and `Lambda>=2/sqrt(D)`. Rough-density exceptional slices are handled through the nonnegative test-function formulation. No rotated independence is used. |
| 485--525 | `lem:quarter` quarter-power concentration | PASS | Diagonal-pivot branch is immediate from the square profile. In the off-diagonal branch, random signs produce a physical cut with crossing norm at least `L/4`; retaining one singular factor in the determinant theorem gives the `|t|^{-1/4}` envelope. Gaussian smoothing, the gamma integral, and the chosen `v=1/8` give a coefficient below 16. Layer cake yields the logarithmic potential bound and rules out atoms. |
| 528--544 | `def:pivot-volume`, no-pivot entry bounds | PASS | From `|a_ii|<eta` and the principal `2x2` determinant bound, `|a_ij|^2<eta^2+eta<2eta`, hence `|a_ij|<1/7`. Ordered disjoint volume conventions are consistent with the random-cut formula. |
| 545--564 | `lem:sampling` volume-sampled interpolation | PASS | Bordered-determinant identity is exact for nonsingular seeds. Squaring removes ordering signs. Each ordered `(r+1)` disjoint minor can be charged at most `(r+1)^2` times; singular seeds may have nonsingular extensions, so the proof correctly uses an inequality rather than equality. Interpolation on rows `S` and columns `T` and rank `<=r` are exact. |
| 566--580 | `lem:completion` | PASS | With `E` equal to the off-diagonal residual on `LxL` and `D` the diagonal residual on `L`, `R_{L,L}=P_{L,L}` and `D=0` on `S union T`. Support of `R-P` is confined to rows `T` or columns `S`, giving global rank `<=3r`; the restricted rank is `<=r`. Symmetry is not falsely imposed on the auxiliaries. |
| 582--619 | `prop:volume` no-pivot spectral-to-volume | PASS | The telescoping/first-zero alternative finds a bad ratio. At `r=0`, the operator norm is below one. For `1<=r<=4`, `||E||<=1/16`; rank perturbation gives `r+1` large entries of diagonal `D`, all in `L`. The constants `371/400` and `23/112` make every `(r+1)x(r+1)` restricted block strictly diagonally dominant, contradicting `rank R_{L,L}<=r`. The argument correctly uses singular values for the nonsymmetric `D+R`. |
| 621--630 | `lem:cut` random coordinate cut | PASS | A disjoint ordered pair of `k`-sets lands in opposite labeled banks with probability `4^{-k}`. Linearity of expectation gives the claimed cut. |
| 632--645 | `cor:no-pivot` | PASS | `Z_k^{-1/(2k)}<=2 kappa^{-1/2}=160`; the order-three half-potential constant is below 200 and the order-five density constant is below 2400. All affine/same-bank terms are retained by the cross-form theorem. |
| 646--653 | Truncated half potential definition | PASS | Atom convention and later full-vs-truncated decomposition are consistent. |
| 654--674 | `lem:kernels` singular integrals | PASS | Near/far split for `J(d)` gives the logarithmic bound; the log-kernel superlevel-set argument correctly maximizes interval overlap at aligned centers and evaluates to 8. |
| 676--714 | `prop:pivot-H` | PASS | Scalar pivot: Schur leaves one spectral direction, quarter-power lemma excludes an atom and controls the logarithm. Definite pair gives direct conditional density. Indefinite pair uses the hyperbolic envelope and the exact scalar maximization `sup D^{-1/2} log_+ D=2/e`. Constants are below 600. |
| 716--724 | `prop:nine` | PASS | Pivot branch uses the previous proposition; no-pivot branch uses the full half potential `<200`. Outside the truncation interval the kernel is at most one, giving 601. |
| 726--749 | `thm:main` proof and `cor:33` | PASS | No-pivot uses order five. A scalar pivot leaves at least sixteen spectral directions and hence enough for the nine-direction half-potential theorem. Pair pivots are uniformly controlled. The final normalization `Y=KX`, `A/s`, and `Q=(s/K^2) Qtilde` gives exactly `10000 K^2/s`. Interval domination and essential density equivalence are standard measure arguments. |
| 750--790 | Threshold accounting, limitations, remarks, acknowledgment, bibliography | PASS for mathematical statements; literature attribution not independently priority-checked | The text accurately distinguishes order-five direct density from order-three half-potential use and explicitly disclaims a three-eigenvalue theorem/continuity shortcut. The two bibliography entries are attribution only and are not dependencies of the proof. I did not perform a fresh literature-priority audit in this B04 run, so priority/attribution beyond the stated classical context is **UNCHECKED** here and has no downstream mathematical effect. |

### Specialized B04 heat-flow checks

The sensitive heat-flow points all pass:

1. **Derivative sign:** exact expansion yields `sum c_i v_i^2 - |sum c_i u_i v_i|^2`; the frame matrix is a contraction in precisely the required direction.
2. **Integration by parts:** only positive times are used before the limit; compact initial support plus heat convolution gives Gaussian tails uniformly on compact positive-time intervals. The frame identity turns the product into a Gaussian in all `d` directions.
3. **Large-time Gaussian domination:** the scaling limit and normalization `(4 pi)^(-d/2)` are correct, and an integrable `exp(-|z|^2/8)` majorant is available for `t>=1`.
4. **Small-time approximation:** Lebesgue differentiation is applied only along nonzero one-dimensional functionals; inverse images of null sets are null. Fatou has the correct inequality direction because the heat-flow integral is nondecreasing.
5. **Rough-law limit:** `min(h_i,m) 1_{[-m,m]}` increases monotonically to `h_i`, so monotone convergence applies to both sides with no smoothness/moment/support hypothesis left in the theorem.

## Support-file audit

- `proof_map.csv`: **PASS** as an accurate source-range map for the labeled statements used above.
- `SOURCE_MANIFEST.json`: **PASS** for source identity/provenance; the manuscript blob/hash/bytes/lines match the fetched source.
- `verify.py`: **PASS as a finite regression suite, not as a proof certificate.** Its exact checks correctly test the interpolation support/ranks, bordered-minor relation, volume-sampling inequality and diagonal-dominance arithmetic; the floating tests are explicitly diagnostics.
- `checks.json`: **PASS as the recorded output of that new suite**: 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict cases, exact slack `297/2800`, 240 floating Schur threshold cases, and 30 graph-weight cases.
- `AUDIT.md`: **PASS as historical self-audit metadata, not independent evidence.** Its older finite-test counts are not reproduced by `verify.py`; the repository explicitly documents that the newly supplied suite is different.

## Lower-threshold status after this audit

The baseline 17 theorem survives this review. I do **not** claim an unconditional 16-eigenvalue theorem. Fresh repository work shows the `s_16` attempt has been reduced to a genuine terminal order-four geometry, not solved: one branch gives an exact three-bank rank-four collar and another gives a carrier-orthogonal same-bank crossing, but both explicitly stop short of an `L^infinity` theorem.

This run adds a separate exact mixed-exterior identity and a paid `s_16` sub-branch in the sibling improvement file `MIXED_EXTERIOR_ENDPOINT.md`. It closes the terminal `s_16` chamber whenever at least half of the forced mixed four-plus-one exterior energy is physically disjoint. If not, the only remaining obstruction is an explicit weighted row-leverage/self-coordinate trapping functional. This is a strict narrowing of the `17 -> 16` debt, not a full threshold reduction.

## Final status

- Mathematical manuscript: **PASS in this independent B04 read**.
- Fatal defects found: **none**.
- Mathematical portions left UNCHECKED: **none in the manuscript itself**.
- External literature priority/attribution: **UNCHECKED in this B04 run** (not a proof dependency).
- Candidate independent-validation status: **NOT AWARDED**.
- Lowest unconditional `L^infinity` multiplicity certified by a complete proof in this run: **17**.
- Full three-eigenvalue conjecture: **OPEN**.
