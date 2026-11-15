# Rigorous results proved in this investigation

These are elementary partial results and reductions, not a solution for any fixed d>=3.

## 1. Degrees 0, 1 and 2

**Proposition.** The requested conclusion holds for d=0,1,2. For d=0,1 it holds for every admissible graph, and for uniform simple 2-regular graphs the defect is O_p(log n/n).

**Proof.** Degree zero is immediate. A 1-regular graph is a perfect matching. Put one endpoint of every edge on each side to get MaxBis=n/2. If n/2 is even, put whole matching edges on each side to get MinBis=0. If n/2 is odd, split exactly one matching edge and otherwise use whole edges, giving MinBis=1. Thus the normalized defect is at most 1/n.

Every simple 2-regular graph is a disjoint union of cycles. Write O(G) for its number of odd cycles and C(G) for its total number of cycles. Alternating colors on each even cycle cuts all its edges with equal side sizes. An odd cycle loses exactly one edge and has side imbalance one; because n is even, the number of odd cycles is even. Choose opposite majority colors on half of them to cancel the imbalance. This proves the exact deterministic formula MaxBis=n-O(G): no cut can do better on an odd cycle. To construct a small bisection, order the cycles and take whole cycles until adding another would pass n/2, then take a contiguous segment of that one cycle to reach exactly n/2. At most two edges cross, so 0<=MinBis<=2. Consequently

    (MaxBis+MinBis)/n - 1 = (MinBis-O(G))/n,
    |(MaxBis+MinBis)/n - 1| <= (C(G)+2)/n.

It remains to bound C(G) for a uniform simple 2-regular graph. Use a uniform pairing of 2n labeled half-edges, two at each vertex. For 3<=l<=n, counting cyclic choices of l distinct vertices and their half-edges gives

    E C_l = (n)_l 2^l/(2l) * (2n-2l-1)!!/(2n-1)!!
          = 1/(2l) * product_{j=0}^{l-1} [2(n-j)/(2(n-j)-1)].

For l<=n/2, log of the product is at most sum 1/(2(n-j)-1) <= l/(n+1)<1/2; hence E C_l<=1/l. There is deterministically at most one component cycle longer than n/2. Therefore E C<=H_floor(n/2)+1=O(log n), allowing the harmless loop/double-edge components to be handled separately. More explicitly their expected counts are n/(2n-1) and n(n-1)/[(2n-1)(2n-3)], respectively. The probability of a nonsimple pairing is at most their sum=3/4+o(1), so simplicity has probability bounded away from zero. Conditional on simplicity, every simple labeled 2-regular graph has equally many pairings, and E C remains O(log n). Markov's inequality yields C=O_p(log n), proving the claim. □

Here O_p is boundedness in probability at that scale, not an assertion of a particular uniform high-probability constant. For every diverging a_n, the bound gives C<=a_n log n with probability tending to one.

## 2. First-moment bounds with exact complement symmetry

**Proposition.** Let d>=3 be fixed, and let q_d be the unique root in (0,1/2) of

    H(q_d) = (1-2/d) log 2,
    H(q) = -q log q -(1-q) log(1-q), with H(0)=H(1)=0.

Set alpha_d=d q_d/2. For every epsilon>0, with probability tending to one in the uniform simple d-regular model,

    MinBis/n >= alpha_d-epsilon,
    MaxBis/n <= d/2-alpha_d+epsilon.

**Proof.** In the pairing model fix a bisection; each part has a=dn/2 half-edges. For k crossing edges, choose k half-edges from each part, match them bijectively, and pair the remaining half-edges internally. Thus, when a-k is even,

    P(cut=k) = binom(a,k)^2 k! [(a-k-1)!!]^2 / (2a-1)!!,

and the probability is zero for the other parity. Adopt (-1)!!=1. Stirling's formula, uniformly in k with an O(log n) error, gives

    log P(cut=k) = a[H(k/a)-log 2]+O(log n).

