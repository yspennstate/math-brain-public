# Checks and attempted counterexamples

## Independent derivations

1. **Interpolation probability, directly from likelihoods.** Conditional on the inputs, the probability of any specified label vector is at most `prod_i(1-q(X_i))`: each chosen label has posterior probability at most `1-q(X_i)`. There are at most `M_{n,d}` affine label vectors. Union-bound, then average. Independence gives `E prod_i(1-q(X_i))=(1-alpha)^n`. This recovers Theorem 1 at zero errors without the stochastic-domination or Chernoff arguments.

2. **Hyperplane count.** The proof uses central arrangements and their insertion recurrence. The script independently enumerates all binary sequences on moment-curve points. A degree-`d` polynomial changes sign at most `d` times, and every such sequence is realized by putting roots halfway between its sign changes. Exact integer polynomial evaluations confirm all 2,482 realizations in 34 `(n,d)` cases. Their counts equal `2 sum_{j<=d} binom(n-1,j)`. Thus the counting bound is attained for these samples, not merely a loose combinatorial estimate. The large numerical counts are calculated both as exact integer binomial sums and by a floating-point recurrence with log-sum-exp.

3. **Noise bounds.** All 1,024 label vectors on ten moment-curve inputs are enumerated, using exact rational probabilities. The 36 tested constant-noise tails satisfy (1); fair-noise zero-error probabilities attain its untruncated bound exactly. Six additional tests use different posterior error probabilities at each input and the exact Poisson-binomial comparison. An unconditional iid four-point input distribution is checked over all 32,768 joint samples, verifying the step that averages conditional noise into one binomial law.

4. **Gaussian numbers.** `Phi(-s)` is evaluated using `erfc` and independently by Simpson quadrature of the normal density for `s=0,2,5,10`. The largest observed relative discrepancy is recorded in audit_results.json. Numerical interpolation exponents also agree with the zero-error KL expression. The elementary Gaussian tail lower bound used for the growing-signal corollary is checked at the same four values, in addition to its analytic proof.

5. **Literature defect.** The rank argument and the kernel trace argument are independent. An exact rational six-point unit-circle sample supplies a nonzero vector in the nullspace of `XX^T`. Separately, unit-sphere kernel diagonal `1/2` forces `lambda_min(H)<=trace(H)/n=1/2`, incompatible with `n/(5d)` once `n/d>5/2`. This does not imply that the full nonlinear kernel is rank deficient.

## Cases that could invalidate an overbroad conclusion

- **Very strong signal without label flips.** For `n=10000,d=20,s=5,eta=0`, the bound truncates to one. It provides no obstruction there. The proof does not claim interpolation is impossible for all Gaussian mixtures with `n>d`.
- **Vanishing flip probabilities.** The fixed-noise conclusion uses a nonvanishing Bayes error. With changing parameters, use `n alpha-log M -> infinity`; no blanket impossibility follows solely from `n/d -> infinity`.
- **`n<=d+1`.** The counting factor becomes `2^n`, and the interpolation bound is generally vacuous. Generic affine classifiers can then fit arbitrary labels. The theorem is consistent with this.
- **Ties and repeated inputs.** The fixed tie convention is handled by a bias perturbation. Repeated inputs reduce the available prediction vectors. The iid finite-input audit includes repetitions.
- **Data-dependent training and initialization.** The probability bound holds simultaneously over all affine classifiers, so data dependence does not evade it. It does not bound the prediction count of all nonlinear networks by the affine count.
- **Directional convergence with zero limiting margins.** Subleading nonlinear terms can interpolate even if normalized scores vanish on some training inputs. A claim excluding every linear-looking normalized limit would be unjustified. The limiting-network conclusion explicitly requires positive training margins.
- **Generalization versus capacity.** Failure of affine interpolation says nothing by itself about the test error of nonlinear interpolants. Equation (11) forces nonlinear training decisions on a positive fraction of points, but those decisions could still be localized to sets of small population probability.
- **Hashimoto's different noise model.** No independent flip variable appears in its stated mixture model. The no-flip Gaussian corollary applies at fixed signal, and the separate flip corollary applies to the target's corrupted-label variant. They should not be conflated.

## Execution limits

The guarded audit exited successfully, checked actual niceness `20`, and used `16,744,448` bytes peak resident memory (about 16 MiB). It uses only the standard library and no child processes, GPU, or numerical thread pools. Wall time for that tool call was about 0.11 seconds. The `nice` wrapper warns because the sandbox denies its adjustment; inherited priority already satisfies the requirement. The first wrapper's `/usr/bin/time -l` resource query was also sandbox-denied. Both events are recorded in LOG.md.
