# C0047 proof route and corrected spectral special case

The full target is every fixed Cayley graph of every infinite finitely generated nonamenable group, with Bernoulli bond percolation. The original 1996 formulation is broader and uses site notation. Current openness is UNKNOWN because a September 2026 paper claims the full theorem, but this packet has not validated its Section 4 switching lemma.

## Exact hardest input for this route

For a fixed graph G, let τ_p(x,y)=P_p(x↔y), and let T_p be its kernel on counting-measure ℓ²(V). The peer reductions prove that **||T_pc||_(2→2)<∞ implies p_c<p_u**. What remains is to derive this bound from nonamenability for every original generating set. An F-dependent finite-volume bound, a pointwise decay estimate, or a favorable replacement generating set does not close it. In the claimed 2026 full proof, Lemma 4.8's joint inverse-code injection is a concrete load-bearing input still requiring referee reconstruction.

## Independently rederived spectral criterion, bond model

Let G be an infinite simple d-regular Cayley graph, P=A/d the simple random walk transition operator on ℓ²(V), and ρ=||P||_(2→2). Suppose dρ p_c<1. Choose q with p_c<q<min(1,1/(dρ)). For vertices x,y at distance r, each open connection has a finite self-avoiding path, so a union bound over all walks gives

τ_q(x,y) ≤ ∑_{n≥r} q^n (A^n)(x,y) = ∑_{n≥r}(dq)^n P^n(x,y) ≤ (dqρ)^r/(1−dqρ).

The last step uses |P^n(x,y)|≤||P^n||≤ρ^n. Thus τ_q(x,y) tends to zero uniformly as dist(x,y)→∞. If there were a unique infinite cluster almost surely at q, transitivity and Harris–FKG would give τ_q(x,y)≥P_q(x↔∞)P_q(y↔∞)=θ_q²>0 for all x,y. Contradiction. The same argument excludes almost-sure uniqueness at every p<min(1,1/(dρ)); below p_c no infinite cluster exists, while above p_c the FKG contradiction applies. Hence p_u≥min(1,1/(dρ))>p_c. This is a sufficient special case, not the general conjecture.

The 1996 paper's Theorem 4 states a site version with maximum degree k and condition ρ(G)kp<1 (PDF p. 76–77, lines 272–276). The September 2026 intake attempt C0047-A001 instead writes `p_c < 1/rho` as if sufficient. With ρ<1 for nonamenable Cayley graphs, p_c<1/ρ is automatic once p_c<1; the degree factor is indispensable. On a 3-regular tree, p_c dρ=√2>1 though p_c<p_u. Thus the path criterion cannot be elevated to an equivalent characterization.

## Independent audit of the claimed 2026 proof route

The paper's Theorem 1.1 asserts bounded T_pc and p_c<p_{2→2}≤p_u on infinite connected locally finite nonamenable quasi-transitive graphs. Its introductory outline says the proof converts a heavy critical cluster tail to local endpoint maps, bounds a switched load's second moment, then uses deformation and a contradiction. The earliest nonstandard load-bearing bound I identified is Lemma 4.8: E[L²]≤Q(k,M)u^(2k). The proof partitions paired inverses into no-switch, overlapping/adjacent hanging pieces, and disjoint nonadjacent hanging pieces. The last class removes an exponential code factor by claiming two inverse maps can be jointly undone injectively after restoring the common root cluster. I checked the subsequent Markov truncation algebra, but not the joint injection. Status: **input unproved by this referee**, so the claimed paper's theorem is not promoted by this packet.

NEXT: Reconstruct the switching state and inverse code from the PDF's Sections 4.2–4.4, then verify or refute the disjoint-case injection without assuming output fields remain independent.
