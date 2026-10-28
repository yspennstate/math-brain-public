from pathlib import Path
from fractions import Fraction as F
import json, time, sys
from functools import lru_cache

RUN=Path(__file__).resolve().parents[1]
NCHK=0
def ck(b):
    global NCHK
    assert b
    NCHK+=1
def dump(name,v):
    p=RUN/'out'/name;p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(v,indent=2),encoding='utf-8')
@lru_cache(maxsize=10000)
def log2(x):
    x=F(x);e=0
    while x>=2:x/=2;e+=1
    while x<1:x*=2;e-=1
    def ln(z):
        t=(z-1)/(z+1);s=sum((t**(2*j+1)/F(2*j+1) for j in range(28)),F(0))*2
        return s,s+2*t**57/(57*(1-t*t))
    lo,hi=ln(x);a,b=ln(F(2))
    return F(e)+lo/b,F(e)+hi/a
def ce(P,Q):
    lo=hi=F(0)
    for p,q in zip(P,Q):
        if p:
            ck(q>0);a,b=log2(1/q);lo+=p*a;hi+=p*b
    return lo,hi
def walsh(v):
    a=list(map(F,v));h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h):a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
        h*=2
    return [x/len(a) for x in a]
def influence(v):
    d=len(v).bit_length()-1
    return sum((F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(d)),F(0))
def child(v,i,b):
    return [v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2)]
