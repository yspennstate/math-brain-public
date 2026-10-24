from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,math,sys
ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def ck(x):
    global COUNT
    assert x
    COUNT+=1
def fwht(v):
    v=list(v);step=1
    while step<len(v):
        for j in range(0,len(v),2*step):
            for i in range(j,j+step):
                a,b=v[i],v[i+step];v[i],v[i+step]=a+b,a-b
        step*=2
    return v
def coeff(v):return [F(x,len(v)) for x in fwht(v)]
def pmass(v):return [x*x for x in coeff(v)]
def influence(p,bit):return sum(x for s,x in enumerate(p) if s&bit)
def add(*xs):
    out={}
    for x in xs:
        for k,v in x.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def mul(x,c):return {k:v*c for k,v in x.items() if v*c}
@lru_cache(None)
def factor(x):
    d={};k=2
    while k*k<=x:
        while x%k==0:d[k]=d.get(k,0)+1;x//=k
        k+=1
    if x>1:d[x]=d.get(x,0)+1
    return d
@lru_cache(None)
def logexpr(q):
    q=F(q)
    assert q>0
    return add(factor(q.numerator),mul(factor(q.denominator),-1))
def entexpr(p):return add(*(mul(logexpr(q),-q) for q in p if q))
def phiexpr(u,v):return add(entexpr([u,v]),mul(entexpr([u+v]),-1))
def bexpr(p,bit):return add(*(phiexpr(p[s],p[s|bit]) for s in range(len(p)) if not s&bit))
@lru_cache(None)
def lnunit(q):
    z=(q-1)/(q+1);total=F(0)
    for j in range(48):total+=2*z**(2*j+1)/(2*j+1)
    err=2*abs(z)**97/(97*(1-z*z))
    return total-err,total+err
@lru_cache(None)
def logint(q):
    q=F(q);assert q>0
    k=q.numerator.bit_length()-q.denominator.bit_length()
    x=q/(F(2)**k)
    if x<1:k-=1;x*=2
    if x>=2:k+=1;x/=2
    assert 1<=x<2
    lo,hi=lnunit(x);a,b=lnunit(F(2))
    return F(k)+lo/b,F(k)+hi/a
def intadd(*intervals):return sum(x[0] for x in intervals),sum(x[1] for x in intervals)
def intmul(c,interval):return (c*interval[0],c*interval[1]) if c>=0 else (c*interval[1],c*interval[0])
@lru_cache(None)
def phiint(u,v):
    if not u or not v:return F(0),F(0)
    return intadd(intmul(u,logint((u+v)/u)),intmul(v,logint((u+v)/v)))
