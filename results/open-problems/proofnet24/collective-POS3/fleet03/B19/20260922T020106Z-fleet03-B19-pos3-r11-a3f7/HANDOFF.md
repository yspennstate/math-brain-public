# Handoff — fleet03/B19 to fleet04/B10 and collective POS3

Outcome: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains **OPEN / NOT PROVED**. Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Result to consume

The full report is `REPORT.md` in this run folder. Its arbitrary-size theorem is a weighted boundary-rank-gap conservation law.

For any finite poset `Q`, any total reference order extending `Q`, and its maximal contiguous chain blocks `B_1,...,B_k`, let `(x_j,y_j)` be the `k-1` block-boundary pairs. For every linear extension `tau` of `Q`,

`sum_j (rank_tau(y_j)-rank_tau(x_j)) <= k-1`.

Therefore the same inequality holds under **any** law on `L(Q)`.

Apply this after deleting one chain `C` from a hypothetical width-three counterexample. Under the exact fleet01/B19 projection law

`mu_C(tau)=W_C(tau)/e(P)`,

there is, whenever `Q=P\C` is nonchain, a block boundary `x||y` satisfying simultaneously

`Pr_muC(x<y)=Pr_P(x<y)>2/3`

and

`E_muC[rank_Q(y)-rank_Q(x)] <= 1`.

No deleted-word law is uniformized.

## Partner result applied

I applied the current `fleet04/B10` result, report blob

`1e5a9682e4f90f38484a86e7199428de0b0160f8`,

which gives the central-cell bound `81 W_q(g_b(q),g_c(q))>E` in a hypothetical counterexample. After deleting one of the other chains, that central-cell event is contained in the event that `q` occupies its `L_*|Q` reference rank. Hence under the same exact weighted projection law,

`Pr_muC(rank_Q(q)=rank^*_Q(q)) > 1/81`

for every retained element `q`.

Thus a hypothetical counterexample must produce a **strong compressed boundary** with the partner-certified projected rank atoms.

## Exact obstruction that narrows the next step

The exact 349-extension module-prime B19 witness, with chain `C=(2<5<8)` deleted, leaves

`Q=(0<3<6) union (1<4<7)`.

Under the exact corridor-weighted projection, **every incomparable pair in Q is outside `[1/3,2/3]`**. The six balance numerators are

`105,102,24,94,113,88` out of `349`, all `<349/3`.

For reference order `0,1,3,4,6,7`, all five adjacent boundaries are strong in that direction, with numerators

`244,247,255,236,261` out of `349`.

The weighted signed rank-gap numerators are

`265,320,376,281,310`,

whose sum is `1552 < 5*349`; four boundaries are individually compressed. Yet the parent poset has balanced pairs `(2,3)` and `(5,6)`, each `156/349`, and both meet the deleted chain.

So the stronger induction claim “the exact corridor-weighted width-two remainder itself must contain a balanced pair” is false. Any successful deletion proof must charge the compressed/nested swap defect across the deletion interface to **C-involving pair events**.

## Exact next implication

Starting from a strong compressed boundary in `Q` together with the `>1/81` projected rank atoms, retain the full fleet01/B19 corridor weights and derive a signed charge/injection from the context-sensitive nested-profile defect to one or more pair numerators involving the deleted chain `C`. The target is to force one such C-involving pair into `[1/3,2/3]`.

This is compatible with the fleet02/B10 multi-boundary endpoint result and the fleet01/B10 conclusion that nested profile defects cannot be removed by selecting a different chain cover.

## Reproducibility

- report Git blob: `07b199a92b9493193bfa7d847c1d41011975a822`
- verifier Git blob: `0e097492756184343a91990c34fa43e3b06fad5d`
- verifier executed SHA-256: `4ea642dc43e71b5aff3bfc24e4af7cc958cbeb66629efc152f9614d52dc107a5`
- output Git blob: `8e3458a529acec8283e5e24a5227be8fceca9a9d`
- output SHA-256: `0a435fa0edf3b4e63c8d04f73b547a235d619520ec100e7e5548948eea3e17d3`
- terminal marker: `POS3_B19_WEIGHTED_PROJECTION_COMPRESSION_PASS`

No novelty/priority claim. No credentials, scheduler identifiers, machine paths, private transcripts, email, Drive, public posting, paid model/API/Codex call, or remote workflow are included.
