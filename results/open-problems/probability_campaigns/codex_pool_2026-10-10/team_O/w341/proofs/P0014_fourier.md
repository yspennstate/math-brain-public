# P0014: Fourier calibration and exact small expectations

Status: a rederivation of a known computational reduction, exact small cases and numerical evidence, pending w347. The cached *Randomstrasse101: Open Problems of 2025*, Entry 9, Conjecture 18, lines 749-810, poses E theta=(1+o(1))sqrt(n). It already describes the Fourier LP and cites the partial-bound paper Bandeira, Blasiok, Dmitriev, Faure, Kireeva and Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227 (2025), at lines 1393-1397. Its quoted upper bound is O(sqrt(n) log log n), not a solution of the asymptotic conjecture. This packet does not claim the LP reduction as new.

For a simple undirected circulant graph on Z/nZ with nonzero generator set S=-S, theta is the SDP maximum <J,X> over real symmetric positive semidefinite X with trace one and X_ij=0 at graph edges. Average X over cyclic shifts; this preserves feasibility and objective and makes X circulant. Fourier diagonalization gives nonnegative eigenvalues y_j summing to one, with y_j=y_{n-j}. Its edge constraint is sum_j y_j cos(2*pi*j*s/n)=0 for each s in S, and its objective is n*y_0.

Equivalently let m=floor(n/2) and aggregate z_j=y_j+y_{n-j} for paired frequencies, leaving z_0=y_0 and the self-inverse frequency unpaired when n is even. Then

theta(G)=n*max z_0, subject to z_j>=0, sum_{j=0}^m z_j=1, and sum_{j=0}^m z_j cos(2*pi*j*s/n)=0 for each unordered generator representative s.

Conversely any such z, split equally over paired frequencies, reconstructs a real positive semidefinite circulant X, proving equality of the LP and SDP. The even self-inverse generator and frequency require no extra factor of two after aggregation.

For independent fair inclusion of each unordered nonzero generator pair, exact small expectations are 3/2 at n=2, 2 at n=3, 9/4 at n=4, and (3+sqrt(5))/2 at n=5. At n=4 the four graphs are empty, a four-cycle, a perfect matching, and complete, with theta 4,2,2,1. At n=5 they are empty, two five-cycles and complete. The five-cycle LP has cosines (sqrt(5)-1)/4 and -(sqrt(5)+1)/4, maximized by putting nonconstant mass on the latter; z_0=1/sqrt(5), so theta=sqrt(5).

The earlier complement-identity reduction is still necessary: theta(G)theta(complement G)=n for vertex-transitive G, and the fair model is complement invariant. With Z=log(theta(G)/sqrt(n)), E theta/sqrt(n)=E cosh Z. Hence the desired result implies E Z^2->0, because cosh Z>=1+Z^2/2. Convergence in probability alone is insufficient without exponential-tail control. A sufficient stronger route would be an MGF bound E exp(tZ)<=exp(t^2*sigma_n^2/2) at t=1 with sigma_n->0; it would sandwich the expectation ratio between one and exp(sigma_n^2/2). That bound is not established here.

The implemented LP enumerated all 60 graphs for n=2,...,9 in double precision. Maximum constraint residual was 1.12e-15 and maximum complement-product discrepancy 8.89e-15. These are numerical checks, not exact certificates or evidence of a large-n limit. Audit the theta convention, cyclic averaging, normalization, pairing at even n, exact small cases and tail gap.
