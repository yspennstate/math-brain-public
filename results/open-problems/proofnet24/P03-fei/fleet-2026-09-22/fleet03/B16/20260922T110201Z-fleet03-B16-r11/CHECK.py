#!/usr/bin/env python3
import math, random, json

LN2 = math.log(2.0)
TOL = 5e-10

def kl_bits(P,Q):
    z=0.0
    for p,q in zip(P,Q):
        if p:
            if q <= 0:
                return math.inf
            z += p*math.log2(p/q)
    return z

def bridge(P,Q,t):
    logs=[(1.0-t)*math.log(p)+t*math.log(q) for p,q in zip(P,Q)]
    m=max(logs)
    w=[math.exp(x-m) for x in logs]
    Z=sum(w)
    return [x/Z for x in w]

def bridge_data(P,Q,t):
    L=[math.log2(p/q) for p,q in zip(P,Q)]
    r=bridge(P,Q,t)
    mean=sum(x*l for x,l in zip(r,L))
    var=sum(x*(l-mean)**2 for x,l in zip(r,L))
    J=[[LN2*r[i]*r[j]*(L[i]-L[j]) for j in range(len(r))]
       for i in range(len(r))]
    div=[sum(row) for row in J]
    dr=[-LN2*r[i]*(L[i]-mean) for i in range(len(r))]
    pair=0.5*sum(J[i][j]*(L[i]-L[j])
                 for i in range(len(r)) for j in range(len(r)))
    return L,r,mean,var,J,div,dr,pair

