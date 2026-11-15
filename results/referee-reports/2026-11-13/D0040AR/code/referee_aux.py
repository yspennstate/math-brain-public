"""Independent cross-checks of source algebra and auxiliary claims."""
import os
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[variable] = '1'
import json
import math
import pathlib
from fractions import Fraction
import numpy as np
from scipy.special import betaln, gammaln
from scipy.stats import gamma, kstest

ROOT = pathlib.Path(__file__).resolve().parents[1]
rng = np.random.default_rng(13112026)
result = {'nice': os.getpriority(os.PRIO_PROCESS, 0)}
assert result['nice'] >= 10

# Second derivation of trace, trace-square and density normalizations.
identities = []
normalization_errors = []
for beta in (.5, 1, 2, 3.7):
    for a in (-.5, 1.25):
        theta = beta / 2
        alpha = theta * (a + 1) - 1
        for n in (1, 2, 3, 6):
            di = a + np.arange(1, n+1)
            li = np.arange(0, n)
            # E sum diagonal^2 + 2 sum offdiag^2, from gamma primitive moments.
            m2 = np.sum((di + li)**2 + 2/beta*(di + li))
            m2 += 2*np.sum((a+np.arange(1, n))*np.arange(1, n))
            density_target = n*(n+a)*(2*n+a-1+2/beta)
            identities.append(abs(m2-density_target))
        K = 2*(alpha+1)+beta
        logZ_selberg = -math.log(2)-K*math.log(beta/2)+gammaln(alpha+1)+gammaln(alpha+1+theta)+gammaln(1+beta)-gammaln(1+theta)
        logZ_tu = gammaln(K)-K*math.log(beta/2)+betaln((beta+1)/2, alpha+1)-(alpha+1)*math.log(4)
        normalization_errors.append(abs(logZ_selberg-logZ_tu))
result['max_trace2_independent_derivations_error'] = max(identities)
result['max_n2_log_normalization_identity_error'] = max(normalization_errors)

# KN theorem (1.11)-(1.12): derive scalar means via rational beta moments.
means = []
for beta in (Fraction(1,2), Fraction(1), Fraction(2), Fraction(4)):
    p, q = Fraction(3,10), Fraction(11,10)
    S, d, theta = p+q+2, p-q, beta/2
    m_t = (theta-S)/(theta+S)
    direct = ((1-m_t)*d/S-(1+m_t)*d/(S+2*theta)+2)/4
    simplified = Fraction(1,2)+d/(2*(S+beta))
    assert direct == simplified
    means.append({'beta': str(beta), 'candidate': str(direct), 'target': str((p+1)/S)})
result['KN_exact_means'] = means
for S in (Fraction(2), Fraction(17,5)):
    for theta in (Fraction(1,4), Fraction(1), Fraction(2)):
        var = (S+theta*(theta+1)/(S+2*theta+1))/(4*(S+theta)*(S+theta+1))
        assert var == 1/(4*(S+2*theta+1))
result['KN_symmetric_variance_identity'] = 'exact rational agreement for six cases; proof by factoring numerator'

# Generalized residue Jacobian, independent numerical finite difference.
residue_error = jacobian_error = 0.0
for n in (2, 3, 5):
    for repeat in range(20):
        x = np.cumsum(rng.uniform(1, 2, n))
        y = x[:-1]+rng.uniform(.2,.8,n-1)*np.diff(x)
        def residues(y):
            return np.array([np.prod(x[i]-y)/np.prod(x[i]-np.delete(x,i)) for i in range(n)])
        q = residues(y)
        residue_error = max(residue_error, abs(q.sum()-1))
        eps = 1e-6
        jac = np.column_stack([(residues(y+eps*np.eye(n-1)[j])-residues(y-eps*np.eye(n-1)[j]))[:n-1]/(2*eps) for j in range(n-1)])
        def vandermonde(z):
            return math.prod(z[j]-z[i] for i in range(len(z)) for j in range(i+1,len(z)))
        target = vandermonde(y)/vandermonde(x)
        jacobian_error = max(jacobian_error, abs(abs(np.linalg.det(jac))/target-1))
result['residue_sum_error'] = residue_error
result['jacobian_relative_error'] = jacobian_error

# Antisymmetric N=2,3 densities reduce exactly to one Gamma law for lambda^2.
antisymmetric = []
for beta in (.5,1,2,3.7):
    for n in (2,3,4,7):
        r2 = rng.gamma(beta*np.arange(1,n)/4, 1, size=(40000,n-1))
        H = np.zeros((len(r2),n,n))
        j = np.arange(n-1)
        H[:,j,j+1] = H[:,j+1,j] = np.sqrt(r2)
        ev = np.linalg.eigvalsh(H)
        positive = ev[:,-(n//2):]
        stat = (positive**2).sum(axis=1)
        eta = beta/2-1 if n%2==0 else 3*beta/2-1
        m = n//2
        # Homogeneity after squaring the positive eigenvalues.
        shape = m*(eta+1)/2+beta*m*(m-1)/2
        assert abs(shape-beta*n*(n-1)/8)<1e-12
        ks = kstest(stat,gamma(shape).cdf)
        antisymmetric.append({'beta':beta,'N':n,'shape':shape,'KS':float(ks.statistic),'p':float(ks.pvalue),
                              'trace_identity_error':float(np.max(np.abs(stat-r2.sum(axis=1))))})
result['antisymmetric_tests'] = antisymmetric

# Confirm submitted data summaries without executing or importing claim code.
claimed = json.loads((ROOT/'claim_files/data/checks.json').read_text())
rows = claimed['positive_checks']
p = np.array([row['p'] for row in rows])
order = np.argsort(p)
adjusted = np.minimum(1,np.maximum.accumulate((len(p)-np.arange(len(p)))*p[order]))
result['claim_data_only'] = {'tests':len(p),'min_p':float(p.min()),'holm_rejections':int(np.sum(adjusted<.05)),
                           'holm_max_error':float(max(abs(row['holm_p']-v) for row,v in zip(np.array(rows,dtype=object)[order],adjusted)))}
(ROOT/'data/referee_aux.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
