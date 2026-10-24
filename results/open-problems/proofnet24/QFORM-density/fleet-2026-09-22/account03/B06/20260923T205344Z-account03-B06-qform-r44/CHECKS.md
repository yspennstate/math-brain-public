# r44 checks

Executed the companion `check_r44.py` logic in the current run. Output:

```text
WMAX 0.3280414319251811
anchored_K_partner_lower 0.08201035798129527
arcsine_constant 16.47813715125694
r43_innovation_branch_bound 1054.6007776804443
partner_bound 110.48033984697105
anchored_minor_identity_max_normalized_error 1.2991563273241666e-14
rank_one_bridge_max_normalized_error 2.3197857840959186e-16
counterexample_spectrum 1.0 [1.0, -2.0, 0.0]
counterexample_spectrum 0.5 [1.0, -2.5, 0.0]
counterexample_spectrum 0.1 [1.0, -10.1, 0.0]
counterexample_spectrum 0.01 [1.0, -100.01, 0.0]
QFORM_B06_R44_CHECK_PASS
```

The random tests are sanity checks only. The proofs are the exact Hardy--Littlewood/arcsine estimates, completion identities, the explicit factorization of the indefinite obstruction, and the Schur/adjugate determinant identity in `REPORT.md`.
