# account02/B15 independent audit — fixed multiplicity candidate

Run: 20260924T133137Z-account02-B15-fixed-multiplicity-r11

## Source pin and verdict

Audited mathematical baseline: `manuscript.tex` at source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines. I re-read the unchanged blob through master snapshot `dab87716858e08fcf071327812f6091525cb590b` together with README, SOURCE_MANIFEST, AUDIT, proof_map, verify.py, checks.json, and DELIVERY_STATUS.

**Mathematical verdict: PASS for the stated fixed-multiplicity theorem.** I found no fatal mathematical gap in the 17-direction proof. I found one non-fatal notation/presentation GAP in the main proof: `\|A/B\|` is used for the Schur complement without defining `A/B`; replacing it there by the already-defined Schur complement `S=D-C^TB^{-1}C` removes the ambiguity. This does not affect the argument. This report is one independent audit, not formal verification and not a claim that unrestricted three-eigenvalue QFORM is solved.

No lower multiplicity is certified here. In particular, I do not replace 17 by 13: the present no-pivot Fourier chain at order four gives only the borderline envelope `|phi(t)| \lesssim |t|^{-1}`, and absolute Fourier inversion does not close at that exponent. A genuinely new replacement argument is required.

## B15 reconstruction: Gaussian inversion and Riesz half-potential

**PASS, manuscript 80–120 (Fourier identities).** With the manuscript convention `\hat f(t)=\int e^{itx}f(x)dx` and `g_epsilon(x)=(4 pi epsilon)^(-1/2) exp(-x^2/(4 epsilon))`, direct Gaussian integration gives `\hat g_epsilon(t)=exp(-epsilon t^2)`. For any probability law `mu` of `Z`, convolution with `g_epsilon` has density

`p_epsilon(x)=(2 pi)^(-1) \int exp(-itx-epsilon t^2) phi_Z(t) dt`.

If `phi_Z in L^1`, dominated convergence is uniform in `x`, so `p_epsilon` converges uniformly to the inversion formula and the limit is continuous. Weak convergence of `mu*g_epsilon` identifies that limit with the law. This continuity conclusion is used only where the characteristic function is actually integrable.

The more general identity was rebuilt from

`exp(-v x^2)=(2 sqrt(pi v))^(-1) \int exp(-t^2/(4v)) exp(-itx) dt`,

and after expectation and `t -> -t` gives exactly

`E exp(-v(Z-a)^2)=(2 sqrt(pi v))^(-1) \int exp(-t^2/(4v)) exp(-ita) phi_Z(t) dt`.

No density of `Z` is needed for this identity.

**PASS, manuscript 132–160 (negative half moments).** The gamma representation

`|z|^(-1/2)=Gamma(1/4)^(-1) \int_0^infty v^(-3/4) exp(-v z^2) dv`

combined with the Gaussian identity produces the inner integral

`\int_0^infty v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4) |t|^(-1/2)`.

The prefactors therefore reduce exactly to `1/sqrt(2 pi)`, proving

`E|Z-a|^(-1/2) <= (2 pi)^(-1/2) \int |t|^(-1/2)|phi_Z(t)| dt`.

For `|phi_Z(t)| <= min(1,(u/|t|)^(3/4))`, the weighted integral is exactly

`2\int_0^u t^(-1/2)dt + 2u^(3/4)\int_u^infty t^(-5/4)dt = 12 sqrt(u)`,

hence the stated `12 sqrt(u/(2 pi))`. Tonelli is applied only to nonnegative expressions; extended values are legitimate. No output continuity is needed.

## Full line-range audit

The labels below are mathematical status labels, not software-test statuses.

