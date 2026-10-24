# account03/B11 pass-2 r19 audit

SIGNED IN - auditing the exact fourteen-page five-singular-value proof, account account03, slot B11, 2026-09-25T09:14:32Z.

Source: yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c, short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8, PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.
Control at start: math-research-brain@30dd2c723a64939298b93b421660c9f3a42edf28; revision 2026-09-25.1.
Audited in pass 2 this run: short.tex lines 173-371; PDF pages 4-8 rendered at 200 dpi.

## Verdict

No new theorem-bearing defect was found. Theorem 3.1, Lemma 3.2's statement, Lemma 3.3, Lemma 4.2 and Lemma 4.3 survive an independent reconstruction. Two retained literal-source issues were independently reproduced:

- L224 GAP: the source takes log p(y) before separating the possible case p(y)=0. Minimal repair: if p(y)=0 the estimate is immediate; otherwise take logarithms.
- L319-L321 / C02 GAP under B11's strict literal-step standard: insert |E F(X_{I'})|^2 <= E|F(X_{I'})|^2 before averaging the pointwise conditional estimate to obtain (4.5).

There is a genuine peer classification disagreement on C02: account02/B04@f4af985300fb2de251f6487d8afd970a8d91f7e5 treats "and averaging" as acceptable Jensen/Cauchy shorthand (PASS), while account02/B18@d51c83dd102cd50ff4b6a43da2c04832484685d7 and B11 classify the literal inference as a local GAP. The repaired inequality agrees.

## Theorem 3.1

The frame identity gives sum_i c_i=d. With F=prod_i f_i(tau,u_i dot x)^{c_i} and v_i=partial_y log f_i,
(partial_tau F-Delta F)/F = sum_i c_i v_i^2 - |sum_i c_i v_i u_i|^2.
If W has columns sqrt(c_i)u_i, WW^T=I, so the last squared norm is at most sum_i c_i v_i^2.

On compact tau intervals, Gaussian support estimates give f_i(tau,y)<=C exp(-y^2/(16 tau_1)); f_i'/f_i is a probability-weighted average of -(y-z)/(2 tau), and f_i''/f_i is a probability-weighted average of (y-z)^2/(4 tau^2)-1/(2 tau). Hence F, partial_tau F and the first two x-derivatives are polynomial times exp(-|x|^2/(16 tau_1)). Differentiation under the integral and int Delta F=0 are valid, so int F is nondecreasing.

After x=sqrt(tau)z, sqrt(tau)f_i(tau,sqrt(tau)s) tends to (4pi)^(-1/2)mu_i exp(-s^2/4), and is uniformly bounded by C_i exp(-s^2/16) for tau>=1. The frame identity gives an integrable product majorant C exp(-|z|^2/16), so the large-time limit is prod_i mu_i^{c_i}. At small time, Gaussian convolution converges at Lebesgue points; inverse images of 1D null exceptional sets under nonzero u_i are null in R^d. Fatou plus monotonicity gives the BL inequality. Truncations min(h_i,m)1_{[-m,m]} remove the bounded-support reduction by monotone convergence.

## Lemma 3.2

For d<n, complete U to (U,W). The marginal density is the z-integral of the original product density. With beta_i=|w_i|^2, orthogonality gives sum w_iw_i^T=I, sum beta_i=n-d and 0<=beta_i<=1. beta_i=0 factors are z-independent and <=1. For positive beta_i, v_i=w_i/sqrt(beta_i) is a BL frame with weights beta_i and h_i(t)=f_i(a_i+sqrt(beta_i)t)^{1/beta_i}; int h_i<=beta_i^(-1/2). Hence p(y)<=prod beta_i^(-beta_i/2). L224 needs the p(y)=0 split before taking logs. Then beta log(1/beta)<=1-beta gives p<=e^{d/2}. Thin SVD gives part (b).

## Lemma 3.3

The difference density is int f(x+y)f(y)dy<=1. For m=floor(p/2), m>=1, 2m<=p and m>=p/4. Since |fhat|<=1 and f in L2,
int|fhat|^p <= int|fhat|^{2m} <= int|fhat|^2 <=2pi.
|fhat|^{2m} is the characteristic function of sum_j(Y_j-Y_j'). Fourier inversion gives a continuous density with p_Z(0)=(2pi)^(-1)int|fhat|^{2m}. Lemma 3.2 applied to the independent variables Y_j,-Y_j' gives an a.e. bound sqrt(e)/sqrt(2m); continuity upgrades it at zero. The stated 2pi sqrt(2e)/sqrt(p) follows.

## Lemma 4.2

sum_i alpha_i=m. Rewriting the entropy expression over positive w_T and applying Jensen yields log sum_T prod_{i in T}alpha_i. In (sum_i alpha_i)^m each square-free m-monomial occurs m! times and all other terms are nonnegative, hence the sum is <=m^m/m!=omega(m).

## Lemma 4.3

Theta_l(H)>0 implies H rows independent and Theta(H)>0. Orthogonal residual rows c_i give Theta(H union T')=Theta(H)theta(T'). Thus w_T'=theta/Z is a probability and alpha_i=Theta_l(H union {i})/Theta_l(H)<=1/2.

With an independent copy X_J', D=X_J-X_J' has independent original-coordinate components with density caps one. The displayed Q and R decompositions are exact.

Step 1: Cauchy-Schwarz in X_I after conditioning on X_J, copy expansion, and integration over the original independent X_i give (4.4).

Step 2: a=e^{itF}p_H has ||a||_2^2<=1. Y=M_HX_J has density cap e^{k/2}Theta(H)^(-1/2). For fixed x, nu_x(B)=E[e^{itR(x,X_J)}1_B(Y)] has density g_x p_Y with g_x=E[e^{itR}|Y], |g_x|<=1. Hence ||nu_x||_2^2<=||p_Y||_infty. Scaled Plancherel gives the pointwise square bound with coefficient (pi/|t|)^k. Insert the missing Jensen inequality to obtain (4.5).

For mollification, kappa_e(z)=int rho_e(y)rho_e(y+z)dy is a probability density. Expanding ||nu_x*rho_e||_2^2 gives the copy identity with kappa_e(M_HD). L2 approximate-identity convergence plus Young's inequality supplies the dominated-convergence step. Integrating the original X_{I'} coordinates produces the characteristic-function product and (4.6).

Step 3: positive-alpha exponents satisfy sum_{T' contains i}w_T'/alpha_i=1; weighted Holder is exact, and only positive w_T' are used.

Step 4: the combined hub/residual row matrix B has block-diagonal Gram matrix and det(BB^T)=Theta(H)theta(T')>0. BD therefore has the projection-density cap e^{ell/2}(Theta(H)theta)^(-1/2). The inner z_i integrals are bounded using Lemma 3.3 with p=1/alpha_i>=2, giving pi sqrt(2e alpha_i)/|t|.

Step 5: theta(T')=Z_H w_T' gives the determinant product Theta_l(H)^(-1/2)e^{H(w)/2}; the alpha product is exp((1/2)sum_i alpha_i log alpha_i). Lemma 4.2 produces omega(ell')^{1/2}, and all pi,t,e exponents combine exactly to (4.3).

## Coverage state

Pass 2 is now covered on 98-127 and 140-639. Still UNCHECKED in pass 2: 1-97, 128-139, 392-394, 640-675. First unchecked line: 1. Pass 2 remains incomplete.

Execution status: WITHOUT_VERIFIED_BRAIN. No schedule, notification, permission, task-count, or email setting was changed.
