"""Independent prefix simulation against density integrals, never claim code.

One process, one numerical thread; inherited nice must be >=10.
The n=2 targets are integrations of the complete ordered density.
At beta=2, n=3,6 targets use the orthogonal-polynomial determinantal density.
"""
import os
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[variable] = '1'
import csv
import hashlib
import json
import math
import pathlib
import resource
import time

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import beta as beta_function, digamma, gammainc, gammaln, eval_genlaguerre
from scipy.stats import chisquare, gamma, kstest, norm

ROOT = pathlib.Path(__file__).resolve().parents[1]
SEED = 40002113112026
SAMPLES = 50000
NMAX = 6
TESTS, DETAILS, CHECKS = [], [], {}

def record(kind, beta, a, n, statistic, p):
    TESTS.append(dict(kind=kind, beta=beta, a=a, n=n, statistic=float(statistic), p=float(p)))

def moment_test(kind, beta, a, n, samples, target):
    se = samples.std(ddof=1) / math.sqrt(len(samples))
    if se == 0:
        CHECKS[f'uninformative_{kind}_beta{beta}_a{a}_n{n}'] = {
            'observed': float(samples.mean()), 'target': float(target),
            'reason': 'zero empirical variance; no normal approximation test'}
        return
    z = (samples.mean() - target) / se
    record(kind, beta, a, n, z, 2 * norm.sf(abs(z)))
    DETAILS.append(dict(kind=kind, beta=beta, a=a, n=n, empirical=float(samples.mean()),
                        target=float(target), se=float(se), z=float(z)))

def n2_cdf(x, y, beta, a):
    """P(lambda_min<=x,lambda_max<=y) from the ordered Laguerre density.

    t=lambda1+lambda2, v=((lambda2-lambda1)/t)^2:
    t ~ Gamma(2(alpha+1)+beta, rate=beta/2),
    v ~ Beta((beta+1)/2, alpha+1), independently.
    Quad's endpoint-weight option handles the integrable hard-edge singularity.
    """
    if x <= 0 or y <= 0:
        return 0.0
    p, q = (beta + 1) / 2, beta * (a + 1) / 2
    shape, rate = 2 * q + beta, beta / 2
    def integrand(v):
        root = math.sqrt(v)
        t1 = math.inf if math.isinf(x) or root == 1 else 2 * x / (1 - root)
        t2 = math.inf if math.isinf(y) else 2 * y / (1 + root)
        return gammainc(shape, rate * min(t1, t2)) / beta_function(p, q)
    # Split at the kink; retain endpoint weights after affine rescaling.
    if math.isfinite(x) and math.isfinite(y) and x < y:
        kink = ((y - x) / (x + y)) ** 2
        low = quad(lambda u: kink**p * (1-kink*u)**(q-1) * integrand(kink*u),
                   0, 1, weight='alg', wvar=(p-1, 0), epsabs=2e-10, epsrel=2e-9, limit=150)[0]
        high = quad(lambda u: (1-kink)**q * (kink+(1-kink)*u)**(p-1)
                    * integrand(kink+(1-kink)*u), 0, 1,
                    weight='alg', wvar=(0, q-1), epsabs=2e-10, epsrel=2e-9, limit=150)[0]
        return low + high
    return quad(integrand, 0, 1, weight='alg', wvar=(p - 1, q - 1),
                epsabs=2e-10, epsrel=2e-9, limit=150)[0]