There are binom(n,n/2) candidate sets, at most exp(n log 2). Hence the expected number of bisections of size k=xn has exponent at most

    n Phi_d(x)+O(log n),
    Phi_d(x)=log 2+(d/2)[H(2x/d)-log 2].

This is strictly negative on closed subintervals below alpha_d and above d/2-alpha_d, since H(q)=H(1-q). A union bound over the O(n) possible k proves the exclusions for the pairing model. For fixed d, the probability of simplicity converges to exp(-(d^2-1)/4)>0, so conditioning on simplicity preserves events whose failure probability tends to zero. Each simple labeled graph has (d!)^n representing pairings, giving the required uniform model. □

The standard simplicity limit is used only for this transfer; it is also implicit in all cited configuration-model papers. Approximate roots (not required for the symbolic proof) are alpha_3=0.0922357051181, alpha_4=0.220055728877, alpha_5=0.365256008530. The complementary bounds do NOT establish a direction for MinBis+MaxBis: one is a lower bound and the other an upper bound.

## 3. Ground-state and finite-temperature reduction

Let Omega={sigma in {-1,+1}^n : sum sigma=0}, m=dn/2, and Q_G(sigma)=sum_{uv in E}sigma_u sigma_v. Put A=max_Omega Q and B=min_Omega Q. Since cut(sigma)=(m-Q(sigma))/2,

    MaxBis+MinBis-m = -(A+B)/2.                         (1)

This identity is deterministic. If Z_G(beta)=sum_{sigma in Omega}exp(beta Q_G(sigma)) and beta>0, then

    A <= log Z_G(beta)/beta <= A+log|Omega|/beta,
    -B <= log Z_G(-beta)/beta <= -B+log|Omega|/beta.

Subtracting, the two nonnegative entropy errors differ in absolute value by at most log|Omega|/beta. Combining with (1) gives

    | (MaxBis+MinBis-m)/n
      + [log Z_G(beta)-log Z_G(-beta)]/(2 beta n) |
       <= log binom(n,n/2)/(2 beta n) <= log 2/(2 beta). (2)

Thus equality of the limiting normalized log partition functions at positive and negative beta for an unbounded sequence beta->infinity would imply the conjecture. Agreement only for beta below a finite reconstruction threshold cannot make the right side vanish. This explains precisely the gap left by the 2025 positive-temperature theorem; its Hamiltonian conventions differ by a harmless affine change from Q.

## 4. Concentration: expected versus typical formulation

For fixed d, the conjecture in probability is equivalent to

    E[MaxBis+MinBis]/n -> d/2.

**Proof.** A two-edge switching of a pairing changes the crossing size of every fixed cut by at most two. Taking a maximum or a minimum preserves this Lipschitz bound. Their sum F=MaxBis+MinBis therefore changes by at most four. Reveal a uniform perfect matching pair by pair; alternative partners can be coupled by one two-edge switching of the unexposed completion. The Doob martingale has increments of absolute value at most four and at most dn/2 steps. Azuma-Hoeffding gives, for the pairing-model expectation,

    P(|F-E_pair F|>=t) <= 2 exp[-t^2/(16dn)].          (3)

Conditional on simplicity, divide this probability by the fixed positive simplicity probability. Integrating (3) shows E_simple|F-E_pair F|=O_d(sqrt n), so the two expectation centers differ by O_d(sqrt n). Hence F/n-E_simple F/n converges to zero in probability. This proves sufficiency of the expected formulation. Necessity follows from 0<=F/n<=d and bounded convergence in probability (uniform integrability). □

The balance condition does not alter the Lipschitz argument, as the admissible family of vertex subsets is identical before and after a switching.

## 5. Complementary local rules and a sufficient reduction