def outward(q,upper=True):
    denom=10**12
    scaled=q*denom
    num=(-(-scaled.numerator//scaled.denominator)) if upper else (scaled.numerator//scaled.denominator)
    result=F(num,denom)
    ck(result>=q if upper else result<=q)
    return str(result)
start=time.monotonic();num=0
families_only='--families-only' in sys.argv
if families_only:
    checkpoint=json.loads((ROOT/'out/SUBSTITUTION.json').read_text())
    ck(checkpoint['status']=='PASS' and checkpoint['cases']==276)
    num=checkpoint['cases'];COUNT+=checkpoint['assertions_so_far']
for n in ([] if families_only else [1,2,3]):
    for table in range(2**(2**n)):
        src=[1 if table>>x&1 else -1 for x in range(2**n)]
        ps=pmass(src);N=1+3*(n-1);vals=[]
        for z in range(2**N):
            index=z&1
            for j in range(n-1):
                block=(z>>(1+3*j))&7
                index|=(block.bit_count()>=2)<<(j+1)
            vals.append(src[index])
        pe=pmass(vals)
        ck(sum(pe)==1);ck(influence(pe,1)==influence(ps,1))
        ck(bexpr(pe,1)==bexpr(ps,1))
        de=add(entexpr(pe),mul(add(entexpr(pmass(vals[::2])),entexpr(pmass(vals[1::2]))),-F(1,2)))
        ds=add(entexpr(ps),mul(add(entexpr(pmass(src[::2])),entexpr(pmass(src[1::2]))),-F(1,2)))
        ck(de==ds)
        for j in range(n-1):
            outerbit=1<<(j+1)
            expected=add(*(phiexpr(ps[s],ps[s|outerbit]/4) for s in range(len(ps)) if not s&outerbit))
            for ell in range(3):
                bit=1<<(1+3*j+ell)
                ck(influence(pe,bit)==influence(ps,outerbit)/2)
                ck(bexpr(pe,bit)==expected)
        num+=1
        if time.monotonic()-start>60:raise RuntimeError('Frozen runtime exceeded')
if not families_only:
    source_result={'cases':num,'assertions_so_far':COUNT,'status':'PASS','runtime_seconds':time.monotonic()-start}
    (ROOT/'out/SUBSTITUTION.json').write_text(json.dumps(source_result,indent=2),encoding='utf-8')
families=[]
for k in [4,6,8,10,12,14,16]:
    delta=F(1,2**k);s=F(1,2**(k//2));p=delta**2
    mu=s-delta;A=1-mu;u=F(1,2)+delta;t=p*A
    alpha_x=p*u;alpha_z=t;alpha_y=p*delta
    I=k*alpha_x+2*k*alpha_z+alpha_y;d=3*k+1
    ck(alpha_x>=I/(2*d));ck(alpha_z>=I/(2*d));ck(max(alpha_x,alpha_z,alpha_y)<F(1,4))
    beta=intadd((F(1,2)-delta/2,F(1,2)-delta/2),intmul(1/(4*delta),phiint((s-delta)**2,(s+delta)**2)))
    Bx=intadd(intmul(p,beta),(-2*p*mu**2,-2*p*mu**2),intmul(p-p*p,phiint(A*A,mu*mu)),phiint((1-t)**2,p*p*mu*mu))
    Bz=intadd((2*t-2*t*t,2*t-2*t*t),phiint((1-t)**2,t*t))
    chosen=Bx if k==4 else Bz; alpha=alpha_x if k==4 else alpha_z
    ck(chosen[1]<4*alpha)
    # All-dimensional majority expansion checked by rational anchor inequalities,
    # not by building its enormous truth table or central binomial coefficient.
    R=2**(2*k+2);M=2*R+1;rho_upper=delta/2
    ck(1>F(R,R+1));ck(p*rho_upper<=alpha_y/2)
    ck(k*(5*u-2*A)>delta)
    ck(F(4*k+7,2**(k+1))<1)
    ck((1-delta)*(k-2)>1)
    families.append({'family':'B05 and majority-diluted B05','k':k,'original_d':d,'inflated_D':3*k*M+1,'eligible_types':['data','control'],'original_chosen_type':'data' if k==4 else 'control','chosen_ratio_certified_upper':outward(chosen[1]/alpha),'diluted_background_ratio_rational_upper':str(F(4*k+7,2**(k+1))),'selector_ratio_rational_lower':str((1-delta)*(k-2)),'rho_strict_upper':str(rho_upper),'maximum_alpha':str(alpha_y)})
    if k==4:
        vals=[]
        for index in range(2**(3*k+1)):
            x=index&((1<<k)-1);z=(index>>k)&((1<<(2*k))-1);y=index>>(3*k)
            parity=sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2
            b=(-1)**parity;h=b-2*int(x==0 and y==1)
            vals.append(1 if z else h)
        coeffs=coeff(vals); pp=[a*a for a in coeffs]
        ck(influence(pp,1)==alpha_x);ck(influence(pp,1<<k)==alpha_z);ck(influence(pp,1<<(3*k))==alpha_y)
        bx=intadd(*(phiint(pp[j],pp[j|1]) for j in range(len(pp)) if not j&1))
        bz=intadd(*(phiint(pp[j],pp[j|(1<<k)]) for j in range(len(pp)) if not j&(1<<k)))
        ck(max(bx[0],Bx[0])<=min(bx[1],Bx[1]));ck(max(bz[0],Bz[0])<=min(bz[1],Bz[1]))
        # Check coefficient equality directly against analytic activation structure.
        bent=coeff([(-1)**(sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2) for x in range(2**k)])
        for idx,a0 in enumerate(coeffs):
            T=idx&((1<<k)-1);U=(idx>>k)&((1<<(2*k))-1);Y=idx>>(3*k)
            expected=(1-t if U==0 else -p*A) if T==0 and Y==0 else p*(delta if Y else bent[T]-delta)
            ck(a0==expected)
for k in [4,6,8,10]:
    delta=F(1,2**k);s=F(1,2**(k//2));alpha=F(1,2)+delta
    I=k*alpha+delta;d=k+1
    ck(alpha>=I/(2*d));ck(alpha>F(1,4))
    beta=intadd((F(1,2)-delta/2,F(1,2)-delta/2),intmul(1/(4*delta),phiint((s-delta)**2,(s+delta)**2)))
    ck(beta[1]<2*alpha)
    families.append({'family':'X009','k':k,'eligible_chosen_type':'data','weak_regime':False,'chosen_ratio_certified_upper':outward(beta[1]/alpha)})
out={'status':'PASS','helper_version':'A003-stage2-v3','labelled_substitution_sources':num,'source_checkpoint_reused':families_only,'family_cases':families,'assertions':COUNT,'runtime_seconds':time.monotonic()-start,'certificate_arithmetic':'Fraction; exact log-prime substitution identities; 48-term rational atanh intervals for family inequalities; exact outward rounding for serialization','full_FEI':'OPEN'}
(ROOT/'out/VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='family_cases'}))
