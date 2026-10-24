# Parent derivation: uniqueness with controlled parental offspring probability

Candidate theorem for independent audit. This extends strict non-Volterra uniqueness to a larger four-type class; it is not yet promoted in the main note.

Let P be any four-type quadratic stochastic array (nonnegative, symmetric in its two parent indices, each pair's offspring probabilities sum to one). Assume
\[
\delta:=\max_{i,j}\sum_{k\in\{i,j\}}P_{ij,k}<1-\sqrt3/2.
\]
The set in this sum counts a repeated parent only once. No strict prohibition is assumed.

Put a=1-delta, d=sqrt(1+4a^2), r=(d-1)/(2a), q=1-r. Then c<=q<1-1/sqrt3<1/2, and q=delta+a(1-q)^2. Claim: V has a unique fixed point. For any0<lambda<=q, T=(1-lambda)I+lambda V is a contraction on K_q with factor
\[
L=1-\lambda(d-2)<1.
\]

Proof candidate:
1. V_i(x)<=g_delta(x_i):=(1-x_i)^2+delta[1-(1-x_i)^2]=delta+a(1-x_i)^2. Thus every fixed point lies in K_q by solving g_delta(s)>=s on[0,1]. The capped simplex is nonempty since q>=c>1/4.
2. T_i(x)<=f(x_i)=(1-lambda)x_i+lambda g_delta(x_i). Convexity on[0,q], f(0)=lambda<=q, f(q)=q establish invariance.
3. As before A(m)_kj=sum_i P_ij,k m_i is nonnegative column stochastic, but A_ii<=delta rather than0. For a 2+2 partition G,H and i inG,j inH, other indices k inG,l inH, p_ab=sum_{s inG}P_ab,s obey p_ki<=delta and p_lj>=1-delta. Hence
   alpha_i-alpha_j =sum_b m_b(p_bi-p_bj)
   <=m_i(1-p_ij)+m_j p_ij+delta(m_k+m_l)
   <=max(m_i,m_j)+delta(1-m_i-m_j)
   <=delta+(1-delta)q=:beta.
4. For singleton/triple separating cuts alpha_i-alpha_j<=delta<=beta. Same-side cuts still give at most2lambda; reversely separating cuts give3lambda-1. Thus the zero-sum l1 norm of B=(1-lambda)I+2lambda A is at most max{2lambda,1-lambda+2lambda beta}. Since beta>=q andlambda<=q<1/2, latter dominates: difference>=1-q(3-2q)=(1-q)(1-2q)>0.
5. beta=delta+a q=1-a r=(3-d)/2. Therefore latter equals1-lambda(d-2). Assumption delta<1-sqrt3/2 is exactly d>2. Banach gives unique fixed point inK_q, and every fixed point already lies there.

For delta=0 this recovers the original strictly non-Volterra theorem and its contraction. The threshold is a sufficient condition; no optimality claimed. At the threshold d=2 this argument gives only nonexpansion, not uniqueness.

Possible global convergence: scalar envelopes q0=1, q_{n+1}=f(q_n) decrease toq; f is increasing on[q,1] iflambda<=q and q*d<1 (needs algebraic check), and f'(s)<=1-lambda. This would give geometric cap approach and a global finite prefactor for rateL. Leave this additional claim unproved until checked.
