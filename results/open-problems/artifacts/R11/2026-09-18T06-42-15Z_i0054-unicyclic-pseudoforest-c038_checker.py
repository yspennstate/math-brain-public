from fractions import Fraction
from math import factorial
import json

NMAX = 30
R = 5
checks = 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def poly_add(a,b,nmax=NMAX):
    out=[Fraction(0) for _ in range(nmax+1)]
    for i in range(min(len(a),nmax+1)): out[i]+=a[i]
    for i in range(min(len(b),nmax+1)): out[i]+=b[i]
    return out

def poly_scale(a,c,nmax=NMAX):
    out=[Fraction(0) for _ in range(nmax+1)]
    for i in range(min(len(a),nmax+1)): out[i]=a[i]*c
    return out

def poly_mul(a,b,nmax=NMAX):
    out=[Fraction(0) for _ in range(nmax+1)]
    for i,ai in enumerate(a):
        if i>nmax: break
        if ai==0: continue
        for j,bj in enumerate(b):
            if i+j>nmax: break
            if bj: out[i+j]+=ai*bj
    return out

def poly_pow(a,k,nmax=NMAX):
    out=[Fraction(1)]+[Fraction(0)]*nmax
    base=a[:nmax+1]
    while k:
        if k&1: out=poly_mul(out,base,nmax)
        k//=2
        if k: base=poly_mul(base,base,nmax)
    return out

def deriv(a,r,nmax=NMAX):
    # Ordinary power-series coefficients; exact derivative.
    out=[Fraction(0) for _ in range(nmax+1)]
    for n in range(r,min(len(a),nmax+r+1)):
        if n-r<=nmax:
            out[n-r]=a[n]*Fraction(factorial(n),factorial(n-r))
    return out

# Rooted labelled tree EGF T(z): [z^n]T = n^(n-1)/n!.
T=[Fraction(0) for _ in range(NMAX+1)]
for n in range(1,NMAX+1):
    T[n]=Fraction(n**(n-1), factorial(n))

# Connected labelled simple unicyclic graph EGF
# U(z)=1/2(log(1/(1-T))-T-T^2/2).
L=[Fraction(0) for _ in range(NMAX+1)]
power=[Fraction(1)]+[Fraction(0)]*NMAX
for k in range(1,NMAX+1):
    power=poly_mul(power,T)
    L=poly_add(L,poly_scale(power,Fraction(1,k)))
T2=poly_mul(T,T)
U=poly_scale(poly_add(poly_add(L,poly_scale(T,-1)), poly_scale(T2,Fraction(-1,2))), Fraction(1,2))

# Independent direct count:
# u_n = (1/2) sum_{k=3}^n n!/(n-k)! * n^(n-k-1).
u={}
for n in range(1,NMAX+1):
    if n<3:
        direct=0
    else:
        total=Fraction(0)
        for k in range(3,n+1):
            total += Fraction(factorial(n), 2*factorial(n-k)) * Fraction(n**(n-k), n)
        ck(total.denominator==1, f"u_n integer n={n}")
        direct=total.numerator
    u[n]=direct
    ck(U[n]*factorial(n)==direct, f"U EGF identity n={n}")

ck(u[3]==1,"u3")
ck(u[4]==15,"u4")
ck(u[5]==222,"u5")

def set_partitions(n):
    if n==0:
        yield []
        return
    parts=[[[0]]]
    for x in range(1,n):
        new=[]
        for p in parts:
            for j in range(len(p)):
                q=[blk[:] for blk in p]
                q[j].append(x)
                new.append(q)
            q=[blk[:] for blk in p]+[[x]]
            new.append(q)
        parts=new
    yield from parts

def total_assembly_count(N,R=R):
    p=poly_pow(U,R,N)
    val=Fraction(factorial(N),factorial(R))*p[N]
    ck(val.denominator==1,f"assembly integer N={N}")
    return val.numerator

