# R08 E0011 idea before code — stopping-frontier corridor

Methods for this run: B1 / B13 / B30.

The current `b19_full` certificate still multiplies several separately timed local cylinder events. The architecture-cap calculation already says constant-factor tuning of one cylinder cannot close Durrett Problem 5. The new route is therefore to change category: treat corridor propagation as a killed Markov-renewal process whose progress coordinate is the spatial stage.

For one local stage with protected hazard `D`, let `A` be the six-vacancy `2x3` target. Use the already certified maximal support-preserving local alphabet (10 labels; the terminal trimmed stage uses its certified 8-label alphabet). Every protected arrival outside that alphabet is a cemetery transition. Define

`tau_A = first protected-arrival index at which A is reached`,

`tau_dag = first protected-arrival index at which a cemetery clock occurs`.

For a stable entrance descriptor `s`, set

`h_m(s) = P_s(tau_A < tau_dag and tau_A <= m)`.

This is not the old fixed-window endpoint probability. Success stops immediately when the local vacancy target is first reached. With integer reaction weights and `H=36D`, the exact recurrence is

- `G_0(s)=1_A(s)`;
- if `s in A`, `G_m(s)=H^m`;
- otherwise `G_m(s)=sum_{allowed labels l} sum_t w(s,l,t) G_{m-1}(t)`;
- `h_m(s)=G_m(s)/H^m`.

The stage index is then a monovariant: on hitting `A`, advance the active local window immediately to the next spatial stage; later stages keep previously required cleared cells protected. Future untouched material may be arbitrary because the next-stage bounds are minimized over the full certified stable entrance class.

The first finite test is deliberately one-directional. Compute `inf_s h_8(s)` for each of the eight post-bootstrap clearing stages of the current spacing-8 one-column architecture: hazards `150,167,178,187,197,201,218,222`; generated-shield entrance class for the horizontal stages, base class for the two guard stages; terminal stage uses the 8-label trimmed alphabet. Compare these first-hit values with the existing separately timed eight-arrival endpoint factors, but do **not** promote their product to `B_cat` unless the random stage-completion times are stitched into one deterministic block-top event.

A successful result here would isolate exactly how much of the remaining loss is caused by resetting the clock at every stage. The next theorem-sized obligation would be a single fixed-horizon corridor automaton (or a stopping-time oriented-percolation comparison) that ends with the child seed at a deterministic block top. Until that is written, this is a route result, not metric movement.