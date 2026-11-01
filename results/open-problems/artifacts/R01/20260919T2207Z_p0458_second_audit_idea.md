# R01 independent audit idea — P0458 bilateral degree fluctuations

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum.**

This note is intentionally written before any R01 checker for this package.

Audit target: R7-03 / `P0458`, the Dabirian–Subramanian standardized-degree open question for the bilateral-preference graph `LK(n,k)`.

I will not inherit P26's conclusion. I will try three independent attacks before any finite cross-check:

1. **#2 ATTACK THE NEGATION FIRST.** Try to break the claimed regime classification at the two seams where it is most vulnerable: `k -> infinity, n-k -> infinity` with one side diverging arbitrarily slowly, and the dense boundary `r=n-1-k` fixed. Check especially whether the root cutoff centering/scaling, shared-edge covariance, and the complete-graph degeneracy leave an uncovered switching sequence.
2. **#5 ADD A PARAMETER AND DIFFERENTIATE / TRACK IT.** Treat the fixed-complement parameter `r` as the interpolation variable. Re-derive the mixed-Poisson intensity `Lambda_r(a)`, its mean/variance, and the `r -> infinity` scaling independently, checking that it glues to the interior law rather than merely matching the first moment.
3. **#25 COUNT THE SAME THING TWICE.** Re-derive the key constants by genuinely different representations: the interior covariance influence via a beta integral; the fixed-complement mean both from the mixed-Poisson intensity and beta–gamma algebra; and the Gaussian limit constants from positive parts of correlated normals.

A PASS requires source-exact scope, a complete proof in all asymptotic regimes claimed, valid first-two-moment convergence for standardization, correct fixed-`k` prior-art separation, and no hidden dependence gap. Any checker written later is only a finite algebraic cross-check, not the proof.
