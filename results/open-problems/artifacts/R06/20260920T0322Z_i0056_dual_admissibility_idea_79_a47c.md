# R06 idea before code — dual nonpositive-curvature layers for the tetrapentagonal graph

Source remains Russell Lyons–Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056. The frozen regular/co-regular target remains `H_{5,5}={5,5}` with `Phi_V=sqrt(5)` and certified interval width zero. This note concerns the still-open second clause, through the source-valid tetrapentagonal graph

\[
T=r\{4,5\}=M(\{4,5\}),
\]

a 4-regular vertex-transitive plane graph of vertex type `[4,5,4,5]`.

The preceding R06 run isolated one missing all-radius statement, `FAL(4,5,4,5)`: every graph-distance frontier vertex should have one of the three arrival/fraternal/departure types

\[
A=(1,0,3),\qquad B=(1,1,2),\qquad C=(2,0,2),
\]

and every same-generation edge should have one of the two square/pentagon start-close profiles used in the recurrence algebra. That run verified the claim only through finite radius and deliberately left the recurrence conditional.

## New route before code

Use method #21 (ask who else has this shape) and move the distance-layer question to the planar dual. Let

\[
G=T^*.
\]

Then every face of `G` is a quadrilateral, while every vertex of `G` has degree 4 or 5; around a quadrilateral the degrees alternate `4,5,4,5`. Its corner curvature is therefore

\[
\kappa(v,f)=\frac1{\deg v}+\frac14-\frac12
\in\left\{0,-\frac1{20}\right\}.
\]

Thus `G` is a plane tessellation of nonpositive corner curvature.

Faces of `G` are vertices of `T`, and sharing a dual edge is exactly adjacency in `T`. Hence face distance from a root face of `G` is exactly graph distance from the corresponding root vertex of `T`.

Baues–Peyerimhoff (Adv. Geom. 6 (2006), DOI 10.1515/ADVGEOM.2006.014) and the formulation recalled in Klassert–Lenz–Peyerimhoff–Stollmann (Proc. AMS 134 (2006), DOI 10.1090/S0002-9939-05-08103-7) give precisely the missing global geometry for nonpositive corner curvature: face-distance balls are admissible polygons; a newly added face meets the previous boundary in a connected edge path of length at most two and contributes a connected nonempty edge path to the new boundary; the next face sphere has a cyclic ordering in which intersecting sphere faces are consecutive.

For our quadrangulation, this already bounds the number of arrival edges of every `T`-vertex by two at every radius. The admissible-boundary rule (`b` boundary vertices have `a+` neighbours) is the expected mechanism excluding the two forbidden valence-4 configurations: one arrival plus two fraternal edges, and two arrivals plus a fraternal edge.

There is an even cleaner local reduction at each dual vertex. The incident dual faces correspond to the vertices around one square or pentagon of `T`. Write their root distances cyclically as `(d_i)`. Then:

1. adjacent values differ by at most one;
2. for every threshold `m`, the incident faces with `d_i<=m` form one cyclic interval, because every face-distance ball is a polygon;
3. each exact level occurs at most twice: the cyclic face-sphere theorem says sphere faces intersect iff consecutive, while the relevant `T` spheres have at least four vertices (the first two spheres are known exactly; thereafter the inherited positive vertex-expansion lower bound gives this immediately).

For cycle lengths 4 and 5, those three conditions should force, up to an additive constant, rotation and reversal, exactly

\[
(0,0,1,1),\quad (0,1,2,1)
\]

for squares, and

\[
(0,0,1,2,1),\quad (0,1,2,2,1)
\]

for pentagons.

These four profiles are exactly the square/pentagon start-close profiles needed by the predecessor's `A/B/C/X/Y` state equations. If the finite profile classification checks exactly, write the full all-radius proof on the run page and promote the order-six shell recurrence from CONDITIONAL to PROVED.

## Method #20 — test why the obvious algorithm stalls

Once the recurrence is unconditional, do not assume ever-larger metric balls improve the isoperimetric upper bound. The characteristic polynomial is

\[
p(\lambda)=\lambda^6-\lambda^5-2\lambda^4+2\lambda^3-2\lambda^2-\lambda+1.
\]

Compare its dominant growth root with `1+113708/133611`. If the dominant root is larger, the ball boundary/volume ratio tends to a value *above* the current radius-16 witness, proving that blind BFS enlargement is asymptotically the wrong closing strategy.

## Prior-art boundary

- Haslegrave–Panagiotis, DOI 10.1002/rsa.20946, settle triangular and square hyperbolic lattices (face/codegree 3 and 4); those cases remain excluded and are not relabelled.
- de Souza–da Silva, Ars Combinatoria 160 (2024), DOI 10.61091/ars-160-14, develop graph-distance arrival/departure/fraternal counting and rational growth functions for uniform tilings, explicitly computing valence-5 families and selected valence-6 families while saying the method extends to other valences. I did not find the `[4,5,4,5]` graph-distance rational function printed there. The method itself is therefore prior art; any claim here is only that the valence-4 missing-layer argument is now supplied for this specific graph.
- Graves–Pisanski–Watkins, SIAM J. Discrete Math. 23 (2008), DOI 10.1137/070707026, study edge-homogeneous Bilinski growth and transition matrices. That is nearby growth literature but not the same rooted graph-distance shell sequence used here.

No novelty claim is made from a negative search alone. The objective remains the source's vertex-isoperimetric constant; this layer theorem is a structural step toward it.