- **PASS, lines 1–46:** front matter, notation, singular-value convention, density/essential-supremum convention. No hidden regularity assumption.
- **PASS, lines 47–57 (`thm:main`):** quantifiers are unrestricted in dimension, signature, remaining spectrum, affine terms, and rough independent coordinate densities `<=K`; scaling target `10000 K^2/s` is dimensionally correct.
- **PASS, lines 59–78:** 33-direction corollary and proof architecture; the stated threshold bookkeeping `9=4*3-3`, `17=4*5-3` matches the later argument. No claim of the unrestricted 3-direction conjecture.
- **PASS, lines 80–120 (`lem:fourier`):** Plancherel, inversion, Gaussian regularization and constants rebuilt above. Continuity is asserted only under `phi in L^1`.
- **PASS, lines 122–130 (`lem:envelope`):** `\int min(1,(a/|t|)^p)dt=2ap/(p-1)` and inversion give `ap/[pi(p-1)]` for `p>1`.
- **PASS, lines 132–160 (`lem:riesz`):** Riesz half-potential normalization and power-envelope constant rebuilt above.
- **PASS, lines 162–181 (`lem:rank`):** Eckart–Young variational formula gives both Lipschitz perturbation and rank-shift singular-value inequality without symmetry.
- **PASS, lines 183–207 (`lem:schur`):** when invertible, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative eigenvalue interlacing separately imply the absolute-value count. The singular case is correctly recovered by a moving threshold `t-|epsilon|` and eigenvalue continuity.
- **PASS, lines 209–217 (`lem:dd`):** standard strict row diagonal dominance proof; nonsymmetry allowed.
- **PASS, lines 221–255 (`thm:bl`):** heat-flow proof has the correct sign: `partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`; the frame identity gives contraction, and the large-time Gaussian normalization is exact.
- **PASS, lines 258–282 (`lem:projection`):** no rotated-coordinate independence is used. The BL exponents are `b_i=|w_i|^2`; `f_i^(1/b_i)<=f_i` because `0<=f_i<=1`. Summing `-b log b<=1-b` yields at most `d/2` in the exponent (including zero-`b` rows on the harmless right side), so `e^(d/2)` is valid.
- **PASS, lines 284–301 (`lem:scalar-fourier`):** `m=floor(p/2)>=p/4`, `|hat f|^p<=|hat f|^(2m)`, and the density at zero of the signed sum is controlled by the one-dimensional projection theorem. The use of Fourier inversion at zero is valid because `|hat f|^(2m)` is integrable by Plancherel and `|hat f|<=1`.
- **PASS, lines 302–324 (`lem:decoupling`):** Cauchy–Schwarz/Jensen powers two and four are correct; the difference coordinates remain independent and have densities bounded by one. All Fubini steps are bounded by one and require no moments.
- **PASS, lines 326–373 (`thm:determinant`):** I rebuilt the graph-frame factors. With `H=alpha I+a^2 M^TM`, `alpha=(2 pi e)^2`, the coordinate weights `c_j` and row weights `d_i` form an exact geometric frame. The `d_i` powers cancel against the scalar Fourier bound; `prod c_j^(-c_j/2)<=exp(theta/2)` and the Fourier factors contribute `(2 pi sqrt(e))^theta`, so after the determinant factor the residual scalar is `(2 pi e/sqrt(alpha))^theta=1`. Taking the fourth root gives exponent `-1/8` and argument `t^2/(pi^2 e^2)` exactly.
- **PASS, lines 375–400 (`Z_k`, `cor:vol-fourier`):** Cauchy–Binet coefficients are correct. Retaining order `k` gives exponent `k/4`; for `k=5`, inversion gives `5e Z_5^(-1/10)`; for `k=3`, the rebuilt Riesz lemma gives `12 sqrt((e/2) Z_3^(-1/6))`.
- **PASS, lines 404–419 (`lem:square`, profile):** the two square branches give the exact inverse-square-root profile; the interval preimage length bound is `2 sqrt(2 rho/|a|)`. The conditional formula is measure domination through Tonelli, not an independence assertion.
- **PASS, lines 423–434 (`lem:definite`):** completing the square and deterministic orthogonal diagonalization is legal for a bounded joint density; the `(delta,theta)` Jacobian is `1/(2 sqrt(|det B|))`, yielding `pi M/sqrt(|det B|)`.
- **PASS, lines 437–482 (`lem:hyperbola`):** the hyperbolic `(delta,t)` Jacobian is `1/(2 sqrt(D))`. On each tail the chosen original coordinate is monotone with `|w_i'|>=|w_i|/3`; cap one plus total mass one gives tail `<=3 log 2`. The two cutoffs produce `(15/2)log2 + log_+(32/(delta Lambda))<6+...`, and `Lambda>=2/sqrt(D)` yields the stated `16 sqrt(D)/|z-v|` argument. The exceptional critical level is correctly handled in the test-function formulation.
- **PASS, lines 485–525 (`lem:quarter`):** the diagonal branch gives `4(rho/L)^(1/2)` and hence quarter power for `rho<=L`. The random-sign cut gives a cross block of norm at least `L/4`; the determinant theorem supplies the `|t|^(-1/4)` envelope. Gaussian smoothing with `v=1/8` has coefficient `2^(5/8) pi^(-1/4)e^(3/8)Gamma(3/8)=3.9952593615...<16`. Layer cake gives exactly `L0=4+4 log16`.
- **PASS, lines 528–543 (`def:pivot-volume`, small-entry estimate):** ordered disjoint minors are consistently defined; no pivot implies `|a_ij|^2<eta^2+eta`, hence `|a_ij|<1/7` for the chosen `eta=1/100`.
- **PASS, lines 545–564 (`lem:sampling`):** the bordered determinant identity is correct even for nonsymmetric `P`; squared determinants remove sorting signs. Each order-`r+1` disjoint pair is counted at most `(r+1)^2`; singular seeds can have nonsingular extensions, so the manuscript correctly uses an inequality rather than equality.
- **PASS, lines 566–580 (`lem:completion`):** on `LxL`, `R=P`; globally `R-P` is supported in rows `T` or columns `S`, giving `rank R<=r+r+r=3r`, while `rank R[L,L]<=r`. `D` vanishes on the seed and `E` has zero diagonal.
- **PASS, lines 582–619 (`prop:volume`):** the telescoping-volume choice of `r` is valid including first-zero cases. After perturbation, `s_m(D+R)>=1-epsilon` and rank `<=3r` force at least `m-3r>=r+1` large diagonal entries of `D`, all in `L`. With `r<=4`, diagonal lower bound is `371/400`, row off-diagonal bound is `23/28`; exact slack is `297/2800>0`. This contradicts `rank R[L,L]<=r`.
- **PASS, lines 621–630 (`lem:cut`):** every ordered disjoint pair crosses a fair cut in the prescribed orientation with probability `4^(-k)`.
- **PASS, lines 632–645 (`cor:no-pivot`):** `Z_k^(-1/(2k))<=2 kappa^(-1/2)=160`; constants rebuild as `12 sqrt(80e)=176.959336...<200` and `800e=2174.625462...<2400`.
- **PASS, lines 650–674 (`lem:kernels`):** near-region scaling of `J(d)` is finite and `<8`; outside `|x|>2|d|`, the integrand is at most `sqrt(2)/|x|`, giving the logarithmic term. The log-kernel overlap is maximized at coincident interval centers and equals `2 int_0^1 x^(-1/2) log(1/x)dx=8`.
- **PASS, lines 676–714 (`prop:pivot-H`):** scalar pivot combines `J(R-a)` with the one-surviving-eigenvalue logarithmic potential; definite pair gives `4 pi/sqrt(D)`; indefinite pair gives `D^(-1/2)(32+4 log_+(16 sqrt(D)))`. The scalar optimization `sup D^(-1/2)log_+D=2/e` is exact. Rebuilt numerical bounds are `532.711<560`, `40pi<160`, and `432.376<444`, all below 600.
- **PASS, lines 716–724 (`prop:nine`):** pivot and no-pivot cases cover all matrices; truncated half-potential `<=600` plus the far kernel `<=1` gives full half-potential `<=601`.
- **PASS with one notation GAP, lines 726–749 (`thm:main` proof):** no-pivot branch is `<=2400`; scalar pivot leaves at least 16 large Schur directions and gives `10*601=6010`; definite pair is `<40`; indefinite pair leaves at least 15 directions and uses only one surviving direction for the logarithmic potential. The last branch actually rebuilds to `238.998<251`. General scaling `Y=KX`, `Q=(s/K^2)\widetilde Q` gives exactly `10000 K^2/s`. **GAP:** the symbol `A/B` in the indefinite-pair paragraph is not defined; the intended object is plainly the Schur complement from Lemma `lem:schur`. Repair: replace `\|A/B\|>=1` by `\|S\|>=1`, where `S=D-C^TB^{-1}C`.
- **PASS, lines 751–790:** threshold-accounting table and limitations accurately state what has and has not been proved. The final regularity remark correctly distinguishes the no-pivot continuous-density branch from pivot branches established only by measure domination/essential bounds.

