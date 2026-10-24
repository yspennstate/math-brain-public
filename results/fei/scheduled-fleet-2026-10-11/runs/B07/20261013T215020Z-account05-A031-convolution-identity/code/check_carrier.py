import argparse, json, time
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache

R=Path(__file__).resolve().parents[1]

def walsh(values):
    z=list(values); step=1
    while step<len(z):
        for base in range(0,len(z),2*step):
            for j in range(base,base+step):
                a,b=z[j],z[j+step]; z[j],z[j+step]=a+b,a-b
        step*=2
    return z

@lru_cache(None)
def factors(n):
    assert n>0
    ans=[];p=2
    while p*p<=n:
        exponent=0
        while n%p==0:n//=p;exponent+=1
        if exponent:ans.append((p,exponent))
        p+=1
    if n>1:ans.append((n,1))
    return tuple(ans)

def term(bag,coefficient,argument):
    if not coefficient:return
    for p,e in factors(argument):bag[p]+=coefficient*e

def cleaned(bag):return {p:c for p,c in bag.items() if c}

def verify(A,V):
    N=len(A); U=walsh(A); Z=walsh(V)
    assert all(a*v==0 and a*a+v*v==1 for a,v in zip(A,V))
    checks=1
    # All signed cross-shift identities, before any square is compared.
    for shift in range(N):
        assert sum(U[t]*Z[t^shift] for t in range(N))==0; checks+=1
    E=[t for t in range(N) if Z[t]]
    D=sum(v*v for v in Z); C=sum(U[t]**2+Z[t]**2 for t in E)
    assert 0<=D<=C<=N*N;checks+=1
    assert sum((U[t]+Z[t])**2 for t in E)==C
    assert sum((U[t]-Z[t])**2 for t in E)==C;checks+=2
    assert sum((U[t]+Z[t])**2 for t in range(N))==N*N
    assert sum((U[t]-Z[t])**2 for t in range(N))==N*N;checks+=2
    # Exact prime-log encodings, scaled by N^2.
    B=defaultdict(int); mu=defaultdict(int); coarse=defaultdict(int)
    for t in E:
        a=U[t]**2;b=Z[t]**2;q=a+b
        term(B,q,q);term(B,-a,a);term(B,-b,b)
        for mass,sector in [(a,C-D),(b,D)]:
            if mass:
                term(mu,mass,mass);term(mu,mass,C)
                term(mu,-mass,q);term(mu,-mass,sector)
    if C:
        term(coarse,C,C);term(coarse,-D,D);term(coarse,-(C-D),C-D)
    combined=defaultdict(int,B)
    for p,c in mu.items():combined[p]+=c
    assert cleaned(combined)==cleaned(coarse);checks+=1
    return checks

def census(max_m,cap):
    start=time.monotonic();counts={};assertions=0
    for m in range(max_m+1):
        N=1<<m
        for code in range(4**N):
            if time.monotonic()-start>cap-2:raise RuntimeError('Frozen cap approached')
            A=[];V=[]
            for x in range(N):
                digit=(code>>(2*x))&3
                A.append((1,-1,0,0)[digit]);V.append((0,0,1,-1)[digit])
            assertions+=verify(A,V)
        counts[m]=4**N
        (R/'out/checkpoint.json').write_text(json.dumps({'counts':counts,'integer_assertions':assertions}))
    return {'counts':counts,'cases':sum(counts.values()),'integer_assertions':assertions,
            'runtime_seconds':time.monotonic()-start,'arithmetic':'integer signed Walsh, exact integer prime-log coefficients'}

@lru_cache(None)
def ln_unit(x):
    assert Q(1)<=x<=Q(2)
    z=(x-1)/(x+1);power=z;lo=Q(0)
    for j in range(40):
        lo+=2*power/Q(2*j+1);power*=z*z
    return lo,lo+2*power/(81*(1-z*z))

@lru_cache(None)
def lg(x):
    x=Q(x);assert x>0;k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    a,b=ln_unit(x);c,d=ln_unit(Q(2))
    return k+a/d,k+b/c

