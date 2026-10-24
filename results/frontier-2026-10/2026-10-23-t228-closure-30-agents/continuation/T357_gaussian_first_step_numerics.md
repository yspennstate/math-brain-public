# T357: finite-dimensional Gaussian first-step moment checks

Agent 24, 23 October 2026. **Numerical sanity checks only.** No coefficients were fitted, no dimension extrapolation was performed, and no limit theorem or calibration result is claimed.

**Finding.** The tested moments are consistent with the proposed constants and scaling. In the main informative-teacher grid, every covariance and variance target lies within its pointwise approximate 95% Monte Carlo interval. One supplementary stronger-teacher variance estimate at dimension 256 is slightly outside that interval; it is retained and reported below. These intervals describe simulation uncertainty around finite-dimensional moments, not uncertainty in an asymptotic proof.

## 1. Model, exact scaling, and fixed comparison

For each independent replication, generate training rows and a fresh test row as independent standard Gaussian vectors in dimension d, independent feature columns f_j distributed as N(0,I_d/d), and conditionally independent training labels Y_i with success probability sigmoid(beta X_i1). Set Z=X_01 and

\[
H_{ij}=\tanh(f_j^T X_i),\qquad
w=\frac1m H^T(Y-\tfrac12\mathbf1),\qquad
S(X_0)=\frac{cd}{n}\tanh(F^T X_0)^T w.
\]

Thus the implemented score is exactly the stated one-step expression, with kernel normalization 1/m and sample multiplier cd/n. There is no additional square-root width scaling, training-label clipping, fitted intercept, or covariance normalization. The ratios are alpha=n/d and gamma=m/d, not n/(2d) or m/(2d). The features and test inputs are independent of training data.

The comparisons, fixed before the main run, are

\[
a=E[G\tanh G],\quad b=E[\tanh^2G],\quad
\mu=E[Z(\sigma(\beta Z)-\tfrac12)],
\]

\[
C_\infty=ca^2\mu,\qquad
V_\infty=c^2\left[(a^2\mu)^2+
\frac{\mu^2a^2b}{\gamma}+
\frac{a^4+b^2/\gamma}{4\alpha}\right].
\]

All experiments use c=1. The main grid uses beta=2, alpha and gamma independently in {1,2}, and d in {64,128,256,512,1024}. The supplementary grid uses beta=1 and beta=4 at d=256 and 1024, alpha=gamma=1. A beta=0 null control uses d=512, alpha=gamma=1. This gives 25 configurations.

## 2. Replications, uncertainty, and independent covariance check

The four base seed streams are 1729, 2027, 4211, and 8089. The full SeedSequence entropy is recorded separately for every replication. There are 16 independent training/features replications per seed in the main grid through d=512 and in the null control, and eight per seed at d=1024 and in the supplementary beta=1/4 grid. Every replication uses 512 independent test queries.

Total: **1,344 independent training/features clusters and 688,128 independent test queries**. The main run completed in 52.0 seconds with one requested BLAS thread. The pilot is not pooled into these results.

Each training/features replication contributes one estimate of E[ZS] and one estimate of E[S²]. Standard errors and Student-t 95% intervals are computed across those independent cluster estimates. Queries sharing the same training set and features are never treated as independent training replications. The intervals are approximate and pointwise; no simultaneous-coverage guarantee is asserted.

For fixed training data and features, the test score is odd in X_0, so E[S | training,F]=0 and E[Z]=0 exactly. Therefore these uncentered second moments are the desired covariance and variance. Conceptually adjoining the antithetic test points -X_0 makes both sample means exactly zero without changing ZS or S²; this does not double the effective query sample size.

The JSON also reports a lower-noise covariance estimate obtained by conditionally integrating out X_0. Gaussian integration by parts yields

\[
E[Z S\mid X,Y,F]
=\frac{cd}{n}\sum_j w_j f_{j1}\,
E_G[1-\tanh^2(\|f_j\|G)].
\]

This identity concerns the finite-dimensional model and does not use the proposed asymptotic formula. The one-dimensional expectations are evaluated by Gauss-Hermite quadrature; orders 128 and 256 are compared. Direct query-based covariance estimates are retained in the JSON alongside this conditional estimate. The tables below use the conditional estimate for covariance and direct test queries for variance.

The largest order-128/order-256 discrepancy in any conditional covariance was 3.48e-12, far below the Monte Carlo standard errors. Direct-query covariance and the conditional estimate differed by at most 2.17 paired Monte Carlo standard errors across the 25 cells. This finite comparison is a wiring check, not a certified quadrature error bound.

