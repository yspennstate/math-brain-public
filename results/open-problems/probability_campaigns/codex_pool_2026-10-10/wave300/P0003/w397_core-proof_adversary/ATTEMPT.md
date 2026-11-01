# P0003: core-proof adversary attempt

Author: w397. Date: 2026-10-10. The fixed-length target remains unsolved here; present openness is UNKNOWN. No novelty assertion is made.

The exact historical question is Grimmett, *Selected problems in probability theory*, arXiv:2205.07318v1, Question 2.2, page 3: "Does a uniformly distributed n-step SAW from the origin of H converge weakly, when suitably rescaled, to the Schramm–Loewner random curve SLE8/3?" H is the hexagonal lattice. This question does not specify the rescaling, SLE geometry, stopping rule or topology completely. Those choices cannot be silently replaced by a critical chordal measure.

w396's statement packet selects a useful related subproblem: critical variable-length honeycomb walks from a to b in a bounded Jordan domain, converging as unparametrized chordal curves. That is the separate formulation of Duminil-Copin--Smirnov, arXiv:1007.0575v2, Conjecture 1, page 9. It is a legitimate research route, but no equivalence to Grimmett's uniform n-step question has been proved in this packet.

The corrected fixed-length route isolates H_disk. With the operational conjectured scale s_n=n^(-3/4), a fixed disk A centered at z with radius r<|z|, and its concentric (1+epsilon)r collar B_epsilon, let Delta_n(epsilon) be the probability that a uniform n-step walk's rescaled trace avoids A but enters B_epsilon. The missing input is limsup_(n->infinity)Delta_n(epsilon)<=C(z,r)*epsilon^alpha for some alpha>0 and all sufficiently small epsilon. The first-entrance injection(U) in the paired packet gives an exact positive counting upper bound but no sufficient estimate of mutually avoiding pieces. H_disk is UNPROVED, as are H_len (identification from length-resolved kernels), ordered-curve tightness, and the scale/continuum conventions.

The related chordal route still has its separate H_5/8 gap: positive partition ratios should approach (|f_A'(a)||f_A'(b)|)^(5/8). The local identity and finite martingale manipulations supply neither this law nor the fixed-length estimate. A reduction assuming either input is not a proof of P0003.

## Independent obstruction to the observable route

INDEPENDENT.md was saved before any paired proof was read. It constructs an exact interior face circulation H with unchanged boundary data, sup norm 1 and adjacent jumps 1 at distance sqrt(3)*delta/2. Thus the vertex equation alone has a compactly supported kernel and cannot give uniqueness or local uniform compactness, even with uniform boundedness. This specifically tests the hardest analytic step in an observable-based attempt.

Primary-source check: Duminil-Copin--Smirnov, Definition 1 and Lemma 1, page 2, use F(z)=sum_gamma exp(-i*(5/8)*W_gamma) x_c^ell(gamma), x_c=1/sqrt(2+sqrt(2)), and precisely sum_(p adjacent v)(p-v)F(p)=0. Their page 10 already explains that the relation is insufficient for existence of a scaling limit. The finite witness is an independent explicit illustration of that known obstruction, not a newly discovered obstruction to the SAW conjecture.

For the witness, the primal-face contour defect is also explicit:

    sum_(j=0)^5 (v_(j+1)-v_j) H(p_j) = 6*delta.

In contrast, a family locally uniformly approaching a continuous function must have this sum o(delta), because the six edge increments sum to zero. This gives a concrete necessary anti-circulation condition. Suppressing this one mode is not by itself sufficient for compactness. A quantitative modulus of continuity, uniform over the required edge orientations and domains, is still needed for the true normalized walk-sum observable.

Proposed hard lemma to attempt next: for each compact K away from the marked source and boundary, the normalized genuine observable has a bound C_K and a mesh-independent modulus omega_K(r) tending to zero, such that its magnitude is at most C_K and its difference on any two edge midpoints within distance r is at most omega_K(r)+o_delta(1). A proof must use constraints of the true walk sums beyond the homogeneous vertex equation, and specify any uniformity over slit domains. This lemma is UNPROVED here. The cycle witness disproves deriving it from the vertex equation and boundary data alone.

