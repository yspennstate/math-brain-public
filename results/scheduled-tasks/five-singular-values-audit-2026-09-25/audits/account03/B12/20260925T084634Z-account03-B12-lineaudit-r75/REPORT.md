# account03/B12 r75 — P3 lines 241–406

Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`.

Pinned source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`,
`proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/short/short.pdf` and `short.tex`.
TeX blob: `c4f2a997cf336ee974e15409b5bccdd8cca039d8`.
PDF SHA-256: `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.

Pass: `P3-B12-rotated-chart-jacobian-adversarial`.

## Fresh controls

Startup fresh-main observation: `5705ee22d96c15b48d93208d78de8b7bd4436c6e`.
Immediately before publication, main had advanced through this run's coverage commits; the objective blob remained
`b167cb098b86d7f000e3fdd58efd17bcb2a58715` and the corrections blob remained
`5d46395f49355daa0c540e6d4518c9380decee10`.
Owner revision therefore remained `2026-09-25.1`; no scope change occurred.

## Coverage in this run

Every physical source line **241–406** was reconstructed and recorded, with exact PDF page anchors:
line 241 page 5; lines 243–300 page 6; lines 301–378 page 7; lines 379–406 page 8.
The two immutable ledgers are:

- `coverage_241_320_p3.jsonl`;
- `coverage_321_406_p3.jsonl`.

No new fatal mathematical defect was found.

## Section 4 reconstruction

The crossing-volume identities at lines 245–249 pass by the principal-minor identity and Cauchy–Binet.
The entropy lemma passes: the inclusion marginals satisfy `sum alpha_i=m`, Jensen for `log` gives the elementary-symmetric sum, and the multinomial expansion supplies the `m!` factor.

The hub construction also passes locally. Positive `Theta_l(H)` gives independent hub rows; orthogonal residualization produces
`Theta(H union T')=Theta(H) theta(T')`; the normalized residual volumes are a probability distribution and the diffuse hypothesis gives `alpha_i<=1/2`.
For `D=X_J-X'_J`, independence is across the original coordinate pairs and each difference density is bounded by one.

Step 1 is correct: Cauchy–Schwarz in `X_I`, expansion with an independent copy of `X_J`, and integration over the original independent `X_i` produce the characteristic-function product.

Step 2 is correct up to the already documented **C02 literal gap**. The projected variable `Y=M_HX_J` has the stated density cap. The complex measure `nu_x` is absolutely continuous with respect to the law of `Y`; its Radon–Nikodym derivative is a conditional expectation of a unit-modulus phase, so `|nu_x|<=p_Y`.
The scaled Plancherel factor is exactly `(pi/|t|)^k`.
However, between the pointwise conditional estimate and equation (4.5), line 319 says only “averaging over `X_{I'}`”. One must insert
[
|mathbb E F(X_{I'})|^2le mathbb E|F(X_{I'})|^2.
]
Thus line 321 and theorem-level statements depending on it remain literal-source GAP; the independently checked repair is valid.

The mollifier/complex-measure continuation passes: `kappa_epsilon` is a probability correlation kernel, convolution converges in `L^2`, Young's inequality gives the uniform bound needed for dominated convergence, and integrating the original independent `X_i` gives line 329.

The Holder step passes including zero marginals: indices with `alpha_i=0` may be dropped because `|psi_i|<=1`, while positive marginals have total weighted exponent one.
The one-set projection step passes because the hub rows and residual rows are orthogonal and full row rank on positive-weight sets.
The Fourier-power lemma applies with `p=1/alpha_i>=2`.
The entropy products at lines 359 and 363 have the correct signs and exponents.

The greedy proof of Theorem 4.1 passes locally: each promotion retains more than half the current extension volume, so
`Theta_l(H)>=2^{-k}E_l`; the `a_k` ratio simplifies to
`e^{-1/2}(omega(m-1)/omega(m))^{1/2}<=e^{-1/2}`, and the final constant is
`(sqrt(2) pi e)^l`.

## Corollary 4.4

The constant reductions independently pass:

- `l=3`: integrable `|t|^{-3/2}` decay yields a continuous density and
  `C3=3 sqrt(2) e (9/2)^{1/6}<15`;
- `l=2`: `beta_2=2^{3/4} pi e` gives
  `C2=8 e^{1/2}2^{-1/8}<12.2`;
- `l=1`: `E1=||M||_F^2` gives the displayed `|t|^{-1/2}` bound.

The literal corollary statements remain downstream GAP only because C02 is omitted upstream; their local derivations are correct after that repair.

## Lemma 5.1 regression

Lines 395–405 were rechecked while closing this range.
The inverse branches and interval-preimage estimate are correct.
The previously recorded one-point presentation gap at line 398 remains:
the displayed expression is undefined at `z=v` unless a density version is specified.
Since `P(Y=m)=0`, one may state the formula for `z!=v` / a.e. `z` and set `p_T(v)=0`.
No measure or constant changes.

## Independent comparison after derivation

After completing the mathematics above, I compared account02/B18's separately executed r18 handoff
(commit `6c7cbbf70c9efb66181bde31a86a45d753ebdc87`).
It independently reports C02 at lines 319–321 and the one-point line-398 issue, and no new theorem-bearing defect.
That comparison was not used as a premise for the reconstruction.

## Pass state

P3 coverage is now durable for lines 1–406, with the separate r73 chart/Jacobian coverage also covering 407–442, 473–510 and 603–615.
The first P3 source line not yet covered by this worker is **443**.
Still-unchecked P3 ranges are **443–472, 511–602, and 616–675**.
A favorable result is not a stop condition.

## PDF/formal status

A direct fetch of the private raw PDF through the screenshot-capable web path was attempted and failed, so a screenshot could not be obtained.
Pixel-level PDF/TeX render equivalence remains **UNCHECKED** in this run.
No new proof-assistant build is credited.

Brain status: **WITHOUT_VERIFIED_BRAIN**.
Configured model/effort telemetry not exposed: **UNKNOWN**.
No task, cadence, enabled state, email/push state, permissions, Drive/public-release setting or unrelated research target was changed.
