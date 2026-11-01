#!/usr/bin/env python3
import math, random, json, hashlib

SEED = 20260920
random.seed(SEED)

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def fwht(vals):
    a=[float(x) for x in vals]
    h=1
    n=len(a)
    while h<n:
        for s in range(0,n,2*h):
            for j in range(s,s+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return [x/n for x in a]

def entropy_coeff(coeff):
    out=0.0
    for x in coeff:
        p=x*x
        if p>0:
            out -= p*math.log2(p)
    return out

def H(f):
    return entropy_coeff(fwht(f))

def restrict_fun(f,n,k,b):
    out=[]
    for y in range(1<<(n-1)):
        lo=y & ((1<<k)-1)
        hi=y>>k
        x=lo | (b<<k) | (hi<<(k+1))
        out.append(f[x])
    return out

def deriv(f,n,k):
    a=restrict_fun(f,n,k,0)
    b=restrict_fun(f,n,k,1)
    return [x*y for x,y in zip(a,b)]

def influence(f,n,k):
    return sum(f[x] != f[x^(1<<k)] for x in range(1<<n))/(1<<n)

def J(f,n):
    s=0.0
    for k in range(n):
        a=influence(f,n,k)
        s += min(a,1-a)
    return s

def E1(f,n):
    return sum(H(deriv(f,n,k)) for k in range(n)) if n else 0.0

def B_i(f,n,k):
    c=fwht(f)
    p=[x*x for x in c]
    ans=0.0
    for t in range(1<<n):
        if t&(1<<k):
            continue
        a=p[t]; b=p[t|(1<<k)]
        q=a+b
        if q:
            ans += q*h2(b/q)
    return ans

def quadratic_phase(n,const,linear,edges):
    vals=[]
    for x in range(1<<n):
        q=const
        for i in range(n):
            if (linear>>i)&1:
                q ^= (x>>i)&1
        for i,j in edges:
            q ^= ((x>>i)&1) & ((x>>j)&1)
        vals.append(-1 if q else 1)
    return vals

def all_quadratic_phases(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for mask in range(1<<(1+n+len(pairs))):
        const=mask&1
        linear=(mask>>1)&((1<<n)-1)
        em=(mask>>(1+n))
        edges=[pairs[t] for t in range(len(pairs)) if (em>>t)&1]
        yield quadratic_phase(n,const,linear,edges)

def tensor(f,g):
    return [f[x]*g[y] for y in range(len(g)) for x in range(len(f))]

CROOT=4.0+2.0/math.log(2)
exhaustive={}
max_local=0.0
max_root=0.0
max_step=0.0
coordinate_cases=0
for n in range(1,5):
    N=1<<n
    nf=1<<N
    exhaustive[str(n)]=nf
    for mask in range(nf):
        f=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        hf=H(f); jf=J(f,n); e1=E1(f,n)
        max_root=max(max_root, hf-0.25*e1-CROOT*jf)
        for k in range(n):
            coordinate_cases += 1
            a=influence(f,n,k); j=min(a,1-a)
            hd=H(deriv(f,n,k))
            max_local=max(max_local, B_i(f,n,k)-0.25*hd-4.0*j)
            fp=restrict_fun(f,n,k,0); fm=restrict_fun(f,n,k,1)
            rhs=hd+0.5*(E1(fp,n-1)+E1(fm,n-1))
            max_step=max(max_step, rhs-e1)

# Quadratic-twist invariance E1((-1)^Q f)=E1(f), exhaustive through n=3.
max_quad_err=0.0
quad_cases=0
for n in range(1,4):
    N=1<<n
    phases=list(all_quadratic_phases(n))
    for mask in range(1<<N):
        f=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        base=E1(f,n)
        for q in phases:
            F=[a*b for a,b in zip(f,q)]
            max_quad_err=max(max_quad_err,abs(E1(F,n)-base))
            quad_cases += 1

# Tensor additivity of E1 and J on deterministic random cases.
max_tensor_e1_err=0.0
max_tensor_j_err=0.0
tensor_cases=0
for _ in range(1000):
    n=random.randint(1,3); m=random.randint(1,3)
    f=[random.choice((-1,1)) for _ in range(1<<n)]
    g=[random.choice((-1,1)) for _ in range(1<<m)]
    fg=tensor(f,g)
    max_tensor_e1_err=max(max_tensor_e1_err,abs(E1(fg,n+m)-E1(f,n)-E1(g,m)))
    max_tensor_j_err=max(max_tensor_j_err,abs(J(fg,n+m)-J(f,n)-J(g,m)))
    tensor_cases += 1

# One-point obstruction: E1(w_n)/J(w_n)=2^(n-1) H(w_(n-1)).
one_point=[]
for n in range(2,21):
    m=n-1
    A=(1-2**(1-m))**2
    b=2**(2-2*m)
    hw=0.0
    if A>0:
        hw -= A*math.log2(A)
    hw -= (2**m-1)*b*math.log2(b)
    ratio=(2**(n-1))*hw
    one_point.append({"n":n,"E1_over_J":ratio})

# Scalar inequality underlying local theorem.
max_scalar_violation=0.0
for k in range(1,100001):
    p=0.5*k/100000
    r=4*p*(1-p)
    max_scalar_violation=max(max_scalar_violation,h2(p)-0.25*h2(r)-4*p)

# Cubic-star obstruction to paying derivative entropy by queried influence.
cubic_star=[]
for r in range(1,17):
    alpha=(1-2**(-r))/2
    h_derivative=2*r  # q_r is tensor product of r two-variable quadratic phases, entropy 2r.
    cubic_star.append({
        "r":r,
        "query_j":alpha,
        "H_D_query":h_derivative,
        "H_D_over_j":h_derivative/alpha
    })

# Sanity check for the robust sparse-physical-defect extension of the
# current quadratic-twist/part-symmetric theorem.
# Generate a random d-part-symmetric core h, flip k truth-table entries,
# apply an arbitrary quadratic phase, and test H <= (12.04+log2(d)+k) J.
def random_part_symmetric(n,d):
    # deterministic nonempty consecutive partition
    labels=[min(d-1,(i*d)//n) for i in range(n)]
    present=sorted(set(labels))
    remap={a:t for t,a in enumerate(present)}
    labels=[remap[a] for a in labels]
    d0=len(present)
    table={}
    vals=[]
    for x in range(1<<n):
        counts=tuple(sum((x>>i)&1 for i in range(n) if labels[i]==a) for a in range(d0))
        if counts not in table:
            table[counts]=random.choice((-1,1))
        vals.append(table[counts])
    return vals,d0

robust_cases=0
max_robust_violation=0.0
for _ in range(3000):
    n=random.randint(2,6)
    d=random.randint(1,min(3,n))
    h,d0=random_part_symmetric(n,d)
    k=random.randint(1,min(3,1<<n))
    defect=set(random.sample(range(1<<n),k))
    g=[-1 if x in defect else 1 for x in range(1<<n)]
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    const=random.randint(0,1)
    linear=random.randrange(1<<n)
    edges=[e for e in pairs if random.randint(0,1)]
    q=quadratic_phase(n,const,linear,edges)
    F=[a*b*c for a,b,c in zip(h,g,q)]
    bound=(12.04+math.log2(d0)+k)*J(F,n)
    max_robust_violation=max(max_robust_violation,H(F)-bound)
    robust_cases += 1

out={
  "status":"PASS",
  "seed":SEED,
  "arithmetic":"Truth tables/influences exact integer counts; entropies IEEE-754 sanity checks.",
  "exhaustive_boolean_functions_by_dimension":exhaustive,
  "exhaustive_coordinate_cases":coordinate_cases,
  "max_local_derivative_entropy_payment_violation":max_local,
  "max_root_derivative_entropy_bound_violation":max_root,
  "max_one_step_E1_supermartingale_violation":max_step,
  "quadratic_twist_E1_cases":quad_cases,
  "max_quadratic_twist_E1_invariance_error":max_quad_err,
  "tensor_cases":tensor_cases,
  "max_tensor_E1_additivity_error":max_tensor_e1_err,
  "max_tensor_J_additivity_error":max_tensor_j_err,
  "max_scalar_grid_violation":max_scalar_violation,
  "one_point_obstruction":one_point,
  "cubic_star_derivative_entropy_query_obstruction":cubic_star,
  "robust_sparse_defect_random_cases":robust_cases,
  "max_robust_sparse_defect_FEI_violation":max_robust_violation,
  "scope":"Finite self-check only. Universal claims rely on the written proofs; this is not independent validation, Lean verification, or source closure."
}
print(json.dumps(out,indent=2))
