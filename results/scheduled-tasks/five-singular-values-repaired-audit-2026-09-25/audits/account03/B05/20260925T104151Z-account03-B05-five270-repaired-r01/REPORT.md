# account03/B05 repaired-source audit

Source: math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa, paper.tex blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.

Coverage this run: lines 175-241. Rendered pages: UNCHECKED because the repaired 15-page reference PDF is not available to the screenshot/runtime path; the historical 14-page PDF was not reused.

Verdict for this range: PASS, no new GAP/FALSE.

Lines 177-205: geometric Brascamp-Lieb heat-flow proof independently rechecked. The differential identity and contraction are correct; Gaussian-polynomial domination justifies differentiation and the Laplacian integral; the large-time and zero-time limits and monotone truncation close.

Lines 218-228: projection-density proof PASS. The orthogonal completion is only a deterministic change of variables. If beta_i=0 then w_i=0, so that factor is fiber-independent and <=1; any number may be dropped. This independently validates repair item 7. For beta_i>0 the normalized rows form the Brascamp-Lieb frame, 0<beta_i<=1, and the one-dimensional integral is <=beta_i^(-1/2).

The p(y)=0 repair also PASS. The source now handles zero density before logarithms; on the positive branch the preceding finite product proves p(y)<infinity, after which beta log(1/beta)<=1-beta and sum beta_i=n-d give p(y)<=e^(d/2). This independently closes old C12.

Line 228 thin SVD/Jacobian gives e^(d/2) det(BB^T)^(-1/2).

Lines 231-240: Fourier-power lemma PASS. Difference densities stay capped by one; m=floor(p/2)>=p/4; Plancherel gives integrability; inversion gives a continuous density; the projection lemma is applied to original independent copies, not rotated coordinates; the printed 2pi sqrt(2e)/sqrt(p) constant follows.

After these derivations, account03/B01 new-source coverage was consulted only as corroboration and also passes this range.

Fresh B05 new-source pass coverage is 175-241. Remaining: 1-174 and 242-683. Next cursor: 242. Execution remains WITHOUT_VERIFIED_BRAIN.
