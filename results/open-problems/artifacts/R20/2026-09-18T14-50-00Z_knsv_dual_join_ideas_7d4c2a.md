# R20 KNSV next-route ideas before checker

Model request in task text: GPT-6 / maximum. Actual runtime model: GPT-5.6 Sol; reasoning telemetry UNVERIFIED.

Current target is the exclusive R20 claim `operations/claims/KNSV-2026-LOOPY-U.md`, not retired Paley I0100. Frozen metric remains `N_sep > 11`.

This note records the ideas before the new exact checker artifact.

## #11 DUALIZE — test whether the first hidden `(4,3)` statistic is a linear consequence of ordinary U

The previous run reduced the first nonautomatic block profile to

`h_r(G) = sum_{B,C disjoint, |B|=4, |C|=3} a_{r-1}(B) beta_C`,

where `C_G(B;q)=q^3 sum_j a_j(B)(1+q)^j` and `beta_C=1` exactly when `G[C]` is a triangle.  For `n=7` there are no outside singleton vertices, so `h_r` is a graph function on seven-vertex simple graphs.

A universal local-linear reconstruction from ordinary U would force `h_r` to lie in the Q-linear span of the ordinary-U coefficient functions `(lambda,cyclomatic-number)` on the finite set of seven-vertex graph types.  This can be attacked by exact linear algebra on all 1044 unlabeled seven-vertex simple graphs (NetworkX graph atlas is only a convenient enumeration source; the final certificate should be self-contained).

The exploratory exact calculation found 67 ordinary-U coefficient coordinates occurring at n=7 and a rank jump from 67 to 68 after adjoining each of `h_1,h_2,h_3` modulo the prime 1000003.  More importantly, it found a small exact integer dual relation for `h_1`: a signed multiset of twelve graph types whose total ordinary-U polynomial cancels but whose total `h_1` does not.  The checker should verify that relation directly over Z from graph6 strings, without relying on the atlas or modular rank computation.

If verified, this does **not** refute Conjecture 8.2: there is no pair of seven-vertex graphs with equal U.  It rules out the most obvious proof route in which `(h_1,h_2,h_3)` is recovered by a universal linear combination of local U coefficients and then summed over seven-subsets.

## #19 MAKE IT AN ALGORITHM — use the hidden vector as a cheap exact separator filter

For any actual U-collision pair, a discrepancy in `(h_1,h_2,h_3)` is already enough to prove `L(1,x)` differs, because the `(4,3,1^{n-7})` transformed block layer depends injectively on those three hidden coordinates once the ordinary layer `S_(4,3,1^{n-7})` is fixed.  Thus future collision searches should compute the hidden vector before full L.

The source appendix gives an O(3^n) connected-block subset recursion and reports its collision data/code at Zenodo DOI `10.5281/zenodo.21929427`.  Direct Zenodo access is not currently available from the web surface used in this run, so no claim is made about reusing the authors' files.  The mathematical filter itself is independent of that access.

## #24 FIND THE EXTREMAL OBJECT — eliminate join-generated n=12 candidates structurally

The source proves that ordinary-U collision classes are preserved under joins.  At first sight this makes the known n<=11 collision classes a natural source of guaranteed U-collisions at the first open order n=12.

But there is a stronger refined closure.  Equality of the extended U-polynomial is preserved under complement: under the equivalent extended polychromate, each block statistic `(s,e)` is sent by complement to `(s, binom(s,2)-e)`, an invertible blockwise substitution.  Extended U is multiplicative under disjoint union.  Therefore, if `U_ext(G)=U_ext(H)`, then for every fixed simple J,

`U_ext(G vee J)=U_ext(H vee J)`.

Since ordinary loopy L is a specialization of the refined/extended invariant, `L(G vee J)=L(H vee J)` as well.

The source's Proposition 8.6 says that through 11 vertices the ordinary-U and extended-U collision partitions coincide.  Hence **no n=12 counterexample obtained by joining a fixed graph to any known <=11 ordinary-U collision can separate L**.  This removes the entire obvious join-generated extremal family, rather than checking one or two joins numerically.

The next checker will validate only the finite dual relation above.  The refined join-closure statement is a symbolic argument and must remain SELF-CHECK ONLY until independently audited.
