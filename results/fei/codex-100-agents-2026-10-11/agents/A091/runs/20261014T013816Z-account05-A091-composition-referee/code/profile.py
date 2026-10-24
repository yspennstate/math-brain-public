import check as c
from exact import Q,add,entropy,check,interval
import itertools,json,time
START=time.perf_counter();instances=resolved=0
def one(ctrl,cores):
    global instances,resolved
    q,ms,U,R=c.potentials(ctrl,cores);P=c.spec(c.table(ctrl,cores))[1]
    means=tuple(Q(1) if label==0 else ms[label-1] for label in ctrl)
    coeff=c.real_coeff(means);profile=entropy(tuple(a*a for a in coeff))
    for j,p in enumerate(q):
        if p:
            coeff=c.real_coeff(tuple(Q(label==j+1) for label in ctrl));norm=tuple(a*a/p for a in coeff)
            check(sum(norm),Q(1));profile=add((1,profile),(p*(1-ms[j]**2),entropy(norm)))
    check(add((1,entropy(P)),(-1,U),(-1,R)),profile)
    if len(set(ctrl))==1:
        j=ctrl[0];m=Q(1) if not j else ms[j-1];V=1-m*m
        check(profile,c.eta(m*m));c.bounded(profile,c.CI,V);c.bounded(profile,c.CI,c.e.inf(P));resolved+=1
    instances+=1
def root(ctrl,cores):
    one(ctrl,cores)
    for i in range(c.dim(ctrl)):
        for b in range(2):one(*c.restrict(ctrl,cores,'control',0,i,b))
    for j,t in enumerate(cores):
        for i in range(c.dim(t)):
            for b in range(2):one(*c.restrict(ctrl,cores,'data',j,i,b))
    if time.perf_counter()-START>110:raise RuntimeError('frozen profile watchdog')
for ctrl in itertools.product(range(3),repeat=4):
    for i in range(4):
        for j in range(4):root(ctrl,(c.e.tab(i,1),c.e.tab(j,1)))
for n in range(4):
    for mask in range(1<<(1<<n)):
        for r in [1,2,3]:root(tuple(1 if z==0 else 0 for z in range(1<<r)),(c.e.tab(mask,n),))
assert instances==20658
out={'status':'PASS','root_and_first_face_instances':instances,'controller_resolved_instances':resolved,'counted_exact_assertions':c.e.COUNT,'runtime_seconds':time.perf_counter()-START,'scope':'H-U-R profile identity exact at all dimension by proof; terminal price <=I_leaf/ln2 only at controller-resolved leaves, not arbitrary frontiers.'}
(c.R/'out/PROFILE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
