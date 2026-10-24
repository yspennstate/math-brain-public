C0072: wired boundary limit from summable arms
Label: proof under explicit percolation tail hypotheses; conditional application to the source model. Blind audit pending. Bulk and zero boundary conditions are not settled here.

Let d >= 2 and let bond states on nearest-neighbor Z^d be independent with a fixed common parameter p. Assume
P(0 is connected to a vertex at l_infinity distance at least r) <= K/(r+1)^gamma
for every integer r >= 1, with gamma > 1. For B_n={0,...,n-1}^d define W_n as the vertices connected to its vertex boundary by open edges within B_n. Wired boundary means identifying all boundary vertices, without changing the Bernoulli law of the internal edges; W_n is the boundary component counted in original vertices.

Let H={x in Z^d:x_1>=0}, and q_r=P((r,0,...,0) connects to {x_1=0} by an open path contained in H). In particular q_0=1 and q_r <= K/(r+1)^gamma for r>=1. Then
|W_n|/n^(d-1) -> a_w = 2d sum_(r=0)^infinity q_r
in L1, and hence in probability. This needs a summable arm bound; it does not need a sharp arm asymptotic or a limit for r^gamma times the arm probability.

Proof. For a cutoff R, vertices farther than R from the boundary contribute in expectation at most
2d K n^(d-1) sum_(r>R)(r+1)^(-gamma).
Indeed each layer has at most 2d n^(d-1) vertices; a vertex in layer r connected to the boundary has a full-space arm of length at least r. This tail tends uniformly to zero after division by n^(d-1).

Fix R and truncate connection tests to l_infinity radius L>R. A vertex at distance r<=R from one face, and at least L+R from all the other faces, sees exactly a translated half-space inside its radius-L neighborhood. The indicator that it reaches that face inside this neighborhood depends on finitely many Bernoulli edges and has mean q_(r,L). Two such indicators are independent when their neighborhoods do not share edges. Its normalized spatial average over a face converges in L2, and therefore L1, to q_(r,L): for fixed L, its variance is bounded by a constant depending on L times n^(-(d-1)).

The actual W_n indicator dominates this local test. If the actual indicator is 1 and the local test is 0, any path witnessing the former must leave the radius-L neighborhood: all nearby boundary points lie on this one face. That discrepancy has expectation at most K/(L+1)^gamma. Face edges and corners omitted from the averages contain O_(R,L)(n^(d-2)) vertices, negligible after normalization. Moreover q_(r,L) increases to q_r as L tends to infinity, since any finite path lies in some finite neighborhood. Summing the fixed finitely many face/layer averages proves that the boundary layers up to R have normalized L1 limit 2d sum_(r=0)^R q_r, after taking n to infinity and then L to infinity. Taking R to infinity and using the uniform tail bound completes the proof.

To identify W_n with the largest wired component asymptotically, add the explicit full-space cluster-size assumption P(|C(0)|>=k)<=K_2 k^(-1/2) and assume d>3. Any other component with at least k vertices accounts for at least k distinct vertices whose full-space clusters have size >=k. Hence
P(a nonboundary component has size >=k) <= K_2 n^d k^(-3/2).
For k=epsilon n^(d-1), this bound is K_2 epsilon^(-3/2) n^((3-d)/2), which tends to zero. Thus |C_max^(wired)|/n^(d-1) has the same limit a_w. This argument applies to the largest component under the stated two tail assumptions and the stated definition of wiring; it is not an unconditional claim for every nearest-neighbor d>6 model.

The old C0072 attempt says the wired constant needs sharp one-arm asymptotics. This proof removes that proposed requirement for this precisely defined model. The actual constant is a summable half-space connection series, not an equality between a random cluster size and a full-space probability sum. Its exact numeric value is not evaluated here.

Critical checks: independence and finite-range dependence of truncated tests; the boundary wiring convention; the summability exponent gamma>1; corner errors of order n^(d-2); order of the cutoffs n, then L, then R; and the extra cluster-size tail needed to pass from the boundary component to the largest component.
