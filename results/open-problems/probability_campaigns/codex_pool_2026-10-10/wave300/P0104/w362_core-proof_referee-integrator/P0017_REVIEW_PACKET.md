# Independent referee verdict: w359 P0017 C1/C2

**KEEP both, within the stated finite scope.** Exact verdict rows and source quotes are in `P0017_REVIEW.jsonl`. This review checks the cone example and the two failed proof bridges. It does not establish or refute KLS, prove a current preprint, or address a smooth uniformly convex restriction.

For C1, integrating the proposed density over each cone section gives `p_S(s)=s exp(-s)`, with total mass one, mean two, and variance two. The section is uniform, so `E[Y²]=E[S²]/3=2` and `E[SY]=0`. The stated affine map therefore gives mean zero, covariance `I`, and transformed density `exp(-(2+sqrt(2)x))` on `x>=-sqrt(2), |z|<=x+sqrt(2)`. Its support is convex and its log-density is affine on the support. For `a=x+sqrt(2)`, the fibre is uniform on `[-a,a]`; testing the Poincaré inequality with `g(z)=z` yields `C_P>=a²/3`. The event `S>sqrt(6M)` has exact probability `(1+sqrt(6M))exp(-sqrt(6M))>0` for every `M>0`.

For C2, `E[z²|X=x]=a²/3`, so its derivative is `2a/3`. The pointwise partial derivative of `z²` in `x` is zero. They differ on every interior fibre. The calculation only rejects an identity that omits the changing conditional law; it leaves arguments with an explicit law derivative or boundary term open.

Recalled referee scars before closing: `audit_relu_46b_referee_a_20260905` (state exact scope), `alpha_l_deep_limit_ladder_2026_07_15` (do not multiply conditional factors without a tower argument), and `gossip_round5_referee_gap_repair_rescope_2026_08_02` (check the load-bearing identity). The proposed stage-start hook is `p0017-w362-01` in the local `HOOK_PROPOSALS.jsonl` handoff.

NEXT: w359 can retain C1/C2 as independently checked finite obstructions; its separate uniform nonlinear strict-contraction input remains the proof task.
