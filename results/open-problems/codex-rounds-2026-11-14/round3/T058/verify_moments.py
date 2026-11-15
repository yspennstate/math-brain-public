"""Exact overlap sums, exhaustive small graphs, and asymptotic diagnostics."""
import itertools
import json
import math
import os
import resource
import time
from fractions import Fraction
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
start = time.monotonic()

def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0

def edges(k):
    return k*(k-1)//2

def mean(n, k):
    return Fraction(choose(n,k), 2**edges(k))

def conditional_covariance_numerator(n, K, l):
    # Cov(X_K,X_l) / mu_K = S / 2**binom(l,2).
    return sum(choose(K,j)*choose(n-K,l-j)*(2**edges(j)-1)
               for j in range(2,l+1))

def overlap_covariance(n, K, l):
    return mean(n,K)*Fraction(conditional_covariance_numerator(n,K,l),
                              2**edges(l))

def direct_second_moment(n, K, l):
    # Independently sum the joint moment INCLUDING disjoint pairs, then subtract.
    joint = sum(choose(K,j)*choose(n-K,l-j)*2**edges(j)
                for j in range(l+1))
    return mean(n,K)*Fraction(joint,2**edges(l))-mean(n,K)*mean(n,l)

def exhaustive(n):
    pairs = list(itertools.combinations(range(n),2))
    index = {e:i for i,e in enumerate(pairs)}
    masks = {}
    for k in (2,3,4):
        masks[k] = [sum(1<<index[e] for e in itertools.combinations(S,2))
                    for S in itertools.combinations(range(n),k)]
    sums = dict.fromkeys((2,3,4),0)
    products = dict.fromkeys(((2,2),(3,3),(4,4),(3,2),(4,3)),0)
    graphs = 2**len(pairs)
    for graph in range(graphs):
        counts = {k:sum((graph & mask)==0 for mask in masks[k])
                  for k in masks}
        for k in sums:
            sums[k] += counts[k]
        for K,l in products:
            products[K,l] += counts[K]*counts[l]
    for k in sums:
        assert Fraction(sums[k],graphs)==mean(n,k)
    checked = []
    for K,l in products:
        actual = Fraction(products[K,l],graphs)-mean(n,K)*mean(n,l)
        assert actual == overlap_covariance(n,K,l)
        assert actual == direct_second_moment(n,K,l)
        checked.append(dict(K=K,l=l,covariance=str(actual)))
    return dict(n=n,graphs=graphs,checks=checked)

small = [exhaustive(5),exhaustive(6)]

ell = math.log(2)
def f_log(y):
    return 2/ell*(y-math.log(y)+math.log(ell)+1)-1

def n_at_phase(exponent, phase):
    target = math.floor(f_log(exponent*ell))+phase
    lo,hi = max(2.,(exponent-2)*ell),(exponent+2)*ell
    assert f_log(lo)<target<f_log(hi)
    for _ in range(70):
        mid=(lo+hi)/2
        if f_log(mid)<target:
            lo=mid
        else:
            hi=mid
    return round(math.exp((lo+hi)/2))

rows=[]
for exponent in (20,40,80,160):
    for target_phase in (.25,.5,.75):
        n=n_at_phase(exponent,target_phase)
        f=f_log(math.log(n))
        k=math.floor(f)
        t=f-k
        v_k=Fraction(conditional_covariance_numerator(n,k,k),2**edges(k))
        v_l=Fraction(conditional_covariance_numerator(n,k-1,k-1),2**edges(k-1))
        c=Fraction(conditional_covariance_numerator(n,k,k-1),k*2**edges(k-1))
        assert v_k>=1-Fraction(1,2**edges(k))
        assert v_l>=1-Fraction(1,2**edges(k-1))
        assert c>=1-Fraction(1,2**edges(k-1))
        for K,l in ((k,k),(k-1,k-1),(k,k-1)):
            assert overlap_covariance(n,K,l)==direct_second_moment(n,K,l)
        exact_scale=math.sqrt(Fraction(k*(n-k+1),2**(k-1)))
        rho=float(c)/math.sqrt(float(v_k)*float(v_l))*exact_scale
        elementary_scale=2*math.sqrt(2)/math.e*2**(t/2)*math.log2(n)**1.5/math.sqrt(n)
        rows.append(dict(log2_n=round(math.log2(n),6), k=k,phase=round(t,8),
                         var_k_over_mean=float(v_k),var_km1_over_mean=float(v_l),
                         cov_over_k_mu=float(c),correlation=rho,
                         correlation_over_exact_scale=rho/exact_scale,
                         exact_scale_over_elementary_scale=exact_scale/elementary_scale))

# Finite convergence is a diagnostic, with no prescribed rate at these n.
result=dict(status='all checks passed',nice=os.getpriority(os.PRIO_PROCESS,0),
            exhaustive=small,diagnostics=rows,
            elapsed_seconds=time.monotonic()-start,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path('moment_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
