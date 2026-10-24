# R15 idea-before-code note: finite residual Gram reduction for the N=14 F0111 cell

Status: retained F0111 screen only; PENDING / SELF_CHECK_ONLY / NOT CLAIMED. Native I0076 remains retired-handoff and is not reopened.

Methods for this route: #11 DUALIZE, #15 BREAK THE SYMMETRY ON PURPOSE, #24 FIND THE EXTREMAL OBJECT. These differ from the preceding #4/#19/#30 triple; all 30 move numbers have already appeared historically, so this run applies a nonconsecutive triple to a new object.

## Carried scalar cell

For n=30, full-support two-level Hessian-null exact contacts on the z=1+s>1 branch have already been reduced to N=|K| in {11,12,13,14}, with exact scalar cells. The narrowest is N=14, where

- 14/25 < delta < 4/7,
- 0 < s < s_14 < 4340/10^6,
- L_K=y A_K <= 14 < U_K=-29y/k,
- A_K=1+3 t_K^2/R.

The preceding boundary theorem only excludes sequences with s->0. This note seeks an exact finite-s obstruction, beginning with N=14.

## New exact residual-Gram reduction

Let H=D^2(P-F)(q) >= 0, let h=a 1_J-b 1_K be its two-level null vector, and let the projective fourth-order covector be beta_i=r_i t_J on J and beta_j=r_j t_K on K after the common m^2 scaling is removed. With C=R/3, the projective necessary condition is equivalent to the rank-one downdate

K := H - (3/R) beta beta^T >= 0.

Cubic nullity gives beta.h=0, hence Kh=0. Write K as a Gram matrix of residual vectors w_i. Define

A_J = 1+3 t_J^2/R,
A_K = 1+3 t_K^2/R,
A_JK = 1+3 t_J t_K/R.

Then exactly

||w_i||^2 = r_i(1-A_J r_i) for i in J,
||w_j||^2 = r_j(1-A_K r_j) for j in K,

and for i != j

B_ij = <w_i,w_j> + A_{block(i),block(j)} r_i r_j,

where the mixed block coefficient is A_JK.

Let W_J=sum_{i in J}w_i, W_K=sum_{j in K}w_j. Since Kh=0,

a W_J=b W_K.

Put T=||W_K||^2. The aggregate pair-coefficient masses U=sum_{J-J}B, V=sum_{K-K}B, W=sum_{J-K}B collapse *without any within-block symmetry assumption* to

2U=(b^2/a^2)T-x+A_J x^2,
2V=T-y+A_K y^2,
W=(b/a)T+A_JK x y.

Thus the entire projective/PSD subsystem has a one-scalar block-sum compression. The aggregate null equations should reduce to identities already encoded by the cubic-null scalar formulas, leaving T constrained only by vector-capacity and coefficient-nonnegativity/global-contact information.

## N=14 capacity pinch to exploit

For K-block size N, residual-vector Cauchy gives

T=||W_K||^2 <= N sum_{j in K} r_j(1-A_K r_j)
<= y(N-A_K y)=y(N-L_K).

For N=14 this is tiny throughout the scalar cell because L_K is close to 14, and it vanishes at the scalar upper boundary. At the same time full support gives each r_j>r_min=-k/29 and projective positivity gives r_j<=1/A_K. Since their sum is y, N=14 nearly saturates both bounds.

The route is to combine the exact compressed formulas with one of:

1. gradient-contact nonnegativity A_i>=0 summed over K or J;
2. exact value contact E=sum B_ij q_i q_j, using q_j<=log(S/A_K)=log(29/Q_K) on K;
3. a mixed nonnegative ray from the previously proved all-ray cone.

A useful target is a finite-s inequality that forces a positive lower bound on T or on a heavy-J defect, contradicting T<=y(14-L_K) across the whole N=14 cell. If successful, this eliminates the complete N=14 scalar branch rather than only the s->0 boundary.

No checker or numerical scan is evidence for the theorem; any finite claim will be certified only after an analytic inequality is identified.