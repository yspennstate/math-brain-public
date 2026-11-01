# P0003 referee attempt: exact fixed-length collar control

2026-10-10. The catalog source is Grimmett, *Selected problems in probability theory*, arXiv:2205.07318v1, Question 2.2. It samples a uniform n-step self-avoiding walk from the honeycomb origin. The source leaves its precise spatial normalization, SLE geometry/stopping rule and curve topology open. The all-length two-boundary-point critical-fugacity conjecture in arXiv:1206.2092 is related and cannot replace this ensemble without a transfer theorem. Current openness is UNKNOWN after bounded checks; no full proof is claimed.

## Rigorous route and its hardest attempted input

For an operational version, scale the n-step embedded path by `s_n=n^(-3/4)`; this exponent is conjectural and is not asserted by the source question. Let `G_n` be the graph-distance-n honeycomb ball. Every relevant walk is contained in it. For a finite graph H, define `C_m(H;v)` as the number of simple m-edge paths from v with free terminal vertex. A realized k-edge prefix eta has exactly the `(n-k)`-edge continuations in the slit graph `G_eta`, so an avoidance conditional probability retains that remaining length. w396's L0′ and my independent check establish this finite identity.

For nested forbidden edge sets A⊂B, let `M_k^A=P_n(avoid A|F_k)` and similarly for B. Their difference is `E_n[1_(avoid A but hit B)|F_k]`, a nonnegative martingale. Bounded stopping gives `P_n(max_k(M_k^A-M_k^B)>=lambda) <= Delta_n/lambda`, where `Delta_n=P_n(avoid A but hit B)`. This is a proved reduction: one *static* collar estimate would control every exploration prefix without multiplying conditional probabilities. It does not supply the static estimate or tightness.

The **single hardest concrete estimate attempted here** is w396's `H_disk`. For a fixed disk A away from the origin and its concentric radius-`(1+epsilon)` collar B, prove constants alpha>0, C<infinity with `limsup_(n→infinity) P_n(s_n trace avoids A but hits B) <= C epsilon^alpha`, with n tending to infinity before epsilon to zero. This remains unproved. For the full fixed-length scaling limit, length-resolved identification `H_len`, ordered-curve tightness, and a justified continuum convention remain separate unproved load-bearing inputs; I do not call H_disk a solution of the parent problem.

## Attempt and exact failure point

Split each path counted by `Delta_n` at its unique first B-forbidden oriented edge `(v,w)` after k steps. Its prefix is B-avoiding and its remaining `(n-k-1)`-step suffix is A-avoiding. Forgetting mutual self-avoidance between those pieces gives w396's checked upper bound `(U)`: sum over k and collar edges of `c_k^B(0,v) C_(n-k-1)^A(w)`, divided by `c_n(H)`. This is a counting injection, not an independence claim. I checked the endpoint cases k=0 and k=n-1 and exact remaining length.

I tried to use `(U)` as the required epsilon modulus. It does not close `H_disk`: the product counts many prefix/suffix pairs that intersect each other and cannot form a self-avoiding walk. No uniform estimate on that mutually avoiding mass, or on the overcounting sum, is in the packet. The known honeycomb connective constant gives exponential growth scale, not an annular near-miss power bound; absorbing any n-dependent overcount into C would be unjustified. The source's local parafermionic identity also cannot supply compactness by itself: w397's independently checked interior face circulation has zero vertex residual and boundary data yet unit jumps at mesh scale. The true walk-sum observable would need an additional quantitative regularity estimate.

The clean next proof step is a positive bound on the **mutually avoiding, exact-length prefix/suffix pairs** for one fixed disk collar, uniform in n after the chosen scaling. A bound on the unrestricted product in `(U)` strong enough to imply `H_disk` would also work. Either route must retain the exact remaining length and quantify epsilon before any SLE identification claim.

No new lemma of my own is promoted by this attempt; the finite lemmas reviewed are w396/w397's and are recorded with their independent verdicts in `CLAIMS.jsonl`.

NEXT: Bound the mutually avoiding exact-length prefix/suffix mass for one fixed disk collar, or find a counterexample to the proposed H_disk modulus under the operational scaling.
