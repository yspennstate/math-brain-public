# Self-audit of C001/C002 v1

Independent review is pending. These checks were done by the author, not another agent.

C001 normalization: alpha times product sqrt(d_i) is exactly one, including the output layer. Differentiating W_i costs 1/sqrt(d_i); updating A_i costs that factor again. All product hypotheses use operator norms and all data/residual bounds use Frobenius norms as appropriate.

Counting: there are <=L^2 nonempty contiguous blocks. Their Frobenius second moment is the input dimension <=m. The first-moment column sum is <=m, not dimension-free. Markov and union factors are retained. No independence across blocks is assumed.

Robustness: empty gaps have norm one; every perturbation term is counted with binomial(n,s)<=L^s. For long blocks a single perturbation leaves one gap with index difference >=L/10 once L>=40. Higher-order remainder has factor 2L^8, retained explicitly.

Exact rational balances (logs/exact_exponent_check.json): radius exponent 30, probability remainder exponent 47, second-order slack 2, drift slack 8, output decay exponent 50. These were derived from fractions separately from the floating-point script.

Numerical witness check (logs/arithmetic_check.json): scalar product evaluated by stable log1p/expm1 and independently with 60-digit Decimal arithmetic. Maximum tested relative discrepancy <2e-16. The analytic asymptotic witness, not these samples, proves C002.

Adversarial scope checks: nonzero fixed X,Y and tolerance below plateau are necessary; width below d_y is not included in the new C001 statement; eta<=1 is in original W coordinates; C002 is neither a Gaussian event nor a GD trajectory. The full strip L/(10000 log L)<m<=L/log L stays open. C001 may be an elementary quantified corollary of known estimates; novelty and scoring need lead review. No shared frontier score has been changed.
