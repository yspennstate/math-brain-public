# Linear monotone DNFs: proofs and the remaining gap

All entropy is in bits. Input literals are independent uniform 0/1 bits. The sign output is `f=1-2F`, where F is the DNF truth indicator. A live coordinate has positive influence. Numerical work uses integer Walsh coefficients before evaluating logarithms.

## A. A short term supplies a good coordinate — PROVED

This statement needs monotonicity, but does not need linearity. Let q=P[F=0], v=Var(f)=4q(1-q). If t is a term of width w, then some i in t has

    Inf_i >= 2q/(2^w-1),
    E_i/Inf_i <= 2 + log2(2e(2^w-1)).                 (SHORT)

In particular, a width-2 term suffices even when arbitrary wider terms are present. Which coordinate: choose any maximizer of Inf_i over i in t. The proof only requires that setting all bits of t to 1 forces F=1.

First prove the influence assertion. Order the w coordinates as i_1,...,i_w, let B_j be the event that the first j bits are 1, and put q_j=P[F=0|B_j]. Then q_0=q and q_w=0. Monotonicity gives

    q_(j-1)-q_j = (1/2) P[i_j pivotal | B_(j-1)].

The pivotal event does not depend on i_j. For any event A, P[A|B_(j-1)]<=2^(j-1)P[A]. Therefore

    q <= (1/2) sum_(j=1)^w 2^(j-1) Inf_(i_j)
      <= (2^w-1)/2 max_(i in t) Inf_i.

Now fix any coordinate i and write delta=Inf_i. Since F is monotone, its signed derivative is, up to a global sign, the pivotal indicator. Consequently hhat(empty)^2=delta^2. Write p_T=ghat(T)^2 and r_T=hhat(T)^2. Parseval gives

    sum_(T nonempty) p_T = v-delta,
    sum_(T nonempty) r_T = delta-delta^2,
    p_empty=(E f)^2.

The scalar inequality Phi(p,r)<=2 sqrt(pr) gives an empty-set cost at most 2|E f|delta. To verify this scalar inequality without assuming an entropy estimate, set x=sqrt(p/r) for r>0, use symmetry to restrict x>=1, and define

    L(x)=2x ln 2 - (x^2+1) ln(x^2+1)+x^2 ln(x^2).

L(1)=0, L'(x)=2 ln 2-2x ln(1+x^-2), and x ln(1+x^-2) decreases for x>=1: its derivative is ln(1+x^-2)-2/(x^2+1)<=0, since ln(1+y)<=2y/(1+y) for 0<=y<=1 (the difference has derivative (1-y)/(1+y)^2>=0). Thus L'(x)>=0. The zero cases follow by continuity.

For the remaining coefficients, homogeneity and concavity of Phi imply superadditivity:

    sum_(T nonempty) Phi(p_T,r_T)
      <= Phi(v-delta,delta-delta^2)
      <= (delta-delta^2) log2(e(v-delta^2)/(delta-delta^2))
      <= delta log2(ev/delta).

For the middle inequality, write Phi(P,Q)=Q log2(1+P/Q)+P log2(1+Q/P) and use ln(1+x)<=x on its second summand. For the last inequality, replace v-delta^2 by v and use that x log2(ev/x) is increasing on 0<x<=v; both delta-delta^2 and delta lie in this interval because delta<=v by Parseval. Boundary cases use continuity.

Hence the stronger per-coordinate bound is

    E_i/delta <= 2|E f| + log2(ev/delta).              (REL)

Combining delta>=2q/(2^w-1), v=4q(1-q), and |E f|<=1 proves (SHORT).

If every nonconstant member of a restriction-closed monotone class has a term of width at most W, recursively query the coordinate chosen above. The exact tree identities in the brief give

    H(f) <= [2+log2(2e(2^W-1))+2/ln 2] I(f).         (BW)

This applies in particular to monotone width-at-most-W DNFs. The mere presence of a short term at the original root does not ensure (BW) for all its restrictions: that term can be killed, leaving only wide terms. Thus (SHORT), rather than an induction for the entire mixed-width class, is the conclusion when only one short term is assumed.

