"""Verify saved certificates with fresh exact evaluation on each torus site."""
import os
os.environ.update({k:'1' for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')})
from fractions import Fraction as Q
from itertools import product
from math import lcm
from pathlib import Path
import json
import resource
import time

assert os.getpriority(os.PRIO_PROCESS,0) >= 10
root = Path(__file__).resolve().parent
start = time.monotonic()
counts = {}
total_sites = 0
for name in ['certificates_2d.json','certificates_3d.json','explicit_ford_certificate.json']:
    raw = json.loads((root/'claim_files'/'data'/name).read_text())
    records = raw if isinstance(raw,list) else [raw]
    for record in records:
        c = record['certificate']
        A = [[Q(e) for e in row] for row in c['A']]
        b = [Q(e) for e in c['b']]
        N, u = c['N'],c['u']
        d = len(A)
        assert len(u) == N**d
        assert all(isinstance(v,int) for v in u)
        assert all(A[i][j] == A[j][i] for i in range(d) for j in range(d))
        assert all((N*A[i][j]).denominator == 1 for i in range(d) for j in range(d))
        assert all((N*N*A[i][i]/2+N*b[i]).denominator == 1 for i in range(d))
        den = lcm(*(v.denominator for row in A for v in row),*(v.denominator for v in b))*2
        M = [[int(den*v/2) for v in row] for row in A]
        B = [int(den*v) for v in b]
        def g(x):
            idx = 0
            for xi in x:
                idx = idx*N+xi%N
            numerator = sum(M[i][j]*x[i]*x[j] for i in range(d) for j in range(d))+sum(B[i]*x[i] for i in range(d))
            return -((-numerator)//den)+u[idx]
        sumlap = 0
        for x in product(range(N),repeat=d):
            lap = -2*d*g(x)
            for j in range(d):
                for step in [-1,1]:
                    y = list(x)
                    y[j] += step
                    lap += g(y)
            assert lap <= 1,(name,c['A'],x,lap)
            sumlap += lap
        assert Q(sumlap,N**d) == sum(A[i][i] for i in range(d))
        total_sites += N**d
    counts[name] = len(records)
result = {'valid':True,'counts':counts,'total':sum(counts.values()),'sites':total_sites,'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'nice':os.getpriority(os.PRIO_PROCESS,0)}
(root/'certificate_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
