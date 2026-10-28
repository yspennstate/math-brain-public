"""Conditional-label garbling pays genuine row-odds changes from the old v8 T."""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys,hashlib
import prior8 as v
m=v.m;e=v.e;R=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot';START=time.monotonic()
cases=queries=positive_rows=0;witness={}

def kernel(alpha,b,mode):
    if mode==0:return b,b
    tau=min(alpha,b) if mode==1 else max(F(0),alpha+b-1)
    u=tau/alpha if alpha else F(0)
    z=(b-tau)/(1-alpha) if alpha<1 else F(0)
    m.ck(0<=u<=1 and 0<=z<=1 and alpha*u+(1-alpha)*z==b)
    return u,z

def state(args,mode):
    global positive_rows
    a,g,h,ra,rg,rh=args;s=v.state(*args);pa=m.spectrum(a);pg=m.spectrum(g);ph=m.spectrum(h)
    pf=m.spectrum(m.mux(a,g,h));N=len(a);beta=1-ra[0]
    Q=[];C={};left={};rows=[]
    for t in range(len(g)):
        actual=pf[t*N:(t+1)*N];q=sum(actual);r=sum(s['Q'][t*N:(t+1)*N])
        if not q:
            Q.extend((r,)+(F(0),)*(N-1));continue
        b=sum(actual[1:])/q;alpha=(1-s['p'])*pg[t]/q;rho=(1-s['p'])*rg[t]/r
        u,z=kernel(alpha,b,mode);ell=rho*u+(1-rho)*z
        m.ck(0<=ell<=1 and (beta>0 or ell==0))
        rowC=m.kl((1-b,b),(1-ell,ell));conditional={}
        for y,py,ry in [(0,1-b,1-ell),(1,b,ell)]:
            if not py:continue
            kG=u if y else 1-u;kH=z if y else 1-z
            posterior=(alpha*kG/py,(1-alpha)*kH/py)
            rposterior=(rho*kG/ry,(1-rho)*kH/ry)
            conditional=e.add(conditional,e.scale(m.kl(posterior,rposterior),py))
        m.eq(m.kl((alpha,1-alpha),(rho,1-rho)),e.add(rowC,conditional),'row disintegration')
        m.nn(rowC);m.nn(conditional)
        C=e.add(C,e.scale(rowC,q));left=e.add(left,e.scale(conditional,q))
        Q.append(r*(1-ell));Q.extend(r*ell*x/beta if beta else F(0) for x in ra[1:])
        if e.enclosure(rowC)[0]>0:
            positive_rows+=1
            if not witness:witness.update(a=a,g=g,h=h,mode=mode,row=t,alpha=str(alpha),rho=str(rho),true_odds=str(b),changed_odds=str(ell),kernel=[str(u),str(z)],row_cost=m.encoded(rowC),row_cost_interval=m.interval(rowC))
        rows.append(dict(t=t,q=str(q),r=str(r),alpha=str(alpha),rho=str(rho),b=str(b),ell=str(ell),u=str(u),v=str(z),cost=m.encoded(rowC)))
    Q=tuple(Q);D=m.kl(pf,Q)
    m.eq(D,e.add(s['D'],C),'old changed shape plus row cost')
    m.eq(s['Z'],e.add(C,left),'original source label slack split')
    S=e.add(s['S'],m.neg(C));m.nn(S,'new residual');m.nn(e.add(s['Z'],m.neg(C)),'row payment')
    m.eq(D,e.add(s['T'],m.neg(S)),'same T, smaller S')
    return dict(D=D,S=S,T=s['T'],H=s['H'],Q=Q,C=C,Z=s['Z'],rows=rows,gamma=s['gamma'])

def rowcheck(args,i,parentmode,childmode,s=None):
    global queries
    queries+=1;s=state(args,parentmode) if s is None else s
    aa,release=v.children(*args,i);kk=[state(ar,childmode) for ar in aa]
    A=e.add(s['T'],m.neg(m.avg(*(x['T'] for x in kk))));m.eq(A,release);m.nn(A)
    sigma=e.add(m.avg(*(x['D'] for x in kk)),m.neg(s['D']))
    m.eq(sigma,e.add(s['S'],m.neg(m.avg(*(x['S'] for x in kk))),m.neg(A)))
    f=m.mux(*args[:3]);inh,Ef,Of,rho=m.physical(f,s['Q'],i)
    Dinh=[m.kl(m.spectrum(m.restrict(f,i,b)),inh[b]) for b in (0,1)]
    raw=e.add(m.avg(*(x['D'] for x in kk)),m.neg(m.avg(*Dinh)))
    m.eq(raw,e.add(sigma,Ef,Of),'CURRENT odds-changed output reference')
    receipt=dict(i=i,parent_mode=parentmode,child_mode=childmode,parent_row_cost=m.encoded(s['C']),child_row_cost=[m.encoded(x['C']) for x in kk],sigma=m.encoded(sigma),kappa=m.encoded(raw),Ef=m.encoded(Ef),Of=m.encoded(Of),rho=[str(x) for x in rho],child_D=[m.encoded(x['D']) for x in kk],child_S=[m.encoded(x['S']) for x in kk])
    return aa,kk,A,sigma,receipt

