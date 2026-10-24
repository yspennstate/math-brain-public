# FOREST-KN-TO-ALL-SOURCE-CLOSURE-v1

Producer: account03/B03  
Recipient: assigned partner account04/B01; FOREST lead/review workers  
Context: WITHOUT_VERIFIED_BRAIN  
Outcome: ESSENTIAL_STEP_APPLIED; parent problem not promoted to solved.

## Result to consume

The complete-graph-to-all-simple-graphs implication is source-valid:

1. If Conjecture 1.1 holds for a fixed graph `G`, the final Semple--Welsh paper explicitly records Cocks's theorem that `M(G)` is independence correlated.
2. Independence correlation means the forest/independent-set Rayleigh inequality holds for every positive real edge weighting.
3. Semple--Welsh Proposition 3.5 proves independence correlation is minor-closed.
4. Every finite simple `n`-vertex graph `H` is obtained by edge deletions from `K_n`; hence `M(H)` is a deletion minor of `M(K_n)`.
5. Setting weights to one recovers the uniform law on all forests of `H`, with disconnected forests, the empty forest, and all sizes retained.

Therefore `pNC(K_n) for every n => pNC(H) for every finite simple H`. This resolves the all-graphs globalization gap conditional on the current complete-graph proof candidate.

Source anchors: Semple--Welsh, CPC 17 (2008), Section 2 definition; Proposition 3.5; final added note on Cocks. Cocks, *Correlated Matroids*, CPC 17 (2008), 511--518, DOI 10.1017/S0963548308009152.

Named partner input consumed: account04/B01 report commit `3b53272eba18cdec04e029651173b1410e3b8b12`, whose exact two-cut gluing/3-connected reduction uses this fixed-graph upgrade.

## New exact adversary witness

On the 5-vertex simple graph with edges `{02,03,04,12,13,14,23}`, mark `e=02,f=13,g=23`. For variable weight `w` on `g`, exact all-forest counts give

`Q(w)=36-2w+4w^2`.

Thus the mixed coefficient is negative although `Q(w)>0` for every `w>0` (discriminant `-572`). Exhaustive labelled checks show no negative mixed coefficient on 3 or 4 vertices. This rules out coefficientwise positivity as a universal weighted-proof mechanism.

Checker SHA-256 `e426a3d8b71b0a8ef537c4decf10561a5e7f337863c159498841619a25efe571`; output SHA-256 `a7f20ff34ee9d8aa444ef4536901643620906c5f38ddfdc241f37be33132cd0c`.

## Next gate

Do not spend another run re-proving globalization. Independently audit the full `K_n` Stark/Hermite/Jensen proof end-to-end. If it passes, combine it with this source closure to obtain the parent theorem; if it fails, isolate the first false identity/sign step.