def numerator_visible(N, block_sizes, R=R):
    b=sum(block_sizes); q=len(block_sizes)
    if q>R or N<b: return 0
    P=[Fraction(1)]+[Fraction(0)]*(N-b)
    for s in block_sizes:
        D=deriv(U,s,N-b)
        P=poly_mul(P,D,N-b)
    P=poly_mul(P,poly_pow(U,R-q,N-b),N-b)
    coeff=P[N-b]/factorial(R-q)
    val=coeff*factorial(N-b)
    ck(val.denominator==1,f"visible numerator integer N={N} sizes={block_sizes}")
    return val.numerator

# Minimum-size exact witness.
N0=15
root_count=total_assembly_count(N0)
direct_root=factorial(15)//((factorial(3)**5)*factorial(5))
ck(root_count==direct_root,"N=15 five triangles count")
ck(root_count==1401400,"N=15 count 1401400")

# Exact visible-restriction normalization for N=15..26 and b=2..5.
norm_checks=0
for N in range(15,27):
    denom=total_assembly_count(N)
    ck(denom>0,f"positive denom N={N}")
    for b in range(2,6):
        total=Fraction(0)
        for p in set_partitions(b):
            if len(p)<=R:
                sizes=tuple(len(blk) for blk in p)
                num=numerator_visible(N,sizes)
                total += Fraction(num,denom)
        ck(total==1,f"restriction normalization N={N} b={b}: {total}")
        norm_checks += 1

# Two-label separation and deterministic component-size lower bound.
pair_data={}
for N in range(15,27):
    denom=total_assembly_count(N)
    sep=Fraction(numerator_visible(N,(1,1)),denom)
    same=Fraction(numerator_visible(N,(2,)),denom)
    ck(sep+same==1,f"pair partition N={N}")
    lower=Fraction(12*(2*N-15), N*(N-1))
    ck(sep>=lower,f"pair lower bound N={N}: {sep} < {lower}")
    lam=Fraction(1,1)/sep
    delta=Fraction(1,N*N)
    ck(delta*lam<1,f"attempt legality N={N}")
    pair_data[N]={"p_sep":str(sep),"lambda":str(lam),"lower":str(lower)}

# Exact finite diagnostics for the normalized binary beta shadow at N=30.
diag={}
N=30
denom=total_assembly_count(N)
p11=Fraction(numerator_visible(N,(1,1)),denom)
lam=1/p11
for i,j in [(1,1),(1,2),(1,3),(2,2),(2,3)]:
    if i+j<=5:
        p=Fraction(numerator_visible(N,(i,j)),denom)
        rate=lam*p
        beta=Fraction(factorial(i-1)*factorial(j-1),factorial(i+j-1))
        diag[f"{i}|{j}"]={"rate":str(rate),"beta":str(beta),"difference":str(rate-beta)}

# Full-root successful proposal has five nonempty components. At N=15 each
# connected simple unicyclic component has >=3 vertices, hence sizes 3^5.
min_shape=(3,3,3,3,3)
ck(sum(min_shape)==15,"min shape sum")
ck(all(x>=3 for x in min_shape),"min shape components")

payload={
    "claim":"R11-I0054-C038 finite core self-check",
    "model":"conditioned five-component labelled simple unicyclic pseudoforest",
    "R":R,
    "NMAX":NMAX,
    "connected_unicyclic_counts_n3_n10":{str(n):u[n] for n in range(3,11)},
    "minimum_size_N":15,
    "minimum_root_component_sizes":[3,3,3,3,3],
    "minimum_root_count":root_count,
    "normalization_checks":norm_checks,
    "pair_data_N15_N26":pair_data,
    "N30_binary_rate_diagnostics":diag,
    "exact_checks":checks,
    "result":"ALL_EXACT_CHECKS_PASS"
}
print(json.dumps(payload,indent=2,sort_keys=True))
print("ALL_EXACT_CHECKS_PASS")
