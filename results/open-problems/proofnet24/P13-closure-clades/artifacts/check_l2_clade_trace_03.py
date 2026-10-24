from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
import json, sys

MAX_N = 13
SIZES = tuple(range(2, MAX_N + 1))


def H(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def q(n, i):
    return Fraction(n, 1) / (2 * H(n - 1) * i * (n - i))


for n in range(2, MAX_N + 1):
    assert sum((q(n, i) for i in range(1, n)), Fraction(0)) == 1


@lru_cache(None)
def law(n):
    if n == 1:
        return {tuple(0 for _ in SIZES): Fraction(1)}
    out = defaultdict(Fraction)
    root = tuple(1 if r == n else 0 for r in SIZES)
    for i in range(1, n):
        qi = q(n, i)
        for left, pl in law(i).items():
            for right, pr in law(n-i).items():
                z = tuple(left[k] + right[k] + root[k] for k in range(len(SIZES)))
                out[z] += qi * pl * pr
    assert sum(out.values(), Fraction(0)) == 1
    for z in out:
        assert sum(z[: max(0, n-1)]) == n - 1
        assert all(v == 0 for v in z[max(0, n-1):])
    return dict(out)


def direct(n):
    dist = law(n)
    means = {}
    cov = {}
    for r in SIZES:
        idx = r-2
        means[r] = sum((Fraction(z[idx]) * p for z,p in dist.items()), Fraction(0))
    for r in SIZES:
        ir=r-2
        for s in SIZES:
            is_=s-2
            cov[r,s] = sum(((Fraction(z[ir])-means[r])*(Fraction(z[is_])-means[s])*p for z,p in dist.items()), Fraction(0))
    return means,cov

mu={r:{1:Fraction(0)} for r in SIZES}
mean_checks=0
internal_clade_checks=0
for n in range(2,MAX_N+1):
    dm,_=direct(n)
    for r in SIZES:
        mu[r][n]=Fraction(1 if n==r else 0)+sum((q(n,i)*(mu[r].get(i,Fraction(0))+mu[r].get(n-i,Fraction(0))) for i in range(1,n)),Fraction(0))
        assert mu[r][n]==dm[r]
        mean_checks += 1
    assert sum((mu[r][n] for r in range(2,n+1)), Fraction(0)) == n-1
    internal_clade_checks += 1

@lru_cache(None)
def occupation(n,j):
    if n<j: return Fraction(0)
    if n==j: return Fraction(1)
    return sum((occupation(i,j)/(H(n-1)*(n-i)) for i in range(1,n)), Fraction(0))

eta={}
crec={}
trace_eta={}
trace_c={}
eta_trace_identity_checks=0
green_trace_checks=0
direct_trace_checks=0
support_checks=0
cov_checks=0

for n in range(1,MAX_N+1):
    dm,dcov=direct(n)
    if n==1:
        for r in SIZES:
            for s in SIZES:
                eta[n,r,s]=Fraction(0); crec[n,r,s]=Fraction(0)
        trace_eta[n]=Fraction(0); trace_c[n]=Fraction(0)
        continue

    gr_by_r={r:[mu[r].get(i,Fraction(0))+mu[r].get(n-i,Fraction(0)) for i in range(1,n)] for r in SIZES}
    egr={r:sum((q(n,i)*gr_by_r[r][i-1] for i in range(1,n)),Fraction(0)) for r in SIZES}

    te_diag=Fraction(0)
    te_norm=Fraction(0)
    for i in range(1,n):
        sq=sum(((gr_by_r[r][i-1]-egr[r])**2 for r in SIZES), Fraction(0))
        te_norm += q(n,i)*sq
    te_norm /= n

    for r in SIZES:
        for s in SIZES:
            ep=sum((q(n,i)*gr_by_r[r][i-1]*gr_by_r[s][i-1] for i in range(1,n)),Fraction(0))
            eta[n,r,s]=(ep-egr[r]*egr[s])/n
            if n<max(r,s):
                assert eta[n,r,s]==0
                support_checks += 1
            inherited=sum((crec[i,r,s]/(H(n-1)*(n-i)) for i in range(1,n)),Fraction(0))
            crec[n,r,s]=inherited+eta[n,r,s]
            assert crec[n,r,s]==dcov[r,s]/n
            cov_checks += 1
        te_diag += eta[n,r,r]
    trace_eta[n]=te_diag
    assert te_diag==te_norm
    assert te_diag>=0
    eta_trace_identity_checks += 1

    trace_c[n]=sum((crec[n,r,r] for r in SIZES),Fraction(0))
    direct_trace=sum((dcov[r,r] for r in SIZES),Fraction(0))/n
    assert trace_c[n]==direct_trace
    direct_trace_checks += 1
    green_trace=sum((occupation(n,j)*trace_eta[j] for j in range(2,n+1)),Fraction(0))
    assert trace_c[n]==green_trace
    green_trace_checks += 1

dm4,dc4=direct(4)
assert dc4[2,3] == Fraction(-24,121)

trace_eta_small={str(n): str(trace_eta[n]) for n in range(2,min(MAX_N,8)+1)}
trace_c_small={str(n): str(trace_c[n]) for n in range(2,min(MAX_N,8)+1)}

payload={
    'result':'PASS',
    'arithmetic':'fractions.Fraction exact rational arithmetic only',
    'max_tree_size':MAX_N,
    'mean_recursion_checks':mean_checks,
    'internal_clade_mean_sum_checks':internal_clade_checks,
    'covariance_recursion_checks':cov_checks,
    'eta_support_zero_checks':support_checks,
    'eta_trace_identity_checks':eta_trace_identity_checks,
    'normalized_covariance_direct_trace_checks':direct_trace_checks,
    'green_trace_checks':green_trace_checks,
    'state_counts_by_n':{str(n):len(law(n)) for n in range(1,MAX_N+1)},
    'trace_eta_n_2_to_8':trace_eta_small,
    'trace_C_n_2_to_8':trace_c_small,
    'n4_cov_N2_N3':str(dc4[2,3]),
    'python_version':sys.version.split()[0],
}
print(json.dumps(payload,indent=2,sort_keys=True))
print('ALL L2-TRACE EXACT CHECKS PASSED')
