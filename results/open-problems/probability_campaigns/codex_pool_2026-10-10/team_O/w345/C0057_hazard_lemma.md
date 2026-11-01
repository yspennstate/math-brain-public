# C0057: a sufficient exploration criterion, with the necessity claim removed

Label: proof, author checked; independent audit PENDING w347. This does not solve C0057.

The previous intake attempt (attempts.jsonl:46, C0057-A001) calls whole-map discovery equivalent to divergence of a conditional swallowing-hazard sum. Divergence is a sufficient condition along a never-swallowed history; it is not necessary. A vertex swallowed at the first step has hazard sum one.

Let (F_n) be a filtration and T an integer-valued stopping time with T>=1, the discovery time of one fixed target. Define p_n=E[1_{T=n+1}|F_n], which is zero on {T<=n}, and A_m=sum_{n<m} p_n. Then

    P(T=infinity and A_infinity=infinity)=0.

Proof. Z_m=1_{T>m} exp(A_m) is a nonnegative supermartingale starting at one, because E[Z_{m+1}|F_m]=Z_m (1-p_m) exp(p_m)<=Z_m. For K>0 let sigma_K=inf{m:A_m>=K}. Optional stopping at sigma_K wedge r gives E Z_{sigma_K wedge r}<=1. On {sigma_K<=r,T>sigma_K}, Z_{sigma_K wedge r}>=exp(K), so P(sigma_K<=r,T>sigma_K)<=exp(-K). Increase r to infinity. The event {T=infinity,A_infinity=infinity} is contained in {sigma_K<infinity,T>sigma_K} for every K. Let K tend to infinity to conclude. No independence and no stationary or regular-variation assumption is used.

If a countable family of targets has respective stopping times T_v, and for each v its compensator diverges on {T_v=infinity} outside a null set, then all targets are discovered almost surely, by the lemma and a countable union of null events. For peeling this requires an actual target-specific conditional hazard or a valid lower bound while that target survives. A perimeter-only function q(S_n) cannot be substituted until its lower-bound property has been proved for the exploration rule and the marked target.

Deterministic-rate corollary. If on {T>n}, p_n>=a_n for deterministic a_n in [0,1], then P(T>m)<=product_{n<m}(1-a_n)<=exp(-sum_{n<m}a_n). Thus a_n=c/(n+1), 0<c<=1, gives P(T>m)<=(m+1)^(-c); the harmonic sum is at least log(m+1).

Checks needed: T must be a stopping time; each p_n must condition on the same past; the lower bound must hold on survival histories; countability must cover all targets. The map-specific divergence estimate for arbitrary critical weight sequences remains unproved.

Source: ~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl:46. Short quote: "Whole-map discovery <=> sum_n q_{S_n} = infinity a.s." This quote records an unreviewed route, not an accepted theorem.
