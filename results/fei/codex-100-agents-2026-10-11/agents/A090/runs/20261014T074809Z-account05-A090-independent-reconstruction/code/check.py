import json, time, sys
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).resolve().parents[1]
checks=0
def ck(v):
    global checks
    assert v
    checks+=1
def walsh(v):
    a=v[:]; s=1
    while s<len(a):
        for j in range(0,len(a),2*s):
            for k in range(j,j+s):
                u,v=a[k],a[k+s]; a[k],a[k+s]=u+v,u-v
        s*=2
    return a
def bent(y,d):
    return (-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))
def gate(x,r):
    return (-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(r))
def physical(d,r):
    ny=1<<d; nx=1<<(2*r); n=d+2*r
    delta=Q(1,ny); t=Q(1,1<<(d//2)); alpha=Q(1,1<<r)
    w=Q(1,4**(r-1)); e=delta/2; A=1-delta+2*delta*alpha**2
    bb=[bent(y,d) for y in range(ny)]; bw=walsh(bb)
    sigma=[int(Q(z,ny)/t) for z in bw]
    gg=[gate(x,r) for x in range(nx)]; gw=walsh(gg)
    ag=[Q(z,nx) for z in gw]; ck(all(abs(z)==alpha for z in ag))
    truth=[gg[x] if y==0 else bb[y] for x in range(nx) for y in range(ny)]
    fhat=[Q(z,ny*nx) for z in walsh(truth)]; p=[z*z for z in fhat]
    ck(sum(p)==1); ck(all(z>0 for z in p))
    for x in range(nx):
        for y in range(ny):
            ck(fhat[x*ny+y]==(sigma[y]*t if x==0 else 0)+delta*(ag[x]-(1 if x==0 else 0)))
    influence=[]
    for j in range(n):
        z=Q(sum(truth[k]!=truth[k^(1<<j)] for k in range(ny*nx)),ny*nx)
        ck(z==sum(p[k] for k in range(ny*nx) if k&(1<<j)))
        ck(z==(Q(1,2)+delta*(1-alpha) if j<d else e))
        influence.append(z)
    tail=sum(p[x*ny+y] for x in range(1,nx) for y in range(ny))
    ck(tail==delta*(1-alpha**2))
    # Sufficient entropy upper certificate H<=d+1+2r delta<=4I.
    ck(d+1+2*r*delta<=4*sum(influence))
    for j in range(2*r):
        bit=1<<j; partner=1<<(j^1); mus=[Q(0)]*4; refs=[Q(0)]*4
        rows=[]
        for x in range(nx):
            if x&bit: continue
            idx=(2 if x&partner else 0)+(1 if x&~partner else 0)
            for y in range(ny):
                lower=p[x*ny+y]; upper=p[(x|bit)*ny+y]
                mu=upper/e; ref=lower+upper
                mus[idx]+=mu; refs[idx]+=ref
                rows.append((x,y,idx,mu,ref))
        ck(mus==[w/2,(1-w)/2,w/2,(1-w)/2])
        ck(refs==[A,e*(1-w),e*w,e*(1-w)])
        ck(sum(mus)==sum(refs)==1)
        binary_mu=[mus[0]+mus[1],mus[2]+mus[3]]
        binary_ref=[refs[0]+refs[1],refs[2]+refs[3]]
        ck(binary_mu==[Q(1,2),Q(1,2)])
        ck(binary_ref==[1-e,e])
        for x,y,idx,mu,ref in rows:
            if idx==0:
                R=1+2*sigma[y]*t*(alpha-1)+delta*((alpha-1)**2+alpha**2)
                ck(mu/mus[0]==delta); ck(ref/refs[0]==delta*R/A)
            else:
                ck(mu/ref==mus[idx]/refs[idx])
        # Full row normalizer must include lower mass, not derivative support alone.
        ck(sum(ref for _,_,_,_,ref in rows)==1)
        ck(sum(p[(x|bit)*ny+y] for x in range(nx) if not x&bit for y in range(ny))==e)
    return n
def symbolic(d,r):
    delta=Q(1,1<<d); t=Q(1,1<<(d//2)); alpha=Q(1,1<<r); w=Q(1,4**(r-1))
    a=Q(1,2)+delta*(1-alpha); J=r*delta; Ic=d*a
    A=1-delta+2*delta*alpha**2
    Rplus=(1+t*(alpha-1))**2+delta*alpha**2
    Rminus=(-1+t*(alpha-1))**2+delta*alpha**2
    ck(3*Rplus-A==2*(1-t)*(1-2*t)+6*t*(1-t)*alpha+4*t*t*alpha*alpha)
    ck(A/Rplus<=3); ck(Rminus>=Rplus); ck(A/Rminus<=3)
    ck(d*delta<=Q(1,2)); ck(r*w*(2*r+3)<=5)
    upper=r*delta*w*(d+2*r+1)/2
    ck(upper<=Q(5,8)); ck(upper<Q(3,2)*a)
    ck(2*Ic+3*J+upper<Q(7,2)*(Ic+J))
    ck(d+1+2*r*delta<=4*(Ic+J))
    if r>=2:
        ck(w<=Q(1,4)); ck(w*(2*r-1)<=Q(3,4))
        ck(r*delta*Q(1,2)*((1-w)*d-w*(2*r-1))>=r*delta*(Q(3,8)*d-Q(1,2)))
start=time.perf_counter(); pilot='--pilot' in sys.argv
dom=[(2,1),(2,2)] if pilot else [(2,1),(2,2),(2,3),(4,1),(4,2),(4,3),(6,1),(6,2)]
maxn=max(physical(d,r) for d,r in dom)
sym=0
if not pilot:
    for d in range(2,33,2):
        for r in range(1,65): symbolic(d,r); sym+=1
result={'status':'PASS','physical_cases':len(dom),'symbolic_cases':sym,'exact_assertions':checks,'maximum_physical_dimension':maxn,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh and Fraction; no floating sign claims'}
(root/'out'/('pilot.json' if pilot else 'check.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
