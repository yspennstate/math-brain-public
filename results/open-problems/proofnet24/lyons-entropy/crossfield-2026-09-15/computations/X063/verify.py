"""Self-checks for X063; exact identities plus explicitly labeled quadrature diagnostics."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, log, exp
from pathlib import Path
import json
import numpy as np


def bareiss(matrix):
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if not n:
        return 1
    previous = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def moment(n, k, t):
    value = F(1)
    for j in range(1, k + 1):
        value *= F(factorial(j+t-1)*factorial(n-k+j-1),
                   factorial(j-1)*factorial(n-k+j+t-1))
    return value


checks = 0
for n in range(2, 81):
    hs = [F(0)]
    for j in range(1, n+1):
        hs.append(hs[-1] + F(1, j))
    fs = [sum((hs[n-k+j]-hs[j] for j in range(1, k+1)), F(0))
          for k in range(n+1)]
    for k in range(n+1):
        assert moment(n,k,1) == F(1,comb(n,k))
        assert comb(n,k)*moment(n,k,2) == F((k+1)*(n-k+1),(n+1)*comb(n,k))
        assert fs[k] == fs[n-k]
        checks += 3
    for r in range(n-1):
        assert 2*fs[r+1]-fs[r]-fs[r+2] == F(1,r+2)+F(1,n-r)
        checks += 1

# Paley's 12-by-12 matrix is constructed and checked directly; no theorem is imported.
residues = {(i*i) % 11 for i in range(1,11)}
h = [[1]*12]
for i in range(11):
    row = [1]
    for j in range(11):
        row.append(-1 if i == j else (1 if (i-j)%11 in residues else -1))
    h.append(row)
assert all(sum(h[i][l]*h[j][l] for l in range(12)) == 12*(i==j)
           for i in range(12) for j in range(12))
checks += 144


def projection_law(columns):
    k = len(columns)
    return {rows: F(bareiss([[h[i][j] for j in columns] for i in rows])**2,12**k)
            for rows in combinations(range(12),k)}


a = projection_law(list(range(5)))
b = projection_law(list(range(7)))
p = projection_law(list(range(6)))
q = projection_law(list(range(5))+[6])
m = {s:(p[s]+q[s])/2 for s in p}
for law in [a,b,p,q,m]:
    assert sum(law.values(), F(0)) == 1
    checks += 1
for i in range(12):
    assert 2*sum(v for s,v in m.items() if i in s) == (
        sum(v for s,v in a.items() if i in s)+sum(v for s,v in b.items() if i in s))
    checks += 1

# An exact rational collision certificate is stronger than needed here:
# N sum m^2 < 4 < (e^2/2)*(7/6), since e>8/3 proves RHS>112/27>4.
collision = comb(12,6)*sum((v*v for v in m.values()),F(0))
assert collision < 4
assert F(1,2)*F(8,3)**2*F(7,6) > 4
checks += 2


def entropy(law):
    return -sum(float(v)*log(float(v)) for v in law.values() if v)


def histogram(law):
    out = {}
    for value in law.values():
        key = str(value)
        out[key] = out.get(key, 0)+1
    return out


def small_log_interval(value, terms=32):
    """Rigorous rational atanh series on [1,2]."""
    assert 1 <= value <= 2
    z=(value-1)/(value+1)
    lower=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    remainder=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lower,lower+remainder


def log_interval(value):
    exponent=0
    while value < 1:
        value*=2
        exponent-=1
    while value > 2:
        value/=2
        exponent+=1
    lo,hi=small_log_interval(value)
    l2,u2=small_log_interval(F(2))
    return (lo+exponent*l2,hi+exponent*u2) if exponent>=0 else (lo+exponent*u2,hi+exponent*l2)


def entropy_interval(law):
    lo=hi=F(0)
    for text,count in histogram(law).items():
        value=F(text)
        if value:
            lower,upper=log_interval(value)
            lo-=count*value*upper
            hi-=count*value*lower
    return lo,hi


ha,hb,hm = map(entropy,[a,b,m])
beta = 2*hm-ha-hb
alo,ahi=entropy_interval(a)
blo,bhi=entropy_interval(b)
mlo,mhi=entropy_interval(m)
beta_lo,beta_hi=2*mlo-ahi-bhi,2*mhi-alo-blo
assert F(4,5)<beta_lo<=beta_hi<F(9,10)
checks+=1
n=12;k=6
harmonic = [sum(F(1,i) for i in range(1,j+1)) for j in range(13)]
f6 = sum(harmonic[6+j]-harmonic[j] for j in range(1,7))
mean_kl = log(924)-float(f6)-log(2)+.5
tau = 2-log(2)+log(7/6)

# Independent deterministic active-sphere quadrature for formula (2), on the twelve-site flag.
base = np.array(h,dtype=float)/np.sqrt(12)
rows = list(combinations(range(12),6))
e = np.array([[np.linalg.det(base[np.ix_(s,list(range(6)))]),
               np.linalg.det(base[np.ix_(s,list(range(5))+[6])])]
              for s in rows])
assert np.max(np.abs(e.T@e-np.eye(2))) < 1e-12
nodes,weights=np.polynomial.legendre.leggauss(100)
phases=np.exp(2j*np.pi*np.arange(256)/256)
average=0.
for node,weight in zip(nodes,weights):
    x=(node+1)/2
    probabilities=np.abs(e[:,0,None]*np.sqrt(x)+e[:,1,None]*np.sqrt(1-x)*phases[None,:])**2
    average+=weight/2*(-np.sum(probabilities*np.log(np.maximum(probabilities,1e-300)))/256)
error=abs(average-(hm+.5-log(2)))
assert error < 1e-6

result = {
    'exact_assertions':checks,
    'scope':'Analytic theorems are in X063.md; floating diagnostics are not universal proofs.',
    'hadamard_matrix':h,
    'hadamard_bottom_entropy_histogram':histogram(a),
    'hadamard_top_entropy_histogram':histogram(b),
    'hadamard_middle_entropy_histogram':histogram(m),
    'hadamard_normalized_middle_collision_exact':str(collision),
    'hadamard_collision_certificate':'Exact: collision < 4 < (e^2/2)*(7/6), using e>8/3.',
    'hadamard_beta_float_diagnostic':beta,
    'hadamard_beta_exact_log_certificate':'4/5 < beta_* < 9/10, by rational atanh-series bounds with 32 terms.',
    'n12r5_mean_middle_KL_formula':f'log(924)-({f6})-log(2)+1/2',
    'n12r5_mean_middle_KL_float':mean_kl,
    'n12r5_threshold_float':tau,
    'n12r5_certified_Haar_measure_lower_bound_float':1-mean_kl/tau,
    'fixed_flag_active_orientation_quadrature_error':error,
}
output=Path(__file__).with_name('verified_output.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:value for key,value in result.items() if 'histogram' not in key and key!='hadamard_matrix'},indent=2))
