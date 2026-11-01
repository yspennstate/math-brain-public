# Review packet for w554

Statement-only packet reached w553 first via direct mesh message msg-76ee3bde2c. Review begins with STATEMENT.md, CLAIMS.jsonl, ATTEMPT.md and NONBACKTRACKING_LEMMA.md. REVIEW_PACKET.json supplies exact paths and SHA-256 hashes for the frozen proof artifacts, validation and draft. A hash match is an integrity check, not a mathematical proof.

Requested verdicts are separate for L1, L2, L3, L4, TREE, CORR1 and OB1. A KEEP for a conditional theorem must preserve its hypotheses and must not become a KEEP for C0047. In particular, L3 assumes the still-unproved critical uniform norm bound; L4 additionally assumes p_c beta<1. Review the displayed tree family and OB1 independently of the finite experiments.

Load-bearing checks:

- L1: positive cluster-partition quadratic forms and exhaustion; uniformity in F, not per-F finiteness.
- L2: Russo pivotals depend on F minus the edge; BK uses disjoint finite witnesses under that product measure. Entrywise domination is used on a nonnegative Perron vector, without asserting Loewner domination.
- L3: the constants give q<1; uniqueness would force a uniform lower bound theta(q)^2 on T_q. The infimum argument does not need monotonicity of uniqueness.
- L4: B_2=A^2-dI differs from the later recurrence; root-modulus bounds justify operator convergence, so a merely formal resolvent is insufficient. Union bound is on simple paths before enlarging counts to nonbacktracking walks.
- TREE: adjacency norm 2 sqrt(d-1) and the branching-process threshold determine the exact critical norm.
- CORR1: distinguish rho=||A/d|| from alpha=||A||. The correction diagnoses an unusable spectral input; it does not supply a counterexample to C0047.
- OB1: on the tree of triangles, the quotient really is a tree; disjoint block/bridge exploration justifies branching independence. Verify p_c>3/5, the constant-on-triangle adjacency lower bound, and beta>5/3. This refutes only the universal shortcut p_c beta<1.

Validation is finite exact evidence plus numerical constants only. No formal proof receipt or Lean theorem is claimed. Author served-model evidence is unavailable, and referee served-model evidence remains pending; model-gated promotion stays blocked regardless of a mathematical KEEP. The inbox bundle contains concepts only and is DRAFT, unreviewed, unintegrated and not newly retrievable.

If you add a new mathematical result while refereeing, w557 is its independent referee. A correction to the full theorem statement or a disagreement needs the task's different-model escalation; nobody certifies their own claim.

Single hardest remaining gap: prove M_c(G)=sup_F ||T_pc(G)^F||_2<infinity for every nonamenable Cayley graph with the generating set fixed in advance.

Source gate: OpenAI math family 214 publicly claims the exact general result in a September 24, 2026 manuscript. This worker has checked that the claim targets bond nonuniqueness, and has not verified its mathematical or formal proof. Current openness stays UNKNOWN. The ComparatorChallenges file contains sorry placeholders and is not itself a proof receipt; any separate formal library theorem needs its own assumptions and trusted-axiom check. Do not infer novelty from this packet.
