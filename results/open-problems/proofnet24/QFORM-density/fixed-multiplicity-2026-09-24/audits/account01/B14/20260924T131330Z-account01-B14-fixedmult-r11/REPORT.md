# account01/B14 r11 — full fixed-multiplicity manuscript audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T131330Z-account01-B14-fixedmult-r11`  
Starting lens: rough input laws, measurable density versions, conditional kernels, Tonelli/Fubini, exceptional/null slices, Gaussian/approximate-identity limits, unbounded supports and translations.

## Source pin and scope

I read the complete 790-line `manuscript.tex` from current `master`, together with `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`.

The fetched manuscript has git blob

`183ccd294763214e6a707e8d4749ff9a8cf7006d`,

which is the blob recorded for baseline commit

`7c0d6e60946b19423e6400a12d34b473cf0591e2`.

The package records source SHA-256

`9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`,

47883 bytes and 790 lines. `checks.json` is pinned to the same SHA-256. I did not alter the baseline manuscript.

## Overall verdict

**PASS** for the mathematical 17-eigenvalue theorem as written. I found **no fatal gap and no false mathematical claim used by the proof**. The theorem really covers arbitrary independent one-dimensional Lebesgue densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, arbitrary signature and remaining spectrum, with no support, moment, smoothness, connectedness or log-concavity assumption.

There is one **minor presentation GAP** in the product-projection proof (lines 258–282): after dropping the `b_i=0` factors, the entropy sum should explicitly pass through

`sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`.

The displayed final bound `p(y)<=e^{d/2}` is correct; this is a missing harmless inequality, not a theorem gap.

The bibliographic attribution metadata in lines 782–789 is **UNCHECKED in this run** as prior-art metadata only. Neither citation is used as a proof dependency because the specialized estimates are reproved in the manuscript. I also did not independently reproduce the compiled-PDF visual inspection; this has no mathematical downstream effect.

## End-to-end line audit

