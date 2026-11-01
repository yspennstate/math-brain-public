# R06 idea before code — outer-multiplicity normalization + square-face core budget

Source remains Russell Lyons–Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056. Frozen metric remains the already certified `Phi_V(H_{5,5})=sqrt(5)` interval width `0`; this note concerns only the still-open more-general transitive-plane-graph clause for the 4-regular tetrapentagonal graph `T=r{4,5}` of face type `[4,5,4,5]`.

Immediate predecessor: `runs/R06/20260920T0935Z_i0056_threeclosure_vertex_lower_83_4f8c.md`, with

`2/(sqrt(3)+sqrt(5)-1) <= Phi_V(T) <= 384566/484385`.

## New route

Normalize an arbitrary finite set without increasing its outer-boundary ratio until every outside boundary vertex has multiplicity one after swallowing the remaining multiplicity-two layer. Then replace the original ratio by the auxiliary core quotient

`R(C)=(|partial_E C|-a(C))/(|C|-a(C))`,

where `a(C)` is the number of selected vertices of internal degree exactly two. Hole-filling and leaf-pruning can be arranged so that `R` does not increase. This reduces the global problem to a connected, hole-free, minimum-internal-degree-two plane core whose outer boundary has crossing multiplicity one.

For such a core write `a,b,d,i` for selected vertices of internal degree 2, internal degree 3, internal degree 4 on the unbounded face, and internal degree 4 off the unbounded face. Put `E=|partial_E C|`. Then

`E=2a+b`, `N=a+b+d+i`.

Let `F4,F5` be the bounded square/pentagon faces and let `L` be the unbounded-face walk length. Euler plus face-degree counting gives

`F5=E-L-4`.

Every `a`, `b`, and `d` vertex is on the unbounded face, so `L>=a+b+d`; hence

`F4 >= b/2 + i + 2d - a + 5`.

Because outer boundary multiplicity is one, every partial square has exactly two selected/unselected transitions. Thus if `Q4` is the number of partial squares, `Q4=E/2=a+b/2`. The already retained regular-tessellation face-transfer lemma and exact constant `q=Phi_V(H_{4,5})=2/sqrt(3)` give `q F4 <= Q4`, hence

`(1+q)a + (1-q)b/2 - 2q d - q i >= 5q`.  (A)

For the interior set of `i` vertices, every edge leaving it ends at an outer-face selected vertex. A degree-2 outer vertex has no edge to the interior; degree-3 and outer degree-4 vertices contribute at most 1 and 2 such edges. With the retained global edge expansion

`h=4/(1+sqrt(3)+sqrt(5))`,

we get

`h i <= b+2d`.  (B)

Taking `(A)/(1+q)` plus `lambda*(B)` with

`lambda=q/((1+q)(2+h))`

produces equal coefficients `-r` on `d,i`, where

`r = 2q(1+h)/((1+q)(2+h))
   = 2(5+sqrt(3)+sqrt(5))/((2+sqrt(3))(3+sqrt(3)+sqrt(5)))
   = 0.6897127503723662...`.

The resulting inequality implies

`(E-a)/(N-a)=(a+b)/(b+d+i) > r`.

If the normalization reductions are checked carefully, this would improve the rigorous mixed-face vertex lower bound from `0.6738274795...` to `0.6897127503...`, reducing the current certified interval width from `0.12009883937...` to about `0.10421356857...`.

## Things to verify before promoting

1. Termination and ratio monotonicity of the normalization moves, especially adding a pair of multiplicity-two boundary vertices sharing an outward neighbor.
2. After swallowing all multiplicity-two boundary vertices, the new boundary really has crossing multiplicity one and the original ratio dominates `R(C)`.
3. Hole filling does not increase `R`: every filled-hole vertex becomes internal degree 4, and multiplicity-one before filling forces the number of old degree-1 vertices promoted to degree 2 to be at most the number of filled vertices.
4. Leaf pruning preserves hole-freeness/multiplicity one and does not increase `R` when `R<1`; all-degree-two terminal degeneracies must be excluded directly.
5. The plane identities remain valid with cut vertices by using the unbounded-face boundary *walk* length, counting bridge sides twice.
6. Partial squares have exactly two transitions under outer multiplicity one, so `Q4=E/2` exactly.
7. Recheck current primary literature for an equivalent tetrapentagonal mixed-face bound or the exact edge-to-outer-core inequality; a negative search is not a novelty certificate.

Method-number history is saturated in prior I0056 work, so I will not falsely claim unused labels. Descriptively this route is #18 (say it in another language: boundary multiplicity -> plane core), #3 (prove a stronger core inequality), and #12 (extract the conserved face/curvature budget); this triple is different from the immediate predecessor’s #5/#26/#27.
