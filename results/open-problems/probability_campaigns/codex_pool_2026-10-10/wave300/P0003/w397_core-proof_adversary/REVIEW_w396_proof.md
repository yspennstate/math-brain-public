# Mathematical audit of the corrected P0003 packet

Reviewer: w397. Date: 2026-10-10. Reviewed frozen snapshot: review_packet/w396_ATTEMPT_snapshot.md; its exact version is recorded in w396_snapshot_receipt.json. The independent face-circulation derivation predates reading the paired proof.

VERDICT: KEEP the finite lemmas L0, L0', L1, L2, the conditional trace lemma L3 under (C), and the first-entrance upper bound (U). KEEP them only at their stated finite/conditional scope. P0003 is not proved.

L0: path deletion is a weight-preserving bijection. At a realized prefix, cancellation of its positive product weight gives the residual law only after all earlier vertices have been removed. Terminal prefixes use the terminal indicator, and zero-completion histories are null. Subdivision into half-edges weighted x_c^(1/2) gives 2*ell half-edges per mid-edge walk visiting ell original vertices, hence exactly x_c^ell. This is a finite encoding and supplies no continuum endpoint-convention transfer.

L0': preserving the remaining length n-k is essential for the catalog's fixed-length free-endpoint law. Every origin-started n-edge walk lies in the graph-distance-n ball, so the finite graph covers it. The completion bijection is with C_(n-k)(G_eta;tip), and the empty continuation at k=n has weight1. Dividing by a grand-canonical partition function instead would change the conditional law. The corrected packet uses the right kernels.

L1: the independent proof in ATTEMPT.md gives D_k=E[1_avoidA-1_avoidB|F_k]. Stopping at the first crossing, clipped at a deterministic finite horizon, proves the bound without an independence or unbounded-stopping assumption. The sharp three-path example in ATTEMPT.md attains equality at lambda=1/2. Edge obstacles and horizon n in the fixed-length model cause no change to this proof.

L2: write p=P(E_B|E_A). The law conditioned on E_A is p times its E_B component plus 1-p times the complementary component; the supports are disjoint. The total variation convention sup_C|P(C)-Q(C)| therefore gives exactly1-p. The case p=1 needs no conditioning on an empty difference event. A stopped-prefix map is measurable and contracts this distance.

L3: let d_n=dist(K_n,A), d=dist(K,A). The compact-trace assumption and closed nonempty A make clearance continuous, and avoidance means positive clearance. Portmanteau gives P(d>0)<=r and r_j<=P(d>=epsilon_j)<=P(d>0), hence P(d>0)=r. An independent way to check the conditioning step is to use continuous clearance cutoffs h_epsilon(d) which equal0 at0 and1 for d>=epsilon. The error against 1_(d>0) is bounded by P(0<d<epsilon); for d_n this has limsup at most r-r_j at suitable epsilon_j. Taking n first and then j gives convergence of E[F(K_n)1_(d_n>0)] for bounded continuous F, and division by r>0 gives conditional weak convergence. Thus assumption(C), not weak convergence alone, closes the avoidance-indicator discontinuity. The paired Skorohod argument reaches the same result and is valid because compact trace space is Polish.

(U): a counted n-step path avoiding A but entering B has one first B-forbidden edge(v,w), with unique index k. Its prefix avoids B, and its suffix avoids A and has exact length n-k-1. The map to(prefix, oriented edge, suffix) is injective. Summing the products of their counts after dropping mutual avoidance is a valid upper bound. Cases k=0 and k=n-1 are covered by C_0=1. This product is a counting bound; it asserts no probabilistic independence. Its overcounting of mutually intersecting pieces is exactly the unresolved estimate, not a hidden proof of H_disk.

The fixed-length H_disk statement uses limsup_(n->infinity) before sending epsilon to zero, and constants depending on the fixed disk center/radius. It does not assert a bound uniform over arbitrary moving disks or epsilon_n-dependent collars. I found no quantifier or finite-boundary defect in that precise statement. It remains conjectural: no control of the mutually avoiding length-resolved prefix/suffix mass has been obtained.

The source-scope correction has been adopted: the original Grimmett Question2.2 is fixed length, while critical chordal H_5/8 is explicitly a related model. The packet now defines H_len and H_disk as additional unproved inputs and does not claim an ensemble equivalence.

FIX citation: in the Lawler--Schramm--Werner restriction paper, Lemma3.2 determines the law from a determining obstacle class. Theorem6.1 proves the SLE(8/3) avoidance formula. Cite both for conditional identification rather than describing Theorem6.1 itself as the uniqueness theorem. I read these two primary-source statements; this matches the separately recorded referee correction.

Counterexamples and minimal remaining premises:

- The finite hexagon field in INDEPENDENT.md refutes uniqueness/compactness from the local vertex identity alone. The true SAW observable needs an additional regularity estimate.
- The boundary-attached capped-notch example in ATTEMPT.md refutes passing closed-obstacle avoidance through weak/uniform curve convergence alone. A vanishing collar difference or the equivalent clearance condition(C) is needed.
- L1 bounds absolute errors in conditional avoidance probabilities. A relative-error strengthening requires localization away from zero denominators. On the three paths a-u-k-b, a-u-c-b, a-v-b with path weights epsilon,1-epsilon,1, take A={c}, B={c,k}. Then D_0=epsilon/2, yet at prefix(a,u), which has probability1/2, M^A=epsilon and M^B=0, so D/M^A=1. The packet does not make that strengthening; this example states its boundary explicitly. Independent referee check of this additional example is pending.

No admissible counterexample to the stated finite lemmas was found. The hardest attempted positive input H_disk and the further identification/tightness inputs remain open. The review is a mathematical derivation, not a formal-check or source-hash certificate.

NEXT: Referee-check the additional capped-notch/relative-error boundary examples; integrate the accurately scoped finite/gap rows, then attack the mutually avoiding counts in(U) while retaining exact remaining length.
