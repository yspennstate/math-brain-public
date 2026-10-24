from fractions import Fraction
import math

K0 = 4.0 + (1.0 + 2.0/math.e)/math.log(2.0)

def phi(x):
    if x == 0.0:
        return 0.0
    return x*math.log2(1.0/x)

def walsh(vals):
    N=len(vals); n=N.bit_length()-1
    out=[]
    for s in range(N):
        z=0
        for x,v in enumerate(vals):
            z += v * (-1 if ((s & x).bit_count() & 1) else 1)
        out.append(Fraction(z,N))
    return out

def entropy_influence(vals):
    a=walsh(vals)
    probs=[c*c for c in a]
    H=sum(float(p)*math.log2(1.0/float(p)) for p in probs if p)
    I=sum(s.bit_count()*float(p) for s,p in enumerate(probs))
    mean=float(a[0])
    return H,I,mean,a

def mux(g,h):
    # Selector bit is least significant; then g variables; then h variables.
    ng=(len(g)).bit_length()-1
    nh=(len(h)).bit_length()-1
    vals=[]
    for idx in range(1<<(1+ng+nh)):
        sel=idx&1
        gx=(idx>>1)&((1<<ng)-1)
        hx=(idx>>(1+ng))&((1<<nh)-1)
        vals.append(g[gx] if sel==0 else h[hx])
    return vals

def scalar_overhead(a,b):
    q0=(a+b)**2/4.0
    q1=(a-b)**2/4.0
    return (1-a*a)+(1-b*b)+phi(q0)+phi(q1)-0.5*phi(a*a)-0.5*phi(b*b)

# Exhaustive exact coefficient / identity check for every pair of 2-bit Boolean branches.
funcs=[]
for mask in range(16):
    vals=[1 if (mask>>x)&1 else -1 for x in range(4)]
    funcs.append(vals)

max_id_err=0.0
max_bound_ratio=0.0
worst=None
pairs=0
for g in funcs:
  Hg,Ig,a,_=entropy_influence(g)
  for h in funcs:
    Hh,Ih,b,_=entropy_influence(h)
    f=mux(g,h)
    Hf,If,_,_=entropy_influence(f)
    j=(1-a*b)/2.0
    M=scalar_overhead(a,b)
    predI=0.5*(Ig+Ih)+j
    predH=0.5*(Hg+Hh)+M
    max_id_err=max(max_id_err,abs(If-predI),abs(Hf-predH))
    if j>0:
        r=M/j
        if r>max_bound_ratio:
            max_bound_ratio=r; worst=(a,b,M,j)
    assert M <= K0*j + 1e-12
    pairs += 1

# Exact three-bit multiplexer.
g=[1,-1]
h=[1,-1]
f=mux(g,h)
Hm,Im,_,_=entropy_influence(f)

# Dense scalar stress test of the analytic K0 bound.
gridmax=(-1.0,None,None)
N=1001
for ia in range(N):
    a=-1.0+2.0*ia/(N-1)
    for ib in range(N):
        b=-1.0+2.0*ib/(N-1)
        j=(1-a*b)/2.0
        if j==0.0:
            continue
        r=scalar_overhead(a,b)/j
        if r>gridmax[0]:
            gridmax=(r,a,b)
        assert r <= K0 + 2e-12

print("K0_analytic", format(K0,'.15f'))
print("exhaustive_branch_pairs", pairs)
print("max_identity_error", format(max_id_err,'.3e'))
print("max_pair_overhead_ratio", format(max_bound_ratio,'.15f'), "worst_mean_pair", worst[:2])
print("dense_grid_max", format(gridmax[0],'.15f'), "at", gridmax[1], gridmax[2])
print("three_bit_mux_H", format(Hm,'.15f'))
print("three_bit_mux_I", format(Im,'.15f'))
print("three_bit_mux_H_over_I", format(Hm/Im,'.15f'))
print("status PASS")
