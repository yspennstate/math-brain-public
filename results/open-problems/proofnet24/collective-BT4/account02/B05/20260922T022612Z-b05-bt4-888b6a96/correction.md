# Correction to `BT4-RSC-v5-two-support-lift` — three-sink step

This correction is part of run `20260922T022612Z-b05-bt4-888b6a96` and supersedes only **Step 3** in the proof of Theorem 6 of `report.md` (report blob `9727b3f919f8c071dd12a6e9c4baf0b631424b08`). The theorem itself remains valid.

## Why correction is needed

The original Step 3 cited the lead's four-remainder trident closure blob `45500a8c943831271fc031cf79bafeb5e7faed51` as if it covered every `|R|=4`, three-sink no-six state. Its proved scope is the **distinct-heavy** hard core after separating the branch in which one packed pair already has three sink-supported five-witnesses. Therefore that citation was too broad for the repeated-heavy/witness-concentration branch.

No conclusion should be drawn from that overbroad citation. The three-sink case has the following direct proof, which uses only the already inherited no-six sink predecessor localization, Lemma 2 of this run, arc domination, and the repaired path-fan inequality from the lead state.

## Corrected Step 3 — three sinks are impossible in a no-cross four-remainder state

Assume `|R|=4`, global NO-SIX, and there is **no** cross-packed transition. From Step 1 of the report, every nonsink of `R` has at least two `R`-outneighbors.

Suppose `D[R]` has exactly three sinks. Let `u` be the unique nonsink and let the sinks be `x_1,x_2,x_3`.

The established no-six sink localization says every remainder sink has an inneighbor in `R`. Since the three `x_i` are sinks and hence have no outgoing arc in `R`, their only possible remainder predecessor is `u`. Thus

`u -> x_1, u -> x_2, u -> x_3`.                                  (1)

Hence `d_R^+(u)=3`. Exact outdegree seven gives four packed outneighbors of `u`. By the no-cross contrapositive of Lemma 2 in `report.md`, all four lie on one packed cycle; call it `T`. Thus

`|N^+(u) intersect T|=4`.                                         (2)

Fix any sink `x_i`. The arc `u->x_i` is dominated, so there is a vertex `d_i` with

`d_i->u` and `d_i->x_i`.                                          (3)

The dominator `d_i` cannot lie in `R`: the only other remainder vertices are the sinks, which have no `R`-outarcs; `d_i=u` would require a loop. Therefore `d_i` lies on one of the packed cycles.

If `d_i` lies on a packed cycle different from `T`, choose any `t in N^+(u) intersect T`. Then

`d_i -> u -> t`

is a genuine cross-packed transition with internal vertex `u in R`, contrary to the no-cross assumption. Hence

`d_i in T`.                                                       (4)

Now (3) gives a direct path of length `L=1` from the packed cycle `T` to the remainder vertex `u`. But by (2), the fan of `u` into `T` has size `m=4`. The repaired path-fan inequality in the lead state applies to this `R`-internal return path and requires

`L >= m-1 = 3`,

contradicting `L=1`.

Therefore a four-remainder global-NO-SIX state with no cross-packed transition cannot have three sinks. This argument covers both distinct-heavy and repeated-heavy/witness-concentration patterns; it does not use the lead trident's separated hypotheses.

## Corrected Theorem 6 proof structure

Under the assumption of no cross transition and no neutral exchange:

1. every nonsink `v in R` has `d_R^+(v)>=2` by Lemma 2 plus global NO-SIX;
2. one sink is impossible by topological order; four sinks are impossible because every no-six sink has an `R`-inneighbor;
3. three sinks are impossible by the corrected direct domination/path-fan argument above;
4. with exactly two sinks, the later nonsink has `d_R^+=2`, hence five packed outneighbors all on one cycle; the account01/B06 `m=5` collar gives cross, neutral equality, or `|R|>=13`, contradicting `|R|=4` under the assumed branch.

Thus Theorem 6 remains:

> Every global-NO-SIX state with `|R|=4` has either a genuine cross-packed transition or a size-neutral globally minimum packing exchange.

This correction strengthens rather than weakens the three-sink step and removes dependence there on the distinct-heavy trident subcase.

Outcome remains `ESSENTIAL_STEP_APPLIED`; full BT4 remains open.
