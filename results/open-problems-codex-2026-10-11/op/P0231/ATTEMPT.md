# P0231: exact question and verified partial results

Date: 2026-10-12. No proof or counterexample to the stated question was obtained.

## 1. Model and source scope

Fix distinct deterministic seeds r,b in Q=[0,1]^d. Take independent uniform arrivals X_1,X_2,... in Q. Each arrival inherits the color of its Euclidean nearest earlier site, including the seeds. Let R and B be the closures of all red and blue sites, and F=R intersect B. The question is whether D=dim_H(F) is almost surely constant, for each fixed seed pair, in the original point model. We work on the probability-one event of distinct sites, no nearest-neighbor ties, and dense arrivals. Null sets may be discarded simultaneously for all finite permutations, since there are countably many such permutations.

The source's discussion on PDF page 3, printed page 1567, explicitly asks about a zero-one law. It then turns to planar topological questions. We treat the fractal question for d>=2 (including d=2); Proposition 3.8 explicitly has d>=2. The one-dimensional boundary case below is separate. The segment variant is not used in any claim about the original problem.

## 2. A deterministic envelope over finite recolorings

**Proposition.** For every fixed seed pair and dimension, there exists a deterministic c=c(r,b,d) such that the supremum of the dimensions of frontiers obtained by arbitrarily recoloring any finite prefix of sites, then continuing nearest-neighbor inheritance along the same future arrivals, equals c almost surely. In particular D<=c almost surely. This is a reduction, not a solution of P0231: it does not prove D=c or prove D is constant.

Here recolorings may assign either color to any site in the prefix, including the initial seeds. Constant assignments contribute the empty frontier, whose dimension we define to be zero.

### 2.1. Descendant cells and refinement

Write S_n={r,b,X_1,...,X_n}. At time n assign a distinct abstract root label to each site in S_n. For t>n, follow nearest-earlier-site parent links until the first site in S_n is reached. Parent indices decrease strictly, so this terminates and defines a unique root. Let A_i^(n) consist of root site i and all future sites with this root. Let K_i^(n)=closure(A_i^(n)) relative to Q. All are compact, and their finite union is Q: their unclosed union contains every site, and those sites are dense.

Define

    H_n = union_{i != j in S_n} (K_i^(n) intersect K_j^(n)).

This is compact. When passing from n to n+1, each new root label maps to its old root label: old roots map to themselves, and X_(n+1) maps to its root at time n. Every future site has old root equal to the image of its new root, by following its parent chain. Thus each old A_i is the union of the new A_j mapping to i. This union is finite, so closure commutes with it:

    K_i^(n) = union_{j mapping to i} K_j^(n+1).

If x belongs to two distinct old cells, choose a new cell containing x from each of their two groups. Those new cells have distinct labels. Therefore H_n is contained in H_(n+1).

### 2.2. The envelope equals the supremum over binary recolorings

For a binary assignment a:S_n->{red,blue}, future inheritance yields the closed red set union_{a(i)=red} K_i^(n), and similarly for blue. This follows from the descendant definition and closure of a finite union. Distributivity gives the exact identity

    F_(n,a) = union_{a(i)=red, a(j)=blue} (K_i^(n) intersect K_j^(n)).

It follows that F_(n,a) is contained in H_n. Conversely, for each pair i!=j, the assignment that colors i red and every other root blue puts K_i^(n) intersect K_j^(n) inside its frontier. Consequently H_n is the union of the singleton-red frontiers, a finite union.

Hausdorff dimension is stable under finite and countable unions. For completeness, if s exceeds the supremum of the dimensions of countably many sets E_k, then each has zero s-dimensional Hausdorff measure. For any delta,epsilon>0, choose a delta-cover of E_k of s-cost below epsilon*2^(-k-1); their union covers the union of the E_k with total cost below epsilon. This proves the upper bound on dimension; inclusion gives the lower bound. The same proof covers finite unions. Thus

    dim_H H_n = max_a dim_H F_(n,a),
    D_* := sup_n dim_H H_n = sup_{n,a} dim_H F_(n,a).

No closure of the countable union of H_n is taken. Adding that closure could increase dimension and would invalidate this identification.

The original coloring at time n is one of these assignments. Its future colors follow the same genealogy, so its frontier is exactly F_(n,a_n) for the actual time-n assignment a_n. In particular D<=D_*.

### 2.3. Measurability

All finite parent decisions are measurable inequalities between continuous distance functions (with any measurable deterministic tie rule on the null exceptional set). Root membership of every site is therefore measurable.

