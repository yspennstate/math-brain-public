# P0257 orbit/extremal route — idea recorded before code

Planned Section-B triple for this invocation: **#14 FIND THE GROUP ACTING / #16 COMPUTE EVERY SMALL CASE / #24 FIND THE EXTREMAL OBJECT**.

The current lower bound charges positive-measure Euclidean configurations whose directed two-nearest-neighbor graph `D_2` contains a sink strongly connected component (SCC). Distinct sink SCCs are vertex-disjoint, and a non-endpoint sink SCC forces two Hamiltonian-path boundary crossings, so a qualifying shape family contributes a rigorous positive density to the NUV lower bound.

The new route is to stop hand-picking one labeled topology at a time and instead quotient the finite search by the full `S_5` relabeling action. Enumerate every strongly connected loopless 2-out digraph on five vertices, canonically quotient by isomorphism, record each automorphism-group size, and then look first at **trivial-automorphism classes**. For an ordered positive-measure Euclidean chart realizing a fixed topology `A`, the factorial-moment multiplicity penalty is at most `|Aut(A)|`; therefore an asymmetric class with `|Aut(A)|=1` can double the ordered-chart intensity relative to the just-certified `|Aut|=2` class before any geometric optimization.

For a candidate chart with normalized shape volume `V`, internal second-neighbor bound `U`, exclusion radius `H>U`, guard coefficient `Q`, and topology automorphism count `a`, the source-valid correction has the same structural form

`Delta(A,chart) = (105*pi^(3/2)/(16*a)) * V * (H-U) * Q^(-9/2)`

for five-vertex sink SCCs, after the exact finite-binomial transfer and endpoint discard already proved in the predecessor route. Thus the research objective is not smallest coordinates or prettiest topology but the explicit **intensity functional**

`J = V*(H-U)/(a*Q^(9/2))`.

I will use the finite orbit classification to identify genuinely new isomorphism classes, then search for a rational Euclidean realization with large ranking slack and trivial automorphism, and finally certify one positive-measure rational box if it beats zero and is disjoint by topology from all previously charged size-5 classes. If no such chart is found, the report will record the exact obstruction rather than manufacturing a checker for an unchanged bound.
