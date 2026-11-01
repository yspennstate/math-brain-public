from pathlib import Path
from fractions import Fraction as F
from math import comb
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
start=time.perf_counter()
assert (OUT/'FROZEN_SPEC.json').exists()
checks=0
def ck(b):
    global checks
    assert b
    checks+=1

# ln(2)=2 atanh(1/3); all arithmetic is rational.
z=F(1,3); N=64
lnlo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
lnhi=lnlo+2*z**(2*N+1)/((2*N+1)*(1-z*z))
def interval(A,B):
    return (A+B*lnlo,A+B*lnhi) if B>=0 else (A+B*lnhi,A+B*lnlo)
def phi_poly(t,m):
    return t*(1-t)*sum((2*(1-t)**j/F(j*(j+1)) for j in range(1,m+1)),F(0))
def err(r,m):
    A=B=F(0)
    for k in range(1,r+1):
        t=F(2)**(k-1-r); a=F(4)**(1-k); w=comb(2*r,k)*a
        A+=w*(2*t*(1-t)-phi_poly(t,m))
        B-=w*2*t*t*(r+1-k)
    return A,B

physical=[]
for r in (1,2,3):
    n=2*r; size=1<<n
    vals=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(r)) for x in range(size)]
    walsh=[sum(vals[x]*(-1)**((x&s).bit_count()) for x in range(size)) for s in range(size)]
    ck(all(abs(w)==1<<r for w in walsh))
    ck(sum(w*w for w in walsh)==size*size)
    influence=F(sum(s.bit_count()*walsh[s]**2 for s in range(size)),size*size)
    ck(influence==r)
    ck(F(size-1,size)==1-F(1,4**r))
    profs=0
    for s in range(1,size):
        k=s.bit_count(); complement=(size-1)^s
        moments=[]
        for y in range(size):
            if y&s: continue
            total=0
            b=s
            while True:
                total+=(-1)**(k-b.bit_count())*vals[y|b]
                if b==0: break
                b=(b-1)&s
            ck(total%2==0)
            moments.append(F(total,2))
        mean=sum(moments,F(0))/len(moments)
        d=sum((x*x for x in moments),F(0))/len(moments)
        ck(mean==(-1)**k*F(2)**(k-1)*F(walsh[s],size))
        ck(abs(mean)==F(2)**(k-1-r))
        ck(d==F(2)**(k-2))
        W=F(sum(walsh[t]**2 for t in range(size) if t!=s and t&s==s),size*size)
        ck(d-mean*mean==F(4)**(k-1)*W)
        profs+=1
    physical.append({'r':r,'n':n,'profiles':profs,'H_bits':2*r,'I':r})

rows=[]
rs=list(range(1,13))+[16,24,32,48,64,96,128,256]
ms=[0,1,2,4,8,16]
for r in rs:
    delta=F(r-1)+F(1,4**r)
    ck(0<delta<=r)
    weighted=sum((F(comb(2*r,k),2**k) for k in range(1,r+1)),F(0))
    ck(weighted>=F(1,2)*F(9,4)**r-1)
    prev=None
    for m in ms:
        A,B=err(r,m); lo,hi=interval(A,B)
        lower=F(2)**(-m-1)/((m+1)*(m+2))*F(9,8)**r-F(2)**(-m-r)/((m+1)*(m+2))
        ck(lo>0)
        ck(lo>=lower)
        if prev is not None: ck(hi<prev)
        prev=lo
        growing=None
        if r%4==0 and m+1<=F(2)**(r//4-1):
            # Exponents integral because r is a multiple of four.
            L=3*r//4
            partial=sum((F(comb(2*r,k),2**k) for k in range(1,L+1)),F(0))
            ck(partial>=F(1,9)*F(9,4)**r-1)
            growing=(F(9,8)**r/F(18)-F(2)**(-r-1))/(m+1)
            ck(lo>=growing)
            growing=str(growing)
        rows.append({'r':r,'m':m,'D_over_Delta_lower':str(lo/delta),'D_over_Delta_upper':str(hi/delta),'fixed_order_bound':str(lower),'growing_order_bound':growing})

# Boundary checks: empty finite sum, t=0 and t=1, no erroneous quotient.
for m in ms:
    ck(phi_poly(F(0),m)==0)
    ck(phi_poly(F(1),m)==0)
    ck(sum((F(2,j*(j+1)) for j in range(m+1,2*m+2)),F(0))==F(1,m+1))
    for t in (F(1,2),F(1,4),F(1,16)):
        ck(phi_poly(t,m+1)>=phi_poly(t,m))

result={'status':'PASS','exact_assertions':checks,'physical':physical,'formula_cases':len(rows),'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction plus rigorous rational ln2 interval, 64 atanh terms','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
(OUT/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
