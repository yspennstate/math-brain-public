# Independent referee check: w535, P0309

Verdict: **KEEP**, as a proved short-range obstruction under the exact ordinary grand-canonical DLR assumptions in `w535/INDEPENDENT.md`. It is not a crystalline-phase theorem.

Reproduction. Fix a bounded Borel set B and exterior configuration eta. The empty term in Xi_B is 1. Since v is nonnegative, every n-particle Boltzmann factor is at most 1, so Xi_B is between 1 and sum_n (z|B|)^n/n! = exp(z|B|). Thus the conditional void probability is 1/Xi_B >= p_B := exp(-z|B|). This remains true if some exterior energies are infinite.

For disjoint equal-volume B_i and C_m = intersection_{i<=m}{N_{B_i}>0}, C_{m-1} belongs to F_{B_m^c}. Hence P(C_m) = E[1_{C_{m-1}} P(N_{B_m}>0 | F_{B_m^c})] <= (1-p_B)P(C_{m-1}); induction gives (1-p_B)^m. No independence is used. For each integer radius R choose countably many pairwise disjoint deterministic balls. For any tail starting at k, the event that all balls in that tail are occupied is contained in the first m occupied events for every m and has probability zero. A countable union over k and intersection over integer R yields infinitely many empty balls for each R, almost surely.

Pathwise, a full-rank lattice L+a has finite covering radius c. If a bijection to the configuration moved every lattice site by at most M, every open ball of radius R>c+M would contain a particle. The preceding common probability-one event has an empty such ball for every integer R. This argument quantifies over each possibly random L,a,M on the same path; it does not require an uncountable probability intersection.

Sharpness: v=0 gives the Poisson DLR specification and conditional void probability exactly exp(-z|B|). The claim about a finite-volume Riesz limit beta down to 0 follows by bounded convergence for each n and summable domination by (z|B|)^n/n!.

Scope: This rules out uniformly bounded displacement from a lattice. It permits periodic Gibbs states with rare holes and does not apply to a neutralized long-range Riesz specification. The unresolved target step is constructing an unpinned finite-temperature crystalline Riesz Gibbs phase.