## Rough-law / continuity audit

**PASS.** The proof does not mollify rough input laws in a way that could smuggle continuity into the result. Every input density is used directly as an `L^1 cap L^infinity` function. BL is proved for general nonnegative integrable factors by monotone approximation; projection bounds are direct; decoupling uses bounded characteristic-function integrands; scalar and pair changes of variables are explicitly formulated as domination against nonnegative test functions and Tonelli. In the no-pivot branch the characteristic function is genuinely `L^1` because the order-five exponent is `5/4>1`; only there does Lemma `lem:fourier` furnish a continuous version. The scalar/pair pivot branches claim only existence of an essentially bounded density after averaging their domination inequalities. This scope is correct.

If one nevertheless mollifies original-coordinate input factors, product `L^1` convergence implies total-variation convergence of the joint laws, and deterministic quadratic pushforward contracts total variation. A uniform interval estimate therefore passes to the limit and gives an `L^infinity` density, but **not continuity**. Continuity would require an additional uniform Fourier-integrability or equivalent regularity argument. The manuscript does not make that overclaim.

## Counterexample / method-obstruction stress test

A lower-threshold attempt cannot simply replace the order-five no-pivot step by order four and invoke the same inversion lemma. At `k=4`, Corollary `cor:vol-fourier` gives only `|phi(t)| <= min(1,C/|t|)`, whose absolute integral diverges logarithmically. This is a real analytic barrier, not a technicality: if `G,H` are independent standard Gaussians (their one-dimensional densities are below one) and `Z=GH`, then

