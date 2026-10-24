SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T01:47:17Z.
attacking: bridge ridge leverage to admissible fractional three-volume weights at an intrinsic scale, then optimize and compare both certificates on one explicit rotated indefinite matrix with q=1 volume failure.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

Fresh owner control read before this checkpoint: math-research-brain revision 2026-09-22.15. Required corrections consumed: no law-uniform pointwise quadratic-phase decay, no post-rotation independence, no arbitrary-joint rank-three coarea bound, no positive conditional projection-density moment, and no universally good local physical minor/cross-rank-three cut.

## 1. Weighted sharp fractional-volume extension

Let M=A[I,J] for disjoint ORIGINAL coordinate banks. Index nonzero 3x3 minors by omega=(S,T), write a_omega=det(M[S,T])^2, and let w be any probability law on these minors. Let alpha_i=P_w(i in S), beta_j=P_w(j in T), and

G(w)=exp(sum_omega w_omega log a_omega + H(w)).

Repeating the determinant AM-GM and sharp Hausdorff-Young proof of the current fractional-volume theorem with w in place of the volume-sampling law gives: for 1<=q<3/2, if max_i alpha_i<=q/2, then

||p_(X^TAX+b^TX+c)||_inf <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6).

Indeed the determinant expansion is bounded below by

exp(E_w log(a_omega/w_omega)) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j),

and every later scalar factor is exactly the same as in the source theorem. This keeps arbitrary self blocks, outside couplings and affine terms.

For the Gibbs volume law w*_omega=a_omega/Z, Z=sum a_omega=e3(M^TM), one has the exact identity

log G(w)=log Z-KL(w||w*).

Thus admissible reweighting loses only exp(-KL/6) in the density certificate.

## 2. Intrinsic ridge-volume bridge

Put C=MM^T, let lambda_j be its eigenvalues, E2=e2(lambda), E3=e3(lambda)>0, rho=E3/E2, and let W denote the third-volume marginal matrix. Its spectral weights are

p_j=lambda_j e2(lambda without j)/E3.

Since e2(lambda without j)<=E2 and p_j<=1,

p_j<=min(1,lambda_j/rho).

For every a>0 and x>=0,

min(1,x) <= (1+a)x/(a+x).

Hence, with gamma_a^2=a rho and K_a=C(C+gamma_a^2 I)^(-1),

W <= (1+a)K_a.

Consequently alpha_i<= (1+a)(K_a)_ii and theta_a=tr K_a>=3/(1+a). Therefore, if 0<a<1/2 and max_i(K_a)_ii<=1/2, the SAME original-coordinate cross block satisfies simultaneously:

(1) ridge q=1: max diag K_a<=1/2 and theta_a>2;
(2) fractional volume q=1+a: max alpha_i<=(1+a)/2.

So one intrinsic ridge-leverage test certifies both routes. This is a matrix bridge, not yet an exhaustive consequence of s_3(A)>=1.

## 3. New explicit q=1-failure family to optimize

Take the normalized first three columns of the Sylvester H8 and rotate two ORIGINAL rows whose three-dimensional row vectors coincide. Choose the Givens angle by sin(2theta)=5/12. The resulting rank-three projection P has diagonal

17/32, 7/32, 3/8,3/8,3/8,3/8,3/8,3/8.

Set delta=1/100 and

M=delta I_8+(1-delta)P,
A=[[0,M],[M,0]].

Then A is a genuinely rotated indefinite 16x16 physical matrix with spectrum +1 (x3), -1 (x3), +delta (x5), -delta (x5), hence it satisfies the exact target. All physical scalar diagonals vanish.

For epsilon=delta^2=10^-4,
E3=1+15epsilon+30epsilon^2+10epsilon^3=1.00150030001.
The volume marginal at the 17/32 row is 0.5311251373..., so the q=1 volume-sampling gate genuinely fails. The next step is to compute the KL-optimal admissible tilt, compare its q=1 weighted-volume bound to the direct q>1 fractional-volume certificate and to a one-scale ridge certificate on this same A, and apply the completed account03/B04 local-pair theorem to the same physical matrix as a complementary obstruction.