def n2_tests(eigenvalues, beta, a):
    scale = 2 * (a + 2)
    quantiles = []
    for j in range(2):
        def marginal(x):
            return n2_cdf(x, math.inf, beta, a) if j == 0 else n2_cdf(math.inf, x, beta, a)
        upper = scale
        while marginal(upper) < .8:
            upper *= 2
        edges = [0.0] + [brentq(lambda x: marginal(x) - p, 0, upper,
                               xtol=2e-12) for p in (.2, .4, .6, .8)] + [math.inf]
        quantiles.append(edges)
        counts = np.histogram(eigenvalues[:, j], bins=edges)[0]
        result = chisquare(counts, np.full(5, SAMPLES / 5))
        record('n2_ordered_marginal_integral_' + str(j + 1), beta, a, 2, result.statistic, result.pvalue)
    cdf = np.array([[n2_cdf(x, y, beta, a) for y in quantiles[1]] for x in quantiles[0]])
    probabilities = np.diff(np.diff(cdf, axis=0), axis=1)
    if probabilities.min() < -1e-7 or abs(probabilities.sum() - 1) > 1e-7:
        raise AssertionError('Invalid integrated joint probabilities')
    probabilities = np.maximum(probabilities, 0)
    counts = np.histogram2d(eigenvalues[:, 0], eigenvalues[:, 1], bins=quantiles)[0]
    # Pool all cells with small expected count; preserve total sample size.
    keep = SAMPLES * probabilities >= 10
    expected, observed = list((SAMPLES * probabilities)[keep]), list(counts[keep])
    if (~keep).any() and probabilities[~keep].sum() > 0:
        expected.append(SAMPLES * probabilities[~keep].sum())
        observed.append(counts[~keep].sum())
    expected = np.array(expected)
    expected *= sum(observed) / expected.sum()
    result = chisquare(observed, expected)
    record('n2_joint_5x5_density_integral', beta, a, 2, result.statistic, result.pvalue)
    CHECKS[f'n2_beta{beta}_a{a}'] = dict(edges=quantiles, probabilities=probabilities.tolist(), counts=counts.tolist())

def dpp_interval_matrix(n, alpha, left, right):
    def phi(k, x):
        if x == 0:
            x = 1e-300
        logfactor = .5 * (alpha * math.log(x) - x + gammaln(k + 1) - gammaln(k + alpha + 1))
        return math.exp(logfactor) * eval_genlaguerre(k, alpha, x)
    mat = np.empty((n, n))
    for i in range(n):
        for j in range(i + 1):
            # x=u^2 removes the square-root hard-edge singularity for alpha=-1/2.
            value = quad(lambda u: 2*u * phi(i, u*u) * phi(j, u*u),
                         math.sqrt(left), math.sqrt(right),
                         epsabs=2e-9, epsrel=2e-9, limit=150)[0]
            mat[i, j] = mat[j, i] = value
    return mat

def dpp_tests(eigenvalues, a, n):
    edges = [0, 1, 4, 9, math.inf]
    matrices = [dpp_interval_matrix(n, a, left, right) for left, right in zip(edges[:-1], edges[1:])]
    normalization_error = np.max(np.abs(sum(matrices) - np.eye(n)))
    if normalization_error > 1e-7:
        raise AssertionError('DPP integral normalization')
    CHECKS[f'dpp_n{n}_a{a}_orthogonality_error'] = float(normalization_error)
    counts = np.stack([np.sum((eigenvalues > left) & (eigenvalues <= right), axis=1)
                       for left, right in zip(edges[:-1], edges[1:])], axis=1)
    for i, matrix in enumerate(matrices):
        moment_test(f'beta2_rho1_bin{i}', 2, a, n, counts[:, i], np.trace(matrix))
        for j in range(i, len(matrices)):
            values = counts[:, i] * (counts[:, j] - (i == j))
            target = np.trace(matrix) * np.trace(matrices[j]) - np.trace(matrix @ matrices[j])
            moment_test(f'beta2_rho2_bins{i}_{j}', 2, a, n, values, target)

