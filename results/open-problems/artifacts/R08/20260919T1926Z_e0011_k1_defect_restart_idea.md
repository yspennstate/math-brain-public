# R08 E0011 — idea before production checker: one-defect repair budget for the width-10 restart class

Run: 2026-09-19 UTC. Methods selected by the preceding report: **B5 / B18 / B30**.

Entering frozen source metric: `B_cat >= b21_desc`, with diagnostic `log10(b21_desc) ~= -48.42893853604687` and supported unchanged count `5`. Under the six-unchanged CLOSABLE rule, this invocation must retire E0011 unless it actually improves the source-valid two-child block metric.

The preceding exact `k=0` clean-manifold test showed that the width-10 fuel-strip restart architecture is far too brittle if every CO/O defect excursion is declared fatal. The next materially different test is therefore to add a **defect-budget parameter** rather than optimize another prescribed word.

## B5 — add a parameter

Let `S_0` be the 1024 clean fuel-rail states indexed by the consumed first-rail subset. Define `S_1` to be the set of all physical 44-cell configurations at Hamming distance at most one from `S_0`. Thus one arbitrary cell may disagree with some clean state, while the remaining cells lie on the clean manifold. The successful terminal state is still the exact clean fully translated seed. Leaving `S_1` is fatal for this finite deformation.

This is deliberately only a fixed-all-CO-exterior, one-child deformation. Even a good result here would not by itself move `B_cat`; it is a diagnostic of whether a single repairable defect changes the restart mechanism by orders of magnitude.

## B18 — say it in another language

The flat unrestricted 44-cell process has more than 1.6 million reachable states by depth five. `S_1` can instead be viewed as a one-dimensional rail mask plus one marked defect location/type. The expected physical state count is small enough for an exact full-event kernel, while still admitting the first nontrivial repair excursions excluded by `S_0`.

## B30 — one scale / one direction at a time

The first repair scale is exactly one defect. Do not add two-defect or full-patch states unless the one-defect calculation shows a plausible route toward the required restart ratio. Enumerate every owned internal CO and O2 event, all reaction-choice branches, keep transitions inside `S_1`, and send every other outcome to FATAL. Solve SUCCESS-before-FATAL with rigorous integer-grid lower and upper Bellman iterations.

Decision rule for this run: if this finite deformation does not yield a new complete universal-exterior two-child block certificate, `B_cat` has not moved; the unchanged count reaches six and E0011 is handed off/retired from active R08 research rather than receiving a seventh unchanged attack.