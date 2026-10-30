"""Separate physical/Fourier reconstruction of A005 Sections1--3."""
from pathlib import Path
from fractions import Fraction as F
import time,json
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
    global checks
    checks+=1;assert x,checks
def direct(f):
    return [sum(z*(-1)**((x&s).bit_count()%2) for x,z in enumerate(f)) for s in range(len(f))]
def physical(f):
    n=len(f).bit_length()-1
    return [F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n)]
def restrict(f,i,b):
    n=len(f).bit_length()-1;out=[]
    for y in range(1<<(n-1)):
        x=(y&((1<<i)-1))|((y>>i)<<(i+1))|(b<<i);out.append(f[x])
    return out
roots=0;children=0;weak=0
for n in range(4):
    N=1<<n
    for t in range(1<<N):
        f=[1-2*((t>>x)&1) for x in range(N)];roots+=1
        a=direct(f);p=physical(f);isweak=all(q<=F(1,4) for q in p)
        weak+=isweak
        for i in range(n):
            other=[j for j in range(n) if j!=i]
            ps=[physical(restrict(f,i,b)) for b in [0,1]];children+=2
            tau=sum((max(F(0),2*q-1) for row in ps for q in row),F(0))/2
            formula=F(0)
            for h,j in enumerate(other):
                c=F(sum(a[s]*a[s|(1<<i)] for s in range(N) if not ((s>>i)&1) and ((s>>j)&1)),N*N)
                ck(ps[0][h]==p[j]+2*c)
                ck(ps[1][h]==p[j]-2*c)
                ck(2*abs(c)<=p[j])
                formula+=(max(F(0),2*p[j]+4*c-1)+max(F(0),2*p[j]-4*c-1))/2
                if p[j]<=F(1,2):
                    ck((max(F(0),2*p[j]+4*c-1)+max(F(0),2*p[j]-4*c-1))/2==max(F(0),p[j]+2*abs(c)-F(1,2)))
            ck(tau==formula)
            if isweak:ck(tau==0 and all(q<=F(1,2) for row in ps for q in row))
res={'status':'PASS','assertions':checks,'root_tables':roots,'physical_children':children,'weak_roots_pmax_le_quarter':weak,'arithmetic':'direct character sums and physical edges, Fraction','scope':'A005 DERIVATION Sections1--3 analytic scope; finite replay verifies conditional coefficients and release/zero-release identities; no activation or N11 certificate adopted','runtime_seconds':time.monotonic()-start}
(R/'out/REVIEW_A005_CHECK.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8');print(json.dumps(res,indent=2))
