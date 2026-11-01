from fractions import Fraction
from itertools import permutations, combinations

P=list(permutations(range(1,5)))
name=lambda p: ''.join(map(str,p))

def evt_single(p,i,j):
    return int(p[i-1]==j)

def evt_set(p,S,T):
    return int(tuple(sorted(p[i-1] for i in S))==tuple(sorted(T)))

def deficit(p):
    # Nonnegative compound-event-span deficit used to test the spectral-independent
    # version of the one-cycle payment implication.
    return (1-evt_single(p,1,2)+evt_single(p,1,3)
            -evt_single(p,2,2)-evt_single(p,3,2)
            -evt_set(p,(1,2),(1,3))+evt_set(p,(1,3),(1,2)))

d={name(p):deficit(p) for p in P}
assert min(d.values())==0 and max(d.values())==2

# Eleven ties used in the face-propagation theorem.
ties=['1234','1243','2134','2143','1324','3124',
      '2431','4231','2341','4123','4321']
assert all(d[s]==0 for s in ties)
assert d['1423']==1

# Verify that d really lies in the low-frequency [4]+[31]+[22] compound-event
# span by the central-transposition adjacency annihilator A(A-2I)(A-6I).
idx={p:i for i,p in enumerate(P)}
A=[[0]*24 for _ in range(24)]
for i,p in enumerate(P):
    for r,s in combinations(range(4),2):
        q=list(p); q[r],q[s]=q[s],q[r]; q=tuple(q)
        A[i][idx[q]]+=1

def mv(M,v):
    return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]

dv=[deficit(p) for p in P]
v1=[mv(A,dv)[i]-6*dv[i] for i in range(24)]
v2=[mv(A,v1)[i]-2*v1[i] for i in range(24)]
v3=mv(A,v2)
assert all(x==0 for x in v3)

# Exact one-cycle chain parameters from the fleet03/B08 ellipse reduction.
x=Fraction(9,25); y=Fraction(16,25); u=Fraction(49,625); q=(1-u)**2
alpha=Fraction(3,5)*Fraction(4,5)*Fraction(24,25)*Fraction(24,25)
p0={
 '1234':x*u*u,'1243':x*u*(1-u),'1324':x*(1-u)*u,'1423':x*q,
 '2134':y*u*u,'2143':y*u*(1-u),'3124':y*(1-u)*u,'4123':y*q}
p1={
 '1423':y*q,'2413':y*u*(1-u),'2431':y*u*u,'3421':y*(1-u)*u,
 '4123':x*q,'4213':x*u*(1-u),'4231':x*u*u,'4321':x*(1-u)*u}
assert sum(p0.values(),Fraction())==1
assert sum(p1.values(),Fraction())==1

delta0=sum(w*d[s] for s,w in p0.items())
delta1=sum(w*d[s] for s,w in p1.items())
C2=alpha*alpha*(d['1423']-d['4123'])**2
margin=delta0*delta1-C2
assert delta0==Fraction(2985984,9765625)
assert delta1==Fraction(6211584,9765625)
assert C2==Fraction(47775744,244140625)
assert margin==-Fraction(114709561344,95367431640625)
assert C2/(delta0*delta1)==Fraction(390625,388224)
assert margin<0

print('PASS MOC4-CHAIN-CUBE-FACE-PROPAGATION-v1')
print('required_ties =',len(ties))
print('low_frequency_polynomial = 0')
print('delta0 =',delta0)
print('delta1 =',delta1)
print('C2 =',C2)
print('payment_margin =',margin)
print('ratio =',C2/(delta0*delta1))
