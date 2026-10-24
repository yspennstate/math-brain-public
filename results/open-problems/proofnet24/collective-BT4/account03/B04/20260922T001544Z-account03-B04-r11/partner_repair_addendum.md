# BT4 account03/B04 addendum — repair of partner counting certificate

Outcome: `ESSENTIAL_STEP_APPLIED` (repair / sharper branch split; no BT4 proof).

## Peer snapshot consumed after the primary report

Exact assigned-partner handoff consumed:

`account04/B05`, `BT4-COUNT-v1`, shared handoff blob `9ce99798e661e4d14b2b27a0f647b909eff715b4`, complete derivation blob `28fdfb0b4449ef6d196b05de51d868e0df6a582a`.

Also consumed the corrected account01/B04 `BT4-MCR-v2` handoff blob `30622855b617296a4430c0073244c39c44516f58` and account04/B04 longest-path handoff blob `a8a27686c07c868ad14a94acd32cc302eff8928d`.

## 1. A necessary repair to BT4-COUNT-v1

`BT4-COUNT-v1` applies the minimum-three-packing one-vertex exchange to every five-fan witness surviving deletion of two packed cycles. That is not justified when the witness lies on the *third packed cycle*.

The valid one-vertex exchange is: if x lies in the remainder R, b in C_i has b->x, and x has at least three outneighbors on C_i, then the cycle through b,x and C_i can replace C_i while leaving the other two packed cycles untouched. If instead x lies on C_k, k distinct from i, the replacement cycle still uses x and therefore intersects C_k. It does not by itself give a new three-cycle packing. Consequently the inference

    heavy on C_i  =>  C_i has no arc to x

is currently proved only for remainder witnesses x in R, not for arbitrary survivors of the pair deletion.

This does not invalidate the Lichiardopol-Por-Sereni pair-deletion dichotomy or the exact collision algebra for remainder vertices. It means the pair-target orientation / avoidance certificate must first separate R-supported witnesses from third-cycle-supported witnesses.

## 2. Exact repair: remainder-avoidance versus third-cycle saturation

Work in the exact-seven spanning counterexample D0 and let C1,C2,C3 be a minimum-total three-cycle packing with DAG remainder R. Minimum totality makes each C_k chordless: a vertex x in C_k has exactly one outneighbor in C_k, namely its successor.

Fix a pair {i,j} and let k be the remaining index. Put H_ij=D0-(C_i union C_j). The 2009 two-cycle theorem gives either a six-fan witness or three distinct five-fan witnesses in C_k union R.

### Lemma A — cycle-supported six-fan is completely saturated

If a six-fan witness x lies on C_k, then

    a_i(x)+a_j(x)=6,
    d^+_{C_k}(x)=1,
    d^+_R(x)=0.

Proof. In H_ij the witness has outdegree at most one. Its successor on the chordless directed cycle C_k survives, so its residual outdegree is at least one. Hence it is exactly one. Exact total outdegree seven leaves exactly six arcs into C_i union C_j and no arc into R. QED.

### Lemma B — cycle-supported five-fan has a unique R exit

If a five-fan witness x lies on C_k in the no-six-fan branch, then

    a_i(x)+a_j(x)=5,
    d^+_{C_k}(x)=1,
    d^+_R(x)=1.

Proof. Its H_ij-outdegree is exactly two. One residual outarc is the successor of x on chordless C_k. No other outarc can stay on C_k, so the second residual outarc is a unique arc from x into R. The remaining five outarcs go to C_i union C_j. QED.

Thus every pair certificate falls into a safe branch:

1. **R-supported branch:** witnesses in R retain the account01/B04 exchange. In particular, three R five-witnesses for one pair yield two R witnesses heavy on the same member cycle and therefore a valid two-vertex avoidance certificate.
2. **third-cycle saturation branch:** any cycle-supported six-witness has six cross-cycle arcs and zero R exits; any cycle-supported five-witness has five cross-cycle arcs and exactly one R exit. No reverse-avoidance claim is made without an additional two-cycle exchange.

### Corollary C — corrected condition for BT4-COUNT-v1's K3 orientation

The K3 pair-target orientation and its cyclic/transitive support-count argument are valid as written on a pair only when one has three suitable five-witnesses in R (or another separately proved two-witness R certificate heavy on the same target). If a pair has fewer than three R five-witnesses, then that pair already supplies a third-cycle saturation witness of Lemma A or B and must be routed into the two-cycle-exchange branch instead.

This yields a corrected global split:

- **all-R clean branch:** every pair supplies three R five-witnesses; the collision formula and K3 orientation machinery of BT4-COUNT-v1 apply;
- **saturation branch:** at least one pair has a witness on the complementary packed cycle, giving either exact 6-cross/0-R-exit or exact 5-cross/1-R-exit structure.

## 3. Why the saturation branch is a genuine new pressure point

The old unstructured statement only said that a residual vertex sees five or six vertices across a pair of cycles. For a third-cycle-supported witness the exact-seven/chordless budget now says much more:

- six-fan: every non-successor outgoing arc of x goes to the other two packed cycles;
- five-fan: every non-successor outgoing arc except one goes to the other two packed cycles, and the sole remaining exit enters the acyclic remainder.

For three cycle-supported five-witnesses on the same complementary cycle, there are three distinct tails on that cycle, each with its own unique R-exit arc (the heads may coincide). This is the natural input for a simultaneous two-cycle splice: the exchange worker can follow the unique R exits to sinks and test whether two exits can be paired with heavy cross-cycle return arcs without intersecting the third packed cycle.

The account04/B04 longest-path collar is compatible with this repaired branch once an exit enters R, but its path-fan avoidance conclusion should only be invoked at a remainder endpoint satisfying its own hypotheses.

## 4. Next exact unpaid implication

Attack the following, without using the invalid blanket avoidance step:

> Given a minimum-total three-cycle packing in an exact-seven counterexample, if some pair-deletion certificate is supported on the complementary cycle, use the resulting 6-cross/0-exit or 5-cross/1-exit vertex to construct a disjoint two-cycle exchange, or prove a source-valid obstruction that forces the all-R clean branch.

Only after reaching the all-R clean branch may the partner's cyclic/transitive K3 avoidance-counting argument be applied without further repair.

No target-level proof or novelty claim is made.
