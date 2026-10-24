# Independent mathematical review of `fourier.tex`

Reviewer: `/root/claude_core/adapted_attack`. Date: 23 September 2026.
The reviewer did not author this chapter. The complete chapter through the
quarter-power, logarithmic-potential, and negative-moment conclusions was read
and independently rederived, including the subsequently appended exact-marginal
and general-k Gibbs subsections.

## Conclusion

**Pass**, subject to one minor explicit-hypothesis clarification communicated to
the author: assume `Z_k>0` in the Gibbs discussion, or dispose of `Z_k=0`
separately before using the probability simplex on positive-volume row sets.
No substantive mathematical error was found. This review does not assert that
any sufficient crossing condition is automatic for the unrestricted conjecture.

## Analytic foundation and volume estimates

- Checked Fourier conventions, sharp Hausdorff--Young and Young normalizations,
  geometric Brascamp--Lieb scaling, and the integrable-envelope inversion lemma.
- Recomputed the sharp modulated scalar bound
  `2*pi*p^(-1/2)*(p/(p-1))^((p-1)/2) <= 2*pi*sqrt(e)/sqrt(p)`.
  Arbitrary measurable separable phases do not alter the input norm argument.
- Recomputed the difference-density and Fourier-power norms, including all
  exponents of `q`, `d`, and `q-d`.
- Checked regularized Fresnel signs, determinant branches, absolute values,
  domination, and passage to the oscillatory limit. Checked diffuse-frame
  conditioning and its density constant.
- Recomputed the cross-block decoupling inequality and general-q Jensen step.
- Reconstructed the Gaussian Brascamp--Lieb determinant bound from its minor
  expansion and weighted AM--GM. Checked all cancellation of row and column
  marginal powers. At saturated column marginal one, every active minor uses
  that column, so omission of its density factor and zero determinant variable
  is justified.
- Verified the general volume density constant, its old weaker counterpart,
  the fractional-marginal corollaries, and the weighted-minor relative-entropy
  penalty.

## Exact factors and Gibbs optimization

- Recomputed the unrelaxed exact row/column entropy factors, the rank-three
  q=1 constant, and the balanced six-row/six-column example. Checked its stated
  failure of the separate sufficient tail criterion.
- Verified the row-law reduction by the conditional relative-entropy identity.
- Independently proved the general-k Gibbs dual, including constraint-boundary
  cases, infeasible constraints, and possible absence of a finite dual
  optimizer. The compact-box minimax argument and its limit are valid.
- Checked the complementary-slackness calculation for a finite optimizer.
- Independently rederived bounded-row deletion: weights lambda/sum(lambda),
  the strict cardinality `|H|<k/h`, the lower bound on every surviving dual
  summand, and the finite-subsequence argument as epsilon tends to zero.
- Checked the three-volume alternative and the single-active-row formula.

## Regularized determinants, ridge bounds, and spectral windows

- Recomputed the graph inequality with free regularizer, including the
  transformed geometric frame and both scalar norm products.
- Verified the tangent inequalities giving `L_q=pi*e*sqrt(2/q)`, the
  determinant exponent, the gamma-ratio density integral, and its simpler
  power-envelope bound.
- Checked ridge leverage, its stability inequality, the rank-three ridge
  constant `9*sqrt(3*e)/(2*sigma)`, and the fact that q=2 admissibility is
  automatic.
- Checked the MSS partition specialization at leverage 1/32: partial-frame
  eigenvalues in `[7/32,25/32]`, crossing singular values, range leverage, and
  the resulting density estimate.
- Recomputed the spectral-window perturbation bounds, in particular
  `s_3 >=13*s/64` and `(1/sqrt(7)+sqrt(6)/13)^2<1/2`.
- Verified the spectral formula for volume marginals, the operator upper
  bound involving the distributed singular-value tail, projection stability,
  and the near-diffuse and distributed-tail constants.

## Quarter-power concentration and consequences

- Checked the large-diagonal scalar sublevel estimate and the random-sign
  crossing alternative for an arbitrary nonzero quadratic matrix.
- Recomputed the one-singular-value regularized determinant envelope and the
  Gaussian smoothing conversion to concentration.
- Independently evaluated the coefficient
  `2^(3/8)*pi^(-1/4)*e^(3/8)*Gamma(3/8)<5` and verified the elementary rational
  upper bounds used in the text.
- Checked the layer-cake logarithmic-potential bound and the negative-moment
  factor `5^(4*beta)/(1-4*beta)`.

## Source and cross-reference checks

The cited primary versions of the MSS partition theorem and the Livshyts--
Paouris--Pivovarov product-projection theorem were inspected and match the
specializations used. The lower-level chapter references `four:volume` and
`four:quarter` with their correct hypotheses. Its quarter-power reference was
updated to call the latter a lemma.

This is a mathematical review record, not a compilation certificate. The
chapter author separately reports a successful final standalone compilation.
