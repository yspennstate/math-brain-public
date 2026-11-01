import math
import itertools
import numpy as np
from scipy.optimize import minimize, minimize_scalar, brentq

# Deterministic two-flip truth-table check for sigma(x)=0,sigma(y)=1.
# Literal encoding: ('x',sign), sign=+1 positive, -1 negative; likewise y,z.
def litval(var, sign, x, y, z):
    v={'x':x,'y':y,'z':z}[var]
    return bool(v) if sign==1 else not bool(v)

def clause_sat(cl, x,y,z):
    return any(litval(v,s,x,y,z) for v,s in cl)

# Enumerate 3-literal clauses using x,y,z once each. Find clauses satisfied at (0,1,z),
# but falsified after simultaneous flip (1,0,z). Exclude clauses critical at x or y;
# those are controlled by the hypotheses. Remaining clauses should be exactly the
# dangerous sign pattern (not x) OR y OR (a literal false under sigma).
danger=[]
other=[]
for z0 in (0,1):
  for sx,sy,sz in itertools.product((-1,1), repeat=3):
    cl=(('x',sx),('y',sy),('z',sz))
    before=clause_sat(cl,0,1,z0); after=clause_sat(cl,1,0,z0)
    if before and not after:
      truths=[litval(v,s,0,1,z0) for v,s in cl]
      critx = truths[0] and sum(truths)==1
      crity = truths[1] and sum(truths)==1
      if not critx and not crity:
        danger.append((z0,(sx,sy,sz),truths))
        expected=(sx==-1 and sy==1 and truths[2] is False)
        if not expected: other.append((z0,(sx,sy,sz),truths))
print('TWO_FLIP_TRUTH_TABLE')
print('dangerous_noncritical_cases=', danger)
print('unexpected_cases=', other)
print('truth_table_pass=', len(other)==0 and len(danger)==2)

# Variational diagnostic for an unconditioned first-moment model of positive-weight maxima.
# p = fraction true; u = fraction true roots with zero critical clauses;
# g = fraction false singleton-critical variables whose blocking clause sees a root.
# s is the clause-count saddle. The root-occupancy factor enforces W_child <= W_root.

def H(x):
    if x <= 1e-14 or x >= 1-1e-14: return 0.0
    return -x*math.log(x)-(1-x)*math.log(1-x)

def occ_penalty(g,u):
    if g <= 1e-14: return 0.0, 0.0
    r=g/u
    def mean_occ(y):
        if y < 1e-6: return y/2+y*y/12
        return y/(-math.expm1(-y))-1
    hi=max(2.0,r+2.0)
    while mean_occ(hi)<r: hi*=2
    y=brentq(lambda yy: mean_occ(yy)-r,1e-12,hi)
    logA=math.log(math.expm1(y))-math.log(y)
    psi=g*math.log(g/u)-g + u*logA-g*math.log(y)
    return psi,y

def expo_at(p,u,g,logs,alpha,penalize=True):
    if not (0.005 < u < p < 0.995): return -1e50
    f=1-p
    if not (0 <= g < f): return -1e50
    s=math.exp(logs); x=3*s/8
    c=2*u-u*u
    E=math.expm1(x); rest=E-c*x
    if rest<=0: return -1e50
    val=H(p)+p*H(u/p)
    val += alpha*math.log(alpha)-alpha+s/2-alpha*math.log(s)
    val += (p-u)*math.log(E)
    if g <= 1e-14:
        val += f*math.log(rest)
    else:
        val += f*H(g/f)+g*math.log(c*x)+(f-g)*math.log(rest)
        if penalize: val += occ_penalty(g,u)[0]
    return val

def inner_s(p,u,g,alpha,penalize):
    rr=minimize_scalar(lambda ls:expo_at(p,u,g,ls,alpha,penalize), bounds=(0.5,2.2), method='bounded',
                       options={'xatol':1e-10})
    return rr.fun,rr.x

def phi_local(alpha, penalize=True):
    starts=[(0.544,0.076,0.0125),(0.50,0.05,0.01),(0.60,0.10,0.02),
            (0.45,0.10,0.03),(0.55,0.15,0.05)]
    best=(-1e100,None)
    def outer(z):
        p,u,g=z
        if u<=0.005 or u>=p or p>=0.995 or g<0 or g>=1-p:
            return 1e6
        v,_=inner_s(p,u,g,alpha,penalize)
        return -v
    for st in starts:
        res=minimize(outer, st, method='Nelder-Mead', options={'maxiter':900,'xatol':1e-10,'fatol':1e-11})
        p,u,g=res.x
        if 0.005<u<p<0.995 and 0<=g<1-p:
            v,ls=inner_s(p,u,g,alpha,penalize)
            if v>best[0]: best=(v,(p,u,g,math.exp(ls),occ_penalty(g,u)[1] if penalize and g>0 else 0.0))
    return best

print('\nVARIATIONAL_DIAGNOSTIC')
for a in (4.4898,4.52,4.5245,4.53):
    vp,ap=phi_local(a,True)
    vn,an=phi_local(a,False)
    print(f'alpha={a:.4f} rescue_phi={vp:.12g} rescue_arg={ap} nopair_phi={vn:.12g}')
print('NOTE: floating local optimization only; not a global or interval certificate.')
