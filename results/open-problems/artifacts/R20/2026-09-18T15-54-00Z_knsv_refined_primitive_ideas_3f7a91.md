# R20 KNSV refined-primitive ideas before code

Model request in task text: GPT-6 / maximum. Actual runtime model: GPT-5.6 Sol; reasoning telemetry UNVERIFIED.

Current exclusive target: `operations/claims/KNSV-2026-LOOPY-U.md`, not retired Paley I0100. Frozen metric is `N_sep>11`.

This run deliberately starts from three new Section-B moves, not the preceding #11/#19/#24.

## #4 PROVE SOMETHING WEAKER, COMPLETELY

The first hidden block layer isolated previously is `(4,3,1^{n-7})`. Instead of trying to reconstruct all transformed block layers, characterize when this layer is automatic. The concrete algebraic target is: identify graph classes for which the hidden vector `(h1,h2,h3)` is forced by ordinary block data, and prove the formula. A useful result must cover graphs with triangles, not merely repeat the triangle-free case.

## #20 FIND WHY THE ALGORITHM FAILS

The exact seven-vertex dual certificate from the preceding run kills universal *linear* local recovery of `h1`. The next question is whether any nonlinear local recovery can be lifted to arbitrary `n` using only ordinary U. I will isolate the exact lifting obstruction: ordinary U stores one symmetrized product for each block-size profile, but a nonlinear function of a seven-vertex local U-vector creates cross-terms that require overlap-labelled data not present in ordinary U. I will seek either a clean impossibility theorem for a natural class of nonlinear lifts or a specific nonlinear identity that survives symmetrization.

## #27 SWAP THE QUANTIFIERS

Do not enumerate all 12-vertex graphs. Search first for *refined-primitive* collision mechanisms: transformations that start from a known ordinary-U collision or from the source's five-vertex multigraph U-collision and produce a simple graph pair whose ordinary-U equality can be checked exactly but whose refined information can split. The most promising concrete maps are simple graph functors applied to the source multigraph pair: line graph, incidence graph / barycentric subdivision, total graph, and small two-terminal desingularizations. These are not the already-killed one-root, join, or independent-subdivision routes. If any functor preserves ordinary-U equality for this specific pair while changing the loopy fingerprint, it gives an exact source-level refutation.

Only after one of these routes yields a concrete theorem/candidate will I build or extend an exact checker. Negative computational output is PARTIAL only and does not move `N_sep`.
