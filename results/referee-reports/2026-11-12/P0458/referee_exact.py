"""Independent exact checks. No imports from the authors' programs.

For one root edge with score u, its endpoints independently accept with
probability f(u)=P(Bin(n-2,u)<k). Thus ED=(n-1) integral f^2.
For two root edges u<v, the root accepts both with probability
C(v)=P(Bin(n-3,v)<=k-2). The other endpoints share just W; integrating W
gives u*B(u)*B(v)+(v-u)*A(u)*B(v)+(1-v)*A(u)*A(v).
All polynomials and integrals below are over the rationals.
"""
from fractions import Fraction as Q
from math import comb, factorial
import json

def add(*ps):
    z = [Q(0)] * max(map(len, ps))
    for p in ps:
        for i, a in enumerate(p): z[i] += a
    return z

def mul(p, q):
    z = [Q(0)] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q): z[i+j] += a*b
    return z

def scale(p, a): return [a*x for x in p]
def anti(p): return [Q(0)] + [a/Q(i+1) for i,a in enumerate(p)]
def integ(p): return sum(anti(p), Q(0))

def cdf(m, h):
    p = [Q(0)] * (m+1)
    for j in range(min(h,m)+1):
        for l in range(m-j+1):
            p[j+l] += Q(comb(m,j)*comb(m-j,l)*(-1)**l)
    return p

def moments(n,k):
    f = cdf(n-2,k-1)
    ed = (n-1)*integ(mul(f,f))
    if k == 1:
        pair = Q(0)
    else:
        a,b = cdf(n-3,k-1),cdf(n-3,k-2)
        ua,ub = mul([0,1],a),mul([0,1],b)
        inner = add(mul(b,anti(ub)), mul(mul([0,1],b),anti(a)),
                    scale(mul(b,anti(ua)),-1),
                    mul(mul([1,-1],a),anti(a)))
        pair = 2*integ(mul(b,inner))
    vd = ed+(n-1)*(n-2)*pair-ed*ed
    return Q(k)-ed,vd

def main():
    all_results = {}
    for n in range(3,10):
        row = [moments(n,k)[0] for k in range(1,n)]
        assert row[:-1] == row[-2::-1]
        print('n=%d EH(k=1,...,n-1): '%n + ', '.join(map(str,row)), 'symmetry PASS')
    for n in (4,5,7,12):
        for k in range(1,n-1):
            eh,v = moments(n,k)
            print(f'n={n} k={k} ED={Q(k)-eh} VD={v} decimals {float(Q(k)-eh):.12f} {float(v):.12f}')
            all_results[f'{n},{k}'] = dict(eh=str(eh), var=str(v))
    for n,k in ((10,8),(20,18),(40,38),(80,78),(40,20),(80,30)):
        eh,v = moments(n,k)
        print(f'n={n} k={k} EH={float(eh):.12f} VH={float(v):.12f}')
        all_results[f'{n},{k}'] = dict(eh=str(eh), var=str(v))
    for r in (1,2,5):
        mu = Q(r*comb(2*r,r),4**r)
        sec = sum((Q((r-l)*(r-m)*factorial(r-1+l+m),
                     factorial(r-1)*factorial(l)*factorial(m)*3**(r+l+m))
                   for l in range(r) for m in range(r)),Q(0))
        var = mu+sec-mu*mu
        print(f'r={r} mu={mu} M2={sec} var={var} decimals {float(mu):.12f} {float(var):.12f}')
    with open('referee_exact.json','w') as f: json.dump(all_results,f,indent=2)

if __name__ == '__main__': main()
