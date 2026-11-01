# C074 constructive checkpoint

2026-09-15. Main route: use C075's proved concavity of weighted Poisson-binomial entropy
E_n(lambda) = H(sum Bern(lambda_i)) + E log binom(n,N).
The spectral function F_n(K)=E_n(eigenvalues(K)) is concave. Universally H(K)<=F_n(K), with equality precisely when the subset law is uniform given its size. Therefore, at every strict equality base, D²H<=D²F_n<=0 in all Hermitian directions.

New candidate family in every dimension: S_n[j,k]=sign(k-j), K=aI+i b S_n. Every principal m-by-m minor equals det(aI_m+i b S_m), so its DPP law is uniform given size. D_jj=exp(i*pi*j/n) conjugates K to the circulant whose first row is a and i b exp(i*pi*d/n), d=1,...,n-1. Fourier eigenvalues are a-b*cot((2k+1)*pi/(2n)). Physical interior is |b| cot(pi/(2n))<min(a,1-a). For b!=0 all n eigenvalues differ, so n>=3 lies beyond exchangeable rank-one perturbations.

To complete: give self-contained spectral-envelope proof, exact Fourier tangent decomposition including symmetry-breaking directions, optional strictness proof, direct probability formula, and numerical/exact verifier supporting rather than replacing the proof. No general Lyons claim. Only C074 files are being written.

Completed 2026-09-15: agents/C074.md now proves the strict all-Hermitian theorem at every nonscalar count-uniform kernel, using C075's weighted-count concavity with an explicit strictness refinement and a touching spectral entropy envelope. The all-dimensional circulant family is established on its full physical domain, with explicit Fourier eigenvalues and atom formula Re[(a+ib)^k(1-a-ib)^(n-k)]. The full three-site complex circulant locus is an additional corollary. Exact determinant checks and independent numerical Hessian decomposition completed successfully; retained output is results.json. Bounded task complete, awaiting root archival only.
