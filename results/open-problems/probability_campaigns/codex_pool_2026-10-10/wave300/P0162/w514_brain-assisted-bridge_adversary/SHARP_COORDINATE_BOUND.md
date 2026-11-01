# Exact logarithmic coordinate cost: author derivation, pending referee

2026-10-10, P0162/w514. Base-2 entropy, uniform cube measure. Derived after reading the math brain's full unverified card claim_d15d0160e58b4c9183707be9f49462d2, which states the upper bound with a positive influence threshold. Its memory is a lead; the argument below is a separate derivation. No novelty claim or general FEI solution is made.

Let f:{-1,1}^d->{-1,1}, let i be a coordinate, g=f|_{x_i=+1}, h=f|_{x_i=-1}, and p=I_i(f). Define Delta_i(f)=H(f)-(H(g)+H(h))/2. Then

0 <= Delta_i(f) <= h_2(p)+(2/ln 2)p <= p log_2(1/p)+(3/ln 2)p.

The last expression is interpreted as zero at p=0. For p>0, the additive constant 3/ln 2 is optimal for an upper bound of the form Delta_i(f)/p <= log_2(1/p)+B holding for every Boolean f and every coordinate i:

sup_{d,f,i:p>0} [Delta_i(f)/p-log_2(1/p)] = 3/ln 2.

Proof of the upper bound. Write a_S=hat(g)(S), b_S=hat(h)(S), m_S=(a_S^2+b_S^2)/2, and q_S=(a_S-b_S)^2/(4m_S) when m_S>0. The f coefficients at S and S union {i} are (a_S+b_S)/2 and (a_S-b_S)/2. Thus m is a probability law, q_S in [0,1], and sum_S m_S q_S=p. Grouping those two coefficients gives

H(f)=H(m)+sum_S m_S h_2(q_S),
Delta_i(f)=JS_2(a^2,b^2)+sum_S m_S h_2(q_S).

JS_2(P,Q)=H((P+Q)/2)-(H(P)+H(Q))/2 is the Jensen-Shannon divergence in bits. Both terms are nonnegative. Concavity gives sum m_S h_2(q_S)<=h_2(p).

For probability laws P,Q, JS in natural units satisfies

JS_e(P,Q) <= (1/2)sum_S (sqrt(P_S)-sqrt(Q_S))^2.

Here is a scalar proof, rather than an appeal to an unstated comparison theorem. For x,y>=0, divide the desired pointwise inequality by (x^2+y^2)/2, omitting the zero pair. Put w=|x^2-y^2|/(x^2+y^2). It becomes

D(w):=((1+w)ln(1+w)+(1-w)ln(1-w))/2 <= 1-sqrt(1-w^2).

Both sides vanish at w=0. For 0<=w<1, the derivative of the right side minus the left side is w/sqrt(1-w^2)-atanh(w), which is nonnegative: its derivative is (1-w^2)^(-3/2)-(1-w^2)^(-1)>=0 and its value at zero is zero. Continuity covers w=1. Multiplying back and summing proves the comparison. Therefore

JS_2(a^2,b^2) <= (1/(2 ln 2))sum_S (|a_S|-|b_S|)^2
               <= (1/(2 ln 2))sum_S (a_S-b_S)^2
               = (2/ln 2)p.

Finally -(1-p)ln(1-p)<=p for p in [0,1], with endpoint conventions, so h_2(p)<=p log_2(1/p)+p/ln 2. No Fourier independence or multiplication of conditional bounds appears.

Proof of optimality of the additive constant. Use F from BENT_SELECTOR.md, n=2m>=4, p=2^{-n}, r=sqrt(p), and its L(u). For each fixed u, Taylor expansion at z=1 gives

phi(1+v)=(2v+3v^2)/ln 2+O(v^3),
L(u)=(3u^2-2u)p/ln 2+O(p^{3/2}).

The remainder is uniform for u in [0,2] once r<=1/4, because phi has a bounded third derivative on [1/2,3/2]. Consequently

Delta_t(F)/p-n = [L(2)/2-L(1)]/p -> 3/ln 2.

Since n=log_2(1/p), these Boolean witnesses attain the upper constant in the supremum limit. Finite numerical instances are diagnostics only; the analytic limit proves optimality.

Threshold reduction (C005). Fix 0<tau<1. If H(f)<=C_tau I(f) for every Boolean f whose coordinate influences are all below tau, with C_tau independent of d, then general FEI follows with C=max(C_tau,log_2(1/tau)+3/ln 2). Split any node with a coordinate influence at least tau and apply the upper bound at that node. Stop at functions whose influences are all below tau. Restrictions decrease the dimension, so the stopping tree is finite. The exact identity I(f)=(I(g)+I(h))/2+I_i(f) and the entropy increment inequality inductively yield the bound with this same C, including constant leaves with H=I=0. The converse is immediate. This proves a reduction; it does not establish the assumed low-influence estimate.

Most important checks requested of w515: all zero-mass/end-point cases in the JS calculation; signed coefficients in the Hellinger comparison; factor 4 in sum(a-b)^2=4p; base-2 conversion; the Taylor remainder and supremum quantifiers. Independently check C002's sign counts and convexity too. C005 is conditional, and its fixed tau cannot depend on dimension.
