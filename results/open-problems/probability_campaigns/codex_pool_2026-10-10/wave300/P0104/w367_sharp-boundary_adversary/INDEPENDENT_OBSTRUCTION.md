# Independent sharp-boundary derivation for P0104

Saved before reading w366's ATTEMPT.md or proof claims. Primary framework checked:
Damron--Hanson--Sosoe, arXiv:1401.0917v2, Theorem 1.1; Chatterjee,
arXiv:1105.4566v3, Theorem 1.1. Exact catalog-source recovery is still pending.
This is a special-case proof and an obstruction to a stronger auxiliary assertion,
not a solution or refutation of the parent KPZ conjecture. Novelty is unclaimed.

## Claim C001: exact straight-path threshold

Let d >= 2, n >= 1 an integer, and let every nearest-neighbor edge of Z^d
have a weight in [a,b], with 0 < a < b. Let L_n be the sum along the straight
n-edge path from 0 to n e_1. If n(b-a) <= 2a, then T(0,n e_1) = L_n for
every configuration.

Proof. The straight path has cost at most nb. The only n-edge path between
these endpoints is the straight path. Every other walk has at least n+2 edges:
its length is at least n, and parity of length agrees with n on the bipartite
lattice. Its cost is therefore at least (n+2)a >= nb. Positive weights also
make deleting a repeated-vertex cycle strictly decrease cost. Thus allowing
all finite walks does not affect the conclusion. Equality permits a tie but
still gives the claimed passage-time identity.

The threshold is sharp in the following precise sense. Suppose weights are
iid, have essential infimum a and essential supremum b, and n(b-a) > 2a.
There is a positive-probability event on which the straight path is not a
geodesic. Choose delta > 0 such that
    n(b-delta) > (n+2)(a+delta).
The detour 0 -> e_2 -> n e_1+e_2 -> n e_1 has n+2 edges, none shared with
the straight path. Each of its weights lies below a+delta with positive
probability, and each straight-path weight exceeds b-delta with positive
probability, by the definitions of essential endpoints. Independence gives
positive probability to their simultaneous occurrence. On that event the
detour costs less than the straight path. This proves sharpness of the
configuration-independent sufficient threshold, not an asymptotic exponent.

## Claim C002: an admissible continuous-law variance obstruction

Take iid tau_e ~ Uniform[1,1+epsilon], epsilon > 0, on Z^d, d >= 2.
For every integer n with n epsilon <= 2,
    T(0,n e_1) = sum_{k=1}^n tau_{[(k-1)e_1,k e_1]},
    E T(0,n e_1) = n(1+epsilon/2),
    Var T(0,n e_1) = n epsilon^2/12.
The identities follow from C001 and independence of the deterministic path's
edges; no conditioning on an optimizing path is used. This law is nonatomic,
nondegenerate, bounded and has no atom at zero. The straight path is almost
surely unique even at equality n epsilon = 2, since equality of competing
costs would require endpoint weights attained by the continuous law.

Consequently, for any fixed theta < 1 there is no finite universal C such that
    Var_F T(0,n e_1) <= C Var_F(tau_e) n^theta
for every epsilon in (0,1], F=Uniform[1,1+epsilon], and every sufficiently
large n beyond a common law-independent N. Given C,N, choose n > N with
n^(1-theta) > C and epsilon = 1/n. C001 applies and the proposed inequality
reduces to n <= C n^theta, a contradiction. At theta=2/3 the exact ratio is
n^(1/3). This refutes a bound uniform over laws after normalization by the
one-edge variance. It does not refute a bound with law-dependent constants
or a law-dependent onset, and it gives no fixed-law asymptotic chi.

## Single hardest remaining piece

For a fixed admissible planar law, control unrestricted detour optimization
as n -> infinity beyond this finite straight-path window. The identity above
does not survive beyond n epsilon <= 2. No KPZ exponent follows from it.

Independent reviewer: w368 (pending). Status: author-derived proved special
case; not independently checked. No formal-check receipt is claimed.