Hostile second read: independently checked the factors 1/2 and 2^(j-1) using a disjoint matching, where delta/q=2/3 and the width-2 influence bound is exact. Checked the Fourier totals against Parseval, including delta^2 at the empty derivative coefficient. No assertion of a uniformly good coordinate at every restriction follows from a short term at just one node.

## B. Mixed-width load certificate — PROVED

Let the DNF be linear, with its absorbed terms removed. Fix i, let T_i be its incident terms, B_t=t\{i}, L_t=|B_t|>=1, a_t=2^-L_t, and b=sum_t a_t=lambda_i. Define the background load of a mate j by

    ell_j = sum_(s contains j, i not in s) 2^-(|s|-1),
    eta_t = sum_(j in B_t) ell_j,
    theta = 1 - [sum_t a_t eta_t + sum_(s<t) a_s a_t]/b.

Thus eta_t is a term's residual load. For a mate j in B_t, linearity gives ell_j=lambda_j-a_t. Choose any integers 1<=k_t<=L_t. Put

    gamma_t = a_t sum_(r<k_t) binom(L_t,r),
    alpha_t = 2^(binom(k_t,2)-2 k_t)
       sum_(J subset B_t, |J|=k_t)
          product_(j in J) ell_j / [1-(1/2)sum_(j in J) ell_j],
    eps = min(1, sum_t gamma_t),
    kappa = (sum_t alpha_t)/(b theta).

Assume theta>0, every denominator in alpha_t is positive, and b<=1/4. Then

    |E_i/Inf_i-2| <= 2eps+(8/ln 2)sqrt(kappa)
       +eps log2(e[3+8/(eps b theta)])
       +b log2(e[1+b^-2]).                            (MIX)

Zero eps terms are interpreted by continuity. This is a finite certificate with no maximum-width or maximum-degree parameter. It identifies every coordinate for which the displayed error is bounded; it does not assert that such a coordinate always exists.

Proof. Let N indicate that all terms avoiding i fail, A=E N, A_t the conjunction on B_t, h=N 1[OR_t A_t], and g=2N-h-1. Then delta=E h=Inf_i, with h's sign irrelevant.

For fixed t, remove from N the background terms meeting B_t and call the remaining avoidance event R. Every removed term meets B_t in exactly one variable. Under A_t=1, its residual conjunction has probability 2^-(|s|-1), and conditional on the decreasing event R its probability can only decrease by Harris's inequality. R is independent of the bits in B_t. A union bound gives

    P[N,A_t] >= a_t P[R](1-eta_t) >= a_t A(1-eta_t).

If eta_t>1, the final inequality still holds because its right side is nonpositive. For distinct t,u, the mate sets are disjoint, so Harris gives P[A_t A_u|N]<=a_t a_u. Bonferroni and a union bound now give

    A b theta <= delta <= A b <= b.                  (M1)

Partition the pivotal points by their first satisfied incident term, h=sum_t h_t, with disjoint physical supports. Write h_t=A_t psi_t, where psi_t depends only on variables outside B_t; this follows because on A_t's supporting subcube every bit in B_t is fixed. In the normalized squared spectrum of h_t, the subset of B_t is uniform. Let Omega be the union over t of the Fourier sets meeting B_t in at least k_t variables. It excludes the empty set. Then

    ||1_(Omega complement) hhat||_2
      <=sum_t sqrt(gamma_t ||h_t||_2^2)
      <=sqrt[(sum_t gamma_t)delta].                  (M2)

The last step is Cauchy–Schwarz and the disjointness of the physical supports. In particular, the q-mass outside Omega is at most eps delta.

For J subset B_t with |J|=k_t, fix all variables outside J. No background term contains two members of J. Hence

    N=R_J product_(j in J)(1-z_j Q_j),
    ||D_J N||_2^2=4^-k_t P[R_J, all Q_j=1].

Here Q_j is an OR of residual conjunctions with weights summing to ell_j; it is independent of every bit in J. R_J is decreasing and {all Q_j=1} increasing. Expanding the ORs chooses one distinct background term per j. Any two chosen residual sets intersect in at most one variable. Thus their union has size at least the sum of their sizes minus binom(k_t,2). Summing the chosen products proves

    P[all Q_j=1|R_J] <= 2^binom(k_t,2) product_(j in J) ell_j.

Moreover a union bound, Harris's inequality, and independence of z_j from R_J give

    A >= P[R_J](1-(1/2)sum_(j in J) ell_j).

