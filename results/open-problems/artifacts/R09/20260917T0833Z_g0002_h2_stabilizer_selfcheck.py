from itertools import product

N=8
ALL=range(1<<N)

UPPER_MIN = [
(1,2,5,6), (1,3,5,6), (2,4,5,6), (3,4,5,6), (1,3,5,7), (2,3,5,7),
(1,4,5,7), (1,2,3,4,6,7), (2,5,6,7), (4,5,6,7), (1,2,3,8), (1,3,4,8),
(2,3,4,8), (1,5,8), (2,5,8), (3,5,8), (4,5,8), (2,3,6,8), (1,4,6,8),
(5,6,8), (1,2,7,8), (2,4,7,8), (3,4,7,8), (5,7,8), (1,6,7,8), (3,6,7,8)
]

INSIDE_MIN = [
(1,2,5), (2,3,5), (2,4,5), (1,3,4,5), (1,3,6), (2,3,4,6), (2,5,6),
(1,4,5,6), (1,2,3,4,7), (1,5,7), (3,5,7), (4,5,7), (2,3,6,7),
(1,2,4,6,7), (3,4,6,7), (5,6,7), (1,4,8), (2,3,4,8), (2,5,8),
(1,3,5,8), (2,3,6,8), (2,4,6,8), (1,5,6,8), (3,4,5,6,8),
(1,2,3,7,8), (2,4,7,8), (3,4,7,8), (5,7,8), (1,2,6,7,8),
(3,6,7,8), (4,6,7,8)
]

def mask(t):
    m=0
    for i in t:
        m |= 1<<(i-1)
    return m

def up_family(minsets):
    mins=[mask(t) for t in minsets]
    return {s for s in ALL if any((s & m)==m for m in mins)}

def is_increasing(fam):
    for s in fam:
        for i in range(N):
            if not (s>>i)&1 and (s | (1<<i)) not in fam:
                return False
    return True

def section_boundary(fam,i):
    out=set(); others=[j for j in range(N) if j!=i]
    for y in range(1<<(N-1)):
        s0=0
        for k,j in enumerate(others):
            if (y>>k)&1:
                s0 |= 1<<j
        s1=s0 | (1<<i)
        if s1 in fam and s0 not in fam:
            out.add(y)
    return out

def radius1(B,d):
    U=set(B)
    for y in B:
        for k in range(d):
            U.add(y^(1<<k))
    return U

def h2_obj(fam):
    n1=0; b=0
    for i in range(N):
        Bi=section_boundary(fam,i)
        b += len(Bi)
        n1 += len(radius1(Bi,N-1))
    return (n1, n1-b, b)

def wt(s): return s.bit_count()

def inside_band(fam):
    return all(s in fam for s in ALL if wt(s)>=5) and all(s not in fam for s in ALL if wt(s)<=1)

def upper_out(fam):
    fixed5=sum(1<<i for i in range(5))
    return fixed5 not in fam

def lower_out(fam):
    return 1 in fam

def family_from_thresholds(thr, groupA):
    gA=set(groupA); fam=set()
    for s in ALL:
        a=sum((s>>j)&1 for j in gA)
        b=wt(s)-a
        if b>=thr[a]: fam.add(s)
    return fam

def nonincreasing_thresholds(length,maxval):
    def rec(pos,last,prefix):
        if pos==length:
            yield tuple(prefix); return
        for v in range(last,-1,-1):
            prefix.append(v); yield from rec(pos+1,v,prefix); prefix.pop()
    yield from rec(0,maxval,[])

FU=up_family(UPPER_MIN); FI=up_family(INSIDE_MIN)
assert is_increasing(FU) and is_increasing(FI)
assert upper_out(FU) and inside_band(FI)
objU=h2_obj(FU); objI=h2_obj(FI)
assert objU==(924,670,254), objU
assert objI==(910,654,256), objI

upper_list=[]
for thr in nonincreasing_thresholds(6,4):
    if thr[5] < 1: continue
    fam=family_from_thresholds(thr,range(5))
    assert upper_out(fam)
    upper_list.append((h2_obj(fam),thr))
assert len(upper_list)==84, len(upper_list)
best_upper=max(upper_list,key=lambda x:(x[0][0],x[0][1]))
assert best_upper==((862,584,278),(4,3,3,1,1,1)), best_upper
best_upper_m1=max(upper_list,key=lambda x:(x[0][1],x[0][0]))

lower_list=[]
for thr in nonincreasing_thresholds(2,8):
    if thr[1] != 0: continue
    fam=family_from_thresholds(thr,[0])
    assert lower_out(fam)
    lower_list.append((h2_obj(fam),thr))
assert len(lower_list)==9, len(lower_list)
best_lower=max(lower_list,key=lambda x:(x[0][0],x[0][1]))
assert best_lower==((589,385,204),(4,0)), best_lower
best_lower_m1=max(lower_list,key=lambda x:(x[0][1],x[0][0]))

print('SELF_CHECK_ONLY_H2_NOT_SOURCE_VERIFIED')
print('n=8 factor-two-free H2 objectives psi2, psi2m1, boundary')
print('explicit_upper_out=',objU,'minsets=',len(UPPER_MIN))
print('explicit_inside=',objI,'minsets=',len(INSIDE_MIN))
print('explicit_candidate_differences=',(objU[0]-objI[0],objU[1]-objI[1]),'NOT_GLOBAL_GAPS')
print('S5xS3_upper_out_invariant_count=',len(upper_list))
print('S5xS3_best_psi2=',best_upper)
print('S5xS3_best_psi2m1=',best_upper_m1)
print('S1xS7_lower_out_invariant_count=',len(lower_list))
print('S1xS7_best_psi2=',best_lower)
print('S1xS7_best_psi2m1=',best_lower_m1)
print('PASS')
