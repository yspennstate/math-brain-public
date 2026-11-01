"""Separate direct-character/posterior implementation; no main-checker imports."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
import independent8 as old
b=old.b;R=Path(__file__).resolve().parents[1];START=time.monotonic();nodes=leaves=changed=0

def state(args,mode):
    global changed
    s=old.state(*args);a,g,h,ra,rg,rh=args;pf=b.law(s['f']);pg=b.law(g);beta=1-ra[0];N=len(a)
    ref=[];cost={};residual={}
    for t in range(len(g)):
        actual=pf[t*N:(t+1)*N];q=sum(actual);r=sum(s['ref'][t*N:(t+1)*N])
        if not q:ref.extend((r,)+(Q(),)*(N-1));continue
        alpha=(1-s['p'])*pg[t]/q;rho=(1-s['p'])*rg[t]/r;non=sum(actual[1:])/q
        if mode==0:kg=kh=non
        else:
            # Intersect source-G quantile interval [0,alpha] with sector interval.
            lo,hi=(Q(0),non) if mode==1 else (1-non,Q(1))
            overlap=max(Q(),min(alpha,hi)-max(Q(),lo))
            kg=overlap/alpha if alpha else Q()
            kh=(non-overlap)/(1-alpha) if alpha<1 else Q()
        b.ck(alpha*kg+(1-alpha)*kh==non)
        ell=rho*kg+(1-rho)*kh;d=b.D((1-non,non),(1-ell,ell));post={}
        for true,reference,kj,kl in [(non,ell,kg,kh),(1-non,1-ell,1-kg,1-kh)]:
            if true:
                post=b.add(post,b.mul(b.D((alpha*kj/true,(1-alpha)*kl/true),(rho*kj/reference,(1-rho)*kl/reference)),true))
        b.ck(not b.difference(b.D((alpha,1-alpha),(rho,1-rho)),b.add(d,post)))
        cost=b.add(cost,b.mul(d,q));residual=b.add(residual,b.mul(post,q))
        ref.append(r*(1-ell));ref.extend(r*ell*x/beta if beta else Q() for x in ra[1:])
    D=b.D(pf,tuple(ref));S=b.difference(s['S'],cost)
    b.ck(not b.difference(D,b.add(s['debt'],cost)));b.ck(not b.difference(D,b.difference(s['T'],S)))
    W=b.difference(s['T'],b.mul(s['Da'],s['gamma']));Ddata=b.difference(s['debt'],s['delta']);Z=b.difference(W,Ddata)
    b.ck(not b.difference(Z,b.add(cost,residual)))
    if cost:changed+=1
    s.update(debt=D,S=S,ref=tuple(ref),C=cost)
    return s

def walk(args,labels,order,history=(),data_count=0,adaptive=False):
    global nodes,leaves
    nodes+=1;s=state(args,min(data_count,2));a,g,h,ra,rg,rh=args
    if not labels or (adaptive and len(history)>=3 and sum(history)%2==0):
        leaves+=1;return dict(sig={},A={},Sleaf=s['S'],path={},ce=b.add(s['H'],s['debt']))
    priorities=tuple(reversed(order)) if adaptive and sum(history)%2 else order
    label=next(x for x in priorities if x in labels);i=labels.index(label);na=len(a).bit_length()-1
    inh,Ef,Of=b.joint(s['f'],s['ref'],i)
    if i<na:
        raa,Ea,Oa=b.joint(a,ra,i);children=[(b.child(a,i,j),g,h,raa[j],rg,rh) for j in (0,1)];release=b.mul(b.add(Ea,Oa),s['gamma'])
    else:
        j=i-na;rgg,Eg,Og=b.joint(g,rg,j);rhh,Eh,Oh=b.joint(h,rh,j)
        children=[(a,b.child(g,j,k),b.child(h,j,k),ra,rgg[k],rhh[k]) for k in (0,1)]
        release=b.add(b.mul(b.add(Eg,Og),1-s['p']),b.mul(b.add(Eh,Oh),s['p']))
    nc=data_count+label.startswith('D');kids=[state(ar,min(nc,2)) for ar in children]
    A=b.difference(s['T'],b.mean(*(z['T'] for z in kids)));b.ck(not b.difference(A,release))
    sigma=b.difference(b.mean(*(z['debt'] for z in kids)),s['debt'])
    raw=b.difference(b.mean(*(z['debt'] for z in kids)),b.mean(*(b.D(b.law(b.child(s['f'],i,k)),inh[k]) for k in (0,1))))
    b.ck(not b.difference(raw,b.add(sigma,Ef,Of)))
    b.ck(not b.difference(sigma,b.add(s['S'],b.mul(b.mean(*(z['S'] for z in kids)),-1),b.mul(A,-1))))
    rest=labels[:i]+labels[i+1:];rr=[walk(ar,rest,order,history+(k,),nc,adaptive) for k,ar in enumerate(children)]
    out={name:b.mean(*(z[name] for z in rr)) for name in rr[0]};out['sig']=b.add(sigma,out['sig']);out['A']=b.add(A,out['A'])
    out['path']=b.add(b.difference(s['H'],b.mean(*(z['H'] for z in kids))),out['path'])
    b.ck(not b.difference(b.add(out['sig'],out['A'],out['Sleaf']),s['S']))
    b.ck(not b.difference(b.add(out['path'],out['ce'],out['A'],out['Sleaf']),b.add(s['H'],s['T'])))
    return out

a=tuple(-1 if x<3 else 1 for x in range(8));g=tuple((-1 if x&3==0 else 1)*(-1 if x&4 else 1) for x in range(8));h=tuple(-1 if x.bit_count()>=2 else 1 for x in range(8))
V=1-b.law(a)[0];ra=(1-V,)+tuple(V*Q(x,28) for x in range(1,8));rg=tuple((x+Q(1,8))/2 for x in b.law(g));rh=tuple(Q(1,8) for _ in h)
labels=('C0','C1','C2','D0','D1','D2');order=('C0','D0','C1','D1','C2','D2');results=[]
for adaptive in (False,True):
    before=(nodes,leaves,b.checks);out=walk((a,g,h,ra,rg,rh),labels,order,adaptive=adaptive)
    results.append(dict(adaptive=adaptive,nodes=nodes-before[0],leaves=leaves-before[1],assertions=b.checks-before[2],ledger={k:{str(x):str(y) for x,y in z.items()} for k,z in out.items()}))
assert nodes<=254 and changed>0
result=dict(status='PASS',nodes=nodes,leaves=leaves,assertions=b.checks,changed_row_node_visits=changed,seconds=time.monotonic()-START,policies=results)
(R/'out/independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps({k:v for k,v in result.items() if k!='policies'}))
