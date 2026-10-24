# Root independent analytic audit: matching negative association

2 October 2026 UTC. **PASS for the exact family and conditioning scope in
`forest_rank_one_core3_matching_negative_association_proof.md`.** This is
an internal mathematical audit, not outside peer review or a priority claim.
Root read the complete final proof, the entire author verifier, the earlier
pair theorem and the independent original-graph checker. Root independently
rederived the argument below and reran both exact verifiers successfully.

## The support-at-most-two lemma

For empty/singleton/pair masses A, h_i t_i, K t_i t_j, the hit probabilities
for disjoint E,F have unnormalized joint mass K s_E s_F. Expanding their
marginal product against this joint mass times the full normalizer gives
exactly equation (5) of the proof. In particular, the terms involving
internal pairs q_E and q_F remain present and positive; they have not been
discarded under a false independent-singleton approximation. The bracket
is nonnegative under h_min^2 >= K A and 2 h_min >= h_max, because each
weighted average beta lies between the two extrema and
s_C^2-q_C = sum_C t_i^2+q_C >= 0. Empty blocks are treated directly.

For nontrivial increasing events on disjoint blocks, simultaneous occurrence
uses precisely one triggering singleton in each block. An event requiring
two coordinates in its own block cannot occur jointly with another
nontrivial event, since the support has size at most two. Therefore the joint
event is exactly the corresponding two hit events, while each marginal is
at least its hit marginal. This proves every event inequality, not just
coordinate or hit inequalities. Finite upper-level-set decompositions,
after subtracting constant values, prove the real-function statement.

## Independent reconstruction of the matching law

For each matching group its normalized factor is
1 + theta_i [exp(delta_i P+epsilon_i Q)-1]. Since P^2=2 B Q and every
higher product vanishes, multiplication yields a constant F_0, singleton
terms [M delta_i+J epsilon_i+B J delta_i^2] theta_i, and pair terms
2 B J delta_i delta_j theta_i theta_j. These are exactly the claimed
forced-subset weights. For any matching configuration x, integrating the
independent Bernoulli variables after forcing Y gives
P(R=x) sum_{S subset x} f(S), divided by the normalizer. Direct coefficient
expansion of the original matching partition function gives the same
expression. The OR representation is an equality of full laws, including
all configurations with three or more present matching edges; only the
auxiliary forced subset, not the actual matching configuration, has size
at most two.

## Parameter inequalities

Polynomial division gives
delta = B^-2[1+d(a+b)^-1-d(a)^-1-d(b)^-1], positive and strictly below
B^-2 for positive a,b. The function
[(2/B)alpha(x)-gamma(x)]/x = B^-2[1-d(x)^-2]
is strictly increasing, proving epsilon < (2/B)delta. Consequently
M < h_i < M+3J/B. The primitive-variable certificate for L^2-2BJS is
strictly positive, and B L >= 9J. Together with Gamma_0 <= U_0/B, direct
expansion gives

M^2-2BJ F_0 >= L^2-2BJS+2J(BL-J)U_0+2B^2J^2 U_0^2 > 0.

Thus h_min^2 > K F_0 and h_max < 2 h_min. No bound depends on the number
of terminals or matching edges, or on the positive matching activities.

## Passing to indicators and conditioning

Conditional on Y, increasing functions on disjoint matching blocks depend
on independent Bernoulli blocks. Their Bernoulli-averaged functions remain
increasing in the respective Y blocks. Applying the proved auxiliary NA
lemma therefore proves the matching-vector NA statement directly.
Conditioning matching edges present contracts disjoint terminal pairs and
sums their row activities; conditioning them absent deletes them. The
remaining graph retains exactly the family in the theorem. External fields
change only matching activities. This does not authorize conditioning
spoke/core indicators. Zero-row endpoints give independent bridge indicators
and can be separated; their removal preserves the remaining family.

## Scope and exact checks

Root reran the complete author checker: four original matching tables agree
with the OR representation; all 432 partial conditionings satisfy 10,714
disjoint increasing-event inequalities. Independent forced-law tests also
cover a six-coordinate instance and an equality boundary of the lemma.
Root reran the independent pair checker: two uncontracted original graphs
with a third matching edge, 36 rational nilpotent-basis comparisons through
100 terminals, and four zero-endpoint cases pass. Computations corroborate
the analytic argument; they do not replace it.

The diagonal-theta quadratic for five equal small matching groups has the
negative exact discriminant recorded in the final proof. Its upper-half-
plane zero remains an upper-half-plane zero under the inverse positive
Möbius map w=z/[c(1-z)], and the prefactor is nonzero there. Hence the
matching generating polynomial need not be real stable. NA is proved by
the explicit support-two construction, not inferred from strong Rayleigh.

No all-edge NA, arbitrary-core theorem, non-rank-one spoke theorem, or
general all-fugacity forest conjecture is concluded. The final proof is
continuous with the audited candidate and adds an explicit real-stability
scope witness; both files are preserved separately.