For an open set U relative to Q, K_i^(n) is contained in U if and only if there is an integer m>=1 such that every site of A_i^(n) has distance at least 1/m from the closed complement Q\U. The forward direction is compactness; the reverse follows by taking closure. If the complement is empty the assertion is automatic. The condition on all sites is a countable intersection of measurable conditions. Also K_i^(n) meets U if and only if A_i^(n) meets U, by openness and the definition of closure, a countable union of measurable conditions. These two types of events generate the Borel sigma-algebra of the compact hyperspace. Hence each K_i^(n) is a measurable compact set.

Finite intersections are measurable in that hyperspace. One explicit verification suffices: for compact K,L, K intersect L is contained in open U if and only if, for some m, their closed 1/m-neighborhoods in Q have intersection contained in U. If no such m exists, compactness gives a convergent sequence outside U with limiting point in K intersect L outside U. For each fixed m, containment can be tested by the minimum on the compact complement of U of the continuous function max(dist(x,K),dist(x,L)); equivalently this minimum exceeds 1/m. The distance functions depend continuously on nonempty compacts in Hausdorff distance. The empty-set cases are immediate. Taking the union over m proves measurability. These containment events generate the compact hyperspace Borel sigma-algebra as well: meeting an open set is equivalent to meeting one of countably many closed balls contained in it, with relative neighborhoods at the boundary. Finite unions are measurable too. Thus H_n is measurable.

Finally, for positive rational s, the event H^s(K)=0 can be expressed using countably many finite covers of K by rational-center, rational-radius open balls: for each k,l require a cover with diameters below 1/k and sum of diameter^s below 1/l. Finite covers suffice by compactness. Arbitrary Hausdorff covers can be enlarged into rational balls with bounded-factor cost increase, harmless for zero measure. Containment in each such finite union is measurable. The equivalence dim_H K<t iff H^s(K)=0 for some rational 0<s<t, for t>0, proves measurability of dimension and hence of D_*.

### 2.4. Finite permutations and zero-one

Let pi be any permutation of arrivals supported on {1,...,m}. For n>=m the set S_n is unchanged as a set of spatial sites. For each t>n, the location X_t and the entire set of earlier spatial sites are unchanged. Its nearest parent location is therefore unchanged, although a root's numerical label may have changed. Following parents until S_n is reached gives precisely the same partition into spatial root cells. Thus H_n(pi X)=H_n(X) for every n>=m.

Since H_n increases with n, discarding finitely many terms cannot change sup_n dim_H H_n. Hence D_*(pi X)=D_*(X). The measurable events {D_*<=q}, q rational, are invariant under all finite permutations of the iid arrivals. By the Hewitt-Savage zero-one law, every such event has probability zero or one. Since 0<=D_*<=d, this forces a constant: let c=inf{q rational: P(D_*<=q)=1}. For rational q>c, monotonicity and the definition of infimum give probability one; for q<c the probability is zero. Taking countable rational sequences above and below c gives D_*=c almost surely. This proves the proposition.

For d>=2 the source's Theorem 1.1 and D<=c imply d-1<c<=d. We do not assert c<d here: that would require checking a uniform upper bound over all finite root configurations, rather than merely strict upper bounds one configuration at a time.

## 3. A one-dimensional boundary case (full proof)

In d=1, for any r<b, the limiting frontier is a singleton almost surely, and its dimension is zero. Relabel colors if the seeds occur in the opposite order.

Inductively, every red site lies left of every blue site. Let L_n be the rightmost red site and U_n the leftmost blue site. An arrival x<L_n is closer to some red site (L_n already suffices for x between the extreme colors) than to any blue site; more precisely, if x<=L_n, distance to L_n is L_n-x and distance to any blue site is at least U_n-x>L_n-x. The case x>=U_n is analogous. If L_n<x<U_n, the nearest sites are L_n and U_n, so x is assigned red or blue according to which half of the gap it lies in. This preserves red-before-blue. Ties have probability zero.

The bounded monotone sequences L_n and U_n have limits L<=U. If L<U, a nonempty rational interval J contained in (L,U) contains an arrival by density. At its arrival time it is strictly inside (L_n,U_n). If colored red it exceeds the limit L, and if blue it is below the limit U. Both contradict the definitions of those limits. Therefore L=U=:Z. Limits of extreme sites show Z belongs to both color closures. Every red site is <=Z and every blue site is >=Z, so their closures can intersect only at Z. Thus F={Z} and dim_H F=0.

This resolves a boundary case, not the source's unresolved fractal question for d>=2. Proposition 3.8 in the source confirms the d>=2 scope of its strict lower bound, even though Theorem 1.1's introductory display does not repeat that restriction.

## 4. Hostile-referee checks and failed routes

