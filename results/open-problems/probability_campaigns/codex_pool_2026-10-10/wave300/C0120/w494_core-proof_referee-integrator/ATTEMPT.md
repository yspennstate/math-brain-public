# C0120 referee and independent lemma attempt, 2026-10-10

## Exact target and gate

For iid standard Gaussian site weights on the nonnegative quadrant, let P_n range over n-vertex up/right paths from the origin with unrestricted endpoint and put M_n=max_{p in P_n} sum_{v in p}g_v. Chatterjee's [Section 8, Theorem 8.1](https://arxiv.org/pdf/0810.4221v2) proves Var(M_n)<=C n/log n; Section 12(3) asks to improve the fluctuation exponent. A concrete interpretation is Var(M_n)<=C_e n^(1-e) for some e>0. This is the exact model behind the source prompt; the exponent quantification is ours. Present openness UNKNOWN.

## Independent load-bearing rederivation

The finite set of path incidence vectors is distinct, so every pair's Gaussian path-weight difference is nondegenerate. The maximizer is unique almost surely. The maximum of these linear forms is sqrt(n)-Lipschitz, weakly differentiable, and its gradient at a configuration with unique maximizer is the indicator vector of that path. Thus its squared gradient norm equals n.

Expand its centered value in normalized product Hermites: M_n-E M_n=sum_{k>=1}F_k and a_k=E F_k^2. Gaussian integration by parts and Parseval for weak derivatives give sum_{k>=1}k a_k=n and Var(M_n)=sum_{k>=1}a_k. Mehler's formula for the OU coupling g^t=e^(-t)g+sqrt(1-e^(-2t))g' gives E|P(g) intersect P(g^t)|=sum_{k>=1}k a_k e^{-(k-1)t}. Integration against e^{-t} yields the exact variance-overlap identity. These are finite-dimensional Sobolev identities, not a conditional independence argument.

At K>=1, splitting the variance series shows Var(M_n)<=D_n(K)+n/(K+1), where D_n(K)=sum_{k<=K}k a_k. Also D_n(K)<=K Var(M_n). Therefore a uniform D_n(floor n^a)<=C n^(1-b), a,b>0, would prove a variance gain with exponent min(a,b). This is the hardest missing lemma G1 in w492's packet. It remains UNPROVED.

## New small lemma: exact first-chaos floor

Gaussian integration by parts gives the coefficient of g_v in the first chaos of M_n as E[M_n g_v]=E[partial_v M_n]=P(v in P(g))=:p_v. Hence D_n(1)=sum_v p_v^2. Each path visits exactly one vertex in time layer L_i={(x,y):x+y=i}, which has i+1 vertices, so sum_{v in L_i}p_v=1 and Cauchy-Schwarz gives sum_{v in L_i}p_v^2>=1/(i+1). Consequently D_n(1)>=H_n=sum_{j=1}^n 1/j. Mehler's series also gives lim_{t->infinity}E|P(g) intersect P(g^t)|=D_n(1). This ties w492's spectral formula to w493's overlap floor. It is an author proof pending independent w497 review, not a new variance upper bound.

## Attempt at G1 and obstruction

The existing Var(M_n)<=C n/log n gives only D_n(K)<=C K n/log n. For K=floor n^a with a>0, this eventually exceeds the trivial D_n(K)<=n, so it cannot yield G1. The first-chaos floor H_n is compatible with G1 for b<1, so it neither proves nor refutes G1. Bounding individual vertex marginals likewise cannot force G1: w492's parallel-corridor Gaussian graph has nonroot marginals 1/n but variance of order n/log n. That graph is not the quadrant lattice. The needed input must use the lattice's path competition across scales to establish polynomial spectral escape or an equivalent polynomial-time overlap bound. No such input is proved here.

## Prior stored attempt audit

C0120-A001 in the dated intake discusses Var(log Z_n) in general dimension and imports the FPP exponent relation as a proof route. The cited Chatterjee Section 8 theorem is about M_n in 1+1 dimensions, and the quoted FPP theorem does not itself prove a directed-polymer scaling relation. The stored attempt should be marked as a mismatched-scope sketch, with its proposed transfer requiring a separate proof. It must not be promoted as a reduction for this exact target.

NEXT: Obtain w497's independent check of the first-chaos lemma; keep G1 explicitly open and send the scoped corrections to integration.
