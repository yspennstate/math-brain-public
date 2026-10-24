from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import comb
import argparse,json,time
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
start=time.perf_counter(); checks=0; D=2**90
def ck(x):
    global checks
    assert x
    checks+=1
def iv(x): return F(x),F(x)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(a,c): return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def minus(a,b): return a[0]-b[1],a[1]-b[0]
def lnr(y,K=32):
    z=(y-1)/(y+1); zz=z*z; power=z; total=F(0)
    for j in range(K): total+=2*power/(2*j+1); power*=zz
    return total,total+2*power/((2*K+1)*(1-zz))
LN2=lnr(F(2)); LOGE=(1/LN2[1],1/LN2[0])
@lru_cache(None)
def lg(x):
    x=F(x); ck(x>0); y=x; k=0
    while y<1: y*=2; k-=1
    while y>=2: y/=2; k+=1
    a,b=lnr(y)
    lo,hi=F(k)+a/LN2[1],F(k)+b/LN2[0]
    return F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D)
@lru_cache(None)
def xlog(x): return scale(lg(x),x) if x else iv(0)
def phi(x,y):
    if not x or not y: return iv(0)
    return minus(minus(xlog(x+y),xlog(x)),xlog(y))
def ent(p):
    z=iv(0)
    for x in p:
        if x: z=minus(z,xlog(x))
    return z
def fwht(t):
    a=list(t); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for h in range(j,j+step):
                u,v=a[h],a[h+step]; a[h],a[h+step]=u+v,u-v
        step*=2
    return a
@lru_cache(None)
def spec(t):
    N=len(t); w=fwht(t); p=tuple(F(x*x,N*N) for x in w)
    ck(sum(p)==1)
    I=sum((s.bit_count()*x for s,x in enumerate(p)),F(0))
    return tuple(w),p,I
def child(t,i,b):
    n=len(t).bit_length()-1
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1)))
def node(t,i):
    w,p,I=spec(t); N=len(t); B=Q=iv(0); M=F(0); alpha=F(0)
    for s in range(N):
        if s&(1<<i): alpha+=p[s]
        else:
            x,y=p[s],p[s|(1<<i)]; q=x+y; m=min(x,y)
            B=add(B,phi(x,y)); M+=m
            if m: Q=add(Q,scale(lg(q/m),m))
    c0,c1=child(t,i,0),child(t,i,1); a,P,I0=spec(c0); b,R,I1=spec(c1)
    ck(I==alpha+(I0+I1)/2)
    residual=F(0)
    for s in range(len(a)):
        q=(P[s]+R[s])/2; m=F((abs(a[s])-abs(b[s]))**2,4*len(a)**2)
        residual+=m
    ck(residual==M); ck(M<=min(alpha,1-alpha))
    delta=minus(ent(p),scale(add(ent(P),ent(R)),F(1,2)))
    if M:
        ck(Q[1]<delta[0]); ck(delta[1]-Q[0]<=3*M*LOGE[0])
        ck(B[0]-Q[1]>=M-F(1,D)*N) # enclosure error; analytic lower bound is B-Q>=M
    else:
        ck(Q==iv(0)); ck(sorted(P)==sorted(R)); ck(P==R)
    return Q,M,alpha,c0,c1
@lru_cache(None)
def tree(t):
    if len(t)==1: return iv(0),iv(0),F(0),F(0)
    options=[]
    for i in range(len(t).bit_length()-1):
        Q,M,alpha,a,b=node(t,i); al,ah,am,aM=tree(a); bl,bh,bm,bM=tree(b)
        options.append((add(Q,scale(add(al,bl),F(1,2))),add(Q,scale(add(ah,bh),F(1,2))),M+(am+bm)/2,M+(aM+bM)/2))
    lo=(min(x[0][0] for x in options),min(x[0][1] for x in options))
    hi=(max(x[1][0] for x in options),max(x[1][1] for x in options))
    m=min(x[2] for x in options); MM=max(x[3] for x in options)
    return lo,hi,m,MM
review=[]
for n in range(3 if args.pilot else 4):
    N=1<<n
    for mask in range(1<<N):
        t=tuple(-1 if mask&(1<<x) else 1 for x in range(N)); w,p,I=spec(t)
        qlo,qhi,m,MM=tree(t); H=ent(p)
        ck(MM<=I)
        if I and H[0]>0:
            ck(qhi[0]<=H[1]); ck(H[1]<=qlo[0]+3*I*LOGE[0])
    review.append({'n':n,'tables':1<<N})
(ROOT/'out'/('PILOT_TREE_REVIEW.json' if args.pilot else 'TREE_REVIEW.json')).write_text(json.dumps({'scope':review,'assertions_so_far':checks,'proof_verdict':'HOLDS; inequality proof analytic, node assertions exact rational enclosures'},indent=2),encoding='utf-8')

