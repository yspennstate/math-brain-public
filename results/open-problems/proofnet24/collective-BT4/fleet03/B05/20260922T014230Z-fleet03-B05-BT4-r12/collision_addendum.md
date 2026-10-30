# BT4 fleet03/B05 addendum — staticizing and shrinking the two-pivot collision

Run: `20260922T014230Z-fleet03-B05-BT4-r12`  
Candidate extension: `BT4-TCEX-v3.1-collision`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent report commit: `4b1eb2aaee9d3a0cceda6645ec096621f79a817b`

## Exact later peer input applied

After the parent overlap reduction was written, I consumed the newer fleet01/B06 report

`proofnet24/collective-BT4/fleet01/B06/20260922T013522Z-b06-bt4-r11/report.md`, blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`.

Two of its proved statements matter here.

1. For any **R-supported five-witness** heavy on a packed cycle with fan `m>=3`, the corrected three-path Menger collar gives one of:
   - a genuine cross-packed transition;
   - a size-neutral equality exchange;
   - three strict pure-R collars and the quantitative bound

     `|R| >= 3m-2`.                                                (1)

2. For a fixed pair of untouched packed cycles, the residual degree-two witness set is an exact static vertex set through a neutral light pivot. Thus the “regenerated” witness used below is not a newly created degree event; only its support description changes with the pivot.

I combine this with fleet02/B20's late-lead addendum, blob `aac4b9da986de7371a255291e71268e2f47aeca2`.

## Setup: the exact two-pivot collision inside the three-sink linkage core

Stay in the parent report's hardest no-six state: the remainder has exactly three sinks

`x_A, x_B, x_C`,

with distinct heavy labels `A,B,C`, and every sink is in the named partner's two-way light-linkage alternative.

At `x_A`, the partner gives simultaneous light return ports from `B` and `C`. The newest lead/B20 combination allows the two corresponding neutral pivots. In a persistent no-six state, take off-pivot five-witnesses

- `z_B` for the fixed pair `A union C` after the `B` pivot;
- `z_C` for the fixed pair `A union B` after the `C` pivot.

If they coincide, fleet02/B20 proves that the common vertex `z` lies in the **original remainder** `R\{x_A}` and has, for some `t in {0,1,2}`, the exact original-packing profile

`(a_A(z),a_B(z),a_C(z),d_R^+(z))=(5-t,t,t,2-t)`.                  (2)

Thus the only candidate profiles are

`(5,0,0,2)`, `(4,1,1,1)`, `(3,2,2,0)`.                           (3)

The staticization theorem above confirms that these are properties of the fixed original pair-deletion graphs, not artifacts manufactured by the pivot operation.

## Lemma 1 — the sink collision profile is impossible in the exact three-sink core

The profile

`(3,2,2,0)`                                                       (4)

cannot occur in the present three-sink state.

### Proof

Equation (4) says `d_R^+(z)=0`, so `z` is a sink of the original DAG `D[R]`. Its unique heavy label is `A`.

By the B20 collision lemma, `z!=x_A`. It also cannot equal `x_B` or `x_C`, because in the exact no-six sink normal form each sink has a unique heavy label, while `x_B` and `x_C` are heavy on `B` and `C`, respectively. Thus `z` would be a fourth distinct sink of `R`, contradicting the hypothesis that the hard core has exactly the three sinks `x_A,x_B,x_C`. QED.

So the most recurrent-looking collision endpoint from the general two-pivot trichotomy disappears entirely in the partner's exact three-sink compatibility core.

## Lemma 2 — the two surviving collision profiles carry large-remainder or transition/exchange alternatives

If the collision has profile `(5,0,0,2)`, then at least one of the following holds:

1. a genuine cross-packed transition is produced by the fleet01/B06 three-path collar;
2. a size-neutral equality exchange is produced;
3. `|R|>=13`.

If the collision has profile `(4,1,1,1)`, then at least one of the following holds:

1. a genuine cross-packed transition is produced;
2. a size-neutral equality exchange is produced;
3. `|R|>=10`.

### Proof

In both cases `z` lies in the original remainder and is a five-witness for both pairs `A union B` and `A union C`. Its heavy cycle is `A`, with fan

`m=5` in the first case and `m=4` in the second.

Apply the fleet01/B06 R-supported five-witness collar directly in the original globally minimum packing. If it produces a cross-packed transition or an equality exchange, we are in alternatives 1 or 2. Otherwise (1) gives

`|R|>=3*5-2=13`

or

`|R|>=3*4-2=10`,

respectively. QED.

No averaging is used: the bounds come from three pairwise internally disjoint directed paths into the same R-supported heavy witness.

## Corollary — refined fork for the three-sink partner linkage branch

In the exact three-sink / distinct-heavy-label / all-long-light core, the two neutral pivots at any sink have the following source-valid outcome:

- one pivot enters the six-fan branch; or
- the two off-pivot witnesses are distinct; or
- they coincide in the original remainder, but then only the profiles `(5,0,0,2)` or `(4,1,1,1)` are possible, and either a cross-packed transition/equality exchange occurs or `|R|>=13` / `|R|>=10`, respectively.

The apparent collision profile `(3,2,2,0)` is excluded outright by the exact three-sink hypothesis.

This materially tightens the parent report's remaining pairwise-overlap/collision geometry: the collision branch cannot recursively reproduce another same-heavy sink while remaining inside the three-sink hard core.

## Remaining obligation

Full BT4 is not proved. The most immediate surviving branch is now:

> In the exact three-sink partner linkage core, handle two **distinct** off-pivot five-witnesses, or one of the two low-R-outdegree collision profiles under the corresponding large-remainder bound, together with the parent report's pairwise-only linkage-overlap/packed-port-collision alternative. Use the fixed-pair witness sets and exit-return collars before introducing another neutral pivot.

The separate six-fan closure and the partner's short-light alternative remain live.

Next recipients: fleet02/B04, fleet04/B06, fleet01/B06, fleet02/B20.
