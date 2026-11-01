"""One original inherited controller-shape account; no renewed descendant supplier."""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys,hashlib
import base as m
e=m.e;R=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot';START=time.monotonic()
cases=queries=0;guard_witnesses={}

def state(a,g,h,ra,rg,rh):
    old=m.profile(a,g,h,rg,rh);pa=m.spectrum(a)
    V=1-pa[0];beta=1-ra[0];gamma=F(sum(x!=y for x,y in zip(g,h)),len(g))
    Da=m.kl(pa,ra);C=m.kl((1-V,V),(1-beta,beta));m.nn(C,'vacuum')
    shape=m.kl(tuple(x/V for x in pa[1:]),tuple(x/beta for x in ra[1:])) if V else {}
    m.eq(Da,e.add(C,e.scale(shape,V)),'controller vacuum chain')
    oldrf=old['rf'];Q=[];na=len(a)
    # Actual conditional empty probability is retained; only nonempty shape changes.
    for t in range(len(g)):
        row=oldrf[t*na:(t+1)*na];nonempty=sum(row[1:])
        Q.append(row[0])
        Q.extend(nonempty*x/beta if beta else F(0) for x in ra[1:])
        if nonempty:m.ck(beta>0)
    Q=tuple(Q);D=m.kl(m.spectrum(m.mux(a,g,h)),Q)
    delta=e.scale(shape,gamma*V)
    m.eq(D,e.add(old['D'],delta),'genuine nonempty-shape cost')
    T=e.add(old['W'],e.scale(Da,gamma));S=e.add(old['Z'],e.scale(C,gamma))
    m.eq(D,e.add(T,m.neg(S)),'full debt/slack');m.nn(S,'S')
    out=dict(D=D,T=T,S=S,Da=Da,C=C,delta=delta,Q=Q,H=old['H'],gamma=gamma,p=old['p'],Z=old['Z'],W=old['W'],V=V,beta=beta)
    if V and e.enclosure(delta)[0]>0 and 'positive_shape' not in guard_witnesses:
        guard_witnesses['positive_shape']=dict(a=a,g=g,h=h,ra=[str(x) for x in ra],delta=m.encoded(delta),interval=m.interval(delta))
    if e.enclosure(e.scale(C,gamma))[0]>0 and 'vacuum_needed' not in guard_witnesses:
        guard_witnesses['vacuum_needed']=dict(a=a,g=g,h=h,ra=[str(x) for x in ra],vacuum=m.encoded(e.scale(C,gamma)),interval=m.interval(e.scale(C,gamma)),S=m.encoded(S),Z=m.encoded(old['Z']))
    return out

def children(a,g,h,ra,rg,rh,i):
    na=len(a).bit_length()-1
    if i<na:
        raa,E,O,rho=m.physical(a,ra,i)
        args=[(m.restrict(a,i,b),g,h,raa[b],rg,rh) for b in (0,1)]
        release=e.scale(e.add(E,O),F(sum(x!=y for x,y in zip(g,h)),len(g)))
    else:
        j=i-na;rgg,Eg,Og,rhog=m.physical(g,rg,j);rhh,Eh,Oh,rhoh=m.physical(h,rh,j)
        args=[(a,m.restrict(g,j,b),m.restrict(h,j,b),ra,rgg[b],rhh[b]) for b in (0,1)]
        p=F(a.count(-1),len(a))
        release=e.add(e.scale(e.add(Eg,Og),1-p),e.scale(e.add(Eh,Oh),p))
    return args,release

def rowcheck(args,i,s=None):
    global queries
    queries+=1;a,g,h,ra,rg,rh=args;s=state(*args) if s is None else s
    aa,release=children(*args,i)
    kk=[state(*ar) for ar in aa]
    A=e.add(s['T'],m.neg(m.avg(*(k['T'] for k in kk))))
    m.eq(A,release,'T physical release');m.nn(A,'Atot')
    sigma=e.add(m.avg(*(k['D'] for k in kk)),m.neg(s['D']))
    m.eq(sigma,e.add(s['S'],m.neg(m.avg(*(k['S'] for k in kk))),m.neg(A)),'sigma')
    refs,Ef,Of,rho=m.physical(m.mux(a,g,h),s['Q'],i)
    Dinh=[m.kl(m.spectrum(m.restrict(m.mux(a,g,h),i,b)),refs[b]) for b in (0,1)]
    kappa=e.add(m.avg(*(k['D'] for k in kk)),m.neg(m.avg(*Dinh)))
    m.eq(kappa,e.add(sigma,Ef,Of),'raw output reset')
    if i>=len(a).bit_length()-1:
        m.ck((kk[0]['gamma']+kk[1]['gamma'])/2==s['gamma'])
        m.eq(kk[0]['Da'],s['Da']);m.eq(kk[1]['Da'],s['Da'])
    return aa,kk,A,sigma,dict(coordinate=i,sigma=m.encoded(sigma),kappa=m.encoded(kappa),Ef=m.encoded(Ef),Of=m.encoded(Of),rho=[str(x) for x in rho],child_D=[m.encoded(k['D']) for k in kk],child_S=[m.encoded(k['S']) for k in kk])

def controlrefs(a):
    pa=m.spectrum(a);V=1-pa[0];N=len(a)-1
    if not V:return ((F(1),)+(F(0),)*N,)*2
    uniform=(pa[0],)+tuple(V/N for _ in range(N))
    mixed=(pa[0],)+tuple((x+V/N)/2 for x in pa[1:])
    return uniform,mixed

