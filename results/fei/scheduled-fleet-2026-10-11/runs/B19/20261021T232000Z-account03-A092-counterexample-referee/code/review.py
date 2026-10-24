"""Independent truth-table/complete-reference audit. No peer helper imports."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, sys, hashlib

ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(b):
    global checks
    checks+=1
    assert b, checks

# For m in [1,2], z=(m-1)/(m+1) lies in [0,1/3].
# ln(m)=2 sum z^(2i+1)/(2i+1); tail <=9/[4(2N+1)3^(2N+1)].
# Each truncated summand is rounded DOWN at scale 2^112.
SCALE=1<<112
N=44
def ln_unit(m):
    z=(m-1)/(m+1);a,b=z.numerator,z.denominator
    total=sum((2*pow(a,2*i+1)*SCALE)//(pow(b,2*i+1)*(2*i+1)) for i in range(N))
    tail=F(9,4*(2*N+1)*3**(2*N+1))
    return F(total,SCALE),F(total+N,SCALE)+tail
L2=ln_unit(F(2))
@lru_cache(None)
def lg(x):
    x=F(x);assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    power=F(2)**k
    if x<power:k-=1;power/=2
    m=x/power
    assert 1<=m<2
    # First enclose the mantissa by dyadics; do not run a long series
    # on an exponentially long reset denominator.
    D=1<<100
    v=(m.numerator*D)//m.denominator
    lo=ln_unit(F(v,D))[0]; hi=ln_unit(F(v+1,D))[1]
    return lo/L2[1]+k,hi/L2[0]+k
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(c,a):
    return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def ce(p,q):
    ans=(F(0),F(0))
    for x,y in zip(p,q):
        if x:ans=add(ans,mul(-x,lg(y)))
    return ans
def ent(p):return ce(p,p)
def pretty(a):return [str(a[0]),str(a[1])]

def spectrum(vals):
    # Direct character sums, deliberately not the peer's FWHT path.
    size=len(vals)
    w=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals)) for s in range(size)]
    return [F(x,size) for x in w]
def edges(vals):
    dim=len(vals).bit_length()-1
    return [F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals))),len(vals)) for j in range(dim)]
def ib(p):return sum(F(s.bit_count())*v for s,v in enumerate(p))
def h2(x):return ent([x,1-x])

def run_case(n):
    t=F(1,2**n); M=2**(2*n-2)
    vals=[-1 if x in (0,1,3) else 1 for x in range(2**(n+1))]
    children=[vals[j::2] for j in (0,1)]
    w=spectrum(vals); p=[v*v for v in w]
    ws=[spectrum(v) for v in children]; ps=[[v*v for v in a] for a in ws]
    ck(sum(p)==1 and all(p));ck(all(len(set(v))==2 for v in children))
    ck(w[0]==1-3*t)
    for s in range(1,len(w)):
        sj=s&1; sy=(s>>1)&1
        ck(w[s]==-t*(1+(-1)**sj+(-1)**(sj+sy)))
    influences=edges(vals)
    ck(sum(influences)==(3*n-1)*t);ck(influences[0]==t);ck(ib(p)==sum(influences))
    q=[p[2*s]+p[2*s+1] for s in range(2**n)]
    ck(sum(q)==1 and all(q))
    for s in range(len(q)):ck(q[s]==(ps[0][s]+ps[1][s])/2)
    ck(q[0]==1-6*t+10*t*t);ck(q[1]==2*t*t)
    ck(ps[0][0]==(1-2*t)**2);ck(ps[0][1]==4*t*t);ck(ps[1][1]==0)
    ck(ps[0][1]*M==1)
    qnew=list(q);qnew[1]=q[1]/2**M;qnew[0]+=q[1]-qnew[1]
    ck(sum(qnew)==1 and all(qnew))
    tv=sum(abs(a-b) for a,b in zip(q,qnew))/2
    ck(tv==q[1]*(1-F(1,2**M)));ck(tv<F(1,2**(2*n-1)))
    ck(all(qnew[s]==q[s] for s in range(2,len(q))))
    # All marginal reference fibers are exactly the root's true fibers,
    # so the root conditional KL refund is exactly zero without logs.
    ck(all(p[2*s]/q[s]+p[2*s+1]/q[s]==1 for s in range(len(q))))
    erasure=(F(0),F(0))
    for s,v in enumerate(q):erasure=add(erasure,mul(v,h2(p[2*s+1]/v)))
    oldterminal=mul(F(1,2),add(ce(ps[0],q),ce(ps[1],q)))
    newterminal=mul(F(1,2),add(ce(ps[0],qnew),ce(ps[1],q)))
    root=ent(p)
    # Algebra proves the identity; these independently computed intervals
    # are consistency checks only.
    identity=sub(root,add(erasure,oldterminal));ck(identity[0]<=0<=identity[1])
    bill=sub(newterminal,oldterminal)
    formula=mul(F(1,2),sub((F(1),F(1)),mul(ps[0][0],lg(qnew[0]/q[0]))))
    ck(max(bill[0],formula[0])<=min(bill[1],formula[1]));ck(bill[0]>F(3,8))
    ck(root[1]<8*sum(influences));ck(q[0]>=ps[0][0]/2)
    if n>=3:ck(bill[0]>F(7,16));ck(4*q[1]<=F(1,8))
    else:ck(qnew[0]/q[0]==F(31,16))
    return dict(n=n,dimension=n+1,I=str(sum(influences)),query_influence=str(t),
                TV=str(tv),weighted_reset_interval=pretty(bill),formula_interval=pretty(formula),
                entropy_interval=pretty(root),full_root_support=True,nonconstant_children=True)

def minimality():
    # Exhaust every sign truth table in dimensions 1 and 2.
    eligible=0
    for d in (1,2):
        for table in range(2**(2**d)):
            vals=[1 if (table>>x)&1 else -1 for x in range(2**d)]
            for j in range(d):
                children=[[vals[x] for x in range(2**d) if (x>>j)&1==b] for b in (0,1)]
                if all(len(set(v))==2 for v in children):
                    eligible+=1;ck(not all(spectrum(vals)))
    return eligible

def main():
    tic=time.perf_counter();pilot='--pilot' in sys.argv
    cases=[run_case(n) for n in ([2,3] if pilot else [2,3,4,5,6,7])]
    eligible=minimality()
    # Side conditions in the all-n proof and the relative-error repair.
    for n in range(2,65):
        t=F(1,2**n);q0=1-6*t+10*t*t;p0=(1-2*t)**2
        ck(q0>0 and p0>0 and q0>=p0/2)
        ck(12*(n+1)<=8*(3*n-1))
        if n>=3:ck(8*t*t<=F(1,8))
    result=dict(status='PASS',cases=cases,case_count=len(cases),assertions=checks,
                minimality_eligible_splits=eligible,runtime_seconds=time.perf_counter()-tic,
                arithmetic='integer character sums/physical edges/Fraction; outward positive-atanh log intervals',
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    name='PILOT.json' if pilot else 'REVIEW.json'
    (ROOT/'out'/name).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
if __name__=='__main__':main()
