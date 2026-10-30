# FEI working groups, 22-23 September 2026

Full FEI remains open. This folder holds the work of five groups started on 22 September 2026 at 23:1x (Israel time)
on the owner's order to attack the Fourier Entropy-Influence conjecture with Opus 5.5 agents at maximum reasoning.
Shared context, conventions and rules: [CONTEXT.md](CONTEXT.md). Inputs (Numaro's 18-variable record function, the
read-once potentials, the fleet's research state): [inputs/](inputs/). An independent checker written separately from
the groups' code, used to audit every certified claim before it is reported: [audit/fei_audit.py](audit/fei_audit.py).

This index is updated as results land. Entries marked INTERIM come from the groups' running logs and have not been
audited; they are recorded so that nothing learned is lost if a run stops.

| group | target | state |
|---|---|---|
| [F1](F1-biased-record/) | beat the lower-bound record 6.521845710923046575 by feeding biased inputs into Numaro's gate g (Hod's mechanism on top of the record) | finished 01:18, no record; [REPORT](F1-biased-record/REPORT.md) |
| [F2](F2-new-gates/) | new balanced base functions with H/(I-1) above the record; does the ratio grow without bound along the record constructions? | finished 01:37, no record; [REPORT](F2-new-gates/REPORT.md) |
| [F3](F3-small-arity/) | smallest fan-in at which a gate defeats the read-once potential; FEI for read-once formulas over fan-in-3 gates | finished 01:28; [REPORT](F3-small-arity/REPORT.md) |
| [F4](F4-proof-attempt/) | the general conjecture | finished 00:55; [REPORT](F4-proof-attempt/REPORT.md) |
| [F5](F5-monotone/) | FEI for linear threshold functions (folder name is historical) | finished 01:04; [REPORT](F5-monotone/REPORT.md); independent audit in progress |

## Waves 2 and 3 (launched 23 September, 01:4x and 02:1x)

| group | target |
|---|---|
| W2-A | independent referee of F5's proof for threshold functions, and a novelty search |
| W2-B | extensions of F5's method: polynomial threshold functions, functions of several halfspaces without co-monotone weights |
| W2-C | general FEI through richer reference measures (adaptive or hierarchical orderings), the obstruction being recursive majority |
| W3-01 | FEI for monotone functions |
| W3-02 | FEI for transitive-symmetric functions and graph properties |
| W3-03 | the Fourier min-entropy version (FMEI) |
| W3-04 | removing the log I factor of Kelman-Kindler-Lifshitz-Minzer-Safra |
| W3-05 | interpolation along the noise semigroup |
| W3-06 | new host structures for a lower-bound record |
| W3-07 | value iteration over rich gate sets: read-once constants for fan-in up to 7, and a record if the iteration crosses 6.5218 |
| W3-08 | multiscale random-restriction induction |
| W3-09 | the sharp constant for threshold functions (14.22 against the conjectured 4) |
| W3-10 | structure of near-extremal functions and minimal counterexamples |

## Finished groups

The ten groups still running early on 23 September (W2-A, W3-01 to W3-03, W3-05 to W3-10) were stopped to save compute
budget before they wrote reports. What their logs show is in [STOPPED_GROUPS_2026-09-23.md](STOPPED_GROUPS_2026-09-23.md): a
10-variable balanced function with H/(I-1) = 6.4594, above Hod's 6.4548 (re-checked by the coordinator); an interval
certificate for H <= 4I on AND/OR chains, where 4 is sharp; an explicit FMEI constant 7.1813 for unate functions; and the
referee's lemma-by-lemma numerics for F5, all below 1.

W3-04 ([REPORT](W3-04-kklms/REPORT.md)). The log I factor of Kelman-Kindler-Lifshitz-Minzer-Safra is not removed. The group
mapped their proof and showed that the log comes from the form of their main inequality (Proposition H: level costs add up
harmonically; Proposition M: majority forces the leading constant to be exponential in d for any cross-influence
coefficient below k^(-3/2)). It also proved Theorem A: on their large-coefficient bucket the charge |S| log |S| can be
replaced by exact counting or F5's rank measure, which removes the log for majority.

W2-B (claimed proved; rests on F5's framework, which the W2-A referee is checking; [REPORT](W2-B-extensions/REPORT.md)).
F5's argument becomes a criterion: if every derivative D_i f is "localized" (noise on the units ranked before i makes
D_i f vanish with probability O((noise x rank)^(-1/2))), then H <= C I (Theorem 1). The criterion survives Boolean
combinations by interleaving the orders round robin (Proposition 2; the coordinator re-derived this step), and holds for
thresholds of block-separable functions (Proposition 3). Consequences: every Boolean function of k halfspaces satisfies
H <= C_k I with C_k = 3 log2 k + O(log log k) (C_2 = 17.715; no co-monotonicity needed), covering intersections of k
halfspaces, depth-two threshold circuits and linear decision trees; block-separable polynomial threshold functions of
block size d satisfy H <= C I with C = O(d). The dependence on k cannot be removed by this method (recursive majority).
Also a two-line concavity proof of the scalar inequality that F5's Lemma 5 had only checked on a grid. Numerically,
read-once 2-CNFs (degree-2 PTFs and intersections of halfspaces) have H/I -> 4.8677, so the sharp constant for those
classes exceeds 4.

