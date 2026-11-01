from check import Q,prod,check,uniform_coeff,ent,add,spectrum,inf,delta,ASSERTIONS
from pathlib import Path
import json,time,math
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
def H(t):return ent(t)
def weighted(m,q,eta):
    a=q**m;b=(1-eta)*a/(eta+(1-eta)*a)
    alpha=a/(eta+(1-eta)*a)
    ps=(b,)+(q,)*m
    t=tuple(1 if (x&1) or x>>1==(1<<m)-1 else -1 for x in range(1<<(m+1)))
    raw,P=spectrum(t,ps)
    check(raw[0],2*alpha-1)
    rho=(1-a,)+((1-b)*q**(m-1),)*m
    Is=tuple(4*p*(1-p)*r for p,r in zip(ps,rho))
    check(inf(P),sum(Is))
    check(sum(Is)/(4*alpha),1-eta-b+m*eta*(1-q))
    phys=[]
    for x,f in enumerate(t):
        if f==1:phys.append((x,prod(ps[i] if x>>i&1 else 1-ps[i] for i in range(m+1))/alpha))
    check(sum(p for _,p in phys),Q(1))
    means=[sum(p for x,p in phys if x>>i&1) for i in range(m+1)]
    check(means,[1-eta]+[eta+(1-eta)*q]*m)
    actualTC=add(*[(Q(1),H((r,1-r))) for r in means],(-1,H([p for _,p in phys])))
    expectedTC=add((Q(m),H((eta+(1-eta)*q,1-eta-(1-eta)*q))),(-m*(1-eta),H((q,1-q))))
    check(actualTC,expectedTC)
    pairs=[]
    for j in range(m+1):
        MIs={}
        for k in range(m+1):
            if j==k:continue
            joint=[sum(p for x,p in phys if (((x>>j)&1)|(((x>>k)&1)<<1))==u) for u in range(4)]
            MIs=add((1,MIs),(1,H((means[j],1-means[j]))),(1,H((means[k],1-means[k]))),(-1,H(joint)))
        pairs.append((alpha/Is[j],MIs))
    return {'m':m,'q':str(q),'eta':str(eta),'alpha':str(alpha),'influence':str(sum(Is)),'exact_table_checks':'PASS','local_pair_MI_log_vectors':[{str(p):str(c*v) for p,v in d.items()} for c,d in pairs]}

def bent(m):
    g0=[]
    for y in range(1<<m):
        z=[((y>>i)&1)^((y>>(m-1))&1) for i in range(m-1)]
        g0.append((-1)**sum(z[i]*z[i+1] for i in range(0,m-1,2)))
    g1=[f*(-1 if y>>(m-1)&1 else 1) for y,f in enumerate(g0)]
    Ps=[]
    for parity,g in enumerate((g0,g1)):
        P=tuple(c*c for c in uniform_coeff(tuple(g)))
        check(sum(P),Q(1));check(inf(P),Q(m,2));check(ent(P),{2:Q(m-1)})
        check([s for s,p in enumerate(P) if p],[s for s in range(1<<m) if s.bit_count()%2==parity])
        check(set(p for p in P if p),{Q(1,1<<(m-1))});Ps.append(P)
    Ft=tuple((g0,g1)[x&1][x>>1] for x in range(1<<(m+1)))
    PF=tuple(c*c for c in uniform_coeff(Ft))
    check(set(PF),{Q(1,1<<(m+1))});check(inf(PF),Q(m+1,2))
    check(ent(PF),{2:Q(m+1)})
    return {'m':m,'child_H':m-1,'child_I':str(Q(m,2)),'parent_H':m+1,'parent_I':str(Q(m+1,2)),'selector_I':'1/2','spectral_erasure_child':0,'spectral_erasure_parent':m+1,'status':'PASS'}

# Elementary interval log routine with fixed rational mesh at each return.
MESH=10**25
def mesh(iv):return Q((iv[0]*MESH).__floor__(),MESH),Q((iv[1]*MESH).__ceil__(),MESH)
def plus(*ivs):return mesh((sum(v[0] for v in ivs),sum(v[1] for v in ivs)))
def scale(c,v):return mesh(tuple(sorted((c*v[0],c*v[1]))))
@lru_cache(None)
def lnr(x):
    k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def small(u):
        z=(u-1)/(u+1);n=40
        s=2*sum(z**(2*i+1)/Q(2*i+1) for i in range(n))
        return mesh((s,s+2*z**(2*n+1)/Q(2*n+1)/(1-z*z)))
    lo,hi=mesh((x,x))
    return plus((small(lo)[0],small(hi)[1]),scale(k,small(Q(2))))
def hn(p):return plus(scale(-p,lnr(p)),scale(-(1-p),lnr(1-p)))
def formula(m):
    q=Q(1,m*m);a=q**m;d=1+(m-1)*a;b=(m-1)*a/d;alpha=m*a/d
    r=Q(1,m)+(1-Q(1,m))*q
    TC=plus(scale(m,hn(r)),scale(-(m-1),hn(q)))
    I0=4*b*(1-b)*(1-a);Il=4*m*(1-b)*(1-q)*a;It=I0+Il
    V=4*alpha*(1-alpha)
    # Normalize symbolically BEFORE interval rounding; dividing an absolute 1e-25
    # rounding error by exponentially tiny influence gives an unusable enclosure.
    L=lnr(1/alpha);logone=lnr(1-alpha)
    normalized_credit=plus(
        scale(1-alpha,plus(L,scale(-1,lnr(Q(4))),scale(-1,logone))),
        scale(-(1-Q(1,m)-b),plus(L,lnr(1-a),scale(-1,logone))),
        scale(-(1-q),plus(lnr(Q(m)),scale(-1,logone))))
    def fmt(iv):
        # Exact outward decimal endpoints on a 1e-12 mesh, no floating arithmetic.
        den=10**12;v=[(iv[0]*den).__floor__(),(iv[1]*den).__ceil__()]
        return [('' if z>=0 else '-')+f'{abs(z)//den}.{abs(z)%den:012d}' for z in v]
    return {'m':m,'alpha_TC_over_I_nats':fmt(scale(alpha/It,TC)),'unit_pivotal_credit_residual_over_I_nats':fmt(scale(4*alpha/It,normalized_credit))}
out={'bent':[bent(m) for m in [3,5,7]],'weighted_tables':[weighted(m,Q(1,m*m),Q(1,m)) for m in [2,3,4]]+[weighted(m,q,Q(1,2)) for m in [2,3,4] for q in [Q(1,8),Q(1,64)]],'weighted_formula_intervals':[formula(m) for m in [2,4,8,16,32,64]],'runtime_seconds':time.perf_counter()-start,'status':'PASS'}
(ROOT/'out/controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'runtime_seconds':out['runtime_seconds'],'bent_cases':3,'weighted_exact_tables':9,'weighted_interval_cases':6}))
