import math, random
import numpy as np

TOL=2e-10

def fwht(vals):
    a=np.array(vals,dtype=float).copy(); n=len(a); h=1
    while h<n:
        for s in range(0,n,2*h):
            x=a[s:s+h].copy(); y=a[s+h:s+2*h].copy()
            a[s:s+h]=x+y; a[s+h:s+2*h]=x-y
        h*=2
    return a/n

def entropy_coeff(c):
    p=c*c; nz=p>1e-18
    return float(-(p[nz]*np.log2(p[nz])).sum())

def restrict(vals,n,i,b):
    out=np.empty(1<<(n-1),dtype=int)
    for y in range(1<<(n-1)):
        x=(y & ((1<<i)-1)) | (b<<i) | ((y>>i)<<(i+1))
        out[y]=vals[x]
    return out

def translate(vals,v):
    N=len(vals)
    return vals[np.arange(N)^v]

def influence_total(vals,n):
    if n==0: return 0.0
    N=1<<n; idx=np.arange(N); ans=0.0
    for i in range(n):
        mask=1<<i; base=idx[(idx&mask)==0]
        ans += float(np.mean(vals[base]!=vals[base|mask]))
    return ans

def influence_coord(vals,n,i):
    N=1<<n; idx=np.arange(N); mask=1<<i; base=idx[(idx&mask)==0]
    return float(np.mean(vals[base]!=vals[base|mask]))

def residual_vector(v,i):
    return (v & ((1<<i)-1)) | ((v>>(i+1))<<i)

def local_quantities(vals,n,i,v):
    g=restrict(vals,n,i,0); h=restrict(vals,n,i,1)
    w=residual_vector(v,i); ht=translate(h,w)
    d=g*ht
    neg=float(np.mean(d==-1)); delta=min(neg,1-neg)
    a=fwht(g); b=fwht(h)
    P=a*a; Q=b*b; q=(P+Q)/2
    m=(np.abs(a)-np.abs(b))**2/4
    M=float(m.sum())
    r=np.zeros_like(q); nz=q>1e-18; r[nz]=m[nz]/q[nz]
    hh=np.zeros_like(r); mid=(r>1e-18)&(r<1-1e-18)
    hh[mid]=-r[mid]*np.log2(r[mid])-(1-r[mid])*np.log2(1-r[mid])
    B=float((q*hh).sum())
    H=entropy_coeff(fwht(vals))
    DH=H-(entropy_coeff(a)+entropy_coeff(b))/2
    Id=influence_total(d,n-1)
    return M,delta,B,DH,Id

def vals_from_bits(n,bits):
    N=1<<n; vals=np.ones(N,dtype=int)
    for x in range(1,N):
        if (bits>>(x-1))&1: vals[x]=-1
    return vals

max_M_delta=-1e99; max_B_Id=-1e99; max_DH_2Id=-1e99
cases=0
for n in range(1,4):
    N=1<<n
    for bits in range(1<<(N-1)):
        vals=vals_from_bits(n,bits)
        for v in range(1,N):
            for i in range(n):
                if ((v>>i)&1)==0: continue
                M,delta,B,DH,Id=local_quantities(vals,n,i,v)
                max_M_delta=max(max_M_delta,M-delta)
                max_B_Id=max(max_B_Id,B-Id)
                max_DH_2Id=max(max_DH_2Id,DH-2*Id)
                cases+=1
                assert M<=delta+TOL
                assert B<=Id+TOL
                assert DH<=2*Id+TOL

# Deterministic dimension-4 stress sample.
rng=random.Random(20260920)
n=4; N=1<<n
sample_cases=0
for _ in range(1200):
    vals=np.array([1 if rng.getrandbits(1)==0 else -1 for _ in range(N)],dtype=int)
    vals[0]=1
    v=rng.randrange(1,N)
    piv=[i for i in range(n) if (v>>i)&1]
    i=rng.choice(piv)
    M,delta,B,DH,Id=local_quantities(vals,n,i,v)
    max_M_delta=max(max_M_delta,M-delta)
    max_B_Id=max(max_B_Id,B-Id)
    max_DH_2Id=max(max_DH_2Id,DH-2*Id)
    assert M<=delta+TOL and B<=Id+TOL and DH<=2*Id+TOL
    sample_cases+=1

# Tri-defect rigid obstruction formulas and direct transform checks, n=4..12.
tri=[]
for n in range(4,13):
    N=1<<n
    vals=np.ones(N,dtype=int)
    defects=[0,N-1,1] # e_1 is bit 0
    vals[defects]=-1
    v=N-1; i=0
    M,delta,B,DH,Id=local_quantities(vals,n,i,v)
    I=influence_total(vals,n); infi=influence_coord(vals,n,i)
    g=restrict(vals,n,i,0); h=restrict(vals,n,i,1)
    minchild=min(influence_total(g,n-1),influence_total(h,n-1))
    di=g*h
    half_coord_deriv=0.5*influence_total(di,n-1)
    I_formula=(3*n-2)*2**(1-n)
    inf_formula=2**(1-n)
    Id_formula=(n-1)*2**(2-n)
    assert abs(I-I_formula)<TOL
    assert abs(infi-inf_formula)<TOL
    assert abs(Id-Id_formula)<TOL
    assert abs(minchild/infi-2*(n-1))<TOL
    assert abs(half_coord_deriv/infi-(n-1))<TOL
    # no nonzero positive signed translation symmetry; negative impossible by cardinality.
    for u in range(1,N):
        assert not np.array_equal(translate(vals,u),vals)
        assert not np.array_equal(translate(vals,u),-vals)
    tri.append((n,M,delta,B,DH,Id/I,minchild/infi,half_coord_deriv/infi))

print('PASS')
print('exhaustive_oblique_cases_n_le_3',cases)
print('dimension4_sample_cases',sample_cases)
print('max_M_minus_delta',repr(max_M_delta))
print('max_B_minus_I_d',repr(max_B_Id))
print('max_DeltaH_minus_2I_d',repr(max_DH_2Id))
print('tri_defect_columns n M delta B DeltaH Id_over_I minor_ratio half_coord_deriv_ratio')
for row in tri:
    print(*[f'{x:.15g}' if isinstance(x,float) else x for x in row])
