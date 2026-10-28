import json,time,sys
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
R=Path(__file__).resolve().parents[1]; checks=0
def ck(b,msg=''):
    global checks
    checks+=1
    if not b: raise AssertionError((checks,msg))
def spectrum(t):
    # Deliberately direct characters rather than the source's butterfly audit.
    return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t))**2,len(t)**2) for s in range(len(t))]
def influence(t):
    return sum((F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(len(t).bit_length()-1)),F(0))
def project(p,keep):
    q=[F(0)]*(1<<len(keep))
    for s,v in enumerate(p):q[sum(((s>>i)&1)<<j for j,i in enumerate(keep))]+=v
    return q
def restriction(t,ass):
    free=[i for i,v in enumerate(ass) if v<0];base=sum(v<<i for i,v in enumerate(ass) if v>=0)
    return [t[base+sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free))],free
@lru_cache(None)
def lnraw(x):
    z=(x-1)/(x+1); zz=z*z;s=F(0);power=z
    for j in range(35):s+=2*power/F(2*j+1);power*=zz
    err=2*power/(71*(1-zz))
    return s,s+err
@lru_cache(None)
def lg(x):
    ck(x>0,'positive log argument');e=0
    while x<1:x*=2;e-=1
    while x>=2:x/=2;e+=1
    a,b=lnraw(x);c,d=lnraw(F(2))
    # outward dyadic rounding keeps repeated row sums small.
    scale=1<<70;lo=F((a/d*scale).__floor__(),scale)+e;hi=F((b/c*scale).__ceil__(),scale)+e
    return lo,hi
def ce(p,q):
    lo=hi=F(0)
    for a,b in zip(p,q):
        if a:
            ck(b>0,'support');l,h=lg(1/b);lo+=a*l;hi+=a*h
    return lo,hi
def ev(x):return (-1 if x&7==0 else 1)*(-1 if x&25==0 else 1)
ORIG=[ev(x) for x in range(32)];OP=spectrum(ORIG)
def blocks(pilot=False):
    rows=[];certs=[]
    asslist=list(product((-1,0,1),repeat=5))
    if pilot:asslist=asslist[:27]
    for ass in asslist:
        t,free=restriction(ORIG,ass)
        essential=[i for i in range(len(free)) if any(t[x]!=t[x^(1<<i)] for x in range(len(t)))]
        keep=[free[i] for i in essential]
        clean=[t[sum(((x>>j)&1)<<i for j,i in enumerate(essential))] for x in range(1<<len(essential))]
        p=spectrum(clean);q=project(OP,keep);I=influence(clean);nu=F(sum(clean),len(clean));D=len(clean)**2
        ck(sum(p)==sum(q)==1);ck(sum(F(s.bit_count())*v for s,v in enumerate(p))==I)
        left=2**int(4*I*D);right=1
        for a,b in zip(p,q):
            if a:
                ck(b>0);ex=int(a*D);left*=b.numerator**ex;right*=b.denominator**ex
        ck(left>=right,'clean source contract')
        rows.append((ass,keep,clean,p,q,I,nu))
        certs.append({'assignment':ass,'keep':keep,'truth':clean,'P':list(map(str,p)),'R':list(map(str,q)),'I':str(I),'left':str(left),'right':str(right)})
    (R/'out/BLOCK_CERTIFICATES.json').write_text(json.dumps(certs,indent=2),encoding='utf-8')
    return rows
def corelaws(P,Q,nu,mu,k,kp):
    rho=F(1,2**k);r=F(1,2**kp);p=rho*(1-mu)/2;a=r*(1-nu)/2
    size=2**(kp+1);actual=[F(0)]*(size*len(P));ref=[F(0)]*len(actual)
    actual[1]=1-2*a;ref[1]=(1-2*p)/2;ref[0]=F(1,2)
    for s in range(len(P)):
        for uv in range(size):
            actual[uv+size*s]+=r*r*(P[s]+(1-2*nu if s==0 else 0))/4
            ref[uv+size*s]+=rho*r*(Q[s]+(1-2*mu if s==0 else 0))/8
    ck(min(actual)>=0 and min(ref)>=0);ck(sum(actual)==sum(ref)==1)
    return actual,ref