## 3. Reference constants

Independent adaptive Gaussian quadrature and 256-point Gauss-Hermite quadrature give:

| beta | a | b | mu |
|---|---:|---:|---:|
| 0 | 0.605705509602 | 0.394294490398 | 0.000000000000 |
| 1 | 0.605705509602 | 0.394294490398 | 0.206620964142 |
| 2 | 0.605705509602 | 0.394294490398 | 0.302852754801 |
| 4 | 0.605705509602 | 0.394294490398 | 0.364738765743 |

The identities a=1-b and, at beta=2, mu=a/2 were checked numerically. The largest discrepancy between the two reference integration methods was 1.59e-11, at beta=4; at beta=2 it was 6.33e-15. These are numerical precision checks, not formal integration certificates.

At beta=2 the covariance target is 0.111110365606 for every alpha,gamma. The four variance targets are 0.098130671213, 0.072063132435, 0.061872112913, and 0.045521333207 for (alpha,gamma)=(1,1),(1,2),(2,1),(2,2), respectively.

## 4. Largest-dimension main-grid results

Each bracket is an approximate pointwise 95% Monte Carlo interval across 32 independent training/features replications at d=1024.

| alpha | gamma | Estimated covariance [95% interval] | Variance target | Estimated variance [95% interval] |
|---:|---:|---|---:|---|
| 1 | 1 | 0.110607 [0.107470, 0.113745] | 0.098131 | 0.096912 [0.093383, 0.100440] |
| 1 | 2 | 0.110382 [0.107748, 0.113017] | 0.072063 | 0.072600 [0.069926, 0.075274] |
| 2 | 1 | 0.111633 [0.109479, 0.113787] | 0.061872 | 0.061208 [0.059044, 0.063373] |
| 2 | 2 | 0.111052 [0.109322, 0.112783] | 0.045521 | 0.044927 [0.043676, 0.046178] |

The largest relative discrepancy at d=1024 in this main grid is 0.66% for covariance and 1.31% for variance. Those discrepancies are smaller than the reported Monte Carlo intervals; this does not resolve a smaller finite-dimension bias.

## 5. All tested cells, including the supplementary discrepancy

The ± quantity below is the approximate pointwise 95% half-width, not one standard error. All targets use the displayed formula without adjustment.

| d | beta | alpha | gamma | Covariance target | Covariance estimate ± 95% half-width | Variance target | Variance estimate ± 95% half-width |
|---:|---:|---:|---:|---:|---|---:|---|
| 64 | 2 | 1 | 1 | 0.111110 | 0.114433 ± 0.009405 | 0.098131 | 0.101424 ± 0.009054 |
| 64 | 2 | 1 | 2 | 0.111110 | 0.111865 ± 0.007400 | 0.072063 | 0.071007 ± 0.005211 |
| 64 | 2 | 2 | 1 | 0.111110 | 0.108443 ± 0.006776 | 0.061872 | 0.059754 ± 0.004481 |
| 64 | 2 | 2 | 2 | 0.111110 | 0.111715 ± 0.005931 | 0.045521 | 0.045295 ± 0.002807 |
| 128 | 2 | 1 | 1 | 0.111110 | 0.111481 ± 0.005782 | 0.098131 | 0.096841 ± 0.005546 |
| 128 | 2 | 1 | 2 | 0.111110 | 0.111793 ± 0.004320 | 0.072063 | 0.070470 ± 0.003561 |
| 128 | 2 | 2 | 1 | 0.111110 | 0.108182 ± 0.004621 | 0.061872 | 0.061667 ± 0.002820 |
| 128 | 2 | 2 | 2 | 0.111110 | 0.112547 ± 0.003828 | 0.045521 | 0.045195 ± 0.002248 |
| 256 | 2 | 1 | 1 | 0.111110 | 0.111155 ± 0.004475 | 0.098131 | 0.098108 ± 0.004506 |
| 256 | 2 | 1 | 2 | 0.111110 | 0.110492 ± 0.002902 | 0.072063 | 0.071555 ± 0.002158 |
| 256 | 2 | 2 | 1 | 0.111110 | 0.111388 ± 0.003579 | 0.061872 | 0.061482 ± 0.002469 |
| 256 | 2 | 2 | 2 | 0.111110 | 0.110181 ± 0.002865 | 0.045521 | 0.045743 ± 0.001887 |
| 512 | 2 | 1 | 1 | 0.111110 | 0.112097 ± 0.002885 | 0.098131 | 0.097027 ± 0.002985 |
| 512 | 2 | 1 | 2 | 0.111110 | 0.108475 ± 0.002749 | 0.072063 | 0.071257 ± 0.002135 |
| 512 | 2 | 2 | 1 | 0.111110 | 0.110565 ± 0.002319 | 0.061872 | 0.062737 ± 0.001877 |
| 512 | 2 | 2 | 2 | 0.111110 | 0.111204 ± 0.001874 | 0.045521 | 0.045153 ± 0.001109 |
| 1024 | 2 | 1 | 1 | 0.111110 | 0.110607 ± 0.003137 | 0.098131 | 0.096912 ± 0.003528 |
| 1024 | 2 | 1 | 2 | 0.111110 | 0.110382 ± 0.002635 | 0.072063 | 0.072600 ± 0.002674 |
| 1024 | 2 | 2 | 1 | 0.111110 | 0.111633 ± 0.002154 | 0.061872 | 0.061208 ± 0.002164 |
| 1024 | 2 | 2 | 2 | 0.111110 | 0.111052 ± 0.001731 | 0.045521 | 0.044927 ± 0.001251 |
| 256 | 1 | 1 | 1 | 0.075805 | 0.076563 ± 0.005185 | 0.084439 | 0.082551 ± 0.004592 |
| 1024 | 1 | 1 | 1 | 0.075805 | 0.074998 ± 0.003208 | 0.084439 | 0.084649 ± 0.003279 |
| 256 | 4 | 1 | 1 | 0.133815 | 0.129205 ± 0.005695 | 0.109668 | 0.103249 ± 0.006287 |
| 1024 | 4 | 1 | 1 | 0.133815 | 0.135496 ± 0.003786 | 0.109668 | 0.110681 ± 0.003994 |
| 512 | 0 | 1 | 1 | 0.000000 | -0.000578 ± 0.002590 | 0.072517 | 0.072616 ± 0.002506 |

