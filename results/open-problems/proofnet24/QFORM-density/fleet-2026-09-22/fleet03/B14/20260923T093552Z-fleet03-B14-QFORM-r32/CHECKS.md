# Quantitative checks for fleet03/B14 r32

Run: `20260923T093552Z-fleet03-B14-QFORM-r32`

The partner scalar optimizer is

`H(theta)=8 sqrt(2) theta^(1/4)` for `theta<=1/64`,
`H(theta)=4+2 log(8 sqrt(theta))` for `theta>=1/64`.

Boundary check at `theta=1/64`:

- low branch: `8 sqrt(2) (1/64)^(1/4)=4`;
- log branch: `4+2log(8/8)=4`.

For `s>=1`,

`H(s)/s = [4+2log8+log s]/s`,

whose derivative is

`[1-(4+2log8+log s)]/s^2 <0`.

Thus the target-valid maximum is at `s=1`:

`4+2log8 = 8.158883083359672...`.

Two-sided equal-fragment diagnostic for `a=b=c=d=1`:

| N | summed cell majorant `H(N^2)` |
|---:|---:|
| 1 | 8.158883083359672 |
| 2 | 9.545177444479563 |
| 4 | 10.931471805599454 |
| 16 | 13.704060527839234 |
| 256 | 19.249237972318795 |

This table is only a check of the fragment-first upper-bound mechanism, not evidence that true output densities grow.

The one-sided subprobability mass cancellation is exact:

- fragment mass `m`;
- dominant shear coefficient `b` left unfragmented;
- `||p_W||_infinity <= m/|b|`;
- square small-ball coefficient `4m sqrt(|c|/(|d|b^2))`;
- layer-cake logarithmic integral equals at most `2m Psi(4sqrt(2)r sqrt(theta_b))`;
- every term in the physical-pair bound therefore carries the same factor `m`.

No numerical computation is used as proof in REPORT.md.
