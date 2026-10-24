# Independent rereading of the recorded argument, 2026-10-12

This is the author's second, hostile rereading, not an external peer review.
No full solution of E0062 or novelty of the special cases is claimed.

## Conclusions of the mathematical rereading

The acyclic-sign theorem, nonzero-entry criterion, four-cycle convergence
theorem and balanced-four-cycle divergence theorem survive the rereading.
The divergence theorem's final parameter range is 0<a,b,c,d≤1 and ac=bd;
it treats every nonfixed interior point. All boundary trajectories in that
four-cycle family converge, because every proper induced graph is acyclic.

Checked load-bearing steps:

1. The graph orientation is winner to loser. Its topological ordering gives
   nonnegative cross terms in every prefix sum. Differences of convergent
   prefix sums give coordinate convergence even with ties and boundary
   starts. No strict-sign or transversality assumption is inserted.
2. The triangle obstruction uses a principal invariant face and source
   Theorem 3. This is an explicit published dependency, not a self-contained
   reproof or a theorem addressing arbitrary zero entries.
3. For the convergence family, the exact product expansion yields a
   nonnegative increment. In equality cases the positive initial product
   supplies the missing strictly positive summability constant. Proper
   faces are handled separately, so division by a zero product is avoided.
4. For balanced weights ac=bd, both proportional payoff identities and
   their exponents were checked directly. Weighted AM-GM scales linearly
   with the pair's total mass because its exponents sum to one. A positive
   pair-product limit forces its payoffs to zero. The both-positive limit
   is excluded by a strict initial decrease; a one-positive limit is
   excluded by the two separated roots, vanishing jumps and invasion.
5. The two-root argument uses compactness to put all sufficiently late
   terms in two disjoint neighborhoods, then vanishing increments prevent
   transitions. This is a convergence argument, not an inference from
   merely approaching a continuum of fixed points.
6. Empirical cluster measures are invariant by a bounded continuous
   telescoping identity and are supported on the adjacent-edge network
   by product decay. Each open edge is invariant within that network.
   Equality of measures, established by continuous tests, permits the
   discontinuous bounded Borel edge test. Its strictly positive coboundary
   excludes invariant mass in the edge interior.
7. Coordinate average convergence implies weak empirical-measure
   convergence here only after every cluster measure is shown to be
   vertex-supported; its vertex masses are then uniquely the averages.
   This implication would be false without that support argument.
8. For losing coefficients below one, the logarithm is continuous and
   bounded on the whole simplex. At coefficient one it is replaced by a
   continuous clipped logarithm giving an upper bound. No average of an
   unbounded logarithm or interchange of singular limits is assumed.
9. Adjacent positive average masses force a positive next mass via the
   loser's finite zero rate, or are immediately contradicted by a
   coefficient-one clipped bound. Propagation around the cycle either
   reaches a singular edge or produces four positive masses, contradicted
   by the strict-negative finite rate identity.
10. Opposite-pair averages need only one missing species to be summable.
    Strict logarithmic inequalities exclude both missing finite rates being
    zero; clipped bounds cover singular rates. Summable one-sided
    increments of bounded surviving coordinates imply finite total
    variation and convergence, contradicting pair-product decay.
11. A single-vertex average is excluded separately: its loser is summable,
    giving actual convergence of the vertex and its neutral opposite. The
    remaining predator tends to zero but has a multiplier eventually above
    one, a contradiction to its positive finite-time mass.

The only edit prompted by this rereading was to express the weighted-AM-GM
scaling with t=Tξ explicitly. It does not change the theorem or its range.

## Verification limits and remaining gap

Weak sequential compactness of probabilities on a compact metric space
and uniqueness from continuous integrals are standard dependencies. The
ordinary analytic proofs are written in ATTEMPT.md and are not formalized
in Lean. The Lean file targets finite algebra and inequalities only. Its
compiler outcome is unrecovered, and no Lean-checked claim is made; see
VERIFICATION.md and the preserved original result marker.

The stored exact rational check results are PASS: 2,187 prefix/cut checks,
23,166 strict-parameter product checks and 858 equality-parameter checks.
The simulations are evidence only and are never used as proofs of
infinite-time divergence.

The magnitude-dependent necessary-and-sufficient condition for arbitrary
skew-symmetric matrices with zeros is missing. Even the unbalanced
four-cycle a=c=1/2,b=d=2/5 is not decided by the recorded theorems.
The bounds of the proved convergence region are sufficient only. No
equivalence between average convergence and trajectory convergence is
proved for the general class. Literature status remains bounded-search
“no verified full solution found,” rather than a universal absence claim.