def transport(v,Q,i):
    a=walsh(v);P=[x*x for x in a];vs=[child(v,i,b) for b in (0,1)]
    Ps=[[x*x for x in walsh(vb)] for vb in vs]
    def lift(t,b):return (t&((1<<i)-1))|((t>>i)<<(i+1))|(b<<i)
    r=[Q[lift(t,0)]+Q[lift(t,1)] for t in range(len(Q)//2)]
    raw=[[],[]]
    for t in range(len(r)):
        q=(Ps[0][t]+Ps[1][t])/2
        ck(q==P[lift(t,0)]+P[lift(t,1)])
        for b in (0,1):raw[b].append(r[t]*Ps[b][t]/q if q else r[t])
    Z=[sum(z) for z in raw];ck(sum(Z)==2);ck(min(Z)>0)
    Qs=[[x/Z[b] for x in raw[b]] for b in (0,1)]
    for b in (0,1):ck(sum(Qs[b])==1)
    return vs,Qs
def root(w,m):
    k=w+2;n=k+m;delta=F(1,2**n)
    g=[(-1 if (x&((1<<w)-1))==0 else 1)*(-1 if x>>w==0 else 1) for x in range(2**k)]
    aa=walsh(g);R=[a*a for a in aa]
    v=[g[x&((1<<k)-1)]*(-1 if (x>>n)&1 and (x&((1<<n)-1))==0 else 1) for x in range(2**(n+1))]
    ww=2*delta-2**k*delta*delta
    Q=[(1-ww)*R[s] if s<2**k else delta*delta for s in range(len(v))]
    ck(sum(Q)==1);ck(all(q>0 for q in Q))
    return g,aa,R,v,Q,delta
def history(v,Q,labels,w,mode):
    candidates=[(i,j) for i,j in enumerate(labels) if j<w]
    if not candidates:return [(F(1),v,Q,labels)]
    if mode=='one' and len(candidates)<w:return [(F(1),v,Q,labels)]
    # Different adaptive orders, and a branch-stopping policy.
    i,j=candidates[-1] if mode=='reverse' else candidates[sum(v)<0 and len(candidates)>1]
    vs,Qs=transport(v,Q,i);ll=labels[:i]+labels[i+1:];out=[]
    for b in (0,1):
        leaves=[(F(1),vs[b],Qs[b],ll)] if mode=='zero-path' and b==1 else history(vs[b],Qs[b],ll,w,mode)
        out.extend((p/2,z,q,l) for p,z,q,l in leaves)
    return out
def main():
    start=time.perf_counter();pilot='pilot' in sys.argv
    cases=[(3,0),(4,0)] if pilot else [(w,m) for w in (3,4,5) for m in (0,1,2)]
    records=[]
    for w,m in cases:
        g,aa,R,v,Q,d=root(w,m);av=walsh(v);P=[a*a for a in av];lo,hi=ce(P,Q)
        for s,a in enumerate(av):ck(a==aa[s]-d if s<len(aa) else abs(a)==d)
        # Independent direct character sums at the boundary core.
        if w==4 and m==0:
            for s,a in enumerate(aa):ck(a==F(sum(z*(-1 if (s&x).bit_count()%2 else 1) for x,z in enumerate(g)),len(g)))
        q=F(2,2**w);L=log2(1-q)
        A=sum((a*log2(1/r)[0] for a,r in zip(aa,R)),F(0))
        # Profile checked as formal coefficients of log2(1-q), not rounded signs.
        profileA=2+F(2)*(1-q)*L[0]+(2-q)*(2*w-2)
        ck(abs(A-profileA)<F(1,2**65))
        if w>=4:
            ck(hi<F(1005,256));ck(influence(v)>=F(63,64))
        modes=['one','zero-path'] if w==3 else ['one','zero-path','reverse','adaptive']
        for mode in modes:
            # The accepted width3 theorem stops before its third query.
            if w==3:
                vs,Qs=transport(v,Q,0)
                leaves=[(F(1,2),vs[1],Qs[1],list(range(len(v).bit_length()-2)))]
                if mode=='one':leaves.append((F(1,2),vs[0],Qs[0],[]))
                else:
                    v2,q2=transport(vs[0],Qs[0],0)
                    leaves.extend((F(1,4),z,q,[]) for z,q in zip(v2,q2))
            else:leaves=history(v,Q,list(range(w+3+m)),w,mode)
            infl=sum((p*influence(z) for p,z,qq,l in leaves),F(0))
            clo=chi=F(0)
            for p,z,qq,l in leaves:
                pz=[a*a for a in walsh(z)];a,b=ce(pz,qq);clo+=p*a;chi+=p*b
                ck(any(a!=0 for a in walsh(z)[1:]))
            ck(chi<=lo);ck(4*infl-chi>=(F(3,256) if w>=4 else F(3,64)))
            if w>=4:
                ck(infl>=1-d)
                original_remaining=F(0);edited=[]
                for p,z,qq,l in leaves:
                    last=len(z).bit_length()-2
                    gz=child(z,last,0)
                    original_remaining+=p*influence(gz)
                    if child(z,last,1)!=gz:edited.append((p,w-sum(j<w for j in l)))
                ck(len(edited)==1)
                reach,t=edited[0];ck(reach==F(1,2**t))
                ck(infl==original_remaining+d*(m-w-1+t))
                ck(original_remaining-1>=(w-t)*q)
            records.append({'w':w,'m':m,'mode':mode,'leaves':len(leaves),'remaining_I':str(infl),'surplus_lower_gt':str(F(3,256) if w>=4 else F(3,64))})
    # Rational boundary and recurrence checks, not a finite-to-infinite proof.
    for w in range(4,65):
        q=F(2,2**w);ck((4*w+2)*q<=F(9,4));ck((4*(w+1)+2)*q/2<=(4*w+2)*q)
        ck(F(4*w-1)*q<=F(19,16) if w>=5 else True)
        for m in range(65):ck(16*m+37<=37*2**m)
    dump('PILOT.json' if pilot else 'EXACT_RESULTS.json',{'status':'PASS','assertions':NCHK,'histories':len(records),'records':records,'runtime_s':time.perf_counter()-start,'rung':'exact finite certificates; infinite extension analytic'})
    print(json.dumps({'status':'PASS','assertions':NCHK,'histories':len(records),'runtime_s':time.perf_counter()-start}))
if __name__=='__main__':main()
