from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,time

start=time.perf_counter()
out=Path(__file__).resolve().parents[1]/'out'
checks=0
def ck(v):
    global checks
    assert v
    checks+=1

def factors(n):
    result={}
    d=2
    while d*d<=n:
        while n%d==0:
            result[d]=result.get(d,0)+1
            n//=d
        d+=1
    if n>1: result[n]=result.get(n,0)+1
    return result

def add(D,E,c=Q(1)):
    for p,x in E.items():
        D[p]=D.get(p,Q(0))+c*x
        if D[p]==0: del D[p]
    return D

def log(q):
    D={p:Q(x) for p,x in factors(q.numerator).items()}
    return add(D,{p:Q(x) for p,x in factors(q.denominator).items()},Q(-1))

def term(p):
    return {k:-p*v for k,v in log(p).items()} if p else {}

def entropy(P):
    D={}
    for p in P: add(D,term(p))
    return D

def walsh(table):
    n=(len(table)-1).bit_length()
    return [Q(sum(y*(-1)**((x&S).bit_count()%2) for x,y in enumerate(table)),len(table)) for S in range(len(table))]

def P(table): return [x*x for x in walsh(table)]

activation_count=0
for m in [1,2,3]:
    for mask in range(1,(1<<(1<<m))-1):
        table=[-1 if mask>>x&1 else 1 for x in range(1<<m)]
        core=P(table)
        q=Q(sum(x==-1 for x in table),len(table))
        V=1-core[0]
        for r in [1,2,3]:
            p=Q(1,1<<r)
            actual=P(table+[1]*(len(table)*((1<<r)-1)))
            D={}
            add(D,entropy(core[1:]),p)
            add(D,{2:Q(1)},2*r*p*V)
            add(D,log(1/(4*p*p*q*q)),4*p*q*q*(1-p))
            add(D,term((1-2*p*q)**2))
            ck(D==entropy(actual))
            if q==Q(1,2):
                B={}
                add(B,entropy(core),p)
                add(B,{2:Q(1)},2*r*p*(2-p))
                add(B,term((1-p)**2))
                ck(B==D)
            activation_count+=1

for w in [1,2,3]:
    for s in [1,2,3]:
        z=Q(1,1<<w); q=1-(1-z)**s; v=4*q*(1-q); E=4*s*z*(1-z)**s
        n=w*s; blocks=[((1<<w)-1)<<(j*w) for j in range(s)]
        table=[-1 if any(x&B==0 for B in blocks) else 1 for x in range(1<<n)]
        D=term((1-2*q)**2)
        add(D,{2:Q(1)},-2*v+2*w*E)
        add(D,log(1/(1-z)),2*(s*v-E))
        ck(D==entropy(P(table)))

for n in [1,3,5,7,9]:
    t=(n+1)//2
    table=[-1 if n-x.bit_count()>=t else 1 for x in range(1<<n)]
    probs=P(table)
    levels=[sum((p for S,p in enumerate(probs) if S.bit_count()==d),Q(0)) for d in range(n+1)]
    D=entropy(levels)
    for d,W in enumerate(levels): add(D,log(Q(comb(n,d))),W)
    ck(D==entropy(probs))

allocation_sets=0
for n in [3,5]:
    t=(n+1)//2
    terms=[R for R in range(1<<n) if R.bit_count()==t]
    for A in range(1,1<<n):
        d=A.bit_count()
        if d<=t:
            best=min(Q((A&R).bit_count(),d)**d for R in terms if A&~R==0)
            ck(best==1)
        else:
            best=None
            B=(A-1)&A
            while B:
                C=A^B
                if C:
                    b,c=B.bit_count(),C.bit_count()
                    for R in terms:
                        if B&~R: continue
                        for T in terms:
                            if C&~T or T==R: continue
                            val=Q((R&A).bit_count(),b)**b * Q((T&A).bit_count(),c)**c
                            best=val if best is None else min(best,val)
                B=(B-1)&A
            target=Q(t,t-1)**(t-1) if d==n else Q(1)
            ck(best==target)
        allocation_sets+=1

for a in range(64):
    n=2*a+1
    c=lambda j:Q(comb(2*j,j),4**j)
    ck(sum((c(j)*c(a-j) for j in range(a+1)),Q(0))==1)
    W=[]
    for j in range(a+1):
        b=c(a)*Q(comb(a,j),comb(2*a,2*j))
        mass=comb(n,2*j+1)*b*b
        ck(mass==Q(n,2*j+1)*c(a)*c(j)*c(a-j))
        W.append(mass)
    ck(sum(W)==1)
    ck(sum((mass*(2*j+1) for j,mass in enumerate(W)),Q(0))==n*c(a))
    if a:
        ck(c(a)*c(a)>=Q(1,4*a))
        # Exact induction step for the all-a Wallis lower bound.
        ck(Q(1,4*a)*Q(2*a+1,2*a+2)**2>=Q(1,4*(a+1)))
    if a>=8:
        js=list(range((a+3)//4,(a-1)//2+1))
        ck(len(js)*8>=a)
        for j in js:
            ck((2*j+1)*2>=a and 2*j+1<=a)
            ck(comb(n,2*j+1)>=2**(2*j+1))
            ck(W[j]**2>=Q(1,64*a**3))

ck(activation_count==810 and allocation_sets==38)
result={'status':'PASS','exact_assertions':checks,'activation_entropy_cases':activation_count,
        'allocation_sets':allocation_sets,'majority_closed_form_dimensions':64,
        'elapsed_seconds':time.perf_counter()-start,
        'arithmetic':'Fraction and formal log2-prime basis; direct Walsh sums independent of FWHT'}
(out/'symbolic_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
