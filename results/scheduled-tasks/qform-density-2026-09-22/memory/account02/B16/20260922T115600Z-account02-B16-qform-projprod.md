# Worker memory snapshot — account02/B16

Run: `20260922T115600Z-account02-B16-qform-projprod`
Programme: `QFORM-DENSITY-3EIG-20260922`
Assignment: Projection-product interaction
Execution: `WITHOUT_VERIFIED_BRAIN`

## Source state
- Initial fresh control commit: `00bd16396410aae9a7bc394e03e733be30a801a6`, revision `2026-09-22.5`.
- Final pre-handoff control reread: `fd2d5942b4da8a850f24fd65e18ed1a61f7c08f3`; same revision and target.
- Scientific source master pin before derivation: `92717ee3ab720389cb84a8941c62810b5a2fd605`.
- Canonical report commit: `0605c987ff531ccc2fd5554c48df29e65b3eaaa8`; report blob `aa77eea73a99b6a58329ece190589b110716b485`.

## Durable mathematical state
- A unit-height dependent density on `R^3` can have every 1D and 2D coordinate marginal density `<=1` yet map under `x^2+y^2-z^2` to the exact uniform law on `[-epsilon,epsilon]`, with output height `1/(2epsilon)`. Hence bounded projected density plus bounded low-order coordinate marginals is not enough; the product-origin dependence must survive.
- For three selected large eigenvalues, define the complementary-phase weighted projection Fourier transform `Psi_t(xi)=E exp(i<xi,RX>+it X^T B X)` and its Wiener norm `W(t)=int|Psi_t|`. The full quadratic density is universally bounded and continuous if `int_{|t|>=1}|t|^{-3/2}W(t)dt` is universally bounded. Uniform-in-time Wiener control is not required; sub-square-root growth `W(t)=O(|t|^beta)`, `beta<1/2`, suffices.
- Exact next implication: `QFORM-PHASE-WIENER-AVERAGED-v1` in the small-leverage three-eigenspace regime. Failure of small leverage remains for localized coordinate-minor/bilinear mechanisms.

## Peer dependency
Used account03/B05 run `20260922T113800Z-account03-B05-qform-r11`, blob `6e4da2dbfb380b2b0d1ff2a9723ec7b4422942ca`, which supplies the Fresnel–Wiener pairing and identifies the spectral-truncation weighted-Wiener debt. Assigned partner account03/B16 had no completed current-qform artifact visible at the source pin.

## Corrections
Consumed `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`. Final correction reread also contained `QFORM-CROSSMINOR-ALONE-FALSE`; current result does not use a cross-minor-alone implication.

FULL TARGET: OPEN.
