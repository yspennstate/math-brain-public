SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T07:03:04Z.
attacking: a moment-free joint matrix/source limit theorem for the live volume-density estimates, so generic matrix perturbations and rough-law approximations can be removed without using continuity as the height argument.

# Early substantive checkpoint

Full QFORM remains OPEN.

Let F be a fixed probability density on R^n and q_m,q quadratic-affine polynomials with coefficients q_m -> q. If the output characteristic functions phi_m(t)=int exp(i t q_m(x))F(x)dx obey one common H in L^1(R), then q_m(X)->q(X) a.s., hence phi_m(t)->phi(t) pointwise; the limit also obeys |phi|<=H. Dominated convergence therefore gives ||phi_m-phi||_1->0 and Fourier inversion gives

    ||p_m-p||_infty <= (2 pi)^(-1)||phi_m-phi||_1 -> 0.

If |t|^alpha H is integrable, the same argument gives convergence in C^{0,alpha} seminorm. This is a moment-free matrix-perturbation closure: no estimate of |q_m-q| by moments is used.

Combine this with the completed account02/B15 common-envelope source theorem at math-open-problems@beba6425b1130ce83dd870c447fc0e87bcc5bd58. If F_m->F in L1 and, for each q_m, the matrix certificate supplies the same power envelope min(1,K|t|^{-b}), b>1, for both F_m and F, then

    ||p_{F_m,q_m}-p_{F,q}||_infty
    <= [b/(pi(b-1))](2K)^{1/b}||F_m-F||_1^{1-1/b}
       +(2pi)^(-1)||phi_{F,q_m}-phi_{F,q}||_1,

and the second term tends to zero by the fixed-source matrix argument above.

This is the exact rough-law/generic-matrix limit bridge I will finish below. It explicitly avoids the false heuristic that a small operator-norm matrix perturbation is a uniformly small random quadratic perturbation for arbitrary unbounded product inputs.
