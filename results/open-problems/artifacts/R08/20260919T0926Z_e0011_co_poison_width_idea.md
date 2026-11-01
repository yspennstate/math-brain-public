# R08 E0011 — idea before checker code

Methods for this run: **B3 / B6 / B24**.

Starting point: the preceding run proved that terminal-only tuning of the present certificate is hopeless and proposed a qualitatively different route: build the **full-hazard** protected-state graph, find a closed safe set `S`, prove a uniform finite-horizon lower hitting probability `eta>0`, and amplify it by repeated blocks.

The new idea is to attack that amplification route before implementing a large state graph.

## B24: extremal object

Use the adversary's most obvious extremal phase: the absorbing **all-CO** state. The generated-shield entrance enumeration already permits the locally stable state in which its six frozen entrance vacancies form a `3 x 2` rectangle and every other local state cell is CO. Choose the refreshed exterior/halo to be CO as well.

Until an O2 adsorption occurs on an edge whose two endpoints are still vacant, the only effective events are CO arrivals at the remaining vacancies. If all six vacancies are filled by CO first, then the local protected state becomes all CO; with an all-CO adversarial halo it is an absorbing row and the six-vacancy target can never be reached. The target is not hit on the poisoning path because its two forward cells begin as CO and the path contains no vacancy-creating reaction.

This should directly test the previous proposal that merely waiting under the full hazard can make the local hitting probability arbitrarily close to one.

## B3: stronger statement to prove

For any finite vacancy graph `S` in an all-CO environment, let `q(S)` be the probability that CO fills every vacancy before the first effective O2 adsorption. With the source rates at `p=1/2`, every vacant site has CO rate `1/2` and every vacant-vacant edge has O2 rate `1/4`. If `e(S)` is the number of induced nearest-neighbour vacancy edges, first-event conditioning gives the exact recursion

`q(empty)=1`,

`q(S) = [2/(2|S|+e(S))] * sum_{v in S} q(S\{v}).`

Hence `q(S)>0` for every finite `S`. For the current `3 x 2` entrance rectangle this gives an explicit positive-probability path into the all-CO trap. Therefore any genuinely closed full-hazard safe set containing this entrance state must also contain a state with lower hitting value zero; the proposed `min_S h_m >= eta>0` amplification cannot hold on the current finite seed/core.

This is a restriction on the proposed local amplification architecture, not a refutation of Durrett's source problem.

## B6: deform the seed width

Do not stop at the current width three. Let `q_w` be the same poisoning probability for a vacant `w x 2` rectangle in an all-CO sea. Compute `q_w` exactly for `w=1,...,8`.

The decision quantity is the oriented-percolation failure budget `1/64`. If `q_w>1/64`, then the all-CO poisoning event by itself forces the corresponding worst-boundary eventual local success probability below `63/64`. If `q_w<1/64`, this particular obstruction no longer rules out a threshold-scale local event.

If the crossing occurs at a modest width, the next route should be **spatial redundancy / wider seeds**, not another temporal retry on the width-three seed.

No metric movement is claimed from this idea alone. A checker is warranted only for the exact finite recursion and threshold crossing.