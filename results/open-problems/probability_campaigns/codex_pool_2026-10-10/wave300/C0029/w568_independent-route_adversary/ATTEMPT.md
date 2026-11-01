Independent route recorded 2026-10-10 before opening any w567 proof.

Target: for iid uniform {-1,+1} entries of an n by n real matrix B_n, bound P(s_min(B_n) <= t/sqrt(n)) by t plus a dimension-exponential remainder, uniformly for t >= 0. The exact coefficient one is essential. Current openness is UNKNOWN pending the scoped source/owner-status checks.

Method: construct a scalar distribution countermodel to the implication from near-one universality, exponential singularity, and exact polynomial-scale bounds to the all-scale constant-one conclusion. This is an independent obstruction to a proof strategy; it is not a Bernoulli matrix counterexample. No row-probability products, exchange-of-limits inference, or numerical proof is used.

Let F(t)=1-exp(-t-t^2/2), t>=0; extend F(t)=0 for t<0. This is a probability CDF. Let eta_n=(log(n+e))^(-1/16), a_n=exp(-sqrt(n)), q_n=2^(-n), m_n=eta_n F(a_n)/2. Define H_n(t)=(1-m_n)F(t)+m_n 1_{t>=a_n} and G_n(t)=q_n+(1-q_n)H_n(t) for t>=0, with G_n(t)=0 for t<0. This is the CDF of a mixture of F, an atom at a_n, and an atom at zero.

Candidate obstruction: for large n, G_n(0)=q_n, |G_n(t)-F(t)|<=eta_n F(t)+q_n uniformly for t>=0, G_n(t)<=2t+q_n, and for every fixed d>0, G_n(t)<=t for every t>=n^(-d) once n is large enough depending on d. Nevertheless G_n(a_n)-a_n>=eta_n a_n/16. Consequently there are no constants C,c>0 for which G_n(t)<=t+C exp(-cn) for all large n and all t>=0.

Derivation of the slack: write D(t)=t-F(t) and h(t)=(1+t)exp(-t-t^2/2). Then D'(t)=1-h(t), h'(t)=-(2t+t^2)exp(-t-t^2/2). For 0<=t<=1, integration gives exp(-3/2)t^3/3 <= D(t) <= t^3/3+t^4/12 <= t^3/2. The lower bound lets the polynomial-range cubic slack absorb q_n+m_n. The upper bound, F(a_n)>=a_n/2, and 1-F(a_n)>=1/2 yield H_n(a_n)-a_n >= -a_n^3/2+eta_n a_n/8 >= eta_n a_n/16 when a_n^2<=eta_n/8. Since G_n>=H_n, the same lower bound holds for G_n.

Remaining work: check every quantifier and boundary in this construction, identify exactly which local/core-proof premise it defeats, and obtain w569's independent mathematical review. The source comparison theorem is established literature; the obstruction lemma is an owner-own-work DRAFT until independently reviewed.
