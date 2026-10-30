from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();asserts=0
PILOT='--pilot' in sys.argv;CAP=55 if PILOT else 300
def ck(b):
    global asserts
    assert b;asserts+=1
    if time.perf_counter()-start>CAP:raise RuntimeError('frozen watchdog')
def add(*es):
    d={}
    for e in es:
        for p,v in e.items():d[p]=d.get(p,Q(0))+v
    return {p:v for p,v in d.items() if v}
def mul(e,c):return {p:v*c for p,v in e.items() if v*c}
@lru_cache(None)
def factors(n):
    d={};i=2
    while i*i<=n:
        while n%i==0:d[i]=d.get(i,0)+1;n//=i
        i+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def ent(ps):
    d={}
    for x in ps:
        if not x:continue
        for s,n in ((-1,x.numerator),(1,x.denominator)):
            for p,k in factors(n).items():d[p]=d.get(p,Q(0))+s*x*k
    return {p:v for p,v in d.items() if v}
def hb(x):return ent((x,1-x))
@lru_cache(None)
def lnunit(x):
    z=(x-1)/(x+1);a=z;s=Q(0)
    for j in range(30):s+=2*a/(2*j+1);a*=z*z
    return s,s+2*a/(61*(1-z*z))
L2=lnunit(Q(2))
@lru_cache(None)
def lnprime(p):
    x=Q(p);k=0
    while x>=2:x/=2;k+=1
    a,b=lnunit(x);return a+k*L2[0],b+k*L2[1]
def natural_bounds(e):
    lo=hi=Q(0)
    for p,c in e.items():
        a,b=lnprime(p)
        if c<0:a,b=b,a
        lo+=c*a;hi+=c*b
    return lo,hi
def positive(e):ck(not e or natural_bounds(e)[0]>=0)
def cert(e):
    a,b=natural_bounds(e);corners=[x/y for x in (a,b) for y in L2];a,b=min(corners),max(corners)
    Z=1<<100;lo=Q((a*Z).numerator//(a*Z).denominator,Z);hi=Q(-((-b*Z).numerator//(-b*Z).denominator),Z)
    ck(lo<=a<=b<=hi);return {'lower':str(lo),'upper':str(hi),'display':[float(lo),float(hi)]}
def expr(e):return {str(p):str(c) for p,c in sorted(e.items())}
@lru_cache(None)
def split(t,i,b):
    n=len(t).bit_length()-1
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1)))
@lru_cache(None)
def weights(ps):
    ws=[]
    for x in range(1<<len(ps)):
        w=Q(1)
        for i,p in enumerate(ps):w*=p if x>>i&1 else 1-p
        ws.append(w)
    return tuple(ws)
@lru_cache(None)
def stats(t,ps):
    n=len(ps);N=len(t);a=list(map(Q,t))
    for i,p in enumerate(ps):
        bit=1<<i
        for x in range(N):
            if not x&bit:
                u,v=a[x],a[x|bit];a[x],a[x|bit]=(1-p)*u+p*v,v-u
    masses=[]
    for s,u in enumerate(a):
        norm=Q(1)
        for i,p in enumerate(ps):
            if s>>i&1:norm*=p*(1-p)
        masses.append(u*u*norm)
    ck(sum(masses)==1)
    ws=weights(ps);neg=sum((w for w,v in zip(ws,t) if v==-1),Q(0))
    ds=[]
    for i in range(n):
        g,h=split(t,i,0),split(t,i,1);rp=ps[:i]+ps[i+1:]
        ds.append(sum((w for w,u,v in zip(weights(rp),g,h) if u!=v),Q(0)))
    ck(all(v in (-1,1) for v in t))
    if all(p==Q(1,2) for p in ps):
        direct=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(N)]
        ck(masses==[Q(v*v,N*N) for v in direct])
        for i,d in enumerate(ds):ck(sum(m for s,m in enumerate(masses) if s>>i&1)==d)
    return tuple(masses),neg,tuple(ds)
