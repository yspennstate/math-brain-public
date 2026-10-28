import json, time, sys, hashlib, itertools
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    checks+=1
    assert x, checks
def save(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2),encoding='utf-8')
def spectrum(t):
    n=len(t)
    return tuple(F(sum(v*(-1 if (i&s).bit_count()%2 else 1) for i,v in enumerate(t))**2,n*n) for s in range(n))
def infl(t):
    return sum(F(sum(t[i]!=t[i^(1<<b)] for i in range(len(t))),len(t)) for b in range(len(t).bit_length()-1))
def restrict(t,assign):
    free=[i for i,a in enumerate(assign) if a==-1]
    base=sum(a<<i for i,a in enumerate(assign) if a!=-1)
    return tuple(t[base+sum(((x>>b)&1)<<i for b,i in enumerate(free))] for x in range(1<<len(free))),free
def marginal(p,keep):
    out=[F(0)]*(1<<len(keep))
    for i,v in enumerate(p):out[sum(((i>>a)&1)<<b for b,a in enumerate(keep))]+=v
    return tuple(out)
@lru_cache(None)
def ln_interval(x):
    assert F(1)<=x<=F(2)
    z=(x-1)/(x+1);z2=z*z;t=z;s=F(0);N=40
    for i in range(N):s+=t/F(2*i+1);t*=z2
    return 2*s,2*s+2*t/F((2*N+1),1)/(1-z2)
@lru_cache(None)
def lg(x):
    assert x>0
    e=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**e
    if y<1:y*=2;e-=1
    if y==1:return F(e),F(e)
    a,b=ln_interval(y);c,d=ln_interval(F(2))
    return F(e)+a/d,F(e)+b/c
def ce(p,q):
    lo=hi=F(0)
    for a,b in zip(p,q):
        if a:
            ck(b>0);l,u=lg(1/b);lo+=a*l;hi+=a*u
    return lo,hi
def Evalue(i):
    g=lambda bits: -1 if all(not (i>>b)&1 for b in bits) else 1
    return g((0,1,2))*g((0,3,4))
ORIG=tuple(Evalue(i) for i in range(32));OP=spectrum(ORIG)
def block_contract(pilot):
    states={};cert=[]
    domain=itertools.product((-1,0,1),repeat=3 if pilot else 5)
    for aa in domain:
        assign=tuple(aa)+( (-1,-1) if pilot else () )
        t,free=restrict(ORIG,assign)
        essential=[b for b in range(len(free)) if any(t[i]!=t[i^(1<<b)] for i in range(len(t)))]
        cleaned=tuple(t[sum(((i>>b)&1)<<a for b,a in enumerate(essential))] for i in range(1<<len(essential)))
        keep=[free[a] for a in essential];p=spectrum(cleaned);q=marginal(OP,keep);I=infl(cleaned)
        ck(sum(p)==sum(q)==1);ck(I==sum(v*i.bit_count() for i,v in enumerate(p)))
        D=len(cleaned)**2;power=4*I*D;ck(power.denominator==1)
        left=2**int(power);right=1
        for x,y in zip(p,q):
            exponent=x*D;ck(exponent.denominator==1)
            if exponent:
                ck(y>0);left*=y.numerator**int(exponent);right*=y.denominator**int(exponent)
        ck(left>=right)
        states[(tuple(keep),cleaned)]=(cleaned,q)
        cert.append({'assignment':assign,'keep':keep,'truth':cleaned,'P':list(map(str,p)),'R':list(map(str,q)),'I':str(I),'left':str(left),'right':str(right)})
    if not pilot:ck(len(cert)==243);ck(len(states)==45)
    save('BLOCK_CERTIFICATES_PILOT.json' if pilot else 'BLOCK_CERTIFICATES.json',cert)
    return list(states.values())
