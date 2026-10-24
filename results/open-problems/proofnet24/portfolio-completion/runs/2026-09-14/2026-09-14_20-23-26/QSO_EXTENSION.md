# Parent candidate: quantitative constructive uniqueness for four-type QSO

UNVERIFIED WORKING DERIVATION, for independent audit. See agents/006.md for original fixed-point proof.

Strictly non-Volterra: P_ij,k=P_ji,k >=0, sum_k P_ij,k=1, P_ij,i=P_ij,j=0. V_k(x)=sum_ij P_ij,k x_i x_j. Let c=(3-sqrt(5))/2. Every fixed point has x_i <= (1-x_i)^2, hence x_i <= c.

For q in [c,1/2), K_q={x in simplex: x_i<=q}. For 0<lambda<=min(q,1/2), T_lambda=(1-lambda)I+lambda V preserves K_q: component upper bound f(s)=(1-lambda)s+lambda(1-s)^2 is convex on [0,q], and f(0)=lambda<=q, f(q)<=q.

Claim: T_lambda is an l1 contraction on K_q with factor L=max(1-lambda+2lambda q,2lambda)<1. At m=(x+y)/2 define A_kj=sum_i P_ij,k m_i, so V(x)-V(y)=2A(m)(x-y), A is nonnegative column stochastic, zero diagonal. B=(1-lambda)I+2lambda A has column sum 1+lambda. On zero-sum vectors its induced l1 norm is max_{i,j} (1/2)||B e_i-B e_j||_1 = max_{G,i,j} sum_{k in G}(B_ki-B_kj).

For a subset G and i,j:
- If both i,j lie in G, or both outside, the identity cancels and stochasticity bounds group column difference by 2lambda.
- If i outside G and j inside, bound is -(1-lambda)+2lambda=3lambda-1 <=2lambda.
- If i inside and j outside, and G has size 1 or 3, the A group difference is <=0 by A_ii=A_jj=0 and column stochasticity. Bound is 1-lambda.
- If i inside and j outside and G has size 2, write other G index k and other complement index l, and p_ab=sum_{r in G} P_ab,r. Then p_ik=0,p_jl=1. Sum_a m_a(p_ai-p_aj) <= m_i(1-p_ij)+m_j p_ij <=q. Bound is 1-lambda+2lambda q.
This proves claim if all cases checked. Banach gives existence, uniqueness and geometric convergence from every point in K_q. Every fixed point already lies in K_c, so this covers entire simplex fixed-point uniqueness. Rational choice q=2/5,lambda=1/3 gives L=14/15.

Possible additional extension: For the ODE xdot=V(x)-x, K_q is invariant for q>=c, and an l1 Dini derivative argument with the sign cut gives contraction rate 1-2q inside K_q. Every trajectory enters K_q for q>c in finite time via scalar comparison x_i' <= (1-x_i)^2-x_i. Thus continuous dynamics globally converge. Needs independent proof; not claimed yet.

Discrete V itself need not converge (periodic orbits allowed). Do not conflate averaged iteration, continuous flow, or original discrete iteration.
