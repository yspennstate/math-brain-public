# P0043: finite-radius pivotal concentration

2026-10-10. Exact target and source restrictions are in STATEMENT.md. No proof of the full target is claimed. Referee: w434, pending. This lane addresses parameter-space concentration of Russo pivotal mass; it does not attempt the other triads' spatial renormalisation or uniqueness arguments.

## Definitions

G is infinite, connected and locally finite. Fix o and 0<p_c<1. For n>=1, A_n is connection from o to the graph-distance sphere of radius n by a path contained in the finite ball B(o,n). Write f_n(p)=P_p(A_n). A_n decreases to {|C_o|=infinity}. Thus f_n decreases pointwise to theta_o, f_n is an increasing polynomial, and f_n(0)=0. Define I_n(p)=f_n'(p). For independent Bernoulli bonds, the finite Russo formula gives I_n(p)=sum_{e in E(B(o,n))} P_p(e is pivotal for A_n).

The p_c=0 case of the full target is immediate: the critical configuration has no open bonds and hence only singleton clusters. The substantive reduction can therefore restrict to 0<p_c<1 without losing a target case.

The Russo formula follows by differentiating the finite multilinear expectation with one parameter per edge: the partial derivative for e is P(A_n | e open)-P(A_n | e closed), equal to the probability (over the other independent edges) of pivotality. Restricting all parameters to p and applying the chain rule gives the sum. No conditional probabilities are multiplied without independence.

## L02: a critical jump is exactly a pivotal-measure atom

On the compact interval [0,p_c], let mu_n(dp)=I_n(p) dp. Then mu_n converges weakly to theta_o(p_c) times the point mass at p_c.

Proof. The total mass is f_n(p_c), tending to theta_o(p_c). For each t<p_c, mu_n([0,t])=f_n(t), tending to zero by the definition of p_c. For any continuous h, split its integral at p_c-delta. Below this point, the absolute contribution of h(p)-h(p_c) is bounded by 2||h|| f_n(p_c-delta), which tends to zero. On the remaining interval it is bounded by the modulus of continuity of h at scale delta times mu_n([0,p_c])<=1. First let n tend to infinity, then delta tend to zero. This proves weak convergence. No limit is interchanged with a derivative or a sum of pivotal probabilities.

## L03: exact missing condition and a stronger sufficient estimate

For this graph and root, theta_o(p_c)=0 if and only if

    lim_{delta down to 0} sup_n integral_{p_c-delta}^{p_c} I_n(p) dp = 0.       (UI_c)

Proof of sufficiency. For fixed delta in (0,p_c), the integral equals f_n(p_c)-f_n(p_c-delta) and tends to theta_o(p_c). The asserted uniform bound makes this limit zero as delta tends to zero.

Proof of necessity. Given epsilon>0, choose N with f_N(p_c)<epsilon. For n>=N the integral is at most f_n(p_c)<=f_N(p_c)<epsilon. The finitely many polynomials f_1,...,f_{N-1} have a common continuity modulus at p_c, so choosing delta small makes their increments less than epsilon too.

A sufficient quantitative input is: for some eta>0, r>1 and finite M,

    sup_n ||I_n||_{L^r([p_c-eta,p_c])} <= M.                              (Lr)

Assume eta<p_c. Holder gives each critical-window integral <= M delta^(1-1/r), so (UI_c) holds and theta_o(p_c)=0. The r=infinity case gives M delta. Mere uniformly bounded L^1 norms give no such conclusion: all mu_n have total mass <=1 even when they concentrate into a critical atom.

## Hardest remaining input, explicitly unproved

Derive (UI_c), or a weaker effective estimate implying it, from quasi-transitivity on the residual subexponential-growth graphs with p_c<1. In particular no such estimate is supplied here on nearest-neighbour Z^3. (UI_c) is equivalent to the target, so the reduction must never be relabelled a proof of the conjecture. (Lr) is stronger and is only a possible sufficient route; no assertion is made that it holds on every graph in the target class.

## Attempt to use local pivotal limits: where it fails

For a fixed edge e and fixed p, indicator(e pivotal for A_n) converges pointwise to indicator(e pivotal for the infinite-cluster event). This follows by writing pivotality as the difference between the indicators of A_n with e forced open and forced closed; both decreasing indicators have limits. Dominated convergence therefore gives convergence of each single-edge probability. It supplies neither domination over edges nor a uniform modulus in p. Passing the limit through the full spatial sum and through an interval shrinking to p_c would require precisely the additional bound the argument lacks. Quasi-transitivity alone has not yet supplied that bound.

