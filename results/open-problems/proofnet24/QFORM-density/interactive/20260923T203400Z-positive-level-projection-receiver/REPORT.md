# Positive-level projection receiver for a near-hub quadratic form

## Theorem and scope

Let H be independent of Y=(L,V,P), with probability density bounded by K_H. Assume every normalized one-dimensional orthogonal projection of Y has density bounded by K_1 and every normalized two-dimensional orthogonal projection has density bounded by K_2. Dependence among L,V,P is allowed. For arbitrary real beta,epsilon, put

Q=2HL+beta L^2+V^2+2 epsilon LP.

Then ess sup over s>=0 of p_Q(s) is at most 4 K_H K_1+2 K_2. This is uniform in beta and epsilon, including epsilon=0. This note makes no claim for negative targets or an aH^2 term.

For Y=U^T X with U an orthonormal three-frame and independent original-coordinate probability densities <=1, the linear projection density theorem gives K_1<=sqrt(2), K_2<=2. The bound is therefore 4sqrt(2)+4<10, irrespective of frame diffuseness. Translating Y does not affect the assumptions.

## Coarea identity

Fix s>=0 and r=sqrt(s). Since L has a density, L=0 is a null event. Parameterize V=r+tL. Define c_t=(t^2+beta)/2, W_t=V-tL, U_t=c_t L+epsilon P. Then

Q-s=2L(H+rt+U_t).

The Jacobian dV=|L| dt cancels the 1/(2|L|) factor from integration in H. Let f_t be the joint density of (W_t,U_t). For almost every s>=0,

p_Q(s)=(1/2) integral_R integral_R f_t(r,u) f_H(-rt-u) du dt.       (1)

This can first be read weakly against compactly supported test functions; approximation yields the density identity.

W_t is an unnormalized linear projection with row norm sqrt(1+t^2), so its density cap is K_1/sqrt(1+t^2). Hence the inner integral in (1) is <= K_H K_1/sqrt(1+t^2).

The two rows defining (W_t,U_t) are (-t,1,0) and (c_t,0,epsilon). Their exterior-product norm is

Delta_t=sqrt(c_t^2+epsilon^2(1+t^2)).

Thus f_t<=K_2/Delta_t, and the inner integral in (1) is also <= K_2/Delta_t <= 2K_2/|t^2+beta|. At a zero denominator use the first bound.

## Uniform integral

Write A=K_H K_1, B=K_2. The preceding inequalities give

p_Q(s) <= (1/2) integral_R min{ A/sqrt(1+t^2), 2B/|t^2+beta| } dt.       (2)

For beta>=0, use the first term on |t|<=1 and the second on |t|>1. This gives A+2B.

For beta=-r_0^2 with 0<=r_0<=2, use the first term on |t|<=4. Outside, |t^2-r_0^2|>=3t^2/4. This gives 4A+2B/3.

For r_0>2, split |t|<=r_0/2, r_0/2<|t|<2r_0, and |t|>=2r_0. Use the second term on the first and last regions, contributing <=16B/(3r_0) before the outer factor 1/2. The middle has total length 3r_0 and uses the first term, which is <=2A/r_0; it contributes <=6A before the outer factor. Hence (2) is <=3A+8B/(3r_0)<=3A+4B/3. All cases imply 4A+2B.

## Limitation

For s<0, setting V=tL leaves a nonlinear s/(2L) term in the hub argument. The projection argument above does not control it. A uniform negative-level estimate needs an additional hypothesis or method. An added aH^2 term also lies outside this proof.
