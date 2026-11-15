# Audit of the vanishing-loss amplification theorem

## What changes from the previous result

The previous theorem starts with eventual inverse-polynomial success and reaches any fixed smaller density, with arbitrarily prescribed inverse-polynomial failure. Its proof keeps the refresh rate fixed and may use a very large constant runtime exponent.

The present theorem starts with success n^(-o(1)), uses a logarithmic list of refresh rates tending down to about 1/n, and reaches a target with only o(n) vertices lost. There are n^2 trials at each scale. Failure is bounded by an arbitrary fixed inverse power of log n, with a loss depending on that power. These are different quantifiers: neither result replaces the other in its full scope.

## Independent checks of the inherited argument

The previous script was read and rerun without editing its source. Its PASS output and JSON are recorded locally. Independently, stationarity plus covariance re-derives the reverse conditional probability delta p, and the negative-moment sign and Chernoff optimization re-derive its main bound. Nothing in that check contradicts the earlier theorem.

## The new load-bearing estimates, checked twice

1. The one-scale reachability failure is v^(-1)n^(-delta/2). The imported reverse hypercontractive estimate gives E Q^(-delta/2)<=1/v. Markov gives the stated bound. Independently, if B={Q<1/n}, integrating Q^(-delta/2)>n^(delta/2) over B gives the same bound directly. This checks the exponent and inequality direction, but is not a second proof of the imported analytic theorem.

2. The posterior repair law is Binomial(binom(k,2),delta d/n). One derivation uses the two-edge-indicator joint mass P(X=1,Y=0)=p delta(1-p) and product independence. The verifier instead enumerates all elementary triples (original, refresh, replacement) for up to three pairs, then independently counts refreshed zero-original pairs for up to ten pairs. Both give the full binomial mass, including its normalizing probability (1-p)^t for t observed nonedges.

3. The mean is lambda/2, with lambda=delta d k(k-1)/n. Direct use of E 2^X<=exp(lambda/2) at threshold lambda gives exp[-lambda(log 2-1/2)]. Independently optimize the Poisson-Chernoff expression t log(t/mu)-t+mu at t=lambda and mu=lambda/2. It is exactly lambda(log 2-1/2). Gamma is positive by integral_1^2 (1/x) dx>1/2. Decimal.log and an exact rational atanh series independently evaluate log 2. Exact binomial-tail comparisons cover 111 small cases, including lambda=0.

4. With s=log(1/v) and beta=2(s+K log log n)/log n, a dyadic delta in [beta,2 beta) gives s-(delta/2)log n<=-K log log n. The algebra was checked directly in the proof and numerically at high precision in the verifier. Scale selection in the verifier uses exact rational comparisons, independently of the floor-log formula in the proof.

5. R=ceil(delta d k(k-1)/n) is at most D=ceil(2 beta d k(k-1)/n), by monotonicity of the ceiling. No strict inequality between integer ceilings is needed. Exact rational checks include k=1, k=n, small n, and integers as large as n=2^8192.

6. Each scale has n^2 trials and each trial uses at most n^2 Bernoulli draws. At most m n^4 rounded draws are made over all scales. With w=10m and 2^m>=n, their total coupling error is at most m n^(-6)<=n^(-5). The verifier checks this as an exact rational inequality.

## Dependence and selection

The conditional binomial law is used only for one predetermined trial after conditioning on H and its fresh solver tape. The rule selecting I cannot inspect G. The repair event is bounded uniformly for every such H and tape, then integrated and unioned over the predetermined trials at one scale. No conditional binomial law is claimed for the first successful trial or the final largest output.

Conditional on G, the trials at a fixed scale are independent, which is precisely the independence needed for exp(-n) failure to obtain any solver success. Unconditionally they share G. The repair union bound does not assume otherwise.

Returning the largest set over every scale lets the analysis select one useful scale. There is no union over scales in the success bound. The only all-scale union is for bit-sampling approximation, which uses a deterministic upper bound on the number of draws.

## Uniformity and finite-size issues

The algorithm knows d and the computable target sequence k_n. It knows neither v_n nor s_n, a, K, or a convergence modulus. Its schedule and call count do not depend on any of those quantities. The scale involving beta exists only in the analysis. Thus even a noncomputable convergence rate of s_n/log n does not create a uniformity gap.

The schedule stops at 2^(-ceil(log_2 n)). It contains [beta,2 beta) eventually because beta->0 and beta n->infinity. This need not hold at small n; the initial verifier mistakenly assumed it there and was corrected to test its actual hypotheses. Four cases in its finite grid are excluded for this reason.

For k_n/n->a>0, the product k_n(k_n-1)/n^2 tends to a^2. It is eventually at least a^2/2, without needing to know when. This makes the repair term exp(-Omega(n log log n/log n)) times a polynomial. To verify the asymptotic comparison, put x=log n: n log log n/(log n)^2=e^x log x/x^2->infinity.

The overlap-scale corollary uses integer d and rational epsilon so its target is polynomial-time approximable. Computability of a real constant alone would not suffice. An explicit geometric-series tail proves the claimed polynomial approximation time for log d; no real-number oracle is used.

The case a=1 is allowed by the theorem's form, although its success assumption cannot hold for k_n=n in this model at d>0: that event requires an empty graph and has exponentially small probability. The result is an implication, so such impossible hypotheses create no contradiction. Fixed d is essential to the stated runtime and asymptotics; no growing-d uniformity is claimed.

## Attempts that do not give stronger conclusions

Choosing delta of order 1/log n with constant starting success makes the bad-input bound only a fixed constant when the number of trials has a fixed polynomial exponent. This estimate does not yield high probability. Taking delta log n->infinity, or a dyadic scale with the required margin, is what makes it vanish. This is a limitation of the bound, not a proof that O(n/log n) loss is impossible.

If v_n=n^(-s) for fixed s>0, beta tends to 2s, so this argument does not give vanishing loss. Increasing a fixed polynomial trial exponent changes constants but does not remove this obstruction in this bound.

Polynomially small failure n^(-L) from constant success would require replacing K log log n by L log n in the displayed beta calculation, preventing beta from tending to zero. No such stronger statement follows here.

The theorem does not preserve the exact size k_n. It does not rule out a better algorithm or a sharper amplification theorem. No reduction from planted clique, random SAT, or another average-case assumption is present, and T284 remains unresolved.
