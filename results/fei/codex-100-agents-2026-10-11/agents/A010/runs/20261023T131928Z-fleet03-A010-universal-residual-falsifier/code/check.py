from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import prod
import json, sys, time
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'out'
pilot='--pilot' in sys.argv
start=time.monotonic(); checks=0; anchor_runs=0
limit=55 if pilot else 180

def ck(x):
    global checks
    checks+=1
    assert x,checks
    if checks%2048==0: assert time.monotonic()-start<limit

def save(name,x):
    (OUT/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')

def subsets(mask):
    z=mask
    while True:
        yield z
        if not z:break
        z=(z-1)&mask

def local(mask):
    v=2**mask.bit_count(); d=v*(v-1)
    return [(x,1 if x else (v-1)**2) for x in subsets(mask)],d,F(1,v)

def integer_dp(covers):
    ab={0:(1,0)};den=1;rho=F(0)
    for mask in covers:
        opts,d,t=local(mask);den*=d;rho+=t;new={}
        for A,(a,b) in ab.items():
            for S,w in opts:
                u=A|S;aa,bb=new.get(u,(0,0))
                new[u]=(aa+a*w,bb+(b+bool(S)*a)*w)
        ab=new
    Q={a:F(b,den)/rho for a,(aa,b) in ab.items() if a}
    ck(sum(Q.values())==1)
    return Q

def explicit(covers,target=None):
    global anchor_runs
    opts=[local(m) for m in covers];rho=sum((z[2] for z in opts),F(0));Q={};posterior=[]
    for tup in product(*(z[0] for z in opts)):
        union=0
        for s,w in tup:union|=s
        if not union:continue
        for j,(sj,wj) in enumerate(tup):
            if not sj:continue
            anchor_runs+=1
            # Actual first-anchor probability and forced uniform nonempty draw,
            # followed by the fixed remaining independent draws.
            probability=opts[j][2]/rho/F(2**covers[j].bit_count()-1)
            for k,(sk,wk) in enumerate(tup):
                if k!=j:probability*=F(wk,opts[k][1])
            Q[union]=Q.get(union,F(0))+probability
            if union==target:posterior.append(probability)
    ck(sum(Q.values())==1)
    return Q,posterior

def walsh(v):
    a=v[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a

def physical(v,n):
    return F(sum(v[x]!=v[x^(1<<j)] for j in range(n) for x in range(len(v))),len(v))

logcache={}
def logs(x):
    x=F(x)
    if x in logcache:return logcache[x]
    original=x;e=0
    while x<1:x*=2;e-=1
    while x>=2:x/=2;e+=1
    def ln(y):
        z=(y-1)/(y+1)
        lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(16)),F(0))
        return lo,lo+2*z**33/F(33)/(1-z*z)
    lo,hi=ln(x);l2,u2=ln(F(2));L=e+lo/u2;U=e+hi/l2;scale=2**40
    L=F((L*scale).numerator//(L*scale).denominator,scale)
    U=F(-((-U*scale).numerator//(-U*scale).denominator),scale)
    logcache[original]=(L,U)
    return L,U

def cost(P,Q):
    grouped={}
    for A,p in enumerate(P):
        if A and p:
            ck(Q.get(A,0)>0)
            grouped[Q[A]]=grouped.get(Q[A],F(0))+p
    lo=hi=F(0)
    for q,p in grouped.items():
        l,u=logs(1/q);lo+=p*l;hi+=p*u
    return lo,hi

# Entire support-cover domain on three physical coordinates (no symmetry quotient).
cover_cases=0
for choose in range(1,9 if pilot else 128):
    covers=[m for m in range(1,8) if choose>>(m-1)&1]
    q=integer_dp(covers);e,_=explicit(covers)
    ck(q==e);ck(set(q)==set(subsets(__import__('functools').reduce(int.__or__,covers)))-{0})
    cover_cases+=1
q,post=explicit([3,6],2);ck(q[2]==F(5,18));ck(sorted(p/q[2] for p in post)==[F(1,20),F(1,20),F(9,20),F(9,20)])
duplicate=integer_dp([3,3]);ee,_=explicit([3,3]);ck(duplicate==ee)
save('COVER_CHECKPOINT.json',{'support_families':cover_cases,'actual_anchor_runs':anchor_runs,'center_mass':'5/18','center_posterior':['1/20','1/20','9/20','9/20']})

# Full disjoint paired cost and occupation reconstruction for the A006 statement.
paired=[]
lists=[(w,) for w in range(1,4)]+list(product(range(1,4),repeat=2))
for ws in lists[:3] if pilot else lists:
    b=sum(ws);n=2*b;N=1<<n;off=0;left=[]
    for w in ws:left.append(((1<<w)-1)<<off);off+=w
    right=[m<<b for m in left];covers=left+right
    v=[1 if all(x&m for m in left) and any((x&m)==m for m in right) else -1 for x in range(N)]
    fw=walsh(v);P=[F(c*c,N*N) for c in fw];I=physical(v,n)
    ts=[F(1,2**w) for w in ws];q=prod(1-t for t in ts);rho=sum(ts,F(0));D=sum((w*t/(1-t) for w,t in zip(ws,ts)),F(0))
    ck(I==2*q*D);ck(sum(a.bit_count()*p for a,p in enumerate(P))==I)
    M=[]
    for l,r,t in zip(left,right,ts):
        moment=sum((p*(bool(a&l)+bool(a&r)) for a,p in enumerate(P)),F(0));ck(moment==4*q*t);M.append(moment)
    Q=integer_dp(covers);direct=cost(P,Q);ck(direct[1]<F(155,24)*I)
    # Independently assemble all signed terms of the author's exact cost identity.
    vtot=1-P[0];L=U=F(0)
    for t in ts:
        l,u=logs(1/(1-t));L+=2*vtot*l;U+=2*vtot*u
    l,u=logs(2*rho);L+=vtot*l;U+=vtot*u
    for t,moment in zip(ts,M):
        l,u=logs((1-t)/t);L+=2*moment*l;U+=2*moment*u
    for a,p in enumerate(P):
        if not a or not p:continue
        K=sum(bool(a&m) for m in covers);l,u=logs(K);L-=p*u;U-=p*l
    ck(max(L,direct[0])<=min(U,direct[1]))
    paired.append({'widths':ws,'I':str(I),'cost_upper_bits':str(direct[1])})
    save('PAIRED_CHECKPOINT.json',paired)

# A008's ENTIRE unequal-width common-coordinate family and its repaired cost.
anchor=[]
lists=[ws for length in range(1,4) for ws in product(range(1,4),repeat=length)]
for ws in lists[:3] if pilot else lists:
    off=1;blocks=[]
    for w in ws:blocks.append(((1<<w)-1)<<off);off+=w
    n=off;N=1<<n;v=[1 if (x&1) or all(x&m for m in blocks) else -1 for x in range(N)]
    fw=walsh(v);P=[F(c*c,N*N) for c in fw];I=physical(v,n)
    es=[F(1,2**w) for w in ws];a=prod(1-e for e in es);J=a*sum((w*e/(1-e) for w,e in zip(ws,es)),F(0))
    ck(I==1-a+J);ck(P[1]==(1-a)**2)
    for block,e in zip(blocks,es):ck(sum((p for A,p in enumerate(P) if A&block),F(0))==2*a*e)
    Q=integer_dp([1|m for m in blocks]);R={A:q/2+F(int(A==1),2) for A,q in Q.items()}
    C=cost(P,R);ck(C[1]<=F(29,2)*I)
    vv=1-P[0];l,u=logs(1/vv) if vv else (F(0),F(0));wrapper=vv*u
    if vv<1:
        l,u=logs(1/(1-vv));wrapper+=(1-vv)*u
    ck(C[1]+wrapper<=F(33,2)*I)
    anchor.append({'widths':ws,'I':str(I),'cost_upper_bits':str(C[1])})
    save('ANCHOR_CHECKPOINT.json',anchor)

# New counterfamily: no private clone is substituted for z0,z1,z2.
newrows=[]
for r in ([1,2] if pilot else [1,2,3,4]):
    n=3+4*r;N=1<<n
    X=[3<<(3+2*j) for j in range(r)];Y=[3<<(3+2*r+2*j) for j in range(r)]
    covers=[3|m for m in X]+[6|m for m in Y]
    values=[1 if (x&2) or (((x&1) or all(x&m for m in X)) and ((x&4) or all(x&m for m in Y))) else -1 for x in range(N)]
    fw=walsh(values);I=physical(values,n);a=F(3,4)**r
    Ptarget=F(fw[5]**2,N*N)
    ck(Ptarget==(1-a)**4/16)
    exactI=F(5,4)-a/2-3*a*a/4+F(r,3)*a*(1+a)
    ck(I==exactI)
    ck(sum(A.bit_count()*c*c for A,c in enumerate(fw))==I*N*N)
    # Direct sums over only the actual local-mask tuples compatible with target5.
    # This includes ALL such tuples/anchors; forbidden-coordinate masks cannot output5.
    t=F(1,16);p=1-t;c=F(1,240);rho=2*r*t;mass=F(0);target_runs=0
    allowed=[[(0,p),(1,c)] for j in range(r)]+[[(0,p),(4,c)] for j in range(r)]
    for tup in product(*allowed):
        union=0
        for m,prob in tup:union|=m
        if union!=5:continue
        for j,(m,prob) in enumerate(tup):
            if not m:continue
            actual=t/rho/F(15)*prod(prob2 for k,(m2,prob2) in enumerate(tup) if k!=j)
            mass+=actual;target_runs+=1
    b=F(113,120);formula=F(1,15)*b**(r-1)*(b**r-p**r)
    ck(mass==formula)
    ck(all(5 not in set(subsets(core)) for core in [3,6,2]))
    if r>=4:ck(Ptarget>F(1,81) and F(5,4)<I<2)
    newrows.append({'r':r,'n':n,'inputs':N,'I':str(I),'P_outer_pair':str(Ptarget),'full_Q_outer_pair':str(mass),'actual_target_anchor_events':target_runs})
    save('NEW_CHECKPOINT.json',newrows)

ck(2*113**16<120**16)
scalar=0
for r in range(4,17 if pilot else 257):
    a=F(3,4)**r;p=(1-a)**4/16
    I=F(5,4)-a/2-3*a*a/4+F(r,3)*a*(1+a)
    ck(a<F(1,3));ck(r*a<=F(81,64));ck(F(5,4)<I<2);ck(p>F(1,81))
    ck(F(3*(r+1),4*r)<=F(15,16))
    ck(F(209,16)/I<11)
    scalar+=1

result={'status':'PASS','helper':'A010-two-intersecting-core-falsifier-v1','pilot':pilot,'assertions':checks,'seconds':time.monotonic()-start,'source_cover_families':cover_cases,'actual_anchor_runs_source':anchor_runs,'source_paired_cases':len(paired),'source_common_anchor_cases':len(anchor),'new_physical_cases':newrows,'all_size_scalar_checks':scalar,'source_review':'A006 full new law/disjoint payment and A008 full common-anchor obstruction/repair reconstructed; no source author helper imports','new_bound':'Every fixed mixture of Q and arbitrary laws individually supported within K1 or K2: C/I>(2r-1)/2592 for r>=4, although H/I<11','universal_FEI':'OPEN'}
save('PILOT.json' if pilot else 'CHECK.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='new_physical_cases'}))
