# r41 finite checks

The algebra/checker corresponding to `check_r41.py` was executed during this run. Output values:

```text
E0 0.72674560546875
M0SQ 0.006742268800735474
S0 0.006600326299667359
ETA 0.18849151096435976 42643/226233
TAIL 1.806112063835225e-05 20/1107351
TAIL_REL 0.0027363981443254536 3355443200/1226226237201
V2 0.1857551128200343 4327778067649/23298298506819
V_AMP 0.430993170270753
C_E2 9.39913188784886
PAID_BOUND 345.99783591526193
MAX_ANCHOR_IDENTITY_RELERR 6.003978175527417e-16
MAX_WEDGE_IDENTITY_RELERR 1.095019405327635e-15
QFORM_B06_R41_RECIPROCAL_ANCHOR_CHECK_PASS
```

The 1,000 random matrix tests check only the exact algebraic identities

`Z_ia = b^2 ||C||_F^2 + ||m||^2 ||C e_a||_2^2`

and

`W_i = ||m||^2 ||C||_F^2`.

They are sanity checks, not evidence for the universal density theorem. The proof of both identities is symbolic in `REPORT.md`.
