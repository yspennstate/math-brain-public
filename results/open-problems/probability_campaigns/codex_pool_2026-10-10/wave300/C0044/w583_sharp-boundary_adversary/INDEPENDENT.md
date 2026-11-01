# C0044 independent boundary calculation

Saved 2026-10-10 before reading any paired prover's proof. Author: w583. Independent review pending; no novelty claim.

## Uniform ellipticity does not imply the required harmonic Liouville property

Fix d >= 3 and 0 < kappa < 1/(2d). Put c = 1 - 2(d-1)kappa, p = c-kappa, q = kappa, and r = q/p < 1. Give every transverse step +/-e_i, i >= 2, probability kappa. At a site with first coordinate k >= 1 give +e_1 probability p and -e_1 probability q; at k <= -1 interchange p and q; at k = 0 give each probability c/2. This deterministic nearest-neighbor environment is uniformly elliptic with constant kappa.

Let A_+ = {X_n dot e_1 -> +infinity}. Its quenched probability from first coordinate k is

    h(k) = 1 - r^k/2       (k >= 0),
    h(k) = r^(-k)/2        (k <= 0).

The embedded first-coordinate chain has outward jump probabilities a=p/c and b=q/c. On the positive half-line r^Y is a martingale since a*r+b/r=1. Stopping at {0,M} from 1 <= k <= M-1 gives P_k(T_0<T_M)=(r^k-r^M)/(1-r^M). The finite stopping time is justified by the positive finite-interval exit probability in every fixed block. Letting M increase gives P_k(T_0<infinity)=r^k: a path hitting 0 has a finite maximum before that hit. The negative half-line follows by reflection.

From +/-1 the return probability is therefore r. After each departure from 0, the strong Markov property gives conditional return probability exactly r, whatever the previous excursions were. Iterated conditional expectation gives P(at least n further returns after a departure)=r^n, so only finitely many returns occur almost surely. This product uses conditional probabilities justified by the Markov property, not an assertion of unconditional independence. The first coordinate makes infinitely many moves because the probability of no coordinate move in the next m steps is (1-c)^m, by iterated conditioning. On its final half-line the embedded walk agrees with a biased iid-increment one-dimensional walk up to hitting 0; the ordinary strong law for that unrestricted biased walk implies divergence to the corresponding infinity on the event of no further hit. Reflection at 0 gives h(0)=1/2, and then the displayed formula follows from the hitting probability. Direct substitution also verifies harmonicity.

Thus h is a bounded, nonconstant harmonic function, 0 < h(k) < 1 for every finite k, but inf_k h(k)=0 and inf_k(1-h(k))=0. Both opposite directional events have positive probability from every site; their union has probability one. Arbitrarily strong uniform ellipticity below the symmetric endpoint does not repair a route based only on harmonicity, irreducibility or pointwise positivity.

At kappa=1/(2d), the transition vectors must all equal the simple-symmetric vector. The first coordinate is a lazy symmetric one-dimensional walk, so A_+ and A_- both have probability zero. This records the endpoint of the construction.

Scope: the constructed environment is not a stationary iid environment, so this is a counterexample only to a stronger auxiliary bridge. It is NOT a counterexample to C0044. A proof of C0044 must use iid structure to justify any additional Liouville/constancy/uniform-restart conclusion.

NEXT: Verify the exact source assumptions and peer lane boundaries, then test the paired proof against this obstruction and its valid iid specialization.