def literal(rows,pilot):
    count=0
    selected=rows[:3] if pilot else rows[::12]+[x for x in rows if x[6] in (-1,1)]
    for k in (1,2):
        n=k+7;rho=F(1,2**k);mu=F(5,8)
        parent=[]
        for x in range(1<<n):
            event=((x>>2)&(2**k-1))==0 and ev(x>>(k+2))==-1
            parent.append((-1 if x&1 else 1) if event else (-1 if x&2 else 1))
        # One Walsh transform here; direct characters for all restricted truths.
        w=parent[:];stride=1
        while stride<len(w):
            for b in range(0,len(w),2*stride):
                for i in range(stride):u,v=w[b+i],w[b+i+stride];w[b+i]=u+v;w[b+i+stride]=u-v
            stride*=2
        original=[F(z*z,2*len(w)**2) for z in w];original[1]+=F(1,2)
        for ass,keep,clean,P,Q,I,nu in selected:
            for kp in range(k+1):
                pa=[0]*(k-kp)+[-1]*kp
                retained=[1]+[2+i for i,v in enumerate(pa) if v<0]+[k+2+i for i in keep]
                inherited=project(original,retained)
                formula,formulaQ=corelaws(P,Q,nu,mu,k,kp)
                ck(inherited==formulaQ,'literal ORIGINAL marginal')
                for qb in (0,1):
                    full=[qb,-1]+pa+list(ass)
                    for i in range(5):
                        if full[k+2+i]<0 and i not in keep:full[k+2+i]=0
                    actual,_=restriction(parent,full);pc=spectrum(actual)
                    ck(pc==formula,'literal true core')
                    # Direct outer Boolean edges, including all three spectator bits.
                    outer=[]
                    for x in range(len(actual)*8):
                        gate=x&1;mask=(x>>1)&3;v=actual[x>>3]
                        outer.append(1 if gate==0 else v*(-1 if mask==0 else 1))
                    r=F(1,2**kp);a=r*(1-nu)/2;sigma=1-2*qb
                    ck(4*influence(outer)==6+2*(kp-1)*a+r*I-sigma*a,'physical influence')
                    count+=1
    return count
def rowcost(P,Q,nu,mu,k,kp):
    rho=F(1,2**k);r=F(1,2**kp);p=rho*(1-mu)/2;a=r*(1-nu)/2;N=2/r
    bP=r*r*(1-nu)**2/4;bQ=rho*r*(Q[0]+1-2*mu)/8
    ck(bQ>0)
    pc=[bP,1-2*a+bP];qc=[F(1,2)+bQ,(1-2*p)/2+bQ]
    ck(min(pc)>=0)
    lo,hi=ce(pc,qc)
    if N>2 and bP:
        l,h=lg(1/bQ);lo+=(N-2)*bP*l;hi+=(N-2)*bP*h
    for t in range(1,len(P)):
        if P[t]:
            l,h=lg(8/(rho*r*Q[t]));lo+=r*P[t]*l/2;hi+=r*P[t]*h/2
    source=ce(P,Q)
    ck(hi<=2+2*r*(k+kp+4)+r*source[0]/2,'core upper envelope')
    # Full outer CE from its exact data marginal; uniform gate reference.
    # CEfull=CEcore/2+3 except for the combined data-empty atom.
    # Replace its naive cost using Q0/4+delta and mass P0/8+1/2.
    q0=qc[0];p0=pc[0]
    l,h=lg(1/(q0/4+1));ln,hn=lg(1/q0)
    # 2 gate bits plus sum D log(1/(Qcore*Pw+delta)).
    # Ordinary portion: CEcore/2+1; remove ordinary empty P0/8 log(4/Q0).
    flo=lo/2+3-p0*(2+hn)/8+(p0/8+F(1,2))*l
    fhi=hi/2+3-p0*(2+ln)/8+(p0/8+F(1,2))*h
    ck(fhi<=hi/2+3,'full code inequality')
    return flo,fhi,a,source