def corelaw(t,ref,kp,rho,mu,active=True,sigma=1):
    r=F(1,1<<kp);nu=F(sum(t),len(t));a=r*(1-nu)/2 if active else F(0);p0=rho*(1-mu)/2
    pp=spectrum(t);n=len(t)*(1<<(kp+1));P=[F(0)]*n;Q=[F(0)]*n
    P[1]=1-2*a;Q[1]=(1-2*p0)/2;Q[0]+=F(1,2)
    for s in range(len(t)):
        for uv in range(1<<(kp+1)):
            i=uv+(s<<(kp+1));Q[i]+=rho*r*(ref[s]+(1-2*mu if s==0 else 0))/8
            if active:P[i]+=r*r*(pp[s]+(1-2*nu if s==0 else 0))/4
    def trueval(i):
        u=-1 if i&1 else 1;v=(i>>1)&((1<<kp)-1);g=t[i>>(kp+1)]
        return sigma if active and v==0 and g==-1 else u
    tt=tuple(trueval(i) for i in range(n));actual=spectrum(tt)
    ck(tuple(P)==actual);ck(sum(P)==sum(Q)==1);ck(min(P)>=0);ck(min(Q)>=0)
    # check physical identity, including gate/mask contributions, independently
    # gate is +1 at 0 and core*w at 1: 4I_F=4+2I_core-E(core)
    actual4=4+2*infl(tt)-F(sum(tt),len(tt))
    target4=6+2*(kp-1)*a+(r*infl(t) if active else 0)-sigma*a
    ck(actual4==target4)
    if active:
        T=[i for i in range(n) if i>>(kp+1)]
        subsetP=tuple(P[i] for i in T);subsetQ=tuple(Q[i] for i in T)
        l,u=ce(subsetP,subsetQ);nsce=ce(pp[1:],ref[1:]);c=r*(1-nu*nu)*F(5+kp+3,2)
        ck(l<=c+r*nsce[1]/2 and u>=c+r*nsce[0]/2)
        # Failure controls: signed algebra need not be a nonnegative mixture.
        for i in range(n):
            if i not in (0,1) and not(i>>(kp+1)):ck(Q[i]>=3*rho*r/32)
    cl,ch=ce(P,Q);sl,sh=ce(pp,ref)
    r0=r if active else F(0)
    bound=2+2*r0*(5+kp+4)+r0*sh/2
    ck(ch<=bound)
    # Complete outer gate law data marginal, no actual conditional reset.
    data=[P[i]/8 for mask in range(4) for i in range(n)];data[0]+=F(1,2)
    qdata=[Q[i]/8 for mask in range(4) for i in range(n)];qdata[0]+=F(1,2)
    # uniform gate adds exactly1; actual interference does not affect CE.
    outerhi=ce(data,qdata)[1]+1
    ck(outerhi<=ch/2+3)
    ck(actual4-outerhi>=2-r0*(5+kp+7)+r0*(infl(t)-sh/4))
    return {'nu':str(nu),'kprime':kp,'active':active,'principal_coefficient':str(1-2*a)}
def adaptive_padding_tests():
    # Full outcome-dependent tree over one E block and two padding bits.
    # It can query every source coordinate: no count cap in martingale test.
    rows=[]
    for policy in range(4):
        total=F(0);post=F(0);postk=F(0);leaves=0;mx=0
        def walk(assign,weight,depth):
            nonlocal total,post,postk,leaves,mx
            free=[i for i,a in enumerate(assign) if a==-1]
            r=F(0) if 1 in assign[:2] else F(1,2**sum(a==-1 for a in assign[:2]))
            if not free or (depth>0 and ((sum((i+1)*a for i,a in enumerate(assign) if a!=-1)+policy)%7==0)):
                total+=weight;post+=weight*r;postk+=weight*r*sum(a==-1 for a in assign[:2]);leaves+=1;mx=max(mx,depth);return
            idx=free[(policy+sum(a==1 for a in assign)+depth)%len(free)]
            for b in (0,1):
                aa=list(assign);aa[idx]=b;walk(aa,weight/2,depth+1)
        walk([-1]*7,F(1),0);ck(total==1);ck(post==F(1,4));ck(postk<=F(1,2))
        rows.append({'policy':policy,'leaves':leaves,'max_depth':mx,'posterior_mean':str(post),'posterior_remaining_padding':str(postk)})
    return rows
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv;states=block_contract(pilot);profiles=[]
    chosen=states[:2] if pilot else states
    for t,r in chosen:
        for sign in (-1,1):
            tt=tuple(sign*x for x in t)
            for kp in (0,1,2):profiles.append(corelaw(tt,r,kp,F(1,32),F(5,8)**5))
    for t,r in chosen[:2]:corelaw(t,r,0,F(1,32),F(5,8)**5,False)
    ck(F(11,8)-F(17,32)==F(27,32))
    for k in range(5,129):ck(F(2*k+9,2**(k+1))<F(2*k+7,2**k))
    trees=adaptive_padding_tests();elapsed=time.perf_counter()-start;ck(elapsed<60)
    result={'status':'PASS','checks':checks,'states':len(states),'profiles':len(profiles),'negative_principal_profiles':sum(F(x['principal_coefficient'])<0 for x in profiles),'adaptive_trees':trees,'seconds':elapsed,'FEI':'OPEN'}
    save('PILOT.json' if pilot else 'CHECKS.json',result);print(json.dumps(result))
if __name__=='__main__':main()