Therefore the spectral mass of N containing J is at most A times the corresponding summand of alpha_t. Sum over J and then t to get

    sum_(T in Omega) Nhat(T)^2 <= A sum_t alpha_t
                               <= kappa delta.       (M3)

It remains to pass from spectral separation to entropy. For any real u,beta,

    |d/du Phi(u^2,beta^2)|
       =2|u|log2(1+beta^2/u^2) <=(4/ln 2)|beta|,

using ln(1+x^2)<=2x, with continuity at zero. On nonempty sets ghat=2Nhat-hhat. Integrating from u=-hhat to u=ghat, then applying Cauchy–Schwarz and (M3), bounds the entropy discrepancy on Omega from twice its h-mass by (8/ln 2)delta sqrt(kappa).

On its nonempty complement, ghat^2<=8Nhat^2+2hhat^2. The p-mass is at most 8A+2eps delta and the q-mass at most eps delta. Superadditivity and Phi(P,Q)<=Q log2(e[1+P/Q]), whose right side is increasing in P and Q, give a cost at most

    eps delta log2(e[3+8A/(eps delta)])
       <=eps delta log2(e[3+8/(eps b theta)]).

The actual empty coefficient costs at most Phi(1,delta^2)<=delta^2 log2(e[1+delta^-2]). The function x log2(e[1+x^-2]) is increasing on 0<x<=1/4: after multiplying its derivative by ln 2, it is 1+ln(1+x^-2)-2/(1+x^2)>0 there. Use delta<=b<=1/4. Missing h-mass changes 2delta by at most 2eps delta. These estimates prove (MIX).

Setting all L_t=L and ell_j<=(D-1)2^-L recovers the certificate (LIN) in the brief. Replacing the actual loads by these upper bounds weakens theta and increases alpha, exactly in the permitted directions.

Hostile second read: the conditioned OR events were compared only with the unconditioned product measure by Harris; no independence under N or R_J was assumed. All selected background terms are distinct because none can meet B_t twice. Triple intersections do not invalidate the union-size lower bound. The mate blocks of the h_t pieces need not be independent of N. Width-one terms require section A and are excluded from the k_t notation here.

## C. A theorem requiring loads only on one term — PROVED

Let t have width L+1 with L>=3 and a=2^-L. Suppose every variable j of t satisfies

    lambda_j <= (1+1/(64L^2)) a.                     (LOCAL)

Then EVERY i in t has E_i<6 Inf_i. No load condition on variables outside t is needed, and t need not be shortest. This is a sufficient local condition, not an assertion that its threshold is optimal. Section B is substantially more flexible when all incident neighborhoods can be inspected.

Proof. Put u=1/(64L^2), theta_0=1-Lua. For fixed i in t, the total weight of the other incident terms is at most ua. Each mate j in t\{i} has background load at most ua. Let h_t=N A_t and h_other=h-h_t. They have disjoint physical supports. Harris and the proof of (M1) give

    ||h_t||_2^2<=Aa,  ||h_other||_2^2<=Aua,
    delta>=Aa theta_0,  delta<=A(1+u)a.

Let Omega be the sets meeting the L mates of t at least once. The h_t spectrum misses Omega with probability a. The triangle inequality for the projected Fourier vectors gives q-mass outside Omega at most eps_0 delta, where

    eps_0=(sqrt(a)+sqrt(u))^2/theta_0.

The k=1 case of the background estimate gives N-mass on Omega at most A L ua/[4(1-ua/2)], or kappa_0 delta, with

    kappa_0=Lu/[4theta_0(1-ua/2)].

The entropy argument of section B therefore applies with eps_0, kappa_0, lower relative influence a theta_0, and upper absolute influence b_0=(1+u)a. Its error is at most

    2eps_0+(8/ln 2)sqrt(kappa_0)
    +eps_0 log2(e[3+8/(eps_0 a theta_0)])
    +b_0 log2(e[1+b_0^-2]).                          (LERR)

For L>=3, theta_0>0.99, eps_0<1/5, L eps_0<1/2, and kappa_0<1/[256 L(0.99)(0.99)]. These follow from L2^-L<=3/8, 2^-L<=1/8, and sqrt(u)=1/(8L). The second summand of (LERR) is <1/2. Since eps_0 a theta_0<=1,

    eps_0 log2(e[3+8/(eps_0 a theta_0)])
      <=eps_0[log2(11e/theta_0)+L+log2(1/eps_0)]
      <1+1/2+0.54=2.04.

