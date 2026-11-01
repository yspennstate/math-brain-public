# A052 critical-slack scope

The earlier A052 tensor-purity theorem classifies exact decompositions.  The
new result instead quantifies a single physical split of a descendant-critical
source:

`slack_i = Delta_i H - R I_i`

is exactly the influence-weighted average child ratio loss.  This upgrades
the necessary inequality `Delta_i H >= R I_i` into a stability statement.

The two known component counterexamples remain outside the theorem because
their connected support pieces are not coordinate restrictions.  Criticality
is used only when asserting `R(child)<=R(parent)` for the two actual physical
children.

For equal-ratio critical tensor products, slack is inherited exactly from
the factor containing the split coordinate.  Thus arbitrary tensor powers
remain a mandatory control and no false dimension gain is claimed.

For sparse one-point surgery of a lifted hard core, qualitative
nonfactorization still proves nothing.  The critical reduction may discard
the surgery by restricting to a higher-ratio descendant.  The theorem then
applies to that selected critical descendant and quantifies which subsequent
children can leave its ratio plateau.

The exact open step is an upper bound, on at least one coordinate of every
tensor-prime critical source, for `slack_i/I_i` or for the stronger
`Delta_iH/I_i`.  Without such a bound the stability identity is structural,
not a proof of FEI.
