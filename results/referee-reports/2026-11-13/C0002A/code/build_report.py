"""Assemble the self-contained report from saved proof, literature, and data."""
import csv
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def readcsv(name):
    with (ROOT/'data'/name).open() as f:return list(csv.DictReader(f))

summary=readcsv('summary.csv')
exact=readcsv('exact_means.csv')
fits=json.loads((ROOT/'data'/'fits.json').read_text())
constants=json.loads((ROOT/'data'/'continuum_constants.json').read_text())
meta=[json.loads((ROOT/'data'/f'metadata_{p}.json').read_text()) for p in ['main','large','calibration']]
fields=sum(sum(reps for _,reps in m['plan']) for m in meta)
peak=max(m['peak_bytes'] for m in meta)

numeric=r'''The sampler diagonalizes I-P in the orthonormal sine basis on
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

'''
numeric+=f'''There are {fields:,} independent fields, with four lambda values
(0.2, 0.4, 0.6, 0.8) measured on each, for {4*fields:,} count observations.
The main and independent calibration batches use float64. The three N=8192
fields and one N=16384 field use float32. The largest grid contains
268,402,689 random sites. It is the largest dyadic grid whose float32
field fits below 4 GB; the next, N=32768, requires more than 4 GB for
the field alone. This is not a claim to optimize all possible grid sizes
or all sampling algorithms under the memory cap.

Each FFT uses one worker, and numerical library thread limits are set to
one. Priority was inherited as nice 15, below the requested priority 10;
raising it to exactly 10 was disallowed, so it remained 15. The largest
observed process peak was {peak/1e9:.6f} GB. The largest-grid preflight
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
'''
for row in summary:
    if int(row['N'])==512:
        numeric+='| '+ ' | '.join([row['lambda']]+[f"{float(row[k]):.6f}" for k in ['mean','mean_se','variance','q50','q95','exact_mean']])+' |\n'
numeric+=r'''
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
'''
for row in exact:
    if int(row['N'])==8192:
        numeric+='| '+' | '.join([row['lambda']]+[f"{float(row[k]):.6f}" for k in ['m','B','EX','log_bias']])+' |\n'
numeric+=r'''
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
'''
for fit in fits:
    lo,hi=fit['bootstrap_percentiles']
    numeric+=f"| {fit['lambda']:.1f} | {fit['effective_RMSE_log_exponent']:.3f} | [{lo:.3f}, {hi:.3f}] | {fit['exact_bias_effective_log_exponent']:.3f} |\n"
numeric+=r'''
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
'''
(ROOT/'NUMERICS.md').write_text('# Numerical evidence and limitations\n\n'+numeric)

report=(ROOT/'REPORT.md').read_text()
front=report.split('## Literature result already located')[0].split('## Full proofs')[0]
front=front.replace('Work in progress. Started 13 November 2026, approximately 06:58 Asia/Tbilisi.\nThis file is saved during the investigation; numerical and bibliographic\nsections will be completed below. No claim to a complete solution is made.',
'''Task: “Open problem C0002”, received 13 November 2026, approximately
06:58 Asia/Tbilisi. This is a partial research result. Printed work answers
substantial deviation regimes; the work here proves a finite-lattice
comparison rate and a first-order mean bias. The limiting second-order
fluctuation law and a matching upper rate to the continuum law remain
unestablished here. The numerical investigation is complete within the
stated resource limits.''')
front=front.replace('arXiv version. In particular,','arXiv version (the reproduced Springer volume places it on p. 392). In particular,')
front=front.replace('Full proofs are being recorded in the next section.','Full proofs follow. The literature audit gives the exact source results and their scope.')
proof=(ROOT/'PROOFS.md').read_text().split('\n',1)[1].strip()
lit=(ROOT/'LITERATURE.md').read_text().split('\n',1)[1].strip()
report=front.rstrip()+'\n\n## Full proofs\n\n'+proof+'\n\n## Computation and checks\n\n'+numeric+'\n\n## Literature audit and exact references\n\n'+lit+'\n'
report+='''
## Remaining problem

A matching quantitative upper bound to the law of Z_lambda(D)/beta
requires control of the finite-lattice exponential mass against a
specified continuum GMC approximation. Theorem A does not supply that
control. A fluctuation law around the random limit requires a coupling
and a proof of the second-order expansion, beyond its mean. Existing
upper-deviation exponents and lower-deviation bounds cover important
vanishing-probability events, but do not settle all shrinking-threshold
or moderate-deviation regimes. These are the reasons for the PARTIAL
status. No solution of all three requests is claimed.
'''
assert report.splitlines()[0]=='PARTIAL'
(ROOT/'REPORT.md').write_text(report)
print('Wrote REPORT.md and NUMERICS.md; independent fields:',fields)