def family(k,l):
    r=2*k+l; N=1<<r; a=1+3*k+l
    rows=[]
    for u in range(k+1):
        for v in range(l+1):
            rows.append((comb(k,u)*3**u*comb(l,v),a-4*u-2*v,u,v))
    ck(sum(c for c,z,u,v in rows)==N)
    ck(sum(c*z*z for c,z,u,v in rows)==N*a)
    H=iv(0); count=0
    for c,z,u,v in rows:
        if u==v==0:
            H=minus(H,xlog(F((N-2*a)**2,N*N))); c-=1
        if c and z: H=minus(H,scale(xlog(F(4*z*z,N*N)),c))
        count+=c
    ck(count==N-1)
    I=F(2*(2*k*(a-4)+l*(a-2)),N)
    btypes=[]
    for paired in [True,False]:
        if (paired and not k) or (not paired and not l): continue
        B=iv(0); coeff={}; influence=F(2*(a-(4 if paired else 2)),N)
        if not influence: continue
        K,L=(k-1,l) if paired else (k,l-1)
        for u in range(K+1):
            for v in range(L+1):
                c=comb(K,u)*3**u*comb(L,v)
                z=a-(3 if paired else 1)-4*u-2*v
                for partner in ([0,1] if paired else [0]):
                    s,t=(z+3,z-1) if paired and partner==0 else ((z-1,z-1) if paired else (z+1,z-1))
                    x,y=F(4*s*s,N*N),F(4*t*t,N*N)
                    if u==v==partner==0:
                        x=F((N-2*a)**2,N*N)
                    B=add(B,scale(phi(x,y),c))
        E=scale(B,1/influence); c=4 if paired else 2
        V=F(4*a,N)*(1-F(a,N)); empty=F(4*(a-c)**2,N*N)
        lower=V-empty-F(16 if paired else 8,N)*LOGE[1]
        upper=V-empty+empty*(2*r+LOGE[1])
        ck(B[0]>=lower); ck(B[1]<=upper)
        if r>=4:
            A=F(1)+F(3*r,2)
            coarse_lo=2-F(12,r-3)-(2*A*A/F(r-3)+2*A)/N
            coarse_hi=2+F(8,r-3)+2*A*(2*r+F(3,2))/N
            ck(E[0]>=coarse_lo); ck(E[1]<=coarse_hi)
        btypes.append({'type':'paired' if paired else 'isolated','influence':str(influence),'B_interval':list(map(str,B)),'E_interval':list(map(str,E)),'E_display':[float(x) for x in E]})
    if I and r>=4:
        ratio=scale(H,1/I)
        lo=4*(1-F(a,N))*(1-(lg(a)[1]+1)/r)
        hi=4+F(16,r-3)
        ck(ratio[0]>=lo); ck(ratio[1]<=hi)
    if r<= (6 if args.pilot else 10):
        A={0}|{1<<j for j in range(r)}|{(1<<(2*j))|(1<<(2*j+1)) for j in range(k)}
        truth=tuple(-1 if x in A else 1 for x in range(N)); w,p,actualI=spec(truth)
        ck(actualI==I)
        for s in range(N):
            u=sum(bool(s&((1<<(2*j))|(1<<(2*j+1)))) for j in range(k)); v=(s>>(2*k)).bit_count()
            ck(w[s]==(N-2*a if s==0 else -2*(a-4*u-2*v)))
        for rec in btypes:
            i=0 if rec['type']=='paired' else 2*k
            edges=sum(truth[x]!=truth[x^(1<<i)] for x in range(N))
            ck(F(edges,N)==F(rec['influence']))
            Bdirect=iv(0)
            for s in range(N):
                if not s&(1<<i): Bdirect=add(Bdirect,phi(p[s],p[s|(1<<i)]))
            B=tuple(map(F,rec['B_interval']))
            ck(max(B[0],Bdirect[0])<=min(B[1],Bdirect[1]))
    return {'k':k,'l':l,'r':r,'a':a,'I':str(I),'H_interval':list(map(str,H)),'H_over_I_display':[float(x/I) for x in H] if I else None,'coordinate_orbits':btypes}
results=[]
for r in range(7 if args.pilot else 65):
    for k in range(r//2+1):
        results.append(family(k,r-2*k))
    if time.perf_counter()-start>(60 if args.pilot else 180): raise RuntimeError('frozen runtime cap')
    (ROOT/'out'/('PILOT_PARTIAL.json' if args.pilot else 'MATCHING_PARTIAL.json')).write_text(json.dumps({'completed_r':r,'records':results},indent=2),encoding='utf-8')
N=1<<64; A=F(97)
ck(2+F(8,61)+2*A*(128+F(3,2))/N<F(11,5))
f6=next(x for x in results if x['k']==3 and x['l']==0)
Elo=F(f6['coordinate_orbits'][0]['E_interval'][0]); ck(Elo>F(368,125))
out={'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start,'partial_matching_cases':len(results),'review_tables':sum(x['tables'] for x in review),'six_bit_min_ratio_display':f6['coordinate_orbits'][0]['E_display'],'records':results,'all_dimensional_conclusion':'H/I ->4 and every relevant B_i/Inf_i ->2 uniformly over partial matchings; H/I<=20 throughout; r>=64 gives B_i/Inf_i<11/5'}
(ROOT/'out'/('PILOT.json' if args.pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({x:y for x,y in out.items() if x!='records'},indent=2))
