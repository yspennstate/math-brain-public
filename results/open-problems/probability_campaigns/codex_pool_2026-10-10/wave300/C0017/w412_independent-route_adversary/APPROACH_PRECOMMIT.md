# C0017 independent route, saved before reading w411's proof

2026-10-10. Route: conditional crossing martingales, rather than discrete parafermionic regularity or transferring triangular-lattice interfaces by local moves. No w411 proof or approach has been read. Prior-record/source recovery is still in progress; this is a method commitment, not a novelty claim.

Let C(u) be the normalized integral of [u(1-u)]^(-2/3) from 0 to u. For a continuous chordal Loewner driver W and three surviving ordered boundary points x1<x2<x3 to the right of W0, put Xi(t)=gt(xi)-Wt. If BOTH C(X1/X2) and C(X1/X3) are local martingales in the SAME filtration, the following calculation identifies the driver without first assuming that it is Brownian or even a semimartingale.

First invert C(X1/X2). Its inverse is smooth on compact subsets of (0,1). Since each gt(xi) has finite variation before swallowing, W=(gt(x1)-u*gt(x2))/(1-u) is then a continuous semimartingale. Write W=A+N with quadratic variation V=<N>. Itô's formula for each pair (i,j) gives the finite-variation identity

dA = (1/Xi+1/Xj) * (2 dt - dV/3).

Subtract the identities for (1,2) and (1,3). Since 1/X2-1/X3 is strictly positive, dV=6 dt and dA=0. Thus W is locally sqrt(6) times Brownian motion, up to the stopping/lifetime under consideration.

The hardest unresolved square-lattice premise is convergence of the actual conditional crossing observables to these Cardy functions in random slit domains, with enough joint filtration control to preserve both martingales. Ordinary fixed-domain RSW, exact discrete martingale identities, rotational invariance, or identifying one endpoint observable alone does not supply this premise.

Adversarial focus after the independent proof is saved: determine whether w411 supplies that lattice identification (or an equivalent genuinely new input), and test dependence, random-domain uniformity, observables' boundary conditions, and preservation of martingales under convergence. This conditional reduction is not a proof of C0017.
