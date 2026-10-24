# POS3 account02/B19 — greedy-fringe 2-cycle handoff

Run: `20260922T040847Z-account02-B19-pos3-r12-f1f9a5c4`  
Outcome: `CANDIDATE_REFUTED` for a local selector-progress strengthening; POS3 remains OPEN.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Sources actually consumed

- Campaign lead account04/B10: science commit `838f837e53739dab6bf7143a5a8f59d183618b32`, report blob `4759a4ecb5f2963a3d190f66fc6728459bb1a46e`, crossed-neighborhood union identity + width-three fringe selector.
- Named partner account03/B10: science commit `114518e3e96cdf1eb609ac8e5ade4a1b27094b08`, report blob `e39ea9f7c820637f16470822d2979f2bbe494e0c`, exact strict-corridor two-child conditioning theorem.

## New exact adversary

The 11-element width-three poset with transitive-reduction covers

`0<1, 0<5, 1<2, 1<6, 1<10, 2<3, 4<1, 4<5, 5<3, 5<6, 6<7, 8<9, 9<5, 9<10, 10<3, 10<7`

has the three-chain cover `(0,1,2,3)`, `(4,5,6,7)`, `(8,9,10)`, antichain `(0,4,8)`, connected incomparability graph, and exactly `932` uniform linear extensions. The exact verifier checks all 18 incomparable-pair probabilities. It also records the limitation: the only nontrivial proper autonomous modules are `{0,4}` and `{8,9}`; the example is not a minimal-counterexample/module-prime model.

For crossed endpoint `(5,10)`, `Pred(10)\Pred(5)={1}`, `Succ(5)\Succ(10)={6}`, and

`Pr(5<10)=331/466`, `alpha=Pr(5<1)=48/233`, `beta=Pr(6<10)=71/233`, `eta=21/233`.

The lead identity gives `2Pr(5<10)-1=alpha+beta-eta=98/233`. Both fringe events are in `(1/6,1/3)`, and the larger is the upper fringe, exporting the majority pair `(10,6)` with probability `162/233`.

For `(10,6)`, `Pred(6)\Pred(10)={5}`, `Succ(10)\Succ(6)={3}`, with `alpha'=135/466`, `beta'=41/233`, `eta'=35/466`; now the larger fringe is lower and its complementary majority pair is exactly `(5,10)`. Thus the deterministic largest-fringe selector has the exact cycle

`(5,10) -> (10,6) -> (5,10)`.

This refutes only `LOCAL-GREEDY-PROGRESS`: the local crossed-neighborhood inequalities by themselves do not make the largest-channel outward selector well-founded.

## Named-partner conditioning applied

The same cycle lands twice in account03/B10's still-unpaid larger-predecessor-majority-late branch.

- `(a,b,d)=(10,5,1)`: `gamma=Pr(1<5)=185/233`; in `P+(1<5)`, the predecessor sets of `10,5` are equal and `Pr(10<5)=27/74` is balanced, but the original probability is `(185/233)(27/74)=135/466<1/3`.
- `(a,b,d)=(6,10,5)`: `gamma=Pr(5<10)=331/466`; in `P+(5<10)`, the predecessor sets of `6,10` are equal and `Pr(6<10)=142/331` is balanced, but the original probability is `(331/466)(142/331)=71/233<1/3`.

Hence equal-predecessor child balance cannot be lifted on the same pair by scalar conditioning in the majority-late branch.

## Infinite asymmetric extension and next obligation

For every `s,t>=0`, `C_s ordinal-sum P ordinal-sum C_t` preserves all 18 core incomparable-pair probabilities and the exact 2-cycle, while admitting a three-chain cover of lengths `(4+s+t,4,3)`. Thus the local obstruction persists at arbitrarily large finite sizes and arbitrary first-chain asymmetry.

The first essential missing implication is now a **global anti-cycle / majority-late transport theorem**: in a cardinality-minimal no-balanced module-prime width-three candidate, show that exported fringe mass cannot cycle (or exhibit a well-founded global potential), and show that balanced equal-predecessor child probability in the majority-late conditioning branch forces some possibly different original pair into `[1/3,2/3]`.

## Exact science artifacts

Canonical science commit: `a23e37824f794ce9f269b03bd46c57b58b522234`.

- report blob `a2a326ce5e71abf67cde82f08a6806d067f13978`
- verifier blob `76b35c2e6753d299ada7fa245cc2cf6c8b83151d`; source SHA-256 `c61e836cf62b42b369a137c98f24ce6bd1c8949a07f2a1a8405b48ee3b0b11bf`
- exact output blob `48c839e07b3c4141088940d63955b7125e47b1c5`; output SHA-256 `de017ae20bdf1d48b668bca647aee71b9b1d73f11c84d995aedb956aeffd2cb3`
- verifier terminator `POS3_GREEDY_FRINGE_2CYCLE_PASS`

No POS3 closure, novelty, or priority claim is made.