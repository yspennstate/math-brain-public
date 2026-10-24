# Torus defect-charge neutrality (w545, 2026-10-10)

Statement. Let K be a finite simplicial triangulation of a closed orientable surface with Euler characteristic chi, with every edge incident to exactly two triangular faces. Write deg(v) for the number of edges meeting v and q(v)=6-deg(v). Then sum_v q(v)=6 chi. In particular, on a flat topological torus the total q is zero. If every non-sixfold vertex has degree 5 or 7, the numbers of degree-5 and degree-7 vertices are equal.

Proof. Let V,E,F be the numbers of vertices, edges, and triangular faces. Double-counting incidences gives sum_v deg(v)=2E and 3F=2E. Euler's formula says V-E+F=chi. Substitute F=2E/3 to get E=3(V-chi). Therefore sum_v(6-deg(v))=6V-2E=6chi. On a torus chi=0. If degrees apart from 6 are only 5 or 7, each degree-5 vertex contributes +1 and each degree-7 vertex contributes -1, so their counts agree.

Assumptions matter: the periodic neighbor graph must actually form a closed triangulation; generic Delaunay construction on a torus needs nondegeneracy and a triangulation convention. Boundaries, missing edges, and nontriangular faces change the identity. The lemma is purely combinatorial and independent of the Riesz energy, temperature, and Gibbs measure. Neutral total charge supplies no estimate on spatial separations or defect weights and does not prove a hexatic phase.

Independent reviewer requested: w548. Status: proved special case by w545, independent audit pending. Next step: test an exact periodic Delaunay/triangulation convention for the chosen Riesz ensemble and then seek an energy/entropy estimate beyond this identity.
