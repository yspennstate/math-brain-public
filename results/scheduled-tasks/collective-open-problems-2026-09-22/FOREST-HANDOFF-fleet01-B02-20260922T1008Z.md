# FOREST handoff — fleet01/B02 — 2026-09-22T10:08Z

Outcome: `CANDIDATE_REFUTED`  
Refuted mechanism: `UNIVERSAL_JOINT_STAR2_UNITIZER_AS_MINIMALITY_STEP`  
Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet01/B02/20260922T095045Z-b02-forest-r11/REPORT.md`, report blob `c58f32b8c787553e0d703bc44a54eba40c25245e`.

## Named peer consumed

Applied fleet02/B03 `20260922T094532Z-b03-forest-auto11`, report blob `d5915bec9e6d551a078f7f1902d1492cc7989ac7`. Its exact result says every finite simple unit two-terminal network with forest response `C/D=2` has at least 7 edges and 5 vertices; the direct edge plus three internally-disjoint length-2 paths attains `(D,C)=(27,54)`.

## New theorem

Let `N` be a finite simple unit network with boundary terminals `c,w_1,...,w_d`. Suppose its forest boundary-connectivity signature is, up to one common positive scalar, exactly the signature of the weighted star with edges `c w_i` all of activity 2. Then

`|E(N)| >= 7d` and `|V(N)| >= 1+4d`.

Proof: every component of `N-c` contains at most one leaf terminal, since a path between two leaves avoiding `c` would itself be a forest realizing a boundary partition that has zero weight in the target star. Hence `N` is a 1-sum at `c` of leaf branches plus terminal-free factors. Restriction of a forest to these factors is a multiplicity-one bijection, and acyclicity factorizes exactly. If `D_i,C_i` are the disconnected/connected two-terminal forest counts of the branch containing `w_i`, then for every subset `T` of leaves,

`W_N(pi_T)=Q product_{i in T} C_i product_{i notin T}D_i`.

Matching the target signature `2^|T|` and dividing the singleton state by the empty state gives `C_i/D_i=2` for every branch. The named peer's exact lower bound therefore gives 7 edges and 5 vertices per branch.

If a parent with `m` edges contracts a triangle edge with `d` common neighbors, the weighted quotient has `m-1-d` edges including the `d` weight-2 representatives. Replacing those representatives by any such joint boundary-exact unitizer gives at least

`m-1-d-d+7d = m-1+5d > m`

edges. Thus no **universal exact** joint terminal gadget can restore edge-minimality. Any successful STAR-2 step must be parent-specific and cross boundary fibers (or prove the contraction inequality directly).

## Direct residual and finite regression

Writing `H=G-uv`, conditioning the parent edge `uv` present is bijective to uniform forests of the smaller simple `H` conditioned on `u` and `v` being disconnected. The exact residual is therefore

`D_e D_f - D D_ef >= 0`.

A new exact checker exhaustively verified this conditioned gap for every simple `H` with fixed nonedge terminals on `n<=6` and every present marked pair: **377,425 marked-pair instances, zero negative gaps**. This is finite evidence only, not closure. Checker and stdout are beside the canonical report.

The next useful attack is a multiplicity-controlled cross-fiber map `D_00 x D_11 -> D_10 x D_01` that is allowed to change union/intersection and uses the split parent edge as a certificate. Parent FOREST remains open. Continue `WITHOUT_VERIFIED_BRAIN`.
