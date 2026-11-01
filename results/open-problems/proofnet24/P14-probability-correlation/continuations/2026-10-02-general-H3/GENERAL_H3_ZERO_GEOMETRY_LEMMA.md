# Equality geometry for the proposed fourth coefficient

2 October 2026. This is a proved derived equality lemma using the global
H3 sum-of-squares theorem finalized in `GENERAL_H3_SOS_PROOF.md`. The proof
below has passed independent parent and child analytic audits. It does not
settle any later coefficient or the forest negative-correlation conjecture,
and historical novelty is not certified.

## Definitions and hypotheses

Use the graph, marked edges, current supports E,F, common zero set S,
harmonic rows p, boundary Green matrix T, response rows eta_e,g and eta_f,h,
and positive edge conductances c_g of `GENERAL_H2_SOS_PROOF.md`.
Write A=N(E) intersect S and C=N(F) intersect S. Assume H0=H1=H2=0.
Discard zero response rows. By the response-space kernel lemma, every
e response potential

    a_g(x)=p_x T eta_e,g^T

is constant on C, hence constant on F by harmonicity. Every f response
potential b_h is constant on A and on E. Define the special potentials

    u_g(x)=a_g(x)-a_g(c),  c any vertex in C;
    z_h(x)=b_h(x)-b_h(a),  a any vertex in A.

Thus u_g=0 on C union F, and z_h=0 on A union E. The choices of c and a do
not matter. Viewed on the full graph, their Laplacian sources are supported
on A and C respectively: harmonic extension followed by the Schur complement
gives L u_g=(eta_e,g)^T, L z_h=(eta_f,h)^T, with the omitted ground coordinate
restored to make each source have total sum zero.

The H3 theorem asserts

    H3/tau^2 = sum_{g,h,k} c_g c_h c_k
                 [u_g(x_k) z_h(y_k)-u_g(y_k) z_h(x_k)]^2.

## The equality lemma

If H3=0, define aggregate response supports

    E2={x: u_g(x) is nonzero for at least one g},
    F2={x: z_h(x) is nonzero for at least one h}.

Then E2 and F2 are disjoint and no graph edge joins them. Every component
of E2 meets A, and every component of F2 meets C. If both original response
matrices are nonzero, E2 and F2 are nonempty, and their common zero complement
S2=V(G) minus (E2 union F2) is nonempty.

### Proof for one response pair

All summands in the displayed H3 formula have positive prefactors. Hence
for each pair (g,h), u=u_g and z=z_h have zero wedge on every graph edge.
On a component D of the vertices where (u,z) is not (0,0), the projective
direction [u:z] is constant: adjacent nonzero vectors with zero determinant
are proportional, and this propagates along a path.

Suppose that both coordinates of this direction are nonzero. Then neither
source support A nor source support C can meet D, since z=0 on A and u=0
on C. Therefore u and z are harmonic on D. Any vertex outside D adjacent to
D has both coordinates zero by the definition of a connected component of
the nonzero set. Consequently u has zero boundary values on D and no source
inside D. The finite weighted maximum principle gives u=0 on D, a
contradiction. Thus u(x)z(x)=0 at every vertex. A graph edge from a nonzero
u vertex to a nonzero z vertex would now have a nonzero wedge, also a
contradiction.

### Aggregating the response pairs

If x belonged to both E2 and F2, some g,h would have u_g(x)z_h(x) nonzero,
contradicting the pairwise conclusion. If xy joined E2 to F2, choose g,h
with u_g(x) and z_h(y) nonzero. Pairwise disjointness gives z_h(x)=u_g(y)=0,
so the edge wedge would be nonzero. Hence no such edge exists.

Every response potential u_g is harmonic outside A. If a component D of
E2 did not meet A, each u_g would be harmonic there and zero on its boundary
(outside E2 all u_g vanish). The maximum principle would force every u_g to
vanish throughout D, contrary to D being part of E2. The F2 assertion is
identical. Nonzero B_e gives a nonzero response row, whose potential is
nonconstant because T is positive definite; subtracting a constant cannot
annihilate it. Thus E2 is nonempty, and similarly F2. Connectivity of G and
the absence of E2–F2 edges force S2 to be nonempty. This proves the lemma.

## Limit of the conclusion

This supplies a second separation geometry after the first three Rayleigh
coefficients vanish. It does not yet yield a recursion for H4: the local
marked scores have higher-degree Grassmann terms, so they cannot be replaced
by boundary bilinears at every order. In particular, the already checked
two-port score contains a quartic term at its second order. A recursive
sum-of-squares theorem would have to control those terms rather than infer
independence from separation alone. K4-chain examples already demonstrate
arbitrarily many leading zero coefficients.
