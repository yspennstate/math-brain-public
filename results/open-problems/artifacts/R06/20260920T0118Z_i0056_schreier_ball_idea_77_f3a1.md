# R06 idea before code — direct Schreier growth for the tetrapentagonal graph

Source remains Lyons–Peres Question 6.20 / I0056. The frozen regular/co-regular metric is still the already certified `Phi_V(H_{5,5})=sqrt(5)` with width zero. This note concerns the still-open “more general transitive plane graph” clause, for the tetrapentagonal graph `T=r{4,5}=M({4,5})`.

Methods for this run: **#12 FIND WHAT IS CONSERVED, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.** These differ from the preceding run's #1/#2/#16.

## #14 — quotient the Coxeter action directly

The previous exact checker developed the primal `{4,5}` tessellation and then built its medial graph. That is unnecessary. In the Coxeter group `[4,5]=<s1,s2,s3>`, let `r=s2 s3`; `r` has order five and rotates the five primal edges at one endpoint of a fixed primal edge. The other endpoint is obtained by `s1`, so `q=s1 r s1` rotates the five primal edges at that endpoint.

A scaled midpoint of the fixed primal edge is

`M=(sqrt(2), 2, phi)`, `phi=(1+sqrt(5))/2`.

It is fixed by `s1` and `s3`. Thus the medial graph is the exact Schreier/orbit graph generated from `M` by the four degree-four moves

`r, r^{-1}, q, q^{-1}`.

All matrices lie in the integral ring `Z[a,b]`, with `a^2=2`, `b^2=b+1`; no floating-point identification is needed.

## #19 — exact breadth-first algorithm

Run BFS directly on exact orbit vectors in `Z[a,b]^3`. Because the four generators are the complete set of medial neighbors, a radius-`R` BFS certifies every sphere through `R`; for a graph ball `B_{R-1}`, its outer vertex boundary is exactly sphere `S_R`.

The immediate target is to extend the previously certified radius-10 development far enough to find a strictly smaller exact ball ratio than `1528/1783`.

## #12 — look for a finite growth invariant

The already observed sphere counts strongly suggest that after a short transient the generation process closes on finitely many cone/face-position types. If the new exact shells satisfy a short integer recurrence for many consecutive generations, record that recurrence only as a **candidate structural invariant** unless an all-generation face-position induction is proved. It can guide the next run toward a rational growth function, but it must not be used as an infinite theorem in this run.

A rigorous finite ball improvement, if found, is independent of that conjectural recurrence and can be promoted immediately with the exact BFS certificate.
