# account01/B14 full fixed-multiplicity audit — rough-law / measure-theory lens

Run: `20260924T150955Z-account01-B14-fixedmult-audit-r2`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline commit requested by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob on fresh `master`: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256 from `SOURCE_MANIFEST.json`: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Pinned size: 47,883 bytes, 790 lines.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Executive verdict

**Main 17-eigenvalue theorem: PASS after two local statement-hypothesis repairs described below.** I found no fatal defect in the argument proving the theorem for the stated independent density-capped inputs. However, the self-contained manuscript is **not literally line-by-line PASS as written**: Lemma `lem:quarter` (statement lines 485--494) is false without the product density hypothesis used in its proof, and Proposition `prop:pivot-H` (statement lines 676--681) omits the same normalized input-law hypothesis. These are local formal defects, not a counterexample to Theorem 1.1, because every actual use in the main proof occurs under independent coordinate densities bounded by one after normalization.

A one-dimensional counterexample to the literal `lem:quarter` statement is `X=0` a.s., `S=[1]`, `b=c=0`: then `R=0` has an atom, contradicting the asserted atom exclusion and the small-ball estimate for sufficiently small `rho`. The proof at lines 495--525 explicitly conditions on coordinates with density cap one and later invokes the determinant theorem for product laws; those assumptions must be in the statement.

## Exhaustive source audit by exact manuscript ranges

The ranges below cover the mathematical source and proof map. `PASS` means I rederived the stated implication under its written hypotheses; `GAP` means the argument is repairable but a hypothesis or justification is omitted; `FALSE` means the literal standalone statement has a counterexample; `UNCHECKED` means non-proof bibliographic/priority metadata was not externally verified.

| Lines | Item | Verdict | Audit note |
|---|---|---|---|
| 1--46 | preamble, abstract, definitions of notation | PASS | No mathematical dependency beyond later theorem; rough-law scope is stated without moments/support assumptions. |
| 47--57 | Theorem 1.1 (`thm:main`) | PASS | Quantifiers, affine terms, scaling target, and interval/density formulation are correct once the two local hypotheses below are repaired. |
| 59--61 | Corollary 1.2 | PASS | Immediate since `s_33>=s` implies `s_17>=s`. |
| 62--90 | architecture, parameters, conventions | PASS | No hidden smoothness/moment/support assumption introduced. |
| 91--120 | Fourier inversion / Gaussian regularization (`lem:fourier`) | PASS | `L1∩L2` Plancherel and Gaussian approximate identity are enough; weak convergence of `mu*g_eps` requires no moments. |
| 122--130 | Fourier-envelope consequences | PASS | Direct integrability and inversion; constants consistent. |
| 132--160 | negative-half Riesz formula (`lem:riesz`) | PASS | Nonnegative Tonelli justifies all exchanges; Gaussian regularization handles rough laws and possible infinite values. |
| 169--181 | finite-rank singular-value count | PASS | Correct min-max/rank argument. |
| 183--207 | Schur spectral count (`lem:schur`) | PASS | Invertible case follows from inverse-compression interlacing; the `A+eps I` limit is valid. The moving threshold argument is terse but not defective: if the desired count failed at `t`, continuity gives a fixed gap contradicting the estimates at `t-|eps|`. |
| 209--217 | diagonal-dominance perturbation | PASS | Standard norm/rank estimate. |
| 221--255 | geometric Brascamp--Lieb theorem | PASS | Heat-flow sign, integration by parts/truncation, and monotone approximation check. |
| 258--282 | product-projection density (`lem:projection`) | PASS | There is a harmless omitted intermediate inequality after zero leverage scores are dropped: `sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`. The displayed final bound remains valid. |
| 284--301 | scalar Fourier powers | PASS | `|fhat|^{2m}` is integrable by Plancherel and is the CF of a sum of differences; projection scaling is correct. |
| 310--324 | decoupling identity | PASS | Bounded phases make Fubini automatic; difference coordinates remain independent cap-one. |
| 326--373 | determinant Fourier estimate | PASS | BL exponents, determinant Jacobian, entropy cancellation, and `alpha=(2 pi e)^2` normalization rechecked. No rotated-coordinate independence is assumed. |
| 386--400 | crossing-volume Fourier corollary | PASS | `k=5` gives the stated density bound and `k=3` the full half-potential bound; exponents/constants are consistent. |
| 404--414 | scalar square profile | PASS | Valid for a measurable Lebesgue-density version `f<=1` a.e.; monotone-branch change of variables can be stated measure-theoretically. |
| 415--421 | conditional square-profile domination (`eq:profile`) | PASS | Best read as a test-function/kernel inequality. Tonelli avoids any need to choose pointwise conditional density values on null fibers. |
| 423--434 | definite pair | PASS | Joint-density cap is sufficient; orthogonal diagonalization is only deterministic integration. |
| 437--482 | indefinite/hyperbolic pair | PASS | Tail cutoffs, coarea/Jacobian factors, and null critical level are valid for rough densities via the nonnegative test-function formulation. |
| 485--494 | quarter-power concentration statement (`lem:quarter`) | **FALSE as written** | Missing hypothesis: `X` must have independent coordinates with densities bounded by one. Counterexample: deterministic `X=0`, `S=[1]`. |
| 495--525 | proof of `lem:quarter` | **GAP as written; PASS after hypothesis insertion** | The first conditioning step uses the scalar cap-one law and the second branch invokes the determinant theorem for an original product bank. With the missing hypothesis inserted, the proof and `L0=4+4 log 16` bound check. |
| 528--535 | pivot / disjoint-volume definition | PASS | Definitions coherent, ordered disjoint pairs correctly specified. |
| 537--543 | no-pivot entry bounds | PASS | `eta^2+eta<2 eta` and `sqrt(2 eta)<1/7` at `eta=1/100`. |
| 545--564 | volume-sampled interpolation | PASS | Border determinant identity and `(r+1)^2` counting checked; singular deleted seeds only reduce the sum. |
| 566--580 | interpolation completion | PASS | `rank R<=3r`, while the crucial restriction `rank R[L,L]<=r`; support bookkeeping is correct despite nonsymmetry of `P`. |
| 582--619 | spectral-to-volume proposition | PASS | Rank count `m-3r>=r+1`, seed-zero diagonal, and strict diagonal dominance contradiction all check for `k<=5`. |
| 621--630 | random coordinate cut | PASS | Every ordered disjoint pair survives with probability `4^{-k}`. |
| 632--645 | no-pivot analytic consequences | PASS | Explicitly includes independent cap-one input law; constants and exponents check. |
| 654--674 | singular-kernel integral lemmas | PASS | Rearrangement/Tonelli arguments work for nonnegative kernels and arbitrary shifts. |
| 676--681 | pivot-half-potential proposition statement | **GAP** | `Q`/`X` law is not restated. Standalone claim would be false for arbitrary/discrete inputs. Repair: assume independent coordinate densities bounded by one and define `Q=X^TAX+b^TX+c`. |
| 682--714 | proof of pivot-half-potential proposition | **PASS after the statement repair** | Scalar, definite-pair, and indefinite-pair branches check. The exact scalar branch is `200+120 log 16<560`; the other branches are smaller. |
| 716--724 | nine-eigenvalue half-potential proposition | PASS | This statement explicitly includes independent cap-one coordinate densities; after repairing `prop:pivot-H`, both pivot and no-pivot branches are valid. |
| 726--749 | proof of Theorem 1.1 / Corollary | PASS | Scalar pivot loses one Schur direction, pair pivot loses two, no-pivot uses order five, and `Y=KX` scaling gives exactly `K^2/s`. No moment/support hypothesis enters. |
| 750--790 | acknowledgments / bibliography / formatting | UNCHECKED for bibliographic priority; PASS as non-proof text | I did not externally priority-check citation metadata. None of it is a logical dependency of the proof. |

