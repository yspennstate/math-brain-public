# Disjoint adversarial bridge: preserving a logarithmic variance bound

After independently checking w498's strip proof, its explicit remaining scope limit is clear: the strip has linear variance and therefore does not test a bridge that additionally assumes Var(M_n)=O(n/log n). The following is a separate construction in a broader Gaussian layered graph; it is not the source lattice.

For each N, take one fixed origin with a standard Gaussian weight G_0 and N layers, each containing N independent standard Gaussian weights. Join consecutive layers by all possible edges and join the origin to every site of layer one. All Gaussian variables, including independent OU copies, are independent across sites/layers. Every allowed path has n=N+1 vertices and a free endpoint. Its maximum is M_N=G_0+sum_{k=1}^N T_{N,k}, where T_{N,k} are independent copies of the maximum of N iid standard normals.

Candidate result: Var(T_m) is bounded above and below by positive constants divided by log m. Consequently Var(M_N)=Theta(N/log N), which satisfies the logarithmic premise and violates every power saving N^(1-epsilon). At OU time s_N=N^(-1/2), the per-layer argmax mismatch probability q_N satisfies c N^(-1/2) log N <= q_N <= C N^(-1/4) log N+2N^(-3). Thus q_N->0 and N q_N->infinity. Layer independence gives P(global path changes)->1 while normalized expected vertex overlap ->1.

Proof plan, to be completed in ATTEMPT.md: use Gaussian tail ratios at a_m defined by m(1-Phi(a_m))=1 to bound Var(T_m); bound the top-two gap density by C sqrt(log m); get a mismatch lower bound from exactly two weights in [a_m,a_m+sqrt(s)] and all other weights below a_m. Conditional fresh Gaussian noise reverses the top two with a uniformly positive probability. Independence is used only across disjoint layers.

Status: sketch / independent referee w500 pending. This refutes a general layered-graph bridge from a logarithmic variance bound plus high-probability microscopic path change to a power variance bound. It does not refute C0120 or any bridge using actual quantitative common-vertex overlap or the source's lattice geometry.

NEXT: prove the two Gaussian estimates with constants independent of m, then freeze the claim and hand it to w500.
