import exact as e
from exact import Q,add,entropy,logform,check,interval,nonnegative
from functools import lru_cache
from pathlib import Path
import math,json,time,sys,itertools
R=Path(__file__).resolve().parents[1];START=time.perf_counter()
def dim(t):return (len(t)-1).bit_length()
@lru_cache(None)
def spec(t):return e.spec(t,(Q(1,2),)*dim(t))
def eta(x):return add((-x,logform(x))) if x else {}
def Phi(a,b):return add((1,eta(a)),(1,eta(b)),(-1,eta(a+b)))
def pd(a,b):return add((1,eta(a*a)),(1,eta(b*b)),(-Q(1,2),eta((a+b)**2)),(-Q(1,2),eta((a-b)**2)))
def sumiv(a,b):return e.plus(a,b)
def diviv(a,b):
    assert b[0]>0
    v=[x/y for x in a for y in b];return e.mesh((min(v),max(v)))
EE=sum(Q(1,math.factorial(i)) for i in range(33)); EI=(EE,EE+Q(1,math.factorial(33))/(1-Q(1,34)))
CI=diviv((Q(1),)*2,e.LN2); CD=sumiv(CI,diviv((Q(2),)*2,(EI[0]*e.LN2[0],EI[1]*e.LN2[1]))); CP=sumiv((Q(3),)*2,e.scale(2,CI))
def bounded(form,kiv,mass):
    if not form and not mass:return
    lo,hi=interval(form);assert hi<=kiv[0]*mass,(form,kiv,mass,hi)
def zeros():return {'H':{},'U':{},'R':{},'I':Q(0),'rdata':{},'kappa':{},'ctrlres':{},'cap':(Q(0),Q(0)),'T':Q(0),'pid':Q(0),'pic':Q(0)}
@lru_cache(None)
def table(ctrl,cores):
    nc=dim(ctrl);sizes=[dim(t) for t in cores];out=[]
    for x in range(1<<(nc+sum(sizes))):
        j=ctrl[x&((1<<nc)-1)]
        if not j:out.append(1);continue
        offset=nc+sum(sizes[:j-1]);out.append(cores[j-1][(x>>offset)&((1<<sizes[j-1])-1)])
    return tuple(out)
@lru_cache(None)
def potentials(ctrl,cores):
    qs=tuple(Q(ctrl.count(j),len(ctrl)) for j in range(1,len(cores)+1));U={};RR={};ms=[]
    for q,u in zip(qs,cores):
        m=Q(sum(u),len(u));ms.append(m);P=spec(u)[1]
        U=add((1,U),(q,entropy(P)),(-q,eta(m*m)))
        RR=add((1,RR),((1-m*m),eta(q)))
    return qs,tuple(ms),U,RR
@lru_cache(None)
def real_coeff(t):
    ps=(Q(1,2),)*dim(t);_,norms,rows=e.rows(ps)
    return tuple(Q(sum(a*f for a,f in zip(row,t)),den)*(1<<s.bit_count()) for s,(den,row) in enumerate(rows))
@lru_cache(None)
def outer_rows(ctrl,cores,j):
    nc=dim(ctrl);ms=potentials(ctrl,cores)[1];sizes=[dim(t) if k!=j else 0 for k,t in enumerate(cores)]
    aa=[];cc=[]
    for x in range(1<<(nc+sum(sizes))):
        state=ctrl[x&((1<<nc)-1)];C=int(state==j+1)
        if C:W=0
        elif not state:W=1
        else:
            k=state-1;offset=nc+sum(sizes[:k]);W=cores[k][(x>>offset)&((1<<sizes[k])-1)]
        aa.append(Q(W)+ms[j]*C);cc.append(Q(C))
    return real_coeff(tuple(aa)),real_coeff(tuple(cc))
def restrict(ctrl,cores,kind,j,i,b):
    if kind=='control':return e.restrict(ctrl,[i],b)[0],cores
    us=list(cores);us[j]=e.restrict(us[j],[i],b)[0];return ctrl,tuple(us)
