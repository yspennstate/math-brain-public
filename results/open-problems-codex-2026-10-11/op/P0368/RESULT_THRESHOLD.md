# Threshold insertion for the MBBT (2026-10-12)

Let rho = (1/2)Lebesgue[0,1] + (1/2)delta_infinity. For a coupling mu of rho with itself write F(r,s)=P(Y<=r or Y*<=s). The source's Lemma 20, equation (2.11), gives

2(F_T-F) = -F(r,s)^2 + (r^2+s^2)/4 + integral_0^min(r,s) [F(r,s)-F(t,s)-F(r,t)+F(t,t)]dt =: R(F)(r,s).

For 0<=a<1 put c=1-a, L_a(t)=a+ct (and L_a(infinity)=infinity). Define the probability measure

A_a(mu) = (1/2) integral_0^a delta_(t,t) dt + c (L_a,L_a)_#mu + (a/2)delta_(infinity,infinity).

All summands are nonnegative; their masses sum to a/2+c+a/2=1. Its marginal is rho, since its finite density is 1/2 on each of [0,a] and [a,1], and its infinity mass is c/2+a/2=1/2.

Its union function G is max(r,s)/2 if min(r,s)<=a, and a/2+c F((r-a)/c,(s-a)/c) otherwise. For r<=s with r<=a, the integrand in R(G) is (t-r)/2, so R(G)=0. For a<r<=s set u=(r-a)/c, v=(s-a)/c. The integral over [0,a] is a*c*(F(u,v)-(u+v)/2)-a^2/4. The integral over [a,r] is c^2 times the original integral over [0,u]. Expanding the polynomial terms cancels every term involving a and leaves

R(G)(r,s)=c^2 R(F)(u,v).

This proves: every MBBT fixed point mu gives a fixed point A_a(mu). It also proves an exact conjugacy of the MBBT continuous evolution: if mu_h solves dmu_h/dh=T_chi(mu_h)-mu_h, then A_a(mu_(c h)) solves the same equation. The derivative of the upper-region union function is c^2 times that of F; the lower region is constant. Union functions and the fixed marginal determine the entire law, including mass at infinity, so equality here is equality of signed measures.

For the nontrivial scale-invariant coupling mu_* from Theorem 12 let k=F_*(1,1)>1/2. Then

G_a(t,t)=t/2 for t<=a; G_a(t,t)=t/2+(k-1/2)(t-a) for t>a.

Thus the couplings A_a(mu_*) are distinct for distinct a, and are not scale invariant for 0<a<1. Their threshold is recovered as the largest interval on which G_a(t,t)=t/2. At a=1 the limiting law is diagonal.

This is a proved construction for the MBBT, not a classification of all fixed points. Transfer to the oriented binary tree requires checking the source's bivariate transformation. No global domain-of-attraction assertion has yet been proved.
