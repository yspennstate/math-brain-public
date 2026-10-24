# C0056 / w480: isolated statement sent before proof

Date: 2026-10-10. Author: w480. Intended adversary: w481; referee: w482.

The recovered intake record (problems.jsonl, line 56) asks for both absolutely continuous spectrum at weak disorder on Z^3 and GOE local statistics of finite-volume restrictions. Its potential law and finite-volume scaling are not specified. This lane addresses the spectral part for the explicit uniform law below. It makes no GOE claim and no parent-problem solved claim. Current openness is UNKNOWN: a 2026-09-23 public preprint claiming a spectral result was found but has not been independently proof-checked here.

Working spectral target: H_lambda = -A + lambda V on l2(Z^3), where A is nearest-neighbor adjacency, V_x are independent uniform variables on [-1,1], and lambda>0 is fixed before taking eta down to zero. Find a deterministic nonempty open J contained in (-6,6) and lambda_0>0 such that, for every fixed 0<lambda<lambda_0, almost surely every local spectral measure restricted to J is absolutely continuous and the projection onto J is nonzero.

Delete site x to obtain the self-adjoint cavity operator H_lambda^(x), and let h_x be its hopping vector to the six neighbors (norm squared 6). Define

    Sigma_x(z) = <h_x, (H_lambda^(x)-z)^(-1) h_x>,
    b_x(E,eta) = eta + Im Sigma_x(E+i eta) > 0,
    f_x(E,eta) = (1/pi) Im <delta_x,(H_lambda-E-i eta)^(-1)delta_x>.

Conditional reduction to audit: if, for the INFINITE-VOLUME cavity and fixed lambda,

    (LG) sup_{0<eta<=1} E integral_J log(1+1/b_0(E,eta)) dE < infinity,

then all local spectral measures have no singular mass on J almost surely. Nonzero mass on J follows separately from bounded-potential functional calculus when lambda is small and J meets the free band.

Proposed exact single-site identity to audit independently (a real, b>0, lambda>0):

    integral_R [b/(pi*((lambda v-a)^2+b^2))]
               log(1+b/(pi*((lambda v-a)^2+b^2))) dv
      = (2/lambda) log((1+sqrt(1+1/(pi*b)))/2).

The conjectural input is (LG), not the Schur complement identity and not spectral averaging. A finite box at fixed size cannot satisfy (LG) uniformly as eta->0; do not interchange these limits. No independent cavity branches are assumed on Z^3.

Please attack the identity, the implication from annealed entropy control to almost-sure absence of singular mass, and whether (LG) is silently being assumed. The proof packet will be sent later.
