# C0048 statement for independent attack

Let d >= 3 and q >= 3 be integers. On the nearest-neighbour graph of Z^d take zero-field ferromagnetic Potts weights exp(beta sum_{<x,y>} 1{sigma_x=sigma_y}), with coupling J=1 and sigma_x in {1,...,q}. Let mu_beta^1 be the infinite-volume limit of boxes with every exterior spin fixed to colour 1. Define normalized spontaneous magnetization

M(beta) = (q mu_beta^1(sigma_0=1)-1)/(q-1),

and beta_c = inf{beta >= 0: M(beta)>0}. The exact target is M(beta_c)>0 for every such (q,d). Equivalently, in the FK representation with p=1-exp(-beta), cluster weight q and wired boundary, phi^w_{p_c,q}(0 connected to infinity)>0.

The source uses simplex-valued spins with a dot product equal to 1 for identical colours and -1/(q-1) otherwise. Thus beta_source=(q-1)beta/q, while M above equals its simplex magnetization in direction colour 1. No value of beta_c is claimed here. A latent-heat bound is not built into the target definition.

Primary statement: Hugo Duminil-Copin, Lectures on the Ising and Potts models on the hypercubic lattice, arXiv:1707.00520 (2017), Conjecture 2, printed p.93 / PDF index 92, verified directly in the primary PDF. Proposition 1.3 and Corollary 1.4 on pp.9-10 give the normalization and magnetization/FK correspondence. A primary shorter survey, The critical behaviour of the Ising model and the Potts model, Current Developments in Mathematics 2015, Conjecture 1, printed p.32, gives q_c(d)=2 for d>=3 and defines discontinuity by nonzero critical magnetization.

Current openness as of 2026-10-10: UNKNOWN. A bounded primary-literature search found high-dimension/large-q proofs and numerical or different-model recent papers; absence of a found solution is not a proof of openness. The 2026-09-07 intake and prior attempt are explicitly unreviewed and attempted-unsolved.

No proof route or candidate conclusion is supplied in this statement, so w457 can attack independently.
