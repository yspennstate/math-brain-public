from pathlib import Path
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
ASSERT=0
def check(p):
    global ASSERT
    ASSERT+=1
    assert p
def fwht(t):
    a=t[:];h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return a
def coefficients(m,t):
    r=m-1;h=t-1;D=1<<m
    K=[1]
    if r:K.append(r-2*h)
    for k in range(1,r):
        num=(r-2*h)*K[-1]-(r-k+1)*K[-2]
        check(num%(k+1)==0);K.append(num//(k+1))
    V=[];mult=[]
    for k in range(r+1):
        c=comb(r,k);num=2*comb(r,h)*K[k]
        check(num%c==0);V.append(num//c);mult.append(c)
    U=[D-2*sum(comb(m,j) for j in range(t,m+1))]+V[:-1]
    return U,V,mult
@lru_cache(None)
def profile(m,t):
    U,V,c=coefficients(m,t);D=1<<m
    a=2*comb(m-1,t-1)
    check(sum(c[k]*V[k]*V[k] for k in range(m))==a*D)
    check(sum(c[k]*(U[k]*U[k]+V[k]*V[k]) for k in range(m))==D*D)
    check(sum(c[k]*U[k]*V[k] for k in range(m))==0)
    overlap=sum(c[k]*abs(U[k]*V[k]) for k in range(m))
    minority=sum(c[k]*min(U[k]*U[k],V[k]*V[k]) for k in range(m))
    return overlap,a,minority
def direct(m,t):
    tab=[1-2*(x.bit_count()>=t) for x in range(1<<m)]
    a=fwht(tab);U,V,_=coefficients(m,t)
    for s in range(1<<m):
        k=(s>>1).bit_count();check(a[s]==(V[k] if s&1 else U[k]))
    edge=sum(tab[x]!=tab[x^1] for x in range(1<<m))
    check(edge==2*comb(m-1,t-1))
def tree(n):
    D=1<<n;N=0;MS=0;paid=0;t0=(n+1)//2
    for m in range(1,n+1):
        d=n-m
        for j in range(d+1):
            t=t0-j
            if not 1<=t<=m:continue
            ov,a,mi=profile(m,t);history=comb(d,j)
            N+=history*ov*(1<<(n-m))
            MS+=history*mi*(1<<(n-m))
            paid+=history*a
    I=F(n*2*comb(n-1,(n-1)//2),D)
    check(F(paid,D)==I)
    L=F(3*N,2*D*D)
    return {'n':n,'I':str(I),'L':str(L),'L_over_I':str(L/I),'minority_tree_over_I':str(F(MS,D*D)/I)}
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv
    maximum=6 if pilot else 129
    mx=F(0);witness=None;viol=[];by_m=[]
    for m in range(1,maximum+1):
        local=F(0)
        for t in range(1,m+1):
            ov,a,mi=profile(m,t);ratio=F(ov,a*(1<<m))
            if ratio>mx:mx=ratio;witness=[m,t]
            local=max(local,ratio)
            if ratio>2:viol.append([m,t,str(ratio)])
            if m<=6:direct(m,t)
        by_m.append({'m':m,'max_overlap_over_influence':str(local)})
    ns=[3,5,9,17] if pilot else [3,5,9,17,33,65,129]
    rows=[tree(n) for n in ns]
    out={'status':'PASS','helper':'A078-paired-overlap-v1','mode':'pilot' if pilot else 'full','assertions':ASSERT,'threshold_cases':maximum*(maximum+1)//2,'maximum_overlap_over_influence':str(mx),'maximum_witness':witness,'violations_of_overlap_le_2I':viol,'tree_rows':rows,'by_dimension':by_m,'seconds':time.perf_counter()-start,'arithmetic':'integer Walsh, integer Krawtchouk, rational profiles and physical influence budgets'}
    (ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['by_dimension','violations_of_overlap_le_2I']},indent=2))
if __name__=='__main__':main()