def profiles(rows,pilot):
    count=negative=0;min_margin=None
    subset=rows[:3] if pilot else rows
    for _,_,_,P,Q,I,nu0 in subset:
        for phase in (-1,1):
            nu=phase*nu0
            for k in ((5,) if pilot else (5,8,32)):
                for kp in sorted(set((0,1,k))):
                    lo,hi,a,src=rowcost(P,Q,nu,F(5,8)**5,k,kp)
                    r=F(1,2**kp)
                    for sigma in (-1,1):
                        actual4I=6+2*(kp-1)*a+r*I-sigma*a
                        bound=2-r*(k+kp+7)+r*(I-src[1]/4)
                        ck(actual4I-hi>=bound,'full terminal inequality without U')
                        margin=actual4I-hi-bound
                        min_margin=margin if min_margin is None else min(min_margin,margin)
                        negative+=1-2*a<0;count+=1
    return {'count':count,'signed_principal_profiles':negative,'minimum_certified_slack':str(min_margin)}
def adaptive():
    # Partition a seven-coordinate literal cube: two padding plus one E block.
    # Policies use the full physical history and stop on outcome-dependent sets.
    result=[]
    for mode in range(4):
        leaves=[]
        def walk(ass,depth):
            free=[i for i,v in enumerate(ass) if v<0]
            stop=depth>=4+mode%2 or not free or (depth>0 and sum(v for v in ass if v>=0)%(3+mode)==2)
            if stop:
                # Compulsory exact source cleanup, keeping BOTH physical children.
                st,ff=restriction(ORIG,ass[2:]);ess=[ff[i] for i in range(len(ff)) if any(st[x]!=st[x^(1<<i)] for x in range(len(st)))]
                ghost=[i+2 for i in ff if i not in ess]
                if ghost:
                    i=ghost[0]
                else:
                    mass=F(1,2**sum(v>=0 for v in ass));active=1 not in ass[:2];kp=ass[:2].count(-1);r=F(1,2**kp) if active else F(0)
                    leaves.append((mass,r,kp));return
            else:
                order=free if mode%2==0 else list(reversed(free))
                i=order[(sum(v for v in ass if v>=0)+depth)%len(order)]
            for b in (0,1):n=list(ass);n[i]=b;walk(n,depth+1)
        walk([-1]*7,0)
        ck(sum(x[0] for x in leaves)==1)
        er=sum(m*r for m,r,kp in leaves);erk=sum(m*r*kp for m,r,kp in leaves)
        ck(er==F(1,4));ck(erk<=F(1,2))
        result.append({'mode':mode,'leaves':len(leaves),'E_r':str(er),'E_r_kprime':str(erk)})
    return result
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv;rows=blocks(pilot)
    ck(F(sum(ORIG),32)==F(5,8));ck(influence(ORIG)==F(11,8))
    lit=literal(rows,pilot);pr=profiles(rows,pilot);trees=adaptive()
    ck(31**31>2**152);ck(F(11,8)-F(17,32)==F(27,32))
    for k in range(5,65):ck(F(2*(k+1)+7,2**(k+1))<F(2*k+7,2**k))
    elapsed=time.perf_counter()-start;ck(elapsed<60,'runtime')
    result={'status':'PASS','pilot':pilot,'checks':checks,'block_assignments':len(rows),'literal_original_projection_profiles':lit,'row_profiles':pr,'adaptive_policies':trees,'seconds':elapsed,'rung':'analytic proof independently reconstructed plus exact finite certificates; not Lean-checked'}
    (R/('out/PILOT.json' if pilot else 'out/REVIEW_CHECKS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
