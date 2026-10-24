from fractions import Fraction
from itertools import combinations, permutations
import numpy as np

SCALE = 10**9
LOG_TERMS = 12
REPS = {
  1: [(0,)],
  2: [(0, 1), (0, 3), (0, 7), (0, 15), (0, 31)],
  3: [(0, 1, 2), (0, 1, 6), (0, 1, 14), (0, 1, 30), (0, 3, 5), (0, 3, 12), (0, 3, 13), (0, 3, 28), (0, 3, 29), (0, 7, 25)],
  4: [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 5), (0, 1, 2, 7), (0, 1, 2, 12), (0, 1, 2, 13), (0, 1, 2, 15), (0, 1, 2, 28), (0, 1, 2, 29), (0, 1, 2, 31), (0, 1, 6, 7), (0, 1, 6, 10), (0, 1, 6, 11), (0, 1, 6, 14), (0, 1, 6, 15), (0, 1, 6, 24), (0, 1, 6, 25), (0, 1, 6, 26), (0, 1, 6, 27), (0, 1, 6, 30), (0, 1, 6, 31), (0, 1, 14, 15), (0, 1, 14, 22), (0, 1, 14, 23), (0, 1, 14, 30), (0, 1, 14, 31), (0, 1, 30, 31), (0, 3, 5, 6), (0, 3, 5, 9), (0, 3, 5, 10), (0, 3, 5, 14), (0, 3, 5, 24), (0, 3, 5, 25), (0, 3, 5, 26), (0, 3, 5, 30), (0, 3, 12, 15), (0, 3, 12, 21), (0, 3, 12, 23), (0, 3, 12, 31), (0, 3, 13, 14), (0, 3, 13, 21), (0, 3, 13, 22), (0, 3, 13, 28), (0, 3, 13, 30), (0, 3, 28, 31), (0, 3, 29, 30), (0, 7, 25, 30)],
  5: [(0, 1, 2, 3, 4), (0, 1, 2, 3, 12), (0, 1, 2, 3, 28), (0, 1, 2, 4, 7), (0, 1, 2, 4, 8), (0, 1, 2, 4, 9), (0, 1, 2, 4, 11), (0, 1, 2, 4, 15), (0, 1, 2, 4, 24), (0, 1, 2, 4, 25), (0, 1, 2, 4, 27), (0, 1, 2, 4, 31), (0, 1, 2, 5, 6), (0, 1, 2, 5, 10), (0, 1, 2, 5, 11), (0, 1, 2, 5, 14), (0, 1, 2, 5, 24), (0, 1, 2, 5, 26), (0, 1, 2, 5, 27), (0, 1, 2, 5, 30), (0, 1, 2, 7, 11), (0, 1, 2, 7, 12), (0, 1, 2, 7, 13), (0, 1, 2, 7, 15), (0, 1, 2, 7, 24), (0, 1, 2, 7, 25), (0, 1, 2, 7, 27), (0, 1, 2, 7, 28), (0, 1, 2, 7, 29), (0, 1, 2, 7, 31), (0, 1, 2, 12, 13), (0, 1, 2, 12, 15), (0, 1, 2, 12, 20), (0, 1, 2, 12, 21), (0, 1, 2, 12, 23), (0, 1, 2, 12, 28), (0, 1, 2, 12, 29), (0, 1, 2, 12, 31), (0, 1, 2, 13, 14), (0, 1, 2, 13, 15), (0, 1, 2, 13, 21), (0, 1, 2, 13, 22), (0, 1, 2, 13, 23), (0, 1, 2, 13, 28), (0, 1, 2, 13, 29), (0, 1, 2, 13, 30), (0, 1, 2, 13, 31), (0, 1, 2, 15, 23), (0, 1, 2, 15, 28), (0, 1, 2, 15, 29), (0, 1, 2, 15, 31), (0, 1, 2, 28, 29), (0, 1, 2, 28, 31), (0, 1, 2, 29, 30), (0, 1, 2, 29, 31), (0, 1, 6, 7, 10), (0, 1, 6, 7, 24), (0, 1, 6, 7, 26), (0, 1, 6, 10, 12), (0, 1, 6, 10, 13), (0, 1, 6, 10, 15), (0, 1, 6, 10, 18), (0, 1, 6, 10, 19), (0, 1, 6, 10, 20), (0, 1, 6, 10, 21), (0, 1, 6, 10, 22), (0, 1, 6, 10, 23), (0, 1, 6, 10, 28), (0, 1, 6, 10, 29), (0, 1, 6, 10, 30), (0, 1, 6, 10, 31), (0, 1, 6, 11, 14), (0, 1, 6, 11, 21), (0, 1, 6, 11, 22), (0, 1, 6, 11, 23), (0, 1, 6, 11, 28), (0, 1, 6, 11, 30), (0, 1, 6, 14, 23), (0, 1, 6, 14, 25), (0, 1, 6, 14, 27), (0, 1, 6, 15, 23), (0, 1, 6, 15, 24), (0, 1, 6, 15, 25), (0, 1, 6, 15, 26), (0, 1, 6, 15, 27), (0, 1, 6, 15, 30), (0, 1, 6, 15, 31), (0, 1, 6, 24, 30), (0, 1, 6, 24, 31), (0, 1, 6, 25, 30), (0, 1, 6, 26, 27), (0, 1, 6, 26, 28), (0, 1, 6, 26, 29), (0, 1, 6, 26, 31), (0, 1, 6, 27, 29), (0, 1, 6, 27, 30), (0, 1, 6, 27, 31), (0, 1, 6, 30, 31), (0, 1, 14, 22, 26), (0, 1, 14, 22, 27), (0, 1, 14, 22, 31), (0, 3, 5, 6, 9), (0, 3, 5, 6, 24), (0, 3, 5, 6, 25), (0, 3, 5, 9, 14), (0, 3, 5, 9, 17), (0, 3, 5, 9, 18), (0, 3, 5, 9, 22), (0, 3, 5, 9, 30), (0, 3, 5, 10, 12), (0, 3, 5, 10, 20), (0, 3, 5, 10, 22), (0, 3, 5, 10, 28), (0, 3, 5, 10, 29), (0, 3, 5, 14, 22), (0, 3, 5, 14, 24), (0, 3, 5, 14, 25), (0, 3, 5, 14, 26), (0, 3, 5, 24, 27), (0, 3, 5, 24, 30), (0, 3, 5, 24, 31), (0, 3, 5, 25, 26), (0, 3, 5, 25, 30), (0, 3, 5, 26, 28), (0, 3, 12, 15, 21), (0, 3, 12, 21, 22), (0, 3, 12, 21, 26), (0, 3, 12, 21, 27), (0, 3, 12, 21, 31), (0, 3, 12, 23, 29), (0, 3, 13, 21, 26)],
}