def main():
    start = time.monotonic()
    nice = os.getpriority(os.PRIO_PROCESS, 0)
    if nice < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    rng = np.random.default_rng(SEED)
    max_reversal = max_nesting = max_interlace = 0.0
    for beta in (.5, 1., 2., 3.7):
        for a in (-.5, 1.25):
            # One set of primitive variables per sample, shared by every prefix.
            degrees_d = beta * (a + np.arange(1, NMAX + 1))
            degrees_l = beta * np.arange(1, NMAX)
            d = np.sqrt(rng.chisquare(degrees_d, size=(SAMPLES, NMAX)) / beta)
            ell = np.sqrt(rng.chisquare(degrees_l, size=(SAMPLES, NMAX - 1)) / beta)
            B = np.zeros((SAMPLES, NMAX, NMAX))
            idx = np.arange(NMAX)
            B[:, idx, idx] = d
            B[:, idx[1:], idx[:-1]] = ell
            L = B @ B.swapaxes(1, 2)
            previous = None
            for n in range(1, NMAX + 1):
                block = L[:, :n, :n]
                finite_product = B[:, :n, :n] @ B[:, :n, :n].swapaxes(1, 2)
                max_nesting = max(max_nesting, np.max(np.abs(block - finite_product)))
                eigenvalues = np.linalg.eigvalsh(block)
                if previous is not None:
                    max_interlace = max(max_interlace, np.max(eigenvalues[:, :-1] - previous),
                                        np.max(previous - eigenvalues[:, 1:]))
                previous = eigenvalues
                if n not in (1, 2, 3, 6):
                    continue
                alpha = beta * (a + 1) / 2 - 1
                shape = n * (alpha + 1) + beta * n * (n - 1) / 2
                result = kstest(eigenvalues.sum(axis=1), gamma(shape, scale=2 / beta).cdf)
                record('trace_density_gamma', beta, a, n, result.statistic, result.pvalue)
                # Density's Mellin/Selberg integral, not a second DE matrix draw.
                target = np.sum(digamma(alpha + 1 + beta / 2 * np.arange(n))) + n * math.log(2 / beta)
                logdet = np.log(eigenvalues).sum(axis=1)
                moment_test('logdet_density_Mellin', beta, a, n, logdet, target)
                target = n * (n + a) * (2 * n + a - 1 + 2 / beta)
                moment_test('sum_eigenvalue_squares_density_IBP', beta, a, n,
                            (eigenvalues ** 2).sum(axis=1), target)
                if n == 2:
                    n2_tests(eigenvalues, beta, a)
                if beta == 2 and n in (3, 6):
                    dpp_tests(eigenvalues, a, n)
            # Deterministic algebra, on the same primitive entries.
            C = B[:100].swapaxes(1, 2)[:, ::-1, ::-1]
            right = (C.swapaxes(1, 2) @ C)[:, ::-1, ::-1]
            max_reversal = max(max_reversal, np.max(np.abs(L[:100] - right)))
            print('finished', beta, a, flush=True)
    pvalues = np.array([row['p'] for row in TESTS])
    order = np.argsort(pvalues)
    adjusted = np.maximum.accumulate((len(TESTS) - np.arange(len(TESTS))) * pvalues[order])
    for index, value in zip(order, adjusted):
        TESTS[index]['holm_p'] = min(1.0, float(value))
    result = dict(seed=SEED, samples=SAMPLES, nmax=NMAX, nice=os.getpriority(os.PRIO_PROCESS, 0),
                  threads={key: os.environ[key] for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')},
                  numpy=np.__version__, tests=len(TESTS), holm_rejections=sum(row['holm_p'] < .05 for row in TESTS),
                  min_raw_p=float(min(pvalues)), max_abs_moment_z=max(abs(row['z']) for row in DETAILS),
                  nesting_error=float(max_nesting), reversal_error=float(max_reversal),
                  interlace_violation=float(max_interlace), seconds=time.monotonic()-start,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
    (ROOT/'data'/'referee_summary.json').write_text(json.dumps(result, indent=2))
    (ROOT/'data'/'density_integrals.json').write_text(json.dumps(CHECKS, indent=2))
    for filename, rows in (('referee_tests.csv', TESTS), ('referee_moments.csv', DETAILS)):
        with (ROOT/'data'/filename).open('w') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
