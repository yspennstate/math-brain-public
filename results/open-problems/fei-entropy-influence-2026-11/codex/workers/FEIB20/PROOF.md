# A bounded nested witness at a leaf

This proves alternative (a) in the brief for the tree model. It does not prove FWC for arbitrary Boolean functions or for regular hypergraphs. The tree model is not regular: each terminal leaf belongs to just one clause.

All entropies and logarithms below use bits. Write L=w-1 and let delta=Inf_i. An order always means reveal order, with its last element revealed last.

## Private-clause lemma

Suppose i and k other variables B occur only through their joint AND, so a Boolean function with values in {-1,1} can be written

    f(v,i,B) = A(v) + d(v) AND(i,B).

Here v contains every variable outside this clause. There is no restriction on the other dependence on v. Let pi reveal v in any order, followed by B in any order. Then

    2(1-2^-k) <= E_i/delta <= L_i^pi/delta
              <= 2(1-2^-k) + 2^-k log2(e/(delta 2^-k)).                 (1)

Proof. Use the uniform Fourier basis on 0/1 variables. Every Fourier coefficient of AND on k+1 bits has magnitude 2^{-(k+1)}. For a subset T of v and a nonempty subset S of B, the two coefficients fhat(T+S) and fhat(T+S+i) have equal magnitude, namely 2^{-(k+1)} |dhat(T)|. The same formula for the coefficient including i holds when S is empty. Thus the derivative spectral mass with S empty is exactly q0=delta 2^-k; with S nonempty it is delta-q0.

For S nonempty, Phi(p,q)=Phi(q,q)=2q, giving an exact contribution 2(delta-q0) to E_i. Since B is revealed last, each last-element label in B also groups only pairs with p=q and contributes exactly twice its derivative mass. All remaining labels have S empty. Their total derivative mass is q0, and their total p+q mass is at most 1. Concavity and homogeneity imply superadditivity of Phi, so their total contribution is at most Phi(p0,q0), where p0+q0<=1. Finally

    Phi(p,q) <= q log2(e(p+q)/q)

because p log2(1+q/p)<=q log2(e). This proves (1), including the E_i lower bound and the witness upper bound. For k=0 the lower bound is vacuous and the inequality still holds. QED.

## The leaf influence in this tree

Fix a terminal leaf i in the first clause of Q_0 attached to mate z_0. Put

    a=2^-L, s=(1-a)^(D-1), alpha=(1+s)/2, beta=s/2.

Then the exact influence is

    delta = 2^{-(L+1)} (1-a)^(D-2)
            [ alpha^(DL-1)
              + (alpha^(L-1)-beta^(L-1)) (alpha^L-beta^L)^(D-1) ].       (2)

Derivation. Pivotality requires the other L-1 leaves of the clause to be 1, z_0=1, and all the other D-2 clauses of Q_0 to fail. These cost 2^{-(L-1)}, 1/2, and (1-a)^(D-2). Conditional on root x=0, all other terminal terms must fail, with probability alpha^(DL-1). Conditional on x=1, the target block must also fail its root term, giving alpha^(L-1)-beta^(L-1), and each other block must fail both kinds of term, giving alpha^L-beta^L. Average the two root values. This is (2).

The private-clause lemma applies with k=L-1, because the variables in this terminal clause appear nowhere else. In particular the order is explicit: reveal everything outside the terminal clause first; reveal its L-1 other leaves last.

## A uniform bound in the balanced regime

Assume integers D>=2, L>=2, and lambda=D^2 L 2^-L<=2. This includes all four balanced rows in the brief. Since a<=1/4,

    Da = sqrt(lambda a/L) <= 1/2.

Using ln(1-a)>=-2a gives (1-a)^(D-2)>=exp(-1). Also alpha=1-(D-1)a/2, so ln(alpha)>=-(D-1)a, and

    alpha^(DL-1) >= exp(-D(D-1)La) >= exp(-2).

Discard the nonnegative second term of (2). Consequently

    delta >= 2^{-(L+1)} exp(-3).

Substitute this into (1):

    L_i^pi/delta <= 2 + 2^{-(L-1)} [2L-2+4 log2(e)] < 6.              (3)

The bracket times 2^{-(L-1)} decreases for L>=2, and its largest value is at L=2; `proof_checks.json` evaluates this endpoint. Moreover both E_i/delta and the chosen witness ratio tend to 2 as L tends to infinity under lambda<=2. In particular min_pi L_i^pi/delta tends to 2 at a leaf, and min_{i,pi} L_i^pi/delta <=2+o(1).

For a concrete sequence with D tending to infinity, take D_L=floor(sqrt((7/5) 2^L/L)) for L>=4. Then D_L>=2, D_L^2 L 2^-L<=7/5, and the order above is uniformly bounded. This is an explicit balanced order family.

This is a bound over the optimum across all coordinates and all orders: it supplies one admissible coordinate and order. It makes no assertion that every order is cheap, or that the optimal root/mate order is known. A positive-c log D lower bound for every coordinate and every order on this tree family is impossible along any sequence with D tending to infinity and lambda<=2. A D-regular linear-hypergraph DNF has no degree-one leaf; the argument does not apply there.
