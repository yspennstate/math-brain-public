# Compensated fourth-observable Gaussian replacement

T067-COMPENSATED-REPLACEMENT-EXT-001 v1. Status: proof (unaudited).
Auxiliary lemma only; no new degree cutoff or novelty assertion.
Dependencies: FOURTH-DERIVATIVES-001 v1 and COMPENSATED-CUBIC-001 v1
(both unaudited); SOFTMAX-DERIVATIVES-001 v1 and the geometric identities in
SHARP-LINDEBERG-001 v1 (previous reviewer PASS). Preserve these exact versions.

Let mu be an S3-invariant calibrated posterior law with uniform prior on three
states. Put a=3p-1, A=||a||^2, M=E A, U=E A^2, T=E sum_i a_i^3>=0,
x=M/9. Let d positive integer, 0<lambda<=L<1. Combine d independent
Potts branches conditional on the root, and write x_next and U_next for the
output second deviation and output E||3p-1||^4. Put s=d lambda^2 x and let
g(s)=E_1 softmax(Z)_1-1/3 and U_G(s)=E_1||3 softmax(Z)-1||^4, where
Z|root i is Gaussian with mean (9s/2)P e_i and covariance (9s/2)P,
P=I-11^T/3. For beta=49/4,

 U_next-U_G(s)+9 beta (x_next-g(s))
       <= d lambda^4 [H_U(L) U+H_M(L) M^2].                 (1)

Constants are explicit rational functions below. At L=1/10 they satisfy
H_U<57 and H_M<38. These rounded bounds are not optimized.

## Generic fourth-order error ledger

For a smooth logit observable f, suppose uniformly in its base point W

 |Df[v_i]|<=g1,  |D2f[h,h]|<=c2||Ph||^2,
 |D3f[h,h,h]|<=c3||Ph||^3,
 |D3f[r,h,h]|<=c31||Pr||||Ph||^2,
 |D4f[h,h,h,h]|<=c4||Ph||^4,

where v_i=(e_i-1/3)/2. All these are absolute bounds. Set

 B4=25/288+(49/100)L/(1-L),
 B3=1/6+(49/20)L B4,
 B1=5/24+(49/20)L B3.

After retaining the full cubic term in the replacement, the remaining
absolute upper error for one branch is lambda^4(C_U U+C_M M^2), with

 C_U(g1,c2,c3,c31,c4;L)
  =g1[1/6+(49/20)L B4]
   +(c2/2)[1/24+B3(1/(1-L)+1+L/2)+1/6]
   +(c31/2) B1/(1-L)^2+c3/6+c4/[24(1-L)^4],
 C_M(g1,c2,c3,c31,c4;L)
  =c2/12+5c31/24+5c3 L^2/72+c4(2+4L^2+L^4)/24.         (2)

Here is the derivation, including the root-conditional changes of density.
Work conditional on root 1; permutation gives every other case. Its input
law is (1+lambda a_1)mu. Write b=-P a^2/2, c=P a^3/3,
L_b=P log(1+lambda a)=lambda a+lambda^2 b+lambda^3 c+r4,
C=(lambda^2 M/2)P, m=C e_1=lambda^2 M v_1, and G~N(m,C).
The exact identities ||b||=A/(2sqrt(6)), c=Aa/6,
||Pa^4||^2=A^4/24+4A(sum a_i^3)^2/9<=25A^4/216,
and A<=6 give

 ||r4||<=lambda^4 A^2 B4,
 ||L_b-lambda a-lambda^2 b||<=lambda^3 A^(3/2) B3,
 ||L_b-lambda a||<=lambda^2 A B1,
 ||L_b||<=lambda sqrt(A)/(1-L),
 ||lambda a+lambda^2 b||<=lambda sqrt(A)(1+L/2).

The scalar log remainder is obtained by integrating polynomial division of
1/(1+t), t>=-lambda, so no convergence outside a power-series disk is assumed.
For any equivariant plane-valued V(a), E[a_1 V]=v_1 E[a dot V]. Thus
E_1 L_b=m-lambda^3 T v_1/2+lambda^4 U v_1/6
+lambda v_1 E[a dot r4]. The noncubic mean contribution is bounded by
lambda^4 U g1[1/6+(49/20)L B4], since sqrt(6)<=49/20.

The raw second-moment difference, after its leading cubic term, has nuclear
norm at most

 lambda^4 {U[1/24+B3(1/(1-L)+1+L/2)+1/6]+M^2/6}.

Indeed compare L_b L_b^T with B B^T for B=lambda a+lambda^2 b using
||zz^T-ww^T||_*<=||z-w||(||z||+||w||). The lambda^4 b b^T term costs
U/24. The conditional-density correction on the cubic tensor is exactly
lambda^4 E[a_1(ab^T+ba^T)], whose nuclear norm is lambda^4 U/6.
The Gaussian raw second moment has extra m m^T of norm lambda^4 M^2/6.
All radial bounds have the same expectation under mu and under root 1,
by permutation symmetry. The Taylor factor 1/2 and Hessian operator bound
c2 give the c2 terms in (2).

