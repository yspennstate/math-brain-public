# Checks of the proximal LSI asymptotic

All checks below are analytic. No numerical fit or simulation is used.

## Independent checks of constants and formulas

1. **The correlation kernel.** The proof obtains
   `g(w)=exp(-(1+w^2)/2) sinh(w)` from the cosine characteristic function.
   A separate derivation uses probabilists' Hermite polynomials. Their
   generating function is
   `exp(tx-t^2/2)=sum H_k(x)t^k/k!`; taking the expectation of the product
   of two generating functions gives `exp(ts)` and hence
   `E H_j(X)H_k(X)=k! 1_{j=k}`. Expanding the two sines in this orthogonal
   basis gives
   `g(w)=exp(-(1+w^2)/2) sum_{k odd} w^k/k!`, the same formula. The series
   converge in Gaussian L2, since the sum of squared coefficients times
   `k!` is finite for each fixed w.

2. **The factor `1/(2 lambda^2)`.** Independently of square completion,
   the Gaussian moment generating function gives
   `E_A exp(A g(w)/lambda)=exp(g(w)^2/(2 lambda^2))` for a unit-variance
   A. There is also a variational check: with `b=lambda a`, the part of the
   logarithmic density multiplied by `lambda^2` is
   `-b^2/2+b g(w)-lambda^2 w^2/2`. The supremum of the first two terms
   is `g(w)^2/2`, attained at `b=g(w)`. At the separating line `w=0` its
   supremum is zero. This reproduces the barrier `M^2/2`, including its sign
   and its factor two. The variational observation is a check of the
   exponent; the proof's measure inequalities establish the actual bounds.

3. **The maximizing equation and barrier size.** The proof differentiates
   `exp(-(1+w^2)/2) sinh(w)`. Alternatively differentiate the difference of
   Gaussians in (2). A positive critical point must have `w>1` and satisfy
   `(w-1)/(w+1)=exp(-2w)`, which rearranges to `w tanh(w)=1`.
   Monotonicity of `w tanh(w)` proves uniqueness. The bounds
   `g(1)=(1-exp(-2))/2 <= M < 1/2` imply
   `(1-exp(-2))^2/8 <= M^2/2 < 1/8`.
   The upper inequality follows because, for positive w, g is half the
   difference of a Gaussian factor at most one and a strictly positive
   Gaussian factor, and the maximum is attained. Thus the barrier is a
   strictly positive absolute constant, not a quantity tending to zero
   with lambda.

4. **Gaussian LSI normalization.** The semigroup derivation in the proof
   gives `Ent(h^2)<=2 int |grad h|^2`. As a separate normalization check,
   in one dimension `h(x)=exp(tx/2)` has
   `Ent(h^2)=(t^2/2) exp(t^2/2)` and
   `int |h'|^2=(t^2/4) exp(t^2/2)`. Equality confirms the factor two and
   constant one. Truncation justifies this check if bounded test functions
   are used in the definition.

5. **LSI to Poincare normalization.** In addition to inserting `1+s h`
   as in the proof, insert `sqrt(1+u h)` for a bounded mean-zero h.
   Its entropy is `u^2 Var(h)/2+o(u^2)`; its energy is
   `u^2 int |grad h|^2/4+o(u^2)`. Equation (1) again gives
   `Var(h)<=alpha^(-1) int |grad h|^2`, with no extra factor two.

6. **The shear factor.** Directly, if `H=h composed with T_lambda`,
   then `H_b=h_a` and `H_w=h_w+(g'/lambda)h_a`, evaluated at T_lambda.
   The Euclidean triangle inequality gives
   `|grad H|<=(1+L/lambda)|grad h|`. Squaring recovers the denominator in
   (11). Its logarithm times `lambda^2` vanishes, so it does not alter
   the limiting exponent.

7. **The bottleneck quotient.** Under the even w marginal,
   `E h_r=0`. Its squared value equals one off the strip, giving variance
   at least `1-q`. Its derivative is `1/r` exactly inside the strip,
   giving energy `q/r^2`. Thus the quotient is at most
   `q/(r^2(1-q))`; its exponential scale agrees with the lower estimate
   after delta tends to zero. The constants r and gamma(I) depend on
   delta and g, not on lambda; no limit exchanges involving them occur.

## Attempts to invalidate the interpretation

- **Could this be entropy escape?** No. KL to a probability prior is
  nonnegative and the squared risk is nonnegative. The proximal law is
  normalizable by its exact Gaussian moment generating function.
- **Could the first variation accidentally include the prior twice?**
  No. The first variation of the risk is `-a g(w)`; the Gaussian reference
  appears once in `p proportional to exp(a g/lambda) pi`.
- **Could a missing loss normalization change the barrier?** Yes, using
  full squared loss instead of half squared loss doubles g and multiplies
  `M^2/2` by four. The proof fixes half squared loss throughout.
- **Could the result depend on zero risk being inaccessible to finite-KL
  laws?** No. The Gaussian smoothing family in Section 1 proves that their
  risk infimum is also zero. Exact attainment is unnecessary here.
- **Could it contradict Arrhenius estimates for bounded features?** No.
  Although sine is bounded, the full neuron `a sin(wx)` is unbounded in a.
  If a were bounded, the exponent `a g(w)/lambda` would be a bounded
  perturbation of size `O(1/lambda)`. That is a different parameter model.
- **Could a fixed L2 penalty be substituted without changing the result?**
  No. Section 6 shows directly that a fixed L2 coefficient gives a
  `1/lambda` square-completion term instead. The prior is fixed in this
  result; the coefficient of the quadratic part of lambda KL is lambda.
- **Could the bottleneck prove slow prediction?** No. Equation (17)
  gives exact equal predictions for a continuum of perturbations in this
  mode. This is stronger than a first-order cancellation.
- **Could this be the stationary MFLD distribution?** Not established.
  It is the frozen proximal law at rho_0=pi. A uniform proximal LSI
  estimate must cover it; a trajectory-specific risk estimate need not
  inherit its bottleneck time.
- **Could the theorem apply without its symmetry assumptions?** The
  upper proof needs g odd (in particular g(0)=0 and an even w marginal).
  It is verified for this sine model. For the zero teacher, g is zero,
  the measure is exactly pi, and both constants are one; the positive-M
  hypothesis excludes that degenerate case.
- **Does this answer polynomial versus exponential risk time?** No.
  It proves a sharp limitation of one available proof route in an allowed
  example and identifies why turning that limitation into a runtime lower
  bound would be invalid.
