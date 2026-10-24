from pathlib import Path
import json
p=Path('SECOND_ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write(r'''

## D. Does a clever finite-minimizer tie rule evade the cost theorem?

No. For a continuous full-displacement cost C, the following are equivalent:

1. C has the universal weak uncrossing property (B1).
2. For every finite pair of equal-sized red and blue point sets in planar general position, there exists at least one non-crossing C-minimum perfect matching.

To prove 1=>2, among the finitely many C-minimum matchings choose one minimizing total Euclidean length. If it crosses, uncross the two edges. Property (B1) says that the cost does not increase. If it decreases, C-minimality is contradicted; if it stays equal, strict Euclidean decrease contradicts the secondary minimum. Thus this tie rule gives a non-crossing optimum. This proof does not require C to be coercive or strictly compatible with uncrossing.

For 2=>1, if (B1) fails at a crossing quadruple, its crossing matching has strictly smaller C-cost than the other perfect matching. These are the only two bijections on these two red and two blue points. Hence the crossing matching is the unique C-minimum, contradicting assertion 2. This proves the equivalence.

Together with Section B, this characterizes exactly the continuous additive displacement costs for which every finite general-position input admits a planar optimizer: they are constant plus continuous sublinear costs. If they are also coercive, they dominate length. Thus a secondary tie rule does not rescue the proposed slowly growing cost strategy.

A concrete convex-cost failure is certified exactly: r1=(-1/2,0), b1=(9/2,0), r2=(-27/10,-18/5), b2=(3/10,2/5). The old crossing is at zero because r2=-9 b2 and b1=-9 r1. Its two squared lengths are 25 and 25. The swapped squared lengths are 4/5 and 324/5, for a total 328/5>50. Therefore the unique squared-length optimum crosses. The endpoints lie on two distinct lines through zero with origin interior to both old segments, so the quadruple is in general position. These rational identities and the strict cost comparison are kernel-checked in UncrossingCostChecks.lean.

## E. Hostile-referee audit and final remaining gap

- The cost theorem quantifies over ALL crossing quadruples. Its proof does not silently assume a particular random matching encounters them. The finite-optimizer equivalence explains exactly when that universal quantifier is necessary.
- The nearly parallel configurations used for the functional equation are general-position configurations for every positive angle; degeneracy occurs only in the limiting step, where continuity is explicitly invoked.
- Both arm orientations are tested. Using only one would give a one-sided Jensen inequality and wrongly suggest that arbitrary convex costs suffice. The reverse orientation forces equality.
- The vector theorem needs continuity at zero. Its proof explicitly uses this to identify a common ray intercept C(0). No extension to singular or discontinuous costs is claimed.
- Sublinear here means subadditive and positively homogeneous, not necessarily symmetric or nonnegative. Nonnegativity and a strictly positive uniform directional lower bound are deduced ONLY after assuming coercivity.
- The finite-cost obstruction is not inferred merely from the possibility of infinite expected length. The full proof passes a uniform mean bound through a compactly supported displacement cutoff and monotone convergence, obtaining the actual contradiction to source Theorem 2.
- The convex-cell route requires all points in cell interiors and a measurable stationary cell partition. An arbitrary planar matching is not assumed to yield such a partition.
- The strip theorem assumes a locally finite bi-infinite cut set avoiding input points, and neither finite cut intensity nor any moments of interval size. Its stationary difference bound uses a union bound, never independence of K and K_t. The normal-limit contradiction is justified for shrinking thresholds.
- The strip conclusion is expressly restricted to bounded-cell rectangle constructions. It is not a theorem excluding arbitrary planar strip matchings.
- The colour-blind obstruction conditions on all uncoloured geometric data and independent auxiliary randomness; after that conditioning, the colours really are independent. A colour-aware partition cannot be treated this way.
- Numerical cost_probe.json has ten finite comparisons: linear cost decreases in both orientations; sqrt, log(1+t), and t^0.9 fail in one orientation; squared length fails in the other. These support the exact proof but are not substituted for it.
- second_lean_check.log records exit 0 with no diagnostics. Lean checks the four-arm inequality-to-midpoint identity and exact squared-distance counterexample. It does not check the continuous functional equation, stochastic compactness, cocycle proof, or F0082 itself.

**Remaining gap after this attempt.** The original planar Poisson perfect-matching question is still unresolved here. A uniformly tight stationary non-crossing nearly perfect family is still missing. Continuous coercive additive displacement objectives with automatic finite planarity cannot provide a finite expected-cost bound, because they necessarily grow at least linearly. A different viable construction might use explicit non-crossing constraints with a slower cost, an infinite-mean construction with tail control, or a colour-aware stationary balanced convex-cell partition not confined to fixed-width strips. None of these has been constructed or excluded. No conjectural step is labelled proved, and no novelty claim is made for the strategy-obstruction results.
''')
claim={'problem_id':'F0082','claim':'For continuous additive displacement cost C, existence of a non-crossing C-minimum matching for every finite balanced general-position input is equivalent to universal weak uncrossing, hence to C being constant plus continuous sublinear cost.','status':'proved','proof_location':'SECOND_ATTEMPT.md Section D','remaining_gap':'Does not decide stationarity or perfectness for independent planar Poisson inputs.','checks':'Finite primary-cost/secondary-length minimization; converse unique crossing two-edge optimum; exact squared-cost counterexample certified in Lean.'}
with Path('CLAIMS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(claim,ensure_ascii=False)+'\n')
with Path('ATTEMPT.md').open('a',encoding='utf8') as f:f.write('''\n\n## 8. Requested second attempt\n\nSee SECOND_ATTEMPT.md for two new approaches and complete proofs. The more promising coercive-cost strategy was pursued to a classification theorem: every continuous additive displacement cost admitting a planar minimum on every finite general-position input is a constant plus a continuous sublinear function; coercivity forces a linear Euclidean lower bound. Hence a uniform finite expected-cost route cannot solve the tightness gap. The alternative balanced-convex-cell construction remains sufficient but unconstructed; stationary fixed-strip rectangles and colour-blind partitions are ruled out. New finite algebraic checks passed in UncrossingCostChecks.lean. The original question remains unresolved by this second attempt.\n''')
# Replace the pending check with its actual completed, limited scope.
p=Path('CLAIMS.jsonl');s=p.read_text(encoding='utf8').replace('cost_probe.py; Lean check pending.','cost_probe.py; four-arm midpoint certificate kernel-checked in UncrossingCostChecks.lean (exit 0).');p.write_text(s,encoding='utf8')