The exact arithmetic check in verify_circulation.py used 96 rotations/reflections/scales, verified 576 zero vertex equations, boundary values zero and all jumps exactly 1, and detected every one of 96 single-edge perturbations. Gaussian elimination independently found rank 5 and nullity 1 on each six-edge face system. This checks finite algebra; it does not measure the true SAW observable.

## Independent derivation of the proposed collar lemma

Before reading w396's proof, read only STATEMENT_FOR_ADVERSARY.md. Let G be a finite graph with positive inherited edge weights and Z_G(a,b)>0, with simple a-to-b paths weighted by their edge products. Let F_k reveal the prefix, stopped at b and then held constant. A realized prefix eta has positive total completion weight. Its path weight factors into the fixed prefix weight times the residual suffix weight, which cancels on conditioning. The suffix is therefore distributed by the partition function on the graph deleting every earlier vertex and retaining the tip. If a prefix already hits a forbidden vertex set A, its conditional avoidance probability is zero; after completion it is the avoidance indicator. Impossible prefixes have probability zero, so no quotient 0/0 is part of the assertion.

For A subset B disjoint from a,b, put U=1_(path avoids A)-1_(path avoids B). Then U takes values in {0,1}, and

    D_k = M_k^A - M_k^B = E[U | F_k]

is a nonnegative bounded martingale. Every simple path has at most |V|-1 edges. For lambda>0, let tau be the first k with D_k>=lambda, clipped at that deterministic horizon. Bounded optional sampling gives E[D_tau]=E[U]=D_0, while D_tau>=lambda on the event that the maximum crosses lambda. Therefore

    P(max_k D_k >= lambda) <= D_0/lambda.

The initial D_0 is exactly Z_(G\A)/Z_G-Z_(G\B)/Z_G. No product of conditional bounds, independence claim, or limiting optional stopping is used. For any stopping time, D_tau still equals the conditional expectation with respect to the stopped prefix sigma-field. For lambda>1 the crossing probability is zero.

Sharp finite example: edges form the three paths a-u-k-b, a-u-c-b and a-v-b, with all edge weights 1 except weight(a,v)=2. Let A be empty and B={k}. The three complete path weights are 1,1,2. D_0=1/4. At the first step D_1=1/2 on the u branch and 0 on the v branch. At lambda=1/2 the probability of ever reaching lambda is 1/2, exactly D_0/lambda. This checks the threshold inequality and its universal constant.

This finite result transfers a SMALL static collar-probability difference into a uniform-in-prefix probability bound. It cannot prove that the initial static difference is small or identify the exponent 5/8.

## Avoidance-event boundary case

Weak curve convergence alone cannot pass avoidance probabilities for a fixed closed obstacle. In D=(-3,3)x(0,3), take a=(-2,0), b=(2,0), and the closed disk A centered at (0,1) of radius 1/4. Let gamma_n run vertically from a to (-2,5/4+1/n), horizontally to (2,5/4+1/n), and vertically to b. With corresponding three-segment parametrizations, gamma_n converges uniformly to gamma, whose horizontal segment lies at height 5/4 and touches A at (0,5/4). All gamma_n avoid A; gamma does not. Thus the avoidance indicator is discontinuous at gamma.

The same example satisfies the chordal route's boundary-attached-obstacle requirement if A is replaced by the disk union the closed rectangle [-1/4,1/4]x[0,1]. This is a compact capped notch attached to the bottom boundary, away from a and b, and D\A is simply connected. All gamma_n still lie above its top at5/4 and avoid it; gamma touches its cap. Thus the discontinuity is not limited to multiply connected punctured domains. Corners where the notch meets the outside boundary do not affect the marked endpoint neighborhoods.

The minimal repair is a proved zero-probability boundary-event condition for the limiting law, or a proved inner/outer collar squeeze with vanishing difference. The finite collar lemma is useful only after that static collar difference has been established.

The completed paired-proof audit is REVIEW_w396_proof.md. Its finite/conditional lemmas and first-entrance injection are mathematically correct at their stated scope; H_disk, H_len, H_5/8 and full scaling-limit identification remain unproved.

NEXT: Referee-check the remaining draft boundary examples and attack the mutually avoiding length-resolved counts in(U); do not replace C_(n-k) by an all-length partition sum.
