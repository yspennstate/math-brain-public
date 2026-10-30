# Defect-block latent information tradeoff

All entropies, relative entropies and mutual informations are in bits. A product law means a product over individual frequency bits. No reference conversion is asserted necessary for FEI. This is a generic probability inequality applied to an explicitly Boolean-realizable spectrum; it is not a new Booleanity admission condition.

## 1. Actual spectrum and scalar certificate

The Boolean truth table v=(-1,1,1,1,1,1,1,1), in integer binary order, has Walsh coefficients (3/4,-1/4,...,-1/4). Thus its squared spectrum P has P(000)=9/16 and all other seven masses 1/16. Each frequency bit has marginal mu=(3/4,1/4). Its total correlation is

 tau = sum_i H(mu)-H(P) = 2-(9/8)log2(3), with 1/8<tau<1/4.

The strict bounds follow respectively from 3^3<2^5 and 3^9>2^14. Tensoring r independent actual Boolean copies gives exactly P_r=P^{tensor r}, with total correlation r*tau.

For x,y>=0 there is the exact homogeneous polynomial identity

 4(3x^2+y^2)^3-[8x^3+(x+y)^3]^2
       =3(x-y)^2(3x^2+y^2)^2 >=0.                            (1)

Consequently 8x^3+(x+y)^3 <= 2(3x^2+y^2)^{3/2}. For three nonnegative functions f_i with values (x_i,y_i), the two-term Holder inequality gives

 8 product_i x_i + product_i(x_i+y_i)
 <= product_i [8x_i^3+(x_i+y_i)^3]^{1/3}
 <= 2 product_i (3x_i^2+y_i^2)^{1/2}.

Dividing by16 proves

 E_P product_i f_i(X_i) <= product_i (E_mu f_i^2)^{1/2}.       (2)

This argument includes zero entries without division or limiting exceptions. Holder here follows by normalizing the three nonnegative two-vectors to unit l3 norm and applying abc<=(a^3+b^3+c^3)/3 coordinatewise. Independence of the r blocks tensorizes (2) for arbitrary functions of the 3r individual bits.

## 2. Entropic dual and an all-alphabet tradeoff

For ANY law R on {0,1}^{3r}, set f_i(x)=sqrt(R_i(x)/mu(x)). The tensorized right side in (2) is1. Write F=product_i f_i. On the support of R, F>0. Normalizing P_r*F and using nonnegativity of its relative entropy gives

 D(R||P_r) >= E_R log2 F - log2 E_{P_r} F
             >= (1/2) sum_i D(R_i||mu).                    (3)

The normalizer is positive because P_r has full support and each marginal density is nonzero somewhere. Thus (3) includes degenerate R. For any finite auxiliary Z coupled to X~P_r, applying (3) to each posterior R=P(X|Z=z) and averaging gives

 sum_i I(X_i;Z) <= 2 I(X;Z).                               (4)

No conditional independence between bits of R is assumed. Let q(x)=sum_z w_z product_i q_{zi}(x_i), and suppose q>0 wherever P_r>0. Remove zero-weight components. Define the EXACT mixture posterior k(z|x)=w_z product_i q_{zi}(x_i)/q(x), the lifted joint L(x,z)=P_r(x)k(z|x), v=L_Z, and R_z=L(X|Z=z). Direct logarithmic expansion proves

 D(P_r||q) = TC_L(X|Z)+D(v||w)
              +sum_z v_z sum_i D((R_z)_i||q_{zi}).          (5)

All terms are complete; reference mass outside any chosen subevent is retained. Also

 TC_L(X|Z)=r*tau-sum_i I_L(X_i;Z)+I_L(X;Z)
           >=r*tau-I_L(X;Z),                              (6)

by (4). Combining (5)-(6) yields the stronger entropy-sensitive form

 D(P_r||q)+I_L(X;Z) >= r*tau.                              (7)

