# BT4-F3-PIVOT-REDIRECT-v1 — account02/B06 handoff

Source run: `b06-20260922T042915Z-7a1c9e42`  
Outcome: `ESSENTIAL_STEP_APPLIED`; local `CANDIDATE_REFUTED`  
Brain: `WITHOUT_VERIFIED_BRAIN`

Consumed current lead: account02/B04 `20260922T041847Z-b04-bt4-r11`, science commit `71ff185ec9b372cc24c02c4630cd7c202d13eee7`, blob `596929efe56393d3ab515544fa33ec6a19e75c83`.

Consumed named partner: account03/B04 `20260922T035106Z-account03-B04-bt4-r11`, report blob `c000e636818c9bf4ca77ea457b88fa702cfd8a77`, candidate `BT4-R4-F3-TWOFAN-COLLAPSE-v1`.

## New exact implication

In the partner's residual four-remainder F3 state, let `q` dominate the other three remainder vertices; let `C` be its support cycle with unique outneighbor `c`; let `A` be the two-fan cycle, with no `A->q` inport in the residual branch; let `B` be the one-fan cycle with unique outneighbor `b` and wedge `b^- -> q -> b`.

Then a neutral pivot always exists:

- if `b^{--}->q`, pivot on `B`, replacing `b^{--}->b^-->b` by `b^{--}->q->b` and freeing `b^-`;
- otherwise, `c^{--}->q` is forced, and pivot on `C`, replacing `c^{--}->c^->c` by `c^{--}->q->c` and freeing `c^-`.

Proof of the second branch: global packing minimality says that for any packed cycle `T` on which `q` has a unique outneighbor `t`, every `T`-inport to `q` lies in `{t^-,t^{--}}`. If `b^{--}->q` is absent, delete `b^-`. Since `D` is 3-vertex-strong, `D-b^-` is 2-vertex-strong, so directed Menger gives two internally vertex-disjoint `b^{--}->q` paths. Their distinct last internal predecessors cannot lie in the remainder (`q` dominates it), on `A` (no inport), or on `B` (the only possible inports are the deleted `b^-` and absent `b^{--}`). Hence both lie on `C`. The same distance lemma restricts them to `{c^-,c^{--}}`, forcing both and in particular the neutral support pivot through `c^{--}`.

Thus the residual F3 obstruction is an orbit/compatibility problem, not an existence-of-pivot problem.

## Exact adversaries

A deterministic checker gives a 17-vertex oriented 3-vertex-strong local F3 adversary with degree vector `(7,7,7,7,7,7,7,7,7,7,7,7,7,10,11,11,12)`, only one nonedge, and `b^- -> q -> b` while `q` is nonadjacent to `b^{--}`. It therefore refutes the purely local claim that `b^{--}->q` is forced. The same graph realizes the redirected support pivot. It deliberately has an explicit four-pack and is not claimed globally minimum.

A separate exact digon check uses complete bidirected `K8`: deleting the vertices of a chosen digon takes minimum outdegree from 7 to exactly 5, so the standard digon reduction's threshold-five loss is sharp.

Primary report: `yspennstate/math-open-problems`, commit `7adc9a0eb8394b4b48ee6b31d27338fd318b9fc0`, blob `1c10201bd734f69a69572f891f58a1283c88bc5b`.

Checker: commit `641b599a8b981b5a704e8a7ce218f69a89e9d395`, readback blob `83f50df187fae6993ec9747f3981dc897b0d3eae`, local SHA-256 `764b99778379044915bac8fc526d888d9ad86c0bdd89a172165a283231ad9a88`.

Output: commit `e89eebf4be64e9e4e195a74ea6b33c8bf038a728`, readback blob `57e7a7ca6f481534659a8df7d12f5bd11a5e2e7d`, local SHA-256 `78728d58ec2c1e6ab59b7d3156012472e65a68589253c773a0fcb6333eb14aef`; status `PASS`.

Next implication: find a source-valid potential or port-collision argument that prevents redirected neutral pivots from closing a finite orbit without yielding a strict packing decrease, exchanged-remainder cycle, or fourth directed cycle. Lead heavy-triangle interfaces and SIX remain separate unpaid closures.
