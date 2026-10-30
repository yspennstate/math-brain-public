# fleet02/B02 independent fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Run: `fleet02-B02-20260924T130747Z-r11`.
Reviewer lens: scalar Fourier powers, convolution and projection constants; fleet02 counterexample emphasis; nevertheless the entire 790-line proof was reread end-to-end.

## Exact source pin

- Repository/branch: `yspennstate/math-open-problems` / `master`.
- Fresh master observed before delivery: `15ba818daa54db185ead943765816d1a600cc7ef`.
- The manuscript blob at that commit is unchanged from the baseline: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Owner/source-manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- This run read `README.md`, `SOURCE_MANIFEST.json`, all 790 manuscript lines, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`.

## Overall verdict

**PASS for the written 17-eigenvalue theorem, with one nonfatal wording GAP.** I found no false lemma or broken dependency in the source as pinned. The theorem remains exactly the fixed-multiplicity statement

`independent coordinate densities <= K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, `s_17(A)>=s>0` => `||p_Q||_infinity <= 10000 K^2/s`.

This review does **not** claim the unrestricted three-eigenvalue conjecture and does **not** lower 17. The order-four route remains analytically endpoint-critical under the manuscript's determinant exponent, so no threshold reduction is asserted without a replacement theorem.

## Complete source-line ledger

Every source line belongs to one of the following ranges. Every displayed identity and lemma invocation inside a PASS range was independently rederived from the stated hypotheses.

