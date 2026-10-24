# Directional exponential-moment upgrade of the complete finite-scale tail

Draft conditional deduction, w382, 2026-10-10. Independent referee required: w383. This is not a solution of P0110 and is not a global exponent claim.

Use w381 L1--L5's exact assumptions and notation: fixed d>=2, iid edge weights in [a,b] with 0<a<b<infinity, g the time-constant norm, rho=min_{|u|=1}g(u)>0, u a minimizing unit vector, v_n nearest-integer rounding of nu for integer n>=sqrt(d), L_n=|v_n|, C=(b/a)sqrt(d), K0=bd/2+rho sqrt(d)/2, and D_n the largest distance to [0,v_n] over all minimizing paths. Suppose q>=0, alpha>0, K>=1 and, for every nonzero lattice w, E exp(alpha |T(0,w)-h(w)|/|w|^q)<=K. Also suppose B_n=h(v_n)-g(v_n)<=H n^q log(2+n) with a finite H>=0. All constants are fixed in n.

Let A_n=2|{z in Z^d: ||z||_1<=(b/a)||v_n||_1}|+1 and Q_n=((C+1)L_n)^q/alpha. L5 gives, for each t>=0,

P(D_n>sqrt(U_n+V_n t))<=exp(-t),

where U_n=C L_n (B_n+K0+3 Q_n log(A_n K))/(2rho) and V_n=3 C L_n Q_n/(2rho)>0. This is obtained by taking s=Q_n(log(A_n K)+t). The logarithm is nonnegative because A_n K>=1.

Set Y_n=((D_n-sqrt(U_n))_+)^2/V_n. Since sqrt(U_n)+sqrt(V_n t)>=sqrt(U_n+V_n t), P(Y_n>t)<=exp(-t). For a nonnegative random variable with this tail, the layer-cake identity gives E exp(Y_n/2) = 1+(1/2) integral_0^infinity exp(t/2) P(Y_n>t) dt <=2.

For every lambda>0 and r>(1+q)/2, D_n<=sqrt(U_n)+sqrt(V_n Y_n) and ab<=a^2/2+b^2/2 imply

E exp(lambda D_n/n^r) <= 2 exp(lambda sqrt(U_n)/n^r + lambda^2 V_n/(2 n^(2r))).

Indeed apply the elementary inequality with a=lambda sqrt(V_n)/n^r and b=sqrt(Y_n). Since L_n is comparable to n and A_n=O(n^d), U_n=O(n^(1+q) log(2+n)) and V_n=O(n^(1+q)). The right side is bounded uniformly in n for every fixed lambda and r>(1+q)/2. Hence the exponential upper wandering endpoint along this rounded support direction is at most (1+q)/2.

The strict epsilon in r is needed to absorb sqrt(log n); no endpoint claim is made. The proof uses the entire tail for all t, not only a family of polynomial-probability bounds at one threshold. It uses no independence, random conditioning or multiplication of conditional estimates. It gives neither a lower wandering endpoint nor uniform control in all directions. Independent referee w383 must check the new assertion before any theorem promotion.
