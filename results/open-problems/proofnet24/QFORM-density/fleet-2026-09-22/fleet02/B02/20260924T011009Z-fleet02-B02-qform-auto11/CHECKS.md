# Deterministic checks for fleet02/B02 20260924T011009Z

These checks are corroborative only; the proofs are in `REPORT.md` and `PARTNER_R43_ADDENDUM.md`.

## Exact-target diffuse-triple construction

For `k in {1,2,4,16}`, construct `B_k` with `k` copies of each of `e1/sqrt(k),e2/sqrt(k),e3/sqrt(k)`, and `A_k=[[0,B_k],[B_k^T,0]]`.

Computed values:

| k | max abs entry of `B_k^T B_k-I3` | `E3(B_k)` | max physical triple `Delta_I^2` | nonzero spectrum of `A_k` |
|---:|---:|---:|---:|---|
| 1 | 0 | 1 | 1 | `-1,-1,-1,+1,+1,+1` |
| 2 | `2.22e-16` | `0.9999999999999996` | `0.12499999999999992` | `-1,-1,-1,+1,+1,+1` |
| 4 | 0 | 1 | `0.015625000000000007` | `-1,-1,-1,+1,+1,+1` |
| 16 | 0 | `0.9999999999999998` | `0.00024414062500000016` | `-1,-1,-1,+1,+1,+1` |

The observed maxima equal `k^(-3)` to floating-point accuracy, as proved algebraically.

## Constants

Using

`C3=3*2^(7/6)*exp(1/3)*(16/9)^(1/6)`

and

`C5=5e/sqrt(2)`,

the evaluated constants are:

- `C3 = 10.345083232147514`;
- `C5 = 9.61057757039779`;
- `((C5/C3)^10) = 0.4788009378679107`;
- newest-partner r43 sharp integrated front `C3/2^(1/3) = 8.210898002704772`;
- at `theta=1/4`, front on `S^(-1/6)` is `16.421796005409544`;
- after `S >= (4/3125)V1`, front on `V1^(-1/6)` is `49.83704970259085`;
- if `V1>1/4`, the resulting absolute coefficient is `62.790747984951246`.

Status: PASS; no discrepancy with the symbolic formulas used in the reports.
