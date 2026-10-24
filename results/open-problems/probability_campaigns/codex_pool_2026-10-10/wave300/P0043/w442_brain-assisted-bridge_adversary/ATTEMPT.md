# P0043 independent adversarial work

All deductions here were saved before reading w441's proof. No general solution or novelty is claimed.

## Independent boundary obstruction

Let G have vertex set Z and an edge between each consecutive pair of integers. Perform iid Bernoulli bond percolation with edge parameter p in [0,1]. Define theta_G(p)=P_p(|C(0)|=infinity) and p_c(G)=inf{p:theta_G(p)>0}.

For p<1, an infinite component at 0 requires all edges on one of the two rays from 0 to be open. Each ray has probability lim_n p^n=0. Thus theta_G(p)=0 for p<1. At p=1 all edges are open almost surely, so p_c(G)=1 and theta_G(p_c)=1. G is connected, locally finite, infinite and vertex-transitive.

Consequently an unqualified universal assertion for quasi-transitive graphs needs at least a hypothesis excluding this boundary case, commonly p_c<1. This does not refute a correctly restricted conjecture. Exact source recovery is pending.

## Independent quantifier obstruction

Fix a in (0,1) and define f_n(p)=min{1,(p/a)^n} for p in [0,1], n>=1. Each f_n is continuous and increasing in p, and f_n decreases with n. At p=a, f_n(a)=1 for every n. For every q<a, inf_n f_n(q)=0. Thus finite-scale continuity and uniformly positive values at a do not imply that one common q<a has uniformly positive values at all scales. The inference (for every n there exists q_n<a) => (there exists q<a for every n) fails. This is a countermodel to that logical inference, not a Bernoulli-percolation counterexample in the target graph class.

For actual percolation, write A_R={o connects to graph-distance R} and f_R(p)=P_p(A_R). Local finiteness makes f_R a finite polynomial; the events decrease and their intersection is {|C(o)|=infinity}. Hence theta(p)=inf_R f_R(p). The missing bridge in a finite-continuity approach is a radius-uniform modulus or a robust finite criterion that implies infinite survival at one subcritical parameter. It cannot be replaced by continuity separately for each R.

## Exact scope recovered from a primary source

Hutchcroft, C. R. Math. 354 (2016), Conjecture 1.1, specifies connected locally finite quasi-transitive graphs with p_c(G)<1, iid Bernoulli bond percolation, and almost-sure absence of every infinite cluster at p_c. The paper's Theorem 1.2 proves the exponential-growth subclass. Source: https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2016.07.013.pdf . The conjecture citation and its hypotheses were checked in the source, rather than inferred from the abbreviated ranking.

These two independent obstructions were saved before any paired proof was read. Their referee is w443; review is pending.

## Deterministic obstruction to an anchored-expansion bridge

Derivation saved before the paired ATTEMPT.md was inspected (only its STATUS.md named anchored expansion).

Let G be a connected infinite graph of maximum degree Delta<infinity, with limsup_{r->infinity}|B_G(o,r)|^(1/r)=1. Let H be any infinite connected subgraph containing o. For a finite connected vertex set S containing o, let boundary_H(S) be the H-edges with exactly one endpoint in S. Define iota_*(H,o)=liminf_{n->infinity} inf{ |boundary_H(S)|/|S| : S finite, connected in H, o in S, |S|>=n }.

Then iota_*(H,o)=0. Indeed, if it were positive, choose c>0 and n0 such that every qualifying S with |S|>=n0 has |boundary_H(S)|>=c|S|. Infinite connected local finiteness makes |B_H(o,r)| tend to infinity. For all sufficiently large r, take S=B_H(o,r). Each outside vertex has at most Delta incident edges, so

|B_H(o,r+1)| >= (1+c/Delta)|B_H(o,r)|.

Iteration forces liminf_r |B_H(o,r)|^(1/r)>=1+c/Delta>1. But every H-path is a G-path, hence B_H(o,r) is contained in B_G(o,r), contradicting the assumed subexponential growth of G.

Thus a proposal to deduce positive anchored expansion of a hypothetical infinite critical cluster on a subexponential ambient graph has an impossible premise. This is deterministic and does not rely on conditioning, density, independence of block events or an exchange of limits. It does not prove absence of the critical cluster; it shows why this particular sufficient-condition route misses every subexponential case, including Z^3.

NEXT: Retrieve the exact anchored-expansion/thinning card by bounded read-only lookup, compare w441's assumptions, and save a referee-ready verdict on that bridge.
