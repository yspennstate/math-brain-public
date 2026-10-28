import json, time, argparse, hashlib
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); checks=0
def ck(b):
    global checks
    checks+=1
    if not b: raise AssertionError(checks)
    if time.perf_counter()-START>55: raise RuntimeError('55s frozen cap')
def lnbox(x):
    assert Q(7,8)<=x<=1
    z=(x-1)/(x+1); N=40
    val=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(N)),Q(0))
    err=2*abs(z)**(2*N+1)/(Q(2*N+1)*(1-z*z))
    return val-err,val+err
def transform(table,p):
    c=list(map(Q,table)); n=len(p)
    for i,pi in enumerate(p):
        for a in range(1<<n):
            if a>>i&1: continue
            lo,hi=c[a],c[a+(1<<i)]
            c[a]=(1-pi)*lo+pi*hi; c[a+(1<<i)]=(hi-lo)/2
    mass=[]
    for a,ca in enumerate(c):
        v=Q(1)
        for i,pi in enumerate(p):
            if a>>i&1: v*=4*pi*(1-pi)
        mass.append(v*ca*ca)
    return c,mass
def dist(e):
    q=[Q(1)]
    for x in e:
        q=[(q[k] if k<len(q) else 0)*(1-x)+(q[k-1] if k else 0)*x for k in range(len(q)+1)]
    return q
def elementary(e,k):
    import itertools
    return sum((__import__('functools').reduce(lambda a,b:a*b,t,Q(1)) for t in itertools.combinations(e,k)),Q(0))
def primeness(table,n):
    for A in range(1,1<<n):
        if not 2<=A.bit_count()<n: continue
        ins=[a for a in range(1<<n) if a&~A==0]
        outs=[a for a in range(1<<n) if a&A==0]
        rows={tuple(table[a|b] for b in outs) for a in ins}
        ck(len(rows)>=3)
def case(e,direct=False,modules=True):
    m=len(e); n=m+2; p=[Q(1,2)]*2+e
    table=[1 if 3*(a&1)+3*((a>>1)&1)+2*(a>>2).bit_count()>=5 else -1 for a in range(1<<n)]
    c,P=transform(table,p); ck(sum(P)==1)
    s=sum(e); e2=elementary(e,2); e3=elementary(e,3)
    I=sum(a.bit_count()*v for a,v in enumerate(P)); V=1-P[0]; D=I-V
    R=sum(max(0,a.bit_count()-2)*v for a,v in enumerate(P)); A=sum(P[1<<i] for i in range(n))
    ck(2*D-R==I-A)
    if modules: primeness(table,n)
    q=dist(e); tc=sum(q[:3])/2
    ck(c[1]==c[2]==tc); ck(c[3]==(q[0]-q[1]-q[2])/2)
    ck(Q(3,8)<=c[3]<=Q(1,2)); ck(c[3]*c[3]>=Q(9,64))
    ts=[tc,tc]
    for i in range(m):
        r=dist(e[:i]+e[i+1:]); ti=r[0]/2+r[2]/4 if len(r)>2 else r[0]/2
        ck(c[1<<(i+2)]==ti); ts.append(ti)
        si=s-e[i]; delta=Q(1,2)-ti
        ck((1-s)*si/2<=delta<=si/2)
        ck(0<=si/2-delta<=Q(3,4)*elementary(e[:i]+e[i+1:],2))
    blo=bhi=Q(0); j1=Q(0)
    for i,(t,pi) in enumerate(zip(ts,p)):
        ck(Q(7,16)<=t<=Q(1,2)); v=4*pi*(1-pi)
        lo,hi=lnbox(2*t); phi=t-2*t*t
        blo+=v*(phi+t*t*lo); bhi+=v*(phi+t*t*hi)
        ck(P[1<<i]==v*t*t); j1+=P[1<<i]
        ck(v*t==sum(P[a] for a in range(1<<n) if a>>i&1))
    ck(blo>=Q(49,64)*e2); ck(bhi<=(2+s/6)*e2)
    ck(blo>=2*e2-4*s*e2); ck(bhi<=2*e2+4*s*e2)
    ck(3*e3<=s*e2)
    # Independent physical-coefficient formula (direct product moments).
    if direct:
        for a in range(1<<n):
            got=Q(0); va=Q(1)
            for i,pi in enumerate(p):
                if a>>i&1: va*=4*pi*(1-pi)
            for b,fb in enumerate(table):
                w=Q(fb)
                for i,pi in enumerate(p):
                    xi=1 if b>>i&1 else -1
                    w*=pi if b>>i&1 else 1-pi
                    if a>>i&1: w*=xi-(2*pi-1)
                got+=w
            ck(got/va==c[a])
    return {'m':m,'rare':[str(x) for x in e],'s':str(s),'e2':str(e2),
            'B_over_ln4_interval':[str(blo),str(bhi)],'Delta':str(D),'R':str(R),
            'core_pair_mass':str(P[3])}
def main():
    pilot=argparse.ArgumentParser(); pilot.add_argument('--pilot',action='store_true'); args=pilot.parse_args()
    rows=[]
    for m in ([3] if args.pilot else [3,4,5]):
        profiles=[[Q(1,8*m)]*m,[Q(1,32*m)]*m,[Q(1,16)]+[Q(1,64*m)]*(m-1),[Q(1,16)]+[Q(1,4096*m)]*(m-1)]
        if args.pilot: profiles=profiles[:2]
        for e in profiles: rows.append(case(e,direct=m==3))
    # Contracted zero-pair controls use relevant coordinates only.
    for e in (Q(1,16),Q(1,1024)):
        table=[1 if a.bit_count()>=2 else -1 for a in range(8)]
        c,P=transform(table,[Q(1,2),Q(1,2),e]); ck(c[1]==c[2]==c[4]==Q(1,2))
        ck(P[3]>0); ck(all(lnbox(2*c[a])==(Q(0),Q(0)) for a in (1,2,4)))
    data={'status':'PASS','cases':len(rows),'assertions':checks,'seconds':time.perf_counter()-START,
          'arithmetic':'Fraction and outward 40-term atanh with geometric tail','rows':rows}
    out=ROOT/'out'/('PILOT.json' if args.pilot else 'CHECKS.json')
    out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in data.items() if k!='rows'}))
if __name__=='__main__': main()
