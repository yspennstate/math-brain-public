# A sharper defect-spectrum information charge

All logarithms are base two. The universal FEI conjecture remains open.

## 1. Exact polynomial certificate

Let P(000)=9/16 and P(x)=1/16 otherwise. This is the squared Fourier law of the Boolean function negative only at 000 on three physical bits. Its single-bit marginal is mu=(3/4,1/4), influence is 3/4, and total correlation is tau=2-(9/8)log2(3).

For all u,v>=0,

  F(u,v)=16(3u^7+v^7)^12-[8u^12+(u^4+v^4)^3]^7 >= 0.       (1)

Here is a finite exact certificate valid on the entire quadrant, rather than a sample. Write F(u,v)=sum_{j=0}^{84}c_j u^j v^(84-j). Then

 c_j=16*1[7 divides j]*binom(12,j/7)*3^(j/7)
     -sum_{k0+k1+k2+k3=7,4(k1+2k2+3k3)=j}
       7!/(k0!k1!k2!k3!)*3^(k1+k2)*9^k3.

Let A_k=sum_{j=k}^{84}binom(j,k)c_j and B_k=sum_{j=k}^{84}binom(j,k)c_(84-j). The complete integer arrays in out/scalar.json certify A_k>=0 and B_k>=0 for every k=0,...,84. Two separate implementations reconstruct them, one by convolution and one by direct multinomial coefficients and Horner translation; neither reads the other's results as premises. Therefore

 F(v+w,v)=sum_k A_k w^k v^(84-k)>=0,
 F(u,u+w)=sum_k B_k w^k u^(84-k)>=0

for u,v,w>=0. These cones cover the quadrant, including axes and origin. This proves (1) by a fully specified exact certificate. No real root finding or floating-point sign is used.

Set x=u^4,y=v^4 and take nonnegative seventh roots. Equation (1) says

 8x^3+(x+y)^3 <= 16[(3x^(7/4)+y^(7/4))/4]^(12/7).          (2)

For three nonnegative functions f_i with values x_i,y_i, two-term Holder yields

 E_P product_i f_i = [8 product_i x_i+product_i(x_i+y_i)]/16
 <= product_i[8x_i^3+(x_i+y_i)^3]^(1/3)/16
 <= product_i (E_mu f_i^(7/4))^(4/7).                     (3)

Holder follows by normalizing the three two-vectors in l3 and summing abc<=(a^3+b^3+c^3)/3. A zero norm makes the inequality immediate. Independent blocks tensorize (3) for P_r=P^tensor r over its 3r individual coordinates, since each f_i depends only on its own coordinate.

## 2. Entropy dual and complete mixture posterior

For ANY law R on the 3r bits, choose f_i=(R_i/mu)^(4/7). Each factor on the right of (3) is one. F=product f_i is positive on supp R and E_(P_r) F>0, because P_r has full support. KL to the normalized tilted law P_r F gives

 D(R||P_r)>=E_R log F-log E_(P_r)F
             >=(4/7)sum_i D(R_i||mu).

Thus sum_i D(R_i||mu)<=(7/4)D(R||P_r). Degenerate R is included: zero marginal entries occur only outside its occupied support. For any finite auxiliary J coupled to X~P_r, average this inequality over its posteriors to get

 sum_i I(X_i;J)<=(7/4)I(X;J).                             (4)

Let Q(x)=sum_j w_j product_i q_ji(x_i), with at most M positive-weight components, and suppose Q>0 on supp P_r. Use the exact posterior k(j|x)=w_j product_i q_ji(x_i)/Q(x), joint L=P_r k, posterior weights v, and R_j=L(X|J=j). Direct expansion gives

 D(P_r||Q)=TC_L(X|J)+D(v||w)
             +sum_j v_j sum_i D((R_j)_i||q_ji).

Also TC_L(X|J)=r*tau-sum_i I(X_i;J)+I(X;J). Together with (4),

 D(P_r||Q)+(3/4)I_L(X;J)>=r*tau,                         (5)
 D(P_r||Q)>=max(0,r*tau-(3/4)H_L(J))
             >=max(0,r*tau-(3/4)log2 M).                 (6)

