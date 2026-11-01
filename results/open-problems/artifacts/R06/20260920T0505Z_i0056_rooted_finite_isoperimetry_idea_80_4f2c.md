# R06 / I0056 — idea before checker: attack round-ball near-optimality by exact rooted finite isoperimetry

Status at creation: **RESEARCH IDEA / NO NEW CLAIM YET**.

Source remains Russell Lyons–Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake `I0056`. The frozen regular/co-regular target is still `H_{5,5}={5,5}` with the already certified `Phi_V(H_{5,5})=sqrt(5)` and width zero. This note concerns only the still-open second source clause through the vertex-transitive tetrapentagonal graph

`T = r{4,5}` of cyclic face type `[4,5,4,5]`.

The preceding R06 report proved the all-radius three-state frontier anatomy and the exact graph-distance shell recurrence, then showed that the asymptotic round-ball ratio is strictly worse than the current finite witness `113708/133611`. Therefore another larger round ball is the wrong object.

## New methods this run

- **#2 ATTACK THE NEGATION FIRST.** Attack the implicit extremal guess that centered metric balls, or a one-shell perturbation of them, are close to optimal for `Phi_V(T)`. Search directly for a finite set with smaller outer-vertex-boundary ratio.
- **#24 FIND THE EXTREMAL OBJECT.** Freeze a large rooted finite domain `B_R(o)`. Since `T` is transitive, any finite set may be translated to contain `o`; within the frozen domain solve the exact combinatorial minimization of `|partial_V K|/|K|` over `o in K subset B_R(o)`. This is a finite optimization only; its optimizer is a witness, not a proof of the infinite constant.
- **#19 MAKE IT AN ALGORITHM.** Encode selected vertices by `x_v in {0,1}` and potential boundary vertices by `y_w in {0,1}`. For every directed adjacency `v~w`, impose `y_w >= x_v-x_w` (with `x_w=0` outside the frozen domain), together with `x_o=1`. Dinkelbach linearization at a trial rational `lambda` minimizes `sum y - lambda sum x`. Once a better set is found, discard solver optimality as a theorem claim and archive only the explicit finite witness plus an independent exact-arithmetic boundary recount.

## What would count as movement

A valid improvement must exhibit an explicit finite `K subset V(T)` and exact integer counts `|K|=N`, `|partial_V K|=M` with

`M/N < 113708/133611`.

Only that exact witness inequality will be promoted. A solver objective, floating geometry, sampled ratio, or claimed optimum without an exact recount will not be called a rigorous bound.

## Structural diagnostic to record if the search succeeds

For any optimizer, record shell occupancies. If it consists of a full inner ball plus only one or two partially occupied outer shells, this is evidence for a boundary-layer/Wulff-shape route: the arbitrary-set isoperimetric problem may reduce to a finite-state cyclic optimization on the already proved frontier automaton. That would be mathematically more useful than merely increasing the frozen radius.
