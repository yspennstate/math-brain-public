# PROB20-16 correction addendum — 2026-09-16T03-04-00Z

This append-only addendum corrects one arithmetic typo in the ninth-coordinate run report and its first checker/output artifacts. No theorem statement, C082 membership certificate, or correlation/field Bernstein calculation changes.

## Correction

The main report `runs/2026-09-16/2026-09-16T02-40-48Z__report.md` correctly uses the inherited eight-coordinate complement margin
\[
I-K_8\succeq \frac{413}{3000}I
\]
and the ninth-direction perturbation norm
\[
\|yS_{\rm im}\|_{\rm op}\le 2\cdot\frac1{4500}=\frac1{2250}.
\]
The subtraction was simplified incorrectly there. The correct value is
\[
\boxed{
\frac{413}{3000}-\frac1{2250}
=\frac{2478-8}{18000}
=\frac{2470}{18000}
=\frac{247}{1800}.
}
\]
Thus the correct physical bounds are
\[
\boxed{K_9\succeq\frac{91}{1800}I,\qquad
I-K_9\succeq\frac{247}{1800}I.}
\]
Both remain strictly positive with large slack, so the restricted strong-concavity theorem is unaffected.

## Artifact status correction

The first checker artifact `artifacts/2026-09-16T02-40-48Z__c082_nine_parameter_check.py` contains the same mistaken expected-value assertion `mI==2471/18000`. Therefore that first checker should **not** be treated as an executable verified checker even though its symbolic formulas and all listed Bernstein values are otherwise the same. The first retained output likewise prints the mistaken complement margin.

A corrected append-only checker and corrected retained output are being written under new paths. The earlier files are preserved unchanged for provenance.

## Claim status

- Exact nine-coordinate low-degree Bernstein minima: unchanged.
- Exact coefficient-in-y correlation residuals: unchanged.
- C082 membership of the full nine-coordinate parallelotope: unchanged.
- Strong entropy-concavity/chord theorem on that parallelotope: unchanged.
- Correct complement spectral lower margin: `247/1800`, replacing `2471/18000`.

This correction was found during delivery self-review before the user-facing completion. No security/approval issue was involved.
