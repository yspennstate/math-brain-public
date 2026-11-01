from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, sys
RUN=Path(__file__).resolve().parents[1]
START=time.monotonic(); assertions=0
def ck(b):
    global assertions
    assertions+=1
    assert b
    if assertions%1000==0: assert time.monotonic()-START<55
@lru_cache(None)
def ln(q):
    q=F(q); assert q>0
    k=0
    while q>=2:q/=2;k+=1
    while q<1:q*=2;k-=1
    def base(t):
        z=(t-1)/(t+1); v=sum((z**(2*i+1)/F(2*i+1) for i in range(18)),F(0))*2
        return v,v+2*z**37/(37*(1-z*z))
    lo,hi=base(q); a,b=base(F(2))
    lo,hi=(lo+k*a,hi+k*b) if k>=0 else (lo+k*b,hi+k*a)
    # Outward rounding keeps CE sums on one grid, avoiding denominator explosion.
    grid=1<<96
    return F((lo*grid).__floor__(),grid),F((hi*grid).__ceil__(),grid)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def ce(p,q):
    z=(F(0),F(0))
    for v,w in zip(p,q):
        if v:z=add(z,scale(ln(w),-v))
    return z
def kl(p,q):return sub(ce(p,q),ce(p,p))
def walsh(v):
    a=list(map(F,v)); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for i in range(j,j+step):a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
        step*=2
    return [x/len(a) for x in a]
