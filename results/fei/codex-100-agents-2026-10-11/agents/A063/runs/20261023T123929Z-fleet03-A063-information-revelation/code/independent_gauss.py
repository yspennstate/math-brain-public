"""Independent audit v1: Gauss/autocorrelation constraints, no Walsh transform.
Domain frozen: all alternating matrices n=0..4 and every linear term (1099),
all coordinates/outcomes; sharp extensions k=1..3. Constant phase omitted
because the autocorrelation squares cancel it exactly. <100MB; max300sec.
Exact integer/Fraction only. This is a separate implementation, not external review.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import time

checks = 0
queries = 0
def verify(b, tag):
    global checks
    checks += 1
    if not b:
        raise AssertionError(tag)

def parity(a):
    return a.bit_count() & 1

def polynomial(x, edges, linear):
    return (parity(x & linear)+sum(((x >> a)&1)*((x >> b)&1) for a,b in edges)) & 1

def gauss(n, edges, linear):
    # Direct kernel character constraints; no row elimination, no Fourier transform.
    rows = [sum(1 << (b if a == i else a) for a,b in edges if i in (a,b)) for i in range(n)]
    kernel = [t for t in range(1 << n) if all(parity(t & row) == 0 for row in rows)]
    support = [s for s in range(1 << n) if all(parity(s & t) == polynomial(t,edges,linear) for t in kernel)]
    verify(bool(support), 'nonempty affine coset')
    size = len(support)
    verify(size & (size-1) == 0, 'power-of-two support')
    p = [F(int(s in support),size) for s in range(1 << n)]
    marginals = [sum(p[s] for s in range(1 << n) if s >> i & 1) for i in range(n)]
    Q = []
    for s in range(1 << n):
        mass = F(1)
        for i,d in enumerate(marginals):
            mass *= d if s >> i & 1 else 1-d
        Q.append(mass)
    rank = size.bit_length()-1
    active = sum(bool(row) for row in rows)
    return p,Q,rank,active,rows

def exactlog(a):
    a = F(a)
    u,v = a.numerator,a.denominator
    verify(u > 0 and u & (u-1) == 0 and v & (v-1) == 0,'dyadic log')
    return u.bit_length()-v.bit_length()

def D(p,q):
    return sum((a*exactlog(a/b) for a,b in zip(p,q) if a),F(0))

def project(s,i):
    return (s & ((1 << i)-1)) | ((s >> (i+1)) << i)

def edge(n,edges,linear,i):
    global queries
    queries += 1
    p,Q,r,m,rows = gauss(n,edges,linear)
    child_edges = [(a-int(a>i),b-int(b>i)) for a,b in edges if i not in (a,b)]
    q,Qbar = [F(0)]*(1 << (n-1)),[F(0)]*(1 << (n-1))
    for s in range(1 << n):
        q[project(s,i)] += p[s]
        Qbar[project(s,i)] += Q[s]
    expected_E = None
    prices = []
    for bit in (0,1):
        child_linear = project(linear,i)
        if bit:
            child_linear ^= project(rows[i],i)
        pb,product,rb,mb,_ = gauss(n-1,child_edges,child_linear)
        ref = [Qbar[s] * (pb[s]/(2*q[s]) if q[s] else F(1,2)) for s in range(len(q))]
        mass = sum(ref)
        verify(mass == F(1,2),'true outcome normalization retains fair zero rows')
        ref = [a/mass for a in ref]
        Kold,Knew = D(pb,ref),D(pb,product)
        E = D(p,Q)-D(q,Qbar)
        sigma = Knew-Kold
        if rows[i]:
            drop = (r-rb)//2
            isolates = m-1-mb
            verify(E == 1-drop and sigma == drop-isolates,'independent local payment formula')
        else:
            verify(E == sigma == 0,'isolated deletion')
        verify(Kold == D(p,Q)-E,'chain rule with fair outcome')
        verify(Knew == mb-rb,'actual product admission')
        prices.append(sigma)
        if expected_E is None:
            expected_E = E
        else:
            verify(E == expected_E and prices[0] == prices[1],'both outcomes same cost')
    return prices[0]

def main():
    start = time.monotonic()
    cases = 0
    for n in range(5):
        pairs = list(itertools.combinations(range(n),2))
        for mask in range(1 << len(pairs)):
            edges = [p for j,p in enumerate(pairs) if mask >> j & 1]
            for ell in range(1 << n):
                p,Q,r,m,_ = gauss(n,edges,ell)
                verify(D(p,Q) == m-r,'root admission')
                for i in range(n):
                    edge(n,edges,ell,i)
                cases += 1
    sharp = []
    for k in range(1,4):
        m,n = k+2,2*k+2
        edges = [(0,j) for j in range(1,m)]+[(m+j-2,j) for j in range(2,m)]
        # Audit zero branch of each controller; numerical prices independent of branch,
        # and exhaustive local audit above separately includes all linear terms.
        total = 0
        for t in range(k):
            total += edge(n,edges,0,m)
            edges = [(a-int(a>m),b-int(b>m)) for a,b in edges if m not in (a,b)]
            n -= 1
        p,Q,r,active,_ = gauss(n,edges,0)
        verify(total == k == D(p,Q) and r == 2 and active == m,'sharp prefix independent reconstruction')
        sharp.append({'k':k,'price':int(total)})
    result = {'status':'PASS','cases':cases,'queries':queries,'assertions':checks,'sharp':sharp,
              'method':'kernel annihilator constraints, no Walsh transform; exact Fraction probabilities',
              'elapsed_seconds':round(time.monotonic()-start,3),
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).resolve().parent.parent.joinpath('out','independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
