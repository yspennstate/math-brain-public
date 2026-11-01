# fleet02/B01 fresh end-to-end audit — fixed multiplicity

Run: `20260924T140303Z-fleet02-B01-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
B01 lens: theorem quantifiers, scaling, dependency closure. Fleet02 lens: counterexamples/failure modes.

## Source pin

The audited mathematical baseline is immutable:

- source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`;
- git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- bytes/lines: `47883 / 790`.

During this invocation I fetched the live root, read `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and read `manuscript.tex` in full lines 1--790. The manuscript blob is unchanged. The support checker reports its own new finite suite only; historical self-audit test counts are not silently promoted into evidence.

## Overall verdict

**Literal 17-eigenvalue baseline: PASS in this fresh mathematical audit.** I found no theorem-level gap, false quantifier, missing dependency, scaling error, or illicit independence step.

A currently circulating peer label says manuscript lines 205--207 have a moving-threshold Schur-limit GAP. I do **not** sustain that label. The manuscript inference is rigorous: if `q=N_A(t)-k>0`, the invertible regularizations give `N_{S_epsilon}(t-|epsilon|)>=q`, equivalently `s_q(S_epsilon)>=t-|epsilon|`; since `S_epsilon->S`, singular-value continuity gives `s_q(S)>=t`, hence `N_S(t)>=q`. The speed at which an individual eigenvalue approaches its limit is irrelevant because the ordered singular value is already bounded from below by a threshold converging to `t`. A fixed-delta proof or the later rank-only decomposition is a valid expository alternative, but is not mathematically required to repair the pinned source.

**Best complete lower threshold independently reconstructed in this run: 9, with bound `6010 K^2/s`.** I re-derived the new grouped product-Fourier compiler, the marginal-free order-three density receiver, the order-two full half-potential receiver, and their pivot/no-pivot assembly rather than inheriting a prior PASS. I found no unpaid implication. This run does not self-award an additional independent-review credential; repository release synthesis records separate reviews elsewhere.

**Threshold 8 remains OPEN.** The newest collar, exact-zero two-anchor and half-potential/log-fusion results sharply localize the obstruction, but the nonlogarithmic small-pair term and aggregate-to-local provenance are still unpaid. No eight-direction theorem is claimed here.

## Complete baseline line coverage

| Lines / label | Status | Fresh reasoning, downstream impact, next obligation |
|---|---|---|
| 1--46 front matter / notation | PASS | Definitions match later use. `s_j` means singular values; for symmetric `A` these are eigenvalue moduli. The theorem claims essential boundedness, not global continuity. |
| 47--57 `thm:main` | PASS | Quantifiers are exactly arbitrary dimension, independent real cap-`K` coordinates, arbitrary symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0`. Interval domination is equivalent to an `L^infinity` density bound. |
| 59--80 corollary / architecture | PASS | `s_17>=s_33`; normalization parameters are `eta=1/100`, `kappa=80^-2`. Pivot/no-pivot split is exhaustive and all conditioning remains in original coordinates. |
| 91--120 `lem:fourier` | PASS | Fourier convention, Plancherel factor `2pi`, Gaussian transform and inversion constants check. Approximate-identity and weak-convergence steps are valid for rough laws. |
| 122--130 `lem:envelope` | PASS | `int min(1,(a/|t|)^p)=2ap/(p-1)` for `p>1`; inversion gives the stated density cap. |
| 132--160 `lem:riesz` | PASS | Gamma/Gaussian calculation gives coefficient `1/sqrt(2pi)`; the `3/4` envelope weighted by `|t|^-1/2` integrates to `12 sqrt(u)`. Tonelli handles extended values. |
| 169--181 `lem:rank` | PASS | SVD approximation formula yields both operator-Lipschitz singular values and the rank-shift inequality for nonsymmetric auxiliaries. |
| 183--207 `lem:schur` | PASS | Invertible case follows from the complementary compression of `A^-1`. Singular case is valid as written by the ordered-singular-value argument above. Later fixed-delta/rank-only proofs are optional replacements, not evidence that the literal source is false. |
| 209--217 `lem:dd` | PASS | Maximal-coordinate proof is valid without symmetry, exactly as needed for `R[H,H]`. |
| 221--255 `thm:bl` | PASS | Heat-flow derivative identity and frame contraction are correct; compact-time Gaussian domination justifies differentiation/integration by parts; large-time scaling and Fatou/truncation close the rough-input case. |
| 258--282 `lem:projection` | PASS with editorial clarification | The BL proof gives `prod b_i^{-b_i/2}`. After rows with `b_i=0` are dropped, the final step should be read as `sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`, not necessarily equality on the retained set. The claimed `e^(d/2)` bound remains correct. No rotated independence is used. |
| 284--301 `lem:scalar-fourier` | PASS | `m=floor(p/2)>=p/4`; inversion of the integrable even Fourier power and the product-projection scalar bound give `2pi sqrt(2e)/sqrt(p)`. Difference coordinates remain cap one. |
| 310--324 `lem:decoupling` | PASS | Cauchy--Schwarz is applied before introducing one independent copy of the literal `J` bank. Same-bank phases are discarded only after modulus. Product structure of the difference bank is preserved. |
| 326--373 `thm:determinant` | PASS | The regularized frame sums to identity; graph weights are in `[0,1]`; Jacobian/scaling factors are correct. The scalar Fourier-power factor cancels `d_i^-d_i/2`; `alpha=(2pi e)^2` cancels the remaining graph factor. Fourth root gives exponent `-1/8`. |
| 374--400 crossing volumes / `cor:vol-fourier` | PASS | Cauchy--Binet gives `Z_k=e_k(M^TM)`. Order five gives integrable exponent `5/4`; order three is used only under the Riesz weight. Counterexample boundary: `2XY` for cap-one uniforms has a logarithmic density singularity, so no generic rank-two density conclusion is available. |
| 404--421 `lem:square` / profile | PASS | Inverse branches and interval preimage length are correct. The conditional profile is measure domination via Tonelli, not an independence claim. |
| 423--434 `lem:definite` | PASS | Deterministic diagonalization of the two-dimensional integral gives Jacobian `1/(2sqrt(det B))` and cap `pi M/sqrt(|det B|)`. |
| 437--482 `lem:hyperbola` | PASS | Hyperbolic parametrization, Jacobian, original-coordinate monotone-tail selection, bathtub bound, middle interval and `Lambda>=2/sqrt D` all check. Exceptional critical level is handled measure-theoretically. |
| 485--525 `lem:quarter` | PASS | Diagonal branch uses the square preimage bound. Otherwise random signs produce a literal crossing of norm at least `L/4`; determinant decay plus Gaussian smoothing yields the quarter-power small-ball estimate and atomlessness. Layer cake gives `L_0=4+4log16`. |
| 528--543 pivot-volume definition / no-pivot entry bound | PASS | Ordered disjoint minors and strict no-pivot entry bounds match later sampling/cut formulas. |
| 545--564 `lem:sampling` | PASS | Bordered determinant identity is exact. An ordered `(r+1)` extension is counted at most `(r+1)^2`; singular seeds can have nonsingular extensions, so inequality rather than equality is correct. |
| 566--580 `lem:completion` | PASS | `E` is zero diagonal and supported in `LxL`; `D` vanishes on `S union T`; `R[L,L]=P[L,L]` has rank `<=r`; support of `R-P` in rows `T` or columns `S` gives global rank `<=3r`. Nonsymmetry is harmless because only ranks/singular values are used. |
| 582--619 `prop:volume` | PASS | Ratio selection is exhaustive. `r=0` contradicts `||A||<eta+sqrt(kappa)<1`. For `1<=r<=4`, `||E||<=1/16`; global rank forces `r+1` large diagonal entries in `L`, while restricted rank is `<=r`. Exact diagonal-dominance slack is `371/400-23/28=297/2800>0`. |
| 621--630 `lem:cut` | PASS | Every ordered disjoint `k`-minor survives a fair cut with probability `4^-k`; expectation and existence follow. |
| 632--645 `cor:no-pivot` | PASS | At orders 3 and 5, `Z_k^-1/(2k)<=160`. Constants `12sqrt(80e)<200` and `800e<2400` follow. |
| 654--674 `lem:kernels` | PASS | Near/far split for `J(d)` is integrable; centered-superlevel rearrangement gives the log-kernel bound 8. |
| 676--714 `prop:pivot-H` | PASS | Scalar pivot invokes Schur only for one surviving direction and uses quarter/log potential correctly. Definite and indefinite pair branches retain arbitrary conditioning shifts. `sup D^-1/2 log_+D=2/e`. |
| 716--724 `prop:nine` | PASS | Pivot branch controls truncated half-potential; the outside-unit tail adds at most 1. No-pivot order-three bound is already full. |
| 726--749 main proof / scaling | PASS | No-pivot order five, scalar pivot, definite pair and indefinite pair cover all cases. Scaling `Y=KX`, `A/s` and `Q=(s/K^2)Qtilde` gives exactly `K^2/s`; affine coefficients are transformed correctly. |
| 750--790 accounting / limitations | PASS | Dependency ledger matches the proof. The manuscript explicitly does not claim threshold 3, optimality, or global continuity. |