## L04: an explicit bounded-degree obstruction when symmetry is dropped

Let k_n=floor(log_2((n+1)^2)), k_0=0, and construct a rooted spherically symmetric tree with b_n=2^(1+k_n-k_{n-1}) children at every level-(n-1) vertex. Its level size is N_n=2^(n+k_n). The root has b_1=8 children. For n>=3, ((n+1)/n)^2<=16/9<2, so k_n-k_{n-1} is zero or one; at n=2 the difference is 3-2=1. Thus b_n is 2 or 4 for n>=2. The maximum graph degree is 8. The degree-8 root is unique, so automorphisms preserve distance from it, giving infinitely many orbits. The tree is not quasi-transitive.

Let Z_n count the vertices in level n connected to the root by open bonds, and M_n=E_p Z_n=p^n N_n. For p<1/2,

    M_n=(2p)^n 2^k_n <= (2p)^n (n+1)^2 -> 0.

Markov's inequality gives P_p(Z_n>0)<=M_n, so there is no infinite root cluster. For p>0, take a finite root-to-v path with k edges. Independence gives P(path open and v infinite)=p^k P(v infinite with the path forced open), and opening these edges can only increase survival. Thus theta_root>=p^k theta_v. Every theta_v is consequently zero when theta_root is zero; the countable union over vertices excludes all infinite clusters. At p=0 this is immediate. This argument does not assume independence between cluster events and path events.

At p=1/2, M_n=2^k_n >= (n+1)^2/2. Given Z_{n-1}, the independent offspring counts are Binomial(b_n,p), so W_n=Z_n/M_n is a nonnegative mean-one martingale and

    E(W_n^2) = 1+(1-p) sum_{i=1}^n 1/M_i.

Indeed the conditional variance of Z_n is Z_{n-1} b_n p(1-p), and division by M_n^2 adds (1-p)/M_n to the previous second moment. Therefore at p=1/2,

    E(W_n^2) <= 1 + sum_{i=1}^n 1/(i+1)^2 <= pi^2/6.

Cauchy--Schwarz applied to E(W_n 1_{Z_n>0})=1 gives P(Z_n>0)>=1/E(W_n^2)>=6/pi^2. The events {Z_n>0} decrease, so theta_root(1/2)>=6/pi^2>0. Hence p_c=1/2 and critical survival is positive. There is no independence assumption about different generations beyond the conditional branching calculation. No graph-size simulation is needed.

This is a counterexample only after quasi-transitivity is removed. It invalidates a proposed proof of (UI_c) using bounded degree, independent bonds, or exponential root-volume growth alone. In this example the measures in L02 have a limiting critical atom of mass at least 6/pi^2. It does not contradict the target or Hutchcroft's exponential-growth theorem, both of which retain quasi-transitivity. The construction and argument are self-contained campaign work; novelty is not claimed.

## L05: pointwise influence decay still loses the critical atom

In the tree of L04, for every fixed p in (0,1/2), I_n(p)->0, while integral_0^{1/2} I_n(p) dp=f_n(1/2)>=6/pi^2 for every n. Thus even pointwise convergence to zero together with bounded total L^1 mass does not justify passing a limit under the Russo integral.

Proof. For a finite increasing bond event, p I_n(p) is the expected number of open pivotal edges, because pivotality does not depend on the state of its own edge. For A_n on a tree, when A_n occurs every open pivotal edge lies on every open root-to-level-n path, hence there are at most n of them. When A_n fails there are no open pivotals. Consequently

    I_n(p) <= (n/p) f_n(p) <= (n/p) (2p)^n (n+1)^2 -> 0.

The lower bound on the integral is L04. The endpoints do not matter to Lebesgue integration. This strengthens the obstruction: even vanishing individual finite-event derivatives at every strictly subcritical parameter cannot prove (UI_c).

## L06: the uniform bound can be proved on regular trees

Here is a positive control for the proposed proof route. Let T_D be the D-regular tree, D>=3, and b=D-1. Put

    c_b = (b-1)/(2b) (1-1/b)^(b-2) > 0.

For every radius n>=1, its root-to-sphere probability satisfies

    sup_{p in [1/(2b),1/b]} f_n'(p) <= D(1+2/c_b).                       (RT)

In particular for the 3-regular tree the bound is 27. This is an actual uniform L^infinity bound, not an unproved input; hence (UI_c) holds for this special case.

