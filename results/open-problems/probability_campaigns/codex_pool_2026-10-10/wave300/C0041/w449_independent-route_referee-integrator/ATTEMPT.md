# C0041 independent route, saved before reading the peers' proposed proofs

## Exact working target

For a nearest-neighbor RWRE on Z^d, d >= 2, sample one i.i.d. environment of transition rows, each of its 2d probabilities at least a deterministic kappa > 0 almost surely. For a unit direction l, assume under the annealed law P_0 that X_n·l tends to +infinity almost surely. The question is whether liminf_n (X_n·l)/n > 0 almost surely (indeed a deterministic vector velocity with positive l projection). The local 2012/2014 source calls this a conjecture; an OpenAI repository dated September 2026 claims a resolution, whose actual proof and axioms still need audit.

## Route committed independently

Use two-sided slab exit probabilities, not regeneration-time moments or occupation-time estimates. Let T^-_L=inf{n: X_n·l <= -L} and T^+_L=inf{n: X_n·l >= L}. For positive integer L define q_L=P_0(T^-_L < T^+_L). Directional transience gives q_L -> 0: each sample path satisfying X_n·l -> +infinity has a finite infimum of X_n·l over n, so 1_{T^-_L<infinity}->0; dominate 1_{T^-_L<T^+_L} by it and apply bounded convergence. The argument uses no iid or uniform ellipticity, and yields no rate.

The hoped-for next step is a quenched finite-box renormalization producing, from sufficiently small q_L at one scale, a bound q_{2L} <= C q_L^2 + exp(-cL), with controlled transverse width and modified slab geometry. Iterating such an estimate could reach the known polynomial ballisticity criterion. This recursion is **not proved**. Sites visited by two putative crossings share the same environment; averaging the quenched factors cannot be replaced by multiplying their annealed means. Side exits and arbitrarily long transverse excursions cause additional loss. The single hardest open piece in this route is a valid decoupling/renormalization estimate under bare directional transience that controls these correlations and side exits.

## Status

The vanishing q_L lemma is a proved elementary consequence of directional transience, useful only as the zero-rate input. The proposed recursion is a sketch and does not solve C0041. Priority now is auditing the September 2026 formal solution claim and the peers' actual arguments.