1. **Wrong use of exchangeability.** H_n is invariant under sufficiently early permutations because it erases prefix colors. The original coloring does not erase those colors. Therefore the envelope proof cannot be copied to D. No invariance of D is claimed.
2. **Wrong use of independence.** The iid arrivals yield dependent descendant colors. Independent Poisson rain in disjoint boxes does not alone imply independently colored local frontiers: parent links can cross box boundaries.
3. **Closure trap.** Only finite unions commute with closure in the descendant decomposition. The countable envelope is taken via a supremum, never via closure of the union.
4. **Dimension trap.** Increasing compact sets can have dimensions whose supremum is less than the dimension of the closure of their union. Only countable-union stability, which was proved above, is used.
5. **Regeneration gap.** To show D=c by this route one would need to show that every original two-color process realizes dimensions arbitrarily close to the finite-recoloring envelope. No such statement follows from the finite algebra, and no local transplantation or regeneration argument was proved.
6. **Possible overstrong target.** D=c is sufficient for P0231, but may be stronger than necessary. D could conceivably be deterministic at a value below c. We do not claim equivalence.
7. **Literature gap.** Searches were bounded, and rate limits prevented an OpenAlex citation traversal. Absence of a matching result in the retrieved papers is not certification that the problem remains open everywhere.

There is a concrete positive-probability control for the history-dependence warning. In d=1 with seeds 0 (red) and 1 (blue), suppose X_1 lies in (.39,.41) and X_2 in (.67,.69). In that order X_1 is red and X_2 is red, since X_2-X_1<.30<1-X_2. In reverse order X_2 is blue and X_1 becomes blue, since X_2-X_1<.30<X_1. With the same dense future arrivals, Section 3 implies the first process has frontier Z>=X_2>.67 and the second has frontier Z'<=X_1<.41. Infinitely many subsequent arrivals in (.42,.66) therefore have different colors in the two processes. The event has probability .02^2>0. This proves that a finite permutation can change infinitely many colors and the limiting frontier itself. Both frontiers still have dimension zero, so it is explicitly not a counterexample to dimension determinism, nor proof that the dimension event fails to be a tail event.

## 5. Computation and formal verification

finite_checks.py checks 100 small independent random samples of the parent graph with 82 sites: finite-prefix permutation invariance of the spatial root partition, refinement mapping, and binary grouping algebra. It also checks color order in 20 one-dimensional samples with 500 arrivals. Seed 231; standard-library Python; memory far below 1 GB. These checks cannot determine Hausdorff dimension or establish any infinite-volume assertion. Results are in finite_checks.json.

FrontierAlgebra.lean formalizes exactly the finite existential distributivity identity used in Section 2.2. It imports only Mathlib.Data.Set.Basic, uses ordinary kernel-checked proof terms, and contains neither sorry nor native_decide. The command `lake env lean ~/brain_workers/TRIO_1011/op/P0231/FrontierAlgebra.lean`, run from ~/lean_verify, completed with exit code 0 and no compiler diagnostics after waiting for a shared slot. The analytical and probabilistic proof is written above, not formalized in Lean. The verification record is in lean_check.txt.

## 6. Precise remaining question

For each fixed distinct pair of seeds in [0,1]^d, d>=2, prove or disprove that dim_H(R intersect B) has a point-mass distribution. This attempt establishes deterministic D_* for the enlarged family of finite recolorings and D<=D_*, but establishes no lower bound D>=D_* and no independent argument for constancy of D. No counterexample in the Poisson-coloring model was found. VERDICT: PARTIAL.

One precise sufficient probabilistic estimate can be stated without assuming independent local copies. Put F_n=sigma(X_1,...,X_n). For each rational s<c, it would suffice to find a deterministic p_s>0 such that P(D>s | F_n)>=p_s almost surely for every n. Indeed, the bounded martingale P(D>s | F_n) converges almost surely to 1_{D>s}, since D is measurable with respect to the full arrival sequence. Its uniform lower bound would force 1_{D>s}>=p_s and hence D>s almost surely. Intersecting over rational s<c and combining with D<=c gives D=c. This uses the usual bounded conditional-expectation martingale convergence theorem; no such uniform lower estimate is proved here. In particular a positive *unconditional* probability is insufficient. Any use of regeneration must actually produce this strength of conditional probability, or another justified route to determinism.

## 7. Second attempt requested by the user

See SECOND_ATTEMPT.md for the two new approaches, full pursuit of the minimum-cut approach, proofs, and hostile-referee checks. New result: minimizing frontier dimension over finite-prefix recolorings that keep the original seeds opposite gives a decreasing sequence m_n, with m_0=D, whose limit is a deterministic beta. Thus beta<=D<=c. Each m_n equals the maximum bottleneck along a seed-to-seed path in the finite graph weighted by dimensions of limiting descendant-cell contacts.

An explicit Cantor-product partition of the cube shows that refinement can strictly decrease this minimum, while the inherited frontier retains a larger dimension. This refutes a topological shortcut, not the actual Poisson model. The remaining model-specific gap is threshold connectivity/universality strong enough to collapse the deterministic bounds, or another argument for constancy of D. The second attempt remains PARTIAL.
