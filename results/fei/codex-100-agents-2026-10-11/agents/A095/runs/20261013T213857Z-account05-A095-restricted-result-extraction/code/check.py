from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement
from pathlib import Path
import json,time

ROOT=Path(__file__).resolve().parents[1]
checks=0
def test(condition):
    global checks
    assert condition
    checks+=1

@lru_cache(None)
def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,0)+1
    return tuple(out.items())

def addlog(form,coefficient,x):
    if not coefficient:return
    x=F(x);assert x>0
    for p,k in factors(x.numerator):form[p]=form.get(p,F(0))+coefficient*k
    for p,k in factors(x.denominator):form[p]=form.get(p,F(0))-coefficient*k
    for p in list(form):
        if not form[p]:del form[p]

def combine(*terms):
    out={}
    for scale,form in terms:
        for p,c in form.items():out[p]=out.get(p,F(0))+scale*c
    return {p:c for p,c in out.items() if c}

def ce(p,q=None):
    if q is None:q=p
    out={}
    for v,w in zip(p,q):
        if v:addlog(out,-v,w)
    return out

@lru_cache(None)
def logbracket(x):
    x=F(x);j=0
    while x>=2:x/=2;j+=1
    while x<1:x*=2;j-=1
    def inner(x):
        z=(x-1)/(x+1);s=sum((2*z**(2*k+1)/F(2*k+1) for k in range(40)),F(0))
        err=2*z**81/(81*(1-z*z))
        return s,s+err
    a,b=inner(x);c,d=inner(F(2))
    return (a+j*c,b+j*d) if j>=0 else (a+j*d,b+j*c)

def nonnegative(form):
    if not form:return True
    lo=F(0)
    for p,c in form.items():
        a,b=logbracket(F(p));lo+=c*(a if c>=0 else b)
    return lo>=0

def fwht(values):
    a=values[:];h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def spectrum(table):
    n=len(table);p=[F(a*a,n*n) for a in fwht(table)]
    test(sum(p)==1);return p

def energy(table):
    n=len(table).bit_length()-1
    return sum((F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table)) for i in range(n)),F(0))

def biascalibrate(p,reference):
    v=1-p[0]
    if not v:return [F(1)]+[F(0)]*(len(p)-1)
    return [p[0]]+[v*x/(1-reference[0]) for x in reference[1:]]

def reference(n,theta):
    return [theta**s.bit_count()*(1-theta)**(n-s.bit_count()) for s in range(1<<n)]

def activation(table,r):
    return [table[x>>r] if x&((1<<r)-1)==0 else 1 for x in range(len(table)*(1<<r))]

def transfer(R,mu,r):
    p=F(1,1<<r);out=[]
    for t in range(len(R)):
        for u in range(1<<r):
            out.append((1-p*(1-mu))**2 if t==u==0 else p*p*(1-mu)**2 if t==0 else p*p*R[t])
    test(sum(out)==1);return out

def analyse_activation(table,r,R,pbase=None):
    pcore=spectrum(table) if pbase is None else pbase
    mu=F(sum(table),len(table));cal=biascalibrate(pcore,R)
    test(cal[0]==mu*mu);test(sum(cal)==1)
    C=ce(pcore,cal);H=ce(pcore)
    test(nonnegative(combine((1,ce(pcore,R)),(-1,C))))
    target=activation(table,r);pf=spectrum(target);Q=transfer(cal,mu,r);p=F(1,1<<r)
    expected=transfer(pcore,mu,r)
    test(pf==expected)
    test(energy(target)==p*(energy(table)+r*(1-mu)))
    CF=ce(pf,Q);HF=ce(pf)
    test(not combine((1,CF),(-1,HF),(-p,C),(p,H)))
    margin=combine((p,C),(-1,CF));addlog(margin,6*r*p*(1-mu),F(2))
    test(nonnegative(margin))
    test(Q[0]==pf[0])
    if r==1:
        delta=combine((1,HF),(-F(1,2),H))
        scalar={}
        for x in (((1+mu)/2)**2,((1-mu)/2)**2):
            if x:addlog(scalar,-x,x)
        addlog(scalar,1-mu*mu,F(2))
        if mu:addlog(scalar,F(1,2)*mu*mu,mu*mu)
        test(not combine((1,delta),(-1,scalar)))
    return CF,HF,energy(target)

