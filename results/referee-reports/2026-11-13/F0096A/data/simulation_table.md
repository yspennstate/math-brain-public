| $c$ | $n=1000$ | $n=10000$ | $n=100000$ | Mean solve time at $n=100000$ (s) | Largest observed degree |
|---:|---:|---:|---:|---:|---:|
| 1.50 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 1.867 | 3 |
| 1.55 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 2.217 | 8 |
| 1.60 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 2.061 | 9 |
| 1.75 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 1.849 | 11 |
| 2.00 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 1.984 | 14 |
| 2.25 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 2.077 | 16 |
| 2.50 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 1.529 | 17 |

All 210 cycles passed independent verification. There were no heuristic failures, disconnected samples, bridges, articulation vertices, or degree-3 triples sharing an identical neighborhood. No failure structure was therefore observed. Ten samples per cell provide modest finite-size evidence: even 10/10 successes give only a 0.741 one-sided 95% lower confidence bound on that finite-size success probability, with no simultaneous coverage claim. They do not establish an asymptotic limit.

The serial sweep took 520.9 seconds. Maximum simulator RSS was 61.8 MiB; the independent verifier used 148.9 MiB. Both are well below 4 GB. The longest solver run took 3.157 seconds; sample-generation time is recorded separately and increases substantially with density.
