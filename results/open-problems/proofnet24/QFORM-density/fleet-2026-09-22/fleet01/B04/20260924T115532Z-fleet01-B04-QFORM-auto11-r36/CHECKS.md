# r36 deterministic checks

Checker source: `check_r36.py` in this immutable run directory. No installation was performed.

Observed exact-output marker:

`QFORM_B04_R36_REBALANCED_BASIS_CHECK_PASS`

Exact symbolic checks passed:

- `A=R Lambda R^T` equals
  `[[128,-32,-32,16,-32,-32],[-32,2,-4,-4,2,-4],[-32,-4,2,-4,-4,2],[16,-4,-4,2,-4,-4],[-32,2,-4,-4,2,-4],[-32,-4,2,-4,-4,2]]`.
- Every one of the 36 physical matrix entries is nonzero.
- `det Lambda=-216`; `spec(Lambda)={6,6,-6}`.
- `rank(A)=3` and `spec(A)={156,12,-30,0,0,0}` exactly.
- `R^T R=diag(65,2,2)`.
- Canonical leverage vector is exactly
  `(64/65,1/2,1/2,1/65,1/2,1/2)`, so the canonical half-leverage gate fails at row 1.
- Exactly eight physical 3-row bases are nonzero. Their squared determinants are
  `(64,64,64,64,1,1,1,1)`.
- The uniform law on those eight bases contains every physical coordinate in exactly four bases, hence every marginal is exactly `1/2`.
- Its determinant-entropy currency is exactly `G_R=64`.
- For six half-marginals, `B(alpha)^(2/3)=2`.
- The theorem's stress-matrix bound simplifies exactly to
  `3*2*(64*216)^(-1/3)=1/4`.
- For the designated fleet02/B04 r22 source matrix, the partner inequality evaluates to
  `3*2^(4/3)*158720^(-1/6)=1.02735996979354696...`.

These checks verify finite algebra and constants only; they do not substitute for review of the analytic Brascamp--Lieb/Hausdorff--Young proof or prove the unrestricted QFORM conjecture.
