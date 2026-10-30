# POS3 fleet02/B19 — linear-depth autonomous-chain migration adversary

**Outcome:** `CANDIDATE_REFUTED` for a bounded-depth chain-module migration selector.  
**Parent POS3 status:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.  
**Run:** `20260922T022215Z-fleet02-B19-pos3-r13`.

## 1. Fresh control and source-bound state


The latest complete campaign-lead report actually consumed was fleet04/B10 run `20260922T011127Z-fleet04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. It proves the strengthened `>1/81` common-majority-rank atom in any hypothetical width-three counterexample. The named partner fleet03/B10 run `fleet03-B10-20260922T001407Z-pos3-r11`, report blob `388ac28e375df4e7a49f72ffbf540f362e03696e`, supplies the predecessor pinned-rank/three-chain flux formulation. I also applied fleet01/B19's arbitrary-chain deletion/fiber recurrence from `proofnet24/collective-POS3/fleet01/B19/20260922T004631Z-b19-pos3-r11/REPORT.md`: deleting a chain induces exact nonuniform corridor weights and adjacent swaps cannot in general be treated by a uniform projected law.

The immediately preceding B19 result, report blob `14588aa0c8cfb8bff56ebd7d08b3d361f6653a90`, refuted fixed-pair preservation under autonomous-chain contraction. The present run changes mechanism: instead of another fixed-pair example, it measures **how far into the expanded chain any replacement balanced pair may be forced to migrate**.

## 2. Conditional end-to-end route and the missing chain-module implication

Assume POS3 is false and choose a cardinality-minimal counterexample. Existing collective reductions leave two branches.

1. In the module-prime branch, the fleet04/B10 lead result applies: the common strong-majority order pins every element to its prescribed rank with probability `>1/81`, simultaneously with the fleet01/B10 heavy cumulative flux constraints. That branch still requires a global signed/conservation contradiction.
2. If there is a proper autonomous **chain** `M`, contract it to one point `z` and invoke minimality on the smaller quotient. The previous B19 run showed that a balanced quotient pair need not survive as the same outside pair after expansion.

A natural repair is to lift a quotient pair involving `z` by looking at a bounded number of descendants near one endpoint of `M`, or more generally within `o(|M|)` distance of an endpoint. The family below refutes that entire local repair. It preserves the exact uniform law, width exactly three, connected incomparability, and an autonomous chain whose contraction has a **unique** balanced pair involving the contracted point.

## 3. Infinite exact family

For every integer `m>=1`, define `P_m` on

`{a,b,x,d,e,c_1,...,c_m}`

by the Hasse covers

`a<d`, `a<e`, `b<x`, `b<e`, `x<d`, and

`b<c_1<c_2<...<c_m<d`.

There are no other generating relations.

The three chains

`A=(a<e)`, `B=(b<x<d)`, `C=(c_1<...<c_m)`

cover `P_m`, while `{a,x,c_1}` is an antichain. Hence `width(P_m)=3`. The incomparability graph is connected: `b` is joined to `a`, `d` to `e`, every `c_j` is joined to `a,x,e`, and these links connect all vertices.

The set `C={c_1,...,c_m}` is an autonomous chain. Every outside element has one uniform relation to all of `C`: `b<C<d`, while `a,x,e` are incomparable with every `c_j`. Contracting `C` to one point gives exactly `P_1` (rename `c_1` as `z`).

## 4. Uniform extension count without a biased projection

Fix an order of `x,c_1,...,c_m` that respects the `c`-chain. There are exactly `m+1` such orders, determined by

`r=#{c_j : c_j<x}`, `0<=r<=m`.

Together with the forced endpoints `b` and `d`, this gives a scaffold of length

`N=m+3`: `b`, then the chosen shuffle of `x` through `C`, then `d`.

Now insert the two-element chain `a<e`. Let `t_a,t_e` be the numbers of scaffold elements preceding `a,e`. The defining relations are equivalent to

`0<=t_a<=N-1`, `1<=t_e<=N`, `t_a<=t_e`.

Therefore every one of the `m+1` scaffold words has the same number

`K_m = N + sum_{t=1}^{N-1}(N-t+1) = (N^2+3N-2)/2`

of lifts. Consequently the total number of **uniform** linear extensions is

`E_m = (m+1) K_m = (m+1)(m^2+9m+16)/2`.                 (4.1)

This is a direct exact count of the actual uniform law on `L(P_m)`. No induced distribution has been replaced by a uniform surrogate.

## 5. Closed forms for every incomparable-pair probability

