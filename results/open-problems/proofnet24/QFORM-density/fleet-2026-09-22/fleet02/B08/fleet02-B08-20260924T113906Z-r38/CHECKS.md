# r38 deterministic check output

Executed deterministic calculation for the live constants and the Walsh stress core.

```text
g=0.323223304703363
beta0=5.3947966093944364e-06
bank_residual=3.3717478808715220e-07
bank_s3_gate=0.323215212508449
bank_s4_gate=2.8138981909743913e-12
zero_residual_density_constant=1120.113131231172
full_core_eigenvalues=-1.0000000000001517e+00,1.1390888232654106e-13,1.0000000000000000e+00,2.0000000000000377e+00
bank_core_eigenvalues=-7.8077640640419328e-01,5.7004735769680369e-14,5.0000000000000000e-01,1.2807764064041363e+00
hub_pair_bound=7.8125026341780319e-03
child_pair_bound=1.2207031250000000e-04
augmented_leverage=9.1552734375000000e-05
theorem_H_density_constant=8192.0
QFORM_B08_R38_BANK_PUNCTURE_CHECK_PASS
```

The tiny positive eigenvalues are expected: analytically the full three-dimensional nontrivial cubic is
`p_theta(x)=x^3-x^2-(2+theta^2)x+theta^2`; for `0<theta<1`, its three roots lie in `(-2,-1)`, `(0,1)`, `(2,3)`. Thus together with the separate eigenvalue `1`, exactly three eigenvalues have modulus at least one. The bank cubic is `x^3-(1/2)x^2-(1+theta^2/2)x+theta^2/4`; its roots lie below `-1/2`, between `0` and `1/2`, and above `1`, while a separate eigenvalue equals `1/2`, so the third bank singular value is exactly `1/2` for the checked range.
