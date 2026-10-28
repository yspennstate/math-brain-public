from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
B=Path(__file__).resolve().parents[1]

def submasks(x):
    yield 0
    y=x
    while y:yield y;y=(y-1)&x

def walsh(v):
    a=v[:];h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a

cache={}
def logs(x):
    x=F(x)
    if x in cache:return cache[x]
    orig=x;e=0
    while x<1:x*=2;e-=1
    while x>=2:x/=2;e+=1
    def ln(y):
        z=(y-1)/(y+1);s=2*sum((z**(2*j+1)/F(2*j+1) for j in range(16)),F(0))
        return s,s+2*z**33/(33*(1-z*z))
    l,u=ln(x);ll,uu=ln(F(2));lo=e+l/uu;hi=e+u/ll;scale=2**40
    lo=F((lo*scale).numerator//(lo*scale).denominator,scale)
    hi=F(-((-hi*scale).numerator//(-hi*scale).denominator),scale)
    cache[orig]=(lo,hi);return lo,hi

def run(pilot):
    started=time.monotonic();checks=0;rows=[];tuples=0;actual_events=0
    def ck(x):
        nonlocal checks
        checks+=1;assert x,checks
        if checks%1024==0:assert time.monotonic()-started<(55 if pilot else 120)
    for r in ([1] if pilot else [1,2]):
        n=3+4*r;N=1<<n
        X=[3<<(3+2*j) for j in range(r)];Y=[3<<(3+2*r+2*j) for j in range(r)]
        covers=[3|m for m in X]+[6|m for m in Y]
        # Independent complete allocation enumeration, not the two-array DP.
        integer_mass={};events=0
        for z in product(*(list(submasks(m)) for m in covers)):
            tuples+=1;K=sum(bool(m) for m in z)
            if not K:continue
            union=0
            for m in z:union|=m
            weight=K*225**(2*r-K)
            integer_mass[union]=integer_mass.get(union,0)+weight;events+=K
        actual_events+=events
        rho=F(r,8);den=240**(2*r)
        Q={A:F(w,den)/rho for A,w in integer_mass.items()}
        ck(sum(Q.values())==1 and len(Q)==N-1)
        R={A:q/2+(F(1,14) if A<8 else 0) for A,q in Q.items()}
        ck(sum(R.values())==1)
        ck(all(q>=F(1,240)**(2*r)/rho for q in Q.values()))
        ck(R[5]>=F(1,14)>Q[5]/2)
        ck(all(R[A]>=F(1,14) for A in range(1,8)))
        p=F(15,16);b=F(113,120)
        ck(Q[5]==F(1,15)*b**(r-1)*(b**r-p**r))
        v=[1 if (x&2) or (((x&1) or all(x&m for m in X)) and ((x&4) or all(x&m for m in Y))) else -1 for x in range(N)]
        fw=walsh(v);P=[F(c*c,N*N) for c in fw]
        I=F(sum(v[x]!=v[x^(1<<j)] for j in range(n) for x in range(N)),N)
        a=F(3,4)**r;M=sum((p for A,p in enumerate(P) if A>>3),F(0))
        ck(M==a*(1-a)+a*a*(1-a*a)/2)
        grouped={}
        for A,pA in enumerate(P):
            if A and pA:grouped[R[A]]=grouped.get(R[A],F(0))+pA
        C0=C1=F(0)
        for q,pA in grouped.items():
            l,u=logs(1/q);C0+=pA*l;C1+=pA*u
        ck(C1<24*I)
        ck(C1<4+17*r*M)
        rows.append({'r':r,'n':n,'truth_inputs':N,'allocation_tuples':16**(2*r),'actual_anchor_events':events,'nonempty_outputs':len(Q),'I':str(I),'M_private':str(M),'joint_cost_interval':[str(C0),str(C1)],'Q_outer_pair':str(Q[5]),'R_joint_outer_pair':str(R[5])})
    for r in range(4,17 if pilot else 257):
        a=F(3,4)**r;M=a*(1-a)+a*a*(1-a*a)/2
        I=F(5,4)-a/2-3*a*a/4+F(r,3)*a*(1+a)
        ck(M<F(7,6)*a);ck(r*a<=F(81,64));ck(I>F(5,4))
        ck(4+17*r*M<F(3725,128)<24*I)
    ck(F(3725,160)<24)
    result={'status':'PASS','helper':'A010-joint-core-repair-v1','pilot':pilot,'checks':checks,'seconds':time.monotonic()-started,'complete_allocation_tuples':tuples,'actual_anchor_events':actual_events,'rows':rows,'bound':'C_joint/I<3725/160<24 for every r>=4','new_class':'Fixed original Q plus uniform nonempty dictionary on ALL three public core coordinates'}
    (B/'out'/('JOINT_PILOT.json' if pilot else 'JOINT_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}))

run(True)
run(False)
