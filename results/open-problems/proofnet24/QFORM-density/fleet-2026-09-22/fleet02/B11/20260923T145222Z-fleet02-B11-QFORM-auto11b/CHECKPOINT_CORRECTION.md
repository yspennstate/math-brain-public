# Checkpoint correction — remove the redundant global-diffuse hypothesis

The first checkpoint's condition `max_i ||r_i||^2 <= tau^3/165888` is mathematically sufficient for its cross-cut calculation, but it is NOT useful new coverage: for exact rank three it implies `max_i ||r_i||^2<1/2`, so the already-completed Fresnel--Brascamp--Lieb Theorem F pays the form directly. I therefore do not count that checkpoint statement as new progress.

The corrected compiler is asymmetric and permits arbitrarily heavy rows on the unconstrained side of the decoupling cut.

Let the four nearest-null-line projected clusters from the preceding null-ruling lemma have bank parameters `b=rho` for the two S clusters and `b=1-rho` for the two T clusters, and let `tau=min(rho,1-rho)`. Put

`gamma=tau^3/9216`, `h0=gamma/2=tau^3/18432`.

Assume the covariance projection error satisfies

`eta_S+eta_T <= tau^3/9216`,

and, in EACH of the four projected line clusters, the projected squared mass carried by rows with ACTUAL spectral leverage `||r_i||^2<=h0` is at least `b/48`.

For each cluster choose only light rows, greedily, until projected mass first reaches `b/96`. Since every chosen projected weight is at most `h0<=b/96`, its I-mass lies in `[b/96,b/48]`; put every other original coordinate, including every heavy row, in J. Because the full projected cluster mass is at least `b/12`, J retains at least `b/16` on each line.

Projected Gram lower bounds:

- on I, the S-plane minimum eigenvalue is at least `rho^2/3456` and the T-plane one at least `(1-rho)^2/3456`;
- on J, the corresponding bounds are at least `rho^3/4608` and `(1-rho)^3/4608`.

Hence BOTH full three-dimensional projected Grams are at least `tau^3/4608 I_3`. Subtracting the actual/projection covariance error gives

`G_I,G_J >= gamma I_3`, `gamma=tau^3/9216`.

Every I-row leverage is therefore at most `h0/gamma=1/2`, while J is allowed arbitrary heavy rows. For the ACTUAL cross block `C=A[I,J]=R_I M R_J^T`,

`Z=e_3(C^T C)=det(M)^2 det(G_I)det(G_J)>=s^6 gamma^6`,

so the pinned completed Theorem D gives

`||p_Q||_infinity <= 6 sqrt(e)/(s gamma)=55296 sqrt(e)/(s tau^3)`.

This branch is genuinely outside Theorem F: a row of leverage `>1/2` may sit in J. The remaining failure is now explicit. If a cluster has less than `b/48` light projected mass, its heavy rows carry at least `b/16>=tau/16` projected mass. Since each heavy row has leverage `>h0` and total frame leverage is 3, the complete heavy set has cardinality `<3/h0=55296/tau^3`. Thus failure of the new cross-cut compiler collapses to a finite heavy-spike null-ruling branch rather than a diffuse product-provenance problem.