W2-C (proved and numerical; [REPORT](W2-C-reference-measures/REPORT.md)). Proved: no level-wise product reference
measure (which includes F5's rank measure for every ordering) can prove FEI, since on depth-d recursive ternary
majority every such reference costs at least (d - 1) I while H = 4(I - 1). Proved: count-splitting tree references
(reveal |S|, then split the count down a binary tree over the coordinates) are exact for symmetric functions and closed
under read-once composition. Proved: a restricted block R carries at most (2/ln 2) Inf(R) bits about the rest of the
spectral sample, hence FEI is equivalent to a block-erasure inequality K_b <= C_FEI <= K_b + 2/ln 2. Numerical: for
every function tested (all of n = 4, 100,000 random at n = 5, 20,000 at n = 6, adversarial searches to n = 8, Numaro's
g) some count-splitting tree comes within 1.39 bits of the entropy, i.e. the spectral sample is nearly count-Markov
along a tree; the loss appears only on functions that switch between incompatible hierarchies, and restricting the
switching coordinates prices it.

F2 (certified identification; no new record). Numaro's record function is the perfect-matching property of K_{3,3}:
read the nine core variables as the edges of K_{3,3}; g is true iff the edge set contains a perfect matching, or it is
a "cross" at an edge p (the stars of p's two endpoints, five edges) or that cross minus p and the coin variable y_p is
true. Rebuilding the table from this description reproduces the published SHA-256. This explains both published
record notes exactly (sharing one coin between two sites costs 1/128 of entropy at equal influence, i.e. 1/133 in the
ratio). The construction peaks at exactly nine coins: the ratio is 6.4011, 6.4475, ..., 6.5143, 6.5218 for 1 to 9
coins and falls afterwards (6.5171 at 19 variables). g is a strict local optimum under two-cell changes, coin
relocation and new coins, and the unique optimum among all cores invariant under its order-144 symmetry group; other
hosts (K_{3,4}, K_{4,4}, projective and affine planes) give at most 5.94. A 14-variable member of the family is
certified at 6.4917705, above the published 14-variable value 6.4901128 (not above the overall record). No family with
growing H/(I-1) was found.

F3 (certified and proved parts; the fan-in-3 theorem itself is only numerical). Certified: a composition-prime
monotone 7-input gate G7 (a restriction of Numaro's g) violates the gate inequality of the read-once potential at
p = (1/2, 1/2, 7/24, 1/2, 1/2, 2/7, 5/17), D = -6.7843957708e-3, and also violates it for the certified potential
behind H <= 6.4573 I (D = -5.1036e-3), so that induction cannot pass fan-in seven. The mechanism is that the read-once
potential has narrow V-shaped dips at dyadic measures and G7 puts its output on a shoulder of the dip at 1/2. Certified:
the XOR gate inequality, so every read-once formula over AND, OR, XOR and NOT satisfies H <= 6.4573 I. Proved: the five
composition-prime 3-input NPN classes (one-hot, MAJ3, EQ3, MUX, Q3), a selector-expansion identity for the gate
defect, and a closed form of the MUX remainder. Numerical: no gate of fan-in at most six (monotone at fan-in 5 and 6)
beats the AND margin, and every prime 3-input class asks at most c = 1.04e-3, so read-once formulas over fan-in-3 gates
appear to satisfy the same 6.4573; an interval certificate for the prime 3-input classes is still missing.

F1 (proved local statement, numerical global one; no new record). Numaro's g has 72 automorphisms and 72 dual
isomorphisms g(pi x) = -g(-x), so the one-input composition slack is even in the bias and all first derivatives
vanish; along exactly balanced bias directions the slack rises like eps^2 log2(1/eps^2) Lambda(v) with Lambda
positive definite (exact LDL, smallest pivot 3.58e-3). So g is a strict local minimiser of balanced slack under input
bias. Value iteration over AND/OR/NOT and g with biased inputs converges with V(1/2) = C at the record constant: Hod's
biased-composition mechanism does not improve the record on this gate. An apparent divergence with all nine core
inputs biased together is a chord-interpolation artifact that disappears on a finer grid.

F5 (claimed by the group as proved; independent audit in progress, do not cite yet). Every linear threshold
function f = sgn(w.x - theta) satisfies H(f) <= 14.2142 I(f). The proof orders coordinates by |w_i|, uses the
Erdős-Littlewood-Offord inequality to show that the derivative D_i f is noise-sensitive under noise on the
coordinates at least as heavy as i, deduces that the spectral sample lives on the top O(|S|) coordinates in the
weight order, and closes with a rank-weighted reference measure and the level-entropy lemma of O'Donnell-Wright-Zhou
(H(|S|) <= 3I). Corollary: constant O(log k) for any function of k threshold functions with co-monotone weights.
Numerically the sharp constant for the class looks like 4 (approached by AND/OR chains, 3.99225 at n = 22). FEI for
general linear threshold functions was open before this (only random LTFs and the absolute bound H = O(sqrt n) were
known).

F4 (proved and certified; no change to FEI itself). FEI is equivalent to FEI restricted to functions whose
influences are all below any fixed threshold tau (Theorem 2.1); a counterexample would localize to a subcube
restriction on which the restriction step fails at every coordinate. Exact composition laws for the erasure entropy
and for the restriction drop. On the self-compositions of Numaro's g the restriction-step constant is certified at
6.3290, 6.8901, 7.0519 (324, 5832, 104976 variables; numerical limit 7.1116), so any potential-free coordinate
induction needs a constant above 7.05, and a measure-only potential for it needs a convex corner at 1/2. Three
strengthenings of the erasure route are refuted (per-coordinate erasure fails even for monotone functions: majority
plus one flipped point has ratio at least (n - 3 log2 n)/2).

## Independent checks already done (audit/fei_audit.py, python-flint arb balls, exact integer Walsh transform)

- Numaro's g: H = 6.7766053090059780825 +- 2e-20, I = 261/128, H/(I-1) = 6.521845710923046575658 +- 1.4e-22,
  monotone, not self-dual, no coordinate-swap automorphism.
- The composition identity (CONTEXT.md section 3) against direct expansion of the full truth table: exact agreement
  of the measure and of I, and H to 1e-75, on five random three-level compositions (n = 10).
- The fleet's biased point (one core input of g at Pr[true] = 3/8): p_out = 967/2048, It_1 = 855/4096,
  sum_{i>=2} It_i = 465/256, Htilde = 6.744254737056313266470..., matching
  `fleet-2026-09-21/fleet03/B12/20260922T061544Z-biased-prime-candidate-refutation/REPORT.md` to every digit.
- Every Walsh coefficient of g on a set of two or more auxiliary coordinates (subsets of {9,...,17}) vanishes (502 of
  502 sets), because the nine auxiliaries host disjoint cells. Hence biasing only auxiliary inputs gives
  E F = (sum_j mu_j)/256 exactly, and opposite auxiliary biases keep a composition exactly balanced with dyadic
  measures. Core-auxiliary pair coefficients are nonzero for 72 of the 81 pairs (each +-1024/2^18).

## INTERIM findings (numerical, from the running logs, not yet audited)

- F1. At C = 6.521845710923046575 and at C + 1e-6, C + 1e-7, value iteration over AND/OR/NOT together with g fed by
  biased inputs gives V(1/2) - C = 0: no composition found reaches measure 1/2 with slack below C. The g-moves do
  lower the slack function away from 1/2 (at C + 1e-4, V(0.48) - C = -4.0e-3, V(0.45) - C = -8.3e-2), but not at
  1/2. The group reports that g is a strict local minimiser of the balanced slack under input bias (first
  derivatives vanish, leading term positive definite on the balanced subspace). Hod's mechanism does not improve
  the record locally.
- F2. Simulated annealing started from Numaro's function on a 9-variable core returns exactly 6.521845710923;
  10-variable embeddings reach 6.5171; design-based constructions reach 5.21. No new record so far.
- F3. A 7-input gate (`F3-small-arity/logs/g7_h24_and_xor.out`) asks the read-once potential for a quadratic margin
  c = 4.064e-02 at p = (1/2, 1/2, 0.2904, 1/2, 1/2, 0.2879, 0.2919), about nine times the 2-input AND value
  4.397e-03, under both cert_vi_h24k40 and cert_vi_h96k40: the read-once constant does not extend to fan-in 7. The
  monotone fan-in-6 screen was still running (no violation in the first 32 of 63 subsets). For the if-then-else gate
  MUX a closed-form remainder was found, with min D/W = 9.4e-3 on the tested grid (positive margin), which is the
  basis of a proof attempt for read-once decision trees; for XOR, D_XOR = Gamma(p) + Gamma(q) - Gamma(p+q-2pq) >= 9e-9
  on a 1201^2 logit grid.
- F4. On towers of Numaro's g, the restriction-step constant min_i (Delta_i H)/Inf_i reaches 7.11 at depth 8 and the
  erasure ratio B/Inf is about 4.56 (certified intervals at depths <= 3 per `F4-proof-attempt/logs/certify_tower.log`,
  floating point beyond). Any potential-free coordinate induction therefore needs a constant above 7.1 on these
  functions.
- F5. Largest H/I found so far among linear threshold functions: 3.74; a lemma-by-lemma proof attempt is in progress.
