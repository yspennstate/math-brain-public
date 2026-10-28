import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time,math
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R.parent/'20261014T094139Z-account05-A091-composition-referee'/'code'))
import check as a
import exact as e
start=time.perf_counter()
def exterior():
    out=[]
    for mask in range(16):
        C=tuple((mask>>z)&1 for z in range(4))
        if sum(C)<2:continue
        holes=[z for z in range(4) if not C[z]]
        for signs in range(1<<len(holes)):
            K=[0]*4
            for j,z in enumerate(holes):K[z]=1 if signs>>j&1 else -1
            out.append((C,tuple(K)))
    assert len(out)==33
    return out
def priority(widths):
    labels=[]
    for z in range(1<<sum(widths)):
        off=0;sel=len(widths)
        for j,w in enumerate(widths):
            if (z>>off)&((1<<w)-1)==((1<<w)-1):sel=j;break
            off+=w
        labels.append(sel)
    return tuple(labels)
def case(C,K,us,widths):
    c=Q(sum(C),4);cc=a.coeff(C);kc=a.coeff(K)
    rho=sum(k*k for k,t in zip(kc,cc) if t)/c
    assert rho<=Q(1,1)/c-1
    core=us+((1,),(-1,));gl=priority(widths);labels=[]
    for x in range(1<<(2+sum(widths))):
        z=x&3;labels.append(gl[x>>2] if C[z] else len(us)+(K[z]<0))
    labels=tuple(labels);F=a.compose(labels,core)
    means=[Q(sum(u),len(u)) for u in us]
    queries=0
    for j,wid in enumerate(widths):
        i=2+sum(widths[:j]);q=Q(1,1<<wid);m=means[j]
        pl=priority(widths[:j]);E=tuple(int(k==j) for k in pl)
        Kp=tuple(Q(0) if k==j else means[k] for k in pl)
        ec=a.coeff(E);pc=a.coeff(Kp);guard=Q(sum(E),len(E))
        sl=priority(widths[j+1:]);sc=us[j+1:]+((1,),)
        v=a.compose(sl,sc);n=Q(sum(v),len(v));V=1-n*n;delta=m-n;M=n+q*delta;x=q*abs(delta)
        Z=sum(Q(sl.count(k),len(sl))*(1-Q(sum(u),len(u))**2) for k,u in enumerate(sc))
        kq=e.add((1,a.eta(1-q)),(-Q(1,2),a.eta(1-2*q)))
        kexpected=e.add((1,a.const(c*guard*q*(1-m*m))),(c*guard*Z,kq))
        kids=[a.cut(labels,i,b) for b in (0,1)]
        kap=e.add((1,a.reserve(labels,core)),*[(-Q(1,2),a.reserve(t,core)) for t in kids])
        e.check(kap,kexpected)
        B,D,d=a.local(F,i);e.check(d,c*guard*q*(1-m*n))
        S=e.add(*[(1,a.phi((kk*(T==0)+ct*(kp+M*et))**2,x*x*ct*ct*et*et)) for kk,ct in zip(kc,cc) for T,(kp,et) in enumerate(zip(pc,ec))])
        rhs=e.add((1,a.const(c*guard*(q-2*q*q)*(V+delta*delta))),(c*guard*V,a.phi((1-q)**2,q*q)),(-c*guard*Z,kq),(1,S))
        e.check(e.add((1,B),(-1,kap)),rhs)
        a.pos(e.add((1,a.const(21*d)),(-1,D),(1,kap)))
        # Independently identify the last nonempty earlier block on every row.
        moment={}
        for T,(et,kp) in enumerate(zip(ec,pc)):
            if not et:continue
            off=0;last=-1
            for h,ww in enumerate(widths[:j]):
                if (T>>off)&((1<<ww)-1):last=h
                off+=ww
            tail=e.prod(1-Q(1,1<<ww) for ww in widths[last+1:j])
            assert abs(kp/et+M)<=3/tail
            moment=e.add((1,moment),(et*et/guard,e.logform(1/tail)))
        if moment:
            iv=e.interval(moment)
            assert iv[1]*e.LN2[1]<=1-guard
        queries+=1
    return queries
def main():
    lo,hi=map(int,sys.argv[1:3]);pilot='--pilot' in sys.argv
    roots=queries=0;pool=tuple(e.tab(k,1) for k in range(4))
    for idx,(C,K) in enumerate(exterior()):
        if not lo<=idx<hi:continue
        pairs=list(itertools.product(pool,repeat=2))[:2] if pilot else itertools.product(pool,repeat=2)
        for us in pairs:
            queries+=case(C,K,us,(1,1));roots+=1
        if not pilot:
            and2=(-1,-1,-1,1)
            triples=[((-1,1),(1,-1),and2),((1,),and2,(-1,1)),(and2,tuple(-x for x in and2),(1,)),((-1,),(-1,1),(-1,))]
            for us,widths in itertools.product(triples,((1,1,1),(2,1,1),(1,2,1))):
                queries+=case(C,K,us,widths);roots+=1
        if time.perf_counter()-start>55:raise RuntimeError('frozen watchdog')
    e.check(sum(Q(25,6)**k/math.factorial(k) for k in range(13))>57,True)
    e.check(6+Q(61,6)*Q(81,56)<21,True)
    out={'status':'PASS','range':[lo,hi],'pilot':pilot,'roots':roots,'queries':queries,'exact_assertions':e.COUNT,'seconds':time.perf_counter()-start,'scope':'A059 exact full wrapper row, original fine reserve, rate21, exterior normalization, last-nonempty moment and constant bound'}
    (R/'out'/f'WRAPPER_{lo}_{hi}{"_PILOT" if pilot else ""}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
