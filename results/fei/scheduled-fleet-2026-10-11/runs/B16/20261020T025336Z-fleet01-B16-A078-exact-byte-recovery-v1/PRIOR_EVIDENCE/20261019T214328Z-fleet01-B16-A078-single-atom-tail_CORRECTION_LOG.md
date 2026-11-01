# Correction and mechanism log — fixed-time central atom

1. Preserves the earlier v6 one-sided-event proof and the corrected two-sided random-walk proof inside `PRIOR_EVIDENCE/`; neither is overwritten.
2. The v6 proof's inference `K_s>=s/3 => N_s=s-K_s>=s/3` was false and remains superseded.
3. The prior corrected run repaired that logical gap with a two-sided central band but used a random-walk crossing event to obtain constant probability.
4. This run changes the probability mechanism: a single central-binomial atom gives probability `Omega(m^-1/2)`, enough because the conditional entropy debt is `Omega(m)`. The resulting per-coordinate increment is `1+Omega(sqrt(m))`, still forcing `G/I -> infinity`.
5. No independent end-to-end review is claimed. All analytic claims remain author-derived pending review.
