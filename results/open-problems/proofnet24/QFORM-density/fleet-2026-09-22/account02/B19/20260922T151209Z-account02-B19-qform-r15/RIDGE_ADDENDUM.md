# Late source application — ridge-window or physical pivot/cross export

A fresh control read after the main report exposed the new interactive theorem `QFORM-SPECTRAL-WINDOW-DENSITY-v1`, source `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, brain handoff `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/interactive/20260922T151048Z-ridge-window.md`. Its proof is supplied in stated scope but its independent review is still pending. The full conjecture remains open.

The theorem pays every target matrix for which the spectral projection `P` onto all eigenspaces with `|lambda|>=1/64` satisfies `max_i P_ii<=1/32`, with density bound `<64`.

This gives an immediate quantitative residual useful for the B19 structural splice.

## Lemma — `QFORM-RIDGE-OR-PHYSICAL-RESOURCE-v1`

Let `A` be real symmetric with at least three eigenvalues of modulus at least one, and let `P=1_{|A|>=1/64}`. Then exactly one of the following source-compatible alternatives holds:

1. `max_i P_ii<=1/32`; conditional on the supplied ridge-window theorem, the full form is paid with a continuous density bounded by `64`.
2. There is an original coordinate `i` with

   `|A_ii|>=1/512`

   or

   `||A_{i,-i}||_2>1/512`.

### Proof

If (1) fails, choose `i` with `P_ii>1/32`. Spectrally,

`A^2 >= (1/64)^2 P = P/4096`

as positive semidefinite matrices. Hence

`(A^2)_ii > 1/(32*4096)=1/131072`.

The exact row identity is

`(A^2)_ii = A_ii^2 + ||A_{i,-i}||_2^2`.

If `|A_ii|>=1/512`, the first physical resource occurs. Otherwise

`||A_{i,-i}||_2^2 > 1/131072 - 1/512^2`
`= 1/262144 = 1/512^2`,

which proves the second. QED.

## Consequence for the synthesis residual

After admitting the supplied ridge-window theorem in its stated scope, any hypothetical counterexample has a quantitative high-window-leverage coordinate and therefore a physical scalar pivot or off-diagonal cross-row export at scale `1/512`. The remaining synthesis problem is no longer an arbitrary low-stable-rank matrix: it is a high-leverage physical-resource problem. Existing scalar-plus-mixed-packet theorems pay the pivot branch once a product-compatible rank-two Schur resource is extracted; the one-effective aggregate theorem in the main report pays the clean rank-one-bank endpoint. The unpaid step is to convert the `1/512` resource into one of these paid packets despite same-bank contamination, or else into a ridge/diffuse branch.

This lemma does not claim that a single physical triple is uniformly good; that stronger mechanism is explicitly refuted by the live correction inbox. It also does not upgrade the pending independent-review status of the ridge-window theorem.
