# account02/B14 auto11 — full fixed-multiplicity audit, rough-law/Tonelli lens

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T150131Z-account02-B14-FIXMULT-auto11`  
Package snapshot read: `yspennstate/math-open-problems@7be102673d969ca0814383917079451c689b94c6`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256 from `SOURCE_MANIFEST.json`: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Source size: 47,883 bytes / 790 lines.

## Verdict

**PASS** for the literal baseline theorem in `manuscript.tex`: for independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, and arbitrary affine `b,c`, the law of `X^TAX+b^TX+c` has an essentially bounded density with the stated `10000 K^2/s` bound.

I reread the complete 790-line manuscript rather than accepting a previous worker verdict. I also read the full package `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and the package-mandated `DELIVERY_STATUS.md`. No fatal mathematical defect was found. The unrestricted three-eigenvalue conjecture is **not** proved here.

One B14 issue is **GAP-PRESENTATION, zero mathematical impact**: the product-projection proof says to choose versions of the input densities bounded everywhere, but does not explicitly require those representatives to be Borel. A bounded Borel representative exists after an a.e. modification, so this is repaired at zero cost. I spell out the repair below because it also removes all conditional exceptional-slice ambiguity.

The package finite checker was inspected line by line and `checks.json` records PASS for its advertised new suite. I did **not** independently rerun that finite suite or rebuild/render the PDF in this invocation; those two execution/visual claims are therefore **UNCHECKED here** and are not used as mathematical premises.

## End-to-end line audit

The status below refers to the pinned 790-line baseline source. `PASS` means I checked the statement and proof dependencies against the actual hypotheses. `GAP-PRESENTATION` means a zero-cost exposition/measurability repair is needed, not a theorem failure.

