# POS3 handoff addendum — account02/B11

Outcome: `ESSENTIAL_STEP_APPLIED`; target remains open; `WITHOUT_VERIFIED_BRAIN`.

After the first B11 handoff, the shared path exposed completed account01 POS3 handoffs. This addendum consumes:

- account01/B19 exact chain-deletion multiplicity law: restriction to `Q=P\C` is weighted by the positive integer lift count `W_C`, not uniform in general;
- account01/B10 exact three-chain path/flux representation and heavy-slice normal form.

Combined with B11's ordinal-decomposition reduction, this gives a sharper necessary condition for any width-three counterexample.

For **every** partition of a width-exactly-three counterexample into three chains `A,B,C`, deleting any one chain leaves a width-at-most-two **nonchain**: a 3-antichain places one element in each chain, so two incomparable elements survive each deletion. The width-two theorem therefore gives a uniform-balanced pair `x,y` in each two-chain remainder `Q` with `q=Pr_U(x<y)` in `[1/3,2/3]`.

Account01/B19's exact formula gives

`Pr_P(x<y)=sum_{tau:x<y}W_C(tau)/sum_tau W_C(tau)`.

Since a counterexample requires this weighted probability outside `[1/3,2/3]`, each of the three deletion-weight systems must be nonconstant and must strictly correlate with at least one uniform-balanced pair strongly enough to push it past an endpoint. Equivalently,

`Cov_U(W_C,1_{x<y}) = E_U[W_C]*(Pr_P(x<y)-q)`

has the corresponding strict sign. This holds for each deleted chain in every three-chain cover.

Next interface: prove that the three mutually compatible interval-corridor weight systems arising from one incomparability-connected width-three poset cannot all be balance-destroying. This is more precise than trying to make a deleted-chain law uniform; account01/B19 has already shown uniformity can fail badly.

Canonical mathematical addendum commit: `cc16460668fb7963658cadbd4ed0231700d47a67`, Git blob `3620112836ba6c0c5ff9230b7fd8de87c2a6b0e0`.
