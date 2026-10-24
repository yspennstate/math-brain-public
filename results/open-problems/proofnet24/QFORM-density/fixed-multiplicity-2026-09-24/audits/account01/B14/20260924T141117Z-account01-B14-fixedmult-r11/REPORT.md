# account01/B14 — full fixed-multiplicity audit, rough-law closure, and threshold status

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T141117Z-account01-B14-fixedmult-r11`  
Reviewer: `account01/B14`  
Starting lens: rough input laws, measurable density versions, conditional kernels, Tonelli/Fubini, null slices, weak/approximate-identity limits, unbounded supports and translations.

## Source pin

I read fresh owner control from `math-research-brain/main/AGENTS.md` and `scheduled_tasks/CURRENT_OBJECTIVE.md`, then read the complete canonical package under `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/`: `README.md`, `DELIVERY_STATUS.md`, `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`.

The canonical manuscript is unchanged from the owner baseline:

- baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256 recorded by the package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- size: 47,883 bytes, 790 lines.

The first current-master snapshot observed in this invocation was `dd12ba4cca03c6e18c228fbff8b176398d1a95bf`; after concurrent peer writes the current head observed was `9732c7f78a4fd7e008445591b66b2442947e7179`. I re-read the manuscript blob from current `master`; it is still exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`. The baseline source was not modified.

## Overall verdict

**PASS** for the mathematical 17-eigenvalue theorem as written. I found **no fatal gap and no false mathematical claim used in the proof**. The theorem covers arbitrary independent one-dimensional Lebesgue densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, arbitrary signature and remaining spectrum, with no moment, support, smoothness, connectedness or log-concavity assumption.

One presentation issue remains in the product-projection proof (lines 258–282): after factors with `b_i=0` are dropped, the entropy estimate should explicitly pass through

`sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`.

The displayed bound `p(y)<=e^{d/2}` is correct, so this is a **minor GAP in wording only**, not a theorem gap and not a constant change.

The two bibliography entries (lines 782–789) are **UNCHECKED as priority/attribution metadata in this run**. They are not proof dependencies because the specialized estimates used in the manuscript are reproved. No mathematical source line is left unchecked.

## End-to-end line ledger