`phi_Z(t)=(1+t^2)^(-1/2) ~ |t|^(-1)`,

while the density of `Z` has a logarithmic singularity at zero (`K_0(|z|)/pi`). Equivalently, `2GH` is a two-direction indefinite quadratic form after a 45-degree deterministic spectral rotation. Thus a `1/|t|` envelope alone cannot imply bounded density. This does **not** disprove a 13-direction theorem; it rules out the naive same-proof replacement `k=5 -> k=4` through absolute inversion.

## Package/checker audit

**PASS with scope limitation.** `verify.py` independently recomputes the pinned manuscript SHA-256 before running. Its exact tests cover interpolation/rank/support/bordered-minor identities and volume sampling; floating tests cover Schur spectral counts and graph weights. `checks.json` records 534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur-threshold cases, 30 graph-weight cases, and exact diagonal-dominance slack `297/2800`. These counts differ from historical counts in the author self-audit, but SOURCE_MANIFEST and DELIVERY_STATUS explicitly disclose that this is a new suite and not a reproduction of the old suite. No finite test is treated as a proof certificate.

## Impact and next obligation

The pinned 17-direction candidate survives this B15 end-to-end audit. The only defect found is an editorial notation ambiguity in the final indefinite-pair paragraph. The next mathematical obligation for lowering multiplicity is not regularity or rough-law passage; it is a complete replacement for the order-five no-pivot density step (or a stronger interpolation/rank theorem) with explicit constants and with the same unrestricted hypotheses. Until such a proof exists, 17 should not be lowered and the unrestricted three-eigenvalue conjecture remains open.
