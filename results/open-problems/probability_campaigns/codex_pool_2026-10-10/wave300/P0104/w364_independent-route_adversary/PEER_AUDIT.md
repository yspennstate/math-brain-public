# Adversarial audit of the paired spectral route

2026-10-10. Inputs: w363/ATTEMPT.md, sections L1-L5 and GAP G1; w363/STATEMENT_FOR_ADVERSARY.md. The independent boundary-profile derivation in this folder was saved first. This audits the mathematical argument, not another audit or a code receipt.

Verdict: KEEP the stated finite/special-law lemmas within their hypotheses; P0104 remains unresolved because G1 is unproved. This is one adversarial audit, with final independent referee w365 still pending. No formal checker was used.

L1 is valid for strictly positive bounded weights. A straight route to n e1 costs at most bn; any competitor with cost at most bn has at most floor(bn/a) edges. Removing cycles strictly reduces cost. All possible optimal competitors lie in a finite deterministic ball, so no random-domain conditioning is needed. This localization does not apply as stated when a=0.

L2 uses an explicitly independent coordinate-retention/resampling coupling. The biased Bernoulli product basis is orthonormal, the coupling multiplies only independent coordinate pairs, and each discrete gradient removes one normalized factor. The resulting finite spectral sum integrates to the variance exactly. Its rho=0 endpoint retains the degree-one contribution; rho=1 gives resampling energy. Thus integrating is essential; substituting an endpoint for the integral would be wrong.

L3's sandwich remains valid with ties. An avoiding low minimizer persists at the same cost, giving zero increment; a using high minimizer provides a low competitor cheaper by exactly Delta, forcing the full increment Delta. The conditioning step requires the same deterministic selection rule in forced and unforced environments. With that rule, q Delta^2 EH<=D<=p Delta^2 EL is justified. The packet claims a sandwich, not equality with membership in an arbitrary chosen geodesic, so C05's tie counterexample does not break L3.

L4's path count is valid in d=2. Simple paths have distinct edges, so the per-path iid probability calculation is legitimate. The union bound over different paths needs no path independence. For q=1/100, r=3/(5 sqrt(10))<1/5 follows from 9<10. Therefore (4/3)r^n/(1-r)<1/3 for n>=1. On the complementary event every minimizer has at least n/4 high edges, yielding EH>=n/6. The claimed n/600<=D_n<=(99/50)n follows from L3. This proves linear resampling energy, not linear variance or a KPZ exponent.

L5 correctly normalizes nu_n(S)=|S| fhat_n(S)^2/D_n and obtains Var(T_n)=D_n E_nu[1/|S|]. With the two-sided linear-energy estimate, its exponent reduction is valid. Its correlation-envelope sufficient condition also integrates correctly: substitute u=t n^(1/3); the upper integral is at most (C/epsilon)n^(2/3), and the lower interval contributes c a_0 n^(2/3). The packet explicitly does not prove either envelope. Its weighted-CDF identity has the correct boundary term and does not discard low-degree leakage.

The single missing premise is a quantitative bound on E_nu[1/K] for this actual iid FPP law, of order n^(-1/3+o(1)), including the lower bound. A typical spectral scale, qualitative noise sensitivity, or the existing n/log n variance bound supplies no such estimate. The author already marks this as G1; the audit does not convert that honest gap into a false complete-proof claim.

The independent obstruction C02 addresses a different shortcut: scalar block minima can choose incompatible interface vertices. Both packets independently use a small diamond as a finite check and obtain Var(T)=23/64. That overlap is recorded; w364 does not rerun the paired spectral/energy computations or claim their novelty. Its additional quantities are the matching error and Cov(L,T-L), and its main proposed route uses boundary profiles.

NEXT: Prove a weighted low-degree spectral-mass estimate for the special law, or quantify centered boundary-matching error for the independent route. Another source search does not close either mathematical gap.
