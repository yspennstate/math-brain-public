# Exact bridge checkpoint (own deductions; independent check pending)

Use the notation and uniform Boolean assumptions of STATEMENT.md. Split f on coordinate i and write a_S=hat(f+)(S), b_S=hat(f-)(S), P_S=a_S^2, Q_S=b_S^2, R_S=(P_S+Q_S)/2. All are indexed by subsets of the remaining coordinates. P,Q,R are probability distributions. For R_S>0 set q_S=(a_S-b_S)^2/(2(a_S^2+b_S^2)); zero-weight terms are zero. Let h be binary entropy in bits and t=I_i(f)=sum_S (a_S-b_S)^2/4=sum_S R_S q_S.

Direct entropy chain rule gives, exactly,

Delta_i(f)=H(f)-(H(f+)+H(f-))/2 = JS(P,Q)+B_i(f),
JS(P,Q)=H(R)-(H(P)+H(Q))/2,
B_i(f)=sum_S R_S h(q_S).

Proof: parent squared coefficients without/with i are (a+b)^2/4 and (a-b)^2/4, with common marginal R. Thus H(f)=H(R)+sum R h(q). Subtract average child entropy. Jensen-Shannon divergence is nonnegative. Consequently B <= Delta. In particular Delta is not identically B.

Own two-variable witness: f(x,z)=x when z=+1 and 1 when z=-1. Both restrictions are characters/constants, with disjoint single-atom Fourier spectra. Four parent squared coefficients equal 1/4: H(f)=2, average child entropy=0, t=1/2, B=1, JS=1. Any quoted identity Delta=B fails on this Boolean witness.

Rare-switch construction: on m=2k binary bits, g(x)=(-1)^(sum_{j=1}^k x_(2j-1)x_(2j)), with the usual Walsh characters (-1)^(S dot x). Let h=g-2*1_{x=0}; g(0)=1, so h is Boolean. Let F(x,z)=g(x) for z=+1 and h(x) for z=-1. The new coordinate has t=2^-m. Product of k two-bit Walsh transforms gives |ghat(S)|=2^-k for every S. Parent coefficients are ghat(S)-2^-m without z and 2^-m with z. Put N=2^m, epsilon=N^-1/2. The marginal R_S=(sigma_S epsilon-epsilon^2)^2+epsilon^4 >= epsilon^2/2 for k>=1, so q_S=epsilon^4/R_S <=2/N. Hence

B_z(F) >= sum_S R_S q_S log2(1/q_S) >= (m-1)/N,
Delta_z(F)/I_z(F) >= m-1.

This is a proof for all k, conditional only on the explicitly proved flat Walsh transform. It refutes a universal bound for every arbitrary splitting coordinate. It does not refute FEI, nor the existence of a good coordinate. No monotonicity is claimed for this construction. Exact source comparison and independent referee review remain pending.

Single hardest remaining piece: prove a dimension-free conditional entropy charge B_i <= K I_i for a suitable coordinate at every recursive restriction, or an amortized complete-tree analogue. Bounding B_i by h(I_i) retains the logarithmic loss and does not close the conjecture.
