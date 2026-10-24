# P0218: Verified founding-rate bound at the critical immigration parameter

Label: proof; author checked only. Independent audit: PENDING w347.

In the Aldous-Huang max-influence city model on the unit square, with alpha=1, beta>0 and c0>0, let M_t be the number of cities and let their positive populations sum to t. With I(y,t)=c0*max_i N_i(t)*|y-x_i|^(-beta), a uniform new arrival founds a city with probability 1/(1+I(y,t)). Its conditional founding probability is at least 1/[2*(1+K*t*M_t^d)], where d=max(beta/2-1,0) and K=(2*pi)^(beta/2)*c0. Consequently almost surely liminf M_t/(log t)^(min(1,2/beta))>0. This includes the boundary beta=2 and beta<2 as well as beta>2.

Assumptions: The unit-square max-influence model defined above; alpha=1 and beta>0; A uniform arrival at each integer step and total population t; c0>0 is fixed

For u>0 the set {y:I(y,t)>u} is contained in the union of M_t disks, the ith having area pi*(c0*N_i/u)^(2/beta). Clipping to the unit square and disk overlap only reduce the area. Put q=2/beta>0. If q<=1, concavity gives sum_i N_i^q<=M_t^(1-q)*t^q. If q>=1, each N_i/t is in [0,1], so sum_i (N_i/t)^q<=sum_i N_i/t=1. Together these give sum_i N_i^q<=M_t^max(1-q,0)*t^q. Thus the area is at most pi*(c0/u)^q*M_t^max(1-q,0)*t^q. Choose u=K*t*M_t^max(beta/2-1,0). Substitution makes this bound exactly 1/2. On the complement, the founding chance is at least 1/(1+u). Integrating over the uniform arrival position yields the displayed lower bound. The new-city indicator changes M_t by one, while a join changes it by zero, so the conditional count-process lemma, whose proof also holds for d=0, applies. Its exponent 1/(d+1) is min(1,2/beta), giving the stated almost sure lower bound. The cached primary paper, Section 2, equations (1)-(3) and rules (i)-(ii), explicitly defines the max influence and founding probability and permits alpha=1.

Limits: This gives a lower logarithmic city-count order, not a matching upper bound, a limiting constant, or balanced city population sizes. Independent audit is pending.

Existing card: math:probability.core:open-problem-p0218-growth-exponents-in-the-spatial-city-formation-model
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:5300
