# R06 / I0056 — idea before code: exact Coxeter ball for a mixed-face vertex upper bound

Status at creation: **CONJECTURAL UNTIL THE EXACT CHECKER PASSES**.

The frozen first-clause metric is already zero-width: `Phi_V(H_{5,5})=sqrt(5)`. The still-open source clause asks for `Phi_V` on more general transitive plane graphs. Continue with the established tetrapentagonal graph

\[
T=M(H_{5,4})=r\{4,5\},
\]

a 4-regular vertex-transitive plane graph with alternating face type `[4,5,4,5]`.

The inherited rigorous mixed-face vertex interval is

\[
\frac1{\sqrt3+\sqrt5-2}\le \Phi_V(T)\le \frac2{\sqrt5}.
\]

The previous run reduced the candidate sharp **edge** constant to a boundary-turn inequality. Before spending another run on that same obstruction, attack the source's **vertex** quantity directly.

## New route

Use the exact Coxeter reflection group `[4,5]` over `Q(sqrt(2),sqrt(5))` to develop the regular base tessellation `{4,5}` without floating point, then form its medial graph exactly. A graph-distance ball in the medial graph is an explicit admissible finite set for the outer-vertex Cheeger ratio. This changes the category from hyperbolic geometry to exact algebra, attacks the possibility that the old upper `2/sqrt(5)` is already close to sharp, and computes all small shells rather than sampling an embedding.

A preliminary nonrigorous scout suggested the radius-9 medial ball has

\[
|B_9|=1783,\qquad |\partial_V B_9|=1528,
\]

so, if the exact development confirms these counts,

\[
\Phi_V(T)\le \frac{1528}{1783}\approx0.8569826<\frac2{\sqrt5}\approx0.8944272.
\]

The exact checker must independently verify the Coxeter relations, exact shell counts, full degree 4 on every medial vertex needed to determine `B_9` and its outer boundary, and the integer inequality

\[
5\cdot 1528^2<4\cdot1783^2.
\]

No finite count will be called proved until that checker is executed and its output archived.

Methods for this run: **#1 CHANGE THE CATEGORY, #2 ATTACK THE NEGATION FIRST, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE.**
