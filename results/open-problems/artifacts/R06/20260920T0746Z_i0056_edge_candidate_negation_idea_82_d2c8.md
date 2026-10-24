# R06 / I0056 — idea before archival checker: attack the tetrapentagonal edge candidate instead of proving it

Source remains Russell Lyons–Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056. The frozen regular/co-regular target remains `H_{5,5}={5,5}` with outer-vertex constant `Phi_V(H_{5,5})=sqrt(5)` and interval width zero. This note concerns only the still-open more-general transitive-plane-graph clause through the source-valid tetrapentagonal graph `T=r{4,5}`.

The current rigorous mixed-face state is

`1/(sqrt(3)+sqrt(5)-2) <= Phi_V(T) <= 384566/484385`,

and the older edge interval is

`4/(1+sqrt(3)+sqrt(5)) <= Phi_E(T) <= 2/sqrt(5)`.

The preceding route reduced the conjectural sharp edge value `2/sqrt(5)` to a weighted turn inequality for every realizable quadrangulated disk, but the stronger radial shortcut was later refuted. Before spending another run trying to prove the turn cap, attack its negation exactly.

## Move #22 — READ THE FAILURES, NOT THE SUCCESSES

The failed radial shortcut is evidence that the candidate edge equality itself should be stress-tested, not protected. A single finite set with edge ratio below `2/sqrt(5)` rigorously kills the candidate and the disk turn cap.

## Move #6 — DEFORM TO A POINT YOU CAN SOLVE

For a rational threshold `r=p/q`, deform the infinite edge-Cheeger question to the finite exact decision problem

`exists K subset B_R : q*|partial_E K| - p*|K| < 0`,

where all four neighbors of every selectable vertex are still charged, including neighbors outside `B_R`. This is an integer `s-t` cut: source-to-vertex capacity `p`, graph-edge capacity `q`, and sink capacity `q` for every edge leaving the selectable ball. Any positive closure surplus returns an actual finite set in the infinite graph, hence a rigorous upper bound; failure at one radius is not promoted to a lower bound.

The plan is to start below `2/sqrt(5)` and lower the rational threshold until the finite cut no longer has positive surplus, increasing the radius only while the ratio continues to move.

## Move #9 — RANDOMIZE

Before building the exact cut certificate, try random two-shell deformations of a smaller exact ball as a cheap counterexample generator. This route is deliberately expendable: if random perturbations do not beat the candidate quickly, abandon them rather than certifying noise. The exploratory sample did not get close enough (best edge ratio was above `1.06`), so the exact threshold deformation is the useful route.

The archival checker, if the cut succeeds, must reconstruct the exact Coxeter graph over `Z[sqrt(2),phi]`, rerun the integer max-flow, reconstruct the returned set, count every crossing edge directly, and compare the resulting rational ratio to both the previous edge upper bound `2/sqrt(5)` and the retained edge lower bound. No floating-point comparison will support the claim.