Put

`B_m=m^2+9m+16`, `D_m=(m+1)B_m=2E_m`.

The outside-outside incomparable pairs are exactly

`a||b`, `a||x`, `x||e`, `d||e`.

Counting allowed insertion pairs on the scaffold gives

`Pr(a<b)=Pr(d<e)=2(m+3)/B_m`,                           (5.1)

`Pr(a<x)=Pr(x<e)=(2m^2+19m+36)/(3B_m)`.               (5.2)

For module pairs, `1<=j<=m`, uniformity of the `m+1` scaffold shuffles gives immediately

`Pr(x<c_j)=j/(m+1)`.                                    (5.3)

For `a<c_j`, let `F_m(s)` be the number of `(t_a,t_e)` choices with `a` before the scaffold element in position `s`. Explicitly

`F_m(s)=N + sum_{t=1}^{s-1}(N-t+1)`.

If `x` lies after `c_j` there are `m+1-j` shuffles and `c_j` has scaffold position `j+1`; if `x` lies before it there are `j` shuffles and the position is `j+2`. Hence

`#{L:a<c_j}=(m+1-j)F_m(j+1)+jF_m(j+2)`.

After simplification,

`Pr(a<c_j)=A_m(j)/D_m`,                                  (5.4)

where

`A_m(j)=-(m+3)j^2+(2m^2+11m+13)j+2m^2+8m+6`.           (5.5)

The order-reversing automorphism

`a<->e`, `b<->d`, `x<->x`, `c_j<->c_{m+1-j}`

gives

`Pr(e<c_j)=1-Pr(a<c_{m+1-j})`.                           (5.6)

Equations (5.1)--(5.6) cover **every incomparable pair in `P_m`**.

Two exact comparisons will be useful below. For `1<=j<=m`,

`A_m(j)-jB_m=(j+2)(m+3)(m+1-j)>0`,

while the numerator of `Pr(x<c_j)-Pr(e<c_j)` equals

`j(m+3)(m+3-j)>0`.

Thus along the lower half of the corridor

`Pr(e<c_j) < Pr(x<c_j) < Pr(a<c_j)`,                     (5.7)

and all three are strictly increasing in `j` because

`A_m(j+1)-A_m(j)=2m^2+10m+10-2(m+3)j>0` for `j<=m`.

## 6. Quotient selector succeeds, but expansion forces linear-depth migration

For the contracted quotient `P_1`, (5.1)--(5.6) give all seven incomparable-pair probabilities:

`Pr(a<b)=4/13`, `Pr(a<x)=19/26`, `Pr(a<z)=19/26`,

`Pr(x<e)=19/26`, `Pr(x<z)=1/2`, `Pr(d<e)=4/13`, `Pr(e<z)=7/26`.

So `x||z` is the **unique** balanced incomparable pair of the quotient.

After expanding to `P_m`, every outside-outside pair is unbalanced for every `m>=1`: (5.1) is below `1/3`, while (5.2) is above `2/3`. Thus every balanced pair in `P_m` must touch the expanded module `C`.

Moreover, endpoint migration fails. At `j=1`,

`Pr(a<c_1)=(4m^2+18m+16)/D_m`,

and

`D_m-3(4m^2+18m+16)=m^3-2m^2-29m-32>0` for every `m>=7`.

By (5.7), all three pairs `a||c_1`, `x||c_1`, `e||c_1` are then below `1/3`. The order-reversing symmetry gives the analogous statement at `c_m`: every pair touching `c_m` is strongly oriented. Hence no endpoint descendant of the quotient's contracted vertex supplies a balanced replacement once `m>=7`.

The obstruction is actually linear-depth. If `j/m -> alpha` with `0<alpha<1`, then from (5.3)--(5.6)

`Pr(e<c_j) -> alpha^2`,

`Pr(x<c_j) -> alpha`,

`Pr(a<c_j) -> 2alpha-alpha^2`.                           (6.1)

Let

`alpha_* = 1-sqrt(2/3) = 0.183503...`,

so `2alpha_*-alpha_*^2=1/3`. By monotonicity and (5.7), for every fixed `delta<alpha_*`, all incomparable pairs touching any `c_j` with

`j<=delta m` or `j>=m+1-delta m`

are unbalanced for all sufficiently large `m`. Conversely, for every fixed `delta>alpha_*` but still close enough to `alpha_*`, `Pr(a<c_floor(delta m))` lies in `[1/3,2/3]` for all sufficiently large `m`. Therefore the minimum distance from an endpoint of `C` at which **any** balanced module pair appears satisfies

