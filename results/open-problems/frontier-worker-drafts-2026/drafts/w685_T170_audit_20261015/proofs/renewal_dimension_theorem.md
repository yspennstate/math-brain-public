# Candidate FPP diagonal bounds in dimensions 18 and 19 (C019-v1)

Status: proof (unaudited), owner work draft; novelty not established. Target 2, kind moved. The internal audit is CLEAN; independent-model approval remains required. No new non-ball dimension is claimed here.

Consider nearest-neighbour first-passage percolation on Z^d with independent Exp(1) edge times. Let mu_diag(d)=lim_{k->infinity} T(0,k(1,...,1))/(k sqrt(d)). The candidate bounds are

| d | exact s | exact z | downward lower floor for mu_diag(d) |
|---|---|---|---|
| 18 | 31010781/500000 | 1612528463/500000000 | 0.080099928228 |
| 19 | 1312953/20000 | 64604651/20000000 | 0.077855718601 |

The hardest step is the all-length encoding of fixed simple paths by the height-renewal operator. Its geometric construction and prefix/bridge/suffix proof are C013-v4, with each load-bearing step rederived in renewal_self_audit.md. They are dimension-independent for these d: every local test uses at most four axes, and an appended axis absent from the three-direction history has exactly d-r choices. The saved graph is byte-identical in both cases. The extra seed choices and retained longer returns only overcount simple paths.

Here are the parameter-dependent premises, each checked separately for d18 and d19. Set a=s+1, t=7/5, and w(I,p)=(a/(a+I))^(p+1). All 2,564 rational sign/mark norm inequalities give M_(mark,sign)w <= (d z^sign/a)w. The scalar quota gives r=d(z+t^4/z)/(a t)<91/100. Killed-walk counts and the formal renewal recurrence compute all scalar coefficients through length 400; the remaining mass is at most (7/5)(91/100)^401/(1-91/100). The exact scalar enclosure and all irreducible profiles through length 21 enclose the omitted bridge operator. A positive binary64 boundary vector, interpreted as an exact rational vector, satisfies Bv<=kappa v on all 330 boundary states. The original kappa bounds are 999907618879537695/10^18 in d18 and 999936480509838187/10^18 in d19, both strictly below one. The separately implemented audit gives smaller upper factors, so also verifies these stated bounds. See audits/operator_d18.json and operator_d19.json; no eigenvector assumption is used.

The all-length deterministic height lemmas give 4m>=n-17 for initial/no-cut words and 4m>=n-1 for terminal words. The common norm bounds their sums by geometric series in r. Comparability of positive w and v on the finite boundary space then bounds the remaining sum by a multiple of sum_j kappa^j. Hence the complete tilted Laplace sum is finite. The fixed-path shortcut conditioning, fastest-path existence, Markov estimate, Borel-Cantelli argument and Euclidean normalisation are exactly those rederived in renewal_self_audit.md. They imply mu_diag(d)>=sqrt(d) log(z)/s.

The displayed decimal floors use integer square-root lower bounds at scale 10^24 and 50 positive terms of log(z)=2 sum_{j>=0} ((z-1)/(z+1))^(2j+1)/(2j+1). Thus every truncation is downward. The new arithmetic checker independently reproduces both floors. They exceed the previous C011-v3 candidate floors by 0.000007999952 (d18) and 0.000007999688 (d19). C011-v3 and this result are both unaudited proof candidates. The independently checked fallback remains C003-v2: 0.080065422991 and 0.077824524846 respectively.

Reproduction: run scripts/audit_renewal_independent.py graph, then its arithmetic and operator phases with --d 18 and --d 19. The original certificate producers and their manifests are in dimension_extension/d18/ and d19/. The audit script imports none of those producers. Resource admission requires at least 2 GB free; each operator run uses one core below normal priority with estimated peak below 1 GB.
