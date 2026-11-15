# Numerical evidence and limitations

The sampler diagonalizes I-P in the orthonormal sine basis on
{1,...,N-1}^2. Its eigenvalues are

\[
 d_{kl}=\sin^2(\pi k/(2N))+\sin^2(\pi l/(2N)).
\]

Independent standard normal coefficients divided by sqrt(d_kl), followed by
an orthonormal type-I sine transform, give exactly covariance G_N=(I-P)^-1
in exact arithmetic. In particular, sampling the inverse of the unscaled
graph Laplacian would lose a factor four; this implementation includes it.
The boundary is zero at coordinates 0 and N, with (N-1)^2 random sites.

### Sampling and resource record

There are 7,636 independent fields, with four lambda values
(0.2, 0.4, 0.6, 0.8) measured on each, for 30,544 count observations.
The main and independent calibration batches use float64. The three N=8192
fields and one N=16384 field use float32. The largest grid contains
268,402,689 random sites. It is the largest dyadic grid whose float32
field fits below 4 GB; the next, N=32768, requires more than 4 GB for
the field alone. This is not a claim to optimize all possible grid sizes
or all sampling algorithms under the memory cap.

Each FFT uses one worker, and numerical library thread limits are set to
one. Priority was inherited as nice 15, below the requested priority 10;
raising it to exactly 10 was disallowed, so it remained 15. The largest
observed process peak was 1.485242 GB. The largest-grid preflight
budget was 3.421 GB. Jobs ran sequentially, with no retained fields or
background jobs. Their metadata, seeds, durations and peaks are saved.
The largest four fields are scale/resource checks, not reliable mean,
variance or distribution estimates.

### Empirical size distributions

At N=512, pooling 2,350 independent fields gives the following. Standard
errors are empirical Monte Carlo standard errors, not certified bounds
for heavy tails. The exact means use Gaussian tails and an independently
computed covariance diagonal, without Monte Carlo.

| lambda | mean | standard error | sample variance | median | 95% quantile | exact mean |
|---:|---:|---:|---:|---:|---:|---:|
| 0.2 | 0.636784 | 0.003983 | 0.037287 | 0.610727 | 1.002649 | 0.642421 |
| 0.4 | 0.415721 | 0.004751 | 0.053041 | 0.358060 | 0.885437 | 0.422967 |
| 0.6 | 0.333747 | 0.006713 | 0.105905 | 0.226230 | 0.982017 | 0.343309 |
| 0.8 | 0.321910 | 0.012325 | 0.357002 | 0.111923 | 1.246543 | 0.339022 |

The distributions are asymmetric and increasingly sensitive to rare fields
as lambda increases. At lambda=0.8, the limiting GMC mass has infinite
second moment: its two-point moment kernel has the nonintegrable
diagonal singularity |u-v|^{-4 lambda^2}. A finite-N sample variance
cannot be treated as an estimate of a finite limiting variance there.
At lambda=0.6, second moments exist but fourth moments of the limiting
chaos need not; second-moment error estimates can still be sensitive
to missed tails. Pooling the calibration fields changed some empirical
second moments substantially. The tables retain those outcomes.

[Empirical distribution functions](data/level_size_ecdf.svg) compare
N=128, 512 and 2048. CSV summaries also include skewness, excess kurtosis,
5% and 95% quantiles, and comparisons to exact means. Different N values
use independent fields. These simulations do not directly sample a
coupled continuum Z_lambda, and their residuals are not asserted to be
X_N minus a sample of that continuum limit.

### Exact mean and the slow approach to the bias coefficient

The diagonal of G_N was computed in O(N^2 log N) work using the identity
sin^2(a)=(1-cos(2a))/2 and a type-I cosine transform. Summing univariate
Gaussian upper tails then gives E X_N exactly up to floating-point error.
The continuum integrals are computed independently from the disk-to-square
conformal map f'(z)=C/sqrt(1-z^4), C=0.5393526011883794. Analytic
derivatives of its positive beta-function series give the q and q^2
moments in B_lambda. The area integral returns 1.0000000000018; doubling
the series cutoff changes the reported constants by less than 4e-11.
These are numerical stability checks, not interval-arithmetic enclosures.

| lambda | continuum mean m | bias coefficient B | exact E X_8192 | log(8192)(E X_8192-m) |
|---:|---:|---:|---:|---:|
| 0.2 | 0.996701 | -6.285957 | 0.701965 | -2.655844 |
| 0.4 | 0.513271 | -0.854987 | 0.444477 | -0.619896 |
| 0.6 | 0.386674 | -0.334764 | 0.354899 | -0.286327 |
| 0.8 | 0.377899 | -0.285734 | 0.349695 | -0.254138 |