## Support/reproducibility audit

`SOURCE_MANIFEST.json` is PASS as a source-integrity record; `proof_map.csv` matches the theorem/proof ranges; `verify.py` is PASS within its finite diagnostic scope; `checks.json` records a successful new suite with 534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur threshold cases and 30 graph-weight cases. These checks are not proof certificates. The different historical finite-test counts stated in the author `AUDIT.md` remain **UNCHECKED as historical execution claims**, exactly as the manifest warns; this has no effect on the mathematical proof above.

## Dependency closure and counterexample boundaries

The baseline graph closes internally:

`BL -> product projection -> scalar Fourier powers -> decoupling -> determinant -> crossing-volume envelopes`,

`rank + Schur + diagonal dominance -> sampling -> completion -> spectral-to-volume -> random cut`,

and

`square/definite/hyperbolic + quarter concentration + singular kernels -> pivot half-potential -> nine-direction half-potential`.

The main theorem then combines the order-five no-pivot branch with scalar/pair pivots and exact scaling. No external specialized theorem is required for correctness.

Adversarial boundaries checked again: generic order-two crossing does not imply bounded density (`2XY`); order-three baseline determinant decay is not `L^1`; symmetrizing the interpolation loses the restricted-rank advantage; and no law-uniform pointwise scalar quadratic-phase decay is used.

## Lower-threshold audit status

The complete threshold-nine replacement is reconstructed separately in this run's improvement artifact. The exact next debt at threshold eight is not a vague rank-count issue: in the no-pivot state one can force either paid disjoint third volume or a quantitative repeated-anchor/two-sided collar. The newest exact-zero two-anchor receiver pays the full-zero anchor block, and the newest half-potential/log fusion cancels the logarithmic negative power of a nonzero pair determinant, but a `6 D^-1/2` nonlogarithmic term plus aggregate-to-local provenance remains. Until that implication is paid product-safely, threshold eight is GAP/OPEN rather than a theorem.