def localmask(root,ids):return sum(((root>>g)&1)<<i for i,g in enumerate(ids))
def removebit(x,i):return (x&((1<<i)-1))|((x>>(i+1))<<i)
def run_tree(t,ps,policy):
    n=len(ps);P,neg,ds=stats(t,ps);state={s:w for s,w in enumerate(P) if w}
    sums={'M':{},'J':{},'o':{},'leafF':{},'leafOut':{},'Dbar':{}};removed=Q(0);leafI=Q(0);leaves=[]
    def walk(t,ps,ids,state,path):
        nonlocal removed,leafI
        P,neg,ds=stats(t,ps);reach=sum(state.values());ck(reach>0)
        marg=defaultdict(Q)
        for s,w in state.items():marg[localmask(s,ids)]+=w
        ck(all(marg[x]==reach*w for x,w in enumerate(P)))
        active=[i for i,d in enumerate(ds) if d]
        stop=not active or (policy=='partial' and len(path)>=1) or (policy=='controls' and not any(i<3 for i in ids))
        if stop:
            leaves.append((path,reach,neg,state))
            sums['leafF']=add(sums['leafF'],mul(ent(P),reach));sums['leafOut']=add(sums['leafOut'],mul(hb(neg),reach));leafI+=reach*sum(ds)
            return
        if policy=='controls':i=next(j for j,g in enumerate(ids) if g<3)
        else:i=active[-1] if policy=='reverse' else active[0]
        p=ps[i];rp=ps[:i]+ps[i+1:];rt=[split(t,i,b) for b in (0,1)];children=[stats(v,rp) for v in rt]
        q=[Q(0)]*(len(P)//2)
        for s,w in enumerate(P):q[removebit(s,i)]+=w
        ck(all(q[s]==(1-p)*children[0][0][s]+p*children[1][0][s] for s in range(len(q))))
        M=add(ent(P),mul(ent(q),-1));J=add(ent(q),mul(ent(children[0][0]),-(1-p)),mul(ent(children[1][0]),-p))
        o=add(hb(neg),mul(hb(children[0][1]),-(1-p)),mul(hb(children[1][1]),-p))
        Dbar=add(mul(hb(p),Q(1,2)),M,mul(J,-1))
        for key,e in (('M',M),('J',J),('o',o),('Dbar',Dbar)):sums[key]=add(sums[key],mul(e,reach))
        removed+=reach*ds[i]
        newids=ids[:i]+ids[i+1:]
        for b,prob in ((0,1-p),(1,p)):
            childstate={}
            for root,w in state.items():
                s=localmask(root,newids);ck(q[s]>0);v=w*prob*children[b][0][s]/q[s]
                if v:childstate[root]=v
            ck(sum(childstate.values())==reach*prob)
            walk(rt[b],rp,newids,childstate,path+((ids[i],b),))
    walk(t,ps,tuple(range(n)),state,())
    ck(sum(w for _,w,_,_ in leaves)==1)
    ck(sum(ds)==removed+leafI)
    HP=ent([w for _,w,_,_ in leaves]);HS=ent(P);HY=hb(neg)
    outjoint=[w*v for _,w,q,_ in leaves for v in (q,1-q)]
    outbank=add(ent(outjoint),mul(HY,-1));o=add(HP,mul(outbank,-1));ck(o==sums['o'])
    ck(add(sums['M'],sums['J'],sums['leafF'])==HS)
    positive(add({2:removed},mul(o,-1)))
    J=sums['J'];nb=natural_bounds(J);ck(nb[1]<=4*removed if removed else not J)
    if all(p==Q(1,2) for p in ps):ck(nb[1]<=2*removed if removed else not J)
    witnesses={}
    for label in ('root_spectrum','parity_empty','stochastic_empty'):
        joint=defaultdict(Q);zdist=defaultdict(Q)
        for l,(_,w,_,rootstate) in enumerate(leaves):
            for s,v in rootstate.items():
                if label=='root_spectrum':choices=[(s,Q(1))]
                elif label=='parity_empty':choices=[((s.bit_count()%2,s==0),Q(1))]
                else:
                    beta=Q(1+s.bit_count(),n+2);choices=[((0,s==0),1-beta),((1,s==0),beta)]
                for z,k in choices:joint[z,l]+=v*k;zdist[z]+=v*k
        bank=add(ent(joint.values()),mul(ent(zdist.values()),-1));j=add(HP,mul(bank,-1));gamma=add(outbank,mul(bank,-1))
        ck(gamma==add(j,mul(o,-1)))
        positive(add(J,mul(j,-1)))
        # Exact compatibility ledger, output terms converted together.
        ck(add(sums['leafF'],mul(sums['M'],2),mul(bank,Q(1,2)),mul(j,Q(1,2)),mul(sums['Dbar'],-1))==HS)
        if label=='root_spectrum':ck(j==J)
        witnesses[label]={'information':j,'conversion':gamma}
    return removed,witnesses,len(leaves)

def main():
    out={'roots':0,'trees':0,'overlap_trees':0,'closed_chains':[],'assertions':0,'witness_variants_per_tree':3};signs={'positive':0,'negative':0,'zero':0};largest=None
    laws=[(Q(1,2),)*3,(Q(1,8),)*3,(Q(1,8),Q(1,4),Q(3,8)),(Q(3,4),Q(7,8),Q(1,2))]
    for n in range(3 if PILOT else 4):
        for ps0 in laws:
            ps=ps0[:n]
            for m in range(1<<(1<<n)):
                t=tuple(1-2*((m>>x)&1) for x in range(1<<n));out['roots']+=1
                for policy in ('forward','reverse','partial'):
                    removed,ws,leaves=run_tree(t,ps,policy);out['trees']+=1
                    gamma=ws['root_spectrum']['conversion'];lo,hi=natural_bounds(gamma)
                    if not gamma:signs['zero']+=1
                    elif lo>0:signs['positive']+=1
                    elif hi<0:signs['negative']+=1
                    else:raise AssertionError('unresolved conversion sign')
        out['assertions']=asserts;(R/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf8')
    if not PILOT:
        for g in range(16):
            for h in range(16):
                t=[]
                for x in range(32):
                    z,a,b=(x>>i&1 for i in range(3));y=x>>3
                    hit=(z and a and ((g>>y)&1)) or (z and b and ((h>>y)&1))
                    t.append(1-2*bool(hit))
                for policy in ('forward','controls'):
                    run_tree(tuple(t),(Q(1,2),)*5,policy);out['trees']+=1;out['overlap_trees']+=1
        for r in range(1,17):
            delta=Q(1,1<<r);I=2*r*delta;J={}
            for s in range(r):
                eps=Q(1,1<<s);v=4*eps*(1-eps);js=add(hb(v/2),mul(hb(v),Q(-1,2)))
                J=add(J,mul(js,Q(1,1<<(r-s-1))))
            gamma=add(J,mul(hb(delta),-1));excess=add(gamma,{2:-I})
            row={'r':r,'I':str(I),'J':expr(J),'Gamma':expr(gamma),'Gamma_over_2I':cert(mul(gamma,Q(1,2)/I)), 'excess_Gamma_minus_I':cert(excess)}
            if Q(row['excess_Gamma_minus_I']['lower'])>0 and largest is None:largest=row
            out['closed_chains'].append(row)
        ck(largest is not None);out['half_I_conversion_counterexample']=largest
    out['root_conversion_signs']=signs;out['assertions']=asserts;out['runtime_seconds']=time.perf_counter()-start;out['status']='PASS'
    (R/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf8')
    print(json.dumps({'status':'PASS','trees':out['trees'],'closed_chains':len(out['closed_chains']),'assertions':asserts,'runtime':out['runtime_seconds'],'conversion_signs':signs,'first_half_I_counterexample_r':largest['r'] if largest else None},indent=2))
if __name__=='__main__':main()
