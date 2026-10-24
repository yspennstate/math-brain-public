# Independent trace route: exact reduction and obstructions to generic shortcuts

2 October 2026. **The actual three-crossing middle-trace inequality remains
unproved here.** This checkpoint proves an equivalent four-flux
formulation and a Dirichlet-Gram reduction, then gives a complete new
counterexample to a broader common-score trace claim. It also rules out
using total positivity of the score-ordered noise semigroup. None of
these route obstructions disproves the original three-crossing candidate,
ordinary slab FEI, or unrestricted Boolean FEI.

I read `three_crossing_trace_candidate.md`,
`three_crossing_component_comparison_candidate.md`, the entire exact
stress script/report, and the existing four-crossing construction. The
boundary-endpoint normalization was independently confirmed with the
author. The exact checker `three_crossing_trace_k_route_obstructions.py`
and its JSON record the identities and the new counterexample formulas.
No prior author file or Git state was changed.

## 1. Precise normalization and the remaining inequality

The uniform cube has 2^n vertices. For a Boolean H, let Gamma_H(x) be its
number of pivotal input coordinates, K=E Gamma_H=I(H), and

    nu_H(x)=Gamma_H(x)/(2^n K).

This is a probability measure: it chooses a pivotal undirected edge
uniformly and then one endpoint uniformly. Each undirected edge has two
directed endpoints; physical flux throughout this note is twice the edge
count divided by 2^n.

For four consecutive common-score regions E0,E1,E2,E3 with labels
+,-,+,-, denote the six increasing edge fluxes by e_ij. Set

    x=e_02, y=e_13, o=e_03+e_12, t=e_01+e_23.

The actual middle threshold H at the E1/E2 cut has

    K=x+y+o, I(f)=o+t, E_nu f=(x-y)/K.

Thus

    K Var_nu(f)=K-(x-y)^2/K
               =[4xy+2(x+y)o+o^2]/(x+y+o).

It is at least 2min(x,y); for x<=y, subtracting 2xK from the numerator
leaves 2x(y-x)+2yo+o^2>=0. The proposed bound
K Var_nu(f)<=2I(f) is therefore exactly equivalent to

    **4xy <= o^2+2t(x+y+o).**                         (R)

No approximation or unrecorded factor enters this reduction. If (R)
holds, the component sums I(f)+2x and I(f)+2y have minimum at most
3I(f), which is the conditional FEI route already described by the author.

The exact five-variable weights (2,2,2,2,3), cuts (-2,0,2), give
x=y=3/4, o=3/8, t=1. Their trace ratio is 15/11 and their minimum
component ratio is 23/11. My checker regenerates all six edge fluxes
directly. This retains the known failure of component constant two
without confusing it with the still-plausible trace constant two.

## 2. A Dirichlet-Gram formulation

Use L=(1/2)sum_i(Id-flip_i), and D_i h=(h(x_i=+1)-h(x_i=-1))/2.
The uniform Dirichlet form is

    E(u,v)=E[u Lv]=sum_i E[D_i u D_i v].

For Boolean h, E(h,h)=I(h). A positive-weight sign halfspace has
D_i h in {0,1}. Let Ha,Hb,Hc be the nested endpoint halfspaces at
a<b<c, with Hb=H. Up to the already fixed output orientation,

    f=-Ha+Hb-Hc,
    Hb f=Ha-Hc-1.

Both identities follow by evaluating the four regions. Put
A=E(Ha,Ha), B=E(Hb,Hb), C=E(Hc,Hc),
U=E(Ha,Hb), V=E(Hb,Hc), Z=E(Ha,Hc). Then

    I(f)=A+B+C-2U-2V+2Z,
    K=B, K E_nu f=U-V.

For the second identity, LH=H Gamma_H, so
E[Gamma_H f]=E(Hf,H)=E(Ha-Hc-1,Hb)=U-V.
This is an electrical/Gram formulation of the same candidate.

For each input i, the three derivatives are indicators of intervals of
the *same* width 2w_i in the rest score, with ordered centers a,b,c.
Their possible patterns are 000,100,110,111,010,011,001. In particular
101 is impossible. The 110 and 011 patterns are exactly the same-label
cancellations x and y. This structural reduction is valid, but positivity
of the Gram matrix and these patterns alone do not prove (R): the
abstract majority/dictator monotone-region obstruction has precisely
the adverse cancellation pattern. The missing input is a quantitative
constraint from the single additive score and its fixed edge increments.

## 3. A genuine same-score slab disproves a generic boundary-trace theorem

The following stronger shortcut is false:

    I(H) Var_nu_H(g) <= C I(g)

with a universal C for every parallel slab g and every halfspace H of
the same positive linear score. The counterexample has only two slab
crossings. Its trace threshold lies strictly inside the slab, where g
does not cross. It is therefore **not** a counterexample to (R), which
requires H to be the actual middle crossing of an alternating
three-crossing function.

Take k>=2 coarse signs y_1,...,y_k and an odd number N>=3 of fine signs
x_1,...,x_N. Let p=2^(-k), A=2N+1, and

    Y=sum_(j=1)^k 2^(j-1)y_j,
    T=sum_(i=1)^N x_i,
    S=A Y+T.

All weights are positive. Y takes the odd integers from -(2^k-1) to
2^k-1, each once. Its unique value one is attained at
c*=(-1,...,-1,+1). Since abs(T)<=N<A, the open slab (0,2A) contains
exactly the score copy Y=1. Thus

    g=1-2*1{0<S<2A}=1-2*1{y=c*}.