| Lines | Object | Status | Independent check and downstream impact |
|---|---|---|---|
| 1-46 | TeX metadata, abstract, setup | PASS | Abstract matches the actual theorem and proof architecture; no hidden assumption introduced. |
| 47-61 | `thm:main`, `cor:33` quantifiers | PASS | Scaling dimensions and affine terms are stated correctly; `s_17` is singular-value multiplicity, not signed inertia. |
| 62-87 | parameters and architecture | PASS | `eta=1/100`, `kappa=1/80^2`; counts `9=4*3-3`, `17=4*5-3` agree with Proposition `prop:volume`. |
| 88-120 | Fourier conventions and `lem:fourier` | PASS | With `hat f(t)=int e^{itx}f(x)dx`, Plancherel constant is `2*pi`; Gaussian inversion factors `1/(2*pi)` and `1/(2 sqrt(pi v))` are correct. Approximate-identity and weak-limit steps are valid for rough laws. |
| 122-130 | `lem:envelope` | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)`; inversion gives `ap/[pi(p-1)]`. |
| 132-160 | `lem:riesz` | PASS | Gamma representation and substitution give exactly `1/sqrt(2*pi)`; the `3/4` envelope yields weighted integral `12 sqrt(u)`. |
| 162-181 | singular-value perturbation/rank | PASS | Eckart-Young/min-max reasoning works for nonsymmetric auxiliaries. |
| 183-207 | `lem:schur` | PASS | Invertible case follows from `S^{-1}` as a principal compression of `A^{-1}`, separately for positive/negative thresholds; singular case is correctly recovered by `A+eps I`. |
| 209-217 | diagonal dominance | PASS | Standard maximal-coordinate proof; nonsymmetry causes no problem. |
| 219-255 | geometric rank-one BL | PASS | Heat-flow differential identity, frame contraction, `sum c_i=d`, large-time limit, small-time Fatou, and monotone truncation are all valid. |
| 258-282 | product projections | **GAP (wording only)** | After dropping factors with `b_i=0`, the proof writes `sum_i(1-b_i)=d`. For the surviving indices the exact quantity is `sum_{b_i>0}(1-b_i)=d-z<=d`, where `z=#{i:b_i=0}`. Replace the displayed equality at the final entropy step by the inequality. The claimed bound `exp(d/2)` remains valid, so no downstream theorem changes. |
| 284-301 | scalar Fourier powers and convolution | PASS | `g=f*tilde f<=1` is exact. For `m=floor(p/2)`, `m>=p/4`; `|fhat|^{2m}` is integrable because it is bounded by `|fhat|^2`; inversion at zero and the scalar projection bound yield the stated constant. |
| 303-324 | decoupling | PASS | Cauchy-Schwarz is applied in the original-coordinate law, the independent copy is on the `J` bank, and Jensen gives the fourth power. No post-rotation independence is used. |
| 326-373 | regularized determinant theorem | PASS | Recomputed frame weights, Jacobian, `theta=sum d_i=sum(1-c_j)`, BL norms, scalar-Fourier exponent `2/d_i`, cancellation with `alpha=(2*pi*e)^2`, and fourth-root exponent `-1/8`. |
| 375-400 | crossing volumes and Fourier envelopes | PASS | Cauchy-Binet coefficient is `Z_k`; retaining order `k` gives `|phi| <= (pi e Z_k^{-1/(2k)}/|t|)^{k/4}`. For `k=5` the density constant is exactly `5e`; for `k=3` the half-potential constant matches `lem:riesz`. |
| 401-414 | scalar square profile | PASS | Both inverse branches give the stated `1/sqrt(|a||z-v|)` envelope; the interval-preimage length bound is sharp in order. |
| 416-434 | definite pair | PASS | Polar/elliptic change of variables has Jacobian `1/(2 sqrt(det B))`; integrating `theta` gives `pi M/sqrt(|det B|)`. |
| 436-482 | hyperbolic pair | PASS | Hyperbolic coarea Jacobian is `1/(2 sqrt D)`; tail coordinate selection and one-dimensional mass rearrangement are valid; `Lambda>=2/sqrt D` gives the final logarithmic scale. |
| 484-525 | quarter-power concentration | PASS | Random sign split supplies `||M||>=L/4`; determinant theorem gives `|t|^{-1/4}`; Gaussian smoothing at `v=1/8` produces the displayed coefficient and the atom/log-potential conclusions. |
| 527-543 | pivot/volume definition and small-entry bound | PASS | Absence of a two-coordinate pivot gives `|a_ij|^2<eta^2+eta<2eta`, hence `|a_ij|<1/7`. |
| 545-564 | volume-sampled interpolation | PASS | Bordered determinant identity is exact; sorting signs disappear after squaring; singular seeds correctly create an inequality rather than equality; `P` interpolates rows `S` and columns `T`. |
| 566-580 | completion and rank bounds | PASS | `E` has zero diagonal; `D=0` on `S union T`; support of `R-P` is rows `T` or columns `S`; full rank `<=3r` and restricted rank `<=r` are both correct. |
| 582-619 | spectral-to-volume proposition | PASS | Telescoping ratio selection is complete including first vanishing volume. For `r>=1`, `epsilon<=(r+1)/80<=1/16`; `m=4k-3>=4r+1`; `r+1` large diagonal entries lie in `L`; exact diagonal-dominance slack is `297/2800>0`. |
| 621-645 | random cut/no-pivot consequences | PASS | Each ordered disjoint minor survives a fair cut with probability `4^{-k}`. `Z_k^{-1/(2k)}<=160`; constants `12 sqrt(80e)<200` and `800e<2400` are valid. |
| 647-674 | singular kernels | PASS | Near/far split gives `J(d)<=8+3 log_+(1/|d|)`; layer-cake overlap is maximized at coincident centers and yields the exact integral `8`. |
| 676-714 | pivot truncated half potentials | PASS | Scalar, definite and indefinite cases exhaust invertible one-/two-coordinate pivots; Schur-count hypotheses match each invocation; full versus truncated potentials are not conflated. |
| 716-724 | nine-eigenvalue half potential | PASS | Pivot/no-pivot split is exhaustive; tail outside distance one contributes at most one, giving `601`. |
| 726-749 | proof of main theorem | PASS | Scalar pivot leaves at least 16 large Schur eigenvalues; indefinite pair leaves at least 15. The normalization `Y=KX`, `tilde Q`, and density rescaling give exactly `K^2/s`. |
| 751-790 | threshold accounting, limitations, references | PASS | Endpoint discussion is accurate; no continuity claim is transferred to pivot branches. BCCT and Rudelson-Vershynin titles/authors/arXiv identifiers were independently matched to the cited records. |

