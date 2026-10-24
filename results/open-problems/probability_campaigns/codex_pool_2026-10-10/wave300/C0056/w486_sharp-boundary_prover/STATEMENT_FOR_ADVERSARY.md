# C0056 statement and boundary lane (2026-10-10)

The intake at problems.jsonl:56 states exactly:
"Prove existence of absolutely continuous spectrum (delocalised states) for the random Schrodinger operator -Delta + lambda V on Z^3 at small disorder lambda, and GOE local statistics for its finite-volume restriction."
Source id: bourgade_band_icm_2018, Section 2.1, p. 7. Primary source recovered: Paul Bourgade, arXiv:1807.03031, https://math.nyu.edu/~bourgade/papers/ICMProceedings.pdf . It uses centered iid variables of variance one and periodic boxes for finite volume. Its qualitative GOE discussion does not fix the needed energy/DOS quantifiers. Do not silently erase that clause.

Spectral target to be distinguished from GOE: for a specified nondegenerate iid bounded real single-site law, find lambda_0 > 0 and a deterministic nonempty energy interval I such that, for each fixed 0 < lambda < lambda_0, the nearest-neighbor Anderson operator on l2(Z^3) almost surely has nonzero absolutely continuous spectral weight in I. Pure absolute continuity on I is a stronger conclusion. The public September 2026 manuscript claims purity for iid uniform [-1,1] disorder on a fixed interval above -6; it is an unverified primary claim here. Current openness: UNKNOWN.

Boundary lane statement for independent attack: let H0 be negative nearest-neighbor adjacency on l2(Z^d), V bounded iid real multiplication with M = ess sup |V_x| > 0, and R0(E+i eta) = (H0-E-i eta)^(-1), where E is in the free band [-2d,2d] and eta > 0. Determine the exact almost-sure operator norm and spectral radius of K = lambda V R0, and whether the unrenormalized Born resolvent series R0 sum_n (-K)^n can converge in operator norm uniformly as eta decreases at fixed lambda > 0. Independence and the order of limits must be explicit. No proof has been included in this statement packet.

Independent adversary: w487. Referee: w488. Author identity: native worker w486; response-side served-model evidence unavailable.

NEXT: Check the fixed-height expansion boundary without importing a conclusion about spectral type.
