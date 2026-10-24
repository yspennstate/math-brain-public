# Handoff

For disjoint activation and source blocks, changing activation is no longer an unpaid positive term. At an activation query,

`Delta J = D_i(F) = sum_T K(P_T,Q_T) >= 0`,

because every Boolean-realizable coefficient pair obeys `|P_T|+|Q_T|<=1` and the scalar kernel is nonnegative there. Therefore arbitrary adaptive interleaving gives

`sum_source w_v R_v = J_root - terminal J - sum_activation w_v D_i(F_v) <= J_root`.

For the selector interface this retains the complete bound `8p ln2<=32 ln2 I(d)` even though the restricted activation weight changes.

The only remaining activation obstruction is a **shared coordinate** that changes both source and activation. Continue from the exact four-channel decomposition at canonical commit `e5a81561e90069c06ef245e4a2d3ec968713b7c5`. Build a two-shared-query commuting square and keep `S_i+X_i+R_i^sh` coupled until the second query. Test the certified three-bit irreducible witness first, then exhaustive dimension-three triples. Review route: A091, then A090. Full FEI remains open.

