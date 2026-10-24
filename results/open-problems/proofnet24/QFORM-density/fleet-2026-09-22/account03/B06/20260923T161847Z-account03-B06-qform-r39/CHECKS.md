# r39 finite checks

Checker source: `check_r39.py` in this immutable run directory.

Private same-formula execution result:

`QFORM_B06_R39_RIDGE_TAIL_CHECK_PASS`

Exact/numerical values checked:

- `c3 = 11907/16384 = 0.72674560546875`
- `x2_lb = 11907/1048576 = 0.011355400085449219`
- `kappa0 = 11907/12163 = 0.9789525610457946`
- `top2_trace_lb = 23814/12163 = 1.9579051220915893`
- `eta0 = 14211/48652 = 0.29209487790841077`
- `tail_energy_cap = 14211/141070336 = 0.00010073698272044947`
- `rank2_F_distance_cap = 0.010036781492114365`
- `low_trace_top2_physical_leverage_lb = 10115/48652 = 0.20790512209158923`
- `tail_to_x2_ratio_cap = 404224/45565443 = 0.008871284319566476`
- `q2_density_constant = 288*sqrt(e) = 474.83172596163695`
- `q1_density_constant = 288*sqrt(2e) = 671.5134666999718`

The checker also tests 10,000 random positive pairs for the superadditivity inequality

`x/(a+x)+y/(a+y) >= (x+y)/(a+x+y)`

and 10,000 random finite tail packs for the inversion `eta<eta0 => sum y<T0`. These finite tests are sanity checks only; the symbolic rational identities and the algebra in `REPORT.md` are the proofs.
