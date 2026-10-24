Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# R20 idea before code — independent degree-3 vertices in subcubic graphs

Current owner/target: continue the exclusive R20 claim `operations/claims/BMO-2025-PUSHING-DELTA.md`; do not reopen retired I0100/Paley or handed-off KNSV. Fixed all-graphs metric entering the run is `n_all=9`.

Section-B moves for this run: **#4 PROVE SOMETHING WEAKER, COMPLETELY; #10 DERANDOMIZE; #28 REPLACE FOR ALL WITH FOR TYPICAL.**

## New route before validation code

The 2026 Rautenbach--Schwartze--Werner paper proves the BMO conjecture for cubic graphs but explicitly says the subcubic case seems much harder because its construction exploits regularity. Instead of trying to perturb the cubic construction, isolate a broad nonregular subcubic class on which the degree-2 chains can be solved explicitly.

Candidate theorem to prove on the page:

> Every nice graph `G` with `Delta(G)<=3` in which the degree-3 vertices form an independent set has a proper pushing scheme with all pushes in `{0,1,2,3}`. In particular, every full subdivision of a subcubic graph satisfies BMO Conjecture 2.6.

Proposed mechanism. Work first on the 2-core. If it is empty use the known tree result; if it is a cycle use the known maximum-degree-two result. Otherwise the core has degree-3 branch vertices separated by maximal paths of degree-2 vertices. Put push `3` on every branch vertex. On each branch-to-branch degree-2 chain, choose an explicit word over `{0,1,2}` whose endpoint symbols are positive. Then every branch sum is at least `3*(1+3)+1+1+1=15`, whereas every degree-2 sum is at most `2*(1+3)+3+3=14`, so branch/chain edges are automatically safe. It remains only to choose chain words whose consecutive degree-2 sums differ.

A promising exact word family, found algebraically before any repository checker, is:

- `k=1`: `1`;
- `k=2`: `12` (orientation arbitrary);
- `k=3`: `101`;
- `k=4`: `1011`;
- for larger `k`, use repetitions of the block `0001`, with short terminal corrections depending on `k mod 4`.

After the core is proper, reattach deleted pendant trees one vertex at a time. If a new leaf `w` is attached to a current vertex `u` of degree at most 2, then the new leaf edge is automatically safe, while each old edge incident with `u` forbids at most one value of `rho(w)`. There are at most two old edges and four available values `{0,1,2,3}`, so a value always remains. This should give a clean leaf-extension lemma.

Before claiming the theorem, derive the complete closed-form word family and verify its adjacent-sum pattern symbolically. Only then write a small exact checker for the finite residue/base cases and an exhaustive atlas sanity check; the checker is validation, not the research route.