from fractions import Fraction as Q
from itertools import combinations
from collections import Counter, defaultdict

N=6
FULL=(1<<N)-1
ALL32=(1<<32)-1

def submasks(M):
    x=M
    while True:
        yield x
        if x==0: break
        x=(x-1)&M

def downset(maxs):
    F=set()
    for M in maxs:
        F.update(submasks(M))
    return frozenset(F)

def max_members(F):
    out=[]
    for x in F:
        maximal=True
        for j in range(N):
            if not (x>>j)&1 and (x|(1<<j)) in F:
                maximal=False; break
        if maximal: out.append(x)
    return tuple(sorted(out))

# All downsets with pairwise union of maximal members <=3.
families=set()
families.add(downset([0]))
for vb in range(1,1<<N):
    families.add(downset([1<<j for j in range(N) if (vb>>j)&1]))
edges=[(1<<i)|(1<<j) for i in range(N) for j in range(i+1,N)]
for emask in range(1,1<<len(edges)):
    es=[edges[k] for k in range(len(edges)) if (emask>>k)&1]
    if any((a|b).bit_count()>3 for a,b in combinations(es,2)):
        continue
    covered=0
    for e in es: covered |= e
    iso=[j for j in range(N) if not (covered>>j)&1]
    for sm in range(1<<len(iso)):
        maxs=es+[1<<iso[k] for k in range(len(iso)) if (sm>>k)&1]
        families.add(downset(maxs))
for comb in combinations(range(N),3):
    M=sum(1<<j for j in comb)
    families.add(downset([M]))
assert len(families)==1270
for F in families:
    mx=max_members(F)
    assert all((a|b).bit_count()<=3 for a,b in combinations(mx,2))

# Classify and attach exact minimum normalized row energy e(F)
# for threshold 1 and coordinate cap 1/2. Values follow from the
# orbit-symmetrized 2--4 variable convex programs in the report.
rank1_e={0:Q(1,6),1:Q(1,5),2:Q(1,4),3:Q(3,10),4:Q(1,3),5:Q(5,14),6:Q(3,8)}
star_e={
 (1,0):Q(1,4),(1,1):Q(1,3),(1,2):Q(5,12),(1,3):Q(7,15),(1,4):Q(1,2),
 (2,0):Q(1,3),(2,1):Q(3,7),(2,2):Q(1,2),(2,3):Q(11,20),
 (3,0):Q(3,7),(3,1):Q(1,2),(3,2):Q(5,9),
 (4,0):Q(1,2),(4,1):Q(5,9),(5,0):Q(5,9)}
triangle_e={0:Q(1,3),1:Q(7,15),2:Q(5,9),3:Q(3,5)}

def classify(F):
    mx=max_members(F)
    rank=max(x.bit_count() for x in mx)
    if rank==0:
        return ('rank1',0)
    if rank==1:
        return ('rank1',len(mx))
    if rank==3:
        assert len(mx)==1
        return ('cube',)
    assert rank==2
    es=[x for x in mx if x.bit_count()==2]
    singles=[x for x in mx if x.bit_count()==1]
    common=FULL
    for e in es: common &= e
    if common:
        return ('star',len(es),len(singles))
    assert len(es)==3
    return ('triangle',len(singles))

def energy(F):
    typ=classify(F)
    if typ[0]=='rank1': return rank1_e[typ[1]]
    if typ[0]=='cube': return Q(1,3)
    if typ[0]=='star': return star_e[(typ[1],typ[2])]
    return triangle_e[typ[1]]

type_counts=Counter(classify(F) for F in families)
# Global exact lower envelope by b=|F|.
emin={}
for F in families:
    b=len(F); e=energy(F)
    emin[b]=min(emin.get(b,e),e)
expected={1:Q(1,6),2:Q(1,5),3:Q(1,4),4:Q(1,4),5:Q(1,3),6:Q(1,3),
          7:Q(1,3),8:Q(1,3),9:Q(1,2),10:Q(1,2),11:Q(5,9),12:Q(5,9)}
assert emin==expected

# Exact knapsack: active rows have b in 1..12; strict badness means
# sum of the table minima is STRICTLY below total energy <= 3/2.
profiles=[]
def rec(start,bs,cost,totalb):
    if cost>=Q(3,2): return
    if totalb>=32:
        profiles.append((tuple(bs),cost,totalb)); return
    for b in range(start,13):
        rec(b,bs+[b],cost+emin[b],totalb+b)
rec(1,[],Q(0),0)
assert profiles==[
    ((4,8,8,12),Q(53,36),32),
    ((8,8,8,8),Q(4,3),32),
    ((8,12,12),Q(13,9),32),
]

# Projective sign classes: representative has coordinate 0 positive,
# encoded by its negative-coordinate subset T (so bit 0 is 0).
proj=[]
for x in range(1<<(N-1)):
    T=0
    for k in range(N-1):
        if (x>>k)&1: T |= 1<<(k+1)
    proj.append(T)
