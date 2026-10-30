# T186-Z-C009 v1 — composition at c0 = 6981/500

Kind: narrowed. Target: 1 (subtarget 1b). Status: proof (unaudited).

For every fixed c >= c0, the normalized circumference of G(n,c/n) converges almost surely to a deterministic limit f(c). The function f is continuous on [c0,infinity), is nondecreasing, and satisfies

    0 <= f(c+epsilon)-f(c) <= 16 epsilon/c,  0<epsilon<=10^-3.       (1)

For fixed c in this range the other two assertions of Anastos Theorem 1.1 also follow: with high probability all integer lengths L(G)-j, 0<=j<=0.1 c^3 exp(-c)n, occur, and the longest-path/circumference discrepancy is at most 2000 log(n)/c+1. No uniform claim for a parameter c growing with n is made here. The open fixed-parameter interval for the scaling-limit question would shrink from (1,20) to (1,6981/500) if this composition passes both required audits. This is not a claim that those audits have happened.

The hardest composition issue is the matching/exposure interface. The Hamiltonicity statement proved below is the restriction of source Theorem 3.3 to path-derived matchings measurable from red-incident edges, together with the empty matching on the black core. These are all the applications required for Theorem 1.1. The unrestricted assertion for EVERY arbitrary blue matching is not proved here: Appendix B itself uses a realization by red/blue paths. This distinction is explicit, rather than treating the stronger source statement as a passed input. Auditors should judge the stated scaling-limit theorem and this precise interface.

Primary source: M. Anastos, arXiv:2105.13828v5, Sections 3-6 and Appendices A-B. The previous sufficiently-large-c theorem of Anastos-Frieze, arXiv:1907.03657, is background, not a small-c Hamiltonicity input. No result from its c>=10^6 machinery is imported. The source's primary locators below refer to the printed PDF page numbers.

## 1. Exact passed premises; no numerical input is re-derived

| ID and version | Role in this proof | Proof file / SHA256 |
|---|---|---|
| worker X T186-C003 v1 | Decaying component bound, maximum component size, red and nonblack mass, all at c>=c0 | worker X/T186/proofs/C003_birth_forest_bound.md / 877aa61ba1176842976a557e7a56e047c95c28456f23870483286ee1f17a7cbf |
| T186-Z-C001 v2 | Source c-ledger and scalar/source readings; NOT the excluded Lemma 4.2 scope note | archives/C001_ledger_v2_recovered.md / 305682d79cca8d6c8351f7e40968eb6ebd79eea0225590cf383116d20c466ff9 |
| T186-Z-C003 v1 | Uniform black-core density and the reserve size / exceptional-endpoint bounds | proofs/C003_sampling_c0.md / 9358216f6506b0eeda0ddb93189e19b0f89658497dac4db39bad94e1f7bd37ca |
| T186-Z-C004 v2 | Rotation density and neighbourhood obstructions, using eta=c^-12 | proofs/C004_v2_rotation_density_c0.md / 95af00660bdeb04db8672c0c4127609182c23a7abe7ce2e06ca25b9bb7e67e74 |
| T186-Z-C006 v2 | The large-set matching obstruction; corrected exponent | proofs/C006_v2_matching_c0.md / d3e8df2cf9f4062fff482a5c1811b5747877f89fa42b2b904e9d5bbc8bad8d06 |
| T186-Z-C007 v1 | Alternative partition bound for c>=15, with stronger omitted-set scope; not extrapolated below 15 | proofs/C007_P2_15.md / 97b758887e8f0e8580d61aeb15db78cdcbd25b27468c054c4139780fbd2eb8bd |
| T186-Z-C008 v2 | Actual-colouring forbidden-partition bound for all fixed c>=c0, including small and medium sets | proofs/C008_v2_P2_c0.md / 2fd36042bf09e06356c32467f761cad98b588fa3abc92a4975634b94ddb35750 |
| T186-Z-C005 v2 | Conditional local approximation, Cauchy-limit argument, and sprinkling estimate (1) | proofs/C005_v2_local_approximation.md / 91522869bb9d066997b61ba01a7b44372c90141264f014ad6984d05ff386fa26 |

Each of these exact versions has the reviewer's PASS in the corresponding audit ledger. This does not transfer that status to C009. Some old proof headers still say unaudited; the exact-version audit rows are authoritative. The scope of each premise remains as stated there.

