from itertools import permutations, combinations
from fractions import Fraction

A = [(23,19),(1,17),(25,-26),(-35,19)]
B = [(-21,13),(-1,23),(26,-27),(32,-21)]
P_CAND = (3,2,1,0)   # 4321
P_TOP  = (2,3,0,1)   # 3412

def add(z,w): return (z[0]+w[0], z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def vertex(p):
    z=(1,0)
    for i in range(4):
        z=mul(z, add(A[i],B[p[i]]))
    return z
def L(z,P,Q): return P*z[0]+Q*z[1]
def label(p): return ''.join(str(x+1) for x in p)

perms=list(permutations(range(4)))
verts={p:vertex(p) for p in perms}

P0,Q0=216982,365451
dP,dQ=-17957,-30244
dx=verts[P_TOP][0]-verts[P_CAND][0]
dy=verts[P_TOP][1]-verts[P_CAND][1]
assert P0*dx+Q0*dy == 0
assert dP*dx+dQ*dy == 6

tie={p:L(verts[p],P0,Q0) for p in perms}
assert tie[P_TOP] == tie[P_CAND]
assert all(tie[P_CAND] > tie[p] for p in perms if p not in (P_CAND,P_TOP))

def direction(N):
    assert N >= 1
    return (N*P0+dP, N*Q0+dQ)

P,Q=direction(1)
sup={p:L(verts[p],P,Q) for p in perms}
order=sorted(perms,key=lambda p:sup[p],reverse=True)
assert order[0] == P_TOP
assert order[1] == P_CAND
assert len(set(sup.values())) == 24
assert sup[P_TOP]-sup[P_CAND] == 6

neighbor_losses={}
for i,j in combinations(range(4),2):
    q=list(P_CAND); q[i],q[j]=q[j],q[i]; q=tuple(q)
    loss=sup[P_CAND]-sup[q]
    assert loss > 0
    neighbor_losses[(i+1,j+1)] = (label(q),loss)

# Infinite-family proof data: positivity at N=1 plus positive tie-normal slope.
for r in perms:
    if r in (P_CAND,P_TOP):
        continue
    assert tie[P_CAND]-tie[r] > 0
    assert sup[P_CAND]-sup[r] > 0
for i,j in combinations(range(4),2):
    q=list(P_CAND); q[i],q[j]=q[j],q[i]; q=tuple(q)
    assert tie[P_CAND]-tie[q] > 0

# Two disjoint swaps tunnel.
P12=list(P_CAND); P12[0],P12[1]=P12[1],P12[0]; P12=tuple(P12)
P34=list(P_CAND); P34[2],P34[3]=P34[3],P34[2]; P34=tuple(P34)
assert tuple([P_CAND[1],P_CAND[0],P_CAND[3],P_CAND[2]]) == P_TOP
loss12=sup[P_CAND]-sup[P12]
loss34=sup[P_CAND]-sup[P34]
delta=sup[P_TOP]-sup[P_CAND]
cross=loss12+loss34+delta
assert (loss12,loss34,delta,cross)==(79221639744,36360921450,6,115582561200)

M=sup[P_TOP]; m=min(sup.values()); width=M-m
print('direction_N1 =', (P,Q))
print('candidate =', label(P_CAND), verts[P_CAND], sup[P_CAND])
print('global_top =', label(P_TOP), verts[P_TOP], sup[P_TOP])
print('gap =', delta)
print('support_width =', width)
print('normalized_gap =', Fraction(delta,width), float(Fraction(delta,width)))
print('all_24_distinct =', len(set(sup.values()))==24)
print('neighbor_losses =', neighbor_losses)
print('tie_normal =', (P0,Q0), 'tie_value =', tie[P_CAND],
      'third_gap =', tie[P_CAND]-max(tie[p] for p in perms if p not in (P_CAND,P_TOP)))
print('bezout_perturbation =', (dP,dQ), 'top_minus_candidate =', dP*dx+dQ*dy)
print('two_pair_losses =', (loss12,loss34), 'cross_coefficient =', cross)
threshold=Fraction(loss12+loss34,cross)
print('diagonal_t_threshold =', threshold, float(threshold))
print('certificate = PASS')
