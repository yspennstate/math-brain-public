# P0342: Three fluctuation regimes for the earlier retained-root perturbation

Label: proof; author checked only. Independent audit: PENDING w347.

Assume finite binary trees retain an identifiable original degree-two root after leaf rerooting, and their ordered root split law is q_n(i)=n/(2 H_(n-1) i(n-i)), 1<=i<n. Let B_n indicate min(i,n-i)<=floor(sqrt(n)), let p_n=E B_n, and give every leaf the same score f_a=n^(-a)(B_n-p_n), with score zero on infinite trees and a>0. The finite centered score sum divided by sqrt(n) is n^(1/2-a)(B_n-p_n). It is not tight for 0<a<1/2, converges to a two-point law at a=1/2, and tends uniformly to zero for a>1/2. Every infinite-tree score is zero.

Assumptions: The original degree-two root is retained and identifiable; The displayed critical root-split law; The local topology and score domain retain that root; a>0

For n>=9 put k=floor(sqrt(n))<n/2. Since q_n(i)=(1/i+1/(n-i))/(2 H_(n-1)), symmetry gives p_n=(H_k+H_(n-1)-H_(n-k-1))/H_(n-1). The first numerator term is (1/2) log n+O(1), and the other difference is at most k/(n-k)=O(n^(-1/2)); H_(n-1)=log n+O(1). Thus p_n ->1/2. Both possible values of B_n-p_n have absolute value approaching 1/2. Multiplication by n^(1/2-a) gives the three stated regimes. The scores have expectation zero exactly. On bounded-degree trees with the retained-root topology, every finite tree is isolated locally, while convergence to an infinite tree forces the leaf count to diverge. Therefore |f_a|<=n^(-a) proves continuity at infinite trees. This generalizes the earlier a=1/4 obstruction; it does not verify the retained-root assumption in the original problem's precise topology.

Limits: This is a conditional topology-specific obstruction with a degenerate infinite CLT. It is not a checked solution of Open Problem 12. A concrete nondegenerate beta-splitting counterexample remains open in this packet.

Existing card: math:probability.core:open-problem-p0342-transferring-a-stationary-fringe-process-clt-to-finite-beta-splitting
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:3238
