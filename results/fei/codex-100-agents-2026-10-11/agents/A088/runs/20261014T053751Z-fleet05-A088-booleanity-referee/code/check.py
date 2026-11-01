from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import importlib.util,sys,time,json,hashlib,math
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261014T024038Z-fleet05-A088-booleanity-referee/code/check.py'
sp=importlib.util.spec_from_file_location('own_prior_cells',old); c=importlib.util.module_from_spec(sp); sp.loader.exec_module(c); h=c.h
checks=0
def ck(b):
    global checks
    checks+=1
    assert b
def ge(a): ck(not a or h.interval(a)[0]>=0)
@lru_cache(None)
def flag_certificate(alpha,I):
    if alpha in (0,1): return True
    D=math.lcm(alpha.denominator,I.denominator); N=int(alpha*D); k=2*I*D
    assert k.denominator==1
    return D**D<=(1<<int(k))*N**N*(D-N)**(D-N)
def inspect(branches,p,q):
    r=len(p); nz=1<<r; nx=len(branches[0]); cells,bad=c.cells(p,q)
    _,_,pv=c.controller(p); _,_,qv=c.controller(q)
    v=[branches[pv[z]+2*qv[z]][x] for x in range(nx) for z in range(nz)]
    ps=h.spectrum(v); infl=h.influences(v); iz=sum(infl[:r]); ix=sum(infl[r:]); alpha=sum(ps[s] for s in range(nx*nz) if s%nz)
    ck(flag_certificate(alpha,ix+iz))
    ck(alpha<=iz)
    core=[sum(ps[t*nz:(t+1)*nz]) for t in range(nx)]
    child=[h.spectrum([v[x*nz+z] for x in range(nx)]) for z in range(nz)]
    ck(core==[sum(u[t] for u in child)/nz for t in range(nx)])
    H=h.entropy(ps); HT=h.entropy(core); terminal={}
    for u in child: terminal=h.add(terminal,h.entropy(u),F(1,nz))
    card={}
    for t in range(nx):
        for cell in cells:
            ck(len({ps[t*nz+s] for s in cell})==1)
            mass=sum(ps[t*nz+s] for s in cell)
            card=h.add(card,h.factors(len(cell)),mass)
    tail=h.entropy([alpha,1-alpha])
    CE=h.add(h.add(h.add(HT,tail),h.factors(len(cells)),alpha),card)
    ge(h.add(CE,H,-1))
    Klo=4+h.log2(5 if bad else 4)[0]+2/h.U2
    ck(h.interval(h.add(CE,terminal,-1))[1]<=Klo*iz+2*ix)
    ck(h.interval(h.add(H,terminal,-1))[1]<=Klo*iz+2*ix)
    ck(h.interval(H)[1]<=max(Klo,F(6))*(ix+iz))
    # Exact root conditional tail-flag refund, with the core law retained.
    binary_joint=[F(0)]*(2*nx)
    for t in range(nx):
        binary_joint[2*t]=ps[t*nz]
        binary_joint[2*t+1]=sum(ps[t*nz+1:(t+1)*nz])
    conditional=h.add(h.entropy(binary_joint),HT,-1)
    refund=h.add(tail,conditional,-1)
    ge(refund)
    # Replacing only the flag prior changes CE by precisely this MI.
    corrected=h.add(CE,refund,-1)
    ck(h.add(CE,corrected,-1)==refund)
    ge(h.add(corrected,H,-1))

def branch_domain(pilot):
    patterns=list(product((-1,0,1),repeat=2))
    pairs=[(p,q) for p in patterns for q in patterns if c.controller(p)[0]|c.controller(q)[0]==3]
    if not pilot:
        pairs+=sum((c.geometry(r) for r in (3,4,5)),[])
    cores=list(product((-1,1),repeat=2))
    for p,q in pairs:
        for branches in product(cores,repeat=4): yield branches,p,q
