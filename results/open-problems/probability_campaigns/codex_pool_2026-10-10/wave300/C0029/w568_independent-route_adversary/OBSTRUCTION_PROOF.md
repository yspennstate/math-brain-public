Independent scalar obstruction, C0029, 2026-10-10. Author derivation; w569 review pending.

This result concerns logical consequences of scalar estimates. It is not a construction of iid Bernoulli matrices, and F below is a limiting reference CDF, not the finite-n Gaussian matrix CDF in Sah--Sahasrabudhe--Sawhney Theorem 1.2.

For t>=0 let F(t)=1-exp(-t-t^2/2), and set F(t)=0 for t<0. For positive integer n define

eta_n=(log(n+e))^(-1/16), a_n=exp(-sqrt(n)), q_n=2^(-n), m_n=eta_n F(a_n)/2,

H_n(t)=(1-m_n)F(t)+m_n 1_{t>=a_n},

G_n(t)=q_n+(1-q_n)H_n(t) for t>=0, and G_n(t)=0 for t<0.

Claim: G_n is a probability CDF, G_n(0)=2^(-n), and, uniformly in t>=0,

|G_n(t)-F(t)| <= (eta_n/2)F(t)+q_n,

G_n(t) <= (3/2)t+q_n.

For each fixed d>0 there exists N_d such that G_n(t)<=t for all n>=N_d and all t>=n^(-d). For each fixed k>0, G_n(t)<=t+(3/2)exp(-min{k,log(2)}n) whenever 0<=t<=exp(-kn). Yet for every sufficiently large n,

G_n(a_n)-a_n >= eta_n a_n/16.

Consequently no constants C,c>0 give G_n(t)<=t+C exp(-cn) for every sufficiently large n and all t>=0.

Proof. F is a CDF: F(0)=0, F'(t)=(1+t)exp(-t-t^2/2)>0, and F tends to one. The parameters satisfy 0<eta_n<1, 0<m_n<1/2, and 0<q_n<=1/2. G_n is the mixture of F, the point mass at a_n, and the point mass at zero with weights (1-q_n)(1-m_n), (1-q_n)m_n, and q_n. The weights sum to one. Right continuity includes the jump at t=a_n; the claimed lower bound uses the <= event.

Write D(t)=t-F(t) and h(t)=(1+t)exp(-t-t^2/2). Then D'(t)=1-h(t), h(0)=1, and h'(t)=-(2t+t^2)exp(-t-t^2/2). Thus D>=0, so F(t)<=t for all t>=0. For 0<=t<=1, two integrations, using exp(-3/2)<=exp(-u-u^2/2)<=1, give

exp(-3/2)t^3/3 <= D(t) <= t^3/3+t^4/12 <= t^3/2.                 (1)

If 0<=t<a_n, G_n(t)-F(t)=q_n(1-F(t))-(1-q_n)m_n F(t). This lies between -(eta_n/2)F(t) and q_n. If t>=a_n, the difference is [q_n+(1-q_n)m_n](1-F(t)), which is nonnegative and at most q_n+(eta_n/2)F(t), since F(a_n)<=F(t). This proves the uniform comparison and the (3/2)t+q_n bound.

Always G_n(t)<=F(t)+q_n+m_n. Since m_n<=a_n/2, for every fixed d>0 one has q_n+m_n<=exp(-3/2)n^(-3d)/3 for all sufficiently large n depending on d. Equation (1) then gives G_n(t)<=t for n^(-d)<=t<=1. For t>=1 the same claim follows from G_n(t)<=1. This proves the polynomial-scale assertion with its correct order of quantifiers: d is fixed before choosing N_d. It does not assert a threshold valid uniformly in a growing d.

If t<=exp(-kn), the coarse bound gives G_n(t)<=t+t/2+q_n<=t+(3/2)exp(-min{k,log(2)}n), proving the separate exponential-scale assertion.

For large n, a_n<=1/2 and a_n^2<=eta_n/8. Equation (1) gives F(a_n)>=a_n/2; also 1-F(a_n)>=1-a_n>=1/2. Hence

H_n(a_n)-a_n = -D(a_n)+m_n(1-F(a_n))
                 >= -a_n^3/2+eta_n a_n/8
                 >= eta_n a_n/16.

Since G_n=H_n+q_n(1-H_n)>=H_n, this proves the excess lower bound. For any fixed C,c>0, its ratio to C exp(-cn) is at least eta_n exp(cn-sqrt(n))/(16C), which tends to infinity. This proves the obstruction.

Application to proof auditing. Exact coefficient one at polynomial scales, an exponentially small singular mass, a constant-factor all-scale bound, and vanishing relative error to a limiting hard-edge law do not close the intermediate window by themselves. The earlier C0029-A001 route did not produce an explicit countermodel; this lane supplies one. The law above even has exact coefficient one at every fixed polynomial threshold, while failing every exponential-remainder conclusion at exp(-sqrt(n)).

A sufficient missing matrix premise would be a uniform ONE-SIDED comparison P_n(t)<=Q_n(t)+C exp(-cn) in the remaining window, where P_n is the Bernoulli lower-tail CDF and Q_n is the actual finite-n real Gaussian lower-tail CDF. The established Gaussian inequality Q_n(t)<=t then completes that route. Alternatively the positive comparison error must be bounded by t-Q_n(t) plus an exponential remainder. A two-sided error of order eta_n t has neither sign nor the required size. No such Bernoulli-specific premise is proved here.
