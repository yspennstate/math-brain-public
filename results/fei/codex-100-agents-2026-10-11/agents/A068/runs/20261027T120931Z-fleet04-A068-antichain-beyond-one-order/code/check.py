from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,time,sys
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0; cases=0; sourcecases=0
def ck(x):
    global checks
    checks+=1
    if not x: raise AssertionError(checks)
    if checks%1024==0 and time.perf_counter()-start>55: raise RuntimeError('frozen 55s cap')
def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),h*2):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return a
def edges(a):
    n=len(a).bit_length()-1;counts=[]
    for i in range(n):
        b=1<<i;counts.append(sum(a[x]!=a[x|b] for x in range(len(a)) if not x&b))
    return counts
def core(mask,d):return [1 if mask>>j&1 else -1 for j in range(1<<d)]
def fixtures(d,m):
    n=d+m
    if d==0:
        yield from ((i,) for i in range(64)); yield from combinations(range(64),2)
    elif d==1:
        yield from ((i,) for i in range(128)); yield from ((0,i) for i in range(1,128))
    elif d==2:
        pat=[0,1,4,33]
        for j in range(16):yield tuple((j*61)^v for v in pat[:j%4+1])
    else:
        pat=[0,1,2,3,8,16,(1<<8)|1,(1<<(n-1))|7]
        for k in (1,2,3,4,8):yield tuple(pat[:k])
pilot='--pilot' in sys.argv
groups=[(0,6,[0,1]),(1,6,list(range(4))),(2,8,list(range(16))),(3,12,[0,255,1,254,128,127,150,232])]
observed={}
for d,m,masks in groups:
    if pilot and d>0:break
    n=d+m;size=1<<n;cn=1<<d;before=cases
    for mask in masks:
        g=core(mask,d);gh=fwht(g);ig=F(sum(edges(g)),1<<(d-1)) if d else F(0)
        pg=[F(v*v,cn*cn) for v in gh]
        source_cache=[]
        for q in (pg,[(p+F(1,cn))/2 for p in pg]):
            if ig==0:q=pg
            ck(sum(q)==1);ck(all(qi>0 for pi,qi in zip(pg,q) if pi));source_cache.append(q)
        for E in fixtures(d,m):
            if pilot and cases>=24:break
            k=len(E);theta=F(k,size);eta=4*theta
            ck(len(set(E))==k and all(0<=x<size for x in E));ck(k**4<=1<<m and m>=4*d and m>=6)
            a=[g[x&(cn-1)] for x in range(size)]
            for x in E:a[x]*=-1
            fh=fwht(a);ec=edges(a);If=F(sum(ec),size//2)
            ck(If==F(sum(s.bit_count()*v*v for s,v in enumerate(fh)),size*size))
            ck(If-ig>=m*theta)
            ck(sum(ec[d:])*4>=3*m*k)
            noise=0; ptotal=0
            for s,v in enumerate(fh):
                clean=(gh[s]*(1<<m)) if s<cn else 0
                e=v-clean
                ck(v*v<=2*clean*clean+2*e*e)
                noise+=e*e;ptotal+=v*v
            ck(noise==4*k*size);ck(ptotal==size*size)
            ck(0<eta<=F(1,2));ck(16*n+24<=24*m)
            ck((16*n+24)*theta<=24*(If-ig))
            for q in source_cache:
                floor=eta/size;inside=[(1-eta)*v+floor for v in q]
                ck(sum(inside)+(size-cn)*floor==1)
                ck(all(0<v<=1 and v>=(1-eta)*qi and v>=floor for v,qi in zip(inside,q)))
                cg_upper=d if q==pg else d+1
                if ig==0:cg_upper=0
                c=F(cg_upper,1)/ig if ig else F(0)
                C0=max(2*c,F(24));K=C0+4
                source_upper=2*cg_upper+24*(If-ig)
                ck(source_upper<=C0*If)
                # Full history theorem uses c_JS<81/28; retain eligible old U=I(F).
                ck(K*If-(If+source_upper+F(81,28)*If)>=F(3,28)*If)
                sourcecases+=1
            cases+=1
        if pilot and cases>=24:break
    observed[f'd{d}m{m}']=cases-before
    if pilot:break
# Negative control: unpadded one-point sign flips back to a constant.
g=[-1,1,1,1];f=[1,1,1,1]
ck(sum(edges(g))>sum(edges(f)));ck(sum(edges(f))==0)
out=dict(status='PASS',pilot=pilot,roots=cases,source_certificates=sourcecases,assertions=checks,seconds=time.perf_counter()-start,domains=observed,arithmetic='integer Walsh/physical edges and rational source-envelope certificates',negative_control='without padding, core influence can decrease to zero')
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
