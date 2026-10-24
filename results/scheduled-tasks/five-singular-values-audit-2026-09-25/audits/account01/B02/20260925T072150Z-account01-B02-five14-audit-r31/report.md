# account01/B02 r31 — pass-2 Section 4 conditioning/copy audit

Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`. Audit only.

Fresh owner controls and every required shared-package file were read before work. The pinned source remains `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`, `short.tex` blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`, PDF SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.

Own acknowledgement was successfully created and read back before substantive work.

## Changed-order scope

This second-pass run audits source lines **241–377**, emphasizing probabilistic architecture in reverse direction: final entropy/greedy constant, then one-set projection and Holder, then mollification/complex measures, finally initial copy decoupling. No previous B02 PASS was used as a premise.

## Main verdict

The Section 4 Fourier compiler is **PASS after the already identified local C02 omission at lines 319–321**. No new fatal defect was found.

### GAP — lines 319–321, conditional Jensen

The fixed-`X_{I'}=x` Cauchy–Schwarz/Plancherel estimate is correct. Passing to the unconditional characteristic function requires
[
|E_{X_{I'}}F(X_{I'})|^2\le E_{X_{I'}}|F(X_{I'})|^2.
]
The source says only “and averaging over `X_{I'}`.” This independently reproduces C02. The repair changes no constant or exponent.

## Complex-measure and mollifier audit

For
[
\nu_x(B)=E[e^{itR(x,X_J)}1_B(Y)],
]
conditional expectation with respect to `sigma(Y)` gives a measurable `h_x(Y)` with `|h_x|<=1`, hence
[
d\nu_x(y)=h_x(y)p_Y(y)dy,qquad |\nu_x(y)|\le p_Y(y).
]
Thus `nu_x in L2` and `||nu_x||_2^2<=||p_Y||_infty`.

Scaled Plancherel gives exactly `(pi/|t|)^k`. The autocorrelation mollifier is a probability density; expanding its L2 norm with the independent original copy gives the printed `kappa_epsilon(M_HD)` term. L2 approximate-identity convergence plus Young supplies convergence and DCT domination.

## Independence and conditioning scope

All Section 4 conditionings/copies are on original coordinate blocks. The transformed variables `Y=M_HX_J`, `M_HD`, and residual linear forms are handled via pushforward density bounds; the proof never treats rotated/projected coordinates as independent.

Therefore line 130 is freshly supported for **Section 4** in pass 2. It is not yet globally PASS because Sections 5 and 7 still need fresh pass-2 replay.

## Holder / one-set / entropy audit

Positive-weight subsets contain only positive marginals; zero-alpha factors are dropped using `|psi_i|<=1`; weighted Holder uses exponents `1/w_T'`. The one-set coefficient matrix has Gram determinant `Theta(H)theta(T')`. Applying Lemma 3.2 to `D` is legitimate because `D` has independent original-coordinate differences. Only the joint image-density cap is used.

With `p=1/alpha_i>=2`, Lemma 3.3 gives exactly `pi sqrt(2e alpha_i)/|t|` per residual row. The determinant and alpha weights combine with Lemma 4.2. Greedy promotion loses `2^(k/2)`, and `a_{k+1}/a_k<=e^(-1/2)`, so the diffuse case is worst. Theorem 4.1's constant is reproduced exactly.

## Render status

The package places this material on PDF pages 6–8, but exact formula-by-formula rendered-PDF comparison was not independently reopened in this runtime. Render equivalence remains `UNCHECKED_RENDER`.

## Next pass-2 target

Freshly replay Sections 5 and 7 conditioning branches to finish testing line 130's global assertion, then continue the second pass without relying on first-pass coverage.

Model: GPT-5.6 Sol. Effort/configuration telemetry: UNKNOWN / not exposed.
