# T071 round 5 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 07:56 Asia/Tbilisi (UTC+4).

## 1. Orientation and opening literature check

Read REPORT.md, LOG.md and PROOF.md in all three predecessor folders, and
the latest AUDIT.md. File listings show no mathematical scripts in those
folders. No predecessor file was edited. Read ~/.claude/brain_startup.md,
the startup memory index, BRAIN_INDEX.md and compute_state.json. Compute
state was warn/cpu_saturated, owner_away_open. The later folder-only rule
supersedes requests to write shared mesh, checklist or brain state. No git,
subagents, external messages, or shared-state writers were used.

Shell reads use `env OMP_NUM_THREADS=1 nice -n 15 sh -c '...'` after the
initial listing. The sandbox reports `nice: setpriority: Operation not
permitted`; no numerical workload or background process will be launched.
All verification in this session is analytic.

The bounded literature check ran from approximately 07:56 to 07:58, under
five minutes. Web search queries:

- `"N-BBM" genealogy "2026"`
- `"branching Brownian motion" "selection" "genealogy" Bolthausen Sznitman 2025 2026`
- `"N-BBM" "genealogy" coalescent 2026 theorem`
- `"branching Brownian" "selection" "genealogies" 2025 2026 Maillard`

Opened primary sources:

- Pascal Maillard, *Speed and fluctuations of N-particle branching Brownian
  motion with spatial selection*, https://arxiv.org/html/1304.0562v4.
  Section 1.4 explicitly says its comparison changes genealogical trees.
- Alexandre Legrand and Pascal Maillard, *Time-inhomogeneous N-particle
  Branching Brownian Motion and the continuous random energy model*,
  https://arxiv.org/abs/2402.04917. Latest revision remains v4, 9 April 2026;
  the abstract concerns displacement.
- F. E. Bravo Lozano and M. C. Fittipaldi, *Microscopic Weak Selection
  Principle for the Logistic Branching Brownian Motion with selection*,
  https://arxiv.org/abs/2605.28801. Its abstract concerns a variable-size
  logistic model, hydrodynamics and minimal propagation speed.

No later solution was found. This bounded search does not prove absence of
a solution. No SOLVED_ELSEWHERE.md is warranted by the sources checked.

## 2. Independent recheck of the latest result

The latest main claim holds. Here is a check by expanding all four terminal
labels, rather than first multiplying the aggregated collision increments.
Fix four distinct younger particles a,b,c,d. An ordered terminal sample
using them has exactly w_a w_b w_c w_d choices. Its prescribed pairing
qualifies precisely when a,b share a middle ancestor, c,d share another,
and those two middle ancestors have different older ancestors. That last
condition forces all four younger particles to be distinct. Summing over
this set of ordered quadruples gives exactly the numerator of Q. Each
qualifying unordered sample has 24 label orders and belongs to one of the
three pairings. Thus its conditional probability is 3Q, including unequal
terminal weights and the older filter.

For a binary four-lineage path the allowed window starts are exactly

    0 <= s <= T,  s < S,  U <= s+delta,  s+delta+e < V.

For delta=2h and e=epsilon/2, a path with S>=h, H<=h and G>=epsilon
has an allowed interval of length at least h; S<h is covered by s=0.
Conversely allowed starts occupy at most 2h and imply the enlarged burst
event. This reproduces both sides of Proposition 2, including its factor
three and endpoint term. The Yule factorial moment is independently
2 exp(ell)(exp(ell)-1), from differentiating the geometric probability
generating function. Multiplication for two different unselected roots
and the three pairings gives the stated constant twelve. No error found.

## 3. Chosen extension, before writing the proof

Prove a conditional propagation bound for the actual terminal-weighted
observable. Freeze the older, middle and younger forest; its numerator is
a polynomial with nonnegative coefficients, multilinear in four *distinct*
younger colors. Under subsequent N-BBM evolution each such monomial has
conditional expectation at most exp(4L) times its initial value, where L
is the remaining physical time to sampling. Prove this both by independent
unselected trees and by the generator with selection deaths retained.

