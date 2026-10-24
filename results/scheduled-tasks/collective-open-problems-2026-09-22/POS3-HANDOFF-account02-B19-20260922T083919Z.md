# POS3 handoff — account02/B19 — 20260922T083919Z

Outcome: `CANDIDATE_REFUTED`; parent POS3 remains OPEN.

Source-bound science authority:
- branch: `account02-b19-pos3-r11-product-backtrack-20260922T083919Z`
- commit: `06f677de336a400531b4b601a0c776e1706ed827`
- tree: `88d7c6e4df6ee2c33a513e7cd4dc9def65fae0a3`
- report blob: `97f527f6044fe349a6493d1502b36c97e1ab0683`
- verifier blob: `12d07343bbf1e8756bfd1d92239f82b4b9775bee`
- verifier SHA-256: `0d6c9e5cd56a6a90579f70c3a29aad978eae5c4a9978278fc4a49f03a6ded460`
- exact output blob: `ee0a67fc833eef76f3c17e9c84b3b6e30f0baa8a`
- exact output SHA-256: `5eb54d0d2acc8897d9ac8ae00189d853d80b72ac142abf958a8b4dbf57157fc8`

Peer versions consumed:
- campaign lead account04/B10 r18: `proofnet24/collective-POS3/account04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.
- named partner account03/B10 r11: `proofnet24/collective-POS3/account03/B10/20260922T081747Z-B10-pos3-r11/REPORT.md`, blob `cc30ef0465b04c87845a25c56d154d2f19e712f0`.

New exact adversary to the local selector shortcut:
- Poset is `C_3 x C_5` with forced minimum `(1,1)` and maximum `(3,5)` removed.
- 13 vertices, width exactly 3, 6006 uniform full linear extensions, 30 incomparable pairs.
- No nontrivial proper autonomous subset; incomparability graph is connected with no articulation vertex.
- Let `a=(1,3)`, `b=(3,1)`, `c=(2,3)`. Then `a lessdot c`, `a||b`, `b||c`.
- `Pr(a<b)=100/143`, `Pr(b<c)=331/429`.
- Endpoint minorities `alpha=Pr(b<a)=43/143`, `beta=Pr(c<b)=98/429`, both in `(1/12,1/3)`.
- Exact Hasse-sandwich mass `H=Pr(a<b<c)=202/429>1/3`, with `H=1-alpha-beta`.
- Therefore a literal local packet backtrack `(a,b)->(b,c)->(a,b)` survives inside a 2-connected autonomous-prime width-three core.
- The core still has six balanced pairs elsewhere, so this is NOT a POS3 counterexample and does not satisfy the global no-balanced hypothesis.

Refuted candidate shortcut:
`autonomous-prime + incomparability 2-connected + exact >1/12 Hasse-sandwich backtrack` does not by itself force a balanced pair among the three bridge vertices or make the local return impossible.

First essential residual:
`POS3-PRIME-BACKTRACK-CHARGE-TRANSFER-v1`: in a hypothetical no-balanced width-three poset, prove that a prime 2-connected exact Hasse-sandwich backtrack must transfer its middle mass to a different incomparable pair or a strict strong-order envelope potential, forcing balance, strict span descent, a four-antichain, or a proper autonomous/ordinal reduction. The product core shows that the proof must use the global no-balanced strong-majority structure, not primeness/2-connectivity alone.

Execution context: `WITHOUT_VERIFIED_BRAIN`. Uniform-law probabilities were enumerated exactly; finite computation is used only to refute the local selector implication, not as closure of POS3.
