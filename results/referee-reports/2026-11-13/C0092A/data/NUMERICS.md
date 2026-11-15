# Finite-volume numerical results

p_wrap is the first interpolated 50% wrapping point; p_peak maximizes susceptibility after removing one largest component. These are different finite-size proxies. Intervals below quantify block-sampling error only. Maximum grid spacing is 0.02.

| d | q | L | p_wrap (95% block interval) | p_peak (95% block interval) | chi at p_wrap | peak − wrap |
|---|---|---|---|---|---|---|
| 2 | 0.25 | 8 | 0.3300 [0.3223, 0.3372] | 0.1600 [0.1400, 0.1600] | 48.56 | -0.1700 |
| 2 | 0.50 | 8 | 0.3960 [0.3900, 0.4000] | 0.2600 [0.2400, 0.2600] | 43.00 | -0.1360 |
| 2 | 0.75 | 8 | 0.4252 [0.4199, 0.4316] | 0.3441 [0.3000, 0.3441] | 36.78 | -0.0811 |
| 2 | 0.25 | 12 | 0.3309 [0.3258, 0.3367] | 0.1600 [0.1600, 0.2000] | 104.02 | -0.1709 |
| 2 | 0.50 | 12 | 0.3906 [0.3858, 0.3979] | 0.2800 [0.2600, 0.3142] | 85.62 | -0.1106 |
| 2 | 0.75 | 12 | 0.4385 [0.4356, 0.4420] | 0.3641 [0.3400, 0.3641] | 78.15 | -0.0744 |
| 2 | 0.25 | 16 | 0.3323 [0.3270, 0.3394] | 0.2133 [0.1800, 0.2133] | 177.74 | -0.1190 |
| 2 | 0.50 | 16 | 0.4008 [0.3948, 0.4048] | 0.3142 [0.2800, 0.3142] | 148.70 | -0.0866 |
| 2 | 0.75 | 16 | 0.4408 [0.4374, 0.4453] | 0.3641 [0.3641, 0.3841] | 128.18 | -0.0767 |
| 3 | 0.25 | 4 | 0.1343 [0.1310, 0.1396] | 0.0800 [0.0800, 0.0800] | 34.32 | -0.0543 |
| 3 | 0.50 | 4 | 0.1826 [0.1786, 0.1860] | 0.1400 [0.1200, 0.1400] | 26.62 | -0.0426 |
| 3 | 0.75 | 4 | 0.2194 [0.2153, 0.2236] | 0.1800 [0.1600, 0.2000] | 22.19 | -0.0394 |
| 3 | 0.25 | 6 | 0.1197 [0.1167, 0.1235] | 0.0800 [0.0800, 0.1000] | 86.62 | -0.0397 |
| 3 | 0.50 | 6 | 0.1730 [0.1712, 0.1749] | 0.1400 [0.1400, 0.1600] | 64.73 | -0.0330 |
| 3 | 0.75 | 6 | 0.2158 [0.2131, 0.2196] | 0.1800 [0.1800, 0.2000] | 53.60 | -0.0358 |
| 3 | 0.25 | 8 | 0.1143 [0.1128, 0.1161] | 0.0800 [0.0800, 0.1000] | 172.70 | -0.0343 |
| 3 | 0.50 | 8 | 0.1714 [0.1701, 0.1729] | 0.1600 [0.1600, 0.1600] | 125.88 | -0.0114 |
| 3 | 0.75 | 8 | 0.2156 [0.2133, 0.2180] | 0.2000 [0.2000, 0.2000] | 103.27 | -0.0156 |

The full susceptibility has no finite-p singularity on a finite torus. Largest-cluster-deleted and nonwrapping susceptibility peaks are different quantities and can have large finite-size shifts. No infinite-volume threshold or scaling fit is inferred.

The initial short validation at d=3,L=2,q=.25,p=.6 missed rare connected nonwrapping configurations and gave a 12.64-standard-error discrepancy. Its summary is retained in initial_sampler_validation.csv. That parameter was rerun for one million measured sweeps per chain, stride 10. The final maximum discrepancy over 108 comparisons is 2.775 estimated standard errors.

```json
{
  "points": 294,
  "raw_samples": 235200,
  "validation_comparisons": 108,
  "validation_max_standardized_error": 2.7749380731289914,
  "phase_window_max_rhat": 1.0140653605977101,
  "phase_window_min_ess": 534.1433446129067,
  "phase_window_max_start_z": 2.755185856362215,
  "caveats": "Block bootstrap conditional on short chains; no mixing proof, no finite-size scaling fit. Constant wrapping samples have nominal zero SE but do not certify probabilities 0 or 1. Grid spacing and finite-size bias exceed many Monte Carlo errors."
}
```