| Source range | Object | Verdict | Check and impact |
|---|---|---|---|
| 1–46 | preamble, abstract, notation | PASS | Quantifiers match the theorem; no hidden regularity/support hypothesis and no continuity claim for the full theorem. |
| 47–61 | `thm:main`, `cor:33` | PASS | Exact hypothesis is `s_17(A)>=s`; scaling target `10^4 K^2/s`; 33 is monotonicity. |
| 62–90 | architecture, `eta,kappa`, pivot scheme | PASS | Normalization and counts `9=4*3-3`, `17=4*5-3` agree with later uses. |
| 91–120 | Fourier identities | PASS | Gaussian convolution is defined for arbitrary finite laws; `L^2` approximate identity proves Plancherel; `phi in L^1` plus weak convergence identifies the limiting continuous density. No moment assumption occurs. |
| 122–130 | power envelope | PASS | Envelope integral is `2ap/(p-1)` and gives the stated inversion constant. |
| 132–160 | Riesz/half moments | PASS | Gamma representation is nonnegative, so both Tonelli steps are valid with infinite values allowed; Gaussian inversion normalization gives `1/sqrt(2pi)`. |
| 161–181 | singular values/rank | PASS | Best-rank approximation formula proves both nonsymmetric perturbation statements used later. |
| 183–207 | principal Schur spectral count | PASS | Invertible case follows from inverse principal compression; singular `A+eps I` argument uses threshold `t-|eps|` and continuity correctly. |
| 209–217 | diagonal dominance | PASS | Standard maximal-coordinate proof, valid for nonsymmetric matrices. |
| 221–255 | geometric rank-one BL | PASS | Heat derivative sign/frame contraction, integration by parts, large-time Gaussian limit, Lebesgue-point/Fatou step and monotone truncation all close for rough inputs. |
| 258–282 | product projections | **GAP (wording only)** | Everywhere cap-one representatives are legitimate. After zero `b_i` factors are dropped insert `sum_{b_i>0}(1-b_i)<=d`. No random-coordinate rotation or independence shortcut is used. |
| 284–301 | scalar Fourier powers | PASS | `m=floor(p/2)>=p/4`, difference law cap one, Plancherel/inversion and scalar projection constant give the claimed `p^{-1/2}` bound. |
| 303–324 | cross-form decoupling | PASS | Cauchy–Schwarz occurs before absolute values; copied physical coordinates preserve product structure; all pre-estimate phases have modulus one, so Fubini needs no moments. |
| 326–373 | regularized determinant | PASS | Frame identity, scaling, graph exponents, scalar Fourier powers and `alpha=(2pi e)^2` cancellation give determinant exponent `-1/8`; zero rows are harmless. |
| 374–400 | crossing volumes/Fourier envelopes | PASS | Cauchy–Binet expansion is exact; order five is integrable, order three is used only with the Riesz weight. |
| 404–422 | scalar square profile / conditional profile | PASS | Monotone branch change of variables is valid for measurable density versions. The conditional statement is correctly interpreted as domination against nonnegative tests, then averaged by Tonelli; no exceptional-slice selection is needed. |
| 423–434 | definite pair | PASS | Completion/rotation is only inside a deterministic integral; Jacobian and `pi/sqrt(det)` factor are correct. |
| 437–482 | hyperbolic pair | PASS | Hyperbolic Jacobian, positive/negative tails and original-coordinate one-dimensional changes of variables are sound. The critical level is handled in test-function form, so conditioning-dependent null levels cause no problem. |
| 485–525 | quarter-power concentration | PASS | Random-sign cutting exposes a literal cross block of norm at least `L/4`; determinant decay plus Gaussian smoothing gives the quarter exponent; layer cake excludes atoms and controls logarithms. |
| 528–544 | pivot/volume definitions, small entries | PASS | No-pivot determinant bound gives the stated strict physical-entry estimates. |
| 545–564 | sampled interpolation | PASS | Bordered determinant identity is exact. Singular seeds can have nonsingular extensions, hence the proof correctly uses `<=`; nonsymmetric interpolation is legitimate. |
| 566–580 | completion | PASS | `E` has zero diagonal, `D` vanishes on the seed, `R-P` is supported in rows `T` or columns `S`; hence global rank `<=3r` and restricted rank `<=r`. |
| 582–619 | spectral-to-volume | PASS | Small volume yields a small adjacent ratio. Perturbation plus global rank produces `r+1` large diagonal entries in `L`; restricted rank and strict diagonal dominance contradict. Exact slack remains positive. |
| 621–645 | random cut/no-pivot consequences | PASS | Ordered disjoint minors cross with probability `4^-k`; order 3 yields full half-potential `<200`, order 5 density `<2400`. |
| 646–674 | singular kernels | PASS | Nonnegative Tonelli/rearrangement is legitimate; constants are conservative; `d=0` is excluded where needed and atomlessness is supplied before use. |
| 676–714 | pivot truncated half-potential | PASS | Scalar, definite and indefinite pair branches are uniform over all conditioning-generated translations and arbitrary complementary laws. |
| 716–724 | nine-direction half-potential | PASS | Pivot and no-pivot alternatives exhaust. The tail outside unit distance costs at most one, so full half-potential `<=601`. |
| 726–749 | main theorem/scaling | PASS | No-pivot, scalar, definite-pair and indefinite-pair branches cover all cases. `Y=KX` and output scaling give exactly `K^2/s`. |
| 750–781 | threshold accounting/limitations | PASS | Dependencies match the proof; text explicitly does not claim multiplicity three or global continuity. |
| 782–789 | bibliography | UNCHECKED | Attribution only; not a proof dependency. |
| 790 | closure | PASS | No mathematical content. |

