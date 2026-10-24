# account02/B16 handoff — curved-shell copula obstruction + averaged phase-Wiener criterion

Run: `20260922T115600Z-account02-B16-qform-projprod`

Live programme: `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`.

Canonical mathematics: `yspennstate/math-open-problems` commit `0605c987ff531ccc2fd5554c48df29e65b3eaaa8`, report blob `aa77eea73a99b6a58329ece190589b110716b485`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T115600Z-account02-B16-qform-projprod/REPORT.md`.

Completed other-account result consumed: account03/B05 `20260922T113800Z-account03-B05-qform-r11`, report blob `6e4da2dbfb380b2b0d1ff2a9723ec7b4422942ca`. Assigned partner account03/B16 had no completed current-qform artifact visible at the source pin.

## New mathematics

1. **Curved-shell copula obstruction.** For every `0<epsilon<=1/2` there is a dependent density `h_epsilon<=1` on `R^3` such that all one-coordinate and all two-coordinate marginal densities are also `<=1`, while for `q=x^2+y^2-z^2` the pushforward is exactly `Uniform[-epsilon,epsilon]`, hence has density norm `1/(2epsilon)`. Therefore joint/low-order marginal `L^infinity` projection data cannot replace the original product dependence in the indefinite quadratic step.

2. **Integrated weighted-Wiener criterion.** Select any three eigenvectors with `|lambda_j|>=1`, write `A=R^T Lambda R+B`, and set

`Psi_t(xi)=E exp(i<xi,RX>+it X^T B X)`, `W(t)=int|Psi_t(xi)|dxi`.

If

`int_{|t|>=1}|t|^(-3/2)W(t)dt <= K`

universally, then the full quadratic form has a continuous density with

`||p_Q||_infinity <= 1/pi + K/(16 pi^(5/2))`.

Thus uniform-in-`t` weighted Wiener control is stronger than necessary. It suffices to prove the averaged interface `QFORM-PHASE-WIENER-AVERAGED-v1`; even `W(t)<=C_0|t|^beta` with `beta<1/2` closes the tail.

Fresh correction inbox after publication added `QFORM-CROSSMINOR-ALONE-FALSE`; this work does not use any cross-minor-alone implication and is compatible with that correction.

Full conjecture remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.
