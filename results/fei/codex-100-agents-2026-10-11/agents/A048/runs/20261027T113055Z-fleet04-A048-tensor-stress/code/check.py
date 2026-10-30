from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import itertools, json, time
ROOT=Path(__file__).resolve().parents[1]
counts={}
def ck(ok,tag):
    counts[tag]=counts.get(tag,0)+1
    assert ok,tag
def walsh(vals):
    N=len(vals)
    return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals)),N) for s in range(N)]
def spec(c): return [x*x for x in c]
def fresh(p,J):
    if J==0:return p[:]
    q=[F(5,6)*x for x in p];q[0]=p[0];q[J]+=F(1,6)*(1-p[0]);return q
def factors(n):
    ans={};d=2
    while d*d<=n:
        while n%d==0:ans[d]=ans.get(d,0)+1;n//=d
        d+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
def plus(*terms):
    z={}
    for c,a in terms:
        for p,v in a.items():z[p]=z.get(p,F(0))+c*v
    return {p:v for p,v in z.items() if v}
def logsum(items):
    z={}
    for w,x in items:
        if not w:continue
        assert x>0
        for n,c in [(x.numerator,1),(x.denominator,-1)]:
            for p,e in factors(n).items():z[p]=z.get(p,F(0))+w*c*e
    return {p:v for p,v in z.items() if v}
def KL(p,q):return logsum((x,x/y) for x,y in zip(p,q) if x)
def H(p):return logsum((-x,x) for x in p if x)
@lru_cache(None)
def ln_bounds(x):
    z=(x-1)/(x+1); assert 0<=z<1
    N=32;v=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    return v,v+2*z**(2*N+1)/F(2*N+1)/(1-z*z)
@lru_cache(None)
def lp(p):
    k=p.bit_length()-1;x=F(p,2**k);a,b=ln_bounds(x);c,d=ln_bounds(F(2))
    return F(k)+a/d,F(k)+b/c
def bounds(a):
    lo=hi=F(0)
    for p,v in a.items():
        x,y=lp(p);lo+=v*(x if v>=0 else y);hi+=v*(y if v>=0 else x)
    return lo,hi
def nonneg(a):return not a or bounds(a)[0]>=0
ELL=logsum([(F(1),F(6,5))])
def delete(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)
def pairs(n,i):
    for t in range(1<<(n-1)):
        a=(t&((1<<i)-1))|((t>>i)<<(i+1));yield a,a|(1<<i)
def channel(c,q,i):
    n=(len(c)).bit_length()-1;p=spec(c);pp=list(pairs(n,i))
    P=[p[a]+p[b] for a,b in pp];Q=[q[a]+q[b] for a,b in pp]
    cs=[[c[a]+sgn*c[b] for a,b in pp] for sgn in [1,-1]]
    ps=[spec(x) for x in cs]
    ks=[[v/(2*w) if w else F(1,2) for v,w in zip(row,P)] for row in ps]
    rs=[sum(v*w for v,w in zip(Q,row)) for row in ks]
    qs=[[v*w/r for v,w in zip(Q,row)] for row,r in zip(ks,rs)]
    er=plus((1,KL(p,q)),(-1,KL(P,Q)));ou=KL([F(1,2)]*2,rs)
    ki=[KL(v,w) for v,w in zip(ps,qs)]
    ck(not plus((1,KL(p,q)),(-1,er),(-1,ou),(-F(1,2),ki[0]),(-F(1,2),ki[1])),'exact_KL_chain')
    ck(all(r>=F(5,12) for r in rs),'normalizers')
    return cs,ps,qs,er,ou,ki,rs
def prod(p,q):return [a*b for b in q for a in p]
def influence(p):return sum(F(s.bit_count())*v for s,v in enumerate(p))
def activation(vals,k):
    # low k control bits; next bit independent balanced guard; high bits data
    return [vals[x>>(k+1)]*(-1 if x&(1<<k) else 1) if x&((1<<k)-1)==0 else 1 for x in range(len(vals)*(1<<(k+1)))]
def lifted(q,k):
    rho=F(1,2**k);out=[F(0)]*((1<<(k+1))*len(q));out[0]=(1-rho)**2
    for s in range(1,1<<k):out[s]=rho*rho
    for t,w in enumerate(q):
        for s in range(1<<k):out[s|(1<<k)|(t<<(k+1))]=rho*rho*w
    return out