All 25 covariance targets lie within both the direct-query and conditional covariance intervals. Twenty-four of the 25 variance targets lie within their pointwise intervals. The exception is beta=4, d=256, alpha=gamma=1: estimated variance 0.103249 versus target 0.109668, standard error 0.003083, interval [0.096963,0.109536]. The discrepancy is -2.08 standard errors, with the target just above the interval endpoint. At d=1024 for the same beta/ratios, the estimate is 0.110681 with interval [0.106687,0.114675], containing the target. No additional seeds or altered formula were selected to remove the smaller-dimension discrepancy.

With 25 pointwise comparisons, one such marginal exception is not by itself evidence against an asymptotic formula; it could reflect Monte Carlo fluctuation, finite-dimension bias, or both. The experiment does not separate those possibilities. The beta=0 control gives covariance -0.000578 with interval [-0.003169,0.002012], and variance 0.072616 with interval [0.070111,0.075122], versus targets 0 and 0.072517.

## 6. Interpretation and reproducibility limits

The checks support the specified dimension/width/sample normalization and the proposed moment constants over the tested range. They do not establish a central limit theorem, Gaussianity of the score, quenched convergence, concentration of conditional moments, a convergence rate, calibration error, or early-stopping behavior. Agreement of two moments alone cannot establish any of those conclusions.

The reported intervals quantify Monte Carlo sampling variation around finite-dimensional moments. They do not contain an allowance for unknown finite-dimension bias relative to the limiting formula. Their coverage is approximate, and the grid is not covered simultaneously at 95%. Four seed streams help expose random-stream sensitivity; they do not eliminate these limitations. Per-seed means, every cluster estimate, and the exact seed construction are retained in the JSON.

The conditional covariance quadrature errors and floating-point arithmetic were checked only numerically. The implementation uses float64; it does not certify error bounds. Reproduction under the pinned software should agree up to ordinary platform/BLAS floating-point differences. The script contains no fitted slope, correction term, covariance rescaling, optimized parameter, or extrapolation model.

Run from the workspace root:

```bash
python followup/check_T357_gaussian_first_step.py
```

The script writes a progressively updated JSON and then sets status COMPLETE. It checks its own source hash remains unchanged during the run. Optional `--pilot` performs a small separate run; it should use a distinct output path and is not part of the reported sample total.

Observed software: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0; NumPy default_rng/PCG64; OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1.

Code: `followup/check_T357_gaussian_first_step.py`

SHA-256: `8a9f4ce02198d3f12c61ed0c7d8a3407b3b768b3fdefab41bca354a844230816`

Complete data: `followup/check_T357_gaussian_first_step.json`

SHA-256: `daad1c0bc609b9bf241591b269b2c50b998c6a8b899aba9a6a0746eec9bdc25f`