@lru_cache(None)
def analyze(ctrl,cores,kind,j,i):
    root=table(ctrl,cores);_,P=spec(root);qs,ms,U,RR=potentials(ctrl,cores)
    children=[restrict(ctrl,cores,kind,j,i,b) for b in range(2)];pots=[potentials(c,us) for c,us in children]
    childP=[spec(table(c,us))[1] for c,us in children]
    D=add((1,entropy(P)),*[(-Q(1,2),entropy(pp)) for pp in childP])
    du=add((1,U),*[(-Q(1,2),v[2]) for v in pots]);dr=add((1,RR),*[(-Q(1,2),v[3]) for v in pots])
    globali=i if kind=='control' else dim(ctrl)+sum(dim(t) for t in cores[:j])+i
    inf=sum(v for s,v in enumerate(P) if s>>globali&1)
    check(e.inf(P)-sum(e.inf(pp) for pp in childP)/2,inf)
    local=zeros();local['children']=children
    if kind=='control':
        check(du,{})
        kl={}
        for k,q in enumerate(qs):
            if q:
                x=pots[0][0][k]/(2*q)
                kl=add((1,kl),(q*(1-ms[k]**2),add((1,logform(Q(2))),(-1,entropy((x,1-x))))))
        check(dr,kl);nonnegative(dr);local['kappa']=dr;local['ctrlres']=add((1,D),(-1,dr));local['pic']=inf
    else:
        q=qs[j];m=ms[j];raw,coreP=spec(cores[j]);beta=raw[1<<i]*2;t=beta*beta;V=1-m*m
        rloss=add((t,eta(q)));check(dr,rloss);local['rdata']=dr;local['T']=q*t;local['pid']=inf
        coreInf=sum(v for s,v in enumerate(coreP) if s>>i&1);check(inf,q*coreInf)
        if q:
            aa,cc=outer_rows(ctrl,cores,j)
            check(sum(x*x for x in aa),1-q*V);check(sum(x*x for x in cc),q)
            def M(s):return add(*[(1,Phi(a*a,s*c*c)) for a,c in zip(aa,cc)])
            Mt=M(t);N=add(*[(1,add((1,pd(a,beta*c)),(-1,Phi(a*a,t*c*c)))) for a,c in zip(aa,cc)])
            check(D,add((1,du),(1,Mt),(1,N),(-q,eta(t))))
            nonnegative(N);bounded(N,e.scale(2,CI),q*t)
            bounded(add((1,D),(-1,du),(-1,dr)),e.scale(3,CI),q*t)
            if V and t:
                Mv=M(V);nonnegative(add((1,entropy((q*V,1-q*V))),(-1,Mv)))
                branch=add((t/V,Mv),(q*t,logform(V/t)))
                nonnegative(add((1,branch),(-1,Mt)))
                iv1=interval(Mv);iv2=interval(branch);local['cap']=tuple(min(x,y) for x,y in zip(iv1,iv2))
        else:check(D,{});check(du,{})
    return local
def choose(ctrl,cores,rule,depth):
    candidates=[('control',0,i) for i in range(dim(ctrl))]+[('data',j,i) for j,u in enumerate(cores) for i in range(dim(u))]
    if not candidates:return None
    if rule==0:return candidates[0]
    if rule==1:return next((v for v in candidates if v[0]=='data'),candidates[0])
    if rule==2:
        desired='control' if depth%2==0 else 'data';return next((v for v in candidates if v[0]==desired),candidates[0])
    desired='data' if sum(ctrl)%2 else 'control'
    picks=[v for v in candidates if v[0]==desired] or candidates
    return picks[-1]
def merge(a,b):
    z=zeros()
    for k in ['H','U','R','rdata','kappa','ctrlres']:z[k]=add((Q(1,2),a[k]),(Q(1,2),b[k]))
    for k in ['I','T','pid','pic']:z[k]=(a[k]+b[k])/2
    z['cap']=e.scale(Q(1,2),sumiv(a['cap'],b['cap']));return z
