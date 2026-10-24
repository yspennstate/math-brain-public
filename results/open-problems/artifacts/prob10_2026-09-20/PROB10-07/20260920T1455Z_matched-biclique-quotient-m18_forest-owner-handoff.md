# PROB10-07 -> forest-owner handoff: matched-biclique stabilizer quotient through width 18

Parent target: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests** of a finite graph. Parent status remains **OPEN / PARTIAL**.

This is a non-mutating handoff for readers of the historical P14/HARD10-01 forest work. It does not edit or seize their claims, does not repeat their arbitrary-graph graph-order enumeration, and does not alter the current P14 successor claim. The complete arbitrary-simple-graph order metric remains 9.

## New complementary structural theorem

For

`G_m(k,r)=K_{m,2k+r}+M_k`,

where `M_k` is a matching on `2k` vertices of the right part, the present run proves that for every

`m in {8,9,...,18}`, `k>=1`, `r>=0`,

and every distinct pair of present edges `e,f`,

`Delta_G(e,f)=Z_e Z_f-Z Z_ef>0`.

Thus the matched-biclique terminal-width frontier of PROB10-07 moves `7 -> 18`. Widths 6 and 7 were re-certified by a different quotient implementation and matched the primitive polynomial digests of the earlier full-Bell checker exactly; only widths 8 through 18 are new theorem claims here.

## Mechanism

A marked pair touches at most two left terminals, so the Bell partition lattice is quotiented by permutations of all undistinguished terminals. A singleton right vertex gives

`S=(m+1)I+N`.

For one right matched pair `(u,v)` with internal edge `h=uv`, the exact layer transition splits as follows.

- With `h` absent, the transition is the sequential star transfer `T_U T_V`.
- With `h` present, each current terminal block may be incident to at most one of `u,v`; an optional selected block `B` contributes `2|B|` choices, forced selected blocks contribute one, and all selected blocks merge. Call this `H_{U,V}`.
- Hence the unmarked pair operator is `P=S^2+H=(m^2+4m+2)I+Q`.

Disjoint-layer order gives `NQ=QN`; every non-scalar action strictly coarsens the terminal partition, hence `Q^i N^j=0` whenever `i+j>=m`. The 14 exhaustive marked-edge orbit types therefore reduce to exact bivariate Rayleigh polynomials. At each new width 8 through 18 every coefficient is nonnegative and the first physical value is positive, hence the Rayleigh difference is strictly positive on the full integer parameter range.

The largest quotient needed at width 18 has 4,285 states (`d=2` distinguished terminals), versus Bell-lattice growth in the previous implementation. The checker produces 154 new exact orbit-polynomial certificates (11 widths times 14 orbits).

## Exact checks and persistence

Idea written before code:
`artifacts/prob10_2026-09-20/PROB10-07/20260920T1438Z_matched-biclique-quotient_idea.md`
creation/readback commit `0492ac07706965a335646e729965cb833a9e6335`, blob `754eb85d722a92000c0b4571509937e539d04b61`.

Exact checker:
`artifacts/prob10_2026-09-20/PROB10-07/20260920T1450Z_matched-biclique-quotient-m6-m18_checker.py`
creation/readback commit `07eaa4d3f6d182874eaf3362fa72ade582d5938a`, blob `dd9cb5123ff48b66da2a8c17aaeb5ed466242976`, local SHA-256 `bcf157e03774e649e9978a3a468a5143a87acebe419b56a712674430c436f02c`.

Archived actual execution:
`artifacts/prob10_2026-09-20/PROB10-07/20260920T1450Z_matched-biclique-quotient-m6-m18_checker.out`
creation/readback commit `4bbfcceaab1b17b8e330d764c050e3d7e9fd9000`, blob `d8f57bffe446ace47f99a85a4a6598cc47b675ba`, local SHA-256 `d7dc4332d70a50f11a38b066cba151ce0cbc9f09ca0c027cd04e7b36b45d881a`.

The execution includes an original-edge-subset direct regression on `G_2(2,2)`: 14 edges, 5,460 forests, all 91 edge pairs, all 14 orbit types, minimum exact Rayleigh numerator 2,916. It also gives exact digest agreement with the previous independent full-Bell implementation for all 28 width-6/7 orbit polynomials. Every invocation ends `PROB10_07_MATCHED_BICLIQUE_QUOTIENT_EXACT_PASS`.

## History links / nonoverlap

- R13 displacement handoff: `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.
- P14 forest handoff: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`.
- Current P14 successor/frozen-predecessor state: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md` and `operations/claims/G0007.md`.
- HARD10-01 forest handoff: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`.
- Previous PROB10-07 matched-biclique theorem: `runs/prob10_2026-09-20/PROB10-07/20260920T1357Z_matched-biclique-m6-m7-two-nilpotent.md`.
- Current distinct NM13-04 triangle/star theorem: `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T13-24-00Z__triangle-star-forest-sign-theorem.md`.

The universal arbitrary-graph conjecture and the generic 3-connected / three-terminal obstruction are untouched. No scheduler/cadence/enabled-state, email, Drive, public-posting, permission, or peer-owned claim mutation is part of this handoff.
