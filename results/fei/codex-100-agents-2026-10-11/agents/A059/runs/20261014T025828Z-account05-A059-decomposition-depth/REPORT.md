# A059 stage 3: interrupted priority stopping payment

## exact target, quantifiers, hypotheses and units

Prove a physical stopping theorem with no bound on formula depth for exclusive disjoint-core compositions. The proved scope is ordered priority controllers built from arbitrary-width disjoint point tests, arbitrarily many tests, and arbitrary adaptive data interruptions. All entropy and reserve units are bits. The exact theorem is PRIORITY_PROOF.md (4); the inherited U and actual stopping profile remain explicit. An actual growing-depth family has d point tests of width d and d private literals: d^2+d inputs and a prescribed worst-case controller path of depth d^2. The same constant covers data queries inserted during each point test. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the full execution protocol v2, BOARD snapshot 2026-10-14 02:53 UTC, B12 STREAM_NOTES v2 (2026-10-11 23:30 UTC), own STATUS and prior run proof/kernel. Read A091 run 20261014T013816Z REPORT, CLAIMS and POINT_CONTROL_PAYMENT.md: point price and terminal profile. Read A087 run 20261014T020842Z REPORT, CLAIMS and PROOF.md in full: killed-child/independent-child payment, r=s=1 continuation, and its explicit interrupted r=2 repeated-fallback next gap. A028 control-only arbitrary-width priority payment was learned from A087/BOARD; its proof is not a dependency and no independent acceptance of A028 is asserted. Source paths and SHA256 snapshots are in out/SOURCE_SNAPSHOTS.json.

## complete derivation or exact first unsupported line

PRIORITY_PROOF.md derives the fine reserve release kappa=q Var(u)+[eta(1-q)-eta(1-2q)/2]Vbar and the exact erasure sector identity for F=A u+(1-A)G with the SAME G in both children. Removing the first release and bounding the three remaining terms by 4qd, 8qd and 4qd gives B-kappa<=8 Inf. Physical JS adds 2 Inf/ln2. This is valid after arbitrary data restrictions. Ordered priority induction and the independently accepted signed data drift telescope to (4) with no accumulated depth factor. Controller-resolved terminal is eta(m^2)<=I_leaf/ln2.

PROOF.md also records exact coarse/fine terminal conversion q[T_P-eta(M^2)+s Var(state means)] and an actual Boolean mean-migration witness: querying one of two equiprobably selected literals increases the merging potential by s/2 times actual data influence. This refutes a fixed-price local helper, not FEI. Its mixed outer price overlaps A087's already-proved killed-child theorem and is expressly not claimed as novel.

First unsupported universal line: an arbitrary exclusive controller admits a physical tree whose every controller residual is paid at a universal same-tree influence rate. Even querying later priority tests before earlier tests are settled is outside this stage's theorem. Arbitrary initial core entropy and unresolved terminal payment remain explicit.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede both jobs. Exact Fraction FWHT and rational linear combinations of prime logarithms; signs use 32-term atanh bounds with a proved rational tail. Floating-point values measure runtime only. Commands from A059 cwd:

    python -X utf8 runs/20261014T025828Z-account05-A059-decomposition-depth/code/check.py --pilot
    python -X utf8 runs/20261014T025828Z-account05-A059-decomposition-depth/code/check.py
    python -X utf8 runs/20261014T025828Z-account05-A059-decomposition-depth/code/priority.py --pilot
    python -X utf8 runs/20261014T025828Z-account05-A059-decomposition-depth/code/priority.py

Mixed-state pilot PASS: 16 roots, 64 trees, 2728 assertions, 19.414 s. Main PASS: 560 roots, 1984 trees, 12032 frontiers, 81734 assertions, 854 outer nodes and 1255 terminal conversions, 231.099 s. Includes every 3-label one-bit internal map, all ordered one-bit Boolean core pairs, outer widths 1..3, four policies, and four two-bit fixtures; no symmetry reduction. The exact migration ratio s/2 is certified for s=1..64; its infinite extension is analytic, not a finite inference.

Repeated-fallback pilot PASS: 2 roots, 36 live query states, 324 assertions, 0.048 s. Main PASS: 48 roots, 1008 live private A query states, 9072 assertions, 0.765 s: (r,s)=(2,1),(3,1),(2,2), all 16 ordered one-bit Boolean core pairs, every surviving A prefix and all 9 combinations of earlier core restrictions. Direct full-function Walsh erasure agrees exactly with the new formula. Main jobs ran sequentially, with estimated memory 180 MB each, so memok threshold was not reached. Max truth table was 128 entries in the second job. Actual peak RSS was not measured. No dimension escalation occurred. These finite checks supplement the all-dimensional analytic proof.

## proof dependencies and changed downstream conclusions

Consume A059 interleaved reserve v1 as independently accepted by A091; independently reconstruct A091 point/profile scope and A087 killed/independent-child scope without substantive source repair (REVIEW_A091.md and REVIEW_A087.md). The stream review cap is addressed by these source reviews before the one new candidate is finalized. The new repeated-fallback formula supplies the boundary A087 specifically left open. It permits arbitrary-width priority tests interrupted by data and arbitrary numbers of stages, while retaining one fine reserve and actual terminal. Initial reserve funding is not reused. No arbitrary-order extension or universal FEI conclusion follows.

## one next mathematical action and independent reviewer

A091, alternate A090, should independently reconstruct equations (2),(3), including the off-label release. The next mathematical action is to expose a later priority controller while an earlier test remains undecided, and derive its exact residual under the same fine reserve. That isolates the remaining order restriction rather than reopening a settled control-only family.

## actual persistence receipts or precise save blocker

Required four protocol files, proofs, source reviews, frozen specs, scripts and exact validation outputs are saved in this run; rolling STATUS/WORKLOG/LEARNED are updated. out/RECEIPTS.json records SHA256 and sizes, generated after artifact writes, and out/SCHEMA_CHECK.json verifies exact protocol keys and compatibility equality. Files are below 20 MB. Only A059 files were written. GitHub/brain mirroring is supervisor work and is not verified here. No save blocker.

Universal bridge: This stage advances C019 stopping-tree payment by removing both priority width and depth bounds in the presence of arbitrary data interruptions: controller debt costs at most (8+2/ln2) times same-tree controller influence, and resolved terminals cost at most I_leaf/ln2. The repeated fallback is retained coherently rather than falsely declaring children independent. C018 for arbitrary controllers, arbitrary controller order, inherited arbitrary-core entropy and unresolved terminal profiles remain unpaid. The NEXT is the first out-of-order priority query: removing that order restriction tests the exact obstruction between this stopped theorem and a universal controller payment, rather than producing another isolated class estimate.
