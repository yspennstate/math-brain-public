# Diagnostic checks for auto17

The analytic proofs in `REPORT.md` do not depend on numerical computation. Two arithmetic/algebra diagnostics were run locally for transcription safety.

1. For 5,000 seeded Gaussian rectangular matrices, with squared singular values `lambda_i`, the inequality

   `sum_{i>=2} lambda_i <= 2 e_2(lambda)/(sum_i lambda_i)`

   had maximum observed violation `0.0` at floating precision. The proof in the report is exact:

   `2e_2 - tau F^2 = sum_i lambda_i(lambda_1-lambda_i) >=0`.

2. Constants:

   `4 sqrt(2) = 5.656854249492381`,

   `17.0863179786 * 64^(1/8) = 28.735647076179667`.

These are diagnostics only, not evidence for the theorem beyond the exact proofs.