For q(z)=D3f(W)[z,z,z], integration along the segment from lambda a to L_b
gives |q(L_b)-q(lambda a)|<=3c31 lambda^4 A^2 B1/(1-L)^2.
The Taylor factor 1/6 gives the c31 term in C_U. The conditional-density
correction on the leading cubic is at most c3 lambda^4 U/6, using
|a_1|<=sqrt(A). For G=H+m with centered Gaussian H,
E q(G)=q(m)+3 E D3f(W)[m,H,H]. Since E||H||^2=lambda^2 M and
||m||=lambda^2 M/sqrt(6), the Taylor factor bounds these respectively by
lambda^4 M^2 (5c3 L^2/72) and lambda^4 M^2(5c31/24).
Here M<=6 and 1/sqrt(6)<=5/12 have been used.

Finally the order-four Taylor remainder is at most c4||z||^4/24.
For L_b its expectation is <=c4 lambda^4 U/[24(1-L)^4]. For the Gaussian,
E||G||^4=lambda^4 M^2[2+(2/3)lambda^2 M+lambda^4 M^2/36]
<=lambda^4 M^2(2+4L^2+L^4). This proves every term of (2), with no
independence assumed except the stated conditional independence of W and
the branch. Bounds on second diagonal derivatives imply the Hessian operator
bound by symmetry and the spectral theorem. All Taylor segments lie in R^3.

## Cubic term and calibrated compensation

The cubic terms retained above, for replaced root i, are lambda^3 T ell_i^f,
where, with {i,j,k}={1,2,3},

 ell_i^f=[sum_r D_r^3 f-D_i f-(D_j-D_k)^2 f]/4.        (3)

This follows from the exact conditional mean correction -T v_i/2, the raw
second tensor correction -(T/2)(e_j-e_k)(e_j-e_k)^T, and the third moment
contraction (3T/2)sum_r D_r^3f, including Taylor factors 1,1/2,1/6.

Let F_i=softmax(z)_i, Q=A^2, and H_i=Q+9 beta F_i. Apply (2) separately
to Q with constants (8,20,38,38,99) and to F_i with
(1/8,1/5,2/5,1/2,3/5); add their absolute error bounds with coefficient
9 beta. Thus

 H_U=C_U(8,20,38,38,99;L)+9 beta C_U(1/8,1/5,2/5,1/2,3/5;L),
 H_M=C_M(8,20,38,38,99;L)+9 beta C_M(1/8,1/5,2/5,1/2,3/5;L).   (4)

These derivative constants are applied to H_i, not to the radial function
Q+beta A itself. This distinction matters before taking calibrated expectations.

Each hybrid is a genuine symmetric Bayesian experiment: the Gaussian
densities have likelihood ratios exp(g_i-g_j), and independent sums of log
likelihoods remain calibrated. Its root-i posterior law has density 3p_i
relative to its unconditional symmetric law nu. Consequently the expected
cubic coefficient for H_1 equals the nu-average of

 sum_i p_i ell_i^Q +9 beta sum_i p_i ell_i^{F_i}
 = S_Q+beta S_A = S_{Q+beta A} <= 0.                  (5)

The equality S_A=9 sum_i p_i ell_i^{F_i} can also be checked from
S_A=-9e2(e2-9e3) and sum_i p_i ell_i^{F_i}=-e2(e2-9e3).
The final sign is COMPENSATED-CUBIC-001 v1, and T>=0 preserves it.
Average and telescope (2) over all d replacements; only the favorable cubic
term is discarded. Radial Q has equal conditional and unconditional means,
and calibration gives E_1 F_1-1/3=x_next or g(s). The constants in H_i cancel
between the two endpoints. This proves (1). M=0 is deterministic and immediate.

## Critical fixed-point consequence; remaining obligation

At a critical fixed point lambda=d^(-1/2), x_next=x, U_next=U, write
K=U/(81x^2), gamma=(x-g(x))/x^2. If x>0 and d>H_U,

 K <= [U_G(x)/(81x^2)-beta gamma/9+H_M/d]/[1-H_U/d].    (6)

The usual one-sided F_1 comparison independently gives
K>=(d gamma/81-C_M(F_1;L))/C_U(F_1;L).
These are simultaneous inequalities, not an independence assertion.
Numerically their incompatibility suggested d>=100. That is NOT proved here:
a certified uniform upper bound for U_G and continuous gap comparison are
still required. Full T067 remains open; this lemma asserts no improvement to the
checked cutoff256. The separately submitted cutoff156 retains its audit status.

## Domain extension, with no new small-L assertion

The predecessor v1 stated L<=1/10. This new claim separately permits any L<1.
Every displayed remainder uses only 0<lambda<=L<1 and factors (1-L)^(-k).
In particular log division is an integral identity for t>-1, even when
lambda a_i exceeds1; no alternating-series remainder is used. Bounds A<=6,
sqrt(6)<=49/20 and1/sqrt(6)<=5/12 do not depend on L. The covariance and
third-moment comparisons use exact identities and absolute derivative bounds,
not an unstated small-L truncation. The Gaussian fourth-moment factor is
2+4L^2+L^4 for every L. Exact likelihoods remain positive since lambda<1;
calibration and the retained compensated cubic sign are unchanged. Thus the
entire preceding ledger proves the extended domain. The numerical bounds
H_U<57,H_M<38 are asserted only at L=1/10, not at arbitrary larger L.
No predecessor proof or its receipt is edited. New cutoff compositions must
re-evaluate all constants and verify their positive denominators separately.
