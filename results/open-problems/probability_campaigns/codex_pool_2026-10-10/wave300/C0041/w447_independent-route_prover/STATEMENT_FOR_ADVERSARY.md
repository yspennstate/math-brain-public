# C0041 statement packet (no proposed proof)

Let d >= 2, let U = {+e_i,-e_i:1<=i<=d}, and let the environment rows omega(x,.) be independent and identically distributed probability vectors on U. Assume there is a deterministic kappa > 0 with omega(x,e) >= kappa almost surely for every x and e. The environment is sampled once and retained. Conditional on omega, X is the nearest-neighbor Markov chain from 0 with transition probability omega(x,e) from x to x+e. Write P_0 for the environment-averaged law.

For a fixed unit vector ell, the target implication is

P_0(lim_n X_n dot ell = +infinity) = 1
  implies
P_0(liminf_n (X_n dot ell)/n > 0) = 1.

This is the formulation of Conjecture 1.1 in Campos--Ramirez, Ellipticity criteria for ballistic behavior of random walks in random environment, PTRF 160 (2014), DOI 10.1007/s00440-013-0527-7. It is an almost-sure implication, not a positive-probability formulation.

Current openness: UNKNOWN. A primary repository now claims this implication in family 220 (September 23, 2026), with a Lean comparator named DirectionalBallisticity.lean. No independent mathematical or formal verification has yet been performed by w447. This packet contains the statement only so adversary w448 can begin independently.

Primary links: https://doi.org/10.1007/s00440-013-0527-7 ; https://github.com/openai/math/blob/main/lean/docs/220.md .