Proof. In the forward b-ary tree let s_m(p) be the probability of connection to level m, with s_0=1. Independence between the b child subtrees gives s_{m+1}=g_p(s_m), where g_p(s)=1-(1-ps)^b. At p=1/b, g(0)=0, g'(0)=1 and g''(s)<=-2 c_b for 0<=s<=1. Taylor's formula yields g(s)<=s-c_b s^2. Thus 1/s_{m+1}>=1/s_m+c_b and s_m(1/b)<=1/(1+c_b m). By monotonicity the same upper bound holds for p<=1/b.

The open-pivotal identity proved in L05 applies to any rooted tree, so p s_m'(p)<=m s_m(p). For p in [1/(2b),1/b] this gives s_m'(p)<=1/(c_b p)<=2b/c_b; for m=0 the derivative is zero. In the D-regular tree,

    f_n(p)=1-(1-p s_{n-1}(p))^D.

Consequently f_n'(p)<=D(s_{n-1}+p s_{n-1}')<=D(1+2/c_b). This proves (RT).

For completeness its critical parameter really is 1/b. The expected number of open root-to-level-n paths is D p (bp)^(n-1), so there is no survival for p<1/b. For 1/b<p<1, g_p'(0)=bp>1 and g_p(1)<1, so g_p has a positive fixed point. The iteration from s_0=1 stays above it, and therefore has a positive limit. This gives survival and proves p_c(T_D)=1/b. At p_c the earlier s_m bound gives extinction directly as well. None of these facts is claimed new.

This control completes the route on regular trees and isolates what it does not explain: a comparable critical-window bound on subexponential quasi-transitive graphs with cycles. That remains G01.

## L07: the symmetry attempt leaves an explicit spatial tail

Restrict for this calculation to a transitive graph satisfying the mass-transport principle: for every nonnegative diagonally automorphism-invariant transport F(u,v), sum_v F(o,v)=sum_u F(u,o). This assumption is stated explicitly; no such formula is asserted without unimodularity or the appropriate orbit weights.

For the finite-radius events A_n(u) centred at u, choose

    F(u,v) = (1/2) sum_{e incident to v} P_p(e pivotal for A_n(u)).

The transport is invariant. Every edge has two endpoints, so its outgoing mass from o is I_n(p). The incoming mass is

    I_n(p) = (1/2) sum_{u in V} sum_{e incident to o}
                         P_p(e pivotal for A_n(u)).                     (MT)

All sums are finite for fixed n: an edge incident to o can affect A_n(u) only when it lies inside B(u,n), which implies u in B(o,n). This proves the identity directly from the stated mass-transport assumption. Parallel edges, if present, are counted with multiplicity and still have two endpoints; loops may be omitted as non-pivotal.

This is the attempted use of symmetry in G01. It reduces the edge choices to the finitely many edges at o, but leaves every possible distant centre u. Bounding every probability by one gives only I_n(p)<=deg(o)|B(o,n)|/2. Its integral over a critical window grows with n and does not prove (UI_c). Pointwise convergence for any fixed centre cannot control centres escaping to infinity. The required new estimate is the uniformly vanishing critical-window integral of the entire incoming mass in (MT), not a bound for one centre or one finite orbit. No decay or cancellation establishing that estimate is supplied here. This is the same G01 gap in explicit spatial form, not an additional claimed theorem.

## L08: w433's tightening, independently rederived by w432

The adversary reports that L02-L06 survive as scoped claims, and supplied a stronger regular-tree bound in his 05:28 peer message. Its discovery is credited to w433. Here is an independent derivation, retaining the factor lost in L06.

With D>=3, b=D-1 and c_b as in L06, for every n>=1,

    sup_{p in [0,1/b]} f_n'(p) <= D/c_b.

For the 3-regular tree this is 12, rather than the earlier 27, and covers the whole subcritical interval including both endpoints.

Proof. Put m=n-1. The already established tree pivotal inequality is p s_m'(p)<=m s_m(p), not merely p s_m'<=2/c_b. It therefore gives directly

    f_n'(p) <= D(s_m+p s_m') <= D(m+1)s_m
             <= D(m+1)/(1+c_b m) <= D/c_b.

The last inequality uses 0<c_b<=1 (indeed c_b<1/2 for b>=2). At p=0 no division is used; all quantities are finite polynomials and the inequality remains valid. This proves the larger parameter range and the sharper constant. The old bound 27 remains a true, weaker historical claim. Referee w434 still needs to check the strengthened claim; no full-target progress is inferred from this regular-tree refinement.
