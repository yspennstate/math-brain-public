# PROB20-16 correction addendum — 2026-09-16T10-55-00Z

This is an append-only correction to
`runs/2026-09-16/2026-09-16T10-40-15Z__report.md`
(write commit `a2be61e28d2f9c3c4854d1005662a5618defc17c`, readback blob `9f00a6e422306c6b4bbc715c36da7ef0ee376c31`).
The original report is intentionally not overwritten.

## Corrected arithmetic in Section 4

The theorem, the exact kernel, all atom masses, the four exact logarithmic ratios, the conclusion that the full nine-direction Hessian is strictly negative, and the fact that the point lies outside C082 are unchanged.

The single error is that the final displayed rational value after
\[
(R_\tau-1)+\frac32(R_1-1)
\]
was accidentally copied from an earlier trial kernel. For the actual kernel (4.1), the correct exact value is
\[
\boxed{
(R_\tau-1)+\frac32(R_1-1)
=
\frac{5899858600262616080834697382271130213560000}
{7251745597883276971202201884947975989666109}
<1.
}
\]
Numerically this is approximately
\[
0.8135777132039401.
\]
The exact positive slack is
\[
\boxed{
1-\left[(R_\tau-1)+\frac32(R_1-1)\right]
=
\frac{1351886997620660890367504502676845776106109}
{7251745597883276971202201884947975989666109}>0.
}
\]

The corrected exact checker for this run evaluates this rational identity directly from the eight exact atom masses and asserts the strict inequality before any floating-point diagnostics are run.

**Canonical reading:** cite the 10-40-15Z report together with this correction addendum. No other statement in that report is superseded.