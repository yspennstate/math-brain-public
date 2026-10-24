# Statement only: P0104 martingale supplement

w369, 2026-10-10. Independent adversary w370: statements below precede the proof-packet handoff. Please test the generic constants and the exposure-filtration criterion. No lattice estimate is claimed.

For every finite real martingale (M_k,F_k), k=0,...,N, with M_0=0 and M_N in L^4, let D_k=M_k-M_{k-1} and Q_N=sum_{k=1}^N D_k^2. Then E M_N^4<=81 E Q_N^2 and E Q_N^2<=81 E M_N^4. Also sum E[M_{k-1}^2D_k^2]<=16 E Q_N^2, sum |E[M_{k-1}D_k^3]|<=4 E Q_N^2, and sum E D_k^4<=E Q_N^2. No independence or conditional symmetry of the differences is assumed.

For iid Exp(1) edge weights on undirected nearest-neighbor Z^2, let T_n be the passage time from (0,0) to (n,0), n>=1, and sigma_n^2=Var(T_n)>0. Enumerate all edges, let F_k be the first-k-edge sigma-field with trivial F_0, M_{n,k}=E[T_n|F_k]-E T_n, D_{n,k}=M_{n,k}-M_{n,k-1}, and Q_{n,k}=sum_{j<=k} D_{n,j}^2. Uniform boundedness of E|T_n-E T_n|^4/sigma_n^4 is equivalent up to factor 81 to uniform boundedness of E Q_{n,k}^2/sigma_n^4 over n,k. If V_{n,k}=sum_{j<=k} E[D_{n,j}^2|F_{j-1}] satisfies E V_{n,k}^2<=a sigma_n^4 and sum_{j<=k} E D_{n,j}^4<=b sigma_n^4 uniformly for finite a,b>=0, then E|T_n-E T_n|^4<=81(sqrt(a)+sqrt(b))^2 sigma_n^4. These lattice estimates are hypotheses, not established facts.

Hardest gap: establish sup_{n,k} E Q_{n,k}^2/Var(T_n)^2<infinity for the actual lattice model. Nondegenerate n^(1/3) scaling remains a separate missing input.
