# C0135: reject the inconsistent clock inversion; state the actual transfer gate

Label: proof of an elementary inversion and a conditional process-transfer lemma, not a solution of Problem 6.4. Current literature status is unverified offline.

The earlier C0135-A001 says both that a clock has size m^2 log(m) and that its inverse is sqrt(t)/log(t), and later uses the different scale sqrt(t) log(t). These cannot be equivalent scales.

Let f(x)=x^2 log(x), x>=1. It is strictly increasing for x>1. If a deterministic increasing clock T_m is asymptotic to m^2 log(m), its generalized inverse is asymptotic to sqrt(2t/log(t)). Indeed put u(t)=sqrt(2t/log(t)). Then log(u(t))=0.5(log(t)+log(2)-log(log(t))), so f(u(t))/t tends to one. For every fixed eps>0, T_floor((1-eps)u(t))/t tends to (1-eps)^2<1 and T_ceil((1+eps)u(t))/t tends to (1+eps)^2>1, which brackets the inverse. Thus neither of the two scales in A001 follows from that clock. This is an arithmetic correction; it does not assert that the ERW clock has this asymptotic behavior.

For the actual process question, define S_k=max_{j<=k} X_j and a_n=sqrt(n) log(n). If for every finite T,

max_{k<=floor(nT)} |S_k-X_k| / a_n -> 0 in probability,

and S_floor(nt)/a_n converges in distribution in the Skorokhod J1 topology to a continuous process Y, then X_floor(nt)/a_n converges to Y in J1. The uniform norm bounds their J1 distance by using the identity time change; convergence in probability of this distance and the metric-space Slutsky lemma give the result. A uniform O_P(sqrt(n)) backtracking bound would suffice, since sqrt(n)/a_n=1/log(n) tends to zero.

The missing mathematical work is to establish the maximum limit and this UNIFORM backtracking bound under the precise weaker cookie assumptions. A diffusive backtracking assertion at one fixed time does not prove the uniform bound. No such estimate or removal of POS1 is claimed here.
