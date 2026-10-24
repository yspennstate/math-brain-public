# FOREST-CUBIC-TERMINAL-PARTITION-v1

Producer: account03/B03  
Recipient: assigned partner account04/B01; FOREST lead/review workers  
Context: WITHOUT_VERIFIED_BRAIN  
Outcome: ESSENTIAL_STEP_APPLIED; parent FOREST target remains OPEN.

## Named partner consumed

Consumed account04/B01 report commit `3b53272eba18cdec04e029651173b1410e3b8b12`. Its exact two-cut gluing plus the fixed-graph Cocks upgrade implies any edge-minimal simple counterexample is 3-vertex-connected.

## Exact cubic-vertex theorem

Let `v` have degree three with neighbors `u1,u2,u3`, and let `H=G-v`. Partition weighted forests of `H` by terminal connectivity masses `A` (`1|2|3`), `B12`, `B13`, `B23`, and `C` (`123`). Put `T=A+B12+B13+B23+C`.

For the unit star edges `e1=vu1,e2=vu2,e3=vu3`, exact enumeration of allowable star subsets gives

`Z = 8A + 6(B12+B13+B23) + 4C`,

`Z_1 = 4A + 2B12 + 2B13 + 3B23 + C`,

`Z_2 = 4A + 2B12 + 3B13 + 2B23 + C`,

`Z_12 = 2A + B13 + B23`,

hence

`Delta(e1,e2)=4 B12 T + (B13+C)(B23+C) >= 0`.

Thus every pair of edges incident to a degree-three vertex is negatively correlated under the source law. The conclusion remains valid if all edges of `H` have arbitrary positive weights while the three star edges remain unit weight. Empty/disconnected forests and all sizes are retained.

If `G` is 3-connected, then `H` is 2-connected, so there is a `u1-u2` path avoiding `u3`; therefore `B12>=1` and

`Delta(e1,e2) >= 4 F(H) > 0`.

Combined with the partner reduction: in any edge-minimal counterexample, which must be 3-connected, a violating pair cannot be two edges incident to a cubic vertex. In particular, in a cubic 3-connected candidate every violating pair must be vertex-disjoint.

## Weighted diagnostic

If only `e3` is given weight `g>0`, then

`Delta_12(g)=L g^2 + 2 B12 T g + (B12+C)T`,

where

`L=A B12-A C+B12^2+B12 B13+B12 B23+B13 B23`.

`L` is itself the unit Rayleigh difference for the two edges `u3u1,u3u2` added to `H`. This identifies the precise obstruction to extending the manifest unit factorization to arbitrary third-edge weight. If an added edge duplicates an existing simple edge, a separate parallel-edge/weight argument is required; no simple-graph minimality shortcut is claimed.

## Exact regression

Standard-library exhaustive checker: all 64 simple `H` on four labelled vertices, direct all-forest enumeration, unit identity and `g=2,3,5`; plus four positive-integer-weight stress cases. Result `PASS`.

Checker SHA-256 `2bfd54ddf871ef6c6e56ba1795a758c63214ffd59ce1c7cbef015d0cc707603a`; output SHA-256 `23d7c30ca04e6612dd16f994be7813ab0c85e43d88b0a6f4c0b103fa6395e1b1`.

Full report root: `proofnet24/P14-probability-correlation/collective-2026-09-22/account03/B03/20260922T055815Z-account03-B03-forest-r12/`.

## Next use

Use this theorem as a strict local exclusion in any renewed minimal-counterexample route. The current shortest team closure still depends on independently validating the complete-graph Stark/Hermite/Jensen theorem; if it passes, the already source-checked Cocks/minor globalization closes the all-simple-graphs implication.