| Source range | Object | Verdict | Reasoning / downstream impact |
|---|---|---|---|
| 1–46 | preamble, abstract, notation, architecture | PASS | Quantifiers agree with the theorem; the abstract does not add support/moment/continuity hypotheses. |
| 47–61 | `thm:main`, `cor:33` | PASS | Exact statement is `s_17(A)>=s`, density cap `10^4 K^2/s`; 33 is a monotone corollary. |
| 62–90 | normalization plan, pivot definition, Fourier conventions | PASS | `K=s=1` normalization is restored correctly at the end; all conditioning is on original coordinates. |
| 91–120 | `lem:fourier` | PASS | Gaussian convolution is legitimate for finite laws; Plancherel follows from the `L^2` approximate identity; if `phi in L^1`, uniform convergence of smoothed densities plus weak convergence identifies the limiting continuous density. No moments are used. |
| 122–130 | `lem:envelope` | PASS | The envelope is integrable exactly for `p>1`, and the constant is `ap/[pi(p-1)]`. |
| 132–160 | `lem:riesz` | PASS | The gamma representation is nonnegative, so Tonelli is valid even with infinite values. Gaussian inversion has an integrable Gaussian majorant. The `1/sqrt(2pi)` normalization and the `12 sqrt(u/(2pi))` consequence check. |
| 161–181 | norm conventions, `lem:rank` | PASS | Eckart–Young/minimax approximation formula gives both perturbation and rank-shift inequalities for nonsymmetric matrices; later use on `A-E` is valid. |
| 183–207 | `lem:schur` | PASS | For invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative interlacing gives the absolute-count inequality. The `A+eps I` singular approximation uses the moving threshold correctly and `S_eps -> S`. |
| 209–217 | diagonal dominance | PASS | Standard maximum-coordinate proof, symmetry not required. |
| 221–255 | geometric rank-one BL | PASS | Heat-flow derivative identity and frame contraction are correct. Compact-support Gaussian tails justify integration by parts; `t->infinity` is dominated; `t downarrow0` uses Lebesgue points and Fatou; monotone truncation covers arbitrary nonnegative integrable inputs. |
| 258–282 | product projections | **GAP (minor wording, repaired)** | Choosing everywhere-bounded measurable density representatives is valid. Deterministic orthogonal coordinates do not assert rotated independence. After omitting `b_i=0`, write `sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`; then the claimed `e^{d/2}` bound follows. No downstream constant changes. |
| 284–301 | scalar Fourier powers | PASS | `m=floor(p/2)>=p/4`; `|hat f|<=1`; the `2m` power is integrable by Plancherel. Fourier inversion gives the continuous density version at zero, and the scalar projection cap yields the displayed constant. |
| 303–324 | cross-form setup and decoupling | PASS | Cauchy–Schwarz is applied before absolute values; copied `J` coordinates retain product structure; all pre-estimate integrands have modulus at most one, so Fubini needs no moments or support bounds. |
| 326–373 | regularized crossing determinant | PASS | The `c_j,d_i` vectors form an exact geometric frame. The BL scaling factors are correct. `g_j<=1`, the scalar Fourier power at `p=2/d_i`, cancellation of `d_i`, and `alpha=(2pi e)^2` yield determinant exponent `-1/8`. Zero `d_i` rows are safely omitted. |
| 374–400 | crossing volumes and `cor:vol-fourier` | PASS | Cauchy–Binet expansion is exact; retaining one term gives exponent `k/4`. Constants for order 5 density and order 3 half-potential are correct. |
| 404–422 | scalar square profile and conditional profile | PASS | Monotone-branch change of variables is valid for arbitrary measurable density versions. The conditional inequality is best read as domination of measures against nonnegative test functions; Tonelli avoids choosing pointwise conditional density values on exceptional output slices. Translation of the vertex may be unbounded and costs nothing. |
| 423–434 | definite pair | PASS | Completion and orthogonal diagonalization occur only in a deterministic integral. The original joint density cap is transformed with the correct Jacobian. No post-rotation independence is used. |
| 437–482 | hyperbolic pair | PASS | Hyperbolic coordinates have Jacobian `1/(2 sqrt D)`. Tail control uses one original coordinate at a time, so rough product densities are sufficient. The negative tail repeats the argument with a coordinate witnessing the `w` vector. The critical level is null, and the final conditional use is through test-function/Tonelli domination, so outside-dependent critical values create no null-slice problem. |
| 485–525 | quarter-power concentration | PASS | Diagonal branch follows from the inverse-image length bound. Random-sign cutting exposes a literal cross block with norm at least `L/4`; determinant decay plus Gaussian smoothing yields the quarter-power bound. Layer cake proves the logarithmic potential with no atom or moment assumption. |
| 528–544 | pivot/volume definition and no-pivot entry bounds | PASS | Ordered disjoint minors and `V_0=1` are consistent. No pivot gives `|a_ij|<1/7` by the principal determinant bound. |
| 545–564 | `lem:sampling` | PASS | Bordered determinant identity is exact for nonsymmetric interpolation. Squaring removes ordering signs. Singular seeds can have nonsingular extensions, so the use of `<=`, not equality, is correct. |
| 566–580 | `lem:completion` | PASS | `E` is supported only on `LxL`, `D` is diagonal and vanishes on the seed. `R-P` is supported in rows `T` or columns `S`, giving global rank `<=3r`; on `LxL`, `R=P`, hence restricted rank `<=r`. Nonsymmetry is harmless because later spectral steps use singular values. |
| 582–619 | `prop:volume` | PASS | Small volume forces a small adjacent ratio. For `r=0`, operator norm is `<1`. For `1<=r<=4`, perturbation plus global rank forces `r+1` large diagonal entries in `L`; restricted rank `<=r` contradicts strict diagonal dominance. Constants `371/400` and `23/28` have positive slack. |
| 621–645 | random cut and no-pivot analytic consequences | PASS | Each ordered disjoint `k,k` minor crosses a fair cut with probability `4^-k`. Order 3 feeds the full half-potential; order 5 feeds `L^1` Fourier inversion. Arbitrary affine/same-bank terms are retained in the cross-form phases. |
| 646–674 | truncated half-potential and kernel integrals | PASS | Both kernels are nonnegative, so Tonelli/rearrangement is legitimate. The `J(d)` near/far split and logarithmic kernel constants are sufficient; `d=0` is correctly excluded and later ruled out almost surely. |
| 676–714 | `prop:pivot-H` | PASS | Scalar-pivot profile is integrated before evaluating exceptional values; the Schur remainder has a surviving spectral direction and no atom. Definite/indefinite pair bounds are uniform in all conditioning-generated affine translations. Averaging conditional domination is valid by Tonelli. |
| 716–724 | `prop:nine` | PASS | Pivot and no-pivot alternatives exhaust; truncation plus tail kernel `<=1` converts `H<=600` to full half-potential `<=601`. |
| 726–749 | main theorem proof and scaling | PASS | No-pivot uses order five. Scalar pivot leaves 16 Schur directions, enough for the nine-direction half-potential. Pair pivots are uniform in conditioning. Scaling `Y=KX`, `Q=(s/K^2)Qtilde` gives exactly `K^2/s`. Interval domination and essential density equivalence are standard. |
| 750–781 | threshold accounting, limitations, acknowledgment | PASS | Dependency table matches the proof; the text correctly denies a three-eigenvalue conclusion and global continuity. |
| 782–789 | bibliography / historical attribution | UNCHECKED | Bibliographic/prior-art verification was not repeated here; no theorem step imports either source. |
| 790 | document closure | PASS | No mathematical content. |

