# Conditional lead review of C024 v1's inventory argument

Subject: w674/T186/proofs/C024_late_star_insertion_budget.md, SHA256
`7a7a0aaca0e5a9910bae093fb60eb2b79a334d795fc1d834d22aebec0f8f5a18`.
Result: the new uniform-inventory argument is correct conditional on the
specified integrable stationary-cascade/Palm premises. This is a prose audit
of that argument, not an unconditional review of C009/C021/C022/C023, an
extension of the bounded-offspring numerical check, or a finite-graph theorem.

The relevant general fact is stronger than a bound at one history length.
For a nonnegative integrable S and any sigma-field G, X=E[S|G] satisfies

    E[X 1{X>L}] <= 2 E[S 1{S>L/2}].

Indeed, on B={X>L}, E[X1_B]=E[S1_B] is at most
E[S1{S>L/2}]+(L/2)Pr(B), and L Pr(B)<=E[X1_B]. Rearrange.
The bound is uniform over sigma-fields, so it does not require nested
histories. With S the sum of all six cascade costs, this proves the exact
uniform-integrability statement needed for v_t, not just one for each pair.

Under the stated Poisson Palm law, the expected total potential above L
per template is bounded by A(L)=2c E[S1{S>L/2}], uniformly in t. For fixed t,
the finite history alphabet has a finite maximum positive-probability weight
W_t. Thus F_i<=6W_t K_i and Var(F_i)<=36W_t^2(c+c^2). Independence is used
only across the original iid templates, where it is an explicit premise.
Chebyshev controls their total tail potential. Once that event holds, the
inequality

    sum_(e in U) v_t(H_out,t(e)) <= L |U| + sum_i F_i

holds simultaneously for every subset U, including matching-dependent or
adaptively chosen subsets. There is no multiplication of conditional
probabilities for different selected edges and no assumption that U is
independent of the potentials.

The parameter order is valid for this inventory statement: fix epsilon;
choose L making A(L) small; then choose a cardinality density delta from L;
then choose a fixed t making E[K1{late-star}] sufficiently small; finally
take n large. Dominated convergence uses the integrable K and stabilization
on finitely many incident directions. LLN/Chebyshev for that fixed t controls
the bad-star stub count. A matching maps a half-edge set injectively to its
partners; considering both directions costs a fixed factor, absorbed by
the chosen stub-density allowance. This controls actual recipient-owned
potentials, rather than silently substituting an incoming latent label from
the source template. The claim explicitly prices each terminal pair and
directed response at most once; repeated marks need a separate multiplicity
argument.

The two weighted late-event assertions earlier in C024 also follow under
the same premises. In the incoming representation use conditional
expectation of the integrable sum R given the complete star histories;
the late-star event is measurable there. In the reverse representation
use Poisson Palm and the uniform integrability just proved. No additional
degree-times-cascade integrability assumption is introduced by either step.

The boundary matters. C023 assumes an interior stationary law and a
subcritical stationary change matrix. Its expected cascade costs and the
Palm law must be established for the intended model. These assumptions are
not supplied by this note. The order above does not prove that the error
is smaller than every history-dependent exploration gate gamma_t: both
the gate and the chosen error can change with t. The normal-partner law,
depletion error, repeated-hit cost, and removal of unobservable limiting
labels remain the finite-transfer work. C024 correctly leaves them open.

This is a standard conditional-expectation/uniform-integrability argument;
no originality or threshold claim is made. The final added prose has been
checked independently of the saved bounded-offspring analogue, whose
receipt concerns an earlier draft hash and cannot certify this extension.
