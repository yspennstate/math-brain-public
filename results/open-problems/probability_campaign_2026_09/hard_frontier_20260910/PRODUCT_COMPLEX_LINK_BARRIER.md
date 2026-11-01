# Why the graph-product method cannot cross the local 1/d threshold

Author derivation, 10 September 2026. This applies a classical weighted spectral/cohomological argument to the new intake question H20260910-01. It is a method obstruction, not a solution of that open problem and not a certified novelty claim. The proof below is self-contained. A separate direct calculation checks the constant for the source's original weights.

The model is the product complex Z(G;K,s) in [Mao, Section 5](https://arxiv.org/html/2609.08937v1#S5), based on the construction cited there to Golowich. Its vertices are (v,b) with v a vertex of G and b one of s labels. Each top face uses K+1 distinct labels and projects onto exactly one edge of G. Let Y be its d-skeleton.

**Claim.** Suppose G is finite, connected and contains a simple cycle, K >= d >= 2, and s >= 2K. Give the d-faces of Y any strictly positive probability weights, and give all lower faces and links their induced weights. Some codimension-two link has second-largest transition eigenvalue at least 1/d.

Thus changing the base graph, increasing K, or changing positive face weights cannot make every codimension-two link have two-sided spectral norm strictly below 1/d within this graph-product family. The result requires a cycle in the base graph. It does not rule out different Cayley complexes containing faces that project onto more than two base vertices.

## 1. An elementary spectral descent identity

Take a finite pure weighted two-dimensional complex, with top-face distribution mu_2 and induced distributions mu_1 on unordered edges and mu_0 on vertices. In particular,

    mu_1({u,v}) = (1/3) sum_{triangles containing {u,v}} mu_2(triangle),
    mu_0(v) = (1/3) sum_{triangles containing v} mu_2(triangle).

The global walk has P(v,u)=mu_1({v,u})/[2 mu_0(v)]. The stationary law of the link at v is pi_v(u)=mu_1({v,u})/[2 mu_0(v)]. Assume the global graph is connected and each vertex-link walk has second eigenvalue at most kappa < 1.

Let f be a nonconstant global eigenfunction, Pf=eta f, with eta<1. Write g_v for its restriction to the neighbours of v. The mean of g_v under pi_v is eta f(v). Therefore

    sum_v mu_0(v) Var_pi_v(g_v) = (1-eta^2) ||f||^2_mu_0.

The first term is ||f||^2 because the neighbour distribution averaged over mu_0 is again mu_0. Each weighted triangle contributes its three edge differences once to the sum of link energies. With the above normalization this gives exactly

    sum_v mu_0(v) E_link(v)(g_v,g_v)
      = E_global(f,f) = (1-eta) ||f||^2_mu_0.

Apply the link Poincare inequalities with gap at least 1-kappa. Cancelling the positive factor (1-eta)||f||^2 yields

    1 >= (1-kappa)(1+eta),   hence   eta <= kappa/(1-kappa).

The same statement applies to the weighted two-skeleton of any higher-dimensional link, since taking induced distributions commutes with taking links and lower skeletons. Consequently, if all codimension-two link eigenvalues are at most lambda and all intervening link graphs are connected, the vertex-link second eigenvalues are at most

    lambda / [1-(d-2)lambda].

This follows by d-2 iterations of x -> x/(1-x); for d=2 there is no iteration. If lambda<1/d, all denominators are positive and the displayed vertex-link bound is strictly below 1/2.

## 2. Vertex-link eigenvalues below 1/2 force real first cohomology to vanish

Here is the finite-dimensional argument, including the normalization that fixes the threshold. An edge cochain a is antisymmetric: a(v,u)=-a(u,v). It is closed when

    a(v,u)+a(u,w)+a(w,v)=0

on every triangle. Gradients have the form a(v,u)=h(u)-h(v). Use the edge norm ||a||^2=sum_{unordered edges} mu_1(edge) a(edge)^2.

If a closed cochain is not a gradient, subtract its orthogonal projection onto the gradient subspace. This leaves a nonzero closed cochain a orthogonal to all gradients. Finite-dimensional linear algebra suffices; no analytic Hodge theorem is needed. Orthogonality means

    sum_u mu_1({v,u}) a(v,u)=0

at each vertex. Thus a_v(u)=a(v,u) has zero mean under pi_v. Directly from the edge normalization,

    sum_v mu_0(v) ||a_v||^2_pi_v = ||a||^2.

Closedness gives a_v(w)-a_v(u)=a(u,w). Each triangle therefore contributes its three squared cochain values when local energies are summed. Precisely,

    mu_0(v) E_link(v)(a_v,a_v)
      = (1/6) sum_{triangles {v,u,w}} mu_2({v,u,w}) a(u,w)^2.

Summing over v and using sum_{triangles containing e} mu_2=3 mu_1(e) gives

    sum_v mu_0(v) E_link(v)(a_v,a_v) = (1/2)||a||^2.

If every vertex-link second eigenvalue is at most kappa<1/2, its Poincare inequality instead gives the lower bound (1-kappa)||a||^2. Since 1-kappa>1/2 and a is nonzero, this is impossible. Hence every closed cochain is a gradient.

This argument uses only the two-skeleton, so it applies to a pure weighted d-complex after inducing its triangle weights. Together with Section 1 it proves that codimension-two bounds strictly below 1/d imply vanishing real first cohomology, under the stated connectivity assumptions.

## 3. A cycle survives in every product complex under consideration

Projection p(v,b)=v sends every simplex of Y into either one vertex or one edge of G. Choose an oriented simple cycle in G and an antisymmetric base-edge cochain c whose integral around this cycle is one; for example, use an indicator of one oriented cycle edge.

Define a on edges of Y by pulling back c, assigning zero to edges inside a fiber. On a triangle, the projected vertices take at most two values, so the three cochain values cancel. Thus a is closed.

A cycle is properly three-colorable. Choose labels in {1,2,3} for its vertices so consecutive labels differ, and lift its edges to Y. These are edges of Y because their distinct labels can be completed to a product top face; s>=2K and K>=2 provide enough labels. The lifted cycle has cochain integral one. A gradient has integral zero around every closed walk, so a is not a gradient.

This construction is independent of all positive face weights. It proves that Y has nonzero real first cohomology.

For completeness, the required link graphs are connected. A nonempty face F projects either to a single vertex v or to an edge {u,v}. In the latter case, its link graph has both fiber choices for each unused label, with edges between distinct labels; it is connected. In the former case, the link consists of the remaining v-fiber and its neighbour fibers. Distinct-label edges join each neighbour fiber to the v-fiber. At least three labels remain, so any two link vertices are joined through these edges, possibly using a third label. The global graph is connected because each fiber is connected and base edges join adjacent fibers. Strict positivity of all d-face weights preserves these graphs.

If every codimension-two second eigenvalue were less than 1/d, there would be a common lambda<1/d because the complex is finite. Sections 1 and 2 would make a a gradient, contradicting its nonzero cycle integral. This proves the claim.

## 4. Independent calculation for the original balanced weights

The source weights each K-face projecting to {u,v} proportionally to

    w({u,v}) / binom(K-1,j-1),

where j of its vertices lie over u. Fix a codimension-two face F consisting of q=d-1 distinct labels over a vertex v with at least two neighbours. Put L=K-d. After suppressing the common choice of unused labels, the link edge weights within a neighbour-u fiber and between the u and v fibers are respectively w({u,v})A and w({u,v})B, where

    A = sum_{a=0}^L binom(L,a)/binom(K-1,a+1),
    B = sum_{a=0}^L binom(L,a)/binom(K-1,a).

The elementary beta-integral identity

    1/binom(K-1,j) = K integral_0^1 x^j (1-x)^(K-1-j) dx

and the binomial theorem give

    A = K integral_0^1 x(1-x)^(d-2) dx = K/[d(d-1)],
    B = K integral_0^1 (1-x)^(d-1) dx = K/d.

Choose constants c_u on the neighbour fibers with sum_u w({u,v})c_u=0, and put the function equal to zero on the v-fiber. A step from a neighbour fiber remains in that fiber with probability A/(A+B)=1/d. At a v-fiber vertex the weighted neighbour contributions cancel. This is therefore a nonzero eigenfunction with eigenvalue exactly 1/d. The space of such functions has dimension deg_G(v)-1.

This direct calculation checks the same threshold without the cochain argument. It proves exact attainment for the original weights, whereas Sections 1-3 rule out improvement by any positive reweighting whenever G contains a cycle.

## Consequence for the open-question program

H20260910-01 remains unsolved. A successful construction below 1/d must escape the cycle-preserving graph-product framework, rather than only alter its dimension, base expander or positive weights. The next useful investigation is a genuinely different higher-dimensional relation complex. This packet should be recorded as a proved method obstruction with novelty unverified, not as another solved source question.