def defect_product(widths,terminal=None):
    k=0 if terminal is None else len(terminal).bit_length()-1
    n=k+sum(widths);table=[]
    for x in range(1<<n):
        v=1 if terminal is None else terminal[x&((1<<k)-1)]
        at=k
        for w in widths:
            if ((x>>at)&((1<<w)-1))==0:v=-v
            at+=w
        table.append(v)
    return table

def block_reference(widths,terminal_R=None):
    R=[F(1)] if terminal_R is None else terminal_R[:]
    for w in widths:
        a=F(1,1<<w);local=[(1-2*a)**2]+[4*a*a]*((1<<w)-1)
        R=[x*y for y in local for x in R]
    test(sum(R)==1);return R

def main():
    start=time.monotonic();counts={'core_reference_controls':0,'block_controls':0,'terminal_controls':0,'diagonal':0}
    for n in range(1,4):
        for mask in range(1<<(1<<n)):
            table=[1 if mask>>x&1 else -1 for x in range(1<<n)];pc=spectrum(table)
            for r in range(1,4):
                for theta in (F(1,2),F(1,3),F(2,3)):
                    analyse_activation(table,r,reference(n,theta),pc)
                    counts['core_reference_controls']+=1
            test(time.monotonic()-start<60)
    tuples=[ws for m in range(1,4) for ws in combinations_with_replacement(range(1,5),m) if sum(ws)<=8]
    for ws in tuples:
        table=defect_product(ws);pc=spectrum(table);R=block_reference(ws)
        test(pc==R)
        budget=4*energy(table)
        margin={};addlog(margin,budget,F(2));margin=combine((1,margin),(-1,ce(pc)))
        test(nonnegative(margin))
        for r in range(3):
            if r:
                C,H,I=analyse_activation(table,r,R,pc)
                test(C==H)
                bound={};addlog(bound,6*I,F(2));test(nonnegative(combine((1,bound),(-1,C))))
            counts['block_controls']+=1
    for n in (1,2):
        for mask in range(1<<(1<<n)):
            terminal=[1 if mask>>x&1 else -1 for x in range(1<<n)]
            pq=spectrum(terminal);Rq=biascalibrate(pq,reference(n,F(1,3)));Cq=ce(pq,Rq)
            for ws in ((1,),(2,),(1,1),(1,2),(2,2)):
                table=defect_product(ws,terminal);R=block_reference(ws,Rq);pc=spectrum(table)
                Ih=sum(F(2*w,1<<w) for w in ws)
                test(energy(table)==energy(terminal)+Ih)
                for r in (1,2):
                    C,H,I=analyse_activation(table,r,R,pc);p=F(1,1<<r);mu=F(sum(table),len(table))
                    rhs=combine((p,Cq));addlog(rhs,p*4*Ih+6*r*p*(1-mu),F(2))
                    test(nonnegative(combine((1,rhs),(-1,C))))
                    counts['terminal_controls']+=1
    for L in range(2,33):
        t=4**L;r=4*L+1;p=F(1,1<<r);Ih=F(2*L,1<<L);N=t*L+1
        test((1+F(1,t))**2<2)
        test(4*L+2<=2*L*2**L)
        test(F(t*L,t*Ih+1+r)>=2**(L-2))
        test(p*(2*L*2**L+4*L+2)==p*(t*Ih+1+r))
        # Source diagonal's H bound reduces to 3<4 after the explicit
        # elementary -a ln a <=1-a and ln2>2/3 comparisons.
        test(4*t*Ih+4*r+3<4*(t*Ih+1+r))
        test(3*logbracket(F(2))[0]>2)
        counts['diagonal']+=1
    test(counts=={'core_reference_controls':2484,'block_controls':81,'terminal_controls':200,'diagonal':31})
    result={'helper_version':'A095-common-spine-reference-v1','status':'PASS','exact_assertions':checks,'counts':counts,'runtime_seconds':time.monotonic()-start,'max_truth_table_dimension':10,'note':'Finite certificates supplement all-parameter analytic derivation; no universal core bound asserted'}
    (ROOT/'out/EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps(result))

if __name__=='__main__':main()
