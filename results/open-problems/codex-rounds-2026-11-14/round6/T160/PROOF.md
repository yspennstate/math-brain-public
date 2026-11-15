# The background outside a subsequential incipient cluster

Let P_p be independent Bernoulli bond percolation on the nearest-neighbor
cubic lattice, with 0<p<1 and theta(p)=0. Put

    B_j = [-j,j]^3 intersect Z^3,   S_j = boundary B_j,
    F_j = E(B_j),   E_n = {0 connects to S_n},
    mu_n = P_p( . | E_n).

For a configuration omega, let C(omega) be the vertex set of its full open
root cluster, and let C_R(omega) be its root component using only F_R.
Record the internal open edges by

    tau_{uv} = omega_{uv} 1_{u in C, v in C},
    mathcal C = (C,tau).

Thus mathcal C records both root-cluster vertices and all open edges
inside that cluster; all other coordinates of tau are zero.
Suppose mu is any subsequential cylinder limit of mu_n. The results below
hold for every such subsequence; they do not assert that different
subsequences have the same limit.

**Theorem.** Along that subsequence the joint laws of

    (omega restricted to F_m, C(omega) intersect B_m)

converge in total variation for each fixed m, to the joint law of the same
variables under mu. Under mu, conditional on the vertex set C of the
infinite root cluster and its internal edge states, all edges with both
endpoints outside C are independent Bernoulli(p).

More precisely, for any finite edge set D, write V(D) for its endpoints
and A_D={V(D) intersect C is empty}. If g is any function of omega_D and
f is any bounded measurable function of mathcal C, then

    E_mu[f(mathcal C) 1_{A_D} g(omega_D)]
       = E_mu[f(mathcal C) 1_{A_D}] E_p[g(omega_D)].     (1)

In particular, if every edge incident to C is set to zero, the resulting
configuration is stochastically dominated by P_p. The assertion concerns
edges in the induced complement of C. Edges crossing from C to its
complement are necessarily closed; no product-law assertion is made for
edges whose endpoints lie in C.

## 1. The finite localization estimate

Fix m<R<n, with m>=1. In the ordinary unwired open graph on
F_R minus F_m, let N_{m,R} count components meeting both S_m and S_R.
Set

    H_{m,j} = {S_m connects to S_j using F_j minus F_m},
    b_{m,j} = P_p(H_{m,j}).

Let a_star>0 be the product probability that the interior graph on F_m
connects every vertex of S_m and the root in one component. The preceding
round proved

    P_p(H_{m,n}, N_{m,R}>=2) <= b_{m,n} b_{m,R}.       (2)

Its witness argument is recalled here. Contract the components meeting
S_m in the graph on F_R minus F_m. A path from S_m to S_n has a last
visit to their union. Its departure vertex lies on S_R. Replace the prefix
by a path to that vertex inside its local component. The tail now avoids
all other local components meeting S_m. Every other active component
supplies a disjoint short crossing. The BK inequality applied to one long
and one short crossing gives (2). It is applied to increasing connection
events, not to the nonmonotone component-count event.

For the lower bound on the conditioning denominator, require the interior
single-component event independently of H_{m,n}. Their intersection
implies E_n. Thus

    P_p(E_n) >= a_star b_{m,n}.

As E_n is contained in H_{m,n}, (2) yields

    mu_n(N_{m,R}>=2) <= b_{m,R}/a_star.                (3)

These are finite events, so (3) also holds under mu. Also mu gives
probability one to {0 connects to S_j using F_j}, for every fixed j:
this cylinder event holds under mu_n whenever n>j. Their countable
intersection implies that C is infinite under mu.

For fixed m, extinction gives a vanishing error. Writing
alpha_p(t)=P_p(0 connects to S_t), a union bound over S_m gives

    b_{m,R} <= (24m^2+2) alpha_p(R-m) --> 0.           (4)

Indeed any crossing starts at some s in S_m and reaches distance at
least R-m from s. Translation invariance bounds each such probability
by alpha_p(R-m). The boundary count is
(2m+1)^3-(2m-1)^3=24m^2+2. Finally alpha_p(t) decreases to theta(p)=0.

## 2. Full root-cluster membership is uniformly local

The deterministic point is the following. Suppose 0 connects to S_R in
F_R and N_{m,R}=1. Let Q be the root component of the full graph on F_R.
Then every other component of that graph meeting B_m misses S_R.

