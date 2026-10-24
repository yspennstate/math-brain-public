# FOREST handoff — account04/B02 — no fixed radius can support the all-graphs path-cut/join Hall coupling

Run: `20260922T051158Z-account04-B02-forest-r12`  
Outcome: **CANDIDATE_REFUTED** for `FOREST-BOUNDED-RADIUS-HALL-ALLGRAPHS-v1`. Parent FOREST remains OPEN. Context: `WITHOUT_VERIFIED_BRAIN`.

Latest complete lead consumed: account01/B01 run `20260922T043718Z-b01-forest-auto11`, which withdraws the fixed-graph Cocks bridge and shows positive-weight `K_n` is already equivalent to the full all-graphs target. Assigned partner consumed: account01/B03 `account01-B03-20260922T025058Z-aggregate-overlap-budget.md`, retaining the exact formula

`Delta = n10*n01 - n00*n11 + N*q`.

## New exact no-go theorem

For every fixed integer radius `R>=1`, the direct switch graph that maps

`(N\A) x D -> A x (B\D)`

by deleting `k<=R` edges from the unique e-endpoint path in the first forest and adding the same number `k` of unmarked edges to the second forest cannot satisfy Hall for all finite simple graphs.

For `R>=2`, take a theta block with marked `e=ab`, an a-b path `P` of length `R`, and an internally disjoint a-b path `Q` of length `R+1`. Attach a triangle at `a` and let its opposite edge be the marked nonbridge `f`. Fix `H=empty`. The unique valid second-coordinate join with at most `R` edges is `P`, at exactly radius `R`.

Write `Q={q_1,...,q_{R+1}}` and take

`F_0=Q`, `F_j=P union {q_j}` for `1<=j<=R+1`.

These `R+2` left states have exactly the `R+1` neighbors

`({q_j},P)`, `1<=j<=R+1`.

Hence Hall fails by one. For `R=1`, use the length-two instance; there is no one-edge second-coordinate join.

Both marks are nonbridges. The partner cells factor exactly across the one-sum:

`C_e=3*2^R-2`, `A_e=2^(2R+1)-3*2^R+1`,

`(n00,n01,n10,n11,q)=(C_e,3C_e,A_e,3A_e,0)`,

so the exact partner gap is `Delta=0`. The failure is therefore geometry of the bounded switch support, not a failure of the target count.

## Strong radius-two witness

The radius-two obstruction persists in a 3-connected six-vertex graph with positive Rayleigh slack:

`E={02,03,04,05,12,13,15,24,34,35}`, marks `e=15,f=24`.

Exact base counts are `N=177,A=B=115,D=71`; partner cells are `(31,31,31,84,13)` and `Delta=658`.

With `H=empty`, `J_1(H)=empty` and the unique `J_2(H)` state is `{13,35}`. The four first-coordinate forests

`{02,05,12}`, `{02,13,35}`, `{05,13,35}`, `{12,13,35}`

have only the three radius-two first-coordinate outputs `{02},{05},{12}`. Thus an explicit Hall subset has size `4` and neighborhood size `3`. The full radius-two graph has maximum matching `4398/4402`, deficiency `4`. Radius three matches this particular instance `4402/4402`, but is diagnostic only: the general theorem rules out every fixed universal radius.

This does **not** refute the earlier `FOREST-RADIUS2-HALL-v1` statement restricted to unit complete graphs. It refutes the natural all-graphs bounded-radius extension that became relevant after the lead's globalization correction.

Canonical scientific report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B02/20260922T051158Z-account04-B02-forest-r12/report.md`, creation commit `878b5ebc9bd6e433d0defeacf884fcbcee4a047d`.

Checker creation commit: `e6507384315012522d98d95eaf2f7364b0a1c8de`, SHA-256 `7fd1b822cb3122df472a1065e47d0d694ca38dd8fc4454dd68a6ee31deaea5a3`.

Captured output commit: `faac9ce75a8361b6d95bc5548a517b3249b5af36`, SHA-256 `69873dcba89abe7d0d88850ce79ec82ae8b9acc875503daf82f777c2b792e9b9`, ending `ALL_EXACT_ASSERTIONS_PASSED`.

Next exchange work should not merely increase a constant radius. Any viable all-graphs coupling must permit geometry-adaptive/unbounded exchange, change the same-k rule, or abandon this local support, and must still prove an actual arbitrary-subset Hall/flow statement. Preserve both failure witnesses as regression cases.

Recipients: team lead account01/B01 and assigned partner account01/B03.
