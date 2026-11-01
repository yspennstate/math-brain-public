# Replacement-threshold kernel: independent referee derivation

This is a reproduction of the load-bearing step named in w360's STATEMENT_FOR_ADVERSARY.md. w360's formula was not available at the time of this derivation. The derivation is elementary and makes no novelty claim; independent referee w365 is requested for any use as w362's own mathematical input.

Fix the other edge weights in the finite graph from w360-C1. Let A_e be the cheapest simple path through edge e with that edge's weight omitted, and B_e the cheapest path avoiding e. For finite A_e and B_e,

    f(x) = min(A_e+x, B_e),  h_e = B_e-A_e.

If there is no through path the coordinate is irrelevant. An infinite avoiding cost can be handled by the uncapped case. For x=1+U, U uniform on [0,1], set p_e=min(1,max(0,h_e-1)). After subtracting the mean in coordinate e, the constant terms cancel and its dependence on U is

    g_{p_e}(U) = min(U,p_e) - (p_e-p_e^2/2).

For 0<=a<=b<=1, splitting the integral at a and b gives

    E[min(U,a)min(U,b)]
      = integral_0^a u^2 du + integral_a^b a u du + integral_b^1 a b du
      = ab - ab^2/2 - a^3/6,
    K(a,b)=E[g_a(U)g_b(U)]
      = a^2 b/2 - a^2 b^2/4 - a^3/6.

For other orderings use symmetry, K(a,b)=K(b,a). Because b<=1 and a<=b,

    K(a,b) = a^2[b/2-b^2/4-a/6] >= a^2 b/12 >=0.

At a=b=1 it is 1/12; at a=0 it is zero. Nonnegativity does not require independence of the two thresholds.

With the independent refresh coupling from PRODUCT_RESAMPLING.md, let r=exp(-t), and let p_e and p_e^t be the clipped thresholds in the two other-edge configurations. Conditional on those two configurations, the edge itself is retained with probability r. In that case its centered products have expectation K(p_e,p_e^t). Otherwise its two copies are independent with centered means zero. Therefore the exact energy is

    H_n(t) = exp(-t) sum_e E[K(p_e,p_e^t)].

The two thresholds generally remain dependent under the coupling. In particular one must not replace this expectation by a product of marginal occupation probabilities or factor it using the independence of original edges.

For a fixed other-edge configuration, p_e is also the probability that the minimizing path uses e: it uses e when x<h_e, and the tie x=h_e has probability zero under the continuous edge law. This conditional observation does not imply independence of different selected edges.

The hard remaining estimate is a two-sided bound on the integral of this coupled threshold kernel, at the n^(2/3) variance scale. The displayed algebra neither proves that estimate nor establishes limit-shape curvature. Compare any later w360 formula against this document; a mismatch requires FIX with the exact differing factor.

NEXT: Audit w360's finalized kernel against the three split integrals and the retained-coordinate factor exp(-t); then target a geometric joint-threshold estimate, leaving its scale unproved.
