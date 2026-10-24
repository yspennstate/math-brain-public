import exact as e
from exact import Q,add,entropy,logform,check,nonnegative,interval
from functools import lru_cache
from pathlib import Path
import json,time,sys,itertools
R=Path(__file__).resolve().parents[1]; START=time.perf_counter()
def dim(t):return (len(t)-1).bit_length()
def eta(x):return add((-x,logform(x))) if x else {}
def phi(a,b):return add((1,eta(a)),(1,eta(b)),(-1,eta(a+b)))
@lru_cache(maxsize=4096)
def coeff(t):
    a=list(t);h=1
    while h<len(a):
        for start in range(0,len(a),2*h):
            for j in range(start,start+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return tuple(Q(v,len(a)) for v in a)
@lru_cache(maxsize=4096)
def spec(t):
    a=coeff(t);P=tuple(x*x for x in a);check(sum(P),Q(1));return a,P
def mean(t):return Q(sum(t),len(t))
def inf(t):return e.inf(spec(t)[1])
def table(c,us):
    nc=dim(c);sz=[dim(u) for u in us];out=[]
    for x in range(1<<(nc+sum(sz))):
        j=c[x%len(c)]
        if j==0:out.append(1)
        else:out.append(us[j-1][(x>>(nc+sum(sz[:j-1])))%len(us[j-1])])
    return tuple(out)
def pots(c,us):
    qs=[Q(c.count(j),len(c)) for j in range(1,len(us)+1)]
    U=add(*[(q,add((1,entropy(spec(u)[1])),(-1,eta(mean(u)**2)))) for q,u in zip(qs,us)])
    RR=add(*[(1-mean(u)**2,eta(q)) for q,u in zip(qs,us)])
    return qs,U,RR
def restrict(c,us,ids,kind,i,b):
    if kind=='c':
        pos=ids.index(i);cc=e.restrict(c,[pos],b)[0];return cc,us,tuple(x for x in ids if x!=i)
    uu=list(us);uu[i]=e.restrict(uu[i],[0],b)[0];return c,tuple(uu),ids
def bounded(form,rate,d):
    if not form and not d:check(form,{});return
    lo,hi=interval(form);assert hi<=rate[0]*d,(form,d,hi,rate);e.COUNT+=1
CI=e.mesh((Q(1)/e.LN2[1],Q(1)/e.LN2[0]))
RATE=e.plus((Q(8),Q(8)),e.scale(2,CI));A087RATE=e.plus((Q(4),Q(4)),e.scale(2,CI))
STATS={'roots':0,'trees':0,'nodes':0,'override_nodes':0,'source_shared_nodes':0,'resolved_leaves':0,'data_nodes':0}
def local(c,us,ids,kind,i):
    F=table(c,us);P=spec(F)[1];qs,U,RR=pots(c,us)
    ch=[restrict(c,us,ids,kind,i,b) for b in (0,1)]
    fp=[spec(table(v[0],v[1]))[1] for v in ch];pp=[pots(v[0],v[1]) for v in ch]
    D=add((1,entropy(P)),*[(-Q(1,2),entropy(v)) for v in fp])
    dr=add((1,RR),*[(-Q(1,2),v[2]) for v in pp]);du=add((1,U),*[(-Q(1,2),v[1]) for v in pp])
    ix=ids.index(i) if kind=='c' else len(ids)+sum(dim(v) for v in us[:i])
    d=sum(v for s,v in enumerate(P) if s>>ix&1)
    check(e.inf(P),d+sum(e.inf(v) for v in fp)/2)
    STATS['nodes']+=1
    if kind=='d':
        beta=coeff(us[i])[1];T=qs[i]*beta*beta
        check(dr,add((beta*beta,eta(qs[i]))));bounded(add((1,D),(-1,du),(-1,dr)),e.scale(3,CI),T)
        STATS['data_nodes']+=1;return ch,D,dr,d,T
    check(du,{});nonnegative(dr)
    folded=[Q(0)]*(len(P)//2)
    for s,v in enumerate(P):folded[e.compressed(s,[k for k in range(dim(F)) if k!=ix])]+=v
    B=add((1,entropy(P)),(-1,entropy(tuple(folded))));J=add((1,D),(-1,B))
    nonnegative(J);bounded(J,e.scale(2,CI),d)
    res=add((1,D),(-1,dr))
    if i==0:
        STATS['source_shared_nodes']+=1;mu0=mean(table(ch[0][0],us));mu1=mean(table(ch[1][0],us))
        g0=tuple(Q(1) if j==0 else mean(us[j-1]) for j in ch[0][0]);g1=tuple(Q(1) if j==0 else mean(us[j-1]) for j in ch[1][0])
        if len(set(table(ch[0][0],us)))==1 or len(set(table(ch[1][0],us)))==1:
            # One-sided source geometry: all nonconstant selectors are confined to one X branch.
            k=0 if len(set(table(ch[1][0],us)))==1 else 1
            live=[g0,g1][k];m=mean(live);z=(1-m)/2
            ex=add(((sum(v*v for v in live)/len(live)-m*m)/2,logform(Q(2))),(1,phi((1-z)**2,z*z)))
            check(add((1,B),(-1,dr)),ex)
        else:
            check(d,(1-mu0*mu1)/2)
            vv=[sum(x*x for x in g)/len(g)-mean(g)**2 for g in (g0,g1)]
            ex=add(((vv[0]+vv[1])/2,logform(Q(2))),(1,phi(((mu0+mu1)/2)**2,((mu0-mu1)/2)**2)))
            check(add((1,B),(-1,dr)),ex)
        nonnegative(res);bounded(res,A087RATE,d)
    # A priority query after the common X has been fixed in same orientation.
    if i in (1,2) and pp[1][0][0]==0 and pp[0][0][0]>0:
        q=qs[0];p=2*q;mu=mean(us[0]);W=table(ch[1][0],us);nu=mean(W);V=1-nu*nu;delta=mu-nu
        Z=sum(pp[1][0][j]*(1-mean(us[j])**2) for j in range(len(us)))
        K=add((1,eta(1-q)),(-Q(1,2),eta(1-p)))
        L=add((p*(1-p)/2,logform(Q(2))),(1,phi((1-q)**2,q*q)))
        check(d,p*(1-mu*nu)/2);check(dr,add((q*(1-mu*mu),logform(Q(2))),(Z,K)))
        ex=add((1,phi((nu+q*delta)**2,(q*delta)**2)),(p*(1-p)*delta*delta/2,logform(Q(2))),(V,L),(-Z,K))
        check(add((1,B),(-1,dr)),ex)
        nonnegative(K);bounded(add((1,B),(-1,dr)),(8-4*p,8-4*p),d)
        STATS['override_nodes']+=1
    bounded(res,RATE,d)
    return ch,D,dr,d,Q(0)
def leaf(c,us):
    P=spec(table(c,us))[1];qs,U,RR=pots(c,us);S=add((1,entropy(P)),(-1,U),(-1,RR))
    assert len(set(c))==1
    m=mean(table(c,us));check(S,eta(m*m));bounded(S,CI,e.inf(P));STATS['resolved_leaves']+=1
    return {'H':entropy(P),'U':U,'R':RR,'I':e.inf(P),'pic':Q(0),'pid':Q(0),'T':Q(0),'ctrl':{},'kap':{}}
def tree(c,us,ids,ops,k=0):
    if len(set(c))==1:return leaf(c,us)
    while k<len(ops):
        kind,i=ops[k]
        if kind=='c' and i not in ids:k+=1;continue
        if kind=='d' and dim(us[i])==0:k+=1;continue
        break
    assert k<len(ops)
    kind,i=ops[k];ch,D,dr,d,T=local(c,us,ids,kind,i)
    vv=[tree(*v,ops,k+1) for v in ch];z={}
    for field in ['H','U','R','ctrl','kap']:z[field]=add(*[(Q(1,2),v[field]) for v in vv])
    for field in ['I','pic','pid','T']:z[field]=sum(v[field] for v in vv)/2
    if kind=='c':z['ctrl']=add((1,z['ctrl']),(1,D),(-1,dr));z['kap']=add((1,z['kap']),(1,dr));z['pic']+=d
    else:z['pid']+=d;z['T']+=T
    qs,U,RR=pots(c,us);P=spec(table(c,us))[1]
    check(e.inf(P),z['I']+z['pic']+z['pid']);bounded(z['ctrl'],RATE,z['pic'])
    debt=add((1,entropy(P)),(-1,z['H']),(-1,U),(1,z['U']),(-1,RR),(1,z['R']),(-1,z['ctrl']))
    bounded(debt,e.scale(3,CI),z['T'])
    return z
def controller(r,s,opposite):
    nc=1+r+s;out=[]
    for x in range(1<<nc):
        X=x&1;A=((x>>1)% (1<<r))==0;B=(x>>(1+r))==0
        out.append(1 if X==0 and A else (2 if X==int(opposite) and B else 0))
    return tuple(out)
def main():
    pilot='--pilot' in sys.argv;lo=int(sys.argv[sys.argv.index('--start')+1]) if '--start' in sys.argv else 0
    hi=int(sys.argv[sys.argv.index('--end')+1]) if '--end' in sys.argv else (2 if pilot else 22)
    cores=[e.tab(m,n) for n in (0,1,2) for m in range(1<<(1<<n))]
    if pilot:cores=cores[:6]
    opss=[[('c',0),('c',1),('c',2),('c',3)], [('c',0),('c',1),('d',0),('c',2),('c',3)], [('c',0),('c',1),('d',1),('c',2),('c',3)], [('c',0),('d',1),('c',1),('d',0),('c',2),('c',3)]]
    for ix in range(lo,hi):
        for v in cores:
            for opposite in (0,1):
                us=(cores[ix],v);c=controller(2,1,opposite);STATS['roots']+=1
                for ops in opss:tree(c,us,(0,1,2,3),ops);STATS['trees']+=1
        coeff.cache_clear();spec.cache_clear()
        if time.perf_counter()-START>(55 if pilot else 180):raise RuntimeError('frozen watchdog')
    out={'status':'PASS','pilot':pilot,'slice':[lo,hi],'stats':STATS,'exact_assertions':e.COUNT,'runtime_seconds':time.perf_counter()-START,'arithmetic':'integer FWHT; Fraction spectra/edges/selector probabilities; exact prime-log identities; rational 40-term atanh sign intervals','control_rate_interval':[str(x) for x in RATE]}
    (R/'out'/('PILOT.json' if pilot else f'CHECK_{lo}_{hi}.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
