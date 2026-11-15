For this law, E[1/alpha]=1.1 and mu=0.9 (also checked with exact fractions). The homogeneous K=2 run estimates M_2=0.419204850; it is a finite-size, finite-time estimate. Its eight-block standard deviation is 0.000539, not a confidence interval.

| K | Infinite-volume level r M_K | Guaranteed half-width mu r M_K | Guaranteed interval |
|---|---:|---:|---|
| 1 | 0.125000000 | 0.112500000 | [0.387500000, 0.612500000] |
| 2 | 0.209602425 | 0.188642183 | [0.811357818, 1.188642182] |

The K=2 entries use the estimated M_2; only the K=1 level and interval are exact numerical values. Long runs on the same sampled environment give:

| K | Density | Initial state | Current | Block SD | Across-bond current range |
|---|---:|---|---:|---:|---|
| 1 | 0.3875 | random | 0.152217837 | 0.000795 | 0.152085–0.152325 |
| 1 | 0.5000 | random | 0.152424610 | 0.000919 | 0.152290–0.152545 |
| 1 | 0.6125 | random | 0.152715946 | 0.000966 | 0.152585–0.152820 |
| 2 | 0.8115 | random | 0.243175604 | 0.001512 | 0.242915–0.243625 |
| 2 | 1.0000 | random | 0.243685634 | 0.001508 | 0.243530–0.243855 |
| 2 | 1.1885 | random | 0.244171567 | 0.000950 | 0.244055–0.244300 |
| 1 | 0.5000 | packed | 0.152905396 | 0.001153 | 0.152765–0.153055 |
| 2 | 1.0000 | packed | 0.243798642 | 0.000569 | 0.243610–0.244075 |

For K=1, the long random-state currents span 0.152217837–0.152715946. The center exceeds the proposed thermodynamic level by 21.9%. The short random-state center was 0.169206295.
For K=2, the long random-state currents span 0.243175604–0.244171567. The center exceeds the proposed thermodynamic level by 16.3%. The short random-state center was 0.273258740.

Block standard deviations describe temporal variation, not independent-sample errors or disorder uncertainty. Across-bond agreement and packed/random agreement are equilibration diagnostics, not proofs of stationarity. The sampled longest slow run is six; the second environment has only three and gives substantially higher short-run center currents. Finite-size capacity and time-to-equilibrium therefore matter separately. These experiments exhibit a nearly flat central finite-ring curve but do not verify the infinite-volume plateau height, its exact half-width, or the true endpoints. Being above r M_K at finite n is compatible with (R2), whose rare-strip limit takes place on the infinite lattice. A wider observed flat interval would also be compatible, because the theorem provides a guaranteed subinterval.