Combine this propagation with the preceding short-window estimate to bound
the weighted statistic away from the sampling endpoint. Retain the older
ancestor filter exactly. Then test whether the factor exp(4L) can be improved
uniformly over positions: four particles far to the right, grouped into two
middle families, should saturate it as N grows at each fixed L.

This is one piece: a terminal-weight propagation lemma and its sharpness.
It addresses the previously uncontrolled weights on bounded physical future
intervals. It will not yield the required fixed-window log-cubed estimate.
The sharpness example will identify why a position-uniform propagation
bound alone cannot supply that estimate.

## 4. Propagation proof and sharpness saved

Created PROOF.md. The conditional estimate is
E[Q(L)|H_2]<=exp(4L)Q(0), with the older filter retained. Expanding the
numerator as a sum over four distinct younger colors permits a product
of four independent dominating Yule means; no selected-family independence
is used. A second derivation gives the exact generator 4F-R, R>=0, hence
an integrating-factor formula with the selection loss subtracted.

The earlier short-window bound now yields (6) in PROOF.md for unequal
terminal weights and a physical future interval L. Its dependence on the
short merger interval remains quadratic. The sliding-window bound yields
an explicit physical-time disjoint-burst estimate (8).

To test the factor exp(4L), place four younger colors far right and group
them as two pairs with distinct older ancestors. All other younger colors
are singleton middle families. Their frozen polynomial is exactly
F(x)=8x_1x_2x_3x_4. Until saturation, leftmost selection removes only low
fillers, so these four colors evolve as independent unselected families.
The proof bounds both saturation and spatial crossings. It proves sharpness
at fixed L, and relative sharpness through L<=(1-eta)log N. At deterministic
L_N=log(N/16), the conditional filtered sampling probability has liminf
at least 3/16384, although its unweighted initial value tends to zero.

This is a bound for compatible separated marked states, not for the
all-zero population observed at (log N)^4. No global counterexample to
the conjecture is claimed. The logarithmic-time estimate is analytic;
no simulation or numerical workload was run.

## 5. Readback and independent audit

Read the complete saved proof with

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'

It matched the written proof; timestamp 2026-11-15 08:05:41 +04. The
priority warning was the same as before. Clarified that the weighted
short-window bound also holds conditional on history through t_1, not
conditional on an arbitrarily fixed later short-window realization.

Created AUDIT.md. Checked the generator directly on a monomial, including
the negative cross term for different birth/death colors. Counted the
sharpness sample independently by unordered sampling. Re-derived the
weighted saturation mean through size-biased geometric variables; its
factor is 8 exp(L)-4, not the ordinary mean 4 exp(L). An independent
exponential-martingale Brownian bound is stronger than the conservative
constant used in the proof. Checked both fixed-L and growing-L errors,
the deterministic horizon log(N/16), and the exact lower bound 3/16384.

No failure found. The new estimate is a conditional physical-time bound;
position-uniform bounds alone still fail on the conjectured clock. The
separated example gives no assertion about its frequency in the prescribed
all-zero late-time population.

## 6. Report saved

Created REPORT.md with the required PARTIAL verdict. It states the new
conditional propagation estimate, the exact selection-loss identity,
the weighted short-window consequence, and the sharpness construction.
The next step is an estimate averaged over the actual random marked
spatial configuration, rather than another bound uniform over positions.
No N-BBM genealogy convergence or literature novelty is claimed.

Final readback command:

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'wc -l LOG.md PROOF.md AUDIT.md REPORT.md; cat REPORT.md; date "+%Y-%m-%d %H:%M:%S %Z"'

Output before this append: 156, 294, 154 and 111 lines, respectively;
timestamp 2026-11-15 08:08:10 +04. The report starts with the required
VERDICT line and matches the saved proof. The same sandbox priority
warning appeared; only text was read. Tightened H_2's definition to the
actual past history, excluding any interpretation that allows future
information. All new load-bearing constants have the independent checks
recorded in AUDIT.md. All writes remained inside this task folder.
