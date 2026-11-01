# Can the three-site Schur optimizer be assumed semidefinite?

Coordinator method probe, 15 September 2026. This is a small numerical diagnostic of a proposed lemma, not a proof or a counterexample to entropy concavity.

X006 proves all semidefinite directions on the τ=0 locus. A tempting way to extend that result to the full Hessian is to show the unique potentially dangerous Schur optimizer is semidefinite. Using the exact criterion in old-097, let M=diag(c23,c13,c12), δ=det M, S=M^(1/2), and let F be the full nine-dimensional Fisher operator in A=SBS coordinates. The optimizer can be normalized as

    B_*=(Id+F/δ)^−1 I.

A direct evaluation on X006's explicit τ=0 family with e=2^−10 and unit odds fields gives

    lambda_min(B_*) approximately −0.00227071246787,
    tr(B_*) approximately 0.615786541378.

The Schur scalar is below one, so this is consistent with negative entropy curvature. It suggests that assuming B_* positive semidefinite is an invalid route even on this special locus. The eigenvalue sign has not been certified by interval or exact arithmetic here; do not cite this diagnostic as a rigorous obstruction.

Reproduction data are entirely explicit: in X006 Section 5 take a=b=sqrt(3)/2, c=(8−5e+i sqrt(e(16−25e)))/8, L=[[1,a,conj(c)],[a,1,b],[c,b,1]], K=L(I+L)^−1, and M=diag(log4,log(1/e),log4). In the orthonormal Hermitian matrix basis, form F=Σ_S p_S g_S g_S^T with g_S,α=tr(S(K−I_{S^c})^−1 S E_α), then solve the displayed nine-dimensional system. A proof route could instead show the optimizer lies in X006's larger conditional cone, or directly control its indefinite part; neither assertion is established here.