Here log2(11e/0.99)<5 and x log2(1/x)<=1/(e ln 2)<0.54. Finally b_0<0.13<1/4, and the monotonicity already checked plus 1+0.13^-2<64 implies the last summand is <0.13(1.5+6)<1. Thus (LERR)<0.4+0.5+2.04+1=3.94, proving E_i/Inf_i<5.94<6.

For widths one, two, and three, (SHORT) gives an absolute coefficient below 8 for a maximum-influence variable in t, without any load hypothesis. Thus a uniform coefficient 8 is available for a term satisfying (LOCAL), with the small-width cases interpreted separately.

Hostile second read: h_other is bounded by the residual incident load using Harris even when it depends on all mates. Its projection was bounded by its full norm, so no unproved spectral concentration for the other incident terms is needed. The only background estimates use mates of t itself. The local threshold is close to a private term's minimum possible load; this theorem does not solve the larger-load regime.

## D. Quantitatively extreme bias — PROVED

For every Boolean function on n essential variables, put m=min(P[f=1],P[f=-1]) and r=log2(1/m). If f is nonconstant, then

    H/I <= 2[n/r+1+(log2 e)/r].                     (BIAS)

In particular m<=2^(-alpha n), for a fixed alpha>0, implies H/I<=2/alpha+2+2log2 e. This does not give an absolute constant when m tends to zero subexponentially in n.

Proof. The mass outside the empty spectral set is v=4m(1-m). Entropy conditional on emptiness gives H<=h2(v)+v log2(2^n-1)<=v[log2(e/v)+n]. Since v>=m and v<=4m, this is at most 4m[r+log2 e+n]. The edge-isoperimetric inequality gives I>=2m log2(1/m)=2mr, proving (BIAS).

Here is an elementary proof of the isoperimetric inequality used. A set of a vertices in the n-cube induces at most a log2(a)/2 edges. Induct on n. Split it into sizes a_0,a_1 along the last coordinate; the cross edges are at most min(a_0,a_1). The inductive bound follows from

    a_0 log2(a_0)+a_1 log2(a_1)+2min(a_0,a_1)
      <= (a_0+a_1)log2(a_0+a_1),

because h2(p)>=2min(p,1-p), the chord bound from concavity of binary entropy. The total edge boundary is therefore at least a[n-log2 a]. Divide by 2^n and multiply by two to obtain the influence of a sign function with minority set of size a.

Hostile second read: m is the minority probability, v is the spectral nonempty mass, and the boundary-to-influence conversion has a factor two. All three are checked on AND_n, where I=2n2^-n. The theorem is dimension-sensitive; calling an arbitrary small-bias function covered would be unjustified.

## E. Exhaustive enumeration — PROVED algorithm; CHECKED NUMERICALLY outputs

Every monotone Boolean function has a unique family of minimal true sets. If it has a linear monotone DNF representation, deleting absorbed terms leaves a linear family, so it is enough to enumerate linear antichains. Singleton minimal terms share no variable with any other minimal term. Their vertices may be separated from the terms of size at least two.

For fixed n, enumerate all linear hypergraphs with edges of size at least two, allowing isolated vertices. Start with the empty family. Process widths from n down to two. At width w, repeatedly append every compatible w-set (intersection at most one with each existing edge), and retain one exact canonical family per isomorphism class. Continue until the layer adds nothing, then decrease w. Induction on the number of w-edges proves completeness. Earlier larger edges are never removed. No non-singleton edge can contain another in a linear family.

Canonicalization refines a partition of the variable vertices by the multiset of incident-edge color-count profiles; if cells remain unresolved, it individualizes each possible vertex of a chosen cell and continues. At a discrete leaf it records the entire transformed sorted edge list, and selects the lexicographically least leaf. Refinement and branching are invariant under relabeling. Transposition twins may be skipped because the swap is checked on the complete edge family. A shared key therefore supplies an actual isomorphism, rather than only matching an invariant.