| Source lines / label | Status | Independent check and impact |
| --- | --- | --- |
| 1–46 front matter, definitions, conventions | PASS | Singular values, essential supremum, Lebesgue-density conventions are consistent with the theorem. No hidden support/moment/continuity hypothesis appears. |
| 47–57 `thm:main` | PASS | Quantifiers are exactly arbitrary independent real densities `<=K`, arbitrary symmetric `A`, arbitrary affine `b,c`; conclusion is essential density only. |
| 59–61 `cor:33` | PASS | Immediate from monotonicity `s_17>=s_33`. |
| 63–89 architecture/normalization | PASS | The claimed counts `9=4*3-3`, `17=4*5-3` match the later spectral-to-volume proposition. No post-rotation independence is asserted. |
| 91–120 `lem:fourier` | PASS | Gaussian regularization, Plancherel via monotone convergence, inversion via uniform convergence plus weak convergence, and Gaussian inversion all have correct constants and legal Fubini/dominated-convergence hypotheses. |
| 122–130 `lem:envelope` | PASS | Envelope integral is `2ap/(p-1)` and inversion gives `ap/[pi(p-1)]`. |
| 132–160 `lem:riesz` | PASS | Gamma representation is nonnegative, so both Tonelli steps are legal for arbitrary laws; the Fourier Gaussian majorant is integrable. The `12 sqrt(u)` weighted integral is correct. |
| 169–181 `lem:rank` | PASS | Both singular-value perturbation and rank-shift inequalities follow from best low-rank approximation and do not require symmetry. |
| 183–207 `lem:schur` | PASS | Invertible case via inverse principal compression is sound. In the singular case, applying the invertible result to `A+eps I` at threshold `t-|eps|` and passing ordered eigenvalue moduli to the limit really gives `N_S(t)>=N_A(t)-k`; there is no lost strictness at the endpoint. |
| 209–217 `lem:dd` | PASS | Standard max-coordinate proof works for nonsymmetric matrices. |
| 221–255 `thm:bl` | PASS | Heat-flow differentiation, frame contraction, integration by parts on compact positive-time intervals, large-time Gaussian asymptotic, a.e. Lebesgue-point limit, Fatou, and monotone truncation are all compatible with merely integrable rough factors. |
| 258–282 `lem:projection` | **GAP-PRESENTATION / repaired** | Mathematics is correct. The phrase “choose versions ... bounded by one everywhere” should say “bounded **Borel** representatives.” With that convention the marginal integral is Borel and all BL inputs are legal. See the repair lemma below. |
| 284–301 `lem:scalar-fourier` | PASS | Difference density is cap one; the even power is integrable by Plancherel/inversion and its value at zero is controlled by the actual product-projection theorem, not by rotated independence. |
| 310–324 `lem:decoupling` | PASS | Cauchy–Schwarz duplicates only the `J` bank; original-coordinate independence produces the Fourier product. All pre-estimate integrands have modulus at most one, so no moments are needed. Difference coordinates remain independent and cap one. |
| 326–373 `thm:determinant` | PASS | The regularized frame weights `c_j,d_i`, trace identity, BL scaling factors, scalar Fourier exponent `2/d_i`, entropy factor, `alpha=(2 pi e)^2` cancellation, and final fourth-root exponent `-1/8` are consistent. Zero weights are harmless. |
| 375–400 crossing volumes / `cor:vol-fourier` | PASS | Cauchy–Binet expansion is correct. Keeping the order-`k` term gives exponent `k/4`; `k=5` is integrable and `k=3` is exactly the weighted half-Riesz regime. Constants `5e` and `12 sqrt(e/2)` check. |
| 404–414 `lem:square` and 416–421 profile | PASS | Inverse-branch density and interval-preimage bound are correct. The conditional profile is explicitly a domination-of-measures statement, not a pointwise conditional-version claim. |
| 423–434 `lem:definite` | PASS | Deterministic translation/orthogonal diagonalization is only a change of variables in the integral; no rotated independence is used. Polar Jacobian gives `pi M/sqrt(|det B|)`. |
| 437–482 `lem:hyperbola` | PASS | Hyperbolic parametrization and Jacobian `1/(2 sqrt D)` are correct. The tail estimates use one **original** coordinate density, preserve arbitrary translations, and the critical level is handled by test-function measure domination rather than a condition-dependent choice of pointwise density values. |
| 485–525 `lem:quarter` | PASS | Diagonal branch, random sign cut, determinant receiver, Gaussian small-ball smoothing and layer cake are all valid for arbitrary rough product laws. The bound excludes atoms without any support assumption. |
| 528–535 `def:pivot-volume` and small-entry bound | PASS | No-pivot algebra gives `|a_ij|^2<eta+eta^2`; the convenient `<1/7` bound is safe. |
| 545–564 `lem:sampling` | PASS | Bordered determinant identity, ordered-pair counting, singular-seed inequality, nonsymmetric interpolation, rank and exact row/column interpolation were all checked. |
| 566–580 `lem:completion` | PASS | `D` vanishes on the seed, `E` has zero diagonal, `R-P` has support only in rows `T` or columns `S`, hence global rank `<=3r`; on `L x L`, `R=P`, so restricted rank `<=r`. |
| 582–619 `prop:volume` | PASS | Telescoping selection of `r`, `r=0` contradiction, singular-value transfer to `D`, count `m>=4r+1`, location of large diagonal entries in `L`, and strict diagonal-dominance contradiction are all sound with nonsymmetric `R`. |
| 621–630 `lem:cut` | PASS | Each ordered disjoint `k`-minor survives the fair cut with probability `4^-k`; no independence beyond the random cut is used. |
| 632–645 `cor:no-pivot` | PASS | `Z_k^{-1/(2k)}<=160` follows exactly; `k=3` yields the full half potential `<200`, while `k=5` yields density `<2400`. |
| 654–674 `lem:kernels` | PASS | Near/far split in `J(d)` and interval-overlap layer cake for the logarithmic kernel are valid; all singularities are locally integrable in the stated weighted forms. |
| 676–714 `prop:pivot-H` | PASS | Scalar, definite-pair and indefinite-pair branches meet their exact hypotheses after conditioning on original coordinates. The scalar displayed arithmetic actually gives `200+120 log 16`, stronger than the rounded `600`. |
| 716–724 `prop:nine` | PASS | Pivot branch uses only two surviving directions; no-pivot branch uses the full half-potential estimate. Adding the outer tail contributes at most one. |
| 726–749 proof of `thm:main` | PASS | No-pivot, scalar-pivot and pair-pivot cases exhaust the problem. Schur counts are sufficient in every branch. Scaling with `Y=KX` gives exactly `K^2/s`. |
| 751–790 accounting/limitations | PASS | Scope is accurately stated: no claim of `s_3`, no global continuity claim, and no spectral-remainder independence shortcut. |

There are no mathematically relevant portions of the baseline manuscript left **UNCHECKED** in this run. The only UNCHECKED items are the independent rerun of `verify.py` and the PDF visual/build receipt, neither of which is a proof dependency.

## B14 repair: bounded Borel representatives and parameter-uniform Tonelli

A clean convention closes every rough-density interface at once.

**Lemma (Borel representative + mixture domination).** If a probability law on `R` has a Lebesgue density `f` with `0<=f<=K` a.e., then it has a Borel representative `f_bar` equal to `f` a.e. and satisfying `0<=f_bar<=K` everywhere. Replacing `f` by `f_bar` does not change the law. For finitely many independent coordinates, the joint density may therefore be fixed once and for all as the Borel product of these representatives.

Now let `(Omega,nu)` be any positive environment measure and let `mu_y` be an output kernel. Suppose a jointly Borel `k(y,z)>=0` satisfies, for every nonnegative Borel test function `h`,

` int h(z) mu_y(dz) <= int h(z) k(y,z) dz `

for `nu`-a.e. `y`. Then Tonelli gives

` int h(z) [int mu_y(dz) nu(dy)] <= int h(z) [int k(y,z)nu(dy)] dz. `

Thus the mixture has density dominated by `K(z)=int k(y,z)nu(dy)` with no common exceptional set in `z` required.

This is precisely the legal form of the manuscript's scalar profile, definite-pair calculation and hyperbolic envelope. The inverse-branch and hyperbolic parametrizations are Borel after the bounded-Borel representative convention; the critical hyperbolic level may be assigned `+infinity` in the majorant without changing its Lebesgue integral. Consequently arbitrary translations, unbounded/fragmented supports and conditioning-generated affine coefficients incur no hidden regularity cost.

