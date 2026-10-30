"""Frozen small exact check; all writes stay in this run. No external imports."""
from pathlib import Path
from fractions import Fraction as F
import json, time, hashlib, sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
OUT.mkdir(exist_ok=True)
N=0
def ck(b):
    global N
    N+=1
    assert b, N

def log_interval(x, terms=90):
    x=F(x); assert x>0
    e=0
    while x>=2: x/=2; e+=1
    while x<1: x*=2; e-=1
    def nat(v):
        z=(v-1)/(v+1); z2=z*z; power=z; total=F(0)
        for j in range(terms):
            total+=power/F(2*j+1); power*=z2
        return 2*total,2*total+2*power/(F(2*terms+1)*(1-z2))
    lo,hi=nat(x); l2,u2=nat(F(2))
    return F(e)+lo/u2,F(e)+hi/l2

def kl(p,q):
    lo=hi=F(0)
    for k,v in p.items():
        if v:
            l,u=log_interval(v/q[k]); lo+=v*l; hi+=v*u
    return lo,hi

def fwht(vals):
    a=list(map(F,vals)); m=len(a); h=1
    while h<m:
        for j in range(0,m,2*h):
            for k in range(j,j+h): a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return {k:v/m for k,v in enumerate(a) if v}

def physical(r,alpha):
    # bits: x=0,j=1,z=2,w starts at 3; epsilon=+1.
    n=r+3
    vals=[]
    for x in range(1<<n):
        j=(x>>1)&1; z=(x>>2)&1; w=x>>3
        v=(-1 if z else 1)*(-1 if w==0 or(j and w==3) else 1)
        vals.append(v if x&1 else 1)
    co=fwht(vals); p={k:v*v for k,v in co.items()}; full=(1<<n)-1
    ck(full in p); q={k:(1-alpha)*v for k,v in p.items()}
    q[full]+=alpha/4; q[full^1]+=alpha/4
    # Activation preserves the two controller-only atoms, each of mass 1/4.
    for k in [0,1]: q[k]=p[k]
    ck(sum(q.values())==1)
    ep={}; eq={}
    for k,v in p.items(): ep[k&~2]=ep.get(k&~2,F(0))+v
    for k,v in q.items(): eq[k&~2]=eq.get(k&~2,F(0))+v
    ss={k:co.get(k,F(0))*co.get(k|2,F(0))/v for k,v in ep.items()}
    mean=sum(ep[k]*ss[k] for k in ep); ck(mean==0)
    V=sum(ep[k]*ss[k]**2 for k in ep)
    X=sum(ep[k]*(eq[k]/ep[k]-1)**2 for k in ep)
    t=sum(eq[k]*ss[k] for k in ep)
    eta=sum(v for k,v in p.items() if k&2)
    d=F(1,1<<r); A=1-3*d
    vv=(d*d*A*A/(A*A+d*d)+F(7,10)*d-F(9,10)*d*d)/2
    ck(V==vv); ck(X==alpha*alpha*(1/(10*d*d)-1)/2)
    ck(t==-3*alpha/20); ck(eta==d/2)
    ck(V<=eta*(1-eta)); ck(t*t<=X*V)
    # Independent child Walsh spectra and own outcome normalization.
    children=[]; inherited=[]; outcome=[]
    for y in [0,1]:
        cv=[vals[k] for k in range(1<<n) if ((k>>1)&1)==y]
        cp0=fwht(cv)
        cp={((k&1)|((k>>1)<<2)):v*v for k,v in cp0.items()}
        kernel={k:F(1,2)+(-1 if y else 1)*ss[k] for k in ep}
        ck(all(cp.get(k,0)==2*ep[k]*kernel[k] for k in ep))
        ry=sum(eq[k]*kernel[k] for k in ep); ck(ry>0)
        iq={k:eq[k]*kernel[k]/ry for k in ep if kernel[k]}
        ck(sum(iq.values())==1)
        children.append(cp); inherited.append(iq); outcome.append(ry)
    ck(outcome==[F(1,2)+t,F(1,2)-t])
    root=kl(p,q); erased=kl(ep,eq)
    oi=kl({0:F(1,2),1:F(1,2)},dict(enumerate(outcome)))
    ki=[kl(p0,q0) for p0,q0 in zip(children,inherited)]
    ck(erased[0]<=oi[1]+sum(x[1] for x in ki)/2)
    ck(erased[1]>=oi[0]+sum(x[0] for x in ki)/2)
    ck(root[1]>=oi[0])
    return {'r':r,'alpha':str(alpha),'V':str(V),'chi2':str(X),'t':str(t),'checks':N}

def grouped(r):
    d=F(1,1<<r); a=F(1,r*r); b=1-a; A=1-3*d
    V=(d*d*A*A/(A*A+d*d)+F(7,10)*d-F(9,10)*d*d)/2
    X=a*a*(1/(10*d*d)-1)/2
    k=kl({0:d*d,1:1-d*d},{0:a+b*d*d,1:b*(1-d*d)})
    K=(k[0]/2,k[1]/2)
    l2,u2=log_interval(F(2)); # exact value 1, ln2 computed below via log2(e) unnecessary
    # Compare X*V to K without any numerical ln constant.
    ck(K[0]>0); ck(X*V>0); ck(V<=d/2*(1-d/2))
    # 1/2 < ln2 < 1 gives X V < 2 XV/ln2 < 4 XV.
    if r>=16: ck(2*X*V>K[1])
    return {'r':r,'alpha':str(a),'XV_over_K_lower':str(X*V/K[1]),
            'XV_over_K_illustrative':float(X*V/((K[0]+K[1])/2)),
            'V_over_d':str(V/d),'K_lo':str(K[0]),'K_hi':str(K[1])}

def main():
    start=time.perf_counter(); pilot='--pilot' in sys.argv
    rows=[physical(r,a) for r in ([3] if pilot else [3,4,5]) for a in [F(1,6),F(1,r*r)]]
    gr=[grouped(r) for r in ([8] if pilot else [3,4,8,16,32,64,128])]
    result={'status':'PASS','pilot':pilot,'checks':N,'runtime_seconds':time.perf_counter()-start,
            'physical':rows,'grouped':gr,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','pilot','checks','runtime_seconds']}))
if __name__=='__main__': main()
