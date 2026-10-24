import json, sys, time
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).resolve().parents[1]
checks=0
def ck(v):
    global checks
    assert v
    checks+=1
def walsh(v):
    a=v[:]; step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):
                x,y=a[k],a[k+step]; a[k],a[k+step]=x+y,x-y
        step*=2
    return a
def bent(y,d):
    return (-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))
def case(d,r,table):
    ny=1<<d; nx=1<<r; delta=Q(1,ny); t=Q(1,1<<(d//2))
    g=[1 if (table>>x)&1 else -1 for x in range(nx)]
    ag=[Q(a,nx) for a in walsh(g)]
    b=[bent(y,d) for y in range(ny)]; bw=walsh(b)
    sig=[int(Q(a,ny)/t) for a in bw]
    ck(set(sig)=={-1,1}); ck(sum(sig)==1/t)
    truth=[g[x] if y==0 else b[y] for x in range(nx) for y in range(ny)]
    spec=[Q(a,ny*nx) for a in walsh(truth)]; p=[a*a for a in spec]
    ck(sum(p)==1)
    for v in range(nx):
        for y in range(ny):
            ck(spec[v*ny+y]==(sig[y]*t if v==0 else 0)+delta*(ag[v]-(1 if v==0 else 0)))
    for j in range(d):
        e=Q(sum(truth[z]!=truth[z^(1<<j)] for z in range(ny*nx)),ny*nx)
        ck(e==Q(1,2)+delta*(1-ag[0]))
    sum_single=0; unequal=False
    for i in range(r):
        bit=1<<i; eg=sum(ag[v]**2 for v in range(nx) if v&bit)
        ef=sum(p[z] for z in range(ny*nx) if z&(bit*ny))
        ck(ef==delta*eg)
        ck(ef==Q(sum(truth[z]!=truth[z^(bit*ny)] for z in range(ny*nx)),ny*nx))
        sum_single+=ag[bit]**2
        if not eg: continue
        mu={}; ref={}; qm={}; qr={}; vm={}; vr={}
        for v in range(nx):
            if v&bit: continue
            for y in range(ny):
                a=p[v*ny+y]; bb=p[(v|bit)*ny+y]
                key=(v,y); s=(v,sig[y])
                mu[key]=bb/ef; ref[key]=a+bb
                qm[s]=qm.get(s,0)+mu[key]; qr[s]=qr.get(s,0)+ref[key]
                vm[v]=vm.get(v,0)+mu[key]; vr[v]=vr.get(v,0)+ref[key]
        ck(sum(mu.values())==1); ck(sum(ref.values())==1)
        ck(sum(qm.values())==1); ck(sum(qr.values())==1)
        for (v,y),mass in mu.items():
            if mass:
                ck(mass/ref[v,y]==qm[v,sig[y]]/qr[v,sig[y]])
                if v: ck(mass/ref[v,y]==vm[v]/vr[v])
        rho=1-delta+delta*(ag[0]**2+ag[bit]**2)
        ck(vr[0]==rho); ck(vm[0]==ag[bit]**2/eg)
        ck(rho<=1)
        for sigma in (-1,1):
            c=(sigma+t*(ag[0]-1))**2+delta*ag[bit]**2
            ck(c>=Q(1,4)); ck(rho/c<=4)
        if ag[bit]:
            # Conditional reference on the exceptional residual gate cell.
            for y in range(ny):
                c=(sig[y]+t*(ag[0]-1))**2+delta*ag[bit]**2
                ck(ref[0,y]/rho==delta*c/rho)
                ck(mu[0,y]/vm[0]==delta)
            if ag[0]!=1: unequal=True
    ck(sum_single<=1)
    ck(2*delta*sum_single<=Q(1,4)*(Q(1,2)+delta*(1-ag[0])))
    return unequal
start=time.perf_counter(); cases=0; unequal=0
domains=[(4,1),(4,2)] if '--pilot' in sys.argv else [(4,1),(4,2),(4,3),(6,1),(6,2)]
for d,r in domains:
    for table in range(1<<(1<<r)):
        unequal+=case(d,r,table); cases+=1
ck(unequal>0)
result={'status':'PASS','cases':cases,'exact_assertions':checks,'genuine_nonproduct_cases':unequal,'elapsed_seconds':time.perf_counter()-start,'maximum_dimension':max(d+r for d,r in domains),'arithmetic':'integer Walsh and Fraction; no floating sign claims'}
(root/'out'/('pilot.json' if '--pilot' in sys.argv else 'check.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
