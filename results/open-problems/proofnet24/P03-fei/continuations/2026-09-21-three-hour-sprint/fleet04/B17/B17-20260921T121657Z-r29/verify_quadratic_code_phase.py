#!/usr/bin/env python3
"""Exact checker for B17 quadratic-code phase obstruction.

Standard library only. All Walsh transforms use exact integers.
"""
import json
import math
from fractions import Fraction
from itertools import product, combinations

# Explicit s=3 simplex-radical quadratic phase on n=7 bits.
N = 7
QUAD_TERMS = [
    (0,1),(0,4),(0,6),
    (1,5),(1,6),
    (2,3),(2,4),(2,5),(2,6),
    (3,4),(3,5),(4,5),
]
# Rows span the radical R; each nonzero row-combination has weight 4.
G = [
    (0,0,0,1,1,1,1),
    (0,1,1,0,0,1,1),
    (1,0,1,0,1,0,1),
]

def dot2(a,b):
    return sum(x*y for x,y in zip(a,b)) & 1

def qval(x):
    return sum(x[i]*x[j] for i,j in QUAD_TERMS) & 1

def hval(x):
    return -1 if qval(x) else 1

def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y, x-y
        h *= 2
    return a

def idx_bits(i,n):
    return tuple((i >> j) & 1 for j in range(n))

def bits_idx(x):
    return sum((b&1)<<j for j,b in enumerate(x))

def rank_gf2(rows, n):
    rows = [sum((b&1)<<j for j,b in enumerate(r)) for r in rows if any(r)]
    rank=0
    bit=0
    while bit<n and rank<len(rows):
        pivot = next((k for k in range(rank,len(rows)) if (rows[k]>>bit)&1), None)
        if pivot is None:
            bit+=1
            continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for k in range(len(rows)):
            if k!=rank and ((rows[k]>>bit)&1):
                rows[k]^=rows[rank]
        rank+=1; bit+=1
    return rank

def entropy_from_num_weights(nums, denom):
    # nums are exact numerator probabilities over denom, sum nums = denom
    out=0.0
    for m in nums:
        if m:
            p=m/denom
            out -= p*math.log2(p)
    return out

# ---- Radical/code checks ----
assert rank_gf2(G,N)==3
R=set()
for c in product((0,1), repeat=3):
    v=tuple(sum(c[t]*G[t][j] for t in range(3))&1 for j in range(N))
    R.add(v)
weights=sorted(sum(v) for v in R if any(v))
assert len(R)==8
assert weights == [4]*7

# Polar form B(x,z)=Q(x)+Q(z)+Q(x+z). Verify radical exactly R.
def bval(x,z):
    return qval(x)^qval(z)^qval(tuple(a^b for a,b in zip(x,z)))
allv=[idx_bits(i,N) for i in range(1<<N)]
rad={z for z in allv if all(bval(x,z)==0 for x in allv)}
assert rad==R

# ---- Walsh support of h ----
truth=[hval(idx_bits(i,N)) for i in range(1<<N)]
W=fwht_int(truth)
support=[idx_bits(a,N) for a,w in enumerate(W) if w]
assert len(support)==16
assert {abs(w) for w in W if w}=={32}
assert W[0]==0   # balanced

# Affine syndrome of support with respect to G.
syndromes={tuple(dot2(g,a) for g in G) for a in support}
assert syndromes=={(1,0,0)}

# Every <=3-coordinate projection of support is uniform.
projection_counts={}
for t in range(1,4):
    for J in combinations(range(N),t):
        counts={}
        for a in support:
            key=tuple(a[j] for j in J)
            counts[key]=counts.get(key,0)+1
        expected=len(support)//(1<<t)
        assert len(counts)==1<<t and set(counts.values())=={expected}
        projection_counts[str(J)] = expected

# Total correlation of uniform support vs fair product is 7-log2(16)=3 bits.
spectral_entropy_h=math.log2(len(support))
tc_h=N-spectral_entropy_h
assert tc_h==3.0

# ---- Exact non-unateness check ----
# In {0,1} notation, a function is unate if for each coordinate its 0->1
# differences all have one weak sign (after possibly complementing that input).
direction_sets=[]
for j in range(N):
    diffs=set()
    for base in product((0,1), repeat=N-1):
        x0=list(base); x0.insert(j,0)
        x1=list(base); x1.insert(j,1)
        diffs.add(hval(tuple(x1))-hval(tuple(x0)))
    direction_sets.append(sorted(diffs))
    assert -2 in diffs and 2 in diffs
non_unate=True

