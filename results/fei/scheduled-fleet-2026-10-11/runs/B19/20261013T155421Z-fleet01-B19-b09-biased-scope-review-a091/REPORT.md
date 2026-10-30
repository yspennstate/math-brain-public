# B19 / A091 independent review of B09 biased restriction uncertainty

## Verdict

The B09 report contains a correct product-biased block identity and a correct
Maassen--Uffink uncertainty bound at its stated normalized scope. Its repaired
two-bit interval certificate separately and rigorously refutes the tax-free
helper `J_A <= M_A`.

Two broader consequences require separation:

| B09 component | Verdict | Exact scope |
|---|---|---|
| `L_A=M_A+J_A` | **ACCEPTED** | finite physical block under product bias |
| `0<=J_A<=M_A+Delta_A` | **ACCEPTED** | B09 normalized product-biased transform |
| fixed `p=1/8,q=1/4` AND witness | **ACCEPTED separately** | `J_A-M_A>0.1195` bits, using repaired signed intervals |
| “an `O(p)` correction is impossible” | **ORIGINAL JUSTIFICATION REJECTED; CLAIM REPAIRED** | new Boolean AND family proves order `p log(1/p)` is necessary |
| exact disjoint tensor additivity | **ACCEPTED** | genuinely disjoint coordinate blocks |
| general Boolean-composition transfer | **NOT PROVED** | changing biases, overlaps, and reused variables remain unpaid |
| coefficient optimality of `Delta` | **NOT PROVED** | the new family proves order, not the sharp coefficient |

Because this review supplies the substantive rare-bias repair, B19 is a
contributor to that repaired claim and cannot independently accept its new
version. Route it to A085 or A090 for a fresh source-complete review. The
original main lemma itself is accepted independently.

Full FEI remains **OPEN**.

## Target and sources

- Primary packet: `A091` (composition referee).
- Reviewed object: B09 run
  `20261011T195500Z-fleet01-B09-biased-restriction-uncertainty`, report at
  canonical commit `adb671ffcda143fa68347806bb96e8c305621a7d`, blob
  `71b68e4decf9658a42fef6bb2668e19f25bd214a`.
- Certificate repair: `verification/B09_interval_repair_20261011/` at commit
  `a1ff93577685acd461b154b04e0c1aa0c65645c8`; report blob
  `2674d84116f7454c45b37fdd4991f78d65eaf31c`, checker blob
  `e0e834cca2e2705652c76bd38df98eb0bbdcab52`, output blob
  `3bfcf7ddae830e0766863b41e89ebb2ef55f6ba2`.
- B19 compact contract: current `assignments/B19.json`, blob
  `ee688080aba90acd2daed1b26e809e38285dcb85`.
- Execution protocol revision `2026-10-11-execution-v2`, current blob
  `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Owner focus control revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.

The B09 report's primary-source use of the Maassen--Uffink entropic
uncertainty relation and O'Donnell--Tan disjoint composition framework was
checked at the theorem level needed here. Neither source, as used by B09,
supplies a single-use correction for overlapping arbitrary hierarchies.

## Reconstruction of the main lemma

Let `Q` be the parent squared Fourier law and let `Q^z` be the corresponding
law after restricting block `A` to outcome `z`, with `z` distributed by the
physical product bias. The average child law has the parent residual marginal.
The entropy chain rule and concavity give the exact decomposition

`L_A=M_A+J_A`, with `M_A>=0` and `J_A>=0`.

On each normalized fiber, let `a` be the normalized coefficient vector and
`b=U_A a` its normalized restriction transform.  The largest entry magnitude
of `U_A` is

`prod_{i in A} sqrt(max(p_i,1-p_i))`.

Maassen--Uffink therefore gives

`H(|a|^2)+H(|b|^2) >= -sum_i log2(max(p_i,1-p_i))`.

Averaging fibers, preserving their exact weights, and substituting into the
ledger yields

`0 <= J_A <= M_A + Delta_A`,

where

`Delta_A=sum_{i in A}[h_2(p_i)+log2(max(p_i,1-p_i))]`.

The normalization, signs, and endpoint behavior are consistent. This is an
accepted bounded-block theorem, not yet a universal composition payment.

## New mathematical delta: a genuine Boolean lower-bound family

For `g(X,Y)=(-1)^(XY)` with independent biases `P(X=1)=p` and
`P(Y=1)=q`, the exact squared product-biased Fourier masses are

`((1-2pq)^2, 4q^2p(1-p), 4p^2q(1-q), 4p(1-p)q(1-q))`.

The complete derivation in `PROOF.md` proves, for every fixed
`0<q<1/2`,

`J_X-M_X = 4q(1-2q)p log2(1/p) + O_q(p)`.

This closes the precise logical gap in B09 Section 5(4): an actual Boolean
lower-bound family, not merely the asymptotic of an upper bound, now rules out
a correction bounded by `Cp` uniformly in `p`. At `q=1/4` the leading
coefficient is `1/2`; hence the order is sharp but the exact coefficient of
the B09 uncertainty tax is not established as sharp.

## Executed validation

Command:

`python3 CHECK_RARE_AND_FAMILY.py`

Arithmetic: exact Python `Fraction` arithmetic; logarithms enclosed by a
positive atanh series with an explicit rational tail bound; quotient intervals
use all four corners. Domain: `q=1/4`, `p=2^{-k}` for
`k in {4,8,16,32,64}`, plus the repaired source point `p=1/8`.

Results:

- source point: `0.119545016024424957 < J_X-M_X < 0.119545016024424958`;
- normalized by `p log2(1/p)`, the intervals progress from
  `0.388982...` at `k=4` to `0.495646...` at `k=64`;
- every displayed `k>=8` has rigorous normalized lower endpoint above `2/5`.

The full output is in `CHECK_RARE_AND_FAMILY.out`. This independent checker
also reconstructs the genuine Boolean spectrum rather than importing the B09
numeric values.

## Composition and physical-input accounting

Exact tensor additivity follows for products on genuinely disjoint coordinate
blocks because the squared Fourier law factors and both entropy and influence
add. This covers a sequence of independent block products with their actual
product biases.

It does not cover a general Boolean composition merely because a standard
composition identity is available. In a hierarchy, induced biases may change,
several nodes may refer to the same physical variable, and the uncertainty
credit may overlap. The reviewed source gives no injection assigning each tax
to a disjoint physical event and no cocycle showing telescopic cancellation.
Those are additional hypotheses, not consequences of disjoint additivity.

## Downstream status and next action

- Consumers may use the main product-biased uncertainty lemma at its exact
  normalized block scope.
- Consumers may use the repaired two-bit interval witness only as a finite
  helper refutation.
- The new AND family may be used conditionally until A085 or A090 independently
  reconstructs its asymptotic proof.
- Do not use the B09 report as evidence of arbitrary composition closure or a
  full-FEI theorem.

Next mathematical action: determine the sharp Boolean-realizable one-bit
correction as a function of `(p,q)`, then seek a gate-cocycle/owned-payment
lemma that remains valid when child biases change and physical variables are
reused. The first unpaid universal line is precisely that hierarchy-level
single-use payment.

