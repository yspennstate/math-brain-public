# account03/B13 r38 deterministic checks

Executed the sibling `CHECK.py` logic in the current invocation.

```text
QFORM_B13_R38_SHARP_DPP_CHECK_PASS
random_frames_checked 8653
minimum_random_delta 0.3011242390432118
max_q2_formula_error 4.440892098500626e-16
sharp_delta_floor 0.1875
W_floor 0.08333333333333333
improved_mu_constant 3037500.0
nonrank1_mu_mean_constant 267.630809134903
R2_center_size 48
R2_star_mass_floor 0.010416666666666666
light_bank_area_floor 0.20412414523193154
light_transverse_row_marginal_cap 0.5
```

The finite random sample is only a sanity check. The `3/16` disjointness floor and all structural inequalities in `REPORT.md` are proved analytically. The equality example is the four-row Parseval frame with leverage `1/2` and coefficient-line angles `0, pi/4, pi/2, 3pi/4`, which attains `delta=3/16` exactly.