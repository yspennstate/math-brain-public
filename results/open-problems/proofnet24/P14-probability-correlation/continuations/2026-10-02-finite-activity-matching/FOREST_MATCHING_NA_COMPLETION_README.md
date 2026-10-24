# Finite-activity forest continuation: source boundaries and exact checks

2 October 2026. This checkpoint covers only the new finite-activity
continuation. It does not recycle the all-graph high-fugacity proof as an
all-fugacity solution. Historical novelty and external review remain
unverified.

## Strongest theorem in this continuation

`forest_rank_one_core3_matching_negative_association_proof.md` proves
**negative association of the entire terminal-matching indicator vector**
over the rank-one weighted three-vertex core described below. It also
proves this after conditioning any matching indicators and under arbitrary
positive external fields on those indicators. This is the strongest final
scope of the continuation. It has received a full independent analytic
PASS in `MATCHING_NEGATIVE_ASSOCIATION_ANT_INDEPENDENT_AUDIT.md`; the parent
has independently rederived the forced-subset lemma and exact law, read
the entire final proof and independent checker, and rerun that checker.
Its separate complete audit is `FOREST_MATCHING_NA_ROOT_AUDIT.md`.

The matching law is exactly an independent Bernoulli vector with a random
forced subset of size at most two. A self-contained quadratic-weight lemma
proves negative association of the forced subset, and a direct conditional
expectation argument proves its preservation under the Bernoulli OR map.
No general forest negative-association preservation theorem is assumed.

`forest_rank_one_core3_arbitrary_matching_proof.md` proves the Rayleigh
inequality for **every pair among an arbitrary matching of terminal edges**
over a weighted three-vertex core. There may be arbitrarily many terminals
and matching edges. The spoke activities are rank one:
`z_(terminal j,core i)=a_j b_i`, with arbitrary positive column weights
`b_i` and arbitrary nonnegative row weights `a_j`. The core activities are
arbitrary nonnegative numbers. Matching activities are arbitrary nonnegative
numbers, with positive values for the two indicators being compared.

The Rayleigh difference is strictly positive when the four marked endpoints
have positive row weights. Zero row weights at a marked endpoint give a
bridge or a trivial component and are covered by the nonnegative limit.
Parallel core edges aggregate exactly. The proof retains the logarithmic
variance introduced by summing over all other matching-edge states, rather
than proving an inequality only after conditioning them away.

The theorem does **not** cover arbitrary spoke/core pair types, arbitrary
non-rank-one spoke arrays, cores of unrestricted size, all forest indicators
on these graphs, or the full forest/random-cluster conjecture. Its negative
association assertion concerns only the matching indicator vector. The
final proof gives an exact five-coordinate example whose matching
polynomial is not real stable, so strong Rayleigh is not claimed.

## Immutable progression of complete derivations

| Derivation | Scope | Main verification |
|---|---|---|
| `TWIN_MATCHING_CORE3_ALL_TERMINAL_COUNTS.md` | Common spoke activity, arbitrary terminal count, arbitrary core weights, two added matching edges | `twin_matching_core3_all_terminal_counts.py` and results JSON |
| `forest_three_core_twins_queueing_independent_derivation.md` | Independent full common-spoke derivation and equivalence of two positive formulas | Complete algebraic derivation |
| `THREE_CORE_TWINS_ANT_INDEPENDENT_AUDIT.md` | Independent analytic common-spoke audit | `three_core_twins_ant_independent_check.py` and checks JSON |
| `forest_twin_matching_heterogeneous_core3_proof.md` | Arbitrary terminal row activities, common column weights, two added matching edges | `forest_twin_matching_heterogeneous_core3_exact.py` and results JSON |
| `THREE_CORE_HETEROGENEOUS_ANT_INDEPENDENT_AUDIT.md` | Independent analytic heterogeneous-row audit | `three_core_heterogeneous_ant_independent_check.py` and checks JSON |
| `forest_rank_one_core3_arbitrary_matching_proof.md` | Arbitrary row and column factors, arbitrary additional disjoint matching edges, every matching/matching pair | `forest_rank_one_core3_arbitrary_matching_exact.py` and results JSON |
| `RANK_ONE_ARBITRARY_MATCHING_ANT_INDEPENDENT_AUDIT.md` | Independent full rank-one/matching pair audit, including integrated matching variance | `rank_one_matching_ant_independent_check.py` and checks JSON |
| `forest_rank_one_core3_matching_negative_association_proof.md` | Entire matching vector negatively associated, also conditionally and under fields | `forest_matching_negative_association_exact.py` and results JSON |
| `MATCHING_NEGATIVE_ASSOCIATION_ANT_INDEPENDENT_AUDIT.md` | Independent full NA proof audit, literal OR law and scope boundary | `matching_na_ant_independent_check.py` and checks JSON |
| `FOREST_MATCHING_NA_ROOT_AUDIT.md` | Parent's separate full analytic audit and independent-check rerun | All final proof steps and scope limits PASS |

