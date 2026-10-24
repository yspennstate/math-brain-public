import math, functools, json

CSTAR = 2.0 / math.log(2.0)

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1.0-x)*math.log2(1.0-x)

def jfun(s):
    return 1.0 - h2(0.5 + math.sqrt(s*(1.0-s)))

def rho(q):
    s = min(q, 1.0-q)
    return CSTAR*(q-s) + (CSTAR*(s-s*s/3.0) - jfun(s))

def qd(d):
    return 1.0/(1.0 + 2.0**(2.0-2.0/d))

def fwht(vals):
    a = [float(x) for x in vals]
    h = 1
    n = len(a)
    while h < n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h *= 2
    return [x/n for x in a]

def spectral_stats(values,m,coord):
    coeff = fwht(values)
    p = [x*x for x in coeff]
    B=M=Q=0.0
    bit=1<<coord
    for T in range(1<<m):
        if T & bit:
            continue
        x,y=p[T],p[T|bit]
        w=x+y
        if w == 0.0:
            continue
        s=min(x,y)/w
        B += w*h2(s)
        M += w*s
        Q += w*s*s
    infl=sum(p[T] for T in range(1<<m) if T&bit)
    return B,M,Q,infl

def restrict_values(values,m,coord,valbit):
    out=[]
    for mask in range(1<<(m-1)):
        low=mask & ((1<<coord)-1)
        high=mask>>coord
        full=low | (valbit<<coord) | (high<<(coord+1))
        out.append(values[full])
    return tuple(out)

@functools.lru_cache(None)
def phi(values):
    m=len(values).bit_length()-1
    if all(v==values[0] for v in values):
        return 0.0
    best=float("inf")
    for i in range(m):
        B,M,Q,p=spectral_stats(values,m,i)
        v0=restrict_values(values,m,i,0)
        v1=restrict_values(values,m,i,1)
        cost=B-(CSTAR/3.0)*Q+0.5*(phi(v0)+phi(v1))
        best=min(best,cost)
    return best

def entropy_influence(values):
    coeff=fwht(values)
    p=[x*x for x in coeff]
    H=-sum(q*math.log2(q) for q in p if q>0.0)
    I=sum(q*mask.bit_count() for mask,q in enumerate(p))
    return H,I

def width2_tribes(s):
    n=2*s
    out=[]
    for mask in range(1<<n):
        bad=any(((mask>>(2*j))&1) and ((mask>>(2*j+1))&1) for j in range(s))
        out.append(-1 if bad else 1)
    return tuple(out)

def tensor(v1,v2):
    n1=len(v1).bit_length()-1
    n2=len(v2).bit_length()-1
    return tuple(v1[m & ((1<<n1)-1)] * v2[m>>n1] for m in range(1<<(n1+n2)))

reserve=[]
for d in [1,2,3,5,10,15,30,100]:
    q=qd(d)
    r=rho(q)
    reserve.append({
        "degree":d,
        "q_d":q,
        "rho_q_d":r,
        "weighted_seed":(4.0**(1-d))*r,
    })

tribes=[]
for s in range(1,6):
    phi.cache_clear()
    v=width2_tribes(s)
    ph=phi(v)
    H,I=entropy_influence(v)
    tribes.append({
        "tribes":s,
        "variables":2*s,
        "H_over_I":H/I,
        "Phi_over_I":ph/I,
        "Cstar_plus_Phi_over_I":CSTAR+ph/I,
        "accumulated_reserve_over_I":CSTAR+ph/I-H/I,
    })

f=width2_tribes(1)
g=tuple(1 if mask.bit_count()<=1 else -1 for mask in range(8))
phi.cache_clear(); pf=phi(f)
phi.cache_clear(); pg=phi(g)
phi.cache_clear(); pfg=phi(tensor(f,g))
tensor_check={
    "Phi_f":pf,
    "Phi_g":pg,
    "Phi_tensor":pfg,
    "Phi_f_plus_Phi_g":pf+pg,
    "abs_error":abs(pfg-(pf+pg)),
}
print(json.dumps({
    "cstar":CSTAR,
    "reserve_seed_table":reserve,
    "width2_tribes_bellman_demo":tribes,
    "tensor_additivity_demo":tensor_check,
}, indent=2, sort_keys=True))
