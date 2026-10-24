# C0041: statement first, independent adversary packet

Date: 2026-10-10. Prover w444; adversary w445; referee w446.

Let d >= 2 and U = {+/-e_i: 1 <= i <= d}. Sample once an i.i.d. field of probability vectors omega(x, .), x in Z^d, and retain that field throughout the walk. Assume a fixed kappa > 0 with omega(x,e) >= kappa for all sites and steps almost surely. Given omega, the nearest-neighbor walk started at 0 has transition probability omega(x,e) from x to x+e. Write P_0 for its annealed law. For a fixed unit direction ell, assume P_0(lim_n X_n dot ell = +infinity) = 1. The target is P_0(liminf_n (X_n dot ell)/n > 0) = 1. A deterministic limiting velocity with positive projection is a stronger equivalent conclusion when the regeneration law of large numbers is available.

Exact published formulation: Conjecture 1.1 in Campos and Ramirez, Ellipticity criteria for ballistic behavior of random walks in random environment, https://doi.org/10.1007/s00440-013-0527-7. Definitions/source details are being recovered. This is not the stronger conjecture requiring transience on an open set to imply condition (T).

Current openness UNKNOWN. A public primary-repository scope note found on 2026-10-10 claims a complete solution: https://github.com/openai/math/blob/main/lean/docs/220.md. That announcement has NOT been proof-audited here; source code, theorem assumptions and trusted axioms must be checked before changing the target's status.

This packet intentionally contains no proof route so the adversary's first attempt can be independent. No solved or novelty claim.
