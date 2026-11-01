from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, math, sys, time

HERE=Path(__file__).resolve().parents[1]
START=time.monotonic()
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    assert x
    if COUNT%1000==0 and time.monotonic()-START>55: raise TimeoutError('frozen 55s guard')

def walsh(v):
    n=len(v)
    return [F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(v)),n) for s in range(n)]
def delete(m,i):
    return (m&((1<<i)-1))|((m>>(i+1))<<i)
def restrict(v,i,y):
    return [a for x,a in enumerate(v) if (x>>i)&1==y]
def law(v): return [a*a for a in walsh(v)]
def reference(p,j):
    if j==0: return p[:]
    q=[x*F(5,6) for x in p];q[0]=p[0];q[j]+=(1-p[0])/6
    return q
@lru_cache(None)
def factors(n):
    ans=[];d=2
    while d*d<=n:
        k=0
        while n%d==0: n//=d;k+=1
        if k:ans.append((d,k))
        d+=1
    if n>1:ans.append((n,1))
    return tuple(ans)
def add(*terms):
    out={}
    for weight,word in terms:
        for k,v in word.items():out[k]=out.get(k,F(0))+weight*v
    return {k:v for k,v in out.items() if v}
def logword(x):
    out={}
    for n,s in [(x.numerator,1),(x.denominator,-1)]:
        for p,k in factors(n):out[p]=out.get(p,0)+s*k
    return {k:F(v) for k,v in out.items() if v}
def kl(p,q):
    return add(*[(x,logword(x/y)) for x,y in zip(p,q) if x])
PREC=90; SCALE=1<<PREC
def down(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-x)
@lru_cache(None)
def ln_bounds(x):
    z=(x-1)/(x+1);s=F(0);term=z
    for k in range(32):s+=term/F(2*k+1);term*=z*z
    err=2*abs(term)/(65*(1-z*z))
    return down(2*s),up(2*s+err)
@lru_cache(None)
def log_bounds(p):
    e=p.bit_length()-1;x=F(p,1<<e)
    lo,hi=ln_bounds(x);l2,h2=ln_bounds(F(2))
    return down(F(e)+lo/h2),up(F(e)+hi/l2)
def bounds(word):
    lo=hi=F(0)
    for p,c in word.items():
        a,b=log_bounds(p)
        if c<0:a,b=b,a
        lo+=c*a;hi+=c*b
    return lo,hi
ELL=logword(F(6,5))

def main():
    pilot='--pilot' in sys.argv;nmax=2 if pilot else 3
    rows=inside=absorbed=ghost=iso=0
    max_reset=None
    for n in range(1,nmax+1):
      for code in range(1<<(1<<n)):
        v=[1 if code>>x&1 else -1 for x in range(1<<n)]
        a=walsh(v);p=[t*t for t in a]
        for j in range(1,1<<n):
          q=reference(p,j);K=kl(p,q);aroot=1-p[j]
          ck(sum(q)==1);ck(q[0]==p[0]);ck(bounds(add((1,K),(-aroot,ELL)))[1]<=0 or not add((1,K),(-aroot,ELL)))
          for i in range(n):
            rows+=1;jc=delete(j,i);inside+=bool(j>>i&1);absorbed+=jc==0
            pc=[law(restrict(v,i,y)) for y in range(2)]
            qc=[reference(t,jc) for t in pc]
            pb=[F(0)]*(1<<(n-1));qb=pb[:]
            for s in range(1<<n):pb[delete(s,i)]+=p[s];qb[delete(s,i)]+=q[s]
            kernel=[[pc[y][t]/(2*pb[t]) if pb[t] else F(1,2) for t in range(len(pb))] for y in range(2)]
            ghost+=sum(pb[t]==0 and qb[t]>0 for t in range(len(pb)))
            r=[sum(qb[t]*kernel[y][t] for t in range(len(pb))) for y in range(2)]
            inherited=[[qb[t]*kernel[y][t]/r[y] for t in range(len(pb))] for y in range(2)]
            ck(all(t>=F(5,12) for t in r));ck(sum(r)==1)
            for y in range(2):ck(sum(pc[y])==sum(inherited[y])==sum(qc[y])==1)
            er=add((1,K),(-1,kl(pb,qb)));out=kl([F(1,2)]*2,r)
            ki=add(*[(F(1,2),kl(pc[y],inherited[y])) for y in range(2)])
            fresh=add(*[(F(1,2),kl(pc[y],qc[y])) for y in range(2)])
            sigma=add((1,fresh),(-1,ki))
            ck(not add((1,K),(-1,er),(-1,out),(-1,ki)))
            ck(not add((1,K),(1,sigma),(-1,er),(-1,out),(-1,fresh)))
            expected_a=sum(1-t[jc] for t in pc)/2
            ck(expected_a==aroot-p[j^(1<<i)])
            bank=F(n-1)*aroot
            cb=sum(F(n-2)*(1-t[jc]) if jc else F(0) for t in pc)/2
            if jc:ck(bank-cb==aroot+(n-2)*p[j^(1<<i)]);ck(bank-cb>=expected_a)
            else:ck(not fresh);ck(bank>=0)
            bill=add((1,sigma),(-(bank-cb),ELL))
            ck(not bill or bounds(bill)[1]<=0)
            if jc==0:ck(not sigma or bounds(sigma)[1]<=0)
            iso+=pc[0]==pc[1]
    result={'status':'PASS','rows':rows,'assertions':COUNT,'inside_anchor_queries':inside,'empty_anchor_queries':absorbed,'reference_only_erased_rows':ghost,'isospectral_queries':iso,'elapsed_seconds':time.monotonic()-START,'arithmetic':'Fraction and exact prime-log identities; outward rational log intervals'}
    name='PILOT.json' if pilot else 'CHECK.json'
    (HERE/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
