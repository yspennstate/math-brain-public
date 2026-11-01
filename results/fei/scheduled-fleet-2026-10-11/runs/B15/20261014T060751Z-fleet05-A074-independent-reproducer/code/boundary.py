"""Two current positive-curvature witnesses, binary polynomial representation."""
from fractions import Fraction as F
from pathlib import Path
import time,json,sys
import verify as v
a=v.a;R=v.R;check=a.check
def centered(c,ps):
    b=c.copy()
    for i,p in enumerate(ps):
        for s in range(len(b)):
            if not s>>i&1:b[s]+=p*b[s|(1<<i)]
    return b
def masses(c,ps):
    b=centered(c,ps);mu=[]
    for s,x in enumerate(b):
        w=F(1)
        for i,p in enumerate(ps):
            if s>>i&1:w*=p*(1-p)
        mu.append(x*x*w)
    return mu
def core(table):
    w,mu,ds,B,H=v.spectral(table)
    return {'p':F(sum(x<0 for x in table),len(table)),'H':H,'I':sum(ds),'ds':ds}
def profile(cores):
    ps=[g['p'] for g in cores];mu=masses(v.C,ps);check(sum(mu)==1)
    qs=[]
    for j in range(6):
        inds=[i for i in range(6) if i!=j];physical=F(0);der=[]
        for z in range(32):
            x=sum(((z>>k)&1)<<i for k,i in enumerate(inds));d=F(v.J[x]-v.J[x|(1<<j)],2);der.append(d)
            weight=F(1)
            for k,i in enumerate(inds):weight*=ps[i] if z>>k&1 else 1-ps[i]
            physical+=d*d*weight
        spectral=sum(masses(a.mobius(der),[ps[i] for i in inds]));check(spectral==physical)
        check(sum(mu[s] for s in range(64) if s>>j&1)==4*ps[j]*(1-ps[j])*physical)
        qs.append(physical)
    C=a.entropy(mu);H=(F(0),F(0));I=F(0)
    for j,g in enumerate(cores):
        C=a.sub(C,a.mul(a.entropy([4*ps[j]*(1-ps[j]),(1-2*ps[j])**2]),qs[j]))
        H=a.add(H,a.mul(g['H'],qs[j]));I+=qs[j]*g['I']
    return {'ps':ps,'qs':qs,'C':C,'H':a.add(H,C),'I':I}
def case(i):
    table=[-1 if x in {0,1,2} else 1 for x in range(64)]
    parent=core(table);children=[]
    for bit in [0,1]:
        child=[]
        inds=[k for k in range(6) if k!=i]
        for z in range(32):
            x=(bit<<i)+sum(((z>>k)&1)<<j for k,j in enumerate(inds));child.append(table[x])
        children.append(core(child))
    P=profile([parent]*6);K=[]
    for child in children:K.append(profile([child]+[parent]*5))
    for j in range(6):check((K[0]['qs'][j]+K[1]['qs'][j])/2==P['qs'][j])
    check(K[0]['qs'][0]==K[1]['qs'][0]==P['qs'][0])
    dc=a.sub(P['C'],a.mul(a.add(K[0]['C'],K[1]['C']),F(1,2)))
    dh=a.sub(P['H'],a.mul(a.add(K[0]['H'],K[1]['H']),F(1,2)))
    innerdh=a.sub(parent['H'],a.mul(a.add(children[0]['H'],children[1]['H']),F(1,2)))
    identity=a.sub(dh,a.add(a.mul(innerdh,P['qs'][0]),dc));check(identity[0]<=0<=identity[1])
    edge=P['qs'][0]*parent['ds'][i]
    # Independently sum all32 inner fibers times all32 other-outer assignments.
    inds=[k for k in range(6) if k!=i];physical=F(0)
    for z in range(32):
        x=sum(((z>>k)&1)<<j for k,j in enumerate(inds))
        if table[x]==table[x|(1<<i)]:continue
        for outer in range(32):
            y=outer<<1;p=parent['p'];weight=p**outer.bit_count()*(1-p)**(5-outer.bit_count())
            if v.J[y]!=v.J[y|1]:physical+=weight/F(32)
    check(physical==edge)
    check(P['I']-(K[0]['I']+K[1]['I'])/2==edge)
    excess=a.sub(dh,(4*edge,4*edge));check(dc[0]>0);check(excess[0]>0)
    if i==2:check(children[1]['p']==0);check(children[1]['H']==(0,0));check(children[1]['I']==0)
    return v.encode({'gate':'J','block':0,'inner_coordinate':i,'core_negative_set':[0,1,2],'parent_bits':36,'child_bits':35,'parent':P,'children':K,'inner_parent':parent,'inner_children':children,'DeltaC':dc,'DeltaH':dh,'physical_influence':edge,'DeltaH_minus4Inf':excess,'identity_residual':identity,'status':'PASS'})
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv;rows=[]
    for i in ([2] if pilot else [0,2]):
        rows.append(case(i));v.save('BOUNDARY_PILOT_PARTIAL.json' if pilot else 'BOUNDARY_PARTIAL.json',rows)
    out={'status':'PASS','pilot':pilot,'checks':a.CHECKS,'runtime_seconds':time.perf_counter()-start,'rows':rows,'independence':'Unequal-bias binary Moebius coefficients without division by variance; physical fibers and outer assignments counted separately; no source code/output premises'}
    v.save('BOUNDARY_PILOT.json' if pilot else 'BOUNDARY_VALIDATION.json',out)
    print(json.dumps({k:x for k,x in out.items() if k!='rows'}))
if __name__=='__main__':main()
