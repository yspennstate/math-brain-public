# R08 E0011 second idea-before-code — full-hazard vacancy rectangle instead of a rare Harris cylinder

The direct-poison sweep suggested a sharper experiment. Do not prescribe a clock word at all. Start a finite rectangle completely vacant and run **every effective internal ZGB adsorption** at `p=1/2, q=1`, with the finite rectangle treated as a closed graph. Stop on the first of:

1. a stable configuration containing both CO and O (success),
2. the all-CO state,
3. the all-O state.

Until success, the state is monochromatic, so the transient state space is only `empty` plus CO-subsets plus O-subsets, not all `3^n` configurations. For a `3 x 6` rectangle this is 524,285 transient/nonpoison states, which is finite and tractable.

This is not yet a source-valid R08 block certificate: the closed boundary omits the arbitrary exterior, success is a seed *class* rather than the exact two-child seed, and event-count time is not a deterministic block top. But it directly tests whether the microscopic no-stirring dynamics itself can produce a threshold-scale local active event once we stop killing almost every ordinary clock.

I will first solve the finite chain numerically only to locate a scale. If it crosses `63/64`, I will not use that numerical solve as a theorem. I will instead run a monotone fixed-point iteration from zero and round **downward** to a common integer grid after every step. Because the hitting operator is monotone, this produces a rigorous rational lower bound. A denominator `10^9` loses at most `10^-9` per iteration in sup norm; after 28 iterations the cumulative rounding loss is at most `28*10^-9`.

Transition probabilities are exact. Scale adsorption rates by four: each effective CO site clock has weight 2 and each effective O2 vacant-edge clock weight 1. Conditional reaction choices have denominators at most four per newly adsorbed atom; a common reaction-branch scale 144 clears all local denominators. Thus every rounded update can be performed with integer arithmetic and checked by the single inequality `64*v_empty > 63*10^9`.