`min_balanced_depth(P_m)/m -> alpha_*`.                  (6.2)

So no selector inspecting `O(1)` descendants, no fixed fraction smaller than `alpha_*`, and in particular no `o(m)` endpoint neighborhood can repair the contraction step. A valid chain-module induction must use a genuinely global corridor crossing/charge through a linear fraction of the module.

This does **not** refute POS3. Equation (5.3) itself shows many balanced pairs: whenever

`ceil((m+1)/3) <= j <= floor(2(m+1)/3)`,

`x||c_j` is balanced. The family refutes only the bounded-depth migration selector.

## 7. Ordinal-sum amplification

For arbitrary finite chains `C_s,C_t`, the ordinal sum

`C_s op P_m op C_t`

still has width three. Every linear extension is the forced prefix `C_s`, followed by one uniform linear extension of `P_m`, followed by the forced suffix `C_t`; there are no new incomparable cross-factor pairs. Hence all probabilities (5.1)--(5.6), the unique quotient selector, and the linear-depth obstruction (6.2) are unchanged. The failure therefore persists at arbitrarily large finite orders and is not a small-size artifact.

I did not use a Cartesian product: such products can raise width and are not automatically admissible in the width-three source model.

## 8. Exact executable certificate

`verify_pos3_corridor_depth.py` is a dependency-free integer DP verifier. It independently:

- computes exact linear-extension counts from the transitive closure for `m=1,...,12`;
- checks every incomparable-pair count against (4.1) and (5.1)--(5.6);
- proves by exact finite checks that the quotient `P_1` has exactly one balanced pair;
- checks width exactly three, incomparability connectivity, and autonomy of `C` for the concrete `m=12` certificate;
- prints all **40** incomparable-pair probabilities for `P_12` under the actual uniform law;
- checks endpoint failure from the closed forms for `7<=m<=100` as regression evidence;
- reports first balanced module depths `2,2,6,11,22` for `m=7,12,30,60,120`, converging to the analytic `alpha_* m` law proved above.

Executed verifier SHA-256: `3da1b8cd4d44b47501664a32bbf6dfb28aa64945b0d661f3844c54f9b3dca1b8`.  
Captured output SHA-256: `f3ec110fbf9311d47f6384ed77fe0f8d3df200d4a0ec3e9108b92d17d40e9198`.  
Terminal marker: `POS3_CORRIDOR_DEPTH_CERTIFICATE_PASS`.

The exact DP is regression evidence. The infinite-family and linear-depth claims are proved symbolically above; no finite census is used as universal closure.

## 9. Accepted gate before/after and residual

**Before:** fixed-pair chain contraction was known false, but a local repair could still hope to inspect endpoint descendants of the expanded chain and find a replacement balanced pair.

**After:** that entire bounded-depth repair is false. There is an explicit connected width-three autonomous-chain family whose quotient has a unique balanced pair through the contracted vertex, whose expansion makes every outside-outside pair unbalanced, and whose first balanced replacement pair is asymptotically `alpha_* m` positions from an endpoint, `alpha_*=1-sqrt(2/3)`.

The first essential chain-module implication is therefore now:

> **Global weighted corridor crossing.** Starting from a balanced quotient pair involving the contracted autonomous chain, use the exact nonuniform insertion weights across the **entire** expanded chain to prove that some descendant/outside pair crosses the `1/3--2/3` band. Any proof restricted to bounded endpoint neighborhoods is impossible.

A proof of that implication would close the autonomous-chain branch and reduce a minimal counterexample to the module-prime branch, where the lead's `>1/81` pinned-majority-rank atom and the common heavy-flux constraints become the active global obstruction. No such global crossing theorem is proved here.

**Final classification:** `CANDIDATE_REFUTED` for the bounded-depth chain-module migration selector; parent POS3 remains open.

## 10. Provenance and runtime truth

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid API/model/Codex, remote workflow, permission bypass, or brain installation was used. Scheduler inspection was account-local only; the twenty current managed fleet02 slots were present, enabled, hourly, role-aligned, and B20 was enabled, so B19 made no scheduler mutation.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning effort: `UNKNOWN / NOT_EXPOSED`. Known reasoning effort: `UNKNOWN / NOT_EXPOSED`. Provider reasoning-token/thinking-time counters: `NOT_EXPOSED`. Measured elapsed execution is reported in the immutable receipt and is wall-clock/instrumented execution, not pure thinking time.