def exposed_guard(m):
    # Bits z,w,Y; b(Y)=(-1)^(sum paired 0/1 products).
    n=2*m+2; N=1<<n; v=[]
    for s in range(N):
        z=1 if s&1 else -1; w=(s>>1)&1; Y=s>>2
        b=1 if sum(((Y>>(2*j))&1)*((Y>>(2*j+1))&1) for j in range(m))%2==0 else -1
        v.append(b+(z-1 if w==0 and Y==0 else 0))
    ps=h.spectrum(v); inf=h.influences(v); delta=F(1,1<<(2*m+1)); A=F(1,1<<m)
    ck(inf[0]==delta and sum(inf)==m+(2*m+2)*delta)
    row=[ps[2*t]+ps[2*t+1] for t in range(N//2)]
    B=h.add(h.entropy(ps),h.entropy(row),-1)
    alpha=sum(ps[1::2]); ck(alpha==delta)
    tail=h.entropy([alpha,1-alpha]); refund=h.add(tail,B,-1); ge(refund)
    for t,qmass in enumerate(row):
        ck(ps[2*t+1]==delta*delta)
        if t&1: ck(qmass==2*delta*delta)
        else: ck(qmass>=delta*delta*(1<<(2*m+1)))
    # Exact row inequalities give B>=delta*(m+3/2); interval independently confirms.
    ck(h.interval(B)[0]>=delta*(m+F(3,2)))
    ck(sum(inf)>=m and n<=3*m) # H<=n therefore H/I<=3.
    # Reconstruct the parent as b(c,w,Y)+point(q(z)-1) and check actual c=0 restriction.
    parent=[]
    for s in range(1<<(n+1)):
        child_index=s>>1; cc=s&1; zz=1 if child_index&1 else -1; ww=(child_index>>1)&1; Y=child_index>>2
        b=1 if (cc*ww+sum(((Y>>(2*j))&1)*((Y>>(2*j+1))&1) for j in range(m)))%2==0 else -1
        parent.append(b+(zz-1 if cc==0 and ww==0 and Y==0 else 0))
    ck(parent[::2]==v and all(s in (-1,1) for s in parent))
    blo,bhi=h.interval(B); rlo,rhi=h.interval(refund)
    return {'m':m,'dimension':n,'control_influence':str(delta),'conditional_flag_over_I_lower':str(blo/delta),'conditional_flag_over_I_upper':str(bhi/delta),'analytic_lower':str(m+F(3,2)),'MI_refund_over_I_lower':str(rlo/delta),'MI_refund_over_I_upper':str(rhi/delta),'total_influence':str(sum(inf)),'H_over_I_upper':'3','actual_parent_first_core_query_checked':True}
def main():
    pilot='pilot' in sys.argv; start=time.perf_counter(); cases=0; digest=hashlib.sha256()
    for args in branch_domain(pilot):
        if pilot and cases>=128: break
        ck(time.perf_counter()-start<(60 if pilot else 300))
        inspect(*args); cases+=1; digest.update(repr(args).encode())
    guards=[exposed_guard(m) for m in ((2,) if pilot else (2,3,4,5))]
    a,b=F(4095,4097),F(128,4097); beta=b*b
    ck(a*a+beta==1 and beta<F(1,1024))
    ck(F(842,1215)>F(2,3) and 5**2<2**5)
    out={'branch_cases':cases,'assertions':checks,'domain_sha256':digest.hexdigest(),'runtime_seconds':time.perf_counter()-start,'failures':0,'exposed_conditional_flag_guards':guards,'real_guard':{'alpha_and_I':str(beta),'norm':'1','H_over_I_strict_lower':'10','source_K_strict_upper':'19/2','controller_span':'p=1{z=+},q=1{z=-},X empty'},'scope':'New source proof audited; conditional-flag-only local price refuted, not FEI'}
    (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='exposed_conditional_flag_guards'}))
if __name__=='__main__': main()
