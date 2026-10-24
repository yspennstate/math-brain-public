# r43 exact arithmetic checks

The analytic arguments are in `REPORT.md`; these are arithmetic/symbolic sanity checks only.

```text
rank1_constant=6.727171322029716
rank1_threshold_paid=430.5389646099018
partner_wmax_floor=0.3280414319251811
partner_sharpened_paid=110.48033984697105

Counterexample lower-bound samples at t=epsilon/200:
epsilon=0.5  lower=1.151292546497023
epsilon=0.25 lower=0.5756462732485115
epsilon=0.1  lower=0.2302585092994046
epsilon=0.01 lower=0.02302585092994046

For each sampled epsilon, det([[epsilon,1],[1,1/epsilon]])=0 and its sole singular value is epsilon+1/epsilon.
QFORM_B06_R43_CHECK_PASS
```

No histogram, Monte Carlo estimate, or numerical extremality claim is used.