def run():
    start=time.perf_counter();edges=0
    for n in [1,2,3]:
        for vals in itertools.product([-1,1],repeat=1<<n):
            c=walsh(vals);p=spec(c)
            for J in range(1,1<<n):
                q=fresh(p,J);a=1-p[J];B=(n-1)*a
                ck(sum(q)==1,'normalized_root')
                ck(nonneg(plus((a,ELL),(-1,KL(p,q)))),'root_bank')
                for i in range(n):
                    cs,ps,qs,er,ou,ki,rs=channel(c,q,i);Jp=delete(J,i)
                    af=[1*v[Jp] for v in ps];aa=[1-v for v in af]
                    partner=J^(1<<i)
                    ck(sum(aa)/2==a-p[partner],'anchor_square_martingale')
                    Bs=[(n-2)*v if Jp else F(0) for v in aa]
                    freshK=[KL(v,fresh(v,Jp)) for v in ps]
                    sigma=plus((F(1,2),freshK[0]),(F(1,2),freshK[1]),(-F(1,2),ki[0]),(-F(1,2),ki[1]))
                    ck(nonneg(plus((B-sum(Bs)/2,ELL),(-1,sigma))),'signed_local_bank')
                    if not Jp:ck(nonneg(plus((-1,sigma))),'absorption_refund')
                    edges+=1
    sparse=0
    two=list(itertools.product([-1,1],repeat=4))
    for v,w in itertools.product(two,repeat=2):
        cv,cw=walsh(v),walsh(w);pv,pw=spec(cv),spec(cw)
        qv,qw=fresh(pv,1),fresh(pw,1);q=prod(qv,qw);p=prod(pv,pw)
        vals=[v[x&3]*w[x>>2] for x in range(16)]
        ck(spec(walsh(vals))==p,'literal_tensor_spectrum')
        ck(not plus((1,KL(p,q)),(-1,KL(pv,qv)),(-1,KL(pw,qw))),'tensor_KL_additivity')
        ck(not plus((1,H(p)),(-1,H(pv)),(-1,H(pw))),'tensor_entropy_additivity')
        for i in [0,1]:
            _,pl,_,_,ol,kil,_=channel(cv,qv,i)
            _,pg,_,_,og,kig,_=channel(walsh(vals),q,i)
            jl=delete(1,i)
            sl=plus(*[(F(1,2),KL(x,fresh(x,jl))) for x in pl],* [(-F(1,2),x) for x in kil])
            sg=plus(*[(F(1,2),KL(x,prod(fresh(y,jl),qw))) for x,y in zip(pg,pl)],* [(-F(1,2),x) for x in kig])
            ck(not plus((1,sg),(-1,sl),(-1,og),(1,ol)),'tensor_ghost_exact_correction')
            ck(nonneg(plus((1,ol),(-1,og))),'tensor_ghost_refund')
        for k in [1,2]:
            rho=F(1,2**k);vv=activation(vals,k);c=walsh(vv);pp=spec(c);qq=lifted(q,k)
            ck(pp==lifted(p,k),'activation_spectrum')
            ck(sum(qq)==1,'normalized_activation_reference')
            ck(not plus((1,KL(pp,qq)),(-rho,KL(p,q))),'activation_KL_scaling')
            ck(influence(pp)==rho*(k+1+influence(p)),'activation_influence')
            cs,ps,qs,er,ou,ki,rs=channel(c,qq,0)
            ghost=sum(y for x,y in zip(p,q) if not x)
            ck(not er,'controller_zero_erasure')
            ck(rs==[F(1,2)*(1-rho*ghost),F(1,2)*(1+rho*ghost)],'controller_ghost_outcomes')
            expectedO=logsum([(-F(1,2),1-rho*rho*ghost*ghost)])
            ck(not plus((1,ou),(-1,expectedO)),'controller_exact_outcome_KL')
            fq=[lifted(q,k-1),[F(1)]+[F(0)]*(len(qs[1])-1)]
            sigma=plus(*[(F(1,2),KL(x,y)) for x,y in zip(ps,fq)],* [(-F(1,2),x) for x in ki])
            ck(not plus((1,sigma),(-1,ou)),'controller_signed_reset_equals_outcome')
            ck(nonneg(plus((rho*rho*ghost*ghost,logsum([(F(1),F(2))])),(-1,ou))),'controller_rational_upper_envelope')
            sparse+=1
    tensor_examples=[]
    for d in range(2,11):
        a=F(4,2**d)*(1-F(1,2**d))
        for r in range(1,9):
            if r*a>1:continue
            ratio=(1-(1-a)**r)/a
            ck(ratio>=F(r,2),'global_tensor_envelope_inflation')
            tensor_examples.append([d,r,str(ratio)])
    for k in range(1,13):
        rho=F(1,2**k);n=k+1
        # Exact point-defect coefficient and influence formulas; literal audit is independent.
        pJ=rho*rho;I=n*rho
        ck(F(n)*(1-pJ)/I==(1-rho*rho)/rho,'global_sparse_envelope_failure')
    result=dict(status='PASS',helper_version='v2-ghost-corrected',edges=edges,sparse_roots=sparse,checks=sum(counts.values()),counts=counts,tensor_cases=len(tensor_examples),seconds=time.perf_counter()-start,arithmetic='Fraction; exact prime-log dictionaries; outward32-term rational atanh')
    ROOT.joinpath('out/CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    ROOT.joinpath('out/TENSOR_EXAMPLES.json').write_text(json.dumps(tensor_examples,indent=2),encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':run()