To prove this, let Q' be any component meeting B_m and S_R, and choose
an open path in F_R between these sets. Stop it at its first visit to
S_R and take its last visit to B_m before that stop. The remaining
segment starts in S_m and uses only F_R minus F_m, so it belongs to
an active exterior component. That component is contained in Q'. The
same argument applies to Q. Since there is only one active exterior
component, Q and Q' coincide.

A component of the graph on F_R missing S_R cannot acquire any new edge
when all edges outside F_R are added: every edge leaving B_R has an
endpoint on S_R. Therefore all the other components meeting B_m are
already full components of the infinite configuration. In particular,

    C(omega) intersect B_m = C_R(omega) intersect B_m. (5)

This proof allows arbitrary excursions and mergers outside B_R. If a
vertex in B_m could acquire a new connection to the root through such an
excursion, its local component would have to reach S_R and hence already
equal Q.

Both E_n, when n>R, and the almost-sure infinite-root event under mu imply
that 0 connects to S_R within F_R. Consequently (3) and (5) give

    mu_n(C intersect B_m != C_R intersect B_m)
        <= epsilon_{m,R},
    mu(C intersect B_m != C_R intersect B_m)
        <= epsilon_{m,R},                            (6)

where epsilon_{m,R}=b_{m,R}/a_star. In fact, outside the same exceptional
event every component meeting B_m except Q is a finite full component
contained in B_R.

## 3. Passing to the joint cluster law

Let Gamma_n^m and Gamma^m denote the joint laws in the theorem. Replace
C intersect B_m by C_R intersect B_m in each, obtaining Gamma_{n,R}^m
and Gamma_R^m. The coupling inequality and (6) give

    TV(Gamma_n^m,Gamma^m)
       <= 2 epsilon_{m,R}
          + TV(mu_n restricted to F_R, mu restricted to F_R). (7)

The last term bounds the distance between the two approximating laws
because they are images of the finite F_R configuration. Total variation
here is the supremum over events, or half the sum of atom-mass differences.

For fixed R the last term tends to zero along the given subsequence:
cylinder convergence on a finite edge set is convergence of finitely many
atom probabilities. Taking the limsup in (7), and then sending R to
infinity using (4), proves the asserted joint convergence.

This is the step that allows full-root-cluster membership in (1). Cylinder
convergence alone would not justify passing this nonlocal observable to
the limit.

## 4. The exact finite-cluster factorization

Under P_p there is no infinite cluster almost surely. Each vertex has
probability theta(p)=0 of lying in an infinite cluster, and there are
countably many vertices. In particular C is finite P_p-almost surely,
and also mu_n-almost surely, since mu_n is absolutely continuous with
respect to P_p.

Fix a finite vertex set W containing the root. Write E(W) for its induced
edges and delta W for edges with exactly one endpoint in W. The event
{C=W} is exactly the intersection of the following two events:

1. Every vertex of W connects to the root using open edges of E(W).
2. Every edge of delta W is closed.

For the forward implication, every root path to a vertex of C stays in
C; otherwise the additional vertex would belong to C. All edges leaving
C are closed. For the reverse implication, the internal paths put all of
W in C and the closed boundary prevents any further vertex from joining.

Thus {C=W} depends only on E(W) union delta W. If W is disjoint from
V(D), this edge set is disjoint from D. On {C=W}, E_n is exactly the
deterministic statement W intersect S_n is nonempty. Independence gives

    E_p[f(mathcal C) 1_{C=W} 1_{E_n} g(omega_D)]
       = E_p[f(mathcal C) 1_{C=W}]
           1_{W intersect S_n nonempty} E_p[g].       (8)

Here, on {C=W}, f(mathcal C) depends only on internal edges of W:
the vertex set is fixed and tau is zero outside E(W). Therefore the
same independence proves (8) even for arbitrary bounded f. Sum over
finite W disjoint from V(D), and divide by
P_p(E_n)>0. Absolute convergence follows from boundedness of f and g.
This proves (1) with mu_n in place of mu, for any bounded f.

## 5. Factorization under the subsequential law

