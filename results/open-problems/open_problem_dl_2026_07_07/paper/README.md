# The law of robustness for two-layer neural networks with arbitrary weights

`main.tex` (`main.pdf`) is the paper; `supplement.tex` (`supplement.pdf`) is a companion note
developing the reduction of the log-free conjecture to one multiplier estimate. The paper
resolves the Bubeck--Li--Nagaraj law-of-robustness
conjecture (COLT 2021, Conjecture 1) for every piecewise-linear activation, ReLU in particular,
with no assumption on the magnitudes of the weights: for `n` i.i.d. points on the unit sphere in
`R^d` (or from `N(0, I_d/d)`), labels in `[-1,1]` of conditional noise level `sigma^2 > 0`,
every width-`m` two-layer network (arbitrary real weights, biases, skip) that fits the data
`eps` below the noise floor satisfies

    Lip(f) >= c * eps * sqrt( n / (m * log(C m n d / eps)) ),

with high probability, over the whole range of `m` -- the conjectured `sqrt(n/m)` up to one log.
Bubeck--Sellke (NeurIPS 2021 / J. ACM 2023) proved the law only for polynomially bounded
parameters and showed it fails at depth three without the bound, leaving the unbounded two-layer
case open; this paper closes it for piecewise-linear activations. Depth two is exactly critical.

## What is proved
- **Lower bound, arbitrary weights** (Thm, "main"): the bound above, for all PL activations,
  general noisy labels, and both sphere and Gaussian data.
- **Architecture-independent form** (Thm, "kink"): the bound depends only on the number of
  distinct kink hyperplanes `k(f)` of the realized function (`<= (K-1)m`), not the
  parameterization -- so it holds for convolutional, weight-tied, and low-rank single-hidden-layer
  nets, and for vector outputs. This is strictly sharper than the width form.
- **Matching upper bound at m ~ n** (Prop): an explicit width-`2n` two-layer ReLU spherical-cap
  interpolant fits exactly with `Lip = sqrt(7) = O(1)`, matching the lower bound up to the log:
  the law is sharp at one neuron per point.
- **General isoperimetric data**: the argument uses only isoperimetry, so the theorem holds for
  any c-isoperimetric measure with `E||x|| <= 1` (e.g. strongly log-concave).
- **Sample-size-free logarithm** (Thm, "sharplog"): in the sphere model, once `n >~ m d^2 log(md)`
  the logarithm depends only on the width and the dimension, not on `n`.
- **General Lipschitz activations, small width** (Thms, "genact"/"genact2"): projection-capacity
  floors for every Lipschitz activation; the conjectured rate holds at `m = 1` and `m = 2`
  outright and at `m = 3` for `d >= C log(nd)`, with a general-`m` curve reaching
  `m <= c log n / log log n`.
- **Single direction, every activation** (supplementary note): for every Lipschitz
  activation, arbitrarily many units along one direction cannot fit below
  `Lip = c eps min(sqrt n, d)` -- no width bound, no logarithm.

## The mechanism
Parameter-space covering is impossible for unbounded weights. Instead, a **rigidity lemma**:
after an exact canonical rewriting on the domain, every kink coefficient of a two-layer PL
function is `<= 2 * Lip` (ball) or `<= 2 Lip / sqrt(1-t^2)` (sphere, d>=3), because kinks on
distinct hyperplanes cannot cancel -- at a generic point of one kink hyperplane the function is
affine across the others, and a directional-derivative jump of an L-Lipschitz function is `<= 2L`.
The Lipschitz ball then has metric entropy `O(k d log(k d L / eps))` independently of the weights,
and the Bubeck--Sellke isoperimetry argument (reproved self-contained) finishes. The mechanism is
kink-specific: for smooth activations, discrete-derivative families are bounded-Lipschitz but need
unbounded parameters, so the general Lipschitz-activation case stays open. Rigidity genuinely
fails at `d=2` (an explicit even-cycle of four kink circles; ratio 4.99), so the sphere model is
stated for `d >= 3`.

## Still open
The clean rate without the log -- the paper states the single multiplier estimate (a
conjecture) to which the critical band of widths reduces, and the supplementary note proves
the reduction and all the structure surrounding it; the full curve `m << n` for two-layer
nets; general Lipschitz activations at large width.

## Numerics (all in `numerics/`, seed 20260707 unless noted)
- `check_rigidity.py` -- rigidity on random ReLU nets with `1e6` cancellation plants: 27/27.
- `check_sphere_cap.py` -- the sphere factor is exact (`1.000`).
- `check_d2_rigidity_fails.py` -- the d=2 even-cycle: ratio 4.99, so rigidity is false on `S^1`.
- `check_upper_bound.py` -- the matching width-`2n` construction: exact interpolation, `Lip=sqrt(7)`.
- `check_law_fast.py`, `check_law_empirical.py` -- trained nets have measured `Lip > sqrt(n/m)`.
- `validate_at_scale.py` (+ `.log`) -- rigidity to d=40/m=80 and the construction to n=2000, both pass.
- `check_static_rigidity.py` -- single-pole static rigidity: `max_s |B(s)| sqrt(1-s^2) / Lip` reaches
  `1.0000` over 2000 adversarial stacks and never exceeds it.
- `check_projection_floor.py` -- the width-1 projection floor grows as `sqrt(n)`, flat against the
  `sqrt(n)` growth that the sharp-threshold halfspace capacity would force.
- `check_sector_throttle.py` (seed 20260708) -- the deep/shallow/mid multiplicity throttles behind the
  band reduction of the supplementary note, each checked against its stated bound.

The scripts are also at https://github.com/yspennstate/law-of-robustness-two-layer.
