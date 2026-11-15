"""Exact finite pairing audit and independent numerical formula evaluation."""
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]

def cycles(n):
    for tail in itertools.permutations(range(1, n)):
        if tail[0] < tail[-1]:
            v = (0,) + tail
            yield frozenset(tuple(sorted((v[i], v[(i+1)%n]))) for i in range(n))

def falling(d, k):
    return math.prod(range(d-k+1, d+1)) if k <= d else 0

def q(D, edges):
    if 2*edges > D:
        return Fraction(0)
    return Fraction(1, math.prod(D-2*j-1 for j in range(edges)))

def formula(d):
    n, D = len(d), sum(d)
    first = Fraction(math.factorial(n-1),2)*math.prod(falling(v,2) for v in d)*q(D,n)
    second = Fraction(0)
    cs = list(cycles(n))
    for c in cs:
        for e in cs:
            common = list(c & e)
            for mask in range(1 << len(common)):
                a = [0]*n
                k = 0
                for j, (u,v) in enumerate(common):
                    if mask >> j & 1:
                        a[u] += 1
                        a[v] += 1
                        k += 1
                second += math.prod(falling(d[v], 4-a[v]) for v in range(n))*q(D,2*n-k)
    return first, second

def enumerated(d):
    n = len(d)
    labels = [v for v in range(n) for _ in range(d[v])]
    adj = [[0]*n for _ in range(n)]
    cs = list(cycles(n))
    total = hsum = h2sum = 0
    def visit(stubs):
        nonlocal total, hsum, h2sum
        if not stubs:
            h = sum(math.prod(adj[u][v] for u,v in c) for c in cs)
            total += 1
            hsum += h
            h2sum += h*h
            return
        i = stubs[0]
        for j in range(1,len(stubs)):
            u,v = labels[i],labels[stubs[j]]
            adj[u][v] += 1
            if u != v:
                adj[v][u] += 1
            visit(stubs[1:j] + stubs[j+1:])
            adj[u][v] -= 1
            if u != v:
                adj[v][u] -= 1
    visit(list(range(sum(d))))
    return Fraction(hsum,total), Fraction(h2sum,total), total

def numerical():
    mp.mp.dps = 70
    def f(k,x):
        return mp.exp(x) - sum(x**j/mp.factorial(j) for j in range(k))
    root = mp.findroot(lambda x:x**3*f(1,x)-f(2,x)**2, (mp.mpf('4.7'),mp.mpf('4.9')))
    threshold = root*f(2,root)/(2*f(3,root))
    # Independent root bracket, using bisection.
    lo,hi = mp.mpf('4.7'),mp.mpf('4.9')
    for _ in range(220):
        mid = (lo+hi)/2
        if mid**3*f(1,mid)-f(2,mid)**2 > 0:
            lo = mid
        else:
            hi = mid
    assert abs(root-(lo+hi)/2) < mp.mpf('1e-60')
    rows = []
    for c in map(mp.mpf, ('1.5','1.55','1.6','1.75','2','2.25','2.5')):
        mu = 2*c
        if c == mp.mpf('1.5'):
            lam = mp.mpf(0)
            probs = [(3,mp.mpf(1))]
        else:
            lo,hi = mp.mpf('1e-20'),mu
            for _ in range(240):
                mid = (lo+hi)/2
                if mid*f(2,mid)/f(3,mid) < mu:
                    lo = mid
                else:
                    hi = mid
            lam = (lo+hi)/2
            probs = [(k,lam**k/mp.factorial(k)/f(3,lam)) for k in range(3,256)]
        rho = mu-2
        var = sum((k-mu)**2*p for k,p in probs)
        nu = sum(k*(k-1)*p for k,p in probs)/mu
        a = sum((k-2)*(k-3)*p for k,p in probs)/rho
        alpha = (1+a+mp.sqrt((1-a)**2+8*rho))/2
        beta = (1+a-mp.sqrt((1-a)**2+8*rho))/2
        p3 = probs[0][1]
        gap = p3**2*(mu-3)**2/(mu*rho)
        rate = sum(mp.log(k*(k-1))*p for k,p in probs)+((mu-2)*mp.log(mu-2)-mu*mp.log(mu))/2
        assert abs(nu-(rho+1+var/(rho+2))) < mp.mpf('1e-60')
        char_nu = (nu-1)*(nu-a)-2*rho
        assert abs(char_nu+2*var**2/(rho*(rho+2)**2)) < mp.mpf('1e-60')
        corrections = []
        for k in range(1,21):
            base = nu**k/(2*k)
            planted = (alpha**k+beta**k-1)/(2*k)
            delta = planted/base-1
            corrections.append(dict(k=k,lambda_k=str(base),planted_lambda_k=str(planted),delta_k=str(delta),term=str(base*delta**2)))
        rows.append(dict(c=str(c),mu=str(mu),lambda_parameter=str(lam),p3=str(p3),variance=str(var),nu=str(nu),alpha=str(alpha),alpha_minus_nu=str(alpha-nu),e33_gap_per_vertex=str(gap),first_moment_log_rate=str(rate),cycle_corrections=corrections))
    return dict(posa_root=str(root),posa_threshold=str(threshold),rows=rows)

if __name__ == '__main__':
    audits = []
    for d in ([3,3,3,3], [3,3,4,4], [4,4,4]):
        expected = formula(d)
        observed = enumerated(d)
        assert expected == observed[:2], (d,expected,observed)
        audits.append(dict(degrees=d,pairings=observed[2],first_moment=str(expected[0]),second_moment=str(expected[1]),ratio=str(expected[1]/expected[0]**2)))
    output = dict(exact_audits=audits,**numerical())
    (ROOT / 'data/moments.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(dict(exact_audits=audits,posa_threshold=output['posa_threshold']),indent=2))
