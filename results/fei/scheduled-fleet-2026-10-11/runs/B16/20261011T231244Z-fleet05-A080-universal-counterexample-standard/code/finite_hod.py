from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
D=2**80; K=28; started=time.perf_counter(); checks=0
def rd(a): return F((a*D).__floor__(),D)
def ru(a): return F((a*D).__ceil__(),D)
def iv(x): return F(x),F(x)
def add(a,b): return rd(a[0]+b[0]),ru(a[1]+b[1])
def neg(a): return -a[1],-a[0]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    v=[x*y for x in a for y in b]
    return rd(min(v)),ru(max(v))
def div(a,b):
    assert b[0]>0
    return mul(a,(rd(1/b[1]),ru(1/b[0])))
def lnr(y):
    # Keep rigorous series endpoints dyadic instead of multiplying huge exact denominators.
    DD=2**112
    def down(x): return F((x*DD).__floor__(),DD)
    def up(x): return F((x*DD).__ceil__(),DD)
    z=(y-1)/(y+1); zl,zu=down(z),up(z)
    zzl,zzu=down(zl*zl),up(zu*zu)
    pl,pu=zl,zu; sl=su=F(0)
    for j in range(K):
        sl=down(sl+2*pl/(2*j+1)); su=up(su+2*pu/(2*j+1))
        pl=down(pl*zzl); pu=up(pu*zzu)
    tail=up(2*pu/((2*K+1)*(1-zzu)))
    return sl,up(su+tail)
ln2=lnr(F(2))
@lru_cache(maxsize=400)
def lg(x):
    assert x>0
    k=0; y=x
    while y<1: y*=2; k-=1
    while y>=2: y/=2; k+=1
    l,u=lnr(y)
    return rd(F(k)+l/ln2[1]),ru(F(k)+u/ln2[0])
def hs(x):
    assert 0<=x<=1
    if not x or x==1: return iv(0)
    return neg(add(mul(iv(x),lg(x)),mul(iv(1-x),lg(1-x))))
def hb(a):
    assert 0<=a[0]<=a[1]<=1
    left,right=hs(a[0]),hs(a[1])
    return min(left[0],right[0]),F(1) if a[0]<=F(1,2)<=a[1] else max(left[1],right[1])
def ht(a):
    vals=[4*x*(1-x) for x in a]
    v=(rd(min(vals)),F(1) if a[0]<=F(1,2)<=a[1] else ru(max(vals)))
    return hb(v)
def step(lam,child):
    global checks
    p,A,B=lam; q,C,E=child; pq=mul(p,q)
    probability=sub(iv(1),pq)
    influence=add(mul(q,A),mul(p,C))
    entropy=add(add(mul(q,sub(B,ht(p))),mul(p,sub(E,ht(q)))),add(ht(pq),mul(mul(iv(4),pq),sub(add(hb(p),hb(q)),hb(pq)))))
    checks+=1
    assert 0<probability[0]<=probability[1]<1 and influence[0]>0
    return probability,influence,entropy
cur=(iv(F(1,2)),iv(1),iv(0)); records=[]
for m in range(49):
    if m:
        lam=cur; child=lam
        for j in range(80):
            child=step(lam,child)
            if time.perf_counter()-started>180: raise RuntimeError('frozen runtime cap reached')
        cur=child
    p,I,H=cur; ratio=div(H,I)
    records.append({'m':m,'n':str(81**m),'p_interval':list(map(str,p)),'I_interval':list(map(str,I)),'H_interval':list(map(str,H)),'ratio_interval':list(map(str,ratio))})
    (ROOT/'out'/'FINITE_HOD_PARTIAL.json').write_text(json.dumps({'completed_m':m,'records':records},indent=2),encoding='utf-8')
assert ratio[0]>F(64547837,10000000)
assert ratio[1]<F(6454784,1000000)
out={'status':'PASS','recurrences':checks,'runtime_seconds':time.perf_counter()-started,'formula':'F0=identity; F_(m+1)=K_80(F_m), K0(lambda)=lambda, K_(j+1)(lambda)=dual(lambda AND K_j(lambda)), every operand on fresh disjoint copies','dimension':str(81**48),'final_ratio_interval':list(map(str,ratio)),'final_ratio_decimal_display':[float(x) for x in ratio],'records':records}
(ROOT/'out'/'FINITE_HOD_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
