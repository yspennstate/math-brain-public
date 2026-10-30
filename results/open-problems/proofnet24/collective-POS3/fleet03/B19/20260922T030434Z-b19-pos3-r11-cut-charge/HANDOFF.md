# POS3 B19 handoff — exact cut charge + clean-fork collapse

Parent POS3 remains **OPEN / NOT PROVED**. Outcome: `ESSENTIAL_STEP_APPLIED`. Brain status: `WITHOUT_VERIFIED_BRAIN`.

Consumed named partner: fleet04/B10 run `20260922T024220Z-B10-POS3-r39`, whose equal-predecessor channel theorem gives span descent or a two-cover fork with total positive channel mass `>E/3` and one channel `>E/6`.

## New exact identity

For any finite poset `P`, any deleted set `C`, `Q=P\C`, and retained `x,y`, define

`B_P(u,v)=#(u<v)-#(v<u)`,

`R_P(x,y)=sum_L(r_L(y)-r_L(x))`,

`R_Q^C(x,y)=sum_L(r_{L|Q}(y)-r_{L|Q}(x))`.

Then

`sum_{c in C}(B_P(x,c)-B_P(y,c)) = 2(R_P(x,y)-R_Q^C(x,y)).`

For an actual chain deletion this has the fiber refinement

`B_tau(x,c_t)-B_tau(y,c_t)=2 sum_{r=k_x}^{k_y-1} H_t^tau(r)`

when `k_x<k_y`, with opposite sign when reversed. Thus the weighted corridor/rank defect lands exactly on actual deleted-chain pair numerators; no uniformization of the projected law is needed.

In a hypothetical no-balanced candidate, if `h` deleted-chain elements lie strictly between `x prec_* y` in the strong-majority order and `m=|C|`, then

`E_P[r_P(y)-r_P(x)]-E_mu[r_Q(y)-r_Q(x)] > (2h-m)/3`.

## New structural reduction of the partner branch

Starting from any extreme equal-predecessor pair `a prec_* b`:

- partner span descent to `(z,b)` immediately creates unequal predecessors because `a<z` but `a||b`;
- partner fork escalation gives two blockers above `a`; if they have unequal predecessors, stop; if equal, orient them and recurse.

Every recursive clean fork strictly raises the left endpoint in the poset, so finiteness forbids endless clean escalation. Therefore every equal-predecessor branch reaches an extreme incomparable pair `u prec_* v` with `Pred(u)!=Pred(v)` after finitely many exact channel steps.

## Exact regression evidence

Verifier blob: `6828b47d32f82879f26ca0e63afd254868be23ef`. Output blob: `6afa33b8d1065d5964b30b77bb04e1be5650774b`.

On the 349-extension B19 deletion witness, the cut-charge identity passes for every ordered retained pair. For compressed boundaries `(1,3)` and `(4,6)`, the decomposition exposes the already-known balanced cross-interface pairs `(2,3)` and `(5,6)` through signed endpoint numerators `37`, inside the `[-349/3,349/3]` band.

On the 79-extension Hasse-fork witness, the equal-predecessor pair `(4,3)` has positive channels `{5:10,6:23}` with total `33>79/3`; the next blocker pair has predecessor sets `{0,4}` and `{0,1,2,4}`, so clean escalation terminates immediately.

## Exact next target for fleet04/B10

Work only the remaining **lower-distinguisher interface implication**: for the extreme unequal-predecessor pair forced above, combine its first lower distinguisher with the cut-charge identity, any inherited `>E/6` fork channel, the `>1/81` pinned-rank atom and simultaneous heavy-slice constraints. Force one actual chain-touching pair into `[1/3,2/3]`, or derive a four-antichain / proper autonomous nonchain / forbidden decomposition.

Do not reopen the weighted-width-two-uniform shortcut or an indefinitely repeated clean-fork branch; both are now resolved as invalid/finite respectively.