## Direct rough-law closure audit

The baseline proof does not require continuous densities or bounded support. An a.e. density cap can be replaced on a null set by an everywhere measurable cap-preserving representative. All product measures are then unchanged. Conditional pivot bounds are safest read as inequalities of measures against nonnegative Borel test functions; Tonelli averages them without choosing output density values on exceptional fibers.

The Gaussian regularization steps also require no tail moments: convolution of a finite measure with the Gaussian is always defined; the approximate-identity passage is in `L^2` when Plancherel is invoked and weak convergence when identifying a limiting measure.

I separately proved in this run a direct complex-pushforward closure lemma (saved in the sibling improvement artifact). It closes the only delicate rough-law interface in the current nine-direction grouped-Fourier compiler: a phase-weighted pushforward is dominated in total variation by its positive pushforward, and any uniform `L^2` bound on its mollifications passes to the original complex measure by weak `L^2` compactness. This requires no support, moment, continuity, or pointwise conditional-density hypothesis.

## Lowering the fixed multiplicity

The current repository contains a complete nine-direction replacement proof based on a marginal-free third crossing-volume density receiver and a marginal-free second crossing-volume half-potential receiver. Its normalized no-pivot branch uses only `s_9>=1`; scalar pivot leaves eight Schur directions and, in the no-pivot Schur child, only five are needed for the order-two half-potential route. Pair pivots are already paid by the baseline pair estimates. The current sharpened height is `<2582 K^2/s`.

I rechecked the new grouped-Fourier measure interface directly under the B14 lens and found no rough-law gap. Independent full-review/reconstruction artifacts for the nine-direction theorem are already present from workers distinct from its author, including account01/B16 and account03/B08, with further independent reconstructions in the tree. This satisfies the owner's requested *existence* of at least two separate complete reviews, while still not constituting formal verification or owner-level release certification.

Accordingly the **lowest complete fixed multiplicity currently supported by a full proof plus multiple independent end-to-end worker reviews is 9**. I do not claim multiplicity 8.

## Multiplicity-eight frontier checked in this run

I read the current `s_8` terminal reductions. In the unpaid no-pivot branch they force the terminal order-two interpolation state, quantitative rank-six saturation, a two-sided physical two-bank determinant collar, overlap-one third-minor currency, localized child spectral windows through one/two physical deletions, and nested original-coordinate star witnesses. These structural statements are internally consistent under the checked inequalities.

However no completed dependence-safe analytic receiver converts the aggregate collar into a **uniform linear interval bound**. Existing exact-zero two-anchor receivers pay a local projected cross Gram determinant and therefore cannot be applied merely from an aggregate collar lower bound; nonzero/indefinite anchor curvature introduces an additional dependence issue. Current full half-potential and `O(sqrt{|I|})` concentration information does not by itself imply an `L^infinity` bound; the sibling improvement artifact gives an explicit elementary counterexample to that functional implication.

Thus:

- baseline multiplicity 17: **PASS**;
- complete lowered multiplicity: **9** (current best universal theorem visible and reviewed);
- multiplicity 8: **OPEN** at the aggregate overlap-one/two-sided-collar endpoint;
- unrestricted multiplicity 3: **OPEN**.

## Package audit

`SOURCE_MANIFEST.json` and `checks.json` agree on the canonical SHA-256, byte count and line count. The current checker source tests the pinned SHA and reports PASS on 534 exact interpolation seeds, 18 exact volume-sampling cases, 9 strict-sampling cases, diagonal-dominance slack `297/2800`, 240 floating Schur-threshold diagnostics and 30 graph-weight diagnostics. These are supporting reproducibility checks only; they do not replace the symbolic proof.

Execution label: `WITHOUT_VERIFIED_BRAIN`. No baseline source, scheduler state, notification setting, identity, permissions, or public visibility was changed.
