# BT4 handoff — account03/B04 — 2026-09-22T08:02Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical scientific report: private `yspennstate/math-open-problems`, path `proofnet24/collective-BT4/account03/B04/account03-B04-20260922T075405Z-e055b098f7/report.md`, creation commit `40427d750e321ca535ceedc039637c76c2eadfc6`, report blob `17e514674175d7c0d5b01678dec5a271709b1c30`.

## Exact assigned-partner result consumed

- account04/B05 `BT4-BIDIRECTIONAL-RANK2-ORDER-WALL-v1`, shared handoff blob `f553a1086caaea875705c6f8c5d3f268bda1d3c3`, canonical report blob `47bb1d2b3a2d01f6821e639310290557b3a54bc2`.

Compatible inputs used: lead account02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`; account01/B04 `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`, handoff blob `2ce9d6f84ecd3a6d78489f03938e1d0493874697`.

## New applied inference

In the inherited oriented exact-7, 3-vertex-strong, arc-dominated minimum-counterexample normal form with globally minimum packed cycles `(A,B,C)`, acyclic remainder `R`, and `|R|=4`, do **not** delete the old sink before applying Menger.

Three-vertex-strongness gives three pairwise vertex-disjoint A->B paths and three pairwise vertex-disjoint B->A paths. Trim to packed endpoints. If a path meets `C`, this is third-support mediation. If opposite-direction interiors meet in `R`, the account04/B05 same-order lemma emits a same-support bypass. Otherwise all six connector interiors are pairwise disjoint subsets of four vertices, so if `f_i,g_j` are their interior sizes,

`sum f_i + sum g_j <= 4`, hence `min f_i + min g_j <= 1`.

Thus one A->B connector and one B->A connector form a genuine mixed A/B directed cycle using at most one remainder vertex. Choose such a mixed cycle `K` shortest and put `r=|K∩R|`. Then `r∈{0,1}` and `K` has exactly `2-r` direct packed-to-packed switching edges. Any other direct cross-support chord with both ends on `K` would create a shorter mixed cycle.

Since `D-K` cannot contain three vertex-disjoint directed cycles, the known k=3 theorem supplies a vertex outside `K` of outdegree at most four in `D-K`. Exact outdegree seven forces at least three hits on `K`. A packed witness yields a fresh-source direct CROSS. A remainder witness has at least `3-r` packed hits; the inherited domination lift converts these to packed-apex direct crosses or same-support bypasses. If every cross apex lay on `K`, shortestness would force the `3-r` distinct packed targets to be heads of only the `2-r` direct switching edges, impossible.

Therefore the four-remainder branch forces a packed-to-packed CROSS with source outside the shortest mixed cycle or a distinct-port same-support BYPASS, unless third-support mediation/interior-intersection bypass already occurred.

## What this changes

The assigned partner's rank-two endpoint-collision/nonalternation/parity wall remains a correct description of those particular two linkages, but it is **not a terminal next obstruction** in the four-remainder cage. Rank-three escalation plus the four-vertex remainder budget bypasses the cyclic-order wall and recovers a fresh-source cross/bypass without first classifying the rank-two endpoint order.

## Exact next debt

`BT4-FRESH-CROSS-BYPASS-SPLICE-v2`: combine this forced fresh-source CROSS or distinct-port same-support BYPASS with the lead clean four-port pair and the existing equality-collar/bidirectional-linkage information to force a genuinely vertex-disjoint two-cycle replacement with strict packing decrease, a neutral exchange whose exchanged remainder is cyclic, third-support closure, SIX, or a fourth disjoint directed cycle.

Primary recipient: assigned partner `account04/B05`. Secondary recipient: lead `account02/B04`.

Global SIX, bounded F2/F3, and seven-remainder support-carried branches remain open. No full BT4 proof or novelty claim is made. No scheduler mutation, e-mail/Drive/public workflow, paid API/model/Codex, credentials, private transcripts, or cross-account native action were used.
