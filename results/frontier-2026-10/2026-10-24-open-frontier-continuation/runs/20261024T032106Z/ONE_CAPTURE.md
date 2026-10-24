# Same-sign selected law: at most one permanent face capture

Status: PROVED internally after the independent reviews in this run; not an external priority claim. This is an additional deterministic simplification of agents/i02_matching.md, not a statement about arbitrary initially mixed residuals.

Let 0<rho<1, s=1-rho^2, G=[[1,rho],[rho,1]], C be symmetric positive definite with C12>0, P>0, and R1,R2>0. Put Q=C+P G. The selected endpoint population from the same-sign entrance theorem is positive-z only, with total square mass P. Until a face is reached the residual and common normalized endpoint are

    r^a(t)=exp(-Qt)R,
    B(t)=G Q^{-1}(I-exp(-Qt))R=G integral_0^t r^a(v)dv.

All retained endpoints equal z B(t). The first residual-axis crossing is not an endpoint-face event: B has both coordinates strictly positive there. In particular, the matrix Q continues through that residual sign change.

## The explicit one-switch algorithm

Let tau be the first zero of a component of r^a. If tau=infinity, the selected residual is r^a forever and no endpoint face is reached. If tau<infinity, exactly one coordinate b crosses zero; denote the other by p. Define

    ell_b=(G Q^{-1} R)_b.

If ell_b>=0, again r=r^a forever and no finite endpoint capture occurs. If ell_b<0, there is a unique positive time sigma>tau satisfying B_b(sigma)=0. Then

    r(t)=exp(-Qt)R,                              0<=t<=sigma,
    r(t)=exp(-Q_s(t-sigma))exp(-Q sigma)R,        t>=sigma,
    Q_s=C+P s e_p e_p^T.

The normal endpoint coordinate stays zero for every t>=sigma. The supporting coordinate stays positive and increases. There is no later release or recapture in this same-sign branch. This is a formula for output action; it does not assert pre-step tangent-Gram convergence during chatter.

## Proof

The positive off-diagonal of Q makes its two eigenvalues distinct. Its positive Perron eigenvector belongs to the larger eigenvalue. If R lies on that ray, r^a remains positive and tau=infinity. Otherwise the nonzero smaller-eigenvalue component eventually has mixed signs, so tau is finite. Invertibility of exp(-Qt) rules out simultaneous zero of both residual components. At the first axis zero, r_b'= -Q_bp r_p<0, with r_p>0, so the crossing is strict. The mixed quadrant is invariant thereafter for this extended active ODE by the Metzler argument.

Take b=1,p=2; swapping coordinates proves the other case. For t>=tau set k=-r^a_1/r^a_2. Writing Q=[[a,beta],[beta,d]], beta>0, gives exactly

    k'=f_a(k)=beta+(d-a)k-beta k^2,   k(tau)=0.

This quadratic has exactly one positive root kappa. Thus k increases strictly from zero to kappa. Also

    B_1'=r^a_2(rho-k),
    B_2-rho B_1=s integral_0^t r^a_2(v)dv>0.

Before tau both residual coordinates are positive, so B_1,B_2 increase from zero. If kappa<=rho, B_1 is strictly increasing for all finite t and cannot hit zero. If kappa>rho, it first increases, then strictly decreases after the unique time k=rho. Its limit is ell_1. Thus a finite zero exists exactly when ell_1<0; it is unique and transversal, with k(sigma)>rho. If ell_1=0, the strictly decreasing tail remains positive at every finite time and only approaches zero asymptotically. The displayed tangential identity prevents B_2 from reaching zero before B_1. This proves the claimed pre-capture rule, including the equality case.

At sigma the proposed face residual evolves with Q_s=[[C11,C12],[C12,C22+P s]]. Its mixed-quadrant ratio solves

    k'=f_s(k)=C12+(C22+P s-C11)k-C12 k^2.

The key equality is

    f_s(rho)=f_a(rho)
             =C12 s+rho(C22-C11)+P rho s.

Because capture required kappa>rho, f_a(rho)>0. Hence the half-line k>=rho is invariant under the face ODE and its trajectory starting at k(sigma)>rho stays strictly above rho at every finite time. The normal relay driver r_1+rho r_2 is therefore negative. Its reflected normal coordinate, initially zero at sigma, stays zero forever. The support derivative is s r_2>0, and r_2 remains strictly positive by the Metzler argument. This verifies the face law self-consistently. Uniqueness of the already proved reflected Volterra equation identifies it as the selected law. No later regime can occur.

## A realizable strict example requiring the switch

Let rho=1/2, P=1, R=(1,10), C=[[1,1],[1,3]]. Then

    Q=[[2,3/2],[3/2,4]],
    (G Q^{-1}R)_1=-7/23<0.

The first residual crossing is coordinate 1: the positive eigenvector ratio of Q is (2+sqrt(13))/3<10. Consequently there is a finite permanent support-2 face capture. Continuing Q forever is false: its candidate B_1 would eventually be negative, whereas the selected reflected endpoint cannot become negative.

This C is compatible with the original-coordinate ray law. Take x1=(cos(pi/12),sin(pi/12)), x2=(sin(pi/12),cos(pi/12)); they are unit inputs with inner product 1/2. The positive coordinate-ray masses A=2-2/sqrt(3), B=2+2/sqrt(3) produce exactly C above. Each actual stable ray mass has support (0,infinity), the selected P has support (0,infinity), and R has a full-dimensional density with full support independently of those masses. A neighborhood of this strict example therefore has positive probability. The example is not a claim that an exact prescribed environment has positive probability.

## Sign mirror and scope

For R1,R2<0 set r_tilde=-r, R_tilde=-R and use the negative-z survivor mass P_-. Apply this entire construction to R_tilde>0, then negate the residual back. The original endpoint is |z|B_tilde and the signed output contribution is -z^2 B_tilde. There is again at most one permanent face capture. General initially mixed residuals may have both sign populations and retain the prior reflected law with possible release/recapture; the present one-capture proof does not apply to them.