def delete_mask(t,j):return (t&((1<<j)-1))|((t>>(j+1))<<j)
def marginal(v,j):
    z=[F(0)]*(len(v)//2)
    for t,x in enumerate(v):z[delete_mask(t,j)]+=x
    return z
def child(v,j,s):return [v[(t&((1<<j)-1))|((t>>j)<<(j+1))|(s<<j)] for t in range(len(v)//2)]
CONT=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
def wrapper(a,p,m,sgn):
    aa=walsh(a);bb=walsh([1-x*x for x in a])
    return [(aa[u]+sgn*m*bb[u])**2 if t==0 else bb[u]**2*p[t] for u in range(len(a)) for t in range(len(p))]
def run(pilot):
    n=2 if pilot else 3; N=1<<n; count=0;positive=0;ghosts=0;zero=0;energy=0
    shard=int(sys.argv[sys.argv.index('--shard')+1]) if '--shard' in sys.argv else None
    tables=[30,225,105,150] if '--witness' in sys.argv else (range(1<<N) if shard is None else range(64*shard,64*(shard+1)))
    for tab in tables:
        v=[1 if tab>>i&1 else -1 for i in range(N)];f=walsh(v);p=[x*x for x in f];m=f[0]
        ck(sum(p)==1)
        # Independent physical pivotal counts, not a Fourier-side duplicate.
        for j in range(n):ck(sum(p[t] for t in range(N) if t>>j&1)==F(sum(v[i]!=v[i^(1<<j)] for i in range(N)),N))
        refs=[p]
        den=sum(range(2,N+1)); refs.append([m*m]+[(1-m*m)*F(t+1,den) for t in range(1,N)])
        for j in range(n):
            ind=[t for t in range(N) if not t>>j&1]; u=[f[t] for t in ind];w=[f[t|(1<<j)] for t in ind]
            # Two sign bins on remaining NONEMPTY labels, fixed before physical outcome.
            bins=[[t for t in range(1,N//2) if u[t]*w[t]>=0],[t for t in range(1,N//2) if u[t]*w[t]<0]]
            bins=[b for b in bins if b]; cs=[sum((u[t]*w[t] for t in b),F(0)) for b in bins]
            ck(sum((u[t]*w[t] for t in range(N//2)),F(0))==0)
            # All three-bin partitions for n=3: sign bins achieve maximal squared sum.
            if n==3:
                import itertools
                for labels in itertools.product(range(3),repeat=3):
                    val=sum((sum((u[t]*w[t] for t in range(1,4) if labels[t-1]==k),F(0))**2 for k in range(3)),F(0))
                    ck(val<=sum((c*c for c in cs),F(0)))
            for R in refs:
                for sgn in [-1,1]:
                    a=CONT;A=walsh(a);B=walsh([1-t*t for t in a]);beta=sum(b*b for b in B)
                    C=sum(A[i]**2*B[i]**2 for i in range(16));D=sum(A[i]*B[i]**3 for i in range(16));E=sum(b**4 for b in B);gamma=C-D*D/E
                    ck((beta,E,gamma)==(F(3,8),F(21,512),F(9,3584)))
                    x=gamma*w[0]**2+E*sum((c*c for c in cs),F(0));count+=1
                    energy+=x>0;zero+=x==0
                    if w[0]==0:ck((x>0)==any(u[t]*w[t] for t in range(1,N//2)))
                    P=wrapper(a,p,m,sgn);Q=wrapper(a,R,m,sgn);N2=N//2
                    pb=[];qb=[]
                    for k in range(16):pb+=marginal(P[k*N:(k+1)*N],j);qb+=marginal(Q[k*N:(k+1)*N],j)
                    ck(sum(Q)==sum(qb)==1)
                    ghosts+=sum(1 for v0,q0 in zip(P,Q) if not v0 and q0)
                    # Compute erasure as physical frequency-fiber binary entropy.
                    er=(F(0),F(0));occ=(F(0),F(0))
                    for k in range(16):
                        for t in ind:
                            z0=k*N+t;z1=z0+(1<<j);s=P[z0]+P[z1];r=Q[z0]+Q[z1]
                            if s:
                                pp=[P[z0]/s,P[z1]/s];qq=[Q[z0]/r,Q[z1]/r]
                                er=add(er,scale(ce(pp,pp),s));occ=add(occ,scale(kl(pp,qq),s))
                    avg=(F(0),F(0));rho=(F(0),F(0));mix=(F(0),F(0))
                    for s in [0,1]:
                        cv=child(v,j,s);cf=walsh(cv);cp=[z*z for z in cf];cm=cf[0];rr=marginal(R,j)
                        cal=[cm*cm]+[F(0)]*(N2-1)
                        for b in bins:
                            pp=sum(cp[t] for t in b);qq=sum(rr[t] for t in b)
                            if pp:
                                ck(qq>0)
                                for t in b:cal[t]=pp*rr[t]/qq
                        pc=wrapper(a,cp,cm,sgn);qc=wrapper(a,cal,cm,sgn)
                        ck(sum(qc)==sum(cal)==1)
                        groups=[[k*N2] for k in range(16)]+[[k*N2+t for t in b] for k in range(16) for b in bins]
                        pcg=[sum(pc[t] for t in b) for b in groups];qbg=[sum(qb[t] for t in b) for b in groups]
                        # Verify block calibration on EVERY atom, including ghosts.
                        for b,pp,qq in zip(groups,pcg,qbg):
                            for t in b:ck(qc[t]==(pp*qb[t]/qq if pp else 0))
                        rho=add(rho,scale(kl(pcg,qbg),F(1,2)))
                        tail=beta*(1-cm*cm);eps=x/(tail+x) if x and tail else F(0)
                        target=next((t for t in range(1,N2) if cp[t]==0),1)
                        new=list(cal)
                        if eps:
                            for t in range(1,N2):new[t]=(1-eps)*cal[t]+eps*(1-cm*cm)*(t==target)
                        qn=wrapper(a,new,cm,sgn);z=sub(ce(pc,qn),ce(pc,qc))
                        if z[0]>0:positive+=1
                        ck(z[1]<=x or (not x and z[0]<=0<=z[1]))
                        mix=add(mix,scale(z,F(1,2)));avg=add(avg,scale(ce(pc,qn),F(1,2)))
                    ck(rho[0]>=2*x or not x)
                    inc=sub(add(er,avg),ce(P,Q));bound=add(inc,occ)
                    ck(bound[1]<=-x or (not x and bound[0]<=0<=bound[1]))
                    ck(occ[1]>=0)
    result={'mode':'pilot' if pilot else 'full','shard':shard,'seed_bits':n,'truth_tables':len(tables),'transactions':count,'assertions':assertions,'positive_signed_child_changes':positive,'positive_energy_transactions':energy,'zero_energy_transactions':zero,'reference_only_parent_atoms_seen':ghosts,'elapsed_seconds':time.monotonic()-START,'arithmetic':'Fraction; 18-term atanh log intervals; natural-unit theorem; no floats in decisions','verdict':'PASS'}
    filename='PILOT.json' if pilot else ('WITNESS.json' if '--witness' in sys.argv else ('VALIDATION.json' if shard is None else 'VALIDATION_'+str(shard)+'.json'))
    (RUN/'out'/filename).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
