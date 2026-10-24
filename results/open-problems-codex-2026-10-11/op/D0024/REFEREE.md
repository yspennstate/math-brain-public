# Independent hostile audit of the final claim — 2026-10-11

Claim audited: the literal Problem 3 under the general Section 2 standing hypotheses has a negative answer. This is a missing-hypothesis counterexample, not a purported resolution for connected nearest-neighbor kernels.

## Logical checks

* Kernel: p(2)=1 is finite range, translation invariant, normalized and has nonzero drift 2. It fails source (A.1). The source states (A.1) only among assumptions of Theorem 1; neither its general model nor Problem 3 imposes it. This scope check is the main possible point of dispute. If connectivity is supplied implicitly, classify these results only as a boundary counterexample and the general connected question as unsettled here.
* Rates: r(0)=0, r(k)=1 for k>=1 satisfies every bound and monotonicity condition in source (2.1)–(2.2).
* Environments: the periodic two-atom law is ergodic because the shift acts transitively. The second law is iid, supported in [1/2,1], with essential infimum 1/2. Its marginal density integrates to one exactly. Each proof works for a full-probability set of fixed environments.
* Initial spatial ergodicity: the periodic two-point configuration law is ergodic under the unit shift. The product-mixture law is also ergodic: each component is ergodic under the squared shift, and the unit shift exchanges the components. Do not mistake failure of mixing for failure of ergodicity. The iid example even has jointly ergodic environment/initial law, as proved in ATTEMPT.md.
* Density: the geometric-mixture initial law has almost-sure density 5/4 by the iid-pair strong law; the alternating 0/10 configuration has density 5. In the latter example rho*=4 exactly. A symmetric interval has at most one more site of one parity than of the other, so its empirical density differs from 5 by at most 5 divided by its length.
* Stationarity: finite-cycle global balance is checked against every allowed predecessor, including that total mass, and thus product geometric weight, stays constant. Cycle lengths 2–6 and totals 0–8 give 4,995 verified states. This is not a simulation of the infinite process. The independent handwritten Harris argument transfers invariance to infinite volume.
* Invariant empty parity: no arrow connects opposite parities; departures from empty sites have rate zero. The claimed invariant empty set is a property of every finite Harris construction component, so no infinite-volume spontaneous birth is possible.
* Weak-topology obstruction: the single-site and pair emptiness indicators are bounded continuous because N has the discrete topology. Therefore a discrepancy in their expectations rules out weak convergence. No uniform integrability, conservation-of-expectation, or density-continuity assumption is used.
* First nonproduct test: covariance is exactly 1/36, whereas every specified equilibrium is a product law. Exact Fraction arithmetic passed.
* Second critical-target test: the critical empty-site probability is below 1/3, but the evolving probability is at least 1/2 at every time. This proof requires no limiting-process existence theorem.
* Stronger iid actual-limit test: after relabelling each parity, the verified published nearest-neighbor theorem applies with density 10 and critical density 4. Continuous embeddings and a finite mixture give the actual limit. Its covariance at sites 0 and 2 is c^2/(4 alpha_0 alpha_2)>0, so no product equilibrium is possible. This part uses a cited theorem; the elementary critical-target contradiction does not depend on it.
* Literature status: Theorem 2.5 of the 2020 paper is unscaled convergence but explicitly one-dimensional nearest-neighbor. It cannot be labeled a printed theorem for the full 1999 question. The earlier repository report narrowed the source scope without justification. API rate limits also prevent any exhaustive negative claim about the literature.

## Formal verification scope

ParityChecks.lean has no sorry, axiom, or native_decide. It imports only Ring, NormNum and Linarith tactic modules and proves finite rational identities/inequalities. Its command was submitted from ~/lean_verify; the shared-machine slot queue and result are recorded in LEAN_CHECK.md. No infinite-volume theorem is called Lean-verified.

## Audit conclusion

The two explicit counterexamples survive the audit for the literal non-irreducible scope. The nearest-neighbor positive specialization is verified by reduction to a published theorem. The arbitrary connected-kernel problem is not settled by these arguments. All outcome labels must retain that distinction.
