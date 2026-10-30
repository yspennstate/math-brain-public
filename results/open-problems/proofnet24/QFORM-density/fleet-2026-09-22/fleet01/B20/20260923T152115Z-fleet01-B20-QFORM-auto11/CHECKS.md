# Arithmetic and deterministic-identity checks

Run `20260923T152115Z-fleet01-B20-QFORM-auto11`.

All checks below are self-checks, not independent audits.

- `3025/16384 = (55/128)^2 = 0.18463134765625`.
- `(63/64)*(3025/16384) = 190575/1048576 = 0.1817464828491211`.
- `delta = 726327/33554432 = 0.021646231412887573...`.
- `delta^2/4096 = 527550910929/4611686018427387904 = 1.1439436874518573e-7`.
- `(delta^2/4096)/12 = 175850303643/18446744073709551616 = 9.53286406209881e-9`.
- `delta^2/16 = 527550910929/18014398509481984 = 2.9284958398767547e-5`.
- In the R1 `s2>=1/8` branch, `s2<=s1/16` implies `s1>=2`, hence `(s1*s2)^2>=1/16`; row/column two-colouring retains at least one quarter of total squared 2x2-minor mass, so `P2>=1/64`; determinant expansion gives the opposite-matching energy product at least `1/256`.
- In the R1 `s2<1/8` branch, rank-two subtraction plus `s3(A)>=1` yields a same-side principal block operator norm `>7/8`; removing its physical diagonal of norm `<1/64` leaves zero-diagonal operator norm `>55/64`; random cutting gives Frobenius-square energy `>(55/128)^2`.
- D5 on the nested cut gives numerical bound `231.1370879955056... <231.138`.
- D' at `h=2/3` and `Z0=delta^2/4096` gives numerical bound `368.878154749956... <368.879`.
- If `T=sum_(r>=3)s_r^2<1/4096`, then `||N-N2||_F=sqrt(T)<1/64`; coordinate restriction cannot increase Frobenius norm.

STATUS: PASS for the stated arithmetic and elementary deterministic implications.
