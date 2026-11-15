"""Rational PSD coefficient certificates in six nonnegative gap variables."""
import json,itertools,time
from pathlib import Path
import sympy as s
from sympy.polys.domains import QQ
from algebra44 import variables,pair
from inherited17.memory_guard import install

def psd(A):
    # Exact symmetric elimination, including zero pivots.
    A=[list(row)for row in A];n=len(A)
    for i in range(n):
        p=A[i][i]
        if p<0:return False
        if p==0:
            if any(A[i][j]for j in range(i+1,n)):return False
        else:
            for j in range(i+1,n):
                for k in range(j,n):
                    A[j][k]-=A[i][j]*A[i][k]/p;A[k][j]=A[j][k]
    return True

def coefficients(M):
    n=len(M);exps=set().union(*(set(p)for row in M for p in row))
    for e in sorted(exps):yield e,[[p.get(e,QQ.zero)for p in row]for row in M]

def inspect(M):
    count=0;bad=[]
    for e,A in coefficients(M):
        count+=1
        if not psd(A):bad.append((e,A))
    return count,bad

def main():
    install(850_000_000);rr,*_=variables();records=[]
    jobs=[('star','rank',1,j)for j in (0,1)]+[('path','rank',1,j)for j in (0,1)]+[('rank','rank',i,j)for i,j in ((0,0),(0,1),(1,1))]
    for left,right,i,j in jobs:
        t=time.monotonic();M,den,Q1,Q2=pair(rr,left,right,i,j,margin=QQ(1,100))
        count,bad=inspect(M)
        rec=dict(left=left,right=right,endpoints=[i,j],count=count,failed=len(bad),Tstar_margin='1/100')
        print(rec,'seconds',time.monotonic()-t,flush=True)
        if bad:print('first failures',bad[:2],flush=True)
        records.append(rec)
    Path('boundary44_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    assert all(r['failed']==0 for r in records)
    print('PROVED (boundary44.py): mixed and boundary/boundary connected endpoints have Tstar>=1/100, k>=6 and infinity.')

if __name__=='__main__':main()