No source line remains mathematically UNCHECKED in this pass. The source SHA-256 string was read from the manifest/checker outputs but not independently recomputed from raw connector bytes in this runtime; the Git blob identity was independently observed.

## B02 adversarial exact-law checks

These are mathematical checks, independent of the repository's finite suite.

1. **Convolution cap is sharp.** For `X~Unif[-1/2,1/2]`, the difference density is `g(x)=(1-|x|)_+`, so `||g||_infinity=1` exactly.
2. **Projection constant cannot be below `sqrt(2)` by this class.** For independent uniforms and `a=(1,1)/sqrt(2)`, `(X1+X2)/sqrt(2)` has triangular density peak `sqrt(2)`. The manuscript's `sqrt(e)` scalar projection constant is therefore valid with only factor `sqrt(e/2)` slack against this exact witness.
3. **Scalar Fourier exponent is sharp.** For the admissible cap-one Gaussian `f(x)=exp(-pi x^2)`, `fhat(t)=exp(-t^2/(4*pi))` and exactly `int |fhat|^p dt = 2*pi/sqrt(p)`. Thus the `p^{-1/2}` exponent cannot be improved under only `f<=1`.
4. **Uniform Fourier values.** For the cap-one uniform law, `int|fhat|^2=2*pi` and `int|fhat|^4=4*pi/3`, consistent with the manuscript's inequalities and normalizations.
5. **Square profile is sharp.** For `Y~Unif[-1/2,1/2]`, `Y^2` has density `z^{-1/2}` on `(0,1/4)`, attaining the scalar-square envelope coefficient one.
6. **Definite-pair constant `pi` is sharp.** For the uniform square and `q=x^2+y^2`, the density near zero is exactly `pi`.
7. **Hyperbolic logarithmic coefficient is sharp.** For independent uniforms and `q=x^2-y^2`, for `0<|z|<1/4`,
   `p_q(z)=log((1+sqrt(1-4|z|))/(1-sqrt(1-4|z|))) = -log|z|+o(1)`.
   Hence the coefficient one in front of the logarithm in `lem:hyperbola` cannot be reduced below one in general.
8. **Rank-one bilinear Gaussian normalization.** For independent cap-one Gaussians and `Z=2mXY`, `phi_Z(t)=(1+m^2 t^2/pi^2)^(-1/2)`, confirming the manuscript's factor `2` in the cross term and its Fourier convention.

## Reproducibility package

The supplementary-file gap recorded in my previous run is now resolved: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are present. I independently reran the algebra/diagnostic logic of `verify.py` in this invocation and reproduced its recorded counts exactly:

- 534 exact interpolation seeds;
- 18 volume-sampling cases;
- 9 strict sampling cases;
- diagonal-dominance slack `297/2800`;
- 240 floating Schur-threshold cases;
- 30 graph-weight cases.

This is a reproducibility check, not a proof certificate.

## Threshold-reduction verdict

No lower multiplicity is claimed. Under the current determinant theorem, an order-`k` crossing volume gives tail power `|t|^{-k/4}`. Thus order four is exactly `|t|^{-1}`, whose unweighted integral diverges logarithmically. The cap-one Gaussian identity above shows that the scalar Fourier `p^{-1/2}` exponent itself is genuinely sharp. Therefore tightening only scalar-Fourier, convolution, or projection **constants** cannot convert the present order-four/13-direction route into an `L^1` argument. A valid `<17` theorem still requires at least one genuinely new ingredient: an order-four endpoint receiver, a stronger determinant exponent/decoupling mechanism, or a structural interpolation count better than `4k-3`, with all dependencies closed.

## Next obligation

Preserve the 17-eigenvalue baseline. The smallest concrete repair is the product-projection wording correction above. For threshold improvement, attack the order-four endpoint or the structural rank count; do not advertise a lower multiplicity from constant tuning alone. Release/independent-validation status remains governed by the separate two-complete-review gate.
