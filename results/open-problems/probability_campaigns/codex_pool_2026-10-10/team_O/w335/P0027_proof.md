# P0027: smooth deterministic maps are rigid

Label: proof for a regular deterministic-map class, pending w347. It does not turn every arbitrary shy coupling into a deterministic one, nor classify measurable nonsmooth maps.

Let D be a bounded connected C^2 domain in R^d and F:D->D a C^2 diffeomorphism. Suppose for every starting point x in D, normal reflected Brownian motion X started at x has Y_t=F(X_t) with the reflected-Brownian law started at F(x), using the usual identity Brownian covariance in the interior. Then F(x)=Qx+b for a fixed orthogonal Q and vector b.

Proof. At an interior starting point the small-time covariance of F(X_t)-F(x), divided by t, tends to DF(x)*DF(x)^T by Ito's formula (reflection has no first-order effect before the boundary is hit). The corresponding limit for a reflected Brownian motion started at the interior point F(x) is the identity. Thus DF*DF^T=I at every x. Since DF is square, it is orthogonal, so its columns e_i=partial_i F form an orthonormal basis.

Set A_ijk=<partial_i partial_j F,e_k>. Equality of mixed partials gives A_ijk=A_jik. Differentiating <e_j,e_k>=delta_jk gives A_ijk=-A_ikj. Combining the two symmetries,

    A_ijk = A_jik = -A_jki = -A_kji
           = A_kij = A_ikj = -A_ijk,

so every A_ijk is zero. The e_k span R^d, hence every second derivative of F is zero. On a connected open domain this makes DF a fixed orthogonal matrix Q and F-Qx a constant b. This establishes rigidity under the stated regularity and all-starting-points assumptions.

For an isometry F preserving D, normal reflection is equivariant: Q sends Brownian noise to Brownian noise and the inward normal at x to the inward normal at F(x). Thus F(X) has the reflected law. Suppose also that X visits every nonempty interior open set infinitely often almost surely, as normal reflected Brownian motion does in a bounded smooth connected domain. Then the deterministic isometry coupling is shy exactly when

    min_{x in closure D} |x-F(x)| > 0.

If the minimum is positive the distance stays uniformly positive. If it is zero, for every epsilon>0 the set {x in D: |x-F(x)|<epsilon} is nonempty and open by continuity and density of D in its closure. Recurrence forces visits to it. Applying this to epsilon=1/k shows inf_t |X_t-F(X_t)|=0 almost surely, ruling out shyness.

If D is convex, its volume centroid c lies in D. Any preserving Euclidean isometry fixes c: change variables in its centroid integral to obtain Qc+b=c. Therefore this regular deterministic class has no shy coupling on a bounded convex smooth domain. This is not a claim about all nondeterministic couplings on such a domain.

On the annulus R<|x|<R_out in R^2, 0<R<R_out, rotation by theta has minimum displacement 2R*|sin(theta/2)|. Every nontrivial rotation modulo 2*pi is therefore a deterministic shy coupling. The prior antipodal example is theta=pi. Letting R=0 or theta=0 removes the positive-gap check.

Checks: the tensor symmetry/skew-symmetry linear constraints force zero in small dimensions; boundary normal equivariance; domain preservation; disk versus annulus fixed points; strict regularity and recurrence limits. No measurable-map classification or full P0027 solution is claimed.