Thus the negative bias is visible, but the first-order coefficient has
not been reached at these sizes, especially for lambda=0.2. The Gaussian
tail expansion requires beta^2 t=4 lambda^2 log N to be large. Making
lambda small improves moment integrability while making this numerical
asymptotic regime much harder to reach. The discrepancy in the last
table is consistent with the higher-order terms; it is not evidence for
a different asymptotic exponent. The full first-order remainders are
saved in data/exact_means.csv.

[Scaled mean bias](data/mean_bias.svg) displays that discrepancy directly.

### Fitted finite-size rates

The fitted model is RMSE(X_N-c_beta M_N) proportional to (log N)^(-p),
using N=256,512,1024,2048. Each N is resampled independently in 500
bootstrap replicates. This is a fit to the finite-lattice comparison,
not a fit of a distance to the continuum law. The last column fits the
exact deterministic bias m-E X_N on the same range.

| lambda | fitted p for RMSE | bootstrap percentile range | exact mean-bias exponent |
|---:|---:|---:|---:|
| 0.2 | 0.421 | [0.397, 0.442] | 0.482 |
| 0.4 | 0.517 | [0.212, 0.825] | 0.720 |
| 0.6 | 1.069 | [-0.202, 2.615] | 0.829 |
| 0.8 | 1.474 | [-0.682, 3.048] | 0.857 |

These finite-range exponents do not establish an asymptotic power. The
small-lambda fits are preasymptotic, as the exact mean demonstrates;
the larger-lambda fits have substantial tail uncertainty that an empirical
bootstrap can miss. The lambda=0.8 comparison is outside Theorem A's
L2 range. No asymptotic-rate claim is based on that row.

[Comparison rate plots](data/comparison_rate.svg) show both the raw RMSE
and log N times RMSE. All point estimates, fitting choices, bootstrap
seeds, and percentile ranges are saved in data/fits.json.

### Fluctuation candidate: a calculation to test, not a theorem

Formal Laplace inversion around its saddle point suggests, with
F_N(beta)=c_beta M_N(beta),

\[
 X_N=F_N(\beta)-{1\over2t}F_N''(\beta)+\text{smaller terms}.
 \tag{C}
\]

The experiments save D_N=(log N)(X_N-F_N) and the proposed proxy
-F_N''/(2g), using analytic derivatives of the finite sum. Their
empirical differences remain appreciable, particularly at lambda=0.2.
The raw residual has strong skewness in several batches; its
[Gaussian quantile plots](data/residual_qq.svg) do not support an
unqualified finite-size Gaussian approximation.

There is also a structural reason to avoid guessing a central limit
theorem from independent-site counting. If Q_beta=-1/2 partial_beta^2
+ beta^{-1} partial_beta - beta^{-2}, the candidate is c_beta Q_beta M_N/g.
On a power beta^k, Q_beta has coefficient -(k-1)(k-2)/2 times beta^{k-2}.
The linear and quadratic chaos terms cancel. Apart from the deterministic
term, its small-beta expansion starts at third Gaussian chaos. Establishing
(C) with a sufficiently small remainder and identifying it in a specified
DGFF/continuum coupling are further proof obligations. A limiting
non-Gaussian derivative-chaos law is a candidate, not a result of this report.

### Verification and reproduction

- code/validate.py builds the full sampler matrix at N=4,7,12. Its
  covariance agrees with a direct inverse of I-P to at most 1.8e-15;
  the independent diagonal cosine transform agrees to 1.4e-15.
- Float32 and float64 sampling from identical coefficients at N=128
  differ by 2.2e-7 RMS and 1.1e-6 at worst. Large-grid float32 results
  are approximate floating-point samples; no exact threshold-count
  equality with a float64 realization is claimed.
- Direct Gaussian quadrature checks the two-variable saddle cancellation:
  t^2 times the cancelled moment kernel at t=50,100,200,400 is
  1.2983,1.3949,1.4498,1.4792, consistent with a second-order remainder.
- A five-point finite difference of the independently integrated m(beta)
  verifies B=-m''/(2g) within 3.4e-10. The center diagonal constant is
  checked separately; its errors decrease from 6.5e-5 at N=64 to
  2.5e-7 at N=1024.
- code/audit.py checks sample counts, normalizations, every recorded
  resource cap, the bias identity, source-text decoding, and the absence
  of PDFs and paper images. Results are in data/audit.json.

Run from this directory, with Python 3, NumPy, SciPy and Matplotlib installed:

```sh
python3 code/fetch_sources.py
python3 code/validate.py
python3 code/experiment.py --plan main
python3 code/experiment.py --plan large
python3 code/experiment.py --plan calibration
python3 code/exact_means.py
python3 code/analyze.py
python3 code/audit.py
python3 code/build_report.py
```

Run numerical scripts sequentially. They retain the current process's nice
priority if it is at least 10 and otherwise request nice 10. In this run it
was 15. No new packages, scheduled tasks, visible terminals, publications,
pushes or external application changes were created.
