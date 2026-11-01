# P0110 independent route, precommitted before reading w375/w376 proofs

2026-10-10. Target: Question 22 of Auffinger–Damron–Hanson, ordinary iid undirected nearest-neighbor FPP on Z^d, d>=2, with a concrete nondegenerate law for which fluctuation and wandering exponents exist in a stated common sense and satisfy chi=2xi-1. The survey's equation alone does not fix the exponent definitions; Chatterjee's upper and lower exponent definitions are the strongest existing precise conditional theorem I found.

## Route

Use an exact noise interpolation, rather than balancing deterministic curvature against assumed fluctuations. For a concrete smooth law (initial candidate: uniform weights on [1,2]), resample each edge independently with probability t; define C_n(t)=Cov(T_n(omega),T_n(omega^t)). Derive the t=0 derivative from the edgewise Efron-Stein/Walsh decomposition and seek matching bounds on the resampling sensitivity from geodesic overlap at a scale controlled by transverse wandering. This would turn a geometric overlap estimate into passage-time variance estimates. In parallel, seek exponent existence from almost-multiplicative bounds on the variance scale and geodesic width, with constants uniform over dyadic scales. Chatterjee/Auffinger–Damron would then supply the relation if their hypotheses hold.

## Hardest open piece

Matching lower and upper estimates on the noise covariance decay or a uniform variance scale; the FPP variance-ratio scar says an apparently local fourth-moment argument can silently assume the variance comparison it seeks. No such estimate is currently proved here. The exact interpolation identity by itself will not solve P0110.

## Immediate proof step

Derive the finite-edge resampling identity with all factors and limiting assumptions, then identify which implication from overlap to a uniform dyadic variance comparison fails. Review w375/w376 artifacts after this precommit.
