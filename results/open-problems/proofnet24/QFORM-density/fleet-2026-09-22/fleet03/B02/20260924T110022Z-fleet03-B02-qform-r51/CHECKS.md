# B02 r51 deterministic-check record

The checker in `CHECK.py` was reproduced in the run interpreter with NumPy and seed `20260924` on 300 seeded dense symmetric instances, leaf dimensions 3 through 7, with rejection sampling enforcing the diffuse-star condition `max_i d_i^2 <= ||d||_2^2/2`.

Observed output:

```text
seed=20260924
trials=300
violations=0
max_observed_alignment_ratio_err_r2_over_W=1.70340136404524
rigorous_alignment_ratio_bound=6
max_observed_root_fraction_2E_over_W=1.00000000000000 (roundoff at ~1e-15)
rigorous_root_fraction_bound=1
min_sampled_diffuse_margin=0.00115148369024876
delta=0.00438596491228070
delta4=3.70050173356369e-10
Cw=14.5270892696926
live_density_bound_Cw_over_delta=3312.17635348990
live_alignment_frobenius_bound_sqrt6_delta=0.0107433760648385
live_structured_s2_floor=0.989256623935161
```

The numerical exercise is corroborative only. The proof in `REPORT.md` is symbolic and does not rely on random testing, histograms, floating-point spectral claims, or interval extremality.
