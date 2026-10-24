from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
import json, math, time, hashlib, sys

ROOT=Path(__file__).resolve().parents[1]
checks=0
def require(b):
    global checks
    checks+=1
    assert b
def walsh(v):
    a=list(v); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):
                u,w=a[k],a[k+step]; a[k],a[k+step]=u+w,u-w
        step*=2
    return [F(x,len(a)) for x in a]
def spectrum(v): return [a*a for a in walsh(v)]
def influences(v):
    n=(len(v)-1).bit_length()
    return [sum(F((v[j]-v[j^(1<<i)])**2,4*len(v)) for j in range(len(v))) for i in range(n)]
@lru_cache(None)
def factors(q):
    ans={}; d=2
    while d*d<=q:
        while q%d==0: ans[d]=ans.get(d,0)+1; q//=d
        d+=1
    if q>1: ans[q]=ans.get(q,0)+1
    return ans
def add(a,b,c=1):
    a=dict(a)
    for k,v in b.items():
        a[k]=a.get(k,F(0))+c*v
        if not a[k]: del a[k]
    return a
def entropy(p):
    ans={}
    for q in p:
        if q:
            ans=add(ans,factors(q.denominator),q)
            ans=add(ans,factors(q.numerator),-q)
    return ans
def scale(a,c): return {k:v*c for k,v in a.items() if v*c}
def ln_two():
    t=F(1,3); s=sum((2*t**(2*j+1)/(2*j+1) for j in range(24)),F(0))
    return s,s+2*t**49/(49*(1-t*t))
L2,U2=ln_two()
@lru_cache(None)
def log2(q):
    if q==2: return F(1),F(1)
    q=F(q); e=0
    while q>=2: q/=2; e+=1
    t=(q-1)/(q+1)
    s=sum((2*t**(2*j+1)/(2*j+1) for j in range(24)),F(0))
    u=s+2*t**49/(49*(1-t*t))
    lo,hi=e+s/U2,e+u/L2
    D=1<<80
    return F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D)
def interval(a):
    lo=hi=F(0)
    for p,c in a.items():
        l,u=log2(p); lo+=c*(l if c>0 else u); hi+=c*(u if c>0 else l)
    return lo,hi
def le(a,b): require(interval(a)[1]<=b)
def U(p):
    supp=[s for s in range(1,len(p)) if p[s]]
    return sum((p[s]*(max(t.bit_count() for t in supp if t&s==s)-s.bit_count()) for s in supp),F(0))
def inspect(g,m,r,E,k,boolean=True):
    nx,nz=1<<m,1<<r; N=nx*nz
    v=[g[x]*(-1 if x*nz+z in E else 1) for x in range(nx) for z in range(nz)]
    p=spectrum(v); infl=influences(v); iz=sum(infl[:r]); ix=sum(infl[r:])
    mask=[-1 if j in E else 1 for j in range(N)]
    mi=influences(mask); mx=sum(mi[r:]); rho=F(len(E),N)
    sizes=[sum(x*nz+z in E for z in range(nz)) for x in range(nx)]
    eps=F(sum(bool(s) for s in sizes),nx)
    require(max(sizes)<=k)
    children=[[v[x*nz+z] for x in range(nx)] for z in range(nz)]
    cp=[spectrum(c) for c in children]
    require(all(sum(c)==1 for c in cp))
    q=[sum(p[t*nz:t*nz+nz]) for t in range(nx)]
    require(q==[sum(c[t] for c in cp)/nz for t in range(nx)])
    H=entropy(p); HC={}
    for c in cp: HC=add(HC,entropy(c),F(1,nz))
    Q=add(H,HC,-1); B=add(H,entropy(q),-1); J=add(entropy(q),HC,-1)
    require(add(B,J)==Q)
    require(ix==sum(sum(influences(c)) for c in children)/nz)
    le(J,2*iz/U2) # stronger than target using upper ln2
    if not boolean:
        Klo=4+2/U2
        return ix>=mx,interval(Q)[1]<=Klo*iz+2*ix,ix,mx
    require(ix>=mx)
    alpha=sum(p[s] for s in range(N) if s%(1<<r))
    require(alpha==sum((4*F(s,nz)*(1-F(s,nz)) for s in sizes),F(0))/nx)
    require(alpha<=4*rho<=1)
    require(iz>=2*rho*(r-(k.bit_length()-1))) # k=1 or 2
    if eps:
        el,eu=log2(1/eps); require(mx>=2*rho*eu or el==eu and mx==2*rho*el)
    if iz:
        Klo=F(4*r,r-(k.bit_length()-1))+2/U2
        le(Q,Klo*iz+2*ix)
    else: require(not Q)
    # Actual retained terminal entropy and conditional U admission.
    if all(U(c)<=sum(influences(ch)) for c,ch in zip(cp,children)):
        Klo=F(4*r,r-(k.bit_length()-1))+2/U2
        le(H,max(Klo,F(6))*(ix+iz))
    return True,Q,iz,ix

def main():
    pilot=len(sys.argv)>1 and sys.argv[1]=='pilot'
    start=time.perf_counter(); count=0; digest=hashlib.sha256()
    for m,r,k,kind in [(1,2,1,'fibers'),(2,3,2,'pairs')]:
        nx,nz=1<<m,1<<r
        for bits in range(1<<nx):
            g=[1 if bits>>x&1 else -1 for x in range(nx)]
            if kind=='fibers':
                sets=({x*nz+z for x,z in enumerate(v) if z>=0} for v in product(range(-1,nz),repeat=nx))
            else:
                sets=(set(v) for size in range(3) for v in combinations(range(nx*nz),size))
            for E in sets:
                if pilot and count>=100: break
                assert time.perf_counter()-start<(60 if pilot else 180), 'frozen runtime cap'
                inspect(g,m,r,E,k); count+=1
                digest.update(f'{m},{r},{bits},{sorted(E)}\n'.encode())
    # All normalized-real sign-mask relaxations of one rational norm-one seed.
    g=[F(1),F(-1,3),F(5,3),F(1,3)]; guards=0; realcount=0; real_access_failures=0; witness=None
    for row in product(range(-1,4),repeat=4):
        if pilot and realcount>=16: break
        E={x*4+z for x,z in enumerate(row) if z>=0}
        owned,paid,ix,mx=inspect(g,2,2,E,1,False); guards+=not owned; realcount+=1; real_access_failures+=not paid
        if not owned and witness is None: witness={'fiber_labels':row,'final_core_energy':str(ix),'mask_core_influence':str(mx)}
    # Analytic 16-core-bit zero-layer guard, no expanded truth table.
    guard=F(2*16*math.comb(16,8),4*(1<<16))
    require(guard==F(6435,4096)>1)
    # Boolean cap deletion guard.
    require(sum(influences([1,-1,-1,1])[1:])==1)
    require(sum(influences([1,-1,1,-1])[1:])==0)
    out={'boolean_cases':count,'real_cases':realcount,'assertions':checks,'ordered_domain_sha256':digest.hexdigest(),'real_ownership_failures_on_grid':guards,'first_real_ownership_witness':witness,'real_access_interval_failures':real_access_failures,'compressed_real_guard':str(guard),'runtime_seconds':time.perf_counter()-start,'failures':0,'arithmetic':'Fraction; prime-log maps; positive 24-term atanh interval with exact tail and outward dyadic rounding'}
    (ROOT/'out'/('PILOT.json' if pilot else 'CHECK_V2.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
if __name__=='__main__': main()