def one(args,label):
    global cases
    cases+=1;a,g,h,ra,rg,rh=args;s=state(*args)
    m.ck(ra[0]==m.spectrum(a)[0]);m.eq(s['C'],{})
    ceplus=e.add(*(e.scale(e.lg(y),-x) for x,y in zip(m.spectrum(a)[1:],ra[1:]) if x))
    m.eq(ceplus,e.add(e.stats(a)[1],s['Da']),'root calibrated CEplus')
    if rg==rh:m.eq(s['S'],m.profile(a,g,h,rg,rh)['Z'],'same J root')
    for i in range((len(a)*len(g)).bit_length()-1):rowcheck(args,i,s)
    if cases%50==0 and time.monotonic()-START>(60 if MODE=='pilot' else 480):raise TimeoutError('frozen cap')

def walk(args,labels,order,history=(),adaptive=False):
    s=state(*args)
    stop=not labels or not order or (adaptive and len(history)>=3 and sum(history)%2==0)
    if stop:
        return dict(sig={},A={},Sleaf=s['S'],path={},ce=e.add(s['H'],s['D']),leaves=1,nodes=1,receipts=[],terminals=[dict(D=m.encoded(s['D']),delta=m.encoded(s['delta']),vacuum=m.encoded(e.scale(s['C'],s['gamma'])),Z=m.encoded(s['Z']),S=m.encoded(s['S']))])
    choices=tuple(reversed(order)) if adaptive and sum(history)%2 else order
    lab=next(x for x in choices if x in labels);i=labels.index(lab)
    aa,kk,A,sigma,receipt=rowcheck(args,i,s);receipt['label']=lab
    rest=labels[:i]+labels[i+1:]
    # Preserve full priority list in adaptive mode; fixed policy consumes one entry.
    rr=[walk(aa[b],rest,order if adaptive else order[1:],history+(b,),adaptive) for b in (0,1)]
    out={k:m.avg(*(z[k] for z in rr)) for k in ('sig','A','Sleaf','path','ce')}
    out['sig']=e.add(sigma,out['sig']);out['A']=e.add(A,out['A'])
    out['path']=e.add(s['H'],m.neg(m.avg(*(k['H'] for k in kk))),out['path'])
    out.update(leaves=sum(z['leaves'] for z in rr),nodes=1+sum(z['nodes'] for z in rr),receipts=[receipt]+sum((z['receipts'] for z in rr),[]),terminals=sum((z['terminals'] for z in rr),[]))
    m.eq(e.add(out['sig'],out['A'],out['Sleaf']),s['S'],'tree slack')
    m.eq(e.add(out['path'],out['ce'],out['A'],out['Sleaf']),e.add(s['H'],s['T']),'whole bill')
    return out

if __name__=='__main__':
    for na,ca,a in e.tables(1 if MODE=='pilot' else 2):
        for nx,cg,g in e.tables(1):
            for nh,ch,h in e.tables(1):
                if nx!=nh:continue
                for ra in controlrefs(a):
                    for rg in m.refs(g):
                        for rh in m.refs(h):one((a,g,h,ra,rg,rh),(na,ca,nx,cg,ch))
    policies=[]
    if MODE=='full':
        a=tuple(-1 if x<3 else 1 for x in range(8))
        g=tuple((-1 if x&7==0 else 1)*(-1 if x&8 else 1) for x in range(16))
        h=tuple((-1 if (x&7).bit_count()>=2 else 1)*(-1 if x&8 else 1) for x in range(16))
        V=1-m.spectrum(a)[0];ra=(1-V,)+tuple(V*F(x,28) for x in range(1,8));r=tuple(F(1,16) for _ in range(16))
        args=(a,g,h,ra,r,r);s=state(*args);one(args,'fixed seven-variable weighted controller')
        labels=('C0','C1','C2','D0','D1','D2','D3')
        for order,adaptive in [(('D0','C0','D1','C1'),False),(('C0','D0','C1','D1','C2','D2','D3'),False),(labels,True)]:
            ans=walk(args,labels,order,adaptive=adaptive)
            policies.append(dict(order=order,adaptive=adaptive,**{k:ans[k] for k in ('leaves','nodes','receipts','terminals')},ledger={k:m.encoded(ans[k]) for k in ('sig','A','Sleaf','path','ce')}))
        # A fixed original root earmark, including a genuine old debit. Not a general supplier.
        If=e.stats(m.mux(a,g,h))[3];U=4*If;old=F(1,8)
        reserve=e.add({2:U-old},m.neg(e.add(s['H'],s['T'])));m.nn(reserve,'old-debit root admission')
        fixture=dict(I=str(If),U=str(U),old_debit=str(old),root_T=m.encoded(s['T']),root_S=m.encoded(s['S']),root_shape=m.encoded(s['delta']),reserve=m.encoded(reserve),reserve_interval=m.interval(reserve))
    else:fixture=None
    out=dict(status='PASS',mode=MODE,cases=cases,queries=queries,assertions=m.checks,seconds=time.monotonic()-START,guards=guard_witnesses,fixture=fixture,policies=policies,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (R/'out'/('check_'+MODE+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
    print(json.dumps({k:v for k,v in out.items() if k not in ('guards','policies')}))
