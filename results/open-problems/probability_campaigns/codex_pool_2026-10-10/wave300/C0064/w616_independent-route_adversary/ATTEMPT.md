# C0064 independent route: cluster coloring and spectral comparison

Author: w616. Date: 2026-10-10. This derivation was saved before opening any proposed proof by w615. Requested model settings are not served-model evidence; actual served identity is unavailable to this worker.

Target: independent nearest-neighbour Bernoulli bond percolation on Z^d. Put tau_p(x)=P_p(0 connected to x), Dhat(k)=d^{-1} sum_j cos(k_j). Seek a finite A(d) independent of p<pc such that tauhat_p(k)<=A(d)/(1-Dhat(k)) for k nonzero, for d=7,8,9,10. The established cited theorem covers d>=11. Critical Fourier conventions and current source status are recorded separately.

Method chosen: represent connectivity as the covariance of independent fair signs assigned to open clusters, then investigate a transfer of a nearest-neighbour Ising Gaussian bound. This uses a spin covariance comparison rather than a lace-expansion coefficient computation. Its strongest tempting step is a comparison of covariance operators; a pointwise comparison of two-point functions is insufficient.

## Direct covariance identity

On any finite graph, first sample Bernoulli(p) edges. Assign each open cluster an independent fair sign, and give every vertex the sign of its cluster. Conditional on the edges, E[sigma_u sigma_v]=1 when u and v are connected, and 0 otherwise. Thus E[sigma_u sigma_v]=P_p(u connected to v). In particular, this connectivity matrix is positive semidefinite. This fact supplies positivity, but does not identify the spin marginal with a local Ising Gibbs measure.

## An exact four-cycle obstruction

Use the cycle with vertices 0,1,2,3 and four edges i--(i+1 mod 4), with no other edges and free boundary conditions. Throughout 0<p<1. Let W(sigma) be the probability of a particular spin configuration after fair cluster coloring. Write r for its number of equal-spin edges. Any proper edge subset is a forest, so with m open edges its number of components is 4-m. Therefore when r<4,

W(sigma)=2^{-4}(1-p)^{4-r}(1+p)^r.

For an all-equal spin configuration, the full four-edge cycle has one component, rather than the zero components that the forest formula would give. Consequently

W_same=(1+p)^4/16-p^4/2,
W_mid=(1-p^2)^2/16,
W_alternating=(1-p)^4/16.

Every other configuration on a cycle has r=2, hence weight W_mid. For any homogeneous zero-field nearest-neighbour Ising measure on this cycle, the corresponding weights must satisfy W_same W_alternating=W_mid^2, because the three edge spin sums are 4,-4,0. Here instead

W_same W_alternating-W_mid^2=-p^4(1-p)^4/32<0.

The rotation-invariant cluster-color law therefore is not the homogeneous nearest-neighbour Ising law. This is a finite-graph statement, not a claim that reflection positivity itself fails.

## Even pointwise Ising domination reverses at an alternating mode

Let t=tanh(J)=p in the zero-field ferromagnetic Ising measure on this same cycle. Expanding each factor exp(J sigma_i sigma_j)=cosh(J)(1+p sigma_i sigma_j) shows the partition polynomial is 1+p^4. Only even-degree edge subsets survive the spin sum. The two-point numerators are the two arcs connecting each pair. Hence

G_Ising(adjacent)=(p+p^3)/(1+p^4),
G_Ising(opposite)=2p^2/(1+p^4).

Bernoulli connectivity is the union of the events that each of the two edge-disjoint arcs is open:

tau(adjacent)=p+p^3-p^4,
tau(opposite)=2p^2-p^4.

For both distances, G_Ising>=tau: the differences are respectively p^4(1-p-p^3+p^4)/(1+p^4) and p^4(1-p^2)^2/(1+p^4), strictly positive for 0<p<1. The first numerator factors as p^4(1-p)(1-p^3).

For the alternating vector v=(1,-1,1,-1), the covariance matrices are circulant, with eigenvalues

lambda_perc=1-2tau(adjacent)+tau(opposite)=(1-p)^2(1+p^2),
lambda_Ising=1-2G_Ising(adjacent)+G_Ising(opposite)=lambda_perc/(1+p^4).

Thus lambda_perc>lambda_Ising for every 0<p<1, despite domination at every entry and positive semidefiniteness of both matrices. At p=1/2 the two eigenvalues are 5/16 and 5/17. Their ratio is 17/16; their difference is 5/272. Normalized mode variances equal these eigenvalues. This is a concrete counterexample to the inference that entrywise correlation domination gives Fourier-mode domination, even for these percolation and Ising covariances.

## Hardest missing piece and allowable conclusion

To transfer an Ising infrared bound to Bernoulli connectivity one needs a valid domination of the relevant Fourier-mode variances (or a direct Gaussian domination result for the cluster-color measure), uniform in the near-critical percolation parameter. Positive definiteness, FKG, and pointwise domination do not supply it. The cycle disproves the universal comparison inference. It does not disprove C0064, establish a lattice-specific comparison failure, or rule out a different Gaussian argument.

The 2026 Markovian-renormalisation paper offers a different conditional certification route. Its Theorem 1.1 requires an all-space Gaussian bound at a particular subcritical p0 together with sufficiently large susceptibility. Neither its title nor semi-decidability supplies a certificate in d=7..10. Its exact hypotheses will be retained as a source row.

NEXT: Verify these cycle identities by exact edge and spin enumeration under a fresh small-compute gate, then request w617's independent mathematical check and inspect w615's proof.
