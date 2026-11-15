# A bulk-coordinate bound, and why a fixed block cannot see it

This is a derivation from standard percolation arm estimates, written during this task. It is not a claim from Garban, Pete and Schramm about coordinate erasure entropy. It has been checked algebraically here, but has not had an independent referee.

Let f be the ±1 left-right crossing of the L by L rhombus. Keep i in a fixed compact subset of its interior; in particular, take the centre site used in mc_chain.py. Write δ = Inf_i, a(r) = α_4(1,r), and R_r = B(i,r) minus {i}. Changing from graph balls to square boxes changes only constants. Constants below are uniform in L and r, and may depend on the fixed shape and on the bulk margin.

The inputs are standard. Garban, Pete and Schramm give polynomial arm bounds and quasi-multiplicativity in equations (2.1)–(2.3), bulk pivotal probabilities comparable to α_4(L) in (3.1), and P[U meets B] ≤ 4 α_square(B,Q) in Lemma 3.2. Their Proposition 5.1 concerns a positive chance of a substantial sample inside a box, conditional on hitting a larger box and avoiding an arbitrary exterior set. It does not condition on the exact exterior spectral configuration. [The Fourier Spectrum of Critical Percolation](https://arxiv.org/html/0803.3750).

## Two bounds that cancel

For a sufficiently large fixed lattice scale r_0 and r_0 ≤ r ≤ cL, with a sufficiently small fixed c > 0, I obtain

    W(R_r) ≤ C δ a(r),                  V(R_r) ≤ C δ / a(r).             (1)

Here W(R) = P[i in U, U misses R] and V(R) = P[i not in U, U meets R], as in FLOW 12(l).

For W, use monotonicity to write D_i f as the indicator that i is pivotal. Let x and x' agree outside B(i,r) and have independent bits inside, with i omitted because pivotality is independent of x_i. If i is pivotal in both configurations, each configuration has four alternating arms in the inner annulus from a fixed lattice scale to r/2. The shared configuration has four arms in the outer annulus from 2r to d, where d is a fixed positive multiple of L lying inside the board. These three events concern independent sets of bits: two independent copies of the inner annulus, and one shared outer annulus. Omitting the intervening annuli only enlarges the event. Consequently,

    W(R_r) ≤ a(r/2)^2 α_4(2r,d)
           ≤ C a(r)^2 α_4(r,L)
           ≤ C α_4(L) a(r)
           ≤ C δ a(r).

The comparisons use fixed-ratio arm bounds, quasi-multiplicativity, and the bulk comparison for δ. There is no conditioning on the exact exterior spectral sample in this argument.

For V, use a connected box containing R_r and i, still of radius comparable to r. Then

    V(R_r) ≤ P[U meets B(i,r)]
           ≤ C α_4(r,L)
           ≤ C δ / a(r).

At the first fixed scale, V(R_r0) ≤ Cδ, also directly from the sum of the finitely many site influences. At a terminal interior scale r_* comparable to L, the W bound gives W(R_r*) ≤ Cδ². Thus one can finish the chain by jumping from R_r* to all the other sites, because V is always at most one.

Choose a geometric sequence of radii with bounded ratios. For consecutive radii,

    W(R_r) V(R_r_next) ≤ C δ² a(r)/a(r_next) ≤ C' δ².                  (2)

The final jump also satisfies (2). The empty spectral-set cell has q = fhat({i})² = δ² for a monotone Boolean function, so its product with any p mass is at most δ².

The two-sequence entropy lemma in FLOW 11(c), applied in reverse chain order as in 12(l), now bounds the entire nested witness by C''δ. Therefore

    E_i / Inf_i ≤ nested_ball_witness / Inf_i ≤ C'', uniformly in L.     (3)

No numerical value for C'' is certified here. The proof uses no exact arm exponent. Boards too small to contain the fixed starting radius form a finite set and are absorbed into the constant. It applies to a coarsened geometric ball chain; any refinement of that chain has no greater conditional entropy. For the chain in mc_chain.py, select radii at bounded ratios through a terminal interior scale, then use its final all-sites set. The additional geometric cardinality steps refine this subchain.

As a second check, (1) proves summability directly. A geometric shell has q mass at most Cδ a(r), p mass at most Cδ/a(r), and hence entropy at most Cδ a(r)[1 + log(1/a(r))]. The polynomial upper and lower arm bounds make this summable over geometric scales. The final shell has q ≤ Cδ², so costs O(δ² log(1/δ)) = O(δ). This reproduces (3) without the numerical constant in the two-sequence lemma.

This addresses a fixed bulk coordinate on unconditioned crossings. Arbitrary restrictions of crossings have different geometry and boundary conditions. Therefore (3) does not settle general FEI by the good-coordinate recursion.

## A fixed-radius block witness must grow

Fix a block B of b sites near i, independent of L, and let Z = U intersect B. For its empty-pattern atom,

    q_0 = P[i in U, U misses B] = E_y [(E_{x_B} D_i f)^2].

For monotone f, D_i f is a zero-one variable. Given y, its average t_y is an integer multiple of 2^(-b). Thus t_y² ≥ 2^(-b) t_y, and

    q_0 ≥ 2^(-b) δ.

Also,

    p_0 = P[i not in U, U misses B]
        ≥ 1 - sum_{j in B union {i}} Inf_j
        ≥ 1 - C_B δ,

because all finitely many sites stay in the bulk. Since δ tends to zero, Φ(p_0,q_0) ≥ q_0 log_2(1/q_0) plus a bounded-order adjustment. More directly, Φ(p_0,q_0) ≥ q_0 log_2(1+p_0/q_0), and this expression increases in both p_0 and q_0. Substituting their lower bounds yields

    H(1[i in U] | U intersect B) / δ
        ≥ 2^(-b) log_2(1/δ) - O_B(1).                                (4)

The trivial binary-entropy bound supplies an O(log(1/δ)) upper bound. Thus every fixed finite block witness is Θ_B(log(1/δ)); both radius-one and radius-two blocks eventually grow logarithmically. Since δ is comparable to α_4(L), the polynomial arm bounds make log(1/δ) comparable to log L. Its coefficient in (4) is deliberately crude. This is compatible with (3): the block discards the distance to the next spectral point outside it, while the nested ball witness retains that scale.

Prediction for the numerical experiment: the true ratio and a suitable nested ball witness remain bounded; a finite local block eventually grows. A window may reduce the finite-size witness gap, but is not required to remove a logarithm from the bulk percolation nested witness.

The GPS conditional clustering statement is consistent with this prediction, but is not by itself an entropy proof. Its exterior conditioning is an avoidance event, not the exact set U minus {i}; a fixed positive clustering probability would still leave room for a logarithmic contribution on the remaining mass. The argument above instead supplies the required decay of W through independent physical annuli and the complementary bound on V.
