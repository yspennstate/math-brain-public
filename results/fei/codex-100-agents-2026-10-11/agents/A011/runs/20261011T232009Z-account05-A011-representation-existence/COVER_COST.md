# Output-only comb reference: full ledger

This repairs the A011 physical-path code. It changes the generator;
it does not deduct posterior entropy from a transmitted witness.

| Cost component | Exact treatment |
|---|---|
| Gate cover | Each first-positive or terminal path cell AND its selected data character event |
| Used-gate/physical leaf label | Not decoded; all colliding output contributions included coherently in fixed suffix formula |
| Empty-selector atoms | Masses p^2 and q^2, costs L(p^2)+L(q^2); never dropped |
| Nonempty group/root | Group j=max(selector Fourier set), mass v_j=2^-j r_j^2 |
| Conditional data label | One fair bit in every positive group |
| Conditional support/order | Uniform subset of known predecessors [j-1], j-1 bits; include j deterministically |
| Full group cost | v_j[-log2(v_j)+j]=v_j[2j+2log2(1/r_j)] |
| Rarity/amplitude cost | 2 sum v_j log2(1/r_j), bounded by 2 I_sel/(e ln 2) |
| Normalizer | p^2+q^2+sum v_j=1 exactly |
| Inactive/zero groups | Omitted because r_j=0 gives zero true/reference mass |
| Duplicate latent leaves | No duplicate output mass: coefficients are summed with signs before squaring |
| Prior/dictionary | One fixed tree-derived table; no spectrum-dependent free prior |
| Integer prefix rounding | At most one total bit; paid by I_data>=1, or zero bits for deterministic output |
| Tensor terminal | Full CE(P_seed,Q_seed), including its subprobability normalization and empty atom, added exactly |

The exact selector identity is 2 sum j v_j=4 I_sel-2 sum v_j.
The empty-sector correction is <=2 sum v_j. Keep the negative term:
the combined cost is at most 4 I_sel. The rarity term raises this to
(4+2/(e ln 2)) I_sel <(41/8) I_sel. Static data supports and selector
order are part of the fixed function dictionary, as in the original
campaign reference interface.

Passive pushforward of the old uniform-mask Kraft reference is NOT this
generator. For the terminal-only switch its common data output mass
tends to 1/3, yielding nonvanishing reference cross-entropy while
I_sel tends to zero. The repaired table is a coherent output law computed
from physical suffix biases; its expected cost is proved analytically.

This reference is separate from the forest/queue (L)+(S)+(R) reference.
No bound on the original queue infimum, arbitrary selector rows, or an
arbitrary data seed is inferred from the comb repair.