Append singleton edges to any number of isolated vertices; isolates are interchangeable. Removing the remaining unused vertices yields every essential-dimension class. In particular, removing all singleton edges from the essential-n census is a bijection with non-singleton hypergraphs on n vertices with isolates allowed.

Independent completeness check (`labeled_check.cpp`). A linear hypergraph with no singleton edges is a packing of pair-disjoint cliques of size at least three, followed by an arbitrary choice of the unused pairs as 2-edges. Choose an available pair uv. Either no larger clique uses uv, in which case it is absent or a 2-edge (factor two), or exactly one larger clique containing uv is chosen. Remove its pairs and recurse. This counts all labeled families using a different recursion from the census. Compare it with sum n!/|Aut(H)| over the census. Automorphism counts are accumulated over the exact canonical search leaves, with the skipped twin permutations restored as multiplicities. Both counts agree for every n through eight (the eight-variable files give 18,785,639,553 labeled families). The graph-only counts also agree with the standard small unlabeled graph counts; the independently labeled brute-force truth-table enumeration in analyze.py checks all dimensions through five.

`log_intervals.py` computes enclosures of log2(k), 0<=k<=65536, by integer arithmetic. Normalize k=2^a x with 1<=x<2, write z=(x-1)/(x+1)<=1/3, and use ln x=2 sum_(j>=0) z^(2j+1)/(2j+1). Positive terms, enclosing fixed-point products, and the geometric upper tail bound enclose every logarithm. Divide by the enclosed ln 2 and round outwards to units 2^-52 bits. `certify.cpp` uses integer Walsh transforms, integer squared coefficients, and signed 128-bit interval sums. It encloses every H/I and every min_i E_i/Inf_i in the entire census, retaining all possible maximizers. At the final floating conversion and divisions it takes an extra nextafter step outwards after each operation; this matters because Apple ARM long double can have the same precision as double. The report uses fewer digits than the interval width permits.

Exact maxima are also supplied as rational linear combinations of log2 of primes in analysis.json. Candidate ties at smaller dimensions are verified by equality of these expressions. This is an exhaustive computation with certified logarithms, not a random search.

## F. A regular family on which these certificates lose uniformity — PROVED

This is an obstruction to the bounds above, not a counterexample to FEI and not a proof that all possible tree-accounting arguments fail.

Let Q be a prime power and A a set of w distinct field elements, w<=Q. The variables are (x,y) in A times F_Q, and the terms are

    t_(a,b)={(x, ax+b): x in A},    a,b in F_Q.

There are n=wQ variables, Q^2 terms of width w, every variable has degree Q, and two terms intersect in at most one point: two different affine maps agree on at most one field element. Call this TD(w,Q). All variables are live, since a chosen term's vertices can be set to one and all other variables to zero.

Take Q=2^k and w=k+2ceil(log2 k)+1, for k sufficiently large that w<=Q. Write L=w-1, a=2^-L and lambda=Qa=2^-2ceil(log2 k). Then lambda is between 1/(4k^2) and 1/k^2, L/k tends to one, and every residual mate load is ell=(Q-1)a. All these facts are exact or follow immediately from the displayed definitions.

1. There is no bounded-width term, and (LOCAL) fails because lambda/a=Q.

2. The minimum value of the uniform specialization of (MIX), over every permitted threshold r=1,...,L, tends to infinity. Its theta is

       1-L(Q-1)a-(Q-1)a/2 = 1-O(1/k)>0.

   If r>=4, eps=min(1,lambda sum_(j<r)binom(L,j))=1 eventually, since lambda binom(L,3) grows linearly in k. Its entropy-error term is at least log2(8e/lambda), which diverges. For r=1,2,3, the kappa in the uniform certificate is

       binom(L,r) 2^(binom(r,2)-2r) ell^r/[a theta(1-r ell/2)].

   It has respective orders QL, Q, and Q/L, up to fixed positive factors, so its square-root error diverges. These are all possible thresholds. Allowing different thresholds on different incident blocks does not repair this: if any block has threshold at least four, sum gamma_t could conceivably remain small when few such blocks are used, so that stronger mixed optimization requires a separate argument. The all-equal-threshold uniform (LIN) certificate is conclusively obstructed; no unproved assertion about all unequal choices is needed.

