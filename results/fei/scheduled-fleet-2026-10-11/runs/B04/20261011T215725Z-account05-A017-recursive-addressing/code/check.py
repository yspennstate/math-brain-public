"""A017-check-v1. Frozen exhaustive exact self-check, no external packages."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
LIMIT = 60
assertions = 0
cases = 0
digest = hashlib.sha256()
max_nphysical = 0
samples = []

def require(condition):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(f"assertion {assertions}, case {cases}")

def parity(x):
    return x.bit_count() & 1

def rank(rows):
    pivots = {}
    for v in rows:
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)

def kernel(rows, n):
    # Exhaustive kernel listing is independent of row elimination (n<=4).
    vectors = [x for x in range(1 << n) if all(parity(x & row) == 0 for row in rows)]
    basis = []
    for v in vectors:
        if rank(basis + [v]) > len(basis):
            basis.append(v)
    require(len(vectors) == 1 << len(basis))
    return basis

def q_parameters(n, code):
    linear = code & ((1 << n) - 1)
    code >>= n
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    edges = [pair for j,pair in enumerate(pairs) if (code >> j) & 1]
    polar = [0] * n
    for i,j in edges:
        polar[i] ^= 1 << j
        polar[j] ^= 1 << i
    return linear, edges, polar

def q_eval(x, linear, edges):
    return parity(x & linear) ^ (sum(((x >> i) & (x >> j) & 1) for i,j in edges) & 1)

def address(rows, x):
    return sum(parity(row & x) << j for j,row in enumerate(rows))

def fwht(values):
    out = list(values)
    step = 1
    while step < len(out):
        for start in range(0,len(out),2*step):
            for j in range(start,start+step):
                u,v = out[j],out[j+step]
                out[j],out[j+step] = u+v,u-v
        step *= 2
    return out

def check(n, rows, qcode, sample=False):
    global cases,max_nphysical
    if time.perf_counter() - START > LIMIT:
        raise RuntimeError("Frozen 60 second cap reached; partial results are not completion")
    linear,edges,polar = q_parameters(n,qcode)
    r = rank(rows)
    basis = kernel(rows,n)
    def bilinear(u,v):
        return sum(parity(polar[i] & v) for i in range(n) if (u >> i) & 1) & 1
    restricted = [sum(bilinear(u,v) << j for j,v in enumerate(basis)) for u in basis]
    k = rank(restricted)
    c = sum(any((row >> i) & 1 for row in rows) for i in range(n))
    b = sum(not any((row >> i) & 1 for row in rows) and polar[i] != 0 for i in range(n))
    d = sum(not any((row >> i) & 1 for row in rows) and polar[i] == 0 and ((linear >> i) & 1) for i in range(n))
    N = n + (1 << len(rows))
    size = 1 << N
    max_nphysical = max(max_nphysical,N)
    table = []
    for v in range(size):
        x = v & ((1 << n)-1)
        z = address(rows,x)
        exponent = q_eval(x,linear,edges) ^ ((v >> (n+z)) & 1)
        table.append(1 if exponent == 0 else -1)
    w = fwht(table)
    support = [s for s,v in enumerate(w) if v]
    require(sum(v*v for v in w) == size*size)
    require(k % 2 == 0)
    require(len(support) == 1 << (2*r+k))
    require({abs(v) for v in w if v} == {1 << (N-r-k//2)})
    require(w[0] == 0)
    H = 2*r+k  # Exact because all nonzero probabilities are 2^(-H).
    expected_I = Fraction(1) + Fraction(c+b,2) + d
    Ispectral = Fraction(sum(s.bit_count()*w[s]*w[s] for s in support),size*size)
    physical = [Fraction(sum(table[v] != table[v ^ (1 << i)] for v in range(size)),size) for i in range(N)]
    require(Ispectral == expected_I == sum(physical))
    for i in range(n):
        target = Fraction(1,2) if any((row >> i)&1 for row in rows) or polar[i] else Fraction((linear >> i)&1)
        require(physical[i] == target)
        require(physical[i] == Fraction(sum(w[s]*w[s] for s in support if (s >> i)&1),size*size))
    reachable = {address(rows,x) for x in range(1 << n)}
    for z in range(1 << len(rows)):
        require(physical[n+z] == (Fraction(1,1 << r) if z in reachable else 0))
    require(k <= c+b-r)
    require(H <= 4*(expected_I-1-d))
    cases += 1
    digest.update(json.dumps([n,rows,qcode,H,str(expected_I)],separators=(',',':')).encode()+b'\n')
    result = dict(n=n,rows=rows,qcode=qcode,rank=r,kernel_polar_rank=k,c=c,b=b,d=d,H=H,I=str(expected_I),atoms=len(support))
    if sample:
        samples.append(result)
    return result

def main():
    planned = sum((1 << (n+n*(n-1)//2))*sum(1 << (a*n) for a in range(3)) for n in range(4)) + 8*1024 + 20
    require(planned == 13069)
    for n in range(4):
        for a in range(3):
            for rows in product(range(1 << n),repeat=a):
                for qcode in range(1 << (n+n*(n-1)//2)):
                    check(n,list(rows),qcode)
    maps = [[],[1],[15],[1,2],[3,12],[5,10],[15,15],[7,14]]
    for rows in maps:
        for qcode in range(1024):
            check(4,rows,qcode)
    rows = [0,0,0]
    cancellation = []
    for t in range(13):
        if t:
            j = (t-1)%3
            rows[j] ^= 1 << j
        cancellation.append(check(3,rows.copy(),0,sample=True))
    qcode = 0
    quad_tower = []
    pairs = [(i,j) for i in range(4) for j in range(i+1,4)]
    rows = [1,2]
    for t in range(7):
        if t:
            qcode ^= 1 << (4+((t-1)%6))
        quad_tower.append(check(4,rows,qcode,sample=True))
    require(cases == planned)
    result = dict(helper_version='A017-check-v1',status='PASS',cases=cases,assertions=assertions,
                  runtime_seconds=time.perf_counter()-START,max_physical_dimension=max_nphysical,
                  arithmetic='integer Walsh, GF2 rank, exact Fraction influence, exact dyadic entropy',
                  case_digest_sha256=digest.hexdigest(),cancellation_tower=cancellation,quadratic_tower=quad_tower,
                  independent_review='PENDING; both implementations written by A017')
    (ROOT/'out'/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cancellation_tower','quadratic_tower')},indent=2))

if __name__ == '__main__':
    main()
