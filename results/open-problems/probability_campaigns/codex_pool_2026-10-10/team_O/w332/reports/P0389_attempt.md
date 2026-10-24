# P0389: conservation is a global constraint, 2026-10-10

Status: proof of a scope obstruction and a comparison-model lemma; ARW's genuine mesoscopic question remains unresolved in the inspected local material. This continues the prior store card, which already refuted an unrestricted window lower bound.

If binary occupations eta_x have deterministic total k on N sites, then S_B=k-S_(B complement) exactly, so their variances agree. Each sum has range at most its number of sites, hence Var(S_B)<=min(|B|,N-|B|)^2/4. On a cycle with one omitted site, this is <=1/4 even when |B| tends to infinity. Translation invariance strengthens it to (k/N)(1-k/N).

New continuation: uniform sampling of a k-subset makes this obstruction quantitative. Put rho=k/N. Then E eta_x=rho, Var eta_x=rho(1-rho), and for x != y,

Cov(eta_x,eta_y)=k(k-1)/(N(N-1))-(k/N)^2=-rho(1-rho)/(N-1).

Therefore Var(S_B)=|B| rho(1-rho)(N-|B|)/(N-1). With rho -> rho_0 in (0,1), |B| -> infinity and |B|/N -> 0, Var(S_B)/|B| -> rho_0(1-rho_0)>0. The same fixed-mass constraint thus coexists with ordinary mesoscopic variance and strongly suppressed macroscopic variance. This law is a comparison law, NOT asserted to be the ARW free-chain law.

Conservation also gives the exact covariance sum rule sum_y Cov(eta_x,eta_y)=0 for every x. At finite N, zero-frequency cancellation by itself does not establish the infinite-volume or small nonzero-frequency structure-factor limit. Any ARW proof needs a dynamical estimate of spatial correlations, beyond deterministic particle count.

Checks: enumerate all 495 four-subsets on N=12 and every m=1,...,11; check_math.py verifies the variance formula and complement identity using rational arithmetic. Failure modes: confusing the comparison measure with the ARW law; taking fixed-N zero frequency before the mesoscopic limit; dropping the requirement |B|/N -> 0. Auditor: w346, pending.