assert len(proj)==32

def event_mask(F,R):
    m=0
    for k,T in enumerate(proj):
        X=T^R
        if X in F or (X^FULL) in F:
            m |= 1<<k
    return m

masks_by_size=defaultdict(set)
cube_support={}
b8_noncube_min=Q(100)
for F in families:
    typ=classify(F); e=energy(F); b=len(F)
    for R in range(64):
        m=event_mask(F,R)
        assert m.bit_count()==b
        masks_by_size[b].add(m)
        if b==8 and typ==('cube',):
            M=max_members(F)[0]
            S=FULL^M
            if m in cube_support:
                assert cube_support[m]==S
            else:
                cube_support[m]=S
        if b==8 and typ!=('cube',):
            b8_noncube_min=min(b8_noncube_min,e)

assert len(masks_by_size[4])==760
assert len(masks_by_size[8])==9200
assert len(masks_by_size[12])==96
assert len(cube_support)==80
assert b8_noncube_min==Q(3,7)

# Profiles (8,12,12) and (4,8,8,12) are combinatorially impossible
# because their sizes sum to exactly 32, hence they would have to partition.
ms12=sorted(masks_by_size[12]); ms8=masks_by_size[8]; ms4=masks_by_size[4]
part_8_12_12=0
for i,a in enumerate(ms12):
    for b in ms12[i+1:]:
        if a&b: continue
        if (ALL32^(a|b)) in ms8:
            part_8_12_12 += 1
assert part_8_12_12==0

def can_split_8_8(rem):
    # Any first 8-mask in a split must contain the least set bit of rem.
    p=(rem & -rem).bit_length()-1
    bit=1<<p
    for a in ms8:
        if not (a&bit): continue
        if a & ~rem: continue
        b=rem^a
        if b in ms8:
            return True
    return False

part_4_8_8_12=0
for a in ms12:
    for b in ms4:
        if a&b: continue
        rem=ALL32^(a|b)
        if can_split_8_8(rem):
            part_4_8_8_12 += 1
assert part_4_8_8_12==0

# In the (8,8,8,8) profile, if two rows are non-cubes then
# lower energy >= 2*(3/7)+2*(1/3)=32/21>3/2. Hence at least 3 cubes.
assert 2*Q(3,7)+2*Q(1,3) > Q(3,2)
# Exact enumeration: whenever three disjoint cube events leave an 8-set
# that is structurally admissible, the residual is itself a cube event.
cubes=sorted(cube_support)
three_cube_completions=0
noncube_residuals=0
partitions=set()
for i,a in enumerate(cubes):
    for j in range(i+1,len(cubes)):
        b=cubes[j]
        if a&b: continue
        for k in range(j+1,len(cubes)):
            d=cubes[k]
            if (a|b)&d: continue
            rem=ALL32^(a|b|d)
            if rem in ms8:
                three_cube_completions += 1
                if rem not in cube_support:
                    noncube_residuals += 1
                else:
                    partitions.add(tuple(sorted((a,b,d,rem))))
assert three_cube_completions==1280
assert noncube_residuals==0
assert len(partitions)==320

# For every four-cube partition, exact support-load dual: find J subset [6]
# such that (# supports contained in J)/(3|J|) >= 1/3.
# With lambda uniform on J, weighted Cauchy then forces max column load >1/3.
min_dual=None
dual_hist=Counter()
for part in partitions:
    sups=[cube_support[m] for m in part]
    best=Q(0); bestJ=None
    for J in range(1,64):
        q=J.bit_count()
        cnt=sum(1 for S in sups if (S & ~J)==0)
        val=Q(cnt,3*q)
        if val>best:
            best=val; bestJ=J
    dual_hist[best]+=1
    min_dual=best if min_dual is None else min(min_dual,best)
assert min_dual==Q(1,3)
assert min_dual>Q(1,4)

print('R13_K6_LE_2_EXACT_PASS')
print('downsets_union_le_3=',len(families))
print('emin_by_bad_count=',','.join(f'{b}:{emin[b]}' for b in sorted(emin)))
print('only_energy_profiles=',profiles)
print('projective_masks_b4=',len(masks_by_size[4]))
print('projective_masks_b8=',len(masks_by_size[8]))
print('projective_masks_b12=',len(masks_by_size[12]))
print('cube8_masks=',len(cube_support),'noncube_b8_min_energy=',b8_noncube_min)
print('partition_8_12_12=',part_8_12_12)
print('partition_4_8_8_12=',part_4_8_8_12)
print('three_cube_completions=',three_cube_completions,'noncube_residuals=',noncube_residuals)
print('four_cube_partitions=',len(partitions))
print('cube_partition_dual_hist=',dict(sorted(dual_hist.items(), key=lambda z:z[0])))
print('minimum_cube_partition_dual=',min_dual,'column_cap=',Q(1,4))