def walk(args,labels,order,history=(),data_count=0,adaptive=False):
    mode=min(data_count,2);s=state(args,mode)
    if not order or not labels or (adaptive and len(history)>=3 and sum(history)%2==0):
        return dict(sig={},A={},Sleaf=s['S'],path={},ce=e.add(s['H'],s['D']),rowcost=s['C'],leaves=1,nodes=1,receipts=[],terminals=[dict(D=m.encoded(s['D']),S=m.encoded(s['S']),C=m.encoded(s['C']),mode=mode,rows=s['rows'])])
    choices=tuple(reversed(order)) if adaptive and sum(history)%2 else order
    label=next(x for x in choices if x in labels);i=labels.index(label);nextcount=data_count+(label.startswith('D'))
    aa,kk,A,sigma,rec=rowcheck(args,i,mode,min(nextcount,2),s);rec['label']=label
    rest=labels[:i]+labels[i+1:]
    rr=[walk(aa[b],rest,order if adaptive else order[1:],history+(b,),nextcount,adaptive) for b in (0,1)]
    out={k:m.avg(*(z[k] for z in rr)) for k in ('sig','A','Sleaf','path','ce','rowcost')}
    out['sig']=e.add(sigma,out['sig']);out['A']=e.add(A,out['A'])
    out['path']=e.add(s['H'],m.neg(m.avg(*(x['H'] for x in kk))),out['path'])
    out.update(leaves=sum(z['leaves'] for z in rr),nodes=1+sum(z['nodes'] for z in rr),receipts=[rec]+sum((z['receipts'] for z in rr),[]),terminals=sum((z['terminals'] for z in rr),[]))
    m.eq(e.add(out['sig'],out['A'],out['Sleaf']),s['S'],'all switches same S account')
    m.eq(e.add(out['path'],out['ce'],out['A'],out['Sleaf']),e.add(s['H'],s['T']),'full original quota')
    return out

if __name__=='__main__':
    for na,ca,a in e.tables(1 if MODE=='pilot' else 2):
        for nx,cg,g in e.tables(1):
            for nh,ch,h in e.tables(1):
                if nx!=nh:continue
                for ra in v.controlrefs(a):
                    for rg in m.refs(g):
                        for rh in m.refs(h):
                            args=(a,g,h,ra,rg,rh)
                            for mode in (0,1,2):
                                cases+=1;s=state(args,mode)
                                for i in range((len(a)*len(g)).bit_length()-1):rowcheck(args,i,mode,mode,s)
                                if cases%100==0 and time.monotonic()-START>(60 if MODE=='pilot' else 480):raise TimeoutError('frozen runtime cap')
    policies=[];fixture=None
    if MODE=='full':
        a=tuple(-1 if x<3 else 1 for x in range(8))
        g=tuple((-1 if x&7==0 else 1)*(-1 if x&8 else 1) for x in range(16))
        h=tuple((-1 if (x&7).bit_count()>=2 else 1)*(-1 if x&8 else 1) for x in range(16))
        V=1-m.spectrum(a)[0];ra=(1-V,)+tuple(V*F(x,28) for x in range(1,8));r=tuple(F(1,16) for _ in g)
        args=(a,g,h,ra,r,r);root=state(args,0);labels=('C0','C1','C2','D0','D1','D2','D3')
        for order,adaptive in [(('D0','C0','D1','C1'),False),(('C0','D0','C1','D1','C2','D2','D3'),False),(labels,True)]:
            ans=walk(args,labels,order,adaptive=adaptive)
            policies.append(dict(order=order,adaptive=adaptive,nodes=ans['nodes'],leaves=ans['leaves'],ledger={k:m.encoded(ans[k]) for k in ('sig','A','Sleaf','path','ce','rowcost')},receipts=ans['receipts'],terminals=ans['terminals']))
        I=e.stats(m.mux(a,g,h))[3];U=4*I;b=F(1,8)
        reserve=e.add({2:U-b},m.neg(e.add(root['H'],root['T'])));m.nn(reserve)
        fixture=dict(I=str(I),U=str(U),old_debit=str(b),root_T=m.encoded(root['T']),root_S=m.encoded(root['S']),reserve=m.encoded(reserve),reserve_interval=m.interval(reserve))
    out=dict(status='PASS',mode=MODE,cases=cases,queries=queries,assertions=m.checks,positive_row_cost_visits=positive_rows,seconds=time.monotonic()-START,witness=witness,fixture=fixture,policies=policies,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (R/'out'/('check_'+MODE+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
    print(json.dumps({k:v for k,v in out.items() if k not in ('witness','policies')}))
