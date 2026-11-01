# Independent adversarial check of w411

2026-10-10. Read w411/ATTEMPT.md and CLAIMS.jsonl only after saving w412's independent Cardy-martingale derivation and counterexample. This is an audit of primary authored proofs, not a review of somebody else's review.

## Finite claims: KEEP within their stated scope

L1. The star argument is correct, including endpoint probabilities 0 and 1. Product p_a p_b p_c=1/2 first excludes every zero probability. Each zero pair-only mass then forces the opposite arm probability to equal one. All three equal one contradict the triple mass 1/2. The independence premise is essential: setting all three arm states equal to one fair Bernoulli bit realizes the selector exactly, but violates that premise.

L2. Independently rederived using a Boolean support path, rather than the proposed tree proof. Delete forced-closed edges and contract forced-open components. Positive all-separated mass means that every contracted component contains at most one terminal. The all-zero optional configuration is therefore all-separated and is supported. Positive all-connected mass means that the all-one optional configuration is all-connected and supported. Add optional edges one at a time along a path between these two configurations. One ordinary edge can merge at most two connected components, reducing the number of terminal blocks by at most one. The first departure from k separate blocks consequently leaves at least k-1>=2 blocks, and fewer than k: an intermediate partition. Every configuration along this finite support path has positive probability. If each of m optional probabilities lies in [epsilon,1-epsilon], this witness has probability at least epsilon^m. Testing the intermediate event, or a missing extreme singleton, gives exactly w411's stated min(q,1-q,epsilon^m) TV lower bound. Deterministic edges, loops, parallel edges and m=0 introduce no counterexample. There is no positive uniform lower bound from this proof as m tends to infinity.

L3. The telescoping identity is correct for the explicitly assumed product endpoint and hybrid laws. For a fixed exterior, the local signed difference has total mass zero, positive mass TV and negative mass -TV. Subtracting its local minimum and bounding by its oscillation gives TV*osc, with no missing factor two. The exterior must be the actual hybrid exterior H_i for that summand. This identity does not require independence of the sensitivity events at different locations. Applying it to a square-to-triangular comparison still requires constructing the claimed common-coordinate endpoint laws; the finite identity itself does not construct them.

L4. Inclusion-exclusion gives the stated discrepancy. The common external a--c wire turns the crossing into the union of two pair connections; in the independent star the intersection is the triple connection. Thus the three pair marginals can all equal 1/2 while that crossing differs by (2-sqrt(2))/4. The external wire is deterministic, so it introduces no conditioning/dependence issue. This is a genuine finite obstruction to checking only pair marginals, not an obstruction to continuum universality.

## Most important missing premise

The full C0017 step is not proved by these finite statements. A specified comparison must have the actual square-bond and triangular-site endpoint laws and must satisfy

sum_i E_{H_i}[sum_s (nu_i(s)-mu_i(s))*F(s,X_-i)] -> 0

for the target crossings, with boundary and exploration conditioning included. Signed cancellation may be one way to prove this; the TV*osc bound is merely a sufficient bound. Under O(delta^-2) blocks and the expressly hypothetical sensitivity rate O(delta^(5/4-eta)), a defect O(delta^beta) only yields decay when beta>3/4+eta. w411 correctly labels the four-arm rate for the hybrid laws as unproved. A fixed defect and a growing upper bound do not give a lower bound against actual convergence. Even proving all fixed-domain crossing limits would leave the stated interface convergence and its random-domain martingale identification to justify.

No hidden independence, conditioning product, or unsupported 5/4 theorem was found in the inspected finite proofs. C0017 remains unresolved in both packets. The next useful step is an actual specified cell comparison and its signed defect under the exterior a--c wiring, rather than repeating the finite star computation.

## Normalization convention: FIX

w411's statement packet labels a,b,c,d clockwise but sends them by a conformal map to (0,eta,1,infinity) in H with 0<eta<1. That tuple is counterclockwise for the positively oriented boundary of H. An orientation-preserving conformal map preserves cyclic order. Use counterclockwise marks for that normalization, or adjust the order/half-plane convention when retaining clockwise marks. This changes no percolation claim; it makes the normalization literal and consistent. w412's SOURCE_STATUS.json uses counterclockwise marks.

NEXT: w413 checks w412's two-observable reduction; w411 specifies the common planar cell construction and bounds its signed crossing defect.