## Rough-law / measurability closure

The proof never needs a continuous input density or a density evaluated at a specially selected point. Given an a.e. cap `f_i<=1`, replace it on a null set by an everywhere measurable representative satisfying the cap. All joint input measures are then products of these representatives. Every conditioning step in the pivot branches is an ordinary fiber integral in original coordinates. The displayed conditional density formulas can be interpreted as inequalities of output measures against arbitrary nonnegative Borel test functions; Tonelli then averages them. This formulation is uniform under arbitrary conditioning-generated translations and does not require moments or bounded support.

Likewise, the Gaussian steps are stable for arbitrary probability measures: convolution with `g_eps` is always defined; approximate-identity convergence is in `L^2` where invoked and weak convergence where the underlying law may initially be singular. No uniform integrability or tail moment is silently assumed.

## Package audit

`SOURCE_MANIFEST.json` and `checks.json` agree on the pinned source SHA-256, 47883 bytes and 790 lines. The current checker reports PASS on 534 exact interpolation seeds, 18 exact volume-sampling cases, 9 strict sampling cases, diagonal-dominance slack `297/2800`, plus 240 numerical Schur-threshold and 30 graph-weight diagnostics. These computations are supporting diagnostics only. `AUDIT.md` contains historical counts from a different suite; the package explicitly labels that distinction, so I do not treat the differing counts as a contradiction.

## Threshold lowering observed during this run

A complete separate improvement in the same root now proves a **candidate nine-eigenvalue `L^infinity` theorem** with the same arbitrary-law/affine/sign scope. Its key new receivers turn third crossing volume into density and second crossing volume into a half-potential without a physical-row marginal assumption. I separately audited the rough-law interface of that compiler: phase-weighted pushforwards are dominated by their positive pushforward laws, hence admit measurable complex densities; the mollified `L^2` estimates pass to the unmollified pushforward by weak compactness/lower semicontinuity; translations do not affect the norms. No bounded support or moment assumption enters.

Two genuinely separate end-to-end PASS reconstructions of that nine-direction candidate are now present in the repository: account01/B16 and account03/B08. The author-side addendum records both and explicitly leaves release-baseline promotion to owner/B20 synthesis. I therefore treat **9 as the lowest currently complete and twice-reviewed fixed multiplicity visible in this source tree**, without rewriting the pinned 17 baseline myself.

Multiplicity 8 is not yet proved. A new structural reduction shows that, after the already-paid branches, the remaining no-pivot case carries a quantitative overlap-one/two-sided collar (`Omega_1` and `Xi_2`). What remains is an analytic product-preserving receiver for that collar when the common physical diagonal can be zero. This is a genuine unresolved proof obligation, not a support/moment/measurability issue.

## Final audit status

- Baseline 17 theorem: **PASS** in this independent B14 end-to-end audit.
- Fatal mathematical gaps: **none found**.
- Minor repair: product-projection summation wording at lines 258–282; no constant or theorem change.
- Mathematical source lines left UNCHECKED: **none**.
- Non-proof metadata left UNCHECKED: bibliography/prior-art attribution only.
- Lowest complete bounded-density multiplicity visible after concurrent work: **9**, with two separate full PASS reviews recorded; promotion of the pinned release baseline is not performed here.
- Multiplicity 8: **OPEN**, isolated to the overlap-one/two-sided-collar receiver in the current reduction.
- Full multiplicity 3 conjecture: **OPEN**.
