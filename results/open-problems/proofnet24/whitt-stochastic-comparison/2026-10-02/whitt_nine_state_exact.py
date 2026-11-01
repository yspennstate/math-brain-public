"""Nine-state exact certificate for a simpler Whitt1983 counterexample.

The capacity-three queue only supplies a lower bound for the infinite
base queue. Rejected jobs add zero work, giving pathwise domination by
the corresponding infinite FCFS queue. The larger service law reduces
to an M/M/2 queue after zero-work deletion.
"""
from fractions import Fraction as F
from math import lcm, gcd
from functools import reduce
import json

LA, P, MS, ML = F(1,10), F(2,3), F(2), F(1,2)
# (number of customers, number of small jobs currently in service)
STATES = [(0,0),(1,0),(1,1),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)]
INDEX = {x:i for i,x in enumerate(STATES)}
Q = [[F(0) for _ in STATES] for _ in STATES]

for state,j in INDEX.items():
    n,i = state
    def jump(target,rate):
        Q[j][INDEX[target]] += rate
        Q[j][j] -= rate
    if n < 3:
        if n < 2:
            jump((n+1,i+1), LA*P)
            jump((n+1,i), LA*(1-P))
        else:
            jump((n+1,i), LA)
    if n:
        busy = min(n,2)
        if n <= 2:
            if i:
                jump((n-1,i-1),i*MS)
            if busy-i:
                jump((n-1,i),(busy-i)*ML)
        else:
            if i:
                jump((n-1,i),i*MS*P)
                jump((n-1,i-1),i*MS*(1-P))
            if busy-i:
                jump((n-1,i+1),(busy-i)*ML*P)
                jump((n-1,i),(busy-i)*ML*(1-P))

assert all(sum(row,F(0))==0 for row in Q)
assert all(Q[i][j]>=0 for i in range(9) for j in range(9) if i!=j)

# Solve pQ=0 and p1=1 directly, by exact Gauss-Jordan elimination.
A = [[Q[j][i] for j in range(9)] for i in range(9)]
A[-1] = [F(1)]*9
B = [F(0)]*8+[F(1)]
aug = [row+[rhs] for row,rhs in zip(A,B)]
for j in range(9):
    pivot=next(i for i in range(j,9) if aug[i][j])
    aug[j],aug[pivot]=aug[pivot],aug[j]
    scale=aug[j][j]
    aug[j]=[x/scale for x in aug[j]]
    for i in range(9):
        if i!=j:
            scale=aug[i][j]
            aug[i]=[x-scale*y for x,y in zip(aug[i],aug[j])]
pi=[row[-1] for row in aug]
assert sum(pi,F(0))==1 and min(pi)>0
assert all(sum((pi[i]*Q[i][j] for i in range(9)),F(0))==0 for j in range(9))
den=reduce(lcm,(x.denominator for x in pi),1)
weights=[int(x*den) for x in pi]
gg=reduce(gcd,weights)
weights=[x//gg for x in weights]
den=sum(weights)
assert weights==[28428000,1893800,947950,60780,63950,15880,6078,2558,397]
IQ=[[int(30*x) for x in row] for row in Q]
assert all(F(x,30)==q for row,qrow in zip(IQ,Q) for x,q in zip(row,qrow))
assert all(sum(weights[i]*IQ[i][j] for i in range(9))==0 for j in range(9))
busy=sum(weights[3:])
lower=F(busy,den)
rho=LA/2
endpoint=2*rho*rho/(1+rho)
assert endpoint==F(1,210)
gap=lower-endpoint
assert gap==F(1879,2199357510)
assert gap>F(8,10000000)
# A positive threshold follows from the combined departure rate bound4.
h=F(1,10**7)
assert gap-4*h>F(4,10000000)
print(json.dumps({
    'arithmetic':'exact Fraction and integer comparisons',
    'arrival_rate':str(LA),'states':STATES,
    'integer_stationary_weights':weights,'normalizing_sum':den,
    'integer_generator_30Q':IQ,
    'busy_weight_sum':busy,'base_delay_lower_bound':str(lower),
    'zero_exponential_endpoint_delay':str(endpoint),
    'gap_lower_bound':str(gap),
    'gap_display':float(gap),
    'positive_threshold':str(h),
    'positive_threshold_gap_lower_bound':str(gap-4*h),
    'checks':['all generator rows','pQ=0 exactly','positive stationary vector',
              'integer stationary balance w(30Q)=0',
              'delay lower bound exceeds1/210 by8/1e7']
},indent=2))
