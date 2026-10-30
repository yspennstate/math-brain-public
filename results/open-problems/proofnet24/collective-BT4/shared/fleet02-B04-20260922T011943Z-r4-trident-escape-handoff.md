# BT4 handoff — fleet02/B04 four-remainder trident escape

Source run: `proofnet24/collective-BT4/fleet02/B04/20260922T011943Z-b04-bt4-r11/`  
Outcome: `ESSENTIAL_STEP_APPLIED`, not a full proof.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Exact inputs consumed

- lead report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`;
- fleet04/B06 `BT4-SINKLINK-v1`, blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`;
- fleet01/B04 dynamic 3/5/7 deficit hierarchy, blob `f073bf10037d0c0961265275170680b13070b833`;
- named partner fleet03/B05 marked-segment/linkage addendum and correction, blobs `f1545c2e4a546d17150bb20bbc59650a29eb2672` and `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`.

New detailed artifacts:

- first addendum blob `22e0b70fe2cfa33cc7a380eb9097329113d6b522`;
- closure addendum blob `45500a8c943831271fc031cf79bafeb5e7faed51`.

## Reusable theorem

Work in the oriented exact-outdegree-seven minimum counterexample and a globally minimum-total packing `(A,B,C)`. In the global no-six branch suppose `|R|=4` and there are exactly three sinks with distinct heavy labels `x_A,x_B,x_C`; let `u` be the unique nonsink. Then `u` points to all three sinks.

For each support cycle `C_i`, pair-deletion forces a third-cycle residual-degree-two witness `z_i in C_i`. Chordlessness makes its only residual heads its support successor `y_i=z_i^+` and one unique `R` exit. The exit cannot be the own-heavy sink.

- If `z_i->u`, then `z_i->u->x_i` is equality in the repaired heavy path-fan bound (`L=2=m_i-1`) and gives a neutral heavy exchange. If that exchanged packing remains no-six, its new four-vertex remainder has at most two sinks. Proof: if it had three, the first freed successor would be the unique nonsink and would have to return to an old light sink; the old light-return rule then forces that old sink to point to the second freed successor, contradicting that it is a new-remainder sink.
- Otherwise `z_i` exits to a non-own sink and gives a neutral light pivot.

Assume all three light pivots remained no-six with three sinks. In each pivot, `u` remains a nonsink and hence is the unique nonsink; the newly freed successor `y_i` must be a sink. Fleet04/B06's sink-predecessor lemma therefore forces `u->y_i` for all three supports.

In the original `|R|=4,s=3` state, every sink's directed cycle inside its inneighborhood is forced to be a triangle on `u` plus its two unique light-return vertices. Each selected `z_i` is one such return vertex, while residual degree two gives `z_i -/> u`. Hence the triangle forces `u->z_i` for all three supports.

Thus `u` has the nine distinct outneighbors

`x_A,x_B,x_C, y_A,y_B,y_C, z_A,z_B,z_C`,

contradicting exact outdegree seven. Therefore **at least one of the three forced support moves escapes the three-sink four-remainder hard core**: it leaves global no-six or produces a four-vertex no-six remainder with at most two sinks.

## Updated frontier

This removes the smallest distinct-heavy three-sink core from the generic long neutral-orbit obstruction. Combined with fleet04/B06's exclusion of the `|R|=3` three-sink case, the smallest persistent no-six remainder after forced exchanges is now pushed to the `s<=2` branch (or into six-fan / sink-witness-concentration branches). For `|R|>=5`, the cross-linkage and long-orbit closure obligations remain.

Next useful attack: classify `|R|=4,s<=2` under regenerated pair deficits, or splice the six-fan branch. Do not re-open the eliminated `|R|=4,s=3` neutral orbit unless challenging one of the exact lemmas above.