Write R,B,K for the actual Algorithm 1 red, blue and black sets. The worker X input gives, for fixed c>=c0, outside o(n^-2),

* |R union B|<=d(c)n, d(c)=c^3 exp(-c)<0.01;
* every red/blue component has order at most 1000 log(n)/c;
* the decaying bound X_i<=n(4/5)^i/(ci)+n^0.55, through log^3 n, where X_i counts vertices in red/blue components of order i;
* at most 0.03 c^3 exp(-c)n red vertices lie in components with at least two red vertices.

Every remaining vertex has at least four neighbours in K, and there is no R-K edge, deterministically by Algorithm 1. Fixed c eventually lies in both upper-c ranges of worker X's statement. No mass assertion uniform through 2 log n is used.

## 2. A canonical family that does not reveal the reserve

Use source Notation 4.1: phi(T) is the minimum number of red vertices missed by disjoint paths with blue endpoints in a red/blue component T; singleton blue paths are allowed. An optimal family can be chosen using only the colours and edges incident to R. To see this, remove every blue-blue edge of any optimal family. This only splits paths at blue vertices, preserves disjointness and loses no red coverage. Add every uncovered blue vertex as a singleton. Conversely, such a family is also allowed in the full red/blue graph. Thus the optimum is unchanged by discarding all blue-blue edges. Choose a canonical optimum in this smaller graph, by deterministic tie-breaking, and call it P*. This construction works globally even when blue-blue edges join several smaller components: the optimum is additive across components after those edges are discarded.

For any subfamily P of P*, let U(P) be its internal blue vertices, and replace each positive-length path by an edge between its two blue endpoints, obtaining a matching M(P) on B minus U(P). Singleton blue paths produce no loop. Interiors of realizing paths are disjoint from one another and from the retained vertices K union (B minus U(P)). Consequently a Hamilton cycle on those retained vertices containing M(P) expands to a simple G-cycle. All of P*, U(P) and M(P) are measurable from the colours and red-incident edges. They need not inspect whether a blue-blue or black-black reserve pair is present in G.

## 3. Reserve law with its full exposure information

Independently mark each present G-edge with probability p'=1/(c log log n). Let J be the graph of unmarked edges; its unconditional law is G(n,q), q=(c-1/log log n)/n. Fix one of the path-derived pairs U,M above, or U=B,M=empty for the black-only cycle. Let H=G[K union (B minus U)], H1=J[V(H)], and

    V1={v in V(H): d_H1(v,K)<4}.

Reveal all H-edges incident to V1. Put H'=H1 union those revealed edges, and E1=E(H) minus E(H'). Thus H' retains four black neighbours at every retained vertex. Defining V1 using H1 is essential: the literal p.11 sentence omits the graph qualifier, while all vertices already have four black neighbours in H. The H1 interpretation is also the one used by Appendix A's marked-degree proof and by C003.

Here is a detailed justification of the conditional uniformity used on source p.11. Condition on J, the colours, all red-incident G-edges, all G-edges outside H, the H-edges incident to V1, and e1=|E1|. The canonical U,M are then fixed. The candidate set for the unrevealed reserve is

    C = binom(V(H) minus V1,2) minus E(H').

For each pair absent from J, the unconditional conditional probability of a marked present edge is

    theta=(p p')/[1-p(1-p')],   p=c/n,

independently over pairs. Every subset T of C of size e1 is compatible with the specified colours: changing these pairs changes no red-incident edge, and all nonred vertices continue to have four black neighbours. For vertices outside V1 those four witnesses already belong to J; for V1 all incident edges are fixed. The original red-peeling sequence is therefore still legal with the same red-incident edges, and the same terminal colouring has no eligible nonred vertex. Equivalently, throughout that sequence final black vertices remain black, and their four witness neighbours prevent any final nonred vertex from becoming red. This also proves invariance of V1, U and M under the change.

Hence each T has the same remaining product weight theta^e1(1-theta)^(|C|-e1). The reserve is a uniformly random e1-subset of C conditional on this enlarged information. Conditioning on fewer items is unnecessary; this enlarged law is the law actually used below. In particular no assumption that the colouring or M is independent of G is made.