In particular D(P_r||q)>=max(0,r*tau-H_L(Z)) and, for at most M components,

 D(P_r||q)>=max(0,r*tau-log2 M).                           (8)

The posterior law v, not w, occurs in H_L(Z). Infinite KL makes the lower bound immediate without defining a posterior on absent atoms. The case r=0 is ordinary KL nonnegativity. No optimality of the coefficient2 in (3) or of the resulting rate is claimed.

Unlike the cardinality relaxation, (7) is invariant under redundant latent refinement: replacing each component by identical copies and adding a label U independent of X conditional on Z leaves q unchanged and I(X;Z,U)=I(X;Z). An arbitrary number of unused label bits therefore cannot weaken (7). A whole finite history may be used as Z, and its information obeys the ordinary chain rule. However (3) cannot be reapplied to each history-conditioned source unless that source again has the specified tensor law: conditional rows generally lose block independence. No such repeated conditional contraction is used here.

## 3. Complete Boolean handoff and scope

Use the established actual complementary controller a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1), b=1-a^2, beta=3/8. For actual g=v^{tensor r}, h=z1*z2*z3*g and G_sigma=a+sigma*b*h, query z1 from the matched full incoming reference. Both children are nonconstant; both have the same complete spectrum. Child JS, erasure, singleton ghost and the listed phase/coherent refunds are zero. Keep every actual controller vacuum mass ahat(U)^2, and every bhat(U)^2 factor, replacing only the shifted core law by q in both children. Orthogonality of the mandatory remaining z2,z3 labels prevents collision with vacuum. Literal cancellation of the full CE sums gives

 average terminal CE + erasure - incoming CE = beta D(P_r||q). (9)

For different allowed q in the two terminals, apply (7) separately and average. Therefore the mean divergence bill plus beta times mean posterior information is at least beta*r*tau. If each target has at most M product components, the bill is at least beta*max(0,r*tau-log2 M), improving the previous factor2 penalty for this SAME Boolean family. At physical reach eta multiply the entire statement by eta, without changing old bookings or other terminals. A free latent label is not supplied: (7) is an information tradeoff, not an influence-priced account.

The full physical influence is 23/8+9r/32; the full entropy is 5-(9/16)log2(3)+(3r/8)(4-(9/8)log2(3)). Hence this family is not an FEI counterexample. Keeping the inherited core law avoids this optional conversion. The exact product-mixture representation size remains2^r by the earlier rank certificate; (8) is a quantitative approximate-representation bound, not a sign-realizability exclusion. Initial arbitrary-core influence pricing and the necessity/payment of a useful compatible target remain unproved.

## 4. Attempt to break or strengthen the contraction

Let L=sum_{i=1}^3(X_i-1/4). Under P, Var(L)=15/16 and E[L|X_i]=(5/3)(X_i-1/4), so sum_i Var(E[L|X_i])=25/16. For R_epsilon=P(1+epsilon L), positive for sufficiently small signed epsilon, the Taylor expansion of KL at epsilon0 gives

 lim_{epsilon->0} sum_i D((R_epsilon)_i||mu)/D(R_epsilon||P)=5/3.

Indeed (1+t)ln(1+t)=t+t^2/2+O(t^3); the linear terms average to0, leaving the variance ratio25/15. Thus a universal contraction coefficient strictly below5/3 is FALSE, even on this fixed8-atom block. Our proven coefficient2 is bounded away from that excluded range, but not asserted sharp. These laws are dual-test probability laws and are not claimed Boolean spectra. The actual input spectrum P_r is Boolean-certified separately.

## 5. First unsupported universal line

An admissible arbitrary-core reference family with a dimension-independent initial influence price, closed under actual inherited physical marginals, has not been constructed. Neither latent information nor mixture cardinality has been paid from a SAME unused original influence allowance. The new tradeoff cannot substitute for that missing source-price theorem. It sharpens the necessary ledger if a product-mixture handoff is specified and gives an exact contraction mechanism for reviewers to reuse; it does not close C019, C024, C018 or full FEI.