The strongest proof is self-contained; reading the earlier restricted
versions is not needed to infer its validity. The earlier versions are
preserved as independent derivations and checkpoints, not separate claims
of several new resolutions. Their pairwise scopes are superseded by the
complete matching-vector NA theorem; they remain useful as independent
algebraic derivations. The root has completely read the strongest proof
and code and rerun its exact script successfully. Both the rank-one pair
theorem and the stronger matching-vector NA theorem have separate complete
adversarial analytic audits named in the table. The exploratory
`forest_rank_one_core3_matching_negative_association_candidate.md` is
preserved separately; the final proof is the authoritative theorem file.

## Exact-check design and representative values

The scripts use exact integers or Fractions. They separately compute the
four marked forest coefficients `A,B_e,B_f,C`; the Rayleigh difference is
`B_e B_f-A C`. The main independent routes are:

1. Subsets of the original uncontracted graph, with union-find acyclicity
   tests for adding each marked edge or both. This does not calculate the
   coefficients using the closed transfer formula.
2. Explicit five-state core-connectivity transitions, including contractions
   and summation over other matching states. This does not substitute the
   alpha/gamma formula for each transfer.
3. The analytic normalized response and its exact scalar normalization.

Representative exact agreements recorded in the results files include:

* Common spokes: m=4,a=1,core=(2,3,5), `(A,B,C)=(17472,7882,3554)` and
  `R=30436`; m=5,a=1,core=(1,2,3), `R=297024`.
* Heterogeneous rows `(1,2,3,4)`, common column weights, core=(2,3,5):
  `(A,B_e,B_f,C)=(498394,182238,86818,31734)` and `R=5503488`.
* Rank-one rows `(1,2,3,4)`, columns `(2,3,5)`, core=(2,3,5):
  `(A,B_e,B_f,C)=(157916162,21477278,8948618,1216934)` and `R=18409814496`.
* Rank-one rows `(1,2,3,4,5,6)`, columns `(2,3,5)`, core=(2,3,5), with
  a third matching edge of activity 2: `R=658564909074680544`.

The independent common-spoke audit reports forty original-graph rational
cases and forty-two formula cases through m=250. The heterogeneous audit
reports forty original-graph rational cases and thirty further formula
cases through m=100. The final rank-one script includes zero rows at
unmarked terminals, rational activities, more than two matching edges, and
explicit frontier/formula comparisons through m=100. These finite checks
are sanity checks on complete proofs, not an extrapolation argument.

For the stronger NA theorem, the author checker reconstructs four complete
matching laws by literal five-state connectivity transitions, compares
them configuration by configuration with the forced-OR representation,
and checks all disjoint increasing events after all 432 partial matching
conditionings: 10,714 event inequalities. Its six-coordinate generic
forced-subset test checks 140,058 inequalities, with a further 4,560 in a
five-coordinate boundary case. The independent checker uses six matching
indicators and verifies the literal independent OR law, all 729 partial
conditionings, and 86,634 exact event inequalities. Both checkers verify
the non-real-stability witness independently; the diagonal quadratic
discriminant is `-553191/1580777123645`.