C003 supplies, outside o(n^-2), |V1|<=10n/log log n and e1>=n/(1000 log log n). These bounds can be made common to all blue deletions U in this argument. Choose four black-neighbour witness edges for every original nonred vertex before assigning marks. The black set alone spans at least 0.4cn edges on C003's uniform density event; removing at most 4n witnesses leaves the same reserve count proved in C003. Every marked, unprotected black-black edge of marked-degree one at its endpoints survives every blue deletion and lies in E1. V1 is contained in the global set of marked endpoints. Thus a union bound over U is not charged to an o(n^-2) sampling error.

## 4. The missing short-cycle interface

Let L=floor(sqrt(log n)) and h=floor((log n)^(1/10)). A family of disjoint cycles in H' union M expands, using Section 2, to disjoint G-cycles. Every light cycle of length at most L, whose realizing paths all lie in red/blue components of order at most h, expands to length at most Lh <= (log n)^(3/5). A heavy cycle uses a vertex in a red/blue component larger than h. Distinct heavy cycles use distinct such vertices.

Thus, simultaneously for every subfamily of P*,

    packing_{<=L}(H' union M)
       <= packing_{<=(log n)^(3/5)}(G) + mass_{>h}(G_red/blue).    (2)

The second term counts vertices, not components. The printed Appendix B inequality Z_H<=X_{>=h}, with X counting components, fails when two disjoint realizing paths in the same component support two disjoint cycles; the weighted bound (2) is the repair.

The reviewed component estimate and the logarithmic component maximum give

    mass_{>h} <= O_c(n(4/5)^h)+O_c(n^0.55 log^2 n)
              =o(n/sqrt(log n))

outside o(n^-2). This bound deliberately weakens the direct sum of the vertex counts: summing the n^0.55 errors over O_c(log n) sizes is already smaller than the displayed logarithm-squared allowance.

For the first term of (2), the expected total number of ordinary G-cycles of length at most (log n)^(3/5) is n^o(1), by the elementary cycle count for fixed c. The maximum disjoint packing changes by at most one when an independent upper-triangular adjacency row is changed, because every changed edge is incident to that row's vertex. Bounded differences at deviation n^(3/5) bounds its exceptional probability by exp(-2n^(1/5)). Therefore this packing is o(n/sqrt(log n)) with a summable exceptional probability. For all sufficiently large n, (2) is less than n/L. The same bound holds for H' and every blue-deleted induced subgraph. This is a COMMON event for all the path-derived matchings used below, rather than a separate o(n^-2) event per path family.

## 5. Theorem 3.3 at the interface actually needed

Here is the replacement event map for source Lemmas 6.1-6.6.

| Source event/input | Exact payment at c>=c0 |
|---|---|
| Esample, Section 6.1 / Lemma 6.1 / Appendix A | C003 v1 plus worker X T186-C003 v1; conditional reserve law is Section 3 above |
| Appendix B (P1) small-set witness count, original r/s caps and small-set (P2) | C008 v2 Sections 1-4 for actual colourings, retaining four black neighbours |
| Medium-size Appendix B (P2) | C008 v2 Section 5, through size 2n/5 |
| Large-size (P3), originally size 0.3n | C006 v2 and C008 v2 Section 6 at size 2n/5; use the corrected matching exponent |
| P(k,l,0)'s short-cycle clause; added-M short cycles | Section 4 above, including the weighted heavy-cycle repair |
| Eexp(i), at most twelve vertices | C004 v2's small-set estimate |
| Eexp(ii), forbidden density on 5<=|S|<=eta n | C004 v2's dense-set estimate, eta=c^-12 |
| Eexp(iii), no S with <=2|S| outside-blue neighbours on eta n<=|S|<=10^-30 n | C004 v2's repaired black-endpoint count, including B minus S in R, with o(n^-2) core failure |
| Tutte-Berge, the two matchings, and rotations | Deterministic Lemmas 6.2, 6.4, 6.6, with the interfaces and cutoff checked below |

C007 v1 provides an alternative stronger omitted-set partition count when c>=15. C008 v2 replaces it on [c0,15); no application below 15 relies on C007.

C008 applies to H' and H'[V(H') minus W] for every W subset B minus U: these graphs contain all K, retain four K-neighbours, and delete only marked edges relative to their induced G-graphs. Thus their forbidden-partition clause is excluded on one common event. Section 4 supplies the cycle clause. Apply deterministic Lemma 6.2 to H' minus M. In the second application the vertices incident to two edges of M union M1 are blue, so deleting them is an allowed blue deletion. The resulting two-matching construction of Lemma 6.4 gives a cover by at most 4n/L vertex-disjoint paths containing every M-edge. Removing a cycle edge can always avoid M, since M is a matching. This invokes no additional c-dependent estimate.

Check the adjusted rotation range, rather than assuming it. Set eta=c^-12 and epsilon0=10^-30. The deterministic admissible-rotation argument on pp.14-15 uses four retained black neighbours and never deletes M. It gives at least four reachable endpoints. Four endpoints contradict Eexp(i)'s <=12-vertex estimate. Between five and eta n endpoints, the pivot union has at least 1.5|S|+|T| edges with |T|<=2|S|, contradicting C004's density event. If eta n<|S|<=epsilon0 n, the deterministic bound |N_H'(S) minus B|<=2|S| contradicts C004's neighbourhood event. When eta>=epsilon0 the density event alone suffices. Thus both endpoint sets in the two-stage rotation have at least epsilon0 n vertices for each fixed c. The consistent cutoff is eta throughout. The good event is absence of the <=2|S| neighbourhood obstruction; the <= sign in the printed definition is not imposed as a good property.

Conditional on the phase-zero information in Section 3 and these structural properties, the source algorithm has at least (epsilon0^2/2+o(1))n^2 unordered closing pairs at every unsuccessful iteration. Discard V1, H'-edges and previously revealed reserve pairs. The first costs o(n^2); for the latter impose the phase-zero measurable bound |E(H')|+e1<=n log^2 n, whose unconditional failure is superpolynomially small by the usual maximum-degree estimate. Thus it too costs o(n^2). Consequently at least epsilon0^2 n^2/4 available closing pairs remain for all sufficiently large n. A uniformly revealed reserve pair has conditional success probability at least epsilon0^2/4, a deliberately weakened positive constant. All structural good properties needed here are measurable from the phase-zero information H', colours and the realizing paths; underlying G/component estimates were used to bound their unconditional failure probabilities, not to condition the reserve on hidden edges.

The extension-rotation procedure needs at most 4n/L successful closings. There are at least n/(1000 log log n) reserve trials. Their product with the above positive success lower bound dominates 4n/L asymptotically. Adaptive lower domination by Bernoulli trials, followed by Chernoff, bounds failure by exp[-Omega(n/log log n)], conditional on the phase-zero good data. Independence of successive success indicators is not asserted. Unused trials may be assigned success value one once the algorithm has finished. Each closing removes an artificial joining edge, while admissibility preserves M, exactly as in Section 6.3. The output is a Hamilton cycle in H union M containing M.

We need only at most n+2 canonical subfamilies of P*: the full family, and the families obtained by deleting the first j paths each covering exactly one red vertex, plus the black-only empty-matching application. Their structural failure events are common. Union-bounding their conditional exponential algorithmic failures still gives o(n^-2). No factor n is multiplied into an individual o(n^-2) structural estimate. In particular a black-only cycle has at least (1-d(c))n vertices, and all the path-derived applications hold with probability 1-O(n^-2).

## 6. Corrected Lemma 4.2 and the cycle-deficit identity

For a colouring with no red-black edge, Lemma 4.2's upper bound is valid for any cycle not wholly contained in one red/blue component. Indeed its intersection with each such component is a disjoint union of paths with blue endpoints: an edge leaving that component goes to black, so its endpoint cannot be red. The red vertices not covered number at least phi(T). Sum this over components. The unrestricted lemma as printed has the all-red triangle counterexample, so the restriction must be checked in the application.

On the common good event of Section 5, the black-only cycle has length >=(1-d(c))n, which is greater than the maximum red/blue component size 1000 log(n)/c for all sufficiently large n. A longest cycle therefore cannot lie wholly inside any red/blue component. The upper bound applies without using the identity we are about to prove.

For the reverse inequality use P* from Section 2. Expand the Hamilton cycle containing M(P*) from Section 5, reinserting all internal blue and covered red vertices. It covers every black and blue vertex and all but sum_T phi(T) red vertices. Hence, with probability 1-O(n^-2),

    L(G)=n-sum_T phi(T).                                        (3)

This closes Theorem 4.3's identity at c0, including the excluded scope note of C001 v2. Removing the first j single-red paths before the Hamiltonicity application yields cycles of length L(G)-j. A singleton-red component containing a degree-three vertex admits a blue-red-blue path covering that vertex; choose such an optimum for these components in the canonical tie-breaking. The reviewed multi-red mass bound and the standard fixed-c degree-three count imply at least (1/6-0.03)c^3 exp(-c)n+o(n)>0.1c^3 exp(-c)n such paths with high probability. This proves the fixed-c form of Theorem 1.1(b). Similarly, cutting a path at its first and last red/blue components costs at most twice the maximum component size. Together with (3) this gives the fixed-c form of (c), with the harmless +1 convention for path length.

## 7. Section 5: discharge C005 v2's local hypotheses

The component hypotheses of C005 v2 are exactly the reviewed worker X input, and (3) supplies its formerly conditional cycle identity. Its deterministic local-colouring comparison is source Lemma 5.2. The remaining inputs, fixed-radius limits and summable concentration, have no large-c condition. Here is an explicit local-limit formulation that avoids any ambiguity in the source's displayed expectation calculation.

Fix an integer radius k. The truncation defining phi_k gives a FINITE set of rooted trees T. Write t=|T|, a=|{v:dist_T(root,v)<k}|, and A=aut(T,root). The probability that the induced rooted k-ball is T is exactly

    (n-1)_{t-1}/A * p^(t-1)
      * (1-p)^[a(n-t)+binom(t,2)-(t-1)],                        (4)

where p=c/n. Edges from depth-k boundary vertices to outside the ball are unrestricted; edges from the interior to outside are absent. Therefore (4) tends to c^(t-1) exp(-ca)/A. The same limit follows by multiplying the Poisson(c) offspring probabilities of the interior vertices and accounting for root-preserving automorphisms. This is an independent description of the same finite-ball marginal. If a finite-ball formula omits the exterior absence term, it counts tree embeddings rather than balls; (4) is the expression used here.

It follows that n^-1 E[L_{c,n,k}] converges to the finite sum 1-sum_T phi_k(T)c^(t-1)exp(-ca)/A. Fixed-radius rooted-ball counts concentrate with summable failures as in source Lemma 5.4 and Lemma 2.1: on maximum degree <=log^2 n, changing a vertex's incident edges affects only O_k(log^{2k+2}n) eligible rooted neighbourhoods. The maximum-degree failure is superpolynomially small for fixed c. Thus the source typical bounded-differences argument applies with a fixed-k polylogarithmic change bound, a bounded statistic in [0,n], and no lower threshold on c. The same fixed-radius short-cycle neighbourhood estimate pays C005's Y_k term.

C005 v2 now applies with all its hypotheses supplied. For fixed admissible k, its normalized error is at most

    a_k(c)+o(1),   a_k(c)=5(4/5)^k/(ck)+1/(9c^2 k^3),           (5)

outside a summable event. The geometric step requires c^2 k^3>=10, as in C005 v2, and this holds for every k>=1 on the present range. Take n to infinity FIRST for each fixed k and fixed c, then k to infinity. Since a_k(c)->0, the deterministic finite-radius limits are Cauchy, and their limit f(c) is the almost-sure limit of L(G)/n by the triangle inequality and Borel-Cantelli. No independence of the graphs at different n is required for this use of the summable bounds.

## 8. Discharge the component-hit hypothesis; continuity

Use the exact C005 v2 coupling: independently G1~G(n,c/n), H~G(n,epsilon/(n-c)), and G2=G1 union H. The G2 marginal is exactly G(n,(c+epsilon)/n). Cycles persist pathwise, so f is nondecreasing.

For the upper comparison take G1's strong-core colouring and recolour entirely black every red/blue component touched by an endpoint of H. No red-black edge exists in the resulting colouring of G2: an old edge cannot run between two different red/blue components, and an untouched red vertex is incident to no H-edge. The surviving red/blue components are precisely the untouched old ones, with unchanged phi. The black-only cycle of G1 persists in G2 and is longer than every surviving component. Thus the corrected Lemma 4.2 from Section 6 applies to a longest G2-cycle. On G1's identity event it gives

    0<=L(G2)-L(G1)<=sum_{T touched by H} phi(T)
                       <=sum_{T touched by H}|T|.              (6)

This proves the exact deterministic component-hit hypothesis of C005 v2. It uses no monotonicity of the strong-core colours under edge addition. That claim's exact sprinkling marginal and weighted component expectation now give (1). For each compact valid parameter interval with left endpoint b>0 the Lipschitz constant is 16/b. This establishes continuity at c0 from the right and throughout the whole claimed range. Extending f constantly on [0,c0] gives the domain convention of source Theorem 1.1(a).

## 9. Complete c-ledger replacement and source repairs

All c-dependent steps relevant to Theorem 1.1 are paid as follows. Lemma 3.2's geometric base, the finite red counts, degree-0..3 budget, total red bound and total nonblack bound are replaced together by worker X T186-C003 v1. Appendix A's core size, density, Chernoff coefficient and subtraction of four protected edges are replaced by C003 v1. Every Appendix B exceptional-set ratio cap, the small-set witness inequality and both medium-set endpoints are replaced by C008 v2; its large-set step uses C006 v2. The guarded large-c neighbourhood clause and the inconsistent density cutoff in Lemma 6.5 are replaced by C004 v2. The Section 5 tail allowance, its Z_k geometric condition and continuity's constant are replaced by C005 v2 after Sections 6-8 above. Lemma 1.3's auxiliary degree polynomial is not needed for (a)-(c); Theorem 1.1(b)'s 1/6-0.03>0.1 has no new c restriction. The conditional reserve and finite-ball facts above have no large-c assumption. The source's 1907.03657 historical machinery and Theorem 1.2 pancyclicity sprinkling are not premises of Theorem 1.1.

For clarity, the repairs used are stated once in this list, with their scope:

1. Lemma 3.2(c), p.5, loses a factor at least 32 in the degree-six term; worker X C003 v1 replaces that calculation, as well as the p.6 shifted geometric-tail budget. Use the DECAYING (4/5)^i component bound, not the printed negative exponent.
2. Lemma 5.2, p.9, has an invalid small-k tail budget; C005 v2 uses the convergent error (5), with c^2 k^3>=10 for its finite geometric sum. Continuity uses 16/c, not a presumed <=1 bound below 16.
3. Lemma 6.5, pp.13-14, has inconsistent c^-5/c^-9 cutoffs and loses a factor c in its substitution; C004 v2 consistently uses c^-12 and the repaired black-to-black neighbourhood count. Its good neighbourhood event excludes the <=2|S| obstruction.
4. Appendix B's P2 at c0 uses C008 v2, not the printed 0.17 cap or its two endpoint bases. Its matching exponent is C006 v2's corrected expression, not C006 v1's missing-factor expression.
5. Appendix B's added-matching short-cycle claim is used only at the realizable path interface and with weighted heavy-component mass as in (2). This is why the unrestricted arbitrary-matching Theorem 3.3 is not asserted here.
6. Lemma 4.2 is applied only after the linear black-only cycle excludes containment in one red/blue component. Its general printed formulation has the all-red triangle exception.
7. Section 6.1's low-neighbour exceptional set is measured in H1, and the reserve law is justified with the enlarged sigma-field of Section 3. Fixed-radius balls use the full finite-graph probability (4), including the exterior absence factor.

The finite set of common structural failures is O(n^-2); the additional finite-radius failures are summable for each fixed k; and the at-most-n adaptive Hamiltonicity applications have conditional exponential failure. This gives the probability orders needed for (3), the almost-sure scaling limit, and the fixed-c additional conclusions without silently multiplying conditional probabilities.

## 10. Audit and measurement boundary

The scripts/verify_composition_102.py log checks the finite deterministic bridges and conditional-product calculation, including deliberate failures of the unqualified Lemma 4.2 and of the component-count heavy-cycle bound. It does not certify the asymptotic probability proof or substitute for its two audits. Input hashes are checked separately in the composition dependency manifest. No new floating estimate is used as a bound. No Lean proof of C009 is claimed.

Required reviewers: worker S and agent P, for THIS exact v1 hash. Particular attention is requested on: the path-derived interface versus arbitrary M; the colour-invariance argument in the reserve conditioning; the common-event probability accounting; the weighted heavy-cycle replacement; the Lemma 4.2 scope; and (4)'s local-ball marginal. A full unrestricted Theorem 3.3 remains outside this proof. Do not record the T186 move until the two C009 PASSes required by the lead exist.
