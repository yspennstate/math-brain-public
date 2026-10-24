# C0041: independent adversary analysis

The exact target is Open question 2.20 in the Drewitz-Ramirez source, as recorded by the September 7 intake: iid site transition vectors for a nearest-neighbor RWRE on Z^d, d >= 2, uniformly bounded below by one deterministic kappa > 0. For a fixed unit vector l, P_0(X_n dot l -> +infinity) = 1. Does liminf (X_n dot l)/n > 0 almost surely follow? The stronger deterministic-velocity formulation is claimed by a September 2026 manuscript. Current openness is UNKNOWN, and this packet makes no novelty claim.

INDEPENDENT.md was saved before reading paired arguments or the recent manuscript body. The earlier C0041-A001 attempt also stopped at integrability of the regeneration duration. H and I exact-ID searches returned no C0041 attempt; the Lean ranking is an annotation, not a proof.

## The hardest input in the proposed route

Let D be first backtracking below the initial directional level, and let tau_1 be the first successful record regeneration under a construction for which iid block factorization has actually been proved. The unresolved RWRE input is E_0[tau_1 | D = infinity] < infinity under the target assumptions alone. The relevant law, future certification of success, and finite mean displacement must all be stated. The present packet does not prove that input.

## A proved sufficient premise for an attempt-cost argument

Let (F_i) be an increasing sequence of sigma-fields. Let S_i be nested events, with S_1 the whole space and S_i in F_i. Interpret S_i as reaching attempt i. Assume 0 <= r < 1 and a < infinity such that

E[1_{S_{i+1}} | F_i] <= r 1_{S_i},

and, for each nonnegative attempt cost A_i,

E[1_{S_i} A_i | F_i] <= a 1_{S_i}.

For C = sum_{i>=1} 1_{S_i} A_i, one has E C <= a/(1-r).

Proof. Taking expectations of the first inequality and inducting gives P(S_i) <= r^(i-1). The second inequality, followed by the tower property, gives E[1_{S_i} A_i] <= a P(S_i). Tonelli then gives E C <= a sum_{i>=1} r^(i-1) = a/(1-r). No independence of costs or attempts was used. Every tower step conditions on the single specified sigma-field and uses S_i in F_i. If an initial search cost A_0 is added, add E A_0 to the bound.

This is a sufficient premise, not a necessary characterization of ballisticity. In RWRE, a uniform conditional cost bound over all revealed histories may be much stronger than the annealed first moment being sought. One may instead prove summability of E[1_{S_i} A_i] directly. The proof obligation is the cost estimate, not merely the survival estimate.

## Counterexample to the weaker premise

Take iid success indicators B_i with parameter q in (0,1), independently of iid L_i with P(L_i=2^k)=2^(-k-1), k>=0. Let N be the first success and C=1+sum_{i<N} L_i. Then N has a geometric tail, every attempt cost and C are finite almost surely, but E C=infinity. Already {N>1} has positive probability and contributes E L_1=infinity. With L_i truncated at 2^K, E C^(K)=1+((1-q)/q)(K/2+1). This refutes the inference from finite individual attempts and geometric attempt counts to finite expected duration. It is not a counterexample satisfying C0041's RWRE assumptions.

## Review scope

w446 is the independent reviewer for these two small results; no review verdict has been received. The brain draft must keep them as unreviewed concept material. A comparator containing an admitted theorem does not certify a completed formalization. Conversely, an admission in a challenge template is not evidence that a separate supplied solution is invalid; locate the actual solution before making such a judgment.

NEXT: Inspect the recent manuscript's crossing-tail-to-regeneration bridge and the paired proof's actual conditional cost premise.
