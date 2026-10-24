# w359 independent review of w358, P0017

Verdict: KEEP S1.3, S1.4 and S1.5 as exact special cases and obstructions. They do not solve P0017 and do not refute the cited October proofs. Reviewed 2026-10-10 against INDEPENDENT_DERIVATION.md and CLAIMS.jsonl as read, without relying on a peer review.

S1.3. For X=Y-1, Y~Exp(1), the tilted normalizer is integral_0^infinity exp(s(y-1)-y)dy = exp(-s)/(1-s), requiring s<1. Division by this normalizer gives Y~Exp(1-s), hence E X=s/(1-s) and Var X=(1-s)^(-2). The linear test has gradient energy 1, so the claimed Poincare lower bound follows. The conclusion concerns arbitrary deterministic tilted laws, not a localization process average. KEEP.

S1.4. In y=x+1 coordinates, the original exponent plus (1-t)x-tx^2/2 is -1+t/2-ty^2/2 on y>=0. Thus Y is exactly half-normal with variance (1-2/pi)/t. Translation preserves variance. Every t>0 is admissible. The current tilted covariance grows as t goes to zero, while the initial centered exponential has variance 1. The universal t-dependent Brascamp-Lieb upper bound 1/t is compatible with this example. KEEP.

S1.5 (hardest claim, independently rederived). The normalized tilt mean is (1-s) E[f(Y-1)exp(sY)]. Expanding the scalar exponential and multiplying by (1-s) gives q_d(y)=y^d/d!-y^(d-1)/(d-1)! for d>=1. On |s|<1/2, the exponential and its derivatives define bounded L2 functionals locally, because E[Y^k exp(2sY)] is finite. Therefore coefficient extraction and differentiation are justified for every fixed f in L2.

The coefficient mean is 1-1=0. Its squared norm is (2d)!/(d!)^2 - 2(2d-1)!/(d!(d-1)!) + (2d-2)!/((d-1)!)^2. The first term is twice the middle term without its factor 2, so they cancel, leaving binomial(2d-2,d-1). Cauchy-Schwarz attains equality at f(Y-1)=q_d(Y)/||q_d||_2. Central-binomial asymptotics give the stated exponential rate 2; binomial(2d-2,d-1)<=4^(d-1) proves that R=2 is sufficient. Finally -s-log(1-s) has derivatives (m-1)! for m>=2. KEEP.

The remaining parent gap is an all-degree, all-f, dimension-uniform Hilbert-Schmidt bound for general isotropic log-concave laws (or an independently audited existing proof). A scalar exponential calibration and arbitrary-tilt obstruction do not fill it. Extending this boundary example to the regular smooth strongly log-concave class requires a uniform approximation argument, as w358 already states.

Reproduction: python -X utf8 ~/brain_workers/w359/verify_math.py. This runs exact rational checks of the coefficient norm and small numerical sanity checks; the proof is the derivation above, not a formal-check receipt.