3. In fact unequal choices in (MIX) fail too. Let d=Q. If at least d/2 blocks have r_t<=3, sum alpha_t/(d a theta) grows at least as a constant times Q/L (the least of the three orders above). If fewer than d/2 do, at least d/2 have r_t>=4, and sum gamma_t>=lambda binom(L,3)/2 tends to infinity. Thus eps=1 and its entropy term diverges. This proves failure of the full finite certificate for every choice of thresholds.

4. The zero probability q_0 tends to zero, but -log2(q_0)/n tends to zero as well. Let Z be the number of satisfied terms and p=2^-w. Then E Z=Q^2p tends to infinity. Each term meets exactly w(Q-1) others. Disjoint terms have independent satisfaction indicators, and an intersecting pair has covariance p^2. Consequently

       Var(Z)/(E Z)^2 <= 1/(Q^2p)+w/Q ->0,
       q_0=P[Z=0] <= Var(Z)/(E Z)^2 ->0.

   Harris's positive association for the decreasing term-failure events gives

       q_0 >= (1-p)^(Q^2),
       -log2(q_0)/n <= (Q/w)[-log2(1-p)] = O(1/k^3) ->0.

   The dimension-sensitive (BIAS) bound therefore diverges; having q_0 small by itself did not close this regime.

5. The relative-influence bound (REL) loses a uniform coefficient at every coordinate. Let N be background avoidance for a coordinate i, A_i=E N and delta_i=Inf_i. Harris gives delta_i/A_i<=lambda. Since q_0=A_i-delta_i/2,

       delta_i/q_0 <= lambda/(1-lambda/2).

   With Var(f)=4q_0(1-q_0), Var(f)/delta_i tends to infinity uniformly in i. Thus the right side of (REL) diverges for every i, regardless of the actual erasure ratio.

Small prime-field instances are CHECKED NUMERICALLY by `./structured 3 3`, `3 5`, `3 7`, `4 5`, `5 5`; outputs are TD_*.json. They are finite members of the transversal family, not a numerical sample of the asymptotic powers-of-two sequence just used. Those files give actual E/Inf and H/I, and exact finite-tree averages where computed. They do not show divergence of the actual ratios. Their small values leave the universal conjecture quite plausible.

Hostile second read: the second-moment count uses ordered meeting pairs, w(Q-1) per term, so covariance/mean-square is w(Q-1)/Q^2<=w/Q. Harris gives the LOWER bound on q_0 needed to show subexponential bias, not the reverse. The influence-to-bias inequality uses q_0=A_i-delta_i/2 and not A_i-delta_i. None of the upper bounds that diverge is being presented as a lower bound on E/Inf, a tree average, or H/I.

## G. Exact scope of the remaining problem — OPEN

For a concrete root-certificate constant 8, declare a nonconstant member covered if any of the following holds: it has a term of width at most three; the right side of (REL) is at most 8 for some coordinate; some coordinate satisfies (MIX) with error at most 6; some term satisfies (LOCAL); or the right side of (BIAS) is at most 8. Constants are covered trivially. This is an explicit finite, computable description of the cases proved here.

The uncovered set consists exactly of the linear monotone DNFs for which all those tests fail. In particular TD(w,2^k) above is uncovered for sufficiently large k. Its zero probability vanishes, and all widths grow. No bound for its actual minimum erasure ratio, or its whole-term tree average uniformly in k, has been proved here.

If every restriction of f is covered, the good-coordinate induction gives H(f)<=(8+2/ln 2)I(f). The argument does not establish this hypothesis for every linear DNF. For arbitrary f, every tree's erasure average lies between max(0,H/I-2/ln 2) and H/I, directly from the exact path identity and 0<=J<=2Inf/ln 2. This explains why a family with numerically bounded H/I cannot be claimed to refute the averaged-tree route.

There is also a scope issue in FLOW's final sentence of 12(u): min_i E_i/Inf_i<=H/I alone does not prove equality of the two global suprema. The stated tree induction supplies a converse only after adding 2/ln 2. No equality of sharp constants is used in this report.

What is still needed is either a stronger spectral separation estimate using conditional loads under background avoidance, or an amortized whole-term estimate that covers the transversal regime. Neither follows from the unconditional load union bounds above. The brief's central alternative—an absolute theorem for all of L or a family with actual unbounded obstruction statistics—remains unresolved.