def ceil_fraction(x):
    return (x.numerator + x.denominator - 1)//x.denominator

def ln_atanh_partial(z, terms):
    s=Fraction(0)
    zz=z
    z2=z*z
    for k in range(terms):
        s += zz/(2*k+1)
        zz *= z2
    return 2*s

def ln_atanh_upper(z, terms):
    if z == 0:
        return Fraction(0)
    s=ln_atanh_partial(z, terms)
    N=terms
    tail = 2*z**(2*N+1) / ((2*N+1)*(1-z*z))
    return s+tail

LN2_LO = ln_atanh_partial(Fraction(1,3), LOG_TERMS)

def log2_upper(x):
    assert x >= 1
    k=0
    y=x
    while y >= 2:
        y /= 2
        k += 1
    z=(y-1)/(y+1)
    return Fraction(k) + ln_atanh_upper(z, LOG_TERMS)/LN2_LO

ENT_UP = np.zeros(65, dtype=np.int64)
for h in range(1,65):
    p=Fraction(h*h,4096)
    if p == 1:
        up=Fraction(0)
    else:
        up=p*log2_upper(1/p)
    ENT_UP[h]=ceil_fraction(up*SCALE)

CH=np.empty((32,32),dtype=np.int16)
for s in range(32):
    for y in range(32):
        CH[s,y] = -1 if ((s & y).bit_count() & 1) else 1
WT=np.array([s.bit_count() for s in range(32)],dtype=np.int64)

PERMS=list(permutations(range(5)))
PMAPS=[]
for p in PERMS:
    mp=[]
    for x in range(32):
        y=0
        for old in range(5):
            if (x>>old)&1:
                y |= 1<<p[old]
        mp.append(y)
    PMAPS.append(mp)

def orbit_cover(reps,r):
    covered=set()
    for rep in reps:
        for mp in PMAPS:
            base=[mp[x] for x in rep]
            for t in range(32):
                covered.add(tuple(sorted(x^t for x in base)))
    target=set(combinations(range(32),r))
    assert covered == target, (r,len(covered),len(target))
    return len(target)

def A_matrix(subs):
    out=np.empty((len(subs),32),dtype=np.int16)
    for row,sub in enumerate(subs):
        out[row,:]=CH[:,sub].sum(axis=1)
    return out

def A_one(sub):
    return CH[:,sub].sum(axis=1).astype(np.int16)

results=[]
global_min=None
for r in range(1,6):
    reps=REPS[r]
    count=orbit_cover(reps,r)
    subs=list(combinations(range(32),r))
    AMS=A_matrix(subs)
    local_min=None
    local_arg=None
    checked=0
    for ep in reps:
        AP=A_one(ep)
        h0=2*(AMS-AP[None,:])
        h1=-2*(AMS+AP[None,:])
        h1=h1.copy()
        h1[:,0]=64-4*r
        Hsc=(ENT_UP[np.abs(h0)].sum(axis=1)+ENT_UP[np.abs(h1)].sum(axis=1)).astype(np.int64)
        sq0=h0.astype(np.int64)**2
        sq1=h1.astype(np.int64)**2
        Inum=(sq0@WT)+(sq1@(WT+1))
        gap_num=6*(Inum-4096)*SCALE - Hsc*4096
        j=int(np.argmin(gap_num))
        g=int(gap_num[j])
        assert g>0, (r,ep,subs[j],g,int(Hsc[j]),int(Inum[j]))
        if local_min is None or g<local_min:
            local_min=g
            local_arg=(ep,subs[j],int(Hsc[j]),int(Inum[j]))
        checked += len(subs)
    if global_min is None or local_min<global_min[0]:
        global_min=(local_min,r,local_arg)
    results.append((r,len(reps),count,checked,local_min,local_arg))

print("PASS=True")
print("statement=balanced six-bit f with some |hat_f(i)|>=11/16 obeys H(f)<6*(I(f)-1), unless f is a literal where equality 0=0")
print("entropy_upper_scale=", SCALE)
print("ln_terms=", LOG_TERMS)
for row in results:
    r,nrep,nsub,checked,g,arg=row
    print("r",r,"orbit_reps",nrep,"all_half_subsets",nsub,"pairs_checked",checked,
          "certified_gap_lower",g/(4096*SCALE),"arg",arg)
print("total_pairs_checked",sum(x[3] for x in results))
print("global_certified_gap_lower",global_min[0]/(4096*SCALE),"at_r",global_min[1],"arg",global_min[2])
