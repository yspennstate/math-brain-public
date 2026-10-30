from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,math,time,sys
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv;t0=time.perf_counter();checks=0
def ck(b):
    global checks
    checks+=1;assert b
def walsh(v):
    a=v[:];h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
        h*=2
    return a
hist=Counter();paircases=admitted=singlecases=0;witnesses={};geometries=Counter()
for r in range(3 if pilot else 4):
    N=1<<r;mons=[0]+[1<<j for j in range(r)]+[(1<<i)|(1<<j) for i in range(r) for j in range(i+1,r)]
    phases=[]
    for mask in range(1<<len(mons)):
        p=[1-2*(sum(1 for j,s in enumerate(mons) if mask>>j&1 and x&s==s)%2) for x in range(N)]
        A=walsh(p);C=max(abs(x) for x in A);ck(all(x in (0,C,-C) for x in A))
        support={j for j,v in enumerate(A) if v};sign=[(x>0)-(x<0) for x in A]
        ck(len(support)&(len(support)-1)==0);ck((len(support).bit_length()-1)%2==0)
        phases.append((A,C,support,sign,mask))
        for U in (1,2):
            norm=F(U*U*len(support),4*N);ck(norm==1 or norm<=F(5,8));singlecases+=1
    for A,C0,S0,e0,m0 in phases:
        for B,C1,S1,e1,m1 in phases:
            inter=S0&S1
            geom='same' if S0==S1 else ('disjoint' if not inter else 'overlap')
            for a in (1,2,3,4):
                for b in (1,2,3,4):
                    paircases+=1
                    h2=[a*u+v*b*w for u,w in zip(e0,e1) for v in (1,-1)]
                    if any(z%2 or abs(z)>4 for z in h2):continue
                    h=[z//2 for z in h2];admitted+=1;geometries[geom]+=1
                    if geom=='same':ck(a+b<=4 and (a+b)%2==0 and (a-b)%2==0)
                    elif geom=='overlap':ck(a==b==2)
                    else:ck(a in (2,4) and b in (2,4))
                    w=F(sum(x*x for x in h),8*N)
                    nonfair=a*C1!=b*C0
                    ck(w==1 or w<=F(5,8));ck(not nonfair or w<=F(5,8))
                    if w==1:ck(not nonfair)
                    ratio0=a*C1;ratio1=b*C0;g=math.gcd(ratio0,ratio1);ratio=(ratio0//g,ratio1//g)
                    hist[(str(w),nonfair)]+=1
                    # Actual Boolean realization of row h_0=2 E_address F, pointwise.
                    for z in h:
                        signs={2:[1]*4,1:[-1,1,1,1],0:[-1,-1,1,1],-1:[1,-1,-1,-1],-2:[-1]*4}[z]
                        ck(sum(signs)==2*z)
                    key=(geom,ratio,str(w))
                    if key not in witnesses:witnesses[key]={'r':r,'phase0':m0,'phase1':m1,'twice_height0':a,'twice_height1':b,'norm_w':str(w),'coefficient_ratio':list(ratio),'geometry':geom,'physical_row':h}
                    # Independent Fourier check on one witness for each geometry/ratio/norm.
                    if witnesses[key]['physical_row'] is h:
                        W=walsh(h);amp0=F(a,2*C0);amp1=F(b,2*C1)
                        ck(all(F(abs(W[t]),2*N)==(amp1 if t&1 else amp0) for t in range(2*N)))
out={'result':'PASS','pilot':pilot,'pair_candidates':paircases,'single_candidates':singlecases,'admitted_pairs':admitted,'assertions':checks,'runtime_seconds':time.perf_counter()-t0,'geometries':dict(geometries),'norm_profiles':[{'w':w,'nonfair':nf,'count':c} for (w,nf),c in sorted(hist.items())],'witnesses':list(witnesses.values())}
(R/'out').mkdir(exist_ok=True)
(R/('out/pilot.json' if pilot else 'out/validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('norm_profiles','witnesses')},indent=2))
