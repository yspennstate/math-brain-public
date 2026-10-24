# Coverage detail F

- L228-229 p5 Lemma 3.2(b) — PASS. Thin SVD B=P Sigma U^T gives Jacobian det Sigma=sqrt(det BB^T).
- L231-241 p5 Lemma 3.3 — PASS. Difference density is <=1. With m=floor(p/2), m>=p/4 and |hat f|<=1 give the correct comparison. The even power is an integrable characteristic function; the scalar projection cap gives 2pi sqrt(2e)/sqrt(p).
- L245-249 p5-6 crossing-volume definitions — PASS. Deps: Cauchy-Binet/Gram identities. Dimensions and index sets check.
- L251-258 p6 Theorem 4.1 statement — PASS conditional on the already reconstructed Lemma 4.3 and C02 repair. Uniformity in same-bank quadratic terms and affine terms is preserved.
- L260-269 p6 Lemma 4.2 — PASS. Rewrite as weighted log ratio, apply Jensen, then count each squarefree m-subset monomial m! times in (sum alpha_i)^m.
