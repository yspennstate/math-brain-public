# Bradley Question 5 — source-scope proof package

Status: **candidate source-level proof / protocol closure pending independent audits**.

Owner: `R7-01 Counterexamples and Constants`  
Native ID: `6aabe777361481919c9e614646464772`  
Canonical target: `D0033`  
Own root: `research7_2026-09-17/R7-01/`

## Source and exact scope

Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, *Probability Surveys* 2 (2005), 107–144, DOI `10.1214/154957805100000104`, arXiv `math/0511078`, Question 5 in Section 3, printed p. 119 / source-PDF p. 13:

> If a given Markov chain is phi-mixing, does it follow that it is rho-star-mixing?

The repository canonical claim scopes this to strictly stationary Markov chains. The argument in `main.tex` is formulated in Bradley's Section-3 real-state Markov-chain setting and does not use stationarity, so in particular it covers the canonical stationary claim.

## Claimed theorem in this package

For Bradley's coefficients, the proof gives the quantitative estimate

`rho_star(n) <= min(1, 4*sqrt(2*phi(n)))`.

Consequently `phi(n) -> 0` implies `rho_star(n) -> 0` for a Markov chain.

The proof has three ingredients:

1. phi-mixing forces every n-step Markov row, outside one null set, to lie within `phi(n)` in total variation of the corresponding unconditional future marginal; hence the diameter of the family of rows is at most `2 phi(n)`.
2. This row-diameter bound survives arbitrary conditioning on the earlier history, giving maximal correlation at most `2 sqrt(2 phi(n))` across any opposite-colour adjacent block boundary.
3. Order an arbitrary finite interlacing into maximal monochromatic blocks. Peyre's `N against M` maximal-correlation tensorization theorem, in the minimal-hypothesis form of Section 3.4(a), reduces the global correlation to the operator norm of the bipartite path matrix. Nonadjacent opposite-colour blocks have subjective correlation zero by the Markov property; adjacent blocks have the bound in item 2; the path norm is at most twice the edge weight.

Infinite coordinate sets follow by finite-coordinate `L^2` approximation.

## Dependencies and prior-art status

The key external tensorization input is Rémi Peyre, *Tensorizing maximal correlations*, arXiv:1004.1602v2 (2010), Theorem 3.3.1 together with the minimal-hypothesis refinement in Section 3.4(a). Bradley's own standard inequality `rho(A,B) <= 2 sqrt(phi(A,B)) sqrt(phi(B,A))` is also used.

A bounded literature search dated 2026-09-17 recovered Bradley's source, later copula/lower-psi sufficient-condition papers, Bradley's later INAR/interlaced-rho work, and Peyre's tensorization monograph, but did not locate a paper explicitly identifying this implication or resolving exact Question 5. That negative search is **not** a novelty certificate. In particular, the mechanism may already be implicit in the post-2010 maximal-correlation literature.

## Verification and closure state

- Full written proof: `main.tex`.
- Finite-core checker: not applicable; this is an analytic theorem with no finite computational core.
- Self-check: R7-01 only; not an independent audit.
- Required independent P26 audit: **missing**.
- Required distinct OTHER-track audit: **missing**.
- Protocol closure: **NOT CLOSED** until both independent audits pass and prior-art review is adjudicated.
- Public posting: none authorized or asserted.

No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` file is modified by this package.