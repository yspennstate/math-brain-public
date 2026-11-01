# C0047 referee: site boundary and precise status

## Exact target and current status

Benjamini and Schramm's 1996 Conjecture 6 concerns a connected locally finite *almost transitive* graph with positive vertex Cheeger constant. The paper uses Bernoulli **site** percolation by default (definitions, page 2), and says the nonplanar questions also have bond forms. The C0047 intake title narrows this to Cayley graphs and paraphrases the equivalence with group nonamenability. In the Cayley version the quantifier is **every prescribed finite symmetric generating set**, not existence of a favorable set.

The public 2026 OpenAI manuscript, `openai_nonuniqueness_2026.pdf` (SHA256 `46A78D044D2713E48CB3FAA9B0B9D22DA9480193E2202FE63D8E0DAA7D8A3DBB`), Theorem 1.1 and Corollary 1.2, claim the full **bond** statement, including every such Cayley graph. I checked the exact stated hypotheses and the last proof step (text lines 117–149, 3090–3125). I have not independently validated its 53-page proof or the load-bearing Theorem 2.6. Its public Lean comparator has `sorry` in the three main theorem bodies. No formal-proof receipt follows from that comparator. Site status remains UNKNOWN on the sources checked.

## My sharp site special case, for w563 to audit

Let $T_d$ be the infinite $d$-regular tree, $d\ge3$, and perform independent Bernoulli **site** percolation at parameter $p$. Define $p_c$ as the threshold for an infinite open cluster and $p_u=\inf\{p:\text{a.s. exactly one infinite open cluster}\}$. Then

\[p_c(T_d)=1/(d-1),\qquad p_u(T_d)=1.\]

Fix a root. Conditional on the root being open, each nonroot open vertex has independently $\operatorname{Binomial}(d-1,p)$ open children. The nondegenerate Galton–Watson process survives exactly when $(d-1)p>1$; at equality it dies out. Root openness has probability $p$, so the same threshold holds for site percolation. Countability of vertices upgrades absence of an infinite root cluster to absence of any infinite cluster.

For $p_c<p<1$, fix a ray $v_0,v_1,\ldots$. At each $v_n$ choose one side child $u_n$ off that ray. Let $E_n$ say that $v_n$ is closed and $u_n$ has an infinite open descendant cluster inside its hanging subtree. The events depend on pairwise disjoint vertex sets, so they are independent. Their common probability is $(1-p)s(p)>0$, where $s(p)$ is the unconditional probability that $u_n$ has an infinite descendant cluster. By independent trials, infinitely many $E_n$ occur almost surely. Each creates an infinite cluster trapped in a different hanging subtree because its sole attachment vertex $v_n$ is closed. Thus uniqueness fails throughout $(p_c,1)$; at and below $p_c$ no infinite cluster exists, and at $p=1$ the tree is one open cluster. This establishes the exact pair of thresholds.

The derivation covers the original site's model on one nonamenable quasi-transitive graph. It is classical, carries no novelty claim, and does not solve the parent conjecture. Independent referee w563 is requested to check the countability, independence, and isolation steps before any theorem card is promoted.

## Hardest open or unchecked piece

For the **site** target, transfer of the bond theorem to site percolation on every nonamenable quasi-transitive graph is not established in this packet. For the **bond** target, the 2026 manuscript's critical operator boundedness (Theorem 2.6 in the unimodular case) is the load-bearing proof step requiring independent mathematical validation. A source/hash match and comparator scope note do not validate it.

NEXT: Obtain an independent mathematical audit of Theorem 2.6 and a separate site-status check; request w563 review of the site-tree lemma.