Initially let f(mathcal C) depend only on membership of finitely many
vertices in C and the states of finitely many edges of tau. Choose m
containing those vertices and V(D), with all edges involved contained in
F_m. Since tau on F_m is determined by omega on F_m and C intersect B_m,
each side of (1) for mu_n is then an expectation of a bounded
function of (omega restricted to F_m, C intersect B_m).
Section 3 passes that identity to mu.

For completeness, fix D and g and define two finite signed measures on
the space of root-cluster records by

    lambda(U) = E_mu[1_{mathcal C in U} 1_{A_D} g(omega_D)],
    kappa(U)  = E_p[g] mu(mathcal C in U, A_D).

They agree on all cylinders in the record coordinates by the preceding
paragraph. These cylinders generate the record sigma-field. The bounded
monotone-class theorem therefore gives lambda=kappa on that sigma-field.
Integration against any bounded f gives
(1) in full generality.

Equation (1) means

    1_{A_D} E_mu[g(omega_D) | mathcal C]
        = 1_{A_D} E_p[g(omega_D)]

almost surely. Taking g to be indicators of all patterns on D proves
the conditional Bernoulli product law. There are countably many finite
edge sets and patterns, so a single probability-one set of records suffices
for every such assertion.

## 6. Residual domination

Define the residual edge configuration by

    sigma_{uv} = omega_{uv} 1_{u not in C, v not in C}.

Conditional on mathcal C, Section 5 identifies its law as product Bernoulli(p)
on induced-complement edges and zero on all other edges. To include a
finite set of edges whose locations relative to C are random, partition
according to which of their finitely many endpoints belong to C and
apply (1) to the corresponding allowed edge subset.

It follows that the joint law of (mathcal C,sigma) can be generated by first
sampling mathcal C with its mu-law, then sampling an independent full Bernoulli
configuration zeta, and setting

    sigma_{uv} = zeta_{uv} 1_{u not in C, v not in C}.  (9)

In this coupling sigma<=zeta edge by edge. Hence every bounded increasing
cylinder function h satisfies E_mu[h(sigma)]<=E_p[h(zeta)]. This is
stochastic domination on the countable product space.

Moreover the entire configuration is recovered as omega=tau+sigma;
the two configurations have disjoint possible open edges. The reconstruction
on any finite edge set uses only finitely many coordinates of mathcal C
and of zeta. In particular, let Q_n^m be the law under mu_n of
(C intersect B_m, tau restricted to F_m). For n,l>R>m,

    TV(mu_n|F_m,mu_l|F_m)
       <= TV(Q_n^m,Q_l^m)
       <= 2 epsilon_{m,R} + TV(mu_n|F_R,mu_l|F_R).     (10)

The first inequality is contraction under the common reconstruction kernel.
For the second, approximate each record using C_R instead of C, at cost
at most epsilon_{m,R} by (6); the approximating records are images of F_R.
This is the same triangle inequality as (7), with two finite horizons.

Thus, under the extinction premise, convergence of the laws
of mathcal C in their cylinder coordinates is equivalent to edge-cylinder
convergence of mu_n. One direction uses this reconstruction for mu_n,
which follows from Section 4. For the other direction, Sections 2--3
give convergence of C intersect B_m jointly with omega on F_m, and hence
with tau on F_m, whenever the edge laws converge. The limiting record is
the record under the limiting edge law, as shown in Section 3.

As an independent route to the domination statement, the same coupling
holds for each mu_n by Section 4. Section 3 gives cylinder convergence
of the residual configurations sigma_n to sigma. Passing the inequalities
for increasing cylinder functions yields the same domination.

In particular every residual open cluster is finite almost surely, since
the dominating full configuration has no infinite cluster. Together with
the infinite root this reproves uniqueness of the infinite cluster. The
one-endedness conclusion from the preceding round is compatible with
this factorization but is not needed for its proof.

## 7. Scope

The theorem identifies the conditional background and permits nonlocal
root-cluster marks in subsequential convergence. It does not identify
the distribution of mathcal C, including its internal open edges. That
distribution may still differ between subsequences. The alternating-branch tree in
the earlier reports illustrates why a unique infinite cluster and an
ordinary product background do not select a limiting law.

No decay exponent, quasi-multiplicativity, or convergence of the
normalized exterior responses is obtained. At p=p_c(Z^3), this result
assumes theta(p_c)=0 and does not establish that premise or T160.
No claim of literature novelty is made for the cluster factorization.
