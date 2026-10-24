# FOREST handoff — account03/B02 — source closure of complete-graph reduction

**Run:** `20260922T032505Z-account03-B02-r11`  
**Outcome:** `FULL_PROOF_CANDIDATE` under the collective internal gate; no external solved-problem/novelty/priority claim.  
**Context:** `WITHOUT_VERIFIED_BRAIN`.

Consumed named assigned-partner result: **account04/B03**, `account04-B03-20260922T030927Z-full-candidate-integration.md`, blob `27dfbf71a18abf0c89d52c8aaaf11d6c037d2d19`. That handoff identified direct Cocks-source scrutiny as the remaining diligence item.

This run independently retrieved the final author-hosted Semple--Welsh paper and verified the exact fixed-graph dependency used by the lead: the Section 5 Note says that Cocks proved that if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. In the same final paper, independence correlation is defined for **all positive real weightings**, and Proposition 3.5 proves that the class is closed under minors. This is the required pointwise upgrade; it is distinct from the older class-level parallel-copy argument that earlier workers correctly rejected.

I also independently verified the published Cocks record: Clifford C. Cocks, *Correlated Matroids*, CPC 17(4) (2008), 511--518, DOI `10.1017/S0963548308009152`; Cambridge's abstract says it establishes the graphic-matroid equivalences and settles Semple--Welsh open questions. The full Cocks article body was not openly retrievable in this run, so no line-by-line audit of his proof is claimed.

The all-graphs chain is therefore source-closed at the theorem-statement level:

`unit pNC on every K_n -> Cocks fixed-graph all-positive-weight independence correlation of M(K_n) -> Semple--Welsh minor closure -> every finite simple G as a deletion subgraph of K_n -> unit weights`.

I also re-audited the fragile Hermite algebra. For `k=n-4`, `s=k He_(k-1)(n+1)/He_k(n+1)`, the disjoint orbit has gap `He_k(n+1)^2 G_n(s)` with the previously stated `G_n`. The lower bound `s >= (n-4)(n-1)(n+4)/(n+1)^3`, `s<1`, monotonicity on `[0,1]`, and the shifted polynomial

`2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396`

were independently recomputed; no new gap was found. The disjoint orbit remains harder than the adjacent orbit by exactly `Z_n He_(n-4)(n+1)>0` for `n>=4`.

Canonical scientific report: `yspennstate/math-open-problems`, commit `ac6005d73a168d645e246b905671d2cd9b468dfc`, path `proofnet24/P14-probability-correlation/collective-2026-09-22/account03/B02/20260922T032505Z-account03-B02-r11/source_closure_review.md`.

**Earliest remaining diligence:** obtain the full published Cocks article body and line-check the proof, then ordinary external expert scrutiny of the complete candidate. This is validation/publication diligence rather than an unpaid universal implication. Recipient: FOREST lead `account01/B01` and assigned partner `account04/B03`. Do not silently switch account03/B02 to a successor target without later owner approval.
