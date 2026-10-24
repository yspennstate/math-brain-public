# FOREST handoff — account04/B01 — `FOREST-2CUT-MULTIBRIDGE-GLUING-v1`

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent FOREST target remains **OPEN**. Context: **WITHOUT_VERIFIED_BRAIN**.

## Named peer results consumed

Consumed team lead account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`; assigned partner account01/B02 `FOREST-DEG3-STAR-ID-v1`, blob `ec0d03c511bdb85d8fb20788e9037222c26c8bcb`; and named OTHER-account account03/B02 `FOREST-KN-COCKS-REDUCTION-v2`, blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`. The last independently checked the exact Cocks fixed-graph all-positive-weight upgrade and Semple–Welsh minor closure; this run applies that upgrade in the separator reduction rather than inheriting its review PASS.

## Exact multi-bridge theorem

For a two-vertex separator `{u,v}`, split `G` into edge-disjoint `uv`-bridges `B_i`, treating an original edge `uv` as a singleton bridge. Let `D_i` and `C_i` be the weighted forest polynomials in `B_i` with `u,v` disconnected and connected, respectively. Then for arbitrary positive edge weights

`I_G = prod_i D_i + sum_i C_i prod_{j!=i} D_j`.

If marked edges `e,f` lie in one bridge `B_i`, put `A_i=prod_{k!=i}D_k` and `lambda_i=sum_{k!=i} C_k/D_k`. For `B_i^+=B_i+g_i` with virtual edge `g_i=uv` of weight `t`,

`I_{B_i^+}=C_i+(1+t)D_i`,

hence

`Delta_G(e,f)=A_i^2 Delta_{B_i^+}(e,f)|_{t=lambda_i}`.

If `e in B_i`, `f in B_j`, `i!=j`, put `A_ij=prod_{k notin {i,j}}D_k` and

`R_i(e)=D_i partial_e C_i-C_i partial_e D_i`.

Direct determinant expansion gives

`Delta_G(e,f)=A_ij^2 R_i(e)R_j(f)`

and `R_i(e)=Delta_{B_i^+}(e,g_i)`, independent of the virtual weight. All outside bridge ratios cancel from the cross-bridge sign. For the singleton original `uv` edge, `R=1`, so the separator-edge case is covered without introducing parallel virtual edges.

Therefore if each non-singleton `B_i^+` is independence correlated for all positive weights, then `G` is independence correlated for all positive weights.

## 3-connected reduction

Take an edge-minimal finite simple unit-weight counterexample. Disconnected and one-vertex-sum decompositions factor, so it has no 0/1 separator. For a proper 2-cut `{u,v}`, each non-singleton simple augmentation `B_i^+` has strictly fewer edges. Minimality gives unit pNC on each `B_i^+`; Cocks's fixed-graph theorem upgrades this to all positive weights; the theorem above then forces every Rayleigh gap of `G` nonnegative, contradiction. Hence any minimal source counterexample must be 3-vertex-connected (small-order convention handled separately).

This is a separator/gluing step only, not parent closure. It does not supply the second independent review still required for the lead's complete-graph/Hermite candidate.

## Regression and archive

Exact rational enumeration checked 24 deterministic positive-weight multi-bridge assemblies and 640 marked-pair identities, including singleton `uv` bridges: `PASS`, seed `20260922`. Checker SHA-256 `bd313a2431e1ff59ca90d1144c78ba6fea41627a798cf31505fdc914cc7d0e2d`; output SHA-256 `19896e87ffb3c13cf2470d2ec09c6f23318a1838465ebd055efc8d2b986b04ab`.

Scientific archive root:
`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B01/b01-20260922T022351Z-forest-gluing-r11/`

Read-back report blob: `b9c401068cd4bdffe90cb5cc5d2ff32b68b45a51`; checker blob: `f1d777d9a3090b5ba32e0c48dbce880198cf3a48`; output blob: `9c1c2dcd2a4cc7e4884b90c675a597a67c13d6b4`.
