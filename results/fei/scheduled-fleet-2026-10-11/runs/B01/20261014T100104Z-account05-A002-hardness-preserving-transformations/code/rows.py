import sys,json,time,hashlib,itertools
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
sys.dont_write_bytecode=True
import arithmetic as M
R=Path(__file__).resolve().parents[1]
@lru_cache(None)
def ln(q):
    z=(q-1)/(q+1);p=z;s=Q(0)
    for k in range(48):s+=p/(2*k+1);p*=z*z
    return 2*s,2*s+2*p/(97*(1-z*z))
@lru_cache(None)
def log(p):
    k=p.bit_length()-1;a,b=ln(Q(p,1<<k));c,d=ln(Q(2));scale=1<<96
    low=k+a/d;high=k+b/c
    return Q((low*scale).numerator//(low*scale).denominator,scale),Q(-((-high*scale).numerator//(-high*scale).denominator),scale)
@lru_cache(None)
def interval(expr):
    a=b=Q(0)
    for p,c in expr:
        l,u=log(p)
        if c<0:l,u=u,l
        a+=c*l;b+=c*u
    return a,b
def Hweights(weights,den):return M.add(*[(1,M.phi(Q(x,den))) for x in weights if x])
def row(a):
    q=sum(x*x for x in a)
    if not q:return (),Q(0)
    # low bit i, high bit j: a00,a10,a01,a11
    u,v,w,z=a
    zz=Hweights([x*x for x in a],q)
    xz=Hweights([(u+v)**2,(u-v)**2,(w+z)**2,(w-z)**2],2*q)
    zx=Hweights([(u+w)**2,(v+z)**2,(u-w)**2,(v-z)**2],2*q)
    xx=Hweights([(u+v+w+z)**2,(u-v+w-z)**2,(u+v-w-z)**2,(u-v-w+z)**2],4*q)
    return M.add((1,xz),(1,zx),(-1,zz),(-1,xx)),Q(v*v+w*w+2*z*z,q)
spec={'helper_version':'pair-row-scalar-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'normalized real retained quartets, NOT claimed Boolean roots','domain':'integer quartet entries -3..3, first nonzero positive','case_count':1200,'symmetry':'global sign, entropy and influence unchanged','arithmetic':'Fraction, canonical prime-log expressions, 48-term atanh with geometric remainder and outward 96-bit logs','memory_estimate_MB':80,'max_runtime_seconds':55}
if __name__=='__main__':
    (R/'out/ROW_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n')
start=time.perf_counter();tested=0;bad=[]
for a in (itertools.product(range(-3,4),repeat=4) if __name__=='__main__' else []):
    if not any(a) or next(x for x in a if x)<0:continue
    if time.perf_counter()-start>55:raise TimeoutError('frozen cap')
    omega,d=row(a);margin=M.add((1,omega),(1,((2,2*d),)))
    lo,hi=interval(margin);tested+=1
    if hi<0:bad.append({'a':a,'queried_influence':str(d),'margin_prime_logs':[(p,str(c)) for p,c in margin],'interval':[str(lo),str(hi)]})
    elif lo<0 and margin:raise AssertionError('unresolved')
out={'quartets':tested,'violations':len(bad),'first_violations':bad[:5],'seconds':time.perf_counter()-start,'scope':'real row scalar test; no Boolean upper theorem'}
if __name__=='__main__':
    (R/'out/ROW_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
