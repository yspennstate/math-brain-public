# Exact obstruction to replacing two currents by four currents

Status: proved special case, author proof; independent review pending w470. This is a counterexample to two graph-uniform shortcuts, not a counterexample to C0052.

Let T_m be the path a--b--z_1--...--z_(m-1)--c--d, with m bridge edges between b and c, and m >= 1. Give every edge coupling parameter t = beta J > 0. A random current has mass proportional to the product of t^n_e/n_e!, conditional on its prescribed sources. Let n_1 have sources {a,b}, n_2 have sources {c,d}, and n_3,n_4 have no sources. All four are independent.

On a tree, an edge's parity is the parity of the number of sources on either side of its cut. Hence n_1 is odd on a--b and even everywhere else; n_2 is odd on c--d and even everywhere else. Both auxiliary currents are even on every edge. The remaining edge values are independent, since the parity constraints on a tree fix each parity separately.

For an even current edge, P(n_e=0) = 1/cosh(t) = s. Write r = 1-s and p = 1-s^2 = tanh(t)^2. An odd current edge is always present.

1. The original connection probability q_m = P^{ab,cd}(b connected to c in n_1+n_2) is p^m: each of the m bridge edges is present with independent probability p.

2. Let A=C_b(n_1+n_3) and B=C_c(n_2+n_4). Each augmented cluster explores the bridge from its own end with independent edge-presence probability p. If the number L_A of consecutive open edges from b is m, they meet automatically. Otherwise P(L_A=k)=(1-p)p^k for 0<=k<m, and B reaches that endpoint with probability p^(m-k). These cases are disjoint and exhaustive. Thus

   P(A intersects B) = p^m + sum_(k=0)^(m-1) (1-p)p^k p^(m-k)
                     = [1+m(1-p)] p^m.

Consequently q_m/P(A intersects B) = 1/[1+m(1-p)] -> 0 at fixed t. No positive constant c, uniform over all these finite ferromagnetic graphs, can satisfy q_m >= c P(A intersects B).

3. The single-current cluster C_b(n_1) hits c with probability r^m, whereas the augmented cluster C_b(n_1+n_3) hits c with probability p^m. Their ratio is (r/p)^m = [1/(1+s)]^m -> 0. Therefore the exact augmented occupation formula G(b,c)G(c,a)/G(b,a) cannot be substituted for the single-current occupation probability, even up to a positive graph-uniform lower constant.

At t=log(3), s=3/5, r=2/5 and p=16/25. Both examples then have rational probabilities: q_m=(16/25)^m; augmented meeting=[1+9m/25](16/25)^m; single/augmented occupation=(5/8)^m. At m=100 the connection reversal loses a factor exactly 37.

The random-current source for the two distinct probability spaces is Aizenman, arXiv:2112.04248v3, equations (5.9), (5.13), and (8.1). Equation (8.1) is an UPPER bound involving augmented clusters. The elementary tree calculations above are this campaign's own derivation.

Scope: this does not rule out a dimension-specific reversal for critical nearest-neighbor Z^3, a nonlinear comparison, or an independently proved lower bound for the original currents. It rules out the stated universal constant comparisons only.

NEXT: Prove a variance-normalized non-Gaussianity reduction using the original two-current measure and identify its dimension-specific overlap input.
