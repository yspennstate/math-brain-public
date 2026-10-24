# B18 / A090 — independent review of the B10 half-tax certificates

**Verdict:** the B10/A047 source scripts are **formally defective as
published**, but the minimally repaired certificates **PASS** and establish
their exact two-bit scope. Full GU and full FEI remain open.

## Audited claim

For the two-bit point-defect/AND gate, with the first input revealed and
biases `p,q`, the frozen candidate is

\[
J_X\le M_X+\frac12\delta(p),\qquad
\delta(p)=p\log_2\frac{1-p}{p}\quad(0<p\le1/2).
\]

The combined B10 claim was strict validity for

\[
1/64\le p\le0.49,\qquad 0\le q\le1.
\]

Independent truth-table reconstruction recovers the four biased squared
Fourier masses and the displayed formulas for `M_X`, `J_X`, and the favorable
margin. A 450-case 90-digit check agrees to at most `1.3e-89`.

## First unsupported line

Both interval programs advertise 70-digit directed rounding, but
`h_point` evaluates

```text
l1 = log2_point(ONE - x)
```

before entering a directed local context. Python therefore performs
`ONE - x` in its default 28-digit Decimal context. The rounded complement is
then treated as exact and need not contain the true value. This invalidates
the original interval-proof claim as written; the affected lines are 70 of
the compact checker and 71 of the endpoint checker.

## Repair and result

The independent checker changes only that operation: it encloses `1-x` with
70-digit downward/upward rounding and propagates the interval through the
logarithm and product. The unchanged adaptive covers then pass:

- compact core: 7,571 boxes, 3,786 leaves, depth 20, minimum lower endpoint
  `1.7580671042893135e-6`;
- lower-q collar: 89 boxes, 45 leaves, minimum lower endpoint
  `9.30298714791335e-5`;
- upper-q collar: 77 boxes, 39 leaves, minimum lower endpoint
  `1.042616597722943e-4`;
- unresolved boxes: zero.

Thus the mathematical two-bit claim on `p in [1/64,0.49]`, all `q`, is
repaired and proved. Because this review materially repairs the proof, it is
not an independent acceptance of the repaired version; a fresh reviewer is
required.

## Exact GU implication and remaining gap

This result controls one local biased two-bit restriction payment. It does
**not** prove `G(f)<=a I(f)+b U(f)` for arbitrary Boolean `f`. A universal GU
derivation still needs:

1. the remaining `p` strips and rare-tail join;
2. a higher-arity analogue; and
3. a hierarchy/ownership theorem charging every `M+delta/2` term once while
   retaining normalization and terminal costs.

The first unpaid line is therefore the nonreusing all-arity transport, not a
numerical two-bit sign on the certified rectangle.

## Sources and execution

- Compact source SHA-256:
  `58427757012dea237864abf8affc93149a8f73bb6d1f330c6f8959264d1198b2`.
- Endpoint source SHA-256:
  `2cc1f9a9165e64d3297bbddd39e1fb66f916465d286b812f0f21f9f6455198c9`.
- Compact proof-note SHA-256:
  `be5f52cce746aac2ae7e38311db3f83caaa05f3234b150639ba0cf7580d504a9`.
- Endpoint proof-note SHA-256:
  `d2dbca76cdbd1ccd5aad11a9659ee1d386f762640bba60939e5c7d57f12f7b0d`.
- Original B09 report blob:
  `71b68e4decf9658a42fef6bb2668e19f25bd214a`, read from canonical commit
  `2432393841959b4f8b72d959b001d6aed4536a71`.
- Command: `python3 verify_a090_half_tax.py`.
- Randomness: none.
- Runtime model/effort metadata: `UNKNOWN` beyond the exposed Codex runtime.

No universal theorem, second independent review, or full-FEI solution is
claimed.

