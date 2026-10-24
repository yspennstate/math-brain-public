# ProofNet24 P12 — Readback correction for 2026-09-15 16:27:01 run

The immutable complete run report is:

`proofnet24/P12-smooth-iid/runs/2026-09-15/2026-09-15_16-27-01__run-report.md`

Introducing commit:

`d3e9069827d796ddf8d8280674ea1fc22f110d27`

Readback blob SHA:

`d3c2ae8a6c6a7e5a852ae6ca4503bdbd234bc2f6`

Readback found one serialization/display defect in Section 0: the sentence beginning “For a probability density…” contains a stray control character immediately before `mathbb F`.

The intended text is exactly:

> For a probability density \(f\) on \(\mathbb F\), where \(\mathbb F=\mathbb R\) or \(\mathbb C\simeq\mathbb R^2\), write \(f^{*q}\) for the \(q\)-fold additive convolution.

No formula, hypothesis, theorem, proof step, ledger status, peer-audit verdict, or next-attack statement is changed by this correction. The original report remains immutable.