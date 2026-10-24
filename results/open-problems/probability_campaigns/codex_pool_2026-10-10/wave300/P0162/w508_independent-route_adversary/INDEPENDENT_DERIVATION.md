# Bent function with a one-point selector perturbation

Draft proof for independent review by w509. Saved before reading any w507 mathematical artifact. No novelty claim.

Let m >= 4 be even and N = 2^m. Identify the uniform sign cube with F_2^m and use Walsh characters (-1)^(s dot y). Put g(y) = (-1)^(y_1 y_2 + ... + y_(m-1) y_m). The normalized Walsh transform of each two-bit factor has values (1,1,1,-1)/2. By taking products, every coefficient u_s of g has magnitude A = N^(-1/2). Also g(0)=1, so sum_s u_s=1. The numbers of positive and negative coefficients are N_+ = (N+sqrt(N))/2 and N_- = (N-sqrt(N))/2.

Flip g at y=0: h = g - 2 1_{y=0}. This remains Boolean and its coefficient is v_s=u_s-2d, with d=N^(-1). Define the Boolean F(y,t) for t in {-1,1} by F(y,+1)=g(y) and F(y,-1)=h(y). Its coefficients without t are a_s=(u_s+v_s)/2=u_s-d and those with t are b_s=(u_s-v_s)/2=d. Consequently I_t(F)=sum_s b_s^2=1/N.

Define phi(z)=-z^2 log_2(z^2), with phi(0)=0. Then

Delta_t(F) := H(F) - (H(g)+H(h))/2
 = sum_s [phi(u_s-d) + phi(d) - (phi(u_s)+phi(u_s-2d))/2].

For m>=4, the intervals between u_s-2d and u_s avoid zero, since A>=4d. The central second-difference identity gives a point xi_s in that interval such that

phi(u_s-d) - (phi(u_s)+phi(u_s-2d))/2 = -(d^2/2) phi''(xi_s).

Here phi''(z)=-(2 ln(z^2)+6)/ln(2). Thus the summand equals

d^2 [log_2(xi_s^2/d^2) + 3/ln(2)].

Every xi_s satisfies A-2d <= |xi_s| <= A+2d. Dividing the sum by I_t(F)=N d^2 yields the explicit bounds

m + 2 log_2(1-2/sqrt(N)) + 3/ln(2)
 <= Delta_t(F)/I_t(F)
 <= m + 2 log_2(1+2/sqrt(N)) + 3/ln(2).

In particular Delta_t(F)/I_t(F) = m + 3/ln(2) + O(N^(-1/2)), and the ratio is at least m-2+3/ln(2). No universal C can make Delta_i(f) <= C I_i(f) hold for EVERY Boolean f and EVERY coordinate i.

Scope: this does not refute the existential choice of a good splitting coordinate, a condition imposed only at chosen tree nodes, or the global FEI conjecture. It refutes only the universal-coordinate version and a proof that needs that version. The exact spectra are fully Boolean; the obstruction does not discard f^2=1.

Remaining gap: the global FEI inequality and the existence of a dimension-free good-coordinate estimate are not proved. This draft requires w509's independent check before theorem promotion.

## Disjoint extension after reading w507: arbitrary sparse flip sets

The paired prover independently used the same one-point family, with a Jensen-Shannon argument. The following support-size extension uses the second-difference argument above; it does not repeat the prover's one-point calculation.

Let g be ANY Boolean bent function on m even bits, so every Walsh coefficient u_s has absolute value A=N^(-1/2). Let E be ANY nonempty set of K inputs, with 2K<sqrt(N). Set h=g(1-2*1_E), and define F by the same selector. Put b_s=widehat{g*1_E}(s), so v_s=u_s-2b_s, the two F coefficients are u_s-b_s and b_s, and epsilon=I_t(F)=K/N. Define r_s=b_s^2/epsilon, a probability distribution on the nonzero b_s, and theta=2K/sqrt(N)<1.

Triangle inequality gives |b_s|<=K/N and hence r_s<=K/N. Therefore H(r)>=log_2(N/K). For b_s!=0 the central second-difference identity applies on the segment [u_s,u_s-2b_s], which avoids zero because 2|b_s|<=theta A<A. Its intermediate point xi_s satisfies A(1-theta)<=|xi_s|<=A(1+theta). The same entropy calculation yields

H(r)-log_2(K)+2log_2(1-theta)+3/ln(2)
 <= Delta_t(F)/I_t(F)
 <= H(r)-log_2(K)+2log_2(1+theta)+3/ln(2).

Indeed sum_s r_s log_2(xi_s^2/b_s^2) differs from sum_s r_s log_2(A^2/b_s^2)=H(r)-log_2(N epsilon)=H(r)-log_2(K) by a weighted term between 2log_2(1-theta) and 2log_2(1+theta). Zero b_s give exactly zero contribution and are omitted. Parseval gives sum_s b_s^2=E[g^2 1_E]=K/N.

The support-size consequence is the self-contained lower bound

Delta_t(F)/I_t(F) >= log_2(N/K^2)+2log_2(1-2K/sqrt(N))+3/ln(2).

For K<=sqrt(N)/4 this is at least log_2(N/K^2)-2+3/ln(2). Thus K fixed, or K<=N^(1/2-delta) for any fixed delta>0 and sufficiently large even m, produces an unbounded selector charge for EVERY choice of E with that size. No sign or independence hypothesis on E is needed.

Scope is still the universal-coordinate inequality only. The distribution r is derived from an actual Boolean perturbation, not chosen arbitrarily. This extension is a draft pending w509 review; no novelty or general FEI claim.