## Independent audit of the complete multiplicity-nine replacement

After securing the baseline, I independently reconstructed the current grouped physical-product Fourier replacement rather than accepting its previous PASS label. The replacement preserves the same rough-law/affine scope and proves

` s_9(A)>=s  ==>  ||p_Q||_infinity <= C_9 K^2/s, `

with the fully closed conservative constant

` C_9 = 2010+1200 log 16 = 5337.106466687737... <5338. `

The key rough-law point is that the complex pushforward used in the grouped compiler is genuinely `L^2`: full row rank of the literal `J` map gives the law of `M_J X_J` a bounded density by the baseline product-projection theorem; convolution with the independent remaining shift preserves a finite density cap; total-variation domination then gives the complex pushforward a bounded `L^1` density and hence an `L^2` density. The subsequent Gaussian Plancherel regularization duplicates only the `J` variables and avoids any disintegration onto a rough fiber.

The dependency map I checked is:

`bounded Borel representatives`
` -> Fourier/Plancherel/Riesz + geometric BL + product projection + scalar Fourier powers`
` -> Gaussian-regularized grouped compiler`
` -> {marginal-free E_3 density receiver, marginal-free E_2 full half-potential receiver}`

independently of

`sampling + completion + singular-value/rank bounds + diagonal dominance`
` -> spectral-to-volume + fair cut`.

Final branches:

1. no pivot + `s_9` -> `V_3>=kappa^3` -> physical `E_3` -> density `<2372`;
2. scalar pivot -> Schur has eight unit directions -> either pivot half-potential `<=201+120 log16`, or no-pivot `s_5` -> `V_2` -> `E_2` full half-potential `<153`; square profile gives the bottleneck `2010+1200 log16`;
3. definite pair -> `<32`;
4. indefinite pair -> `<251`.

Every promotion is a literal physical original-coordinate row and all same-bank quadratic terms remain in the arbitrary measurable phase. Hence this is a complete threshold reduction `17 -> 9`, not a Gaussian/exact-rank/leverage/bounded-support surrogate. I do not self-award owner release status from this review, and I make no `s_8` or unrestricted `s_3` claim.

## Current lower-threshold obstruction

Multiplicity eight remains open. The exact obstruction is no longer just “the rank count is one short.” In the terminal no-pivot `s_8` chamber with `V_3<kappa^3`, the sampled bad-ratio order is forced to `r=2`; the next artifact from this run records a stronger two-neighbor determinant amplification theorem. It does not itself close `s_8`, because the sampled residual-goodness is not known to transfer to either heavier neighbor.

A separate mechanism counterexample is also important: a robust two-anchor cross determinant alone cannot imply `L^infinity`. For independent cap-one uniforms `U_1,U_2,V_1,V_2`, take

`K=eps [[0,1],[1,0]],   C=I_2,   R=K^{-1}`

and

`Q=U^T K U + 2 U.V + V^T R V`.

Then `det(CC^T)=1`, but exact completion gives

`Q=2 eps (U_1+V_2/eps)(U_2+V_1/eps)`.

The two factors are independent and each has a positive flat density near zero, so the product density diverges logarithmically at zero. The full four-dimensional quadratic matrix has rank two, so this is not a fixed-multiplicity counterexample; it is a counterexample to closing the `s_8` endpoint from robust two-anchor cross density alone. A successful `s_8` proof must also spend the shared-anchor/Schur curvature forced by the eight-large-eigenvalue hypothesis, or obtain a structural exchange principle that transfers the residual-good seed.

## Package/support-file status

- `README.md`: PASS; accurately separates the baseline manuscript from review status.
- `SOURCE_MANIFEST.json`: PASS as a manifest; source blob/line/byte pins agree with the fetched baseline metadata.
- `AUDIT.md`: read in full; treated as historical self-audit only, not proof.
- `proof_map.csv`: PASS; ranges agree with the source sections read here.
- `verify.py`: PASS by code inspection for its stated finite diagnostics; it explicitly checks the pinned source hash before running.
- `checks.json`: records PASS for 534 exact interpolation seeds, 18 exact volume cases, 240 numerical Schur threshold cases and 30 numerical graph-weight cases. Independent rerun in this invocation: **UNCHECKED**.
- Compiled PDF build/visual inspection claimed by the manifest: **UNCHECKED** in this invocation and not used mathematically.

## Next obligation

For `9 -> 8`, prove one of the following without weakening the law/matrix hypotheses:

1. a volume-sampling exchange/charging lemma forcing at least one determinant-amplified neighboring order-two seed to retain the small residual needed by the `s_8` completion; or
2. a genuinely shared-anchor overlap receiver that consumes the surviving Schur/overlap curvature before a one-sided Cauchy--Schwarz/Plancherel step destroys it.

Do **not** replace this by a determinant-free two-anchor theorem: the explicit rank-two logarithmic counterexample above rules that out.