The two actual crossings are 0 and 2A; neither endpoint is attained.
The function is independent of all fine coordinates. Its exact influence
is the point-event influence

    I(g)=2kp.                                        (4)

Choose H=sign(S-A). Since N is odd, S=A never occurs. Below the copy
Y=1 the halfspace is negative and above it positive. Within that copy
it is odd-N majority M(x)=sign(T). Outside that copy its label is y_k.
Equivalently

    H=y_k-2*1{y=c*, T<0}.

Write M_N=E abs(T). It has exact value

    M_N=N binom(N-1,(N-1)/2)/2^(N-1).

The halfspace is monotone, so I_i(H)=E[z_i H] for any input sign z_i.
Summing the coarse-coordinate Chow coefficients yields
1+(k-2)p, because P(T<0)=1/2 and sum_j c*_j=2-k. Summing the fine
coefficients yields p E[M(x)T]=pM_N. Therefore

    K=I(H)=1+(k-2)p+pM_N.                            (5)

We also compute the exact boundary-trace mean. At y=c*, the fine pivotal
count is the majority pivotal count. If T<0, exactly k-1 coarse flips
cross H; if T>0, exactly one does. Hence

    E[Gamma_H 1{y=c*}]=p(M_N+k/2).

Since g=-1 on this fiber and +1 elsewhere,

    K E_nu_H g=E[Gamma_H g]
              =K-2p(M_N+k/2)
              =1-2p-pM_N =: M.                     (6)

It follows exactly that

    K Var_nu_H(g)=(K-M)(K+M)/K,
    K-M=kp+2pM_N,
    K+M=2+(k-4)p.                                   (7)

These identities are independently verified on nine full truth tables,
including k=2,N=17 (nineteen inputs), by directly counting Gamma_H,
the signed endpoint sum Gamma_H g, and the physical g flips. This checks
normalization and the common-score realization rather than relying on
a heuristic approximation.

## 4. The generic trace ratio diverges: complete analytic bounds

Set N=4^k+1, which is odd. For N=2d+1, the elementary central-binomial
bound binom(2d,d)/4^d>=1/(2sqrt(d)) gives

    M_N >= (2d+1)/(2sqrt(d)) >= sqrt(N/2).

For completeness, the central-binomial lower bound follows by induction:
at d=1 it is equality, and the successive ratio (2d+1)/(2d+2) has
square at least d/(d+1). Also M_N<=sqrt(N) by Cauchy-Schwarz.
Thus, with p=2^(-k),

    pM_N >= 1/sqrt(2),
    pM_N <= sqrt(1+p^2) < 9/8.

For k>=2, (k-2)p<=1/8; the maximum is attained at k=3,4.
Equation (5) consequently gives K<9/4. Equations (7) give
K-M>=sqrt(2)>1 and K+M>=3/2. Therefore

    K Var_nu_H(g) >= (1*(3/2))/(9/4)=2/3,
    [K Var_nu_H(g)]/I(g) >= 1/(3kp)=2^k/(3k) -> infinity.

All limiting claims are thus established analytically. The exact symbolic
checker verifies these bounds at k=2,...,6 using the central-binomial
Fraction formula. Its numerical ratio display is illustrative only;
the dimension-independent failure is proved by the inequalities above.

This shows precisely why a generic trace Poincare theorem for scalar-score
functions, or one derived only from ordinary slab FEI, cannot finish the
three-crossing route. The test H must be tied to an actual crossing of f
in the specific alternating pattern. The cube's exact linear-drift and
constant-quadratic-jump identities hold in this counterexample as well,
so those identities do not rescue the proposed generic shortcut.

## 5. Score ordering does not make the noise semigroup totally positive

A second possible shortcut would import one-dimensional TP2 or
variation-diminishing semigroup arguments after ordering cube vertices
by their additive scores. That premise is already false on two inputs.

Take weights (1,2). In increasing score order the states are
00,01,10,11 with scores -3,-1,1,3. At correlation rho=1/2 each coordinate
stays with probability p=3/4 and flips with probability q=1/4, so the
ordered transition matrix is

    [[p^2,pq,pq,q^2],
     [pq,p^2,q^2,pq],
     [pq,q^2,p^2,pq],
     [q^2,pq,pq,p^2]].

The minor using rows 0,1 and columns 1,2 is

    (pq)(q^2)-(pq)(p^2)=-3/32<0.

Thus this score-ordered kernel is not TP2. The exact checker verifies
the rational minor. The underlying full-coordinate product kernel has
the usual correlation properties, but summing coordinates and imposing
a scalar order does not supply the stronger TP2 premise required by
that shortcut. This counterexample is not a counterexample to (R).

## 6. What is still missing

The author's trace normalization, implication to component constant
three, and my equivalent reduction (R) are correct. The new generic
trace counterexample and the TP2 obstruction are complete. They leave
the actual four-flux inequality for a middle *retained crossing*
unresolved. I have neither proved it nor produced a violating
three-crossing common-score example.

The finite stress and subsequent exhaustive small-weight tests reported
by the author provide useful evidence, not the missing structural
estimate. A proof still needs a dimension-independent quantitative
relation among the two canceled fluxes and the opposite-label boundary,
using their common additive score. No unrestricted three-crossing FEI
theorem should be inferred from this checkpoint.
