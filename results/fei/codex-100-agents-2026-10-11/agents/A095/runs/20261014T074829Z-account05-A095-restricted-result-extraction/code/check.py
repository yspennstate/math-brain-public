from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import sys,json,time

RUN=Path(__file__).resolve().parents[1];START=time.monotonic();CHECKS=0
def saved_interval(lo,hi):
    grid=1<<80
    a=(lo.numerator*grid)//lo.denominator
    b=-((-hi.numerator*grid)//hi.denominator)
    return [str(F(a,grid)),str(F(b,grid))]
def check(ok):
    global CHECKS
    CHECKS+=1
    if CHECKS%128==0 and time.monotonic()-START>55:raise TimeoutError('55-second guard')
    if not ok:raise AssertionError(CHECKS)
@lru_cache(None)
def ln(x):
    if x==1:return F(0),F(0)
    if x<1:
        a,b=ln(1/x);return -b,-a
    k=0
    while x>2:x/=2;k+=1
    y=(x-1)/(x+1)
    v=sum((2*y**(2*j+1)/F(2*j+1) for j in range(24)),F(0));err=2*y**49/(49*(1-y*y))
    if k:
        a,b=ln(F(2));return v+k*a,v+err+k*b
    return v,v+err
LN2=ln(F(2))
@lru_cache(None)
def log(x):
    if x.numerator&(x.numerator-1)==0 and x.denominator&(x.denominator-1)==0:
        v=F(x.numerator.bit_length()-x.denominator.bit_length());return v,v
    if x<1:
        a,b=log(1/x);return -b,-a
    a,b=ln(x);return a/LN2[1],b/LN2[0]
def ce(p,q):
    grouped={}
    for x,r in zip(p,q):
        if x:grouped[r]=grouped.get(r,F(0))+x
    lo=hi=F(0)
    for r,x in grouped.items():
        a,b=log(r);lo-=x*b;hi-=x*a
    return lo,hi
def fwht(v):
    v=v[:];d=1
    while d<len(v):
        for a in range(0,len(v),2*d):
            for j in range(a,a+d):
                x,y=v[j],v[j+d];v[j]=x+y;v[j+d]=x-y
        d*=2
    return [F(x,len(v)) for x in v]
def spectrum(v):return [x*x for x in fwht(v)]
def influence(v):
    d=(len(v)-1).bit_length()
    return F(sum(v[j]!=v[j^(1<<i)] for i in range(d) for j in range(len(v))),len(v))
def directional(v,i):return F(sum(v[j]!=v[j^(1<<i)] for j in range(len(v))),len(v))
def split(v,i):
    N=len(v)//2
    return [[v[(j&((1<<i)-1))|((j>>i)<<(i+1))|(b<<i)] for j in range(N)] for b in (0,1)]
def marginal(q,i):
    return [q[(j&((1<<i)-1))|((j>>i)<<(i+1))]+q[(j&((1<<i)-1))|((j>>i)<<(i+1))|(1<<i)] for j in range(len(q)//2)]

TRANSPORTS=0;NORMALIZERS_NONUNIT=0
def transfer(v,Q,i):
    global TRANSPORTS,NORMALIZERS_NONUNIT
    TRANSPORTS+=1
    children=split(v,i);p=[spectrum(x) for x in children]
    m=[(a+b)/2 for a,b in zip(*p)];r=marginal(Q,i)
    rootp=spectrum(v);check(marginal(rootp,i)==m)
    raws=[[r[j]*p[b][j]/m[j] if m[j] else r[j] for j in range(len(r))] for b in (0,1)]
    Z=[sum(x) for x in raws];check(sum(Z)==2 and all(z>0 for z in Z))
    refs=[[x/Z[b] for x in raws[b]] for b in (0,1)]
    for b in (0,1):
        if Z[b]!=1:NORMALIZERS_NONUNIT+=1
        check(sum(refs[b])==1 and all(not x or refs[b][j]>0 for j,x in enumerate(p[b])))
        for j,x in enumerate(p[b]):
            if x:check(x/refs[b][j]==m[j]*Z[b]/r[j])
    cc=[ce(p[b],refs[b]) for b in (0,1)];croot=ce(rootp,Q)
    check((cc[0][0]+cc[1][0])/2<=croot[1])
    # Exact conditional KL and normalizers are preserved by the atom likelihood above.
    return children,refs,Z

HISTORIES=ADMITTED=NONCONSTANT_BOTH=0;CERTS=[]
def history(g,k,m,a,R,policy):
    global HISTORIES,ADMITTED,NONCONSTANT_BOTH
    HISTORIES+=1;n=k+m;delta=F(1,1<<n);base=g*(1<<m);h=base[:];h[a]*=-1;root=base+h
    pg=spectrum(g);support=[T for T,x in enumerate(pg) if x];rs_mass=sum(R[T] for T in support)
    rs={T:R[T]/rs_mass for T in support};w=2*delta-len(support)*delta*delta
    Q=[(1-w)*rs[T] if T in rs else delta*delta for T in range(1<<(n+1))]
    check(sum(Q)==1 and all(Q));check(all(spectrum(root)))
    Ig=influence(g);Cg=ce(pg,R);croot=ce(spectrum(root),Q)
    j=sum(g[a]!=g[a^(1<<i)] for i in range(k));check(influence(root)==Ig+delta*(n+1-2*j))
    totals={'cg_lo':F(0),'cg_hi':F(0),'im':F(0),'ig':F(0),'pi_g':F(0),'pi_m':F(0)}
    ta=ja=0
    def walk(gv,mv,qv,remaining,depth,b0,reach,onpoint):
        nonlocal ta,ja
        more=depth==0 or (depth==1 and k>1 and (policy=='fixed2' or policy=='adaptive' and b0==0))
        if not more:
            c=ce(spectrum(mv),qv);totals['cg_lo']+=reach*c[0];totals['cg_hi']+=reach*c[1]
            totals['im']+=reach*influence(mv);totals['ig']+=reach*influence(gv)
            return
        original=depth;local=remaining.index(original)
        totals['pi_g']+=reach*directional(gv,local);totals['pi_m']+=reach*directional(mv,local)
        if onpoint:
            ta+=1;ja+=int(g[a]!=g[a^(1<<original)])
        mc,refs,Z=transfer(mv,qv,local);gc=split(gv,local)
        if depth==0 and all(influence(x)>0 for x in gc):
            global NONCONSTANT_BOTH
            NONCONSTANT_BOTH+=1
        for b in (0,1):
            walk(gc[b],mc[b],refs[b],[i for i in remaining if i!=original],depth+1,b if depth==0 else b0,reach/2,onpoint and b==((a>>original)&1))
    # gv includes all dummy/selector positions, so use same remaining physical labels for both.
    walk(base+base,root,Q,list(range(n+1)),0,None,F(1),True)
    check(totals['pi_m']==totals['pi_g']+delta*(ta-2*ja))
    check(totals['ig']==Ig-totals['pi_g'])
    check(totals['im']==Ig-totals['pi_g']+delta*(n+1-ta-2*(j-ja)))
    check(totals['cg_lo']<=croot[1])
    if Ig and Cg[1]<=4*Ig:
        beta=totals['pi_g']/Ig;A=F(6*k)+F(7,2)
        if F(1,1<<m)*A<=2-6*beta:
            ADMITTED+=1;check(totals['cg_hi']<=6*totals['im'])
    if k==5:
        CERTS.append({'m':m,'policy':policy,'source_I':str(Ig),'Pi_g':str(totals['pi_g']),'Pi_M':str(totals['pi_m']),'point_depth':ta,'removed_edges_queried':ja,'terminal_I_average':str(totals['im']),'terminal_CE_interval':saved_interval(totals['cg_lo'],totals['cg_hi']),'saved_grid':'outward2^-80'})

mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
if mode in ('pilot','small'):
    limit=4 if mode=='pilot' else 1568
    for k in (1,2,3):
        masks=range(1<<(1<<k)) if k<3 else [1,3,15,23,85,105,127,255]
        for mask in masks:
            g=[1 if mask>>j&1 else -1 for j in range(1<<k)]
            for a in range(1<<k):
                for m in (1,4):
                    for variant in (0,1):
                        R=[F(1 if variant==0 else T+1) for T in range(1<<k)];N=sum(R);R=[r/N for r in R]
                        for policy in (['first'] if k==1 else ['first','fixed2','adaptive']):
                            if HISTORIES==limit:break
                            history(g,k,m,a,R,policy)
                        if HISTORIES==limit:break
                    if HISTORIES==limit:break
                if HISTORIES==limit:break
            if HISTORIES==limit:break
        if HISTORIES==limit:break
elif mode in ('critical-one','critical-two'):
    g=[(-1 if (j&7)==0 else 1)*(-1 if (j>>3)==0 else 1) for j in range(32)]
    pg=spectrum(g)
    history(g,5,6 if mode=='critical-one' else 7,0,pg,'first' if mode=='critical-one' else 'adaptive')
    check(ADMITTED==1);check(NONCONSTANT_BOTH==1)
else:raise ValueError(mode)
elapsed=time.monotonic()-START;check(elapsed<55)
result={'status':'PASS','helper_version':'A095-adaptive-point-history-v1.1','mode':mode,'histories':HISTORIES,'exact_assertions':CHECKS,'transports':TRANSPORTS,'admitted_histories':ADMITTED,'both_nonconstant_first_children':NONCONSTANT_BOTH,'nonunit_child_normalizers':NORMALIZERS_NONUNIT,'elapsed_seconds':elapsed,'critical_certificates':CERTS}
(RUN/'out'/('PILOT.json' if mode=='pilot' else 'EXACT_'+mode+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='critical_certificates'}))
