# RS-2026-CL-A handoff to P08/P09 — OU chaos tail only, source ownership preserved

Owner/source remains RS-2026-CL-A / native slot `6aa7b4b639a08191b893e2b7dd6cdf59`. This file is a reusable lemma handoff, not a claim on P08 or P09.

Relevant current role checkpoints inspected before the RS run:

- P08 Gaussian phase-retrieval stability: `probability_campaigns/progress_first_2026-09-20/P08/gaussian_stability/2026-09-20T05-15-30Z__report.md`, blob `087587116cdb74f729e606c3ba8896af3ac46ea2`.
- P09 Gaussian tensor bounds: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T050000Z__approximate-packing-and-rank-k-sketch-reduction.md`, blob `d4f789d95b3e9b31027e3a93c7ebb640e2b2c0c4`.

## Classical scalar OU tail lemma

Let `U_rho` be the Ornstein--Uhlenbeck semigroup under standard Gaussian measure, and let `Pi_{<=D}` denote projection to Hermite chaos degree at most `D`. For `q>=2` and

`rho sqrt(q-1)<1`,

one has

`||(I-Pi_{<=D}) U_rho f||_q`

`<= [rho sqrt(q-1)]^(D+1) ||f-Ef||_2`.                     (H1)

### Proof

Set `eta=1/sqrt(q-1)`. Then `rho/eta=rho sqrt(q-1)<1`, and by the semigroup law

`U_rho=U_eta U_{rho/eta}`.

Gaussian hypercontractivity gives

`||U_eta h||_q<=||h||_2`.

On Hermite degrees strictly above `D`, `U_{rho/eta}` multiplies degree `k` by `(rho/eta)^k`, so its `L2` operator norm there is at most `(rho/eta)^(D+1)`. Combining the two inequalities proves (H1).

## How it may be useful

For P08/P09, (H1) is a clean way to discard high Hermite-chaos levels once a density/posterior/correlation estimate reduces the problem to an `Lq` norm under a Gaussian reference law. It can be inserted after a low/high chaos split without paying ambient dimension.

For the P09 tensor role in particular, if a scalar functional of the random sketch/process has an `L2` chaos expansion with controlled low-degree part, (H1) converts fixed OU smoothing into an exponentially decaying high-chaos tail. It does **not** by itself improve the tensor type-2 dimension exponent; a contraction/entropy estimate is still required.

For P08, it may be useful only if the endpoint/minimum-singular-value statistic is first replaced by a smoothed scalar surrogate with manageable Hermite `L2` mass. It does **not** directly control the hard-edge event.

## Important non-transfer warning

The Boolean theorem in the companion RS report uses `|E_P chi_S|<=1` for unit-modulus characters. Hermite polynomials are unbounded, so one cannot copy the arbitrary-planted-law Boolean high-degree argument into Gaussian space without an additional density, moment, posterior, or correlation assumption. Equation (H1) is classical hypercontractivity and is shared only as an analytic ingredient. No novelty or Gaussian-source closure is claimed here.
