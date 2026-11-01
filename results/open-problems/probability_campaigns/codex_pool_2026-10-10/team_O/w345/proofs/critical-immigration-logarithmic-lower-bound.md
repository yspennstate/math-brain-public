# P0218: Logarithmic city-count lower bound under the earlier founding-rate estimate

Label: proof; author checked only. Independent audit: PENDING w347.

Let (M_t) be an adapted nondecreasing integer process, t>=1, with M_1>=1, whose increments are zero or one. Suppose P(M_(t+1)=M_t+1|F_t)>=1/[2(1+K*t*M_t^d)] for constants K>0,d>=0. Then constants kappa,c>0 exist such that, for all large integer t, P(M_t<floor(kappa*(log t)^(1/(d+1))))<=exp(-c*(log t)^(1/(d+1))). Moreover almost surely liminf M_t/(log t)^(1/(d+1))>0. For the verified alpha=1, beta>0 city model, d=max(beta/2-1,0), giving exponent min(1,2/beta).

Assumptions: Adapted city-count process with increments in {0,1}; The displayed conditional founding-rate bound at every step; K>0 and d>=0

Set m=floor(kappa*(log t)^(1/(d+1)))>=1. Before M reaches m, the founding chance at step s is at least a_s=1/[2(1+K*s*m^d)]>=1/[2(1+K)*s*m^d] for s>=1. Using independent uniforms to realize the adapted Bernoulli increments, compare with independent Bernoulli(a_s) variables until the threshold; after the threshold extend the comparison success variables arbitrarily. If M_t<m then the threshold was never reached, so the sum B of comparison successes from s=1 to t-1 is smaller than m. Its mean mu is at least H_(t-1)/[2(1+K)*m^d]. Choose kappa so kappa^(d+1)<=1/[16(1+K)]. For large t the harmonic sum is at least (log t)/2, implying mu>=4m and mu is bounded below by a positive multiple of (log t)^(1/(d+1)). The Chernoff lower-tail bound P(B<=mu/2)<=exp(-mu/8) proves the probability assertion. For the almost sure statement use t_j=ceil(exp(j^(d+1))) and sum the bounds exp(-c*j). Borel-Cantelli gives the lower bound eventually on these times. Monotonicity of M_t and log(t_(j+1))/log(t_j)->1 interpolate it to all large t.

Limits: The primary model definition and the spatial founding-rate bound are checked in max-influence-city-founding-rate.md, so the lemma supplies an almost-sure lower bound for the alpha=1, beta>0 Aldous-Huang model. It gives no matching upper bound or comparable city populations.

Existing card: math:probability.core:open-problem-p0218-growth-exponents-in-the-spatial-city-formation-model
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:5300