# ---- Rare-selector lift F_{d,h}: h when gate is all zero, +1 otherwise ----
D=4
M=N+D
def fval(z):
    x=z[:D]; y=z[D:]
    return hval(y) if not any(x) else 1

truthF=[fval(idx_bits(i,M)) for i in range(1<<M)]
WF=fwht_int(truthF)
den=1<<M
# Squared spectral probabilities have denominator den^2.
sq=[w*w for w in WF]
assert sum(sq)==den*den

# Expected exact coefficient classes:
# main (empty) = 1-eps = 15/16 => W=1920
# gate-only nonempty = -eps => |W|=128
# phase layer = eps*(1/4) => |W|=32.
abs_hist={}
for w in WF:
    abs_hist[abs(w)]=abs_hist.get(abs(w),0)+1
assert abs_hist == {0: 1776, 32: 256, 128: 15, 1920: 1}

# Marginals exactly as rational numbers.
gate_marg=[]
phase_marg=[]
for j in range(M):
    num=sum(sq[a] for a in range(1<<M) if (a>>j)&1)
    p=Fraction(num,den*den)
    (gate_marg if j<D else phase_marg).append(p)
assert set(gate_marg)=={Fraction(1,16)}
assert set(phase_marg)=={Fraction(1,32)}

I_exact=sum(gate_marg+phase_marg, Fraction())
assert I_exact==Fraction(15,32)  # eps*(d+n/2) = (4+3.5)/16

# Exact phase-block distribution by marginalizing squared weights over gate labels.
phase_nums={}
for a,w2 in enumerate(sq):
    yidx=a>>D
    phase_nums[yidx]=phase_nums.get(yidx,0)+w2
# Normalize by den^2.
nonzero_phase=[(y,m) for y,m in phase_nums.items() if m]
# Y=0 mass = 15/16; 16 activated code labels each mass 1/256.
assert phase_nums[0]*16 == den*den*15
act=[m for y,m in nonzero_phase if y!=0]
assert len(act)==16 and len(set(act))==1
assert act[0]*256==den*den

# Conditional activated phase support must be the same affine support and <=3-wise fair.
lift_support={idx_bits(y,N) for y,m in nonzero_phase if y!=0 and m}
assert lift_support==set(support)

# Entropy/influence and TC numerical cross-checks from exact probabilities.
H_F=entropy_from_num_weights([m for m in sq if m], den*den)
eps=Fraction(1,16)
H_formula = (
    -float((1-eps)**2)*math.log2(float((1-eps)**2))
    + 4*D*float(eps)
    - 2*D*float(eps*eps)
    + float(eps)*(N-3)
)
assert abs(H_F-H_formula)<1e-12

phase_probs=[m/(den*den) for y,m in nonzero_phase]
H_Y=-sum(p*math.log2(p) for p in phase_probs)
h=lambda p: 0.0 if p in (0.0,1.0) else -p*math.log2(p)-(1-p)*math.log2(1-p)
TC_Y=N*h(1/32)-H_Y
hidden=float(eps)*3
baseline=TC_Y-hidden
assert abs(H_Y-(h(1/16)+(1/16)*4))<1e-12
assert abs(TC_Y-(N*h(1/32)-h(1/16)-(1/16)*4))<1e-12
assert abs(hidden-0.1875)<1e-15

out={
  "status":"PASS",
  "phase":{
    "n":N,
    "radical_dimension":3,
    "radical_nonzero_weights":weights,
    "walsh_support_size":len(support),
    "walsh_nonzero_abs":32,
    "normalized_fourier_nonzero_abs":"1/4",
    "support_syndrome":[1,0,0],
    "balanced":True,
    "kwise_independent_through":3,
    "spectral_entropy_bits":spectral_entropy_h,
    "total_correlation_bits":tc_h,
    "non_unate":non_unate,
    "coordinate_difference_sets":direction_sets
  },
  "rare_selector":{
    "d":D,
    "total_variables":M,
    "epsilon":"1/16",
    "walsh_abs_histogram":{str(k):v for k,v in sorted(abs_hist.items())},
    "gate_marginals":[str(x) for x in gate_marg],
    "phase_marginals":[str(x) for x in phase_marg],
    "influence":str(I_exact),
    "entropy_bits":H_F,
    "entropy_formula_bits":H_formula,
    "phase_block_entropy_bits":H_Y,
    "phase_block_total_correlation_bits":TC_Y,
    "hidden_code_term_bits":hidden,
    "other_phase_tc_bits":baseline,
    "activated_phase_support_size":len(lift_support),
    "activated_phase_kwise_independent_through":3
  }
}
print(json.dumps(out,indent=2,sort_keys=True))
