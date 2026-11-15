"""Independent verifier: Fraction Gaussian determinants of principal kernel minors.

Does not import the producer, SciPy, NumPy, or SymPy. No floating-point arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict,Counter
from pathlib import Path
import json,time,resource,os,hashlib
ROOT=Path(__file__).resolve().parents[1]

def determinant(M):
    A=[row[:] for row in M];n=len(A);answer=F(1)
    for k in range(n):
        j=next((j for j in range(k,n) if A[j][k]),None)
        if j is None:return F(0)
        if j!=k:A[j],A[k]=A[k],A[j];answer=-answer
        v=A[k][k];answer*=v
        for i in range(k+1,n):
            if A[i][k]:
                ratio=A[i][k]/v
                for j in range(k+1,n):A[i][j]-=ratio*A[k][j]
                A[i][k]=F(0)
    return answer

def kernel_law(Q,cols):
    n=len(Q);r=len(cols)
    K=[[sum((Q[i][k]*Q[j][k] for k in cols),F(0)) for j in range(n)] for i in range(n)]
    law={B:determinant([[K[i][j] for j in B] for i in B]) for B in combinations(range(n),r)}
    assert all(v>=0 for v in law.values()) and sum(law.values())==1
    return law

def check(path,cache):
    d=json.loads(path.read_text());n=d['n'];Q=[[F(x) for x in row] for row in d['Q']]
    assert len(Q)==n and all(len(row)==n for row in Q)
    key=tuple(tuple(row) for row in Q)
    if key not in cache:
        assert all(sum((Q[i][j]*Q[i][k] for i in range(n)),F(0))==int(j==k) for j in range(n) for k in range(n))
        cache[key]={}
    cols1=tuple(d['columns1']);cols2=tuple(d['columns2']);cols=tuple(sorted(cols1+cols2))
    assert len(set(cols))==len(cols) and all(0<=c<n for c in cols)
    targets=[]
    for columns in [cols1,cols2,cols]:
        if columns not in cache[key]:cache[key][columns]=kernel_law(Q,columns)
        targets.append(cache[key][columns])
    actual=[defaultdict(F) for _ in range(3)]
    for entry in d['coupling']:
        A=tuple(entry['A']);B=tuple(entry['B']);v=F(entry['mass']);C=tuple(sorted(A+B))
        assert tuple(sorted(set(A)))==A and tuple(sorted(set(B)))==B and len(set(C))==len(C)
        assert len(A)==len(cols1) and len(B)==len(cols2) and all(0<=i<n for i in C)
        assert v>=0
        for marginal,state in zip(actual,[A,B,C]):marginal[state]+=v
    checks=0
    for marginal,target in zip(actual,targets):
        assert all(marginal.get(B,0)==target.get(B,0) for B in marginal.keys()|target.keys())
        assert sum(marginal.values())==1;checks+=len(target)
    return n,len(cols1),len(cols2),checks

def run():
    start=time.monotonic();cache={};counts=Counter();checks=0;digests={}
    files=sorted((ROOT/'data/certificates').glob('*.json'))
    for path in files:
        n,p,q,num=check(path,cache);counts[n]+=1;checks+=num
        digests[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
    record={'verified_certificates':len(files),'by_n':dict(counts),'distinct_orthogonal_matrices':len(cache),
            'exact_marginal_equalities':checks,'method':'Fraction Gaussian elimination on principal projection-kernel minors; all entries nonnegative and all three marginals exact',
            'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'nice':os.getpriority(os.PRIO_PROCESS,0),'certificate_sha256':digests}
    assert record['peak_rss_bytes']<3*1024**3
    (ROOT/'data/verification.json').write_text(json.dumps(record,indent=2)+'\n')
    print({k:v for k,v in record.items() if k!='certificate_sha256'},flush=True)
if __name__=='__main__':run()
