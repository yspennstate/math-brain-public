# Adversarial verdict on w552's C0047 packet

2026-10-10. Auditor: w553. Input: ../w552/ATTEMPT.md (first read after independent w553 ATTEMPT.md was saved). Artifact hash is to be recorded in the final review receipt. This is a mathematical audit of the proof, not a review of another audit.

Verdict: KEEP L1, L2, and L3 as conditional reductions with their stated assumptions. DO NOT promote the parent conjecture: the proposed input M_c(G)<infinity remains unproved. The author correctly labels that input as stronger than C0047 and does not assert a resolution.

L1: A connected finite exhaustion captures every finite witnessing path. Finite percolation kernels are positive semidefinite by the cluster-square formula. The nonnegative-entry bound extends from nonnegative vectors to arbitrary finitely supported vectors using absolute values; polarization then gives the bounded operator. Conversely, entrywise domination plus positivity bounds every finite compression. The finite-volume supremum is the full norm, including the value infinity. Boundary conditions must be FREE throughout; a wired kernel is not the same object.

L2: The pivotal event is evaluated on the product law with the tested edge removed. Its two possible endpoint orientations have edge-disjoint connection witnesses, so BK supplies the product bound. Independence of those connection events is not needed or asserted. Russo's formula has no extra 1/(1-p) factor in this finite pivotal-probability formulation. For 0<p<1 and connected finite F, positivity gives a simple Perron eigenvalue. The entrywise derivative estimate is used only with its nonnegative eigenvector; it is not a Loewner-order claim. Differentiation gives m_F'<=alpha m_F^2, so integration yields the stated reciprocal estimate. A singleton F has constant kernel 1 and requires no differentiation argument.

L3: eta=min((1-pc)/2,1/(2 alpha M)) is strictly positive under pc<1, M<infinity, alpha>0. Every finite norm is <=2M at pc+eta, uniformly in F. L1 and entrywise monotonicity preserve full boundedness at every q in [pc,pc+eta]. If there were almost-sure uniqueness at any such q, countability and transitivity give theta(q)>0; FKG then forces every entry >=theta(q)^2 and an unbounded quadratic form on larger finite supports. Below pc there is no infinite cluster. Thus the entire defining uniqueness set avoids [0,pc+eta], giving pu>=pc+eta. This checks the required interval quantifier without assuming uniqueness is monotone.

The minimal unproved input is a volume-uniform critical norm bound for every prescribed nonamenable Cayley graph. The known spectral inequality alpha<degree does not imply pc alpha<1. For the Cayley graph of the free group on two generators, degree=4, pc=1/3 and alpha=2sqrt(3), so pc alpha=2sqrt(3)/3>1. The walk-resolvent regime therefore fails even on a graph where pc<pu is elementary. This refutes the attempted use of nonamenability to discharge that particular intermediate premise, not C0047.

An additional independent guard is in w553 CLAIMS.jsonl O01: p^distance exponential decay on that tree has a divergent squared row sum whenever 3p^2>=1. Any later attempt to turn unspecified exponential decay into the missing uniform norm must supply the additional summability/operator estimate.

Formal status: no Lean build or axiom-checked receipt is claimed. Requested model settings are not response-side served-model evidence; author and auditor served identity remain unverified. This scoped mathematical KEEP does not pass a different-model identity gate by itself.

NEXT: w554 independently checks L01/O01 and the scoped L1-L3 verdict; the next proof task must supply or refute the uniform M_c input, not repeat the reduction.
