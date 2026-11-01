# A response Gram need not be a graph Laplacian with positive edge weights

Exact independent counterexample, 2 October 2026. This leaves the established
H2 sum-of-squares theorem and the response-space kernel lemma intact.

Take interior E={a,b,x,y} and boundary S={s0,s1,s2}. Mark ab. Internal
conductances are ab=1, ax=4, bx=14, ay=12, by=2; there is no xy edge.
The spoke conductances, in boundary order (s0,s1,s2), are

| Interior vertex | s0 | s1 | s2 |
|---|---:|---:|---:|
|a|3|30|1|
|b|2|28|2|
|x|15|14|3|
|y|5|2|4|

The Dirichlet interior matrix and spoke matrix are

\[
 A=\begin{pmatrix}51&-1&-4&-12\\-1&49&-14&-2\\
 -4&-14&50&0\\-12&-2&0&25\end{pmatrix},\qquad
 C=\begin{pmatrix}3&30&1\\2&28&2\\15&14&3\\5&2&4\end{pmatrix}.
\]

The special unit-current potential is v=(5,-5,-1,2)^T/240. Directly,
Av=(1,-1,0,0)^T and C^Tv=0. Thus it has zero boundary flux and extends by
zero to the boundary, as required. The harmonic rows P=A^{-1}C are

\[
 P=\begin{pmatrix}
 165/1046&401/523&79/1046\\
 165/1046&401/523&79/1046\\
 933/2615&1454/2615&228/2615\\
 754/2615&1332/2615&529/2615
 \end{pmatrix}.
\]

In particular p_a=p_b. Both the eta Gram calculation and a separate raw
delta Gram minus R_e*pi*pi^T calculation give

\[
 B=\frac1{31510540800}
 \begin{pmatrix}
 96428607&-96696674&268067\\
 -96696674&149117052&-52420378\\
 268067&-52420378&52152311
 \end{pmatrix}.
\]

It is positive semidefinite, has zero row sums, and has contrast-space rank
two, as the proved kernel lemma requires. But B_(s0,s2)=268067/31510540800 is
strictly positive. Hence B cannot be written as a nonnegative combination of
ordinary edge Laplacians (e_s-e_t)(e_s-e_t)^T.

Consequently a proposed positive-weight decomposition of arbitrary marked
scores into simple boundary-edge invariants already encounters an obstruction
at its leading bilinear coefficient. A representation with signed weights or
more general response vectors is not excluded.

The small graph and exact matrix are saved in
`response_space_laplacian_small_counterexample.json`. The original search used
exact Fraction arithmetic and found this obstruction after leaving the more
restricted three-vertex and symmetric four-vertex support families.
