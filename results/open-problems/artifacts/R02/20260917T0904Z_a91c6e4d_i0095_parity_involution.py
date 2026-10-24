from collections import defaultdict

N=2048
MASK=(1<<12)-1

def dF(a,b):
    w=(a^b).bit_count()  # representatives have 12th bit 0
    return min(w,12-w)

S=[x for x in range(N) if dF(0,x)<=3]
assert len(S)==299
Sset=set(S)
counts=defaultdict(set)
for z in range(N):
    q=sum(1 for s in S if (s^z) in Sset)
    d=dF(0,z)
    counts[d].add(q)
    if z==0:
        assert q%2==1
    else:
        assert q%2==0
expected={0:299,1:134,2:134,3:62,4:62,5:20,6:40}
assert {d:next(iter(v)) for d,v in counts.items()}==expected
assert all(len(v)==1 for v in counts.values())

# Direct group-algebra/convolution parity check: coefficient of z in 1_S * 1_S.
for z in range(N):
    q=sum(1 for s in S if (s^z) in Sset)
    assert (q & 1)==(1 if z==0 else 0)

print('R02 I0095 parity-involution exact checker')
print('quotient_vertices=',N)
print('radius3_ball_size=',len(S))
print('overlap_by_folded_distance=',dict(sorted(expected.items())))
print('all_nonzero_shift_overlaps_even=1')
print('T_squared_equals_identity_mod2=1')
print('COROLLARY: for any center indicator c, g=T c, h=g-1, T h == 1+c (mod 2)')
print('COROLLARY: if g>=1 is a cover, center membership is exactly recoverable from excess parity via c=1+T h (mod 2)')
print('ALL_EXACT_CHECKS_PASS')