def logs(parts):
    lo=hi=Q(0)
    for weight,argument in parts:
        if not weight:continue
        a,b=lg(argument)
        if weight>=0:lo+=weight*a;hi+=weight*b
        else:lo+=weight*b;hi+=weight*a
    return lo,hi

def hparts(d):return [(x,1/x) for x in (d,1-d) if x]

def rounded_upper(x):
    # Outward rounding only: saves a short exact rational certificate.
    denominator=1<<128
    return Q(-((-x.numerator*denominator)//x.denominator),denominator)

def targeted():
    start=time.monotonic();out={}
    d=Q(25,169);rho=Q(49,169)
    left=logs(hparts(d)); right=logs([(rho*w,arg) for w,arg in hparts(d/rho)])
    assert left[0]>right[1] and left[0]>rho and right[1]<=rho
    out['nonBoolean']={'u':'12/13','v':'-5/13','d':str(d),'claimed_child_rho':str(rho),
        'left_interval':list(map(str,left)),'right_interval':list(map(str,right)),
        'gap_lower':str(left[0]-right[1]),'strict_sign':'CERTIFIED_RATIONAL_INTERVAL'}
    records=[]
    for n in [3,4,8,16,32,64]:
        lower=Q(sum(max(0,j-5) for j in range(1,n+1)),n)
        assert lower==Q(max(0,n-5)*max(0,n-4),2*n)
        # Active nodes: B=2d(1-d)+phi((1-d)^2,d^2).
        node_certs=[]
        for j in range(1,n+1):
            d=Q(1,1<<(j-1));a=(1-d)**2;b=d*d
            if a and b:
                phi=logs([(a,(a+b)/a),(b,(a+b)/b)])
                B=(2*d*(1-d)+phi[0],2*d*(1-d)+phi[1])
            else:B=(Q(0),Q(0))
            upper=rounded_upper(B[1])
            assert B[1]<=upper<3*d
            node_certs.append({'remaining_dimension':j,'d':str(d),'B_upper':str(upper),'3d_minus_upper':str(3*d-upper)})
        records.append({'n':n,'I':str(n*Q(1,1<<(n-1))),'coarse_K4_ratio_lower':str(lower),
                        'true_D4':'0','all_adaptive_orders':'ANALYTIC_UNIQUE_ACTIVE_PATH','nodes':node_certs})
    out['point_defect']=records
    # Disjoint Boolean tensor guard, checked without admitting arbitrary spectra.
    tensor=[]
    phases=[([1,0,0,0],[0,1,-1,1]),([1,1,-1,-1],[0,0,0,0]),([0,0,0,0],[1,-1,1,-1])]
    signs=[[1,1,1,-1],[1,-1,1,-1],[1,1,1,1]]
    for A,V in phases:
        U=walsh(A);Z=walsh(V);N=len(A)
        d=Q(sum(z*z for z in Z),N*N);rho=Q(sum(u*u+z*z for u,z in zip(U,Z) if z),N*N)
        for b in signs:
            AA=[a*s for a in A for s in b];VV=[v*s for v in V for s in b]
            checks=verify(AA,VV);UU=walsh(AA);ZZ=walsh(VV);NN=len(AA)
            assert Q(sum(z*z for z in ZZ),NN*NN)==d
            assert Q(sum(u*u+z*z for u,z in zip(UU,ZZ) if z),NN*NN)==rho
            tensor.append({'d':str(d),'rho':str(rho),'integer_assertions':checks+2})
    out['tensor_guards']=tensor;out['runtime_seconds']=time.monotonic()-start
    assert out['runtime_seconds']<60
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');p.add_argument('--full',action='store_true');p.add_argument('--targeted',action='store_true');args=p.parse_args()
    assert sum([args.pilot,args.full,args.targeted])==1
    if args.targeted:ans=targeted();name='certificates.json'
    else:ans=census(2 if args.pilot else 3,60 if args.pilot else 240);name='pilot.json' if args.pilot else 'validation.json'
    (R/'out'/name).write_text(json.dumps(ans,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'output':name,'cases':ans.get('cases'),'integer_assertions':ans.get('integer_assertions'),'runtime_seconds':ans['runtime_seconds']}))