All reference-only mass and mixture normalizers remain. Infinite divergence gives the lower bound trivially without defining posteriors on absent atoms. At r=0 this reduces to KL nonnegativity. Redundant independent latent labels do not change (5). The information is under the exact posterior joint L, not the mixture prior. No latent capacity has been priced from physical influence by this argument.

## 3. The endpoint 5/3 fails, strictly

The quadratic perturbation guard in A032 excludes coefficients below 5/3; it does not exclude equality. Equality also fails. Set x=10^3,y=11^3 and A=8x^3+(x+y)^3. Exact integers give

 A^5>4(3*10^5+11^5)^9.                                  (7)

The complete integers are saved, and independently recomputed. This is the failure of the scalar Holder inequality at p=5/3. It is also an explicit entropy-dual witness: put R(s)=P(s)x^(3-|s|)y^|s|/(A/16). For p=5/3 and Z=E_P product_i f_i, the variational inequality on each marginal gives

 sum_i D(R_i||mu)-p D(R||P)
 >=p log Z-sum_i log E_mu f_i^p >0

by (7). Hence the optimal coefficient c for sum_i D(R_i||mu)<=c D(R||P) lies strictly above 5/3 and at most 7/4. This R is a probability-law dual witness, not a claimed Boolean spectrum. The input P is independently Boolean-realized. The optimal c inside this interval is not determined.

## 4. Full physical energy and both terminals

For actual Boolean g equal to r disjoint three-bit defects, use h=z1*z2*z3*g and the existing complementary controller

 a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1), b=1-a^2,
 beta=E b^2=3/8, G_sigma=a+sigma*b*h.

Query z1. Both physical children retain tags z2,z3, so the vacuum Fourier sector and tagged sector remain disjoint. Direct expansion gives unchanged controller vacuum coefficients ahat(U)^2 and tagged masses bhat(U)^2 P_r(S). Squared child spectra agree, deletion is injective on occupied sets, and erasure, JS, singleton credit and phase-bin credit are zero. Query influence is beta. Replacing ONLY the core law in the complete children by Q_plus,Q_minus costs exactly

 erasure+mean CE_child-CE_parent=beta*mean D(P_r||Q_sigma).

Therefore (5) applies separately to BOTH full terminals:

 mean bill+(3 beta/4)*mean I_(L_sigma)(X;J)>=beta*r*tau.

For M-component children the bill is at least beta*max(0,r*tau-(3/4)log2 M). Multiply the entire account by the physical reach eta at a subtree. All old bookings and complementary terminals stay in the same original account; no reserve is renewed. Actual full influence is 23/8+9r/32 and entropy is 5-(9/16)log2(3)+(3r/8)[4-(9/8)log2(3)]. Thus this is not an FEI counterfamily, and a product-mixture handoff is necessary only within the declared target class. Free inherited continuation does not incur this optional bill.

The actual conditional auxiliary entropy also remains explicit. With U the controller frequency and V the tag/core frequency, let m(U)=ahat(U)^2+bhat(U)^2. Then

 H(V|U)=c_aux+beta H(g),
 c_aux=sum_U m(U) h2(bhat(U)^2/m(U))
       =5-(9/16)log2(3)-H(m).

Terms with m(U)=0 contribute zero. The physical auxiliary influence is beta[3+I(g)], and controller influence is 7/4. Thus neither conditional auxiliary entropy nor phase-realization energy is removed in obtaining (5).

## 5. Independent review and universal boundary

A032-ISOSPECTRAL-CORE-BOUNDED-MIXTURE-OBSTRUCTION@2 is valid at its stated scope. Its degree-six identity, Holder step, posterior entropy dual, complete KL identity, tensorization and full physical handoff reconstruct without repair. The 7/4 certificate is a separate strengthening of its coefficient 2; it does not refute version 2. Our preceding duplicated-core coefficient-one log M theorem concerns a different family and is not substituted into this unduplicated source.

First unsupported universal line: an influence-priced ORIGINAL reference family for arbitrary Boolean cores, closed under actual physical inherited marginals, or an intrinsically useful REQUIRED compatible handoff paid from the actual same unused original account. Neither (5) nor the exact failure of 5/3 supplies that source. Conditioning an arbitrary spectral history need not preserve P_r, so the contraction may not be reissued at descendants without its hypotheses. Full FEI, initial arbitrary-core payment and independent acceptance of this new coefficient remain open.
