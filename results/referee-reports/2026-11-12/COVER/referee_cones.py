"""Independent exact certificate audit. No imports from authors' code.

Exponents are packed in base 32; determinants use recursive Laplace expansion.
The quadratic numerator is computed using a bordered determinant, not adjugates.
Run with: OPENBLAS_NUM_THREADS=1 nice -n 15 python3 -B referee_cones.py
"""
import gzip
import hashlib
import itertools as it
import json
import math
import resource
import signal
import time
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(280)
START = time.monotonic()
U = [1 << (5*i) for i in range(6)]
EDGES = list(it.combinations(range(4), 2))

def add(*polys):
    r = {}
    for p in polys:
        for e, c in p.items():
            r[e] = r.get(e, 0) + c
    return {e:c for e,c in r.items() if c}

def scale(p, c):
    return {e:c*v for e,v in p.items() if c*v}

def mul(a,b):
    r = {}
    for e,c in a.items():
        for f,d in b.items():
            r[e+f] = r.get(e+f,0) + c*d
    return {e:c for e,c in r.items() if c}

def prod(polys):
    r = {0:1}
    for p in polys:
        r = mul(r,p)
    return r

def det(m):
    if not m:
        return {0:1}
    return add(*(scale(mul(m[0][j], det([row[:j]+row[j+1:] for row in m[1:]])), (-1)**j)
                 for j in range(len(m))))

def encode(e):
    assert len(e)==6 and all(type(k)==int and k>=0 for k in e) and sum(e)==16
    return sum(k*u for k,u in zip(e,U))

def decode(e):
    return [(e >> (5*i)) & 31 for i in range(6)]

def cumulative(p):
    # Descending shears implement y_k -> z_0+...+z_k.
    for hi in range(5,0,-1):
        r = {}
        for e,c in p.items():
            power = (e >> (5*hi)) & 31
            for k in range(power+1):
                f = e + k*(U[hi-1]-U[hi])
                r[f] = r.get(f,0) + c*math.comb(power,k)
        p = {e:c for e,c in r.items() if c}
    return p

def connected(ks):
    seen={0}
    while True:
        old=set(seen)
        for k in ks:
            a,b=EDGES[k]
            if a in seen or b in seen:
                seen.update((a,b))
        if old==seen:
            return len(seen)==4

def main():
    x = [{u:1} for u in U]
    q = [add(*(x[k] for k,e in enumerate(EDGES) if i in e)) for i in range(4)]
    L = [[q[i] if i==j else scale(x[EDGES.index(tuple(sorted((i,j))))],-1)
          for j in range(4)] for i in range(4)]
    triples=[]
    pairs=[]
    for size in (2,3):
        for S in it.combinations(range(4),size):
            m=[[L[i][j] for j in S] for i in S]
            v=[q[i] for i in S]
            numerator=scale(det([row+[v[k]] for k,row in enumerate(m)]+[v+[{}]]),-1)
            (triples if size==3 else pairs).append((det(m),numerator))
    tau=triples[0][0]
    assert all(d==tau for d,n in triples)
    trees=[ks for ks in it.combinations(range(6),3) if connected(ks)]
    assert len(trees)==16
    assert tau==add(*(prod(x[k] for k in ks) for ks in trees))
    R=prod(d for d,n in pairs)
    F=add(scale(mul(add(*(n for d,n in triples)),R),2),
          scale(prod([add(*q),tau,R]),-9),
          *(scale(prod([tau,n]+[d2 for j,(d2,n2) in enumerate(pairs) if j!=i]),-2)
            for i,(d,n) in enumerate(pairs)))
    assert all(sum(decode(e))==16 for e in F)
    stored=json.loads(Path('evidence/four_polynomial.json').read_text())['terms']
    assert len(stored)==len(F)
    assert F=={encode(e):c for e,c in stored}
    actions=[]
    for v in it.permutations(range(4)):
        a=tuple(EDGES.index(tuple(sorted((v[i],v[j])))) for i,j in EDGES)
        actions.append(a)
        assert {sum(decode(e)[i]*U[a[i]] for i in range(6)):c for e,c in F.items()}==F
    manifest=json.loads(Path('evidence/cone_manifest.json').read_text())
    assert hashlib.sha256(Path('evidence/four_polynomial.json').read_bytes()).hexdigest()==manifest['polynomial_sha256']
    records={tuple(r['order']):r for r in manifest['cones']}
    assert len(records)==len(manifest['cones'])==30
    covered=set()
    results=[]
    for o in it.permutations(range(6)):
        if o in covered:
            continue
        orbit={tuple(a[i] for i in o) for a in actions}
        assert len(orbit)==24 and not (orbit & covered)
        covered.update(orbit)
        assert o in records
        rec=records[o]
        ordered={sum(decode(e)[o[i]]*U[i] for i in range(6)):c for e,c in F.items()}
        G=cumulative(ordered)
        assert min(G.values())>0
        raw=gzip.decompress((Path('evidence/cones')/rec['file']).read_bytes())
        assert hashlib.sha256(raw).hexdigest()==rec['sha256_uncompressed']
        rows=json.loads(raw)
        assert all(type(c)==int and c>0 for e,c in rows)
        C={encode(e):c for e,c in rows}
        assert len(C)==len(rows)==rec['terms'] and C==G
        assert G.get(16*U[0],0)==0
        interior=[G.get(14*U[0]+2*U[j],0) for j in range(1,6)]
        assert min(interior)>0
        boundary={j:G.get(16*U[j],0) for j in range(1,6) if connected(o[j:])}
        assert all(c>0 for c in boundary.values())
        results.append(dict(file=rec['file'],order=o,terms=len(G),minimum=min(G.values()),
                            interior=interior,boundary=boundary))
        print('PASS',rec['file'],'terms',len(G),'connected boundary ranks',list(boundary),flush=True)
    assert len(covered)==720 and len(results)==30
    out=dict(passed=True,polynomial_terms=len(F),negative_terms=sum(c<0 for c in F.values()),
             degree=16,cones=results,coefficient_count=sum(r['terms'] for r in results),
             orderings=len(covered),boundary_tests=sum(len(r['boundary']) for r in results),
             seconds=time.monotonic()-START,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    Path('referee_cones_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cones'},indent=2))

if __name__=='__main__':
    main()
