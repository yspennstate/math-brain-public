"""Independent controller-shape tree reconstruction, direct characters only."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
import independent_base as b
R=Path(__file__).resolve().parents[1];START=time.monotonic()
nodes=leaves=0;positive_shape_nodes=0;nonzero_vacuum_nodes=0

def state(a,g,h,ra,rg,rh):
    global positive_shape_nodes,nonzero_vacuum_nodes
    pg,ph,pa=b.law(g),b.law(h),b.law(a)
    p=Q(a.count(-1),len(a));V=1-pa[0];beta=1-ra[0]
    gamma=Q(sum(x!=y for x,y in zip(g,h)),len(g))
    f=tuple((g if y==1 else h)[x] for x in range(len(g)) for y in a)
    pf=b.law(f);q=[];r=[];ref=[]
    for t in range(len(g)):
        row=pf[t*len(a):(t+1)*len(a)];qt=sum(row);rt=(1-p)*rg[t]+p*rh[t]
        b.ck(qt==(1-p)*pg[t]+p*ph[t]);q.append(qt);r.append(rt)
        non=sum(row[1:])
        for u in range(1,len(a)):
            b.ck(row[u]*V==non*pa[u])
        ref.append(rt*row[0]/qt if qt else rt)
        ref.extend(rt*non/qt*x/beta if qt and non else Q() for x in ra[1:])
    debt=b.D(pf,tuple(ref));data=b.D(tuple(q),tuple(r))
    Da=b.D(pa,ra);vac=b.D((1-V,V),(1-beta,beta))
    shape=b.D(tuple(x/V for x in pa[1:]),tuple(x/beta for x in ra[1:])) if V else {}
    W=b.add(b.mul(b.D(pg,rg),1-p),b.mul(b.D(ph,rh),p))
    Z=b.difference(W,data);T=b.add(W,b.mul(Da,gamma));S=b.add(Z,b.mul(vac,gamma))
    delta=b.mul(shape,V*gamma)
    b.ck(not b.difference(Da,b.add(vac,b.mul(shape,V))))
    b.ck(not b.difference(debt,b.add(data,delta)))
    b.ck(not b.difference(debt,b.difference(T,S)))
    if delta:positive_shape_nodes+=1
    if b.mul(vac,gamma):nonzero_vacuum_nodes+=1
    return dict(debt=debt,T=T,S=S,H=b.H(pf),ref=tuple(ref),f=f,p=p,gamma=gamma,delta=delta,vac=vac,Da=Da)

def walk(args,labels,order,history,adaptive):
    global nodes,leaves
    nodes+=1;s=state(*args);a,g,h,ra,rg,rh=args
    if not labels or (adaptive and len(history)>=3 and sum(history)%2==0):
        leaves+=1
        return dict(sig={},A={},Sleaf=s['S'],path={},ce=b.add(s['H'],s['debt']))
    priorities=tuple(reversed(order)) if adaptive and sum(history)%2 else order
    label=next(x for x in priorities if x in labels);i=labels.index(label)
    na=len(a).bit_length()-1
    inherited,Ef,Of=b.joint(s['f'],s['ref'],i)
    if i<na:
        raa,Ea,Oa=b.joint(a,ra,i)
        argschild=[(b.child(a,i,k),g,h,raa[k],rg,rh) for k in [0,1]]
        release=b.mul(b.add(Ea,Oa),s['gamma'])
    else:
        j=i-na;rgg,Eg,Og=b.joint(g,rg,j);rhh,Eh,Oh=b.joint(h,rh,j)
        argschild=[(a,b.child(g,j,k),b.child(h,j,k),ra,rgg[k],rhh[k]) for k in [0,1]]
        release=b.add(b.mul(b.add(Eg,Og),1-s['p']),b.mul(b.add(Eh,Oh),s['p']))
    kids=[state(*ar) for ar in argschild]
    A=b.difference(s['T'],b.mean(*(z['T'] for z in kids)))
    b.ck(not b.difference(A,release))
    sigma=b.difference(b.mean(*(z['debt'] for z in kids)),s['debt'])
    b.ck(not b.difference(sigma,b.add(s['S'],b.mul(b.mean(*(z['S'] for z in kids)),-1),b.mul(A,-1))))
    raw=b.difference(b.mean(*(z['debt'] for z in kids)),b.mean(*(b.D(b.law(b.child(s['f'],i,k)),inherited[k]) for k in [0,1])))
    b.ck(not b.difference(raw,b.add(sigma,Ef,Of)))
    if i>=na:b.ck((kids[0]['gamma']+kids[1]['gamma'])/2==s['gamma'])
    remain=labels[:i]+labels[i+1:]
    ret=[walk(argschild[k],remain,order,history+(k,),adaptive) for k in [0,1]]
    out={name:b.mean(*(z[name] for z in ret)) for name in ret[0]}
    out['sig']=b.add(sigma,out['sig']);out['A']=b.add(A,out['A'])
    out['path']=b.add(b.difference(s['H'],b.mean(*(z['H'] for z in kids))),out['path'])
    b.ck(not b.difference(b.add(out['sig'],out['A'],out['Sleaf']),s['S']))
    b.ck(not b.difference(b.add(out['path'],out['ce'],out['A'],out['Sleaf']),b.add(s['H'],s['T'])))
    return out

a=tuple(-1 if x<3 else 1 for x in range(8))
g=tuple((-1 if x&3==0 else 1)*(-1 if x&4 else 1) for x in range(8))
h=tuple(-1 if x.bit_count()>=2 else 1 for x in range(8))
V=1-b.law(a)[0];ra=(1-V,)+tuple(V*Q(x,28) for x in range(1,8))
rg=tuple((x+Q(1,8))/2 for x in b.law(g));rh=tuple(Q(1,8) for _ in h)
labels=('C0','C1','C2','D0','D1','D2');order=('C0','D0','C1','D1','C2','D2')
results=[]
for adaptive in [False,True]:
    initial=(nodes,leaves,b.checks)
    out=walk((a,g,h,ra,rg,rh),labels,order,(),adaptive)
    results.append(dict(adaptive=adaptive,nodes=nodes-initial[0],leaves=leaves-initial[1],assertions=b.checks-initial[2],ledger={k:{str(x):str(y) for x,y in z.items()} for k,z in out.items()}))
assert nodes<=254 and positive_shape_nodes and nonzero_vacuum_nodes
out=dict(status='PASS',nodes=nodes,leaves=leaves,assertions=b.checks,seconds=time.monotonic()-START,positive_shape_node_visits=positive_shape_nodes,nonzero_vacuum_node_visits=nonzero_vacuum_nodes,policies=results,representation='direct character sums; independent conditional KL expansion; no main/helper import')
(R/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:v for k,v in out.items() if k!='policies'}))
