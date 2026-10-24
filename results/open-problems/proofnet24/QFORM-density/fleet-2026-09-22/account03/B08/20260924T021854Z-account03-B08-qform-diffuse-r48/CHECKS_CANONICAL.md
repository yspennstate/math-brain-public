# r48 canonical deterministic-check note

`CHECKS.py` and `CHECKS.txt` are the canonical regression record for this bundle. They use seed `480021854` and record 1000 parameter tests plus 2000 physical-map tests. Their observed maxima are

- `|w^T K w|`: `3.45521994228416400e-14`;
- `|det R_c|`: `7.96585781778199400e-15`;
- absolute error in `|lambda| |g_k|^2 = |d det R|`: `7.46069872548105200e-14`;
- relative error in the physical currency identity: `1.77931199023141600e-14`.

The checker ends `QFORM_B08_R48_TANGENT_SHEAR_CHECK_PASS` and evaluates the theorem constants as

`3*4^(2/3)=7.559526299369239`,

`3*4^(2/3)*(3/2)^(1/3)=8.653497421844450`.

The numerical paragraph in the initially committed `REPORT.md` was based on an earlier equivalent seeded scratch run and listed 1999 physical-map tests with slightly different floating residual maxima. That paragraph is superseded **only for regression-count/numerical-reporting purposes** by `CHECKS.py`/`CHECKS.txt`; no mathematical statement, proof, constant, scope, or conclusion changes.
