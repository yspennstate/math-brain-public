from pathlib import Path
from fractions import Fraction as F
from math import comb
import argparse, json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
checks=0
def check(ok):
    global checks
    checks+=1
    assert ok, checks

def log_interval(x,N=24):
    assert F(1)<=x<=2
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
    return lo,lo+2*z**(2*N+1)/(F(2*N+1)*(1-z*z))

def scale(c):
    t=abs(c); j=0
    assert 0<t<=1
    while t<=F(1,2):
        t*=2; j+=1
    return j,t

def truth(m):
    return [1 if 3*((x&1)>0)+3*((x&2)>0)+2*(x>>2).bit_count()>=5 else -1
            for x in range(1<<(m+2))]

def spectrum(table,ps):
    n=len(ps); cs=[F(x) for x in table]
    for i,p in enumerate(ps):
        bit=1<<i
        for mask in range(1<<n):
            if mask&bit: continue
            a,b=cs[mask],cs[mask|bit]
            cs[mask]=(1-p)*a+p*b
            cs[mask|bit]=(b-a)/2
    vs=[4*p*(1-p) for p in ps]
    P=[]
    for s,c in enumerate(cs):
        v=F(1)
        for i in range(n):
            if s>>i&1:v*=vs[i]
        P.append(v*c*c)
    return cs,P,vs

def direct_coefficient(table,ps,s):
    total=F(0);v=F(1)
    for i,p in enumerate(ps):
        if s>>i&1:v*=4*p*(1-p)
    for x,y in enumerate(table):
        term=F(y)
        for i,p in enumerate(ps):
            b=(x>>i)&1
            term*=p if b else 1-p
            if s>>i&1:term*=2*b-2*p
        total+=term
    return total/v

def prime_rows(table,n):
    for a in range(1, (1<<n)-1):
        if a.bit_count()<2:continue
        b=((1<<n)-1)^a
        inside=[x for x in range(1<<n) if x&~a==0]
        outside=[x for x in range(1<<n) if x&~b==0]
        rows={tuple(table[x|y] for y in outside) for x in inside}
        check(len(rows)>=3)

def case(m,e,pilot=False):
    n=m+2; ps=[F(1,2)]*2+[e]*m;table=truth(m)
    cs,P,vs=spectrum(table,ps)
    check(sum(P)==1)
    if pilot:
        for s,c in enumerate(cs):check(c==direct_coefficient(table,ps,s))
    I=sum((s.bit_count()*p for s,p in enumerate(P)),F(0))
    var=1-P[0]; delta=I-var
    R=sum(((s.bit_count()-2)*p for s,p in enumerate(P) if s.bit_count()>=3),F(0))
    check(R>0)
    qs=[F(comb(m,k))*e**k*(1-e)**(m-k) for k in range(m+1)]
    tc=sum(qs[:3])/2; c12=(qs[0]-qs[1]-qs[2])/2
    check(cs[1]==tc and cs[2]==tc and cs[3]==c12)
    tr=F(1,2)*(1-e)**(m-1)+F(1,4)*comb(m-1,2)*e**2*(1-e)**(m-3)
    for i in range(2,n):check(cs[1<<i]==tr)
    check(I==2*tc+m*4*e*(1-e)*tr)
    for c in [tc,c12]:check(scale(c)[0]==1)
    j1=F(0); jhi=F(0); ml=F(0);mu=F(0)
    for s,c in enumerate(cs):
        if not s or not c:continue
        j,u=scale(c)
        if s.bit_count()==1:
            j1+=P[s]*j
            lo,hi=log_interval(1/u)
            ml+=P[s]*lo;mu+=P[s]*hi
        else:jhi+=P[s]*j
    # ml <= L1/2 <= mu. D is (Bstar+ln4 R)/ln4.
    dlo=2*delta-j1-mu; dhi=2*delta-j1-ml
    check(dlo>0 and dhi<=5*m*e)
    check(dlo-R>=0)  # Bstar nonnegative, independently with log intervals
    check(jhi>=F(9,64))
    check(jhi>=F(9,320*m)/e*dhi)
    a=F(comb(m,3))*e**3
    check(tc>F(1,4) and c12>=F(3,8))
    check(tc>=(1-a)/2 and j1>=F(1,2)-a)
    check(I<=1+2*m*e and var>=F(3,4))
    check(table[3]==1 and table[12]==-1)
    prime_rows(table,n)
    if pilot:
        # Every three-bit restriction used to certify positive high degree.
        restricted=[table[(x&3)|((x&4))] for x in range(8)]
        check(restricted==[-1,-1,-1,1,-1,1,1,1])
    return {'m':m,'epsilon':str(e),'Delta':str(delta),'R':str(R),
            'Jhi_over_ln4':str(jhi),'denominator_lower':str(dlo),
            'denominator_upper':str(dhi),'ratio_certified_lower':str(F(9,320*m)/e)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    start=time.perf_counter()
    domain=[(3,F(1,24))] if args.pilot else [(m,F(1,k*m)) for m in [3,4,5,6] for k in [8,16,64,256]]
    rows=[]
    for m,e in domain:
        rows.append(case(m,e,args.pilot))
        assert time.perf_counter()-start<55
    # Actual deterministic contraction gives AND2, independently of product basis division.
    for m in [3,4,5,6]:check(truth(m)[:4]==[-1,-1,-1,1])
    out={'status':'PASS','checks':checks,'cases':len(rows),'runtime_seconds':time.perf_counter()-start,
         'rows':rows,'arithmetic':'exact Fraction and outward rational log intervals',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    target=ROOT/'out'/('PILOT.json' if args.pilot else 'CHECKS.json')
    target.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
