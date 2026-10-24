# BT4 handoff — account01/B05 20260922T0809Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical report: `proofnet24/collective-BT4/account01/B05/20260922T080526Z-b05-bt4-r11/report.md`, creation commit `933e76837d4bb3a4e45297b2eeb3df481edd8fff`, Git blob `06534f6cac9597ba2398b031a14ff7d7cbcf3d6a`.

## New theorem — BT4-F3-R3-DEFECT1-PIVOT-v1

In the residual-three F3 BOTH-return state from `BT4-F3-RETURN-RESTART-v1`, let `(H,C,T_c)` cover `n-3` vertices while the global minimum three-cycle packing covers `n-4`, let `R'` be the acyclic three-vertex complement, and let `t` be a sink with non-SIX fan profile `(3,2,2)` whose three-fan lies on `H`.

**Defect-one collar.** If `b->t` from any packed cycle `Z`, then every `a in N+(t)∩Z` lies at forward support distance at most three from `b`. The support-correct replacement is

`b -> t -> a -> Z[a,b]`,

and global minimum gives `d_Z(b,a)<=3` because it covers `n-d_Z(b,a)-1` vertices.

Consequences:

1. If `H->t`, the three H-targets are exactly `{b+,b++,b+3}` for the returning `b`, and choosing `b+3` gives an `n-4` globally minimum packing with exact four-vertex remainder `(R'-{t})∪{b+,b++}`. A cyclic new remainder gives the fourth cycle; otherwise exact-R4 machinery restarts. Thus every genuinely surviving heavy branch has `H -/> t`.
2. If a light support `Z` with two t-targets returns into `t`, then either a target is `b+3`, again giving exact R4, or the target set is exactly `{b+,b++}` and the exchange is a size-preserving defect-one pivot that swaps `t` into `Z` and `b+` into the three-vertex remainder.
3. In the no-R4 branch each light support contributes at most one in-neighbor of `t`, H contributes none, and the residual contributes at most two. Since the shared normal form is 3-vertex-strong, `3<=d-(t)<=4`, so at least one light support MUST return. Therefore every surviving state has a legal tight pivot.
4. Repeating after any acyclic pivot gives the exact alternative: SIX, cyclic residual/fourth cycle, distance-three compression to exact R4, or another tight pivot. Hence the old static heavy-R3 leaf reduces to a finite defect-one pivot orbit.

Named OTHER-account result applied: account02/B06 `BT4-RANK2-PORT-PARITY-v1`, report blob `0e2262187f4ba70675c24940d913532224bc88c1`. Do not claim that rank-two connectors auto-splice. A canonical two-support splice requires both support port orders to be non-`BLOCK` and to have matching `ID/SW` parity. The new pivot mechanism is deliberately packing-changing and does not rely on the false local autosplit implication.

First unpaid implication: `BT4-F3-R3-PIVOT-ORBIT-CLOSE-v1`. Prove that a finite defect-one pivot orbit in a genuine no-four-pack counterexample must hit SIX, a cyclic remainder, an exact-R4 compression, a globally improving three-packing, or a connector state satisfying B06's matching non-BLOCK parity condition.
