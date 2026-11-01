# C0057: Discovery from a divergent conditional survival compensator

Label: proof; author checked only. Independent audit: PENDING w347.

Let T>=1 be an integer-valued stopping time for a filtration (F_n), possibly infinite, and set p_n=E[1_{T=n+1}|F_n] and A_m=sum_(n<m) p_n. Then P(T=infinity and A_infinity=infinity)=0. For countably many targets this implies almost sure discovery of all targets if each target's compensator diverges on its never-discovered event outside a null set. Divergence is a sufficient condition, not a necessary one.

Assumptions: T is a stopping time relative to the actual exploration history; p_n are actual target-specific conditional probabilities; The countable application verifies divergence separately on each survival event

Because p_n=0 after T, Z_m=1_{T>m} exp(A_m) is a nonnegative supermartingale with Z_0=1: its conditional next expectation is Z_m*(1-p_m)*exp(p_m)<=Z_m. For K>0 stop at sigma_K=inf{m:A_m>=K}. Bounded optional stopping at sigma_K wedge r gives P(sigma_K<=r,T>sigma_K)<=exp(-K). Let r increase, and then K increase, to obtain the result. The countable-target conclusion follows by a countable union of null sets. If deterministic a_n in [0,1] satisfy p_n>=a_n on {T>n}, the direct recursion P(T>n+1)<= (1-a_n)P(T>n) gives the product tail bound and hence P(T>m)<=exp(-sum_(n<m)a_n). For a_n=c/(n+1), 0<c<=1, this is at most (m+1)^(-c). Necessity fails when T=1 deterministically, since A_infinity=1 although discovery is certain.

Limits: For filled-in peeling, the lower bound by a perimeter-only q(S_n) and the divergence for all critical weight sequences are still required. The earlier unreviewed equivalence is not imported as a theorem.

Existing card: math:probability.planarmaps:open-problem-c0057-filled-in-peeling-discovers-the-whole-map-for-every-critical-weight-se
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:4364
