# r38 deterministic checks

The symbolic proof is in `REPORT.md`; these are finite sanity checks only.

`check_r38.py` was run with NumPy using seed `12345`.

```text
max_relative_identity_error=3.0603373338757825e-15
c3=0.72674560546875
L0=0.044531278614163679
L0_sq=0.0019830347750122712
Z0=L0_sq/64=3.0984918359566738e-05
Dprime_paid_constant=145.01913768347774
cofactor_relative_distance=0.12405374154836966
cofactor_tail_energy_fraction=0.015389330792149698
cofactor_top1_energy_fraction=0.98461066920785034
D0=0.71250045782661886
core_relative_distance=0.24810748309673933
core_tail_energy_fraction=0.061557323168598792
core_top2_energy_fraction=0.93844267683140126
```

The first line tests, on 1,000 random block matrices with nonzero scalar anchor, the exact identity

`sum anchored_3x3_minor^2 = b^(-2) e_2((bD-cr^T)^T(bD-cr^T))`.

The maximum normalized discrepancy was `3.07e-15`. The remaining lines independently evaluate the exact constants used in Sections 1 and 5 of the report.
