"""Exact reversible-chain calculations for a proposed 3/2 lower bound."""
import json, time
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parent
start = time.perf_counter()
s = sp.symbols('s', positive=True)

def build(weights):
    n = weights.rows
    masses = [sum(weights[i,j] for j in range(n)) for i in range(n)]
    total = sum(masses)
    pi = sp.Matrix([[sp.factor(w/total) for w in masses]])
    Q = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            if i!=j:
                Q[i,j] = weights[i,j]/masses[i]
        Q[i,i] = -sum(Q[i,j] for j in range(n) if i!=j)
    H = sp.zeros(n)
    for target in range(n):
        keep = [i for i in range(n) if i!=target]
        h = (-Q.extract(keep,keep)).inv() * sp.ones(n-1,1)
        for i,val in zip(keep,h):
            H[i,target] = sp.factor(val)
    D = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            D[i,j] = sp.factor(H[i,j] - sum(pi[0,k]*H[k,j] for k in range(n)))
    return Q, pi, H, D

W = sp.Matrix([[0,0,1,0],[0,2*s,1,2*s],[1,1,0,s],[0,2*s,s,4*s*s]])
Q, pi, H, D = build(W)
blocks = [[0],[1],[2,3]]
What = sp.Matrix([[sum(W[i,j] for i in a for j in b) for b in blocks] for a in blocks])
Qhat, pihat, Hhat, Dhat = build(What)
limit_fine = [[str(sp.limit(D[i,j],s,sp.oo)) for j in range(4)] for i in range(4)]
limit_coarse = [[str(sp.limit(Dhat[i,j],s,sp.oo)) for j in range(3)] for i in range(3)]
print('fine entrywise limits:', limit_fine)
print('coarse entrywise limits:', limit_coarse)
table=[]
for value in [1,2,5,10,20,50,100,1000]:
    fine = max(D[i,j].subs(s,value) for i in range(4) for j in range(4))
    coarse = max(Dhat[i,j].subs(s,value) for i in range(3) for j in range(3))
    row={'s':value,'fine':str(fine),'coarse':str(coarse),'ratio':str(sp.factor(coarse/fine)),'ratio_float':float(coarse/fine)}
    table.append(row)
    print(row)
residuals = []
for A, stationary, hits in [(Q,pi,H),(Qhat,pihat,Hhat)]:
    residuals += [sp.simplify(v)==0 for v in stationary*A]
    residuals += [sp.simplify(stationary[0,i]*A[i,j]-stationary[0,j]*A[j,i])==0 for i in range(A.rows) for j in range(A.rows)]
    residuals += [sp.simplify(sum(A[i,k]*hits[k,j] for k in range(A.rows))+1)==0 for i in range(A.rows) for j in range(A.rows) if i!=j]
assert all(residuals)
out={'weights':[[str(v) for v in W.row(i)] for i in range(4)],'fine_D':[[str(D[i,j]) for j in range(4)] for i in range(4)],'coarse_D':[[str(Dhat[i,j]) for j in range(3)] for i in range(3)],'fine_limits':limit_fine,'coarse_limits':limit_coarse,'table':table,'exact_residual_checks':len(residuals),'all_passed':all(residuals),'elapsed_seconds':time.perf_counter()-start}
(root/'evidence/P0242_family.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('exact residual checks:',len(residuals),'elapsed:',out['elapsed_seconds'])