## Exact failed routes preserved separately

`forest_deletion_contraction_obstruction.md` retains the full deletion/
contraction cross term. A weighted K4 with marked e=01,f=23 and remaining
activities z03=z12=2,z13=1,z02=w has

\[
 R_{ef}=36-6w+2w^2>0.
\]

Its middle coefficient is negative. Therefore Rayleigh positivity for the
deletion and contraction does not justify a coefficientwise-positive
recursion. The missing quantitative cross bound is
`M>=-2 sqrt(R(deletion) R(contraction))`. The companion
`forest_deletion_contraction_exact.py` compares direct subset enumeration
with an independent vertex-partition/Kirchhoff calculation. It also gives
the complete arbitrary-weight K4 square identity. This is an obstruction
to a stronger proof method, not a counterexample to forest correlation.

`forest_finite_activity_two_port_reduction.md` gives the exact two-port
connection ratio and raw Ward classification. Its unresolved response sign
`partial_e(X/Y)>=0` is equivalent to the full conjecture by adding a virtual
edge between the ports; it is not an additional monotonicity theorem one
may assume. The same note proves that no positive edge-activity-independent
mixture of `det(L+diag(root weights))` equals the unrooted forest polynomial
even for K4: the required two-component partition moments impose identical
left sides equal to both 4 and 3. This rules out that particular positive
integral representation, not every representation.

`forest_finite_activity_two_port_exact.py` independently compares raw
exterior-algebra integration with the direct separated/connected forest
sums on six weighted gadgets, verifies every associated virtual-edge
identity, and checks nine two-port gluing pairs. Its JSON explicitly states
that the full conjecture has not been proved.

## Primary-source and novelty boundary

The following primary sources were checked during this continuation:

* David G. Wagner, *Negatively correlated random variables and Mason's
  conjecture*, https://arxiv.org/abs/math/0602648 (submitted 28 February 2006).
  The abstract establishes prior two-sum preservation of Rayleigh properties.
* Alejandro Erickson, *Sums of squares and negative correlation for spanning
  forests of series parallel graphs*,
  https://arxiv.org/html/1008.3660v3 (revision 24 October 2011; published 2012).
  Its complete introduction and relevant sections were read. It proves the
  series-parallel SOS theorem and records Wagner's K7 SOS verification by
  personal communication. Minor closure would cover all weighted graphs on
  at most seven vertices from that reported certificate. Thus the common
  spoke m=4/core3 graph and other small special cases must not be advertised
  as historically new.
* R. Altar Ciceksiz and Mohan Ravichandran, *Negative Correlation for Forests
  and the q<1 Random-Cluster Model*,
  https://arxiv.org/html/2610.00549v1, submitted 30 September 2026. The
  original campaign's complete source record covers its leading high-
  fugacity coefficients and equality geometry. The present proof is at
  arbitrary finite activity on a restricted family, rather than a reuse of
  those high-fugacity statements. A crawl date is not a revised submission
  date.

Targeted searches for weighted complete-bipartite, rank-one spoke and
matching-edge forest results did not identify an earlier theorem with this
precise unbounded scope. Some narrowly worded searches returned poor or
irrelevant coverage, so that observation is weak and does not certify
priority. Broader literature and specialist review are still required.
In particular known two-sum, series-parallel, and small-graph SOS results
may subsume further special cases. The exact transfer identities and the
restricted theorem can be mathematically valid without being historically
new.

## Completion boundary

The complete mathematical advance here is a finite-activity conditional
negative-association theorem for the complete matching vector on the
stated unbounded weighted family. The two
failed universal routes have precise algebraic obstructions. The full
all-fugacity forest pair conjecture remains unresolved by this continuation.
