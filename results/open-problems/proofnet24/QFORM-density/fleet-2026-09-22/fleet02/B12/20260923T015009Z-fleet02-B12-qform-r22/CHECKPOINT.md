# fleet02/B12 early mathematical checkpoint

Programme QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. Run 20260923T015009Z-fleet02-B12-qform-r22. Execution WITHOUT_VERIFIED_BRAIN.

Let I,J be disjoint original-coordinate sets and M the I-by-J cross block of a quadratic form in independent real inputs with densities at most one. Define

Z2 = e2(M^T M) = sum_{|S|=|T|=2} det(M_{S,T})^2.

Weight each 2-by-2 minor by w_{S,T}=det(M_{S,T})^2/Z2 and let alpha_i=P_w(i in S). Repeating the completed volume-decoupling proof from RESULTS.md with e2 in place of e3 shows that, when every alpha_i<=1/2,

|phi(t)| <= 2*pi*sqrt(e)*|t|^{-1}*Z2^{-1/4}.

The completed Fourier-potential lemma at exponent 1/2 therefore gives

sup_s E |R-s|^{-1/2} <= 8*e^{1/4}*Z2^{-1/8}.

After a physical scalar square completion with pivot d!=0,

||p_Q||_infinity <= 8*e^{1/4}*|d|^{-1/2}*Z2^{-1/8}.

This uses the dependent Schur remainder directly and does not assert an independent convolution.

Dense-tail stability: suppose M0 has rank two, s2(M0)>=a>0, and its left-range projection P0 has max diagonal <=1/4. If M=M0+F and ||F||op<=delta<=a/7, put sigma=a-delta and r=delta/sigma<=1/6. For final squared singular values x_m, the 2-volume singular-direction inclusion probabilities are p_m=x_m(E1-x_m)/E2. Weyl gives x1,x2>=sigma^2 and x_m<=delta^2 for m>=3. Hence for m>=3,

E2 >= x1*x2 + (x1+x2)*sum_{l>=3,l!=m}x_l >= (sigma^2/2)*(E1-x_m),

so p_m<=2*r^2. If P is the final top-two left singular projection, then (I-P0)M0=0 implies ||(I-P0)U2||op<=r and therefore sqrt(Pii)<=sqrt((P0)ii)+r. Thus

alpha_i <= Pii + 2*r^2 <= (1/2+1/6)^2 + 2*(1/6)^2 = 1/2.

Consequently the final dense-perturbed block satisfies

sup_s E |R-s|^{-1/2} <= 8*e^{1/4}/sqrt(a-delta).

The perturbation may have arbitrary rank. It is used only to verify a certificate on the final matrix, not as a uniformly small random quadratic term on unbounded inputs.