## Rough-law / measure-theory conclusions

1. **Measurable density versions.** Every place using `f<=1` can choose a Borel representative modified on a null set. The conclusions are measure statements; no pointwise value on a null set is logically used.
2. **Conditional kernels.** The scalar profile and indefinite-pair envelopes should be interpreted against nonnegative output test functions and then mixed by Tonelli. This is exactly enough for arbitrary conditioning-generated affine shifts and avoids selecting conditional-density versions on exceptional fibers.
3. **Fubini/Tonelli.** Oscillatory exchanges in the Fourier sections are with bounded integrands under finite probability measures. Singular-kernel exchanges are nonnegative. No moment hypothesis is needed.
4. **Approximate identities / weak limits.** The Gaussian regularizations converge weakly for arbitrary probability laws. Uniform `L2` bounds can be passed to an unmollified complex pushforward by weak `L2` compactness; no bounded support or smoothness is required.
5. **Unbounded supports and translations.** Every bound used in the baseline proof is translation invariant and depends on density caps / deterministic spectral quantities, not support diameter or moments.

## Threshold lowering gate

I also audited the complete `s_9` replacement proof at `improvements/account02/B09/20260924T144107Z-account02-B09-fixedmult-auto11/NINE_EIGENVALUE_REPLACEMENT.md`. Its new grouped product-Fourier compiler is sound under arbitrary rough product laws: hub complex pushforwards are dominated by positive pushforwards, the light-side pushforward is mollified before `L2` expansion, all conditioning remains on literal original-coordinate banks, and the uniform mollified `L2` estimate passes to the original complex measure without support/moment assumptions.

The replacement closes:
- no-pivot `s_9` by order-three crossing volume and the new `E_3` density receiver;
- scalar pivot by a full Schur half-potential, using either an existing pivot or the new order-two `E_2` receiver;
- definite/indefinite pair pivots by the baseline pair estimates.

The complete theorem is therefore valid at multiplicity **9**. The proof artifact is complete, and I found at least three separate complete PASS reconstructions/reviews in the private tree: account01/B07, account01/B16, and account02/B05. Thus the owner's “full replacement proof plus two complete reviews” gate is satisfied for multiplicity 9. I found no complete multiplicity-8 density receiver; the current `s_8` artifacts reduce to overlap/collar/masked-shear structures but remain analytically unpaid. I therefore do **not** validate 8 or any lower multiplicity.

## Final classifications

- Baseline 17-eigenvalue theorem for the stated owner scope: **PASS after local hypothesis repair**.
- Literal self-contained manuscript without repair: **contains one FALSE lemma statement and one GAP proposition statement**, both nonfatal to the main theorem.
- Multiplicity 9 replacement theorem: **PASS / review gate met**.
- Multiplicity 8: **GAP / OPEN**.
- Full multiplicity 3 target: **OPEN**.
