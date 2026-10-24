# C0047 referee packet, 2026-10-10

Original statement: Benjamini and Schramm (1996), Conjecture 6 is about Bernoulli **site** percolation on connected locally finite almost transitive graphs with positive vertex Cheeger constant. The 2018 intake restates a Cayley-graph equivalence. Peers w555 and w556 use **bond** percolation in their lemmas; their results must keep that model label.

## Verdicts

| Artifact | Verdict | Reproduction and limit |
|---|---|---|
| w555 L1 | KEEP | A connecting path intersects each deterministic cut; disjoint edge coordinates make the cut-open events independent. Random adaptively selected cuts need a new proof. |
| w555 L2 | KEEP | Harris on two infinite-cluster membership events gives a fixed `theta^2` lower bound under uniqueness; L1 tends to zero. The uniform bounded-cut hypothesis is essential. |
| w555 L3 | KEEP | I independently checked the minimal-cut finite-side argument below. It blocks the proposed L2 mechanism on one-ended positive-Cheeger graphs. |
| w555 L4 | KEEP, bond special case | The cycle-block quotient of `C_2*C_m` is a tree, and fresh outgoing bridge variables make an iid Galton-Watson exploration with mean `p[2 sum_{k=1}^{m-1}p^k-(m-1)p^m]`. It proves this fixed Cayley graph's bond `p_c<p_u=1`; it does not prove the parent site conjecture. |
| w555 L5 | KEEP, normalized-rho criterion | The walk-count upper bound has factor `d*rho`; it correctly repairs the intake attempt. It is sufficient only where `p_c*d*rho<1`. |
| w556 S1 | KEEP | Independent finite-set Rayleigh calculation below confirms uniqueness precludes a bounded two-point operator. Existence of a bounded supercritical parameter remains the hard gap. |
| w556 S2 | KEEP | The `Z` kernel has row-square sum at most 5 but interval Rayleigh quotients at least `n(1+n)^(-3/4)`. This is a generic kernel counterexample, not iid percolation on a nonamenable graph. |
| w556 S3 | KEEP as source-level warning | Public comparator theorem bodies contain `sorry`; they cannot serve as a formal-check receipt. The mathematical preprint requires separate audit. |

## Independent check of the hardest structural claim, w555 L3

Let `F` be an inclusion-minimal edge set separating x from y. In `G\F`, any edge of `F` must join the x-component to the y-component: restoring that edge must destroy separation, and an edge incident to a third component would not. Connectivity of G rules out another component without an incident edge of F. Hence F is exactly the boundary of each endpoint component. If both were infinite, deleting the finite set of endpoints of F would leave two infinite components, contrary to one-endedness. The finite component A satisfies `h_E |A| <= |F| <= K` and contains x or y. Connectedness of A puts every vertex within `|A|-1 <= K/h_E` of that endpoint. Every edge of F therefore meets `B_R(x)` or `B_R(y)` for `R=ceil(K/h_E)+1`. Edge-disjoint minimal cuts consume distinct edges from a supply of at most `d(|B_R(x)|+|B_R(y)|)`. This independently proves the bound.

## Independent check of the hardest analytic claim, w556 S1

For each vertex x let `I_x` mean its bond cluster is infinite. Each event is the decreasing limit of finite-coordinate events that x connects outside the radius-n ball; Harris inequality passes to the limit and gives `P(I_x ∩ I_y)>=theta^2`. If the infinite cluster is unique almost surely, `I_x∩I_y` implies connection, so `tau_p(x,y)>=theta^2`. For `f_S=1_S/sqrt(|S|)`, the quadratic form is at least `|S|theta^2`; arbitrarily large finite S rule out a bounded operator. If a bounded parameter p exceeds `p_c`, entrywise monotonicity under the usual coupling yields boundedness for every q<=p, which excludes uniqueness there. Thus `p_u>=p>p_c`. The general existence of that p has not been shown.

## Source and status boundary

The dated intake attempt C0047-A001 omits the degree factor in the 1996 spectral condition. The current public comparator documentation describes a full bond proof, but the visible named Lean theorem bodies use `sorry`. A public September 2026 mathematical preprint claims more; its proof is being checked separately. Source hashes, title matching, and these partial lemmas do not settle the parent problem. Until the paper's load-bearing estimate has an independent mathematical check, current openness is UNKNOWN and parent solved status is unverified.

NEXT: Inspect the September 2026 preprint's critical operator estimate, and send a scoped review plus exact model boundary to the integration contact.
