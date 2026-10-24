# FOREST handoff — account02/B03 — sharp book-graph separator/parallel obstruction

**Run:** `20260922T022013Z-b03-forest-auto11`  
**Outcome:** **ESSENTIAL_STEP_APPLIED**; parent FOREST remains **OPEN**.  
**Context:** `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B03/20260922T022013Z-b03-forest-auto11/report.md`, blob `b738b5381e0c4141d7f2a3a625f2647acb65bb1a` in `yspennstate/math-open-problems`.

## Exact correction

For a multigraph forest polynomial, parallel classes aggregate exactly by **summing their weights**: if `C` is a parallel class, replace it by one quotient edge of weight `Y_C=sum_{h in C} y_h`. A marked original member `e in C` is tracked by `partial/partial Y_C`, not by the aggregate-class inclusion event. Thus contraction-created parallel classes may be simplified, but their exact summed weights and marked-member derivative semantics must be retained. A one-edge contraction of a unit simple graph creates class weights only `1` or `2`.

## Infinite source-graph adversary family

Let `B_k` (`k>=2`) be `k` triangles sharing a spine edge `g=01`; page `i` has spokes `a_i,b_i`. Mark `e=a_1`, `f=a_2`. With only `g` weighted by `w`, exact counts are

`A=3^(k-1)(k+3)`, `B=3^k`,
`a0=b0=3^(k-2)(k+5)`, `a1=b1=3^(k-1)`,
`c1=3^(k-2)`, and `c0=3^(k-3)(k+7)` for `k>=3` (`c0=3` at `k=2`).

Hence

`Q(w)=Z_e Z_f-Z Z_ef = 4*3^(2k-4)`

for every finite `w>0`, while the true cross gaps are

`P_e=P_f=2*3^(2k-2)>0`.

Contracting `g` creates `k` parallel classes of size two, so the exact quotient is a star with each class weight `2`. If those weights are falsely reset to `1`, then

`P_e^naive = 2^(k-1)3^(k-2)(1-k)<0`

for every `k>=2`: the naive unit simplification reverses a load-bearing separator sign.

## Sharp corrected separator statement

Condition on `g`. Let `c_i=-Cov(e,f|g=i)` and `d_e=P(e|g=0)-P(e|g=1)`, similarly `d_f`. If `alpha=P_w(g=0)`, `beta=P_w(g=1)`, then exactly

`Cov_w(e,f)=-alpha c0-beta c1+alpha beta d_e d_f`.

Thus, assuming the two conditional endpoint gaps are nonnegative, the actual-response criterion is

`d_e d_f <= c0/beta+c1/alpha`,

and the criterion valid for **all** positive responses is exactly

`d_e d_f <= (sqrt(c0)+sqrt(c1))^2`.

The book family saturates this envelope for every `k>=2`:

`d_e=d_f=2/[3(k+3)]`, `c0=4/[9(k+3)^2]`, `c1=0`.

Therefore no universal strict multiplicative reserve below `1` is possible.

## Named partner applied

Using account03/B01 run `20260922T003307Z-account03-B01-r11`, report blob `4bfacc593182b192e927df9a5bde6e14caa7e4de`, define the activity numerators

`Xi_eg=4 Delta(e,g)=4P_e`, `Xi_fg=4P_f`.

The exact remaining all-response separator obligation becomes

`Xi_eg Xi_fg <= 16 (B sqrt(D0)+A sqrt(D1))^2`.

The book family attains equality in the corresponding normalized envelope, so the next step is to prove this inequality at **constant one** from the activity exchange geometry plus minimal-counterexample matching/external-negative structure, or produce a source-valid counterexample. Do not spend another run on unit-simple contraction or fixed-slack variants.

The current lead account01/B01 v2 fixed-graph Cocks chain was read. This run verified the final Semple--Welsh fixed-graph attribution and minor-closure statement but did not inspect the gated Cocks proof body, so it is not an owner-gate end-to-end review of the lead full candidate.
