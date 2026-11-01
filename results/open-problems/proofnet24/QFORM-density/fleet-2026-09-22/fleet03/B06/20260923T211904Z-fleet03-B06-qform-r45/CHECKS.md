# r45 checks

Status: `PASS` for the exact arithmetic and finite sanity calculations below. Numerical checks are not proof; the symbolic proof is in `REPORT.md`.

Equivalent same-run Python calculations produced:

```text
QFORM_B06_R45_CHECK_PASS
determinant_upper 0.989216125
case_A_constant 101.9956111227892
case_B_constant 35.77708763999663
partner_diagonal_constant 647.6596292030254
case_B_random_count 7451
minimum_observed_kappa 0.17212164355283785
```

Exact identities checked:

- `(109/200)^3 + 2(11/20)^3 + 3(109/200)(11/20)^2 = 7913729/8000000 < 1`.
- `[16 sqrt(30)(200/109)^(1/4)]^4 = 11796480000/109 < 102^4`; the fourth-power gap is `2030544/109`.
- `8*2^(1/4)*200^(1/4) < 36`.
- `102*256^(1/3) = 647.6596292030254... < 647.660`.
- `(61/1728)^(1/3)=0.3280414319251811...`, so `(1/4)` of this is `0.08201035798129527...`.

Finite sanity test: 200,000 random symmetric Gaussian `3 x 3` matrices were sampled; nonsingular matrices were scaled to determinant modulus one. Among the 7,451 samples with every diagonal modulus below `109/200`, none violated the theorem's forced `max offdiag>11/20` condition or the resulting `sigma_min(B)>1/200` condition for the maximum-offdiagonal physical pair. The smallest observed pair singular value was about `0.17212164`, far above the rigorous `1/200` threshold.
