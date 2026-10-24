SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T20:31:05Z.
attacking: turn the fresh two-bank curved-tube estimate into a full rough-input interval theorem with one genuinely independent scalar hub, and isolate the exact b->0 overlap debt.

# Early calculation: dyadic tube-to-hub splice

Let H be independent of two independent R^3 banks A,B, with ||f_H||_infinity<=m. Put (L,V,P)=A+B and let K=K_2+K_3 be the bank-density currency in the proved two-bank curved-tube theorem at math-open-problems@5e23223ed8626d8df8343d2d26879c08cf139093. Thus for 0<r<=1 and b!=0,

P(r<=|L|<=2r, |bP+c+dL+(gamma+V^2)/(2L)|<=a)
 <= C_T a r^(3/2)|b|^(-1/2) K,

uniformly in c,d,gamma.

Consider

Q=2HL+2bLP+V^2+alpha L^2+beta L+gamma_0.

For an interval I of length h and center t, on r<=|L|<=2r the event Q in I implies

|H+bP+(alpha/2)L+beta/2+(gamma_0-t+V^2)/(2L)| <= h/(4r).

Conditioning only on H and using the tube theorem (whose constant is uniform in the translated c) gives

P(Q in I, r<=|L|<=2r)
 <= (C_T/4) h sqrt(r)|b|^(-1/2)K.                         (E1)

For 0<R<=1, decompose 0<|L|<=R into shells with r_k=R 2^(-k-1). Since sum_k sqrt(r_k)=(1+sqrt(2))sqrt(R),

P(Q in I, 0<|L|<=R)
 <= A_b h sqrt(R),
A_b=(C_T/4)(1+sqrt(2))K|b|^(-1/2).                       (E2)

On |L|>R, condition on (L,V,P). Q is affine in H with slope 2L, hence

P(Q in I, |L|>R) <= m h/(2R).                             (E3)

Therefore for every 0<R<=1,

P(Q in I) <= h [A_b sqrt(R)+m/(2R)].                      (E4)

If A_b>=m, the minimizer R=(m/A_b)^(2/3) lies in (0,1] and gives

P(Q in I) <= (3/2) A_b^(2/3)m^(1/3) h.                   (E5)

If A_b<m, take R=1 to get P(Q in I)<(3/2)m h. Hence

||p_Q||_(infinity,ess)
 <= (3/2) m^(1/3) max{m,A_b}^(2/3).                       (E6)

This is already a full-line rough-input density bound for every quantitative nonzero coupling b. It uses no moments, support or post-rotation independence. The only unresolved limit in this core is b->0 when P overlaps the same two product banks as (L,V); treating bP as a small random error is forbidden. The b=0 endpoint is separately controlled when the (L,V) projection has a bounded joint density, so the remaining issue is a punctured overlap-stability bridge, not loss of the endpoint itself.
