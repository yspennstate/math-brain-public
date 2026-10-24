# Theorem 6 of Rozikov's problem list fails for five or more types: a strictly non-Volterra operator with two fixed points

Problem E0064 of the campaign ledger. Source: U. A. Rozikov, *Open problems on quadratic stochastic operators* (2009), Problem 11: "Is Theorem 6 true for m >= 4?", where Theorem 6 (Ganikhodzhaev, Mukhamedov and Rozikov's [40]) states that every strictly non-Volterra quadratic stochastic operator on three types has a unique fixed point, that this fixed point is not attractive, and that the operator has 2-cycles and 3-cycles depending on the parameters. A quadratic stochastic operator V on the simplex S^{m-1} is V_k(x) = sum_{i,j} P_{ij,k} x_i x_j with P_{ij,k} = P_{ji,k} >= 0 and sum_k P_{ij,k} = 1; it is strictly non-Volterra when P_{ij,k} = 0 whenever k is in {i, j}.

Written 2026-09-11 by the Claude agent claude-prob1000-0910. The earlier attempt E0064-A002 (2026-09-08) recorded that the non-attractiveness clause fails for m >= 4 (the symmetric equiprobable operator has a globally attracting fixed point, Jamilov, Ladra and Mukhitdinov 2017) and left the uniqueness clause open. This note settles the uniqueness clause for m >= 5 and reports what the search says about m = 4.

## The uniqueness clause is false for every m >= 5

**Example (m = 5).** Types 1, 2, 3 form a face F; types 4 and 5 are the rest. Define

- on the face, the symmetric operator: P_{ii,k} = 1/2 for i, k in F, k != i; P_{ij,k} = 1 for {i, j, k} = F;
- across: P_{i4,5} = 1 and P_{i5,4} = 1 for i in F; P_{44,5} = 1; P_{55,4} = 1; P_{45,k} = 1/3 for k in F.

Every row sums to one, P is symmetric in (i, j), and P_{ij,k} = 0 whenever k is in {i, j}, so V is a strictly non-Volterra operator on five types. Its coordinates are, for k in F with {a, b} = F \ {k},

    V_k(x) = (x_a^2 + x_b^2)/2 + 2 x_a x_b + (2/3) x_4 x_5,

and V_4(x) = 2 (x_1 + x_2 + x_3) x_5 + x_5^2, V_5(x) = 2 (x_1 + x_2 + x_3) x_4 + x_4^2.

Two fixed points, checked in exact rational arithmetic (`e0064_m5_exact.out`):

    p = (1/3, 1/3, 1/3, 0, 0):    V_k(p) = (1/9 + 1/9)/2 + 2/9 = 1/3 for k in F,  V_4 = V_5 = 0.
    q = (1/9, 1/9, 1/9, 1/3, 1/3): V_k(q) = (1/81 + 1/81)/2 + 2/81 + (2/3)(1/9) = 1/27 + 2/27 = 1/9,
                                    V_4(q) = 2 (1/3)(1/3) + 1/9 = 1/3 = V_5(q).

The point p is the fixed point of the face restriction, which is the symmetric strictly non-Volterra operator on three types; q has all coordinates positive. Their Jacobians on the tangent space of the simplex have eigenvalues (-2, -1, -1, 2) at p and (-4/3, -1/3, -1/3, 0) at q, so p is a saddle with index -1 and q has index +1; the eigenvalue 2 in the radial direction is Euler's identity for a degree-2 homogeneous map and plays no role on the simplex. Neither point is attractive (p has an eigenvalue of modulus 2; q has one of modulus 4/3).

**Every m >= 6.** Split the types into two disjoint triples F and G and choose any strictly non-Volterra operator whose pairs inside F land in F and whose pairs inside G land in G (pairs across the two triples may land anywhere allowed). The restriction of V to the face spanned by F is a strictly non-Volterra operator on three types, so by the source's Theorem 6 it has a fixed point in that face; likewise for G; the two are distinct. So V has at least two fixed points. Numerically (`e0064_face_construction.py`, 30 random operators of this kind on six types) the count was two in 27 cases and three in 3 cases, the third being a fully interior point. For m >= 7 pad with further types.

**Why the same trick stops at m = 5.** Two invariant triples must be disjoint, since a shared pair {i, j} would have to land in two different third types; so m = 5 admits at most one invariant triple, and the second fixed point has to come from outside the face, as in the example. For m = 4 a face-invariant operator has no fixed point outside the face at all: if F = {1, 2, 3} is invariant then V_4(x) = sum P_{ij,4} x_i x_j has no nonzero term (pairs inside F land in F, and pairs containing 4 cannot land on 4), so V_4 = 0 identically and every fixed point has x_4 = 0.

## What the search says about m = 4

Random strictly non-Volterra operators on four types, with all allowed entries positive (Dirichlet weights, 400 operators), sparse ones (Dirichlet concentration 0.1, 150 operators) and face-invariant ones (150 operators) all have exactly one fixed point in the simplex, found by Newton from 120 to 150 random starts and deduplicated at 1e-7 (`e0064_fixed_point_search.py`, `e0064_face_construction.py`). The same for 150 random operators on five types without an invariant face, and 191 of 200 face-invariant five-type operators; the other 9 had two fixed points, one in the face and one interior, which is what led to the example above. So the uniqueness clause of Theorem 6 appears to survive at m = 4 and fails from m = 5 on. A proof for m = 4 is not attempted here; the natural route is an index count (every fixed point of index +1 forces uniqueness), and the five-type example shows that the count can involve a saddle of index -1, so the argument would have to use the dimension.

## Answer to Problem 11, as it now stands

Theorem 6 does not extend to m >= 4. Its non-attractiveness clause fails from m = 4 on (E0064-A002, with the 2017 literature reference); its uniqueness clause fails from m = 5 on (this note, explicit rational example at m = 5 and the two-face construction for m >= 6). At m = 4 uniqueness is unresolved and numerically supported. The cycle clause (2-cycles and 3-cycles in higher dimensions) is not addressed here.