def simpson(f,n=2000):
    assert n%2==0
    h=1.0/n
    z=f(0.0)+f(1.0)
    z += 4.0*sum(f((2*k-1)*h) for k in range(1,n//2+1))
    z += 2.0*sum(f((2*k)*h) for k in range(1,n//2))
    return z*h/3.0

def action_integrand(P,Q,t):
    L,r,mean,var,*_=bridge_data_light(P,Q,t)
    return (1.0-t)*LN2*var

def bridge_data_light(P,Q,t):
    L=[math.log2(p/q) for p,q in zip(P,Q)]
    r=bridge(P,Q,t)
    mean=sum(x*l for x,l in zip(r,L))
    var=sum(x*(l-mean)**2 for x,l in zip(r,L))
    return L,r,mean,var

def walsh_coeff(vals,n):
    N=1<<n
    return [sum(vals[x]*(-1 if ((x&s).bit_count()&1) else 1)
                for x in range(N))/N for s in range(N)]

def solve_c(rs):
    mu=sum(rs)
    if abs(mu-1.0) < 1e-14:
        return None
    lo,hi=1e-15,1.0
    def g(c):
        return (1.0-c)-math.prod(1.0-c*r for r in rs)
    for _ in range(180):
        mid=(lo+hi)/2.0
        if g(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

def q_r(rs):
    c=solve_c(rs)
    if c is None:
        raise ValueError("mu=1 singleton case not used in this check")
    ts=[c*r for r in rs]
    N=1<<len(rs)
    out=[]
    for s in range(1,N):
        p=1.0
        for i,t in enumerate(ts):
            p *= t if ((s>>i)&1) else (1.0-t)
        out.append(p/c)
    return c,out

def maj3(a,b,c):
    return 1 if a+b+c >= 1 else -1

rng=random.Random(20260922)
max_conservation=0.0
max_dirichlet=0.0
max_integral=0.0
positive_cases=0
for nstates in (2,3,4,7):
    for _ in range(5):
        rp=[rng.random()+0.05 for _ in range(nstates)]
        rq=[rng.random()+0.05 for _ in range(nstates)]
        sp,sq=sum(rp),sum(rq)
        P=[x/sp for x in rp]
        Q=[x/sq for x in rq]
        D=kl_bits(P,Q)
        A=simpson(lambda t: action_integrand(P,Q,t), n=1200)
        max_integral=max(max_integral,abs(D-A))
        for t in (0.07,0.23,0.51,0.88):
            L,r,mean,var,J,div,dr,pair=bridge_data(P,Q,t)
            max_conservation=max(max_conservation,
                max(abs(dr[i]+div[i]) for i in range(nstates)))
            max_dirichlet=max(max_dirichlet,abs(pair-LN2*var))
        positive_cases += 1

# Exhaustive n=3 Boolean Walsh-convolution identity.
max_boolean_conv=0.0
for truthmask in range(1<<(1<<3)):
    vals=[1 if ((truthmask>>x)&1) else -1 for x in range(8)]
    a=walsh_coeff(vals,3)
    for u in range(8):
        conv=sum(a[s]*a[s^u] for s in range(8))
        want=1.0 if u==0 else 0.0
        max_boolean_conv=max(max_boolean_conv,abs(conv-want))

# Translation-fiber partition of the complete-graph action.
rawp=[rng.random()+0.2 for _ in range(8)]
rawq=[rng.random()+0.2 for _ in range(8)]
P=[x/sum(rawp) for x in rawp]
Q=[x/sum(rawq) for x in rawq]
L,r,mean,var,J,div,dr,pair=bridge_data(P,Q,0.37)
fiber=0.0
for u in range(1,8):
    fiber += 0.5*sum(J[s][s^u]*(L[s]-L[s^u]) for s in range(8))
fiber_error=abs(fiber-pair)

# Mandatory recursive-majority preflight, depth two (9 variables).
n=9
N=1<<n
vals=[]
for x in range(N):
    bits=[1 if ((x>>i)&1)==0 else -1 for i in range(n)]
    inner=[maj3(*bits[3*j:3*j+3]) for j in range(3)]
    vals.append(maj3(*inner))
a=walsh_coeff(vals,n)
Pfull=[x*x for x in a]
assert abs(Pfull[0]) < 1e-15
P=Pfull[1:]
rs=[sum(Pfull[s] for s in range(1,N) if ((s>>i)&1)) for i in range(n)]
c,Q=q_r(rs)
Kocc=kl_bits(P,Q)
eps=1e-5
Pe=[(1.0-eps)*p+eps*q for p,q in zip(P,Q)]
Keps=kl_bits(Pe,Q)
Aeps=simpson(lambda t: action_integrand(Pe,Q,t),n=4000)
majority_action_error=abs(Keps-Aeps)

# Rare-event log sanity: exact KL grows like delta*m while unweighted L2 is O(delta^2).
delta=2.0**-12
m=40
Prare=[1.0-delta,delta]
Qrare=[1.0-delta*(2.0**-m),delta*(2.0**-m)]
rare_kl=kl_bits(Prare,Qrare)
rare_l2=sum((p-q)**2 for p,q in zip(Prare,Qrare))
rare_ratio=rare_kl/rare_l2

checks = {
    "positive_distribution_cases": positive_cases,
    "max_atomwise_conservation_error": max_conservation,
    "max_dirichlet_identity_error": max_dirichlet,
    "max_KL_action_integral_error": max_integral,
    "exhaustive_n3_boolean_functions": 256,
    "max_full_Walsh_convolution_error": max_boolean_conv,
    "translation_fiber_partition_error": fiber_error,
    "recursive_majority_depth": 2,
    "recursive_majority_variables": 9,
    "recursive_majority_Kocc_bits": Kocc,
    "regularization_epsilon": eps,
    "recursive_majority_regularized_KL_bits": Keps,
    "recursive_majority_action_bits": Aeps,
    "recursive_majority_action_error": majority_action_error,
    "rare_event_m": m,
    "rare_event_delta": delta,
    "rare_event_KL_bits": rare_kl,
    "rare_event_unweighted_L2": rare_l2,
    "rare_event_KL_to_L2_ratio": rare_ratio,
}
ok = (
    max_conservation < TOL and
    max_dirichlet < TOL and
    max_integral < 1e-9 and
    max_boolean_conv < TOL and
    fiber_error < TOL and
    majority_action_error < 1e-9 and
    rare_ratio > 1e4
)
print("PASS" if ok else "FAIL")
print(json.dumps(checks, indent=2, sort_keys=True))
if not ok:
    raise SystemExit(1)
