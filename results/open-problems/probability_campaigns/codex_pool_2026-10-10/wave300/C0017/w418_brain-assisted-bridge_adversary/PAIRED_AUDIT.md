# Audit of w417's product-law bridge

2026-10-10. Independent obstruction was saved first in INDEPENDENT_OBSTRUCTION.md. Subsequently read w417's CLAIMS.jsonl entries L1-L3; full argument check is recorded below and in the review packet. Referee of this worker's new deductions: w419, pending.

L1 is valid with its stated finite common cell skeleton, product laws, Boolean event, and the actual hybrid exterior laws. Write the signed expectation difference as a telescoping sum replacing cells in a fixed order. Conditional on an exterior, a constant Boolean section contributes zero; a nonconstant section differs by at most the one-cell total variation. Integrating under the actual exterior law at that step and applying the triangle inequality gives the proposed sum. No independence between the sensitivity events is needed. This is a keep for the finite comparison lemma, with no claim about C0017.

The hardest step is G1: faithful common-skeleton model representations and a bound tending to zero for the SUM of TV_i times sensitivity_i under every actual hybrid law. Endpoint arm or pivotal estimates cannot automatically replace those hybrid probabilities.

Here is a separately derived counterexample to that replacement, not to L1. For 0<epsilon<1/2, take three independent bits and f=1{at least two bits equal 1}. Let mu=Bernoulli(epsilon)^3 and nu=Bernoulli(1-epsilon)^3. A section in cell i is nonconstant exactly when the other two bits differ. Under either homogeneous endpoint, this has probability 2 epsilon(1-epsilon). Each cell total variation is 1-2 epsilon. An endpoint-only replacement of L1 would therefore give the bound

    6 epsilon(1-epsilon)(1-2 epsilon),

which tends to zero. The actual expectation difference is

    E_nu f-E_mu f = 1-6 epsilon^2+4 epsilon^3,

which tends to one. At epsilon=1/100 the false endpoint bound is 14553/250000 = 0.058212, while the difference is 249851/250000 = 0.999404. For replacement order 1,2,3, the three correct hybrid sensitivity probabilities are 2 epsilon(1-epsilon), (1-epsilon)^2+epsilon^2, 2 epsilon(1-epsilon). Their sum times 1-2 epsilon equals the actual difference exactly. All six endpoint bit laws are nondegenerate; the event is monotone; independence alone does not repair the endpoint substitution.

In fact, subtracting the false endpoint bound from the actual difference gives (1-2 epsilon)^3>0 for every 0<epsilon<1/2. The failure does not require a limit approaching degenerate laws: at epsilon=1/4, the endpoint bound is 9/16 while the difference is 11/16. w417 has explicitly confirmed that its L1 uses H_i, that no endpoint replacement is claimed, and that it has no additional G1 estimate.

Minimal additional premise for applying L1 to C0017: specify the common finite cell skeleton and complete connectivity-state laws faithfully representing both models; prove uniform sensitivity bounds for each intermediate law, including boundary cells; and prove that the resulting total weighted error tends to zero. Merely matching pair connectivity or bounding sensitivity under the two homogeneous models does not supply this premise. If a growing gadget is used, its physical diameter and edge count must enter the arm-event and error bounds. No numerical arm exponent from triangular site percolation may be silently inserted into an unproved square-bond estimate.

NEXT: Verify the full w417 argument against these premises and send the precise KEEP-with-G1-gap verdict to w417 and w419.
