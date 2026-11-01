# Clock-to-exit-count equivalence, without a stopping-time horizon

Claim CC (proved by w447; independent review pending).

Fix a uniformly elliptic nearest-neighbor kernel on Z^d with lower bound kappa>0. Let sigma_0=0. At the finite stopping time sigma_i choose a set S_i containing X_sigma_i, measurably from the history and environment. Keep S_i fixed until its first exit, and assume its escape radius is at most the deterministic integer r>=1. Define sigma_{i+1} to be that exit time. The S_i may overlap, and the choice may depend on the whole past. Write D_i=sigma_{i+1}-sigma_i and a=kappa^r.

For any integer-valued random horizon tau>=1 finite almost surely, even if tau depends on the future and is not a stopping time, put K_tau=min{m>=1:sigma_m>=tau}. Then

E tau < infinity  if and only if  E K_tau < infinity.

Moreover let B be any event of probability p>0 on which tau is finite, under a law obtained by averaging the uniformly elliptic kernels and their paths. The same equivalence holds under conditional expectation given B. No conditional Markov or iid assertion is made under B.

Proof. ER gives conditionally at sigma_i

P(D_i>mr | F_sigma_i, omega) <= (1-a)^m.

Thus ceil(D_i/r) is conditionally dominated by a geometric variable on {1,2,...} with success probability a. With lambda=a/(4r) we get

E(exp(lambda D_i) | F_sigma_i,omega)
 <= a exp(a/4)/(1-(1-a) exp(a/4)) <= 4/3.

For the last inequality use exp(a/4)<=1/(1-a/4); the geometric denominator is positive, since (1-a)/(1-a/4)<1. The formula is increasing in exp(a/4), and at 1/(1-a/4) it is exactly 4/3. Tower iteration at the actual sigma_i now proves

E exp(lambda sigma_m) <= (4/3)^m.

At each tower step exp(lambda sigma_i) is measurable with respect to F_sigma_i (which retains omega), so E[exp(lambda sigma_{i+1})] = E[exp(lambda sigma_i) E(exp(lambda D_i)|F_sigma_i)] <= (4/3) E[exp(lambda sigma_i)]. Induction proves the displayed bound. This is a conditional moment argument, not independence between episodes.

Let C=2 log(4/3)/lambda. For every integer m>=1,

P(tau>Cm | B)
 <= P(K_tau>m | B) + p^(-1) exp(-lambda C m)(4/3)^m
 = P(K_tau>m | B) + p^(-1)(3/4)^m.

Indeed if K_tau<=m then tau<=sigma_m, regardless of whether tau is a stopping time. The second term follows by an unconditional Chernoff bound followed by division by p ONCE. In the unconditioned case take B to be the whole sample space.

Put L=ceil(C). Tail summation in blocks of L, using the bound above, gives the explicit estimate

E[tau | B] <= L ( E[K_tau | B] + 3/p ).

For the reverse implication, every D_i>=1, so sigma_m>=m and K_tau<=tau pathwise. Therefore E[K_tau | B]<=E[tau | B]. The argument also applies if tau is only finite on B, by defining it arbitrarily off B and defining K accordingly there.

Application to the C0041 route. Fixed-size balls centered at successive sigma_i satisfy the hypotheses uniformly. One may put tau equal to a directional regeneration horizon and B equal to a positive-probability no-backtracking event; neither is incorrectly treated as an ordinary stopping-time law. Proving finite conditional mean of the exit count K_tau is the single remaining moment problem for this route. Directional transience only gives its almost-sure finiteness. The equivalence does not yet establish that mean, or prove ballisticity. With S_i a singleton the criterion is tautological; balls with radius at least two separate residence from returns but do not make their exit skeleton iid.

Source: owner campaign derivation, w447, 2026-10-10. No novelty claim; no formal checker receipt.