def tree(ctrl,cores,rule,point=False,depth=0):
    P=spec(table(ctrl,cores))[1];q,ms,U,RR=potentials(ctrl,cores);start=zeros();start.update({'H':entropy(P),'U':U,'R':RR,'I':e.inf(P)})
    option=choose(ctrl,cores,rule,depth)
    if option is None or len(set(table(ctrl,cores)))==1:return [start]
    kind,j,i=option;loc=analyze(ctrl,cores,kind,j,i)
    if point and kind=='control' and q[0]:
        z=q[0]*(1-ms[0]);V=1-ms[0]**2
        B={} ;probs=[Q(0)]*(len(P)//2)
        for s,v in enumerate(P):probs[e.compressed(s,[k for k in range(dim(table(ctrl,cores))) if k!=i])]+=v
        B=add((1,entropy(P)),(-1,entropy(tuple(probs))))
        expected=add(((q[0]-2*q[0]**2)*(1-ms[0])**2,logform(Q(2))),(1,Phi((1-z)**2,z*z)))
        check(add((1,B),(-1,loc['kappa'])),expected);check(loc['pic'],z)
        nonnegative(loc['ctrlres']);bounded(loc['ctrlres'],CP,z)
    sub=[tree(c,us,rule,point,depth+1) for c,us in loc['children']]
    out=[start]
    for d in range(max(len(t) for t in sub)):
        z=merge(sub[0][min(d,len(sub[0])-1)],sub[1][min(d,len(sub[1])-1)])
        for k in ['rdata','kappa','ctrlres']:z[k]=add((1,z[k]),(1,loc[k]))
        for k in ['T','pid','pic']:z[k]+=loc[k]
        z['cap']=sumiv(z['cap'],loc['cap'])
        check(RR,add((1,z['R']),(1,z['rdata']),(1,z['kappa'])))
        check(e.inf(P),z['I']+z['pid']+z['pic'])
        lhs=add((1,entropy(P)),(-1,z['H']),(-1,U),(1,z['U']),(-1,RR),(1,z['R']),(-1,z['ctrlres']))
        bounded(lhs,e.scale(3,CI),z['T'])
        allowance=add((1,RR),(-1,z['R']),(-1,z['kappa']))
        allowance_iv=sumiv(interval(allowance),e.scale(z['pid'],CD))
        assert z['cap'][1]<=allowance_iv[0] or z['cap']==allowance_iv==(0,0)
        if point:bounded(z['ctrlres'],CP,z['pic'])
        out.append(z)
    return out
def initial(ctrl,cores):
    P=spec(table(ctrl,cores))[1];nc=dim(ctrl);ctrlI=sum(v for s,v in enumerate(P) for i in range(nc) if s>>i&1)
    nonnegative(add((2*ctrlI,logform(Q(2))),(-1,potentials(ctrl,cores)[3])))
    return ctrlI
def main():
    pilot='--pilot' in sys.argv;phase='pilot' if pilot else sys.argv[sys.argv.index('--phase')+1]
    roots=trees=frontiers=0;fixtures=[]
    lo=int(sys.argv[sys.argv.index('--start')+1]) if '--start' in sys.argv else 0
    hi=int(sys.argv[sys.argv.index('--end')+1]) if '--end' in sys.argv else None
    if phase in ['pilot','controllers']:
        maps=list(itertools.product(range(3),repeat=4));maps=maps[:8] if pilot else maps[lo:hi]
        cores=[e.tab(mask,1) for mask in range(4)]
        for ctrl in maps:
            for u in cores:
                for v in cores:
                    us=(u,v);initial(ctrl,us);roots+=1
                    for policy in range(4):frontiers+=len(tree(ctrl,us,policy));trees+=1
            if time.perf_counter()-START>110:raise RuntimeError('frozen watchdog')
    if phase in ['pilot','activation']:
        ns=[int(sys.argv[sys.argv.index('--n')+1])] if '--n' in sys.argv else range(2 if pilot else 4)
        for n in ns:
            for mask in range(lo,hi if hi is not None else 1<<(1<<n)):
                u=e.tab(mask,n)
                for r in ([1] if pilot else [1,2,3]):
                    ctrl=tuple(1 if x==0 else 0 for x in range(1<<r));initial(ctrl,(u,));roots+=1
                    for policy in range(4):
                        rows=tree(ctrl,(u,),policy,True);frontiers+=len(rows);trees+=1
                    if time.perf_counter()-START>110:raise RuntimeError('frozen watchdog')
    output={'status':'PASS','phase':phase,'roots':roots,'trees':trees,'frontiers':frontiers,'counted_exact_assertions':e.COUNT,'analyzed_states':analyze.cache_info().currsize,'runtime_seconds':time.perf_counter()-START,'constants_rational':{'data_signed_3_over_ln2':[str(x) for x in e.scale(3,CI)],'positive_cap':[str(x) for x in CD],'point_controller_3_plus_2_over_ln2':[str(x) for x in CP]},'scope':'A059 interleaved reserve and signed DATA bound reviewed; point-controller residual priced; generic-controller and actual terminal functional remain unpaid.'}
    suffix=('_'+str(lo)+'_'+str(hi)) if '--start' in sys.argv else ''
    if '--n' in sys.argv:suffix='_n'+sys.argv[sys.argv.index('--n')+1]+suffix
    output['domain_slice']={'start':lo,'end':hi,'n':int(sys.argv[sys.argv.index('--n')+1]) if '--n' in sys.argv else None}
    (R/'out'/(phase.upper()+suffix+'.json')).write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output))
if __name__=='__main__':main()
