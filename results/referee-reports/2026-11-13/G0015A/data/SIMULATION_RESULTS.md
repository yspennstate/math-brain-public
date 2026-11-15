### Poisson-degree example

| n | Replicates | Scaled height mean ± SE | Scaled width mean ± SE | Height KS | Width KS |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 400 | 1.1936 ± 0.0117 | 1.1269 ± 0.0125 | 0.1157 | 0.2174 |
| 3,000 | 400 | 1.2572 ± 0.0140 | 1.1431 ± 0.0118 | 0.0307 | 0.1749 |
| 10,000 | 300 | 1.2173 ± 0.0164 | 1.1790 ± 0.0143 | 0.1028 | 0.1271 |
| 30,000 | 200 | 1.2534 ± 0.0198 | 1.2054 ± 0.0175 | 0.0456 | 0.0940 |
| 100,000 | 300 | 1.2184 ± 0.0148 | 1.2301 ± 0.0147 | 0.0919 | 0.0573 |

Seed: 151520261114. One worker at nice 10; 33.14 seconds; peak RSS 138,510,336 bytes (132.1 MiB).

### Forward-binomial example

| n | Replicates | Scaled height mean ± SE | Scaled width mean ± SE | Height KS | Width KS |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 400 | 1.1745 ± 0.0124 | 1.1556 ± 0.0125 | 0.1103 | 0.1840 |
| 3,000 | 400 | 1.2060 ± 0.0128 | 1.1833 ± 0.0133 | 0.0841 | 0.1475 |
| 10,000 | 300 | 1.2204 ± 0.0152 | 1.2078 ± 0.0159 | 0.0896 | 0.1020 |
| 30,000 | 200 | 1.2102 ± 0.0185 | 1.2555 ± 0.0178 | 0.0791 | 0.0574 |
| 100,000 | 150 | 1.2221 ± 0.0187 | 1.2185 ± 0.0204 | 0.0934 | 0.0831 |

Seed: 151520261113. One worker at nice 10; 24.04 seconds; peak RSS 121,733,120 bytes (116.1 MiB).

Both limiting means are 1.2533141373. The finite samples have visible bias and Monte Carlo variation: in the primary Poisson run at n=100,000 the scaled height mean is about 2.35 Monte Carlo standard errors below the limiting mean and the width mean about 1.58 below it. These observations neither prove convergence nor refute it; they are not treated as an exact finite-n fit. No samples or seeds were discarded. The secondary run was retained in full. The choice of the Poisson run was made to match the root and forward degree laws, not to improve the numerical agreement.

Across the two runs there are 3,050 trees and 450 at n=100,000. Both runs stay far below 4 GB, use one numerical thread, and inherit nice 10. They simulate genealogical branching models, not diffusion paths on finite graphs.
