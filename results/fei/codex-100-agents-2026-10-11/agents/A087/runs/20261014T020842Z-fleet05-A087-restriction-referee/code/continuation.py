import sys,itertools,json,time,hashlib
from functools import lru_cache
from fractions import Fraction as Q
import exact as e
checks=0
def require(ok):
    global checks
    checks+=1;assert ok
def avg(a,b):return e.scale(e.add(a,b),Q(1,2))
def function(labels,u,v):
    nc=e.dimension(labels);mask=len(labels)-1
    return tuple(1 if labels[z&mask]==0 else u[(z>>nc)&(len(u)-1)] if labels[z&mask]==1 else v[z>>(nc+e.dimension(u))] for z in range(len(labels)*len(u)*len(v)))
def bank(labels,u,v):
    out=()
    for j,h in ((1,u),(2,v)):
        q=Q(labels.count(j),len(labels));out=e.add(out,e.scale(e.phi(q),1-e.walsh(h)[0]**2))
    return out
def inner(labels,u,v):
    return e.add(*(e.scale(e.add(e.entropy(h),e.scale(e.phi(e.walsh(h)[0]**2),-1)),Q(labels.count(j),len(labels))) for j,h in ((1,u),(2,v))))
@lru_cache(None)
def tree(labels,u,v):
    f=function(labels,u,v);R=bank(labels,u,v)
    if len(set(labels))==1:
        G=e.add(e.entropy(f),e.scale(inner(labels,u,v),-1),e.scale(R,-1));ii=sum(e.inf(f,k) for k in range(e.dimension(f)))
        require(not G or e.log_bounds(G)[0]>=0);require(e.log_bounds(G)[1]<=ii)
        return (),Q(0),e.entropy(f),G
    lc=e.child(labels,0,0);rc=e.child(labels,0,1)
    release=e.add(R,e.scale(avg(bank(lc,u,v),bank(rc,u,v)),-1))
    require(not release or e.log_bounds(release)[0]>=0)
    D=e.decrement(f,0);res=e.add(D,e.scale(release,-1));d=e.inf(f,0)
    # X then A then B: every still-unresolved reveal is one-sided or independent.
    lo,hi=e.log_bounds(res);require(not res or lo>=0);require(hi<=4*d*e.ln_interval(2)[0]+2*d)
    a=tree(lc,u,v);b=tree(rc,u,v)
    total=e.add(res,avg(a[0],b[0]));spent=d+(a[1]+b[1])/2;terminal=avg(a[2],b[2]);profile=avg(a[3],b[3])
    require(e.add(total,R,terminal)==e.entropy(f))
    return total,spent,terminal,profile
def labels(o):
    return tuple(1 if z&1==0 and (z>>1)&1==0 else 2 if z&1==o and (z>>2)&1==0 else 0 for z in range(8))
def run(pilot):
    start=time.monotonic();allh=[tuple(x) for n in range(3) for x in itertools.product((-1,1),repeat=1<<n)];roots=0
    for u,v,o in itertools.product(allh,allh,(0,1)):
        ll=labels(o);f=function(ll,u,v);res,spent,terminal,profile=tree(ll,u,v)
        require(spent==sum(e.inf(f,i) for i in range(3)))
        require(e.log_bounds(res)[1]<=4*spent*e.ln_interval(2)[0]+2*spent)
        leafI=Q(ll.count(1),8)*sum(e.inf(u,i) for i in range(e.dimension(u)))+Q(ll.count(2),8)*sum(e.inf(v,i) for i in range(e.dimension(v)))
        require(e.log_bounds(profile)[1]<=leafI)
        roots+=1
        if time.monotonic()-start>(55 if pilot else 120):raise RuntimeError('frozen runtime reached')
        if pilot and roots==8:break
    guards=0
    if not pilot:
        for h in allh:
            if abs(e.walsh(h)[0])==1:continue
            # Same physical core on both children: X is actually irrelevant.
            f=tuple(h[z>>1] for z in range(2*len(h)))
            require(e.inf(f,0)==0);require(e.decrement(f,0)==());require((1-e.walsh(h)[0]**2)/2>0);guards+=1
    out={'status':'PASS','controller_continuation_roots':roots,'distinct_actual_tree_states':tree.cache_info().currsize,'same_core_scope_guards':guards,'exact_assertions':checks,'seconds':time.monotonic()-start,'helper_sha256':hashlib.sha256(e.Path(__file__).read_bytes()).hexdigest(),'scope':'Actual X,A,B controller-resolving frontier; arbitrary cores retained, terminal profile paid at I_leaf/ln2'}
    (e.ROOT/'out'/('CONTINUATION_PILOT.json' if pilot else 'CONTINUATION_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':run(sys.argv[1]=='pilot')
