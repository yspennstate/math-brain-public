from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time
R=Path(__file__).resolve().parents[1]
p=R/'code/check.py';raw=p.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='b216ed7ca44fcc3e44f8d26b57323b244b762da07b6fa32f2dfddda1a1fbff12'
# Reuse explicitly pinned own definitions only; do not execute a different test mode.
ns={'__file__':str(p),'__name__':'pinned_A011_primitives'}
exec(compile(raw.decode('utf-8').split('\nans=scalar()')[0],str(p),'exec'),ns)
ns['LIMIT']=55
ck=ns['ck'];sp=ns['spectrum'];inherit=ns['inherit'];div=ns['div'];add=ns['add'];sub=ns['sub'];mul=ns['mul'];overlap=ns['overlap'];zero=ns['ZERO']
nodes=calibrations=ghosts=0
def erase(w,i):return (w&((1<<i)-1))|((w>>(i+1))<<i)
def representation(p,q,beta,labels):
    z=[beta*x for x in p]
    for mask,c in labels:z[mask]+=c
    ck(z==q);ck(beta>0 and beta<=1);ck(all(c>=0 for _,c in labels));ck(sum(q)==1)
def walk(tab,Q,beta,labels,depth,slot):
    global nodes,calibrations,ghosts
    nodes+=1;p=sp(tab);n=(len(tab)-1).bit_length();s=sum(Q)
    representation(p,[x/s for x in Q],beta,labels)
    ghosts+=sum(c>0 and p[w]==0 for w,c in labels)
    if n==0:return zero,zero,div(p,Q)
    i=(depth+sum(x<0 for x in tab))%n
    tabs,ps,qs,delta,zs=inherit(tab,Q,i)
    pairs=ns['pair_indices'](n,i);m=[p[a]+p[b] for a,b in pairs]
    es=zero;ql=delta;ds=zero
    for bit in range(2):
        pb=ps[bit];qold=[x/s for x in qs[bit]];out=zs[bit]/(2*s)
        bb=beta/(2*out);ls=[]
        for w,c in labels:
            u=erase(w,i);k=pb[u]/(2*m[u]) if m[u] else F(1,2)
            ls.append((u,c*k/out))
        representation(pb,qold,bb,ls)
        rr,zz=pb[0],qold[0]
        if rr==1:
            new=pb[:];bb=F(1);ls=[(w,F(0)) for w,c in ls]
        else:
            ck(zz<1);v=(1-rr)/(1-zz);new=[rr]+[v*x for x in qold[1:]];bb*=v
            ls=[(w,c*v if w else F(0)) for w,c in ls]
            # slot is a single persistent reserved empty label, never appended again.
            ls[slot]=(0,rr*(1-bb))
        representation(pb,new,bb,ls);ck(len(ls)==len(labels))
        Qnew=[s*x for x in new];ck(sum(Qnew)==s)
        change=sub(div(pb,Qnew),div(pb,qs[bit]))
        bern=div([rr,1-rr],[zz,1-zz]);ck(overlap(change,mul(-1,bern)))
        calibrations+=1
        e,l,d=walk(tabs[bit],Qnew,bb,ls,depth+1,slot)
        es=add(es,mul(F(1,2),add(change,e)));ql=add(ql,mul(F(1,2),l));ds=add(ds,mul(F(1,2),d))
    ck(overlap(div(p,Q),add(sub(ds,es),ql)))
    return es,ql,ds
sources=trees=0
for n in range(4):
    for label in range(1<<(1<<n)):
        tab=[-1 if label>>j&1 else 1 for j in range(1<<n)];p=sp(tab);u=F(1,len(p));sources+=1
        for Q in [p,[x/2 for x in p],[(x+u)/6 for x in p]]:
            s=sum(Q);q=[x/s for x in Q];beta=min(y/x for x,y in zip(p,q) if x)/2
            ls=[(w,y-beta*x) for w,(x,y) in enumerate(zip(p,q))]+[(0,F(0))]
            e,l,d=walk(tab,Q,beta,ls,0,len(p));trees+=1
            ck(overlap(div(p,Q),add(sub(d,e),l)))
ans={'status':'PASS','sources':sources,'complete_trees':trees,'tree_nodes':nodes,'calibrations':calibrations,'ghost_slots_observed':ghosts,'assertions':ns['COUNT'],'seconds':time.monotonic()-ns['START'],'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'primitive_sha256':hashlib.sha256(raw).hexdigest()}
(R/'out/CALIBRATION.json').write_text(json.dumps(ans,indent=2),encoding='utf-8');print(json.dumps(ans))
