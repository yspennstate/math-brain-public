"""Frozen exact audit v1: selector between dense/sparse quadratics.
Fixed data dimensions 4,6,8, one physical query each, both outcomes.
No symmetry; direct integer Walsh, Fraction probabilities; <50MB, <60sec.
Pilot is n=4 first, measured separately; do not enlarge the domain.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

checks = 0
def ck(b,tag):
    global checks
    checks += 1
    if not b:
        raise AssertionError(tag)

def law(tab):
    a = list(tab)
    h = 1
    while h < len(a):
        for start in range(0,len(a),2*h):
            for j in range(start,start+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return [F(x*x,len(a)**2) for x in a]

def case(n):
    r,N = n//2,1 << n
    dense,sparse = [],[]
    for x in range(N):
        u,v = x & ((1 << r)-1),x >> r
        dense.append((-1)**((u & v).bit_count() & 1))
        sparse.append((-1)**((u.bit_count()*v.bit_count()) & 1))
    pd,ps = law(dense),law(sparse)
    L = {0,(1 << r)-1,((1 << r)-1) << r,N-1}
    ck(all(a == F(1,N) for a in pd),'dense actual uniform law')
    ck(all(ps[t] == F(int(t in L),4) for t in range(N)),'sparse actual four-atom law')
    root = [val for pair in zip(dense,sparse) for val in pair]
    p = law(root)
    d = [sum(p[t] for t in range(2*N) if t >> i & 1) for i in range(n+1)]
    ck(all(a == F(1,2) for a in d[1:]),'original actual data product fair')
    product = []
    for t in range(2*N):
        a = F(1)
        for i,di in enumerate(d):
            a *= di if t >> i & 1 else 1-di
        product.append(a)
    Qbar = [product[2*t]+product[2*t+1] for t in range(N)]
    qbar = [p[2*t]+p[2*t+1] for t in range(N)]
    ck(all(a == F(1,N) for a in Qbar),'actual original product erasure')
    ck(all(qbar[t] == (pd[t]+ps[t])/2 > 0 for t in range(N)),'true source erasure, no zero rows')
    out = []
    for child in (pd,ps):
        unnormalized = [Qbar[t]*child[t]/(2*qbar[t]) for t in range(N)]
        mass = sum(unnormalized)
        out.append((mass,[a/mass for a in unnormalized]))
    ck(out[0][0] == F(N,N+4) and out[1][0] == F(4,N+4),'actual outcome masses')
    ck(all(out[0][1][t] == F(4 if t in L else N+4,N*N) for t in range(N)),'nonuniform dense predicted reference')
    ck(out[1][1] == ps,'sparse inherited reference equals source law')
    ck(len(set(out[0][1])) == 2,'literal affine-superspace cone fails at dense full support')
    return {'n':n,'N':N,'dense_reference_on_L':str(out[0][1][0]),
            'dense_reference_outside_L':str(next(out[0][1][t] for t in range(N) if t not in L)),
            'pi_dense':str(out[0][0]),'pi_sparse':str(out[1][0]),'sparse_product_admission_gap':n-2}

started = time.monotonic()
rows = [case(4)]
pilot_seconds = time.monotonic()-started
ck(pilot_seconds < 60,'pilot budget')
rows.extend(case(n) for n in (6,8))
result = {'status':'PASS','assertions':checks,'cases':rows,'pilot_seconds':round(pilot_seconds,3),
          'elapsed_seconds':round(time.monotonic()-started,3),'arithmetic':'integer Walsh and Fraction only',
          'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).resolve().parent.parent.joinpath('out','cone_boundary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