**Proposition (tree-gauge pairing).** Fix d>=2 and a finite radius r. Suppose a sequence of d-regular graphs has, for every fixed radius, tree neighborhoods at all but o(n) vertices. Let F be an isomorphism-invariant rule on a rooted radius-r d-regular tree with independent standard Gaussian vertex labels, taking values in {-1,+1}, and suppose F(-x)=-F(x) almost surely under the Gaussian labels. Define its companion by

    F^-(x on B(v,r)) = F(((-1)^dist(v,w) x_w)_{w in B(v,r)}).

For each rule, label the vertices independently by standard Gaussians (the two rules may share the labels), and repair its side sizes to n/2. If C_F and C_Fminus are the resulting cut sizes, then

    (C_F+C_Fminus)/n -> d/2 in probability.

**Proof.** On the union of the two radius-r neighborhoods of the endpoints u,v of an edge, suppose the neighborhood is a tree. Set x'_w=(-1)^dist(u,w) x_w. These are still independent standard Gaussians. The companion output at u equals the original F output with labels x'. At v the transformed labels are the negatives of x' on its neighborhood, so oddness makes its output the negative of the original F output there. Thus the probability that the companion cuts uv is exactly one minus the probability that F cuts uv. Edges whose radius-(r+1) neighborhood contains a cycle are only o(n); their total contribution to the error is o(n). Summing edge expectations therefore gives E(C_F+C_Fminus)=dn/2+o(n), before balancing.

Oddness and label symmetry give mean-zero output spin at each tree vertex. On the exceptional vertices one can use the sign of the root label, preserving mean zero and locality. For a fixed graph of bounded degree and fixed r, outputs on disjoint radius-r neighborhoods are independent. The dependency degree is bounded in terms of d,r, so both the sum of spins and each cut count have variance O_{d,r}(n). Consequently the two side imbalances are O_p(sqrt n), and the cut sums differ from their expectations by O_p(sqrt n). Flip half the excess spins to make each labeling an exact bisection. Each flip changes at most d crossing edges, so the total repair cost is O_p(sqrt n)=o_p(n). This proves the assertion. The same argument conditional on a random locally tree-like graph proves the corresponding random-graph statement. □

The transformation F -> F^- is an involution and preserves oddness and invariance. Hence, if both true optimum densities at a fixed d can be approximated arbitrarily closely by this class of finite-radius odd local rules, the requested identity follows: the achievable local cut-density set is invariant under c -> d/2-c, so its infimum and supremum add to d/2. Approximability of both global optima is an additional hypothesis, not proved here.

A simple example shows the limitation of observing complementary values. Take

    F_v = sign(sqrt(d) X_v + sum_{w~v} X_w),
    F^-_v = sign(sqrt(d) X_v - sum_{w~v} X_w).

On a tree their adjacent Gaussian inputs have correlations 1/sqrt(d) and -1/sqrt(d). The usual planar-angle argument for a centered Gaussian pair gives disagreement probability arccos(rho)/pi: rotate two independent standard Gaussian coordinates, whose direction is uniform on the circle; the sign-disagreement sectors have total angle 2 arccos(rho). Thus their cut densities are

    d/(2pi) arccos(1/sqrt(d)),
    d/2 - d/(2pi) arccos(1/sqrt(d)).

For d=3 these are about 0.45613 and 1.04387, whose sum is exactly 1.5 despite being far from the optima. This is a standard tree-gauge idea (related to the symmetry in Lyons's local-rule constructions), made explicit here. EO's global ranks and balance constraint are not covered by this finite-radius proposition; the example nevertheless establishes that a near-correct sum alone need not indicate accurate endpoints.

## 6. Why a deterministic regular-graph inequality cannot replace randomness

For the disjoint union of an even number of K4 components, MinBis=0 and MaxBis=n, so the sum is n<3n/2. Thus even asymptotically, regularity alone does not imply the identity or a lower inequality. For the finite cubic graph K4, MinBis=MaxBis=4, and the sum is 8>6; a universal finite upper inequality also fails. These are not counterexamples to the uniform random asymptotic conjecture. No all-graph inequality in either direction is being used.
