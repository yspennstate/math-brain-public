#!/usr/bin/env python3
"""Exact endpoint necessary-condition enumeration for two H(2060) construction routes.

Williamson: an order-515 Williamson quadruple would yield H(2060). Evaluating
A^2+B^2+C^2+D^2=4*515 I on the all-ones vector gives four odd row sums
r_i with sum r_i^2=2060. Sign changes and block permutation allow
0<r1<=r2<=r3<=r4.

Turyn type: TT(172) has lengths (172,172,172,171). The standard route
TT(n) -> base sequences -> T-sequences gives T-sequence order 3n-1=515,
hence H(4*515)=H(2060). Evaluating the Turyn-type norm identity at 1 gives
a^2+b^2+2c^2+2d^2=6*172-2=1030. Here a,b,c are even and d is odd.
Sign changes allow nonnegative sums; swapping equal-length A,B allows a<=b.

These are necessary endpoint filters only, not existence or nonexistence certificates.
"""
import math

nW=515
will=[]
for a in range(1,46,2):
    for b in range(a,46,2):
        for c in range(b,46,2):
            for d in range(c,46,2):
                if a*a+b*b+c*c+d*d==4*nW:
                    will.append((a,b,c,d))
assert len(will)==29
assert all(sum(x*x for x in q)==2060 for q in will)

n=172
tt=[]
for a in range(0,n+1,2):
    for b in range(a,n+1,2):
        for c in range(0,n+1,2):
            rem=(6*n-2)-a*a-b*b-2*c*c
            if rem<0 or rem%2:
                continue
            q=rem//2
            d=math.isqrt(q)
            if d*d==q and d<=n-1 and d%2==1:
                tt.append((a,b,c,d))
assert len(tt)==45
assert all(a*a+b*b+2*c*c+2*d*d==1030 for a,b,c,d in tt)

print('target_order=2060')
print('williamson_order=515')
print('williamson_endpoint_candidate_count=',len(will))
for q in will:
    print('W',q)
print('turyn_type_length=172')
print('t_sequence_order=',3*n-1)
print('turyn_endpoint_candidate_count=',len(tt))
for q in tt:
    print('TT',q)
print('SCOPE: endpoint necessary conditions only; no existence/nonexistence claim')
