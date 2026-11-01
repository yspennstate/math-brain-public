from fractions import Fraction as Q
from itertools import permutations

# Exact all-support-direction certificate for the fleet03/B08
# one-cycle SU(2) ellipse stress datum.
# Complex numbers are pairs (re,im) of Fractions.

def add(z,w): return (z[0]+w[0], z[1]+w[1])
def sub(z,w): return (z[0]-w[0], z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def scale(q,z): return (q*z[0], q*z[1])
def dot(z,l): return z[0]*l[0]+z[1]*l[1]
def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def outward(edge):
    dx,dy=edge
    return (dy,-dx)

a=[(Q(10),Q(-13)),(Q(-18),Q(17)),(Q(-20),Q(5)),(Q(-20),Q(11))]
b=[(Q(17),Q(-18)),(Q(-22),Q(3)),(Q(-19),Q(-7)),(Q(2),Q(7))]
(c1,s1)=(Q(3,5),Q(4,5))
(c2,s2)=(Q(7,25),Q(24,25))
(c3,s3)=(Q(7,25),Q(24,25))

P=list(permutations(range(4)))
def name(p): return ''.join(str(j+1) for j in p)
def vertex(p):
    z=(Q(1),Q(0))
    for i,j in enumerate(p):
        z=mul(z,add(a[i],b[j]))
    return z
V={name(p):vertex(p) for p in P}
assert len(set(V.values()))==24

w0={
'1234':c1*c1*c2*c2*c3*c3,
'1243':c1*c1*c2*c2*s3*s3,
'1324':c1*c1*c3*c3*s2*s2,
'1423':c1*c1*s2*s2*s3*s3,
'2134':c2*c2*c3*c3*s1*s1,
'2143':c2*c2*s1*s1*s3*s3,
'3124':c3*c3*s1*s1*s2*s2,
'4123':s1*s1*s2*s2*s3*s3}
w1={
'1423':s1*s1*s2*s2*s3*s3,
'2413':c2*c2*s1*s1*s3*s3,
'2431':c2*c2*c3*c3*s1*s1,
'3421':c3*c3*s1*s1*s2*s2,
'4123':c1*c1*s2*s2*s3*s3,
'4213':c1*c1*c2*c2*s3*s3,
'4231':c1*c1*c2*c2*c3*c3,
'4321':c1*c1*c3*c3*s2*s2}
assert sum(w0.values(),Q(0))==1 and sum(w1.values(),Q(0))==1
assert all(q>=0 for q in w0.values()) and all(q>=0 for q in w1.values())

def combo(w):
    z=(Q(0),Q(0))
    for k,q in w.items():
        z=add(z,scale(q,V[k]))
    return z

D0=combo(w0)
D1=combo(w1)
K=scale(c1*s1*s2*s3,sub(V['4123'],V['1423']))

# Exact convex hull in CCW order, discarding collinear interior points.
pts=sorted((z[0],z[1],k) for k,z in V.items())
lo=[]
for p in pts:
    while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:
        lo.pop()
    lo.append(p)
up=[]
for p in reversed(pts):
    while len(up)>=2 and cross(up[-2],up[-1],p)<=0:
        up.pop()
    up.append(p)
H=lo[:-1]+up[:-1]
assert len(H)>=3

def payment_at_vertex(tau,l):
    u=sub(V[tau],D0)
    v=sub(V[tau],D1)
    return dot(u,l)*dot(v,l)-dot(K,l)**2

rows=[]
m=len(H)
for i,(x,y,tau) in enumerate(H):
    xp,yp,_=H[(i-1)%m]
    xn,yn,_=H[(i+1)%m]
    nminus=outward((x-xp,y-yp))
    nplus=outward((xn-x,yn-y))

    # Both rays really lie in the maximizing normal cone at tau.
    for nvec in (nminus,nplus):
        top=dot(V[tau],nvec)
        assert all(top>=dot(z,nvec) for z in V.values())

    A=payment_at_vertex(tau,nminus)
    C=payment_at_vertex(tau,nplus)
    s=(nminus[0]+nplus[0],nminus[1]+nplus[1])
    B=(payment_at_vertex(tau,s)-A-C)/2

    # Exact 2x2 copositivity criterion on alpha,beta >= 0.
    assert A>=0 and C>=0
    assert B>=0 or B*B<=A*C
    rows.append((tau,nminus,nplus,A,B,C))

# Shared rays must give the same payment from either adjacent maximizer.
for i in range(m):
    tau=H[i][2]
    nxt=H[(i+1)%m][2]
    n=rows[i][2]
    assert payment_at_vertex(tau,n)==payment_at_vertex(nxt,n)

# This datum is strictly certified: every cone coefficient is positive.
assert all(A>0 and B>0 and C>0 for _,_,_,A,B,C in rows)

print('PASS MOC4-ONE-CYCLE-NORMAL-CONE-v1 exact all-direction certificate')
print('target_vertices =', len(V))
print('hull_vertex_count =', len(H))
print('hull_order =', [tau for _,_,tau in H])
print('D0 =', D0)
print('D1 =', D1)
print('K =', K)
for tau,nm,np_,A,B,C in rows:
    print('cone',tau)
    print(' nminus =', nm, 'nplus =', np_)
    print(' A =', A)
    print(' B =', B)
    print(' C =', C)
    print(' copositive = True')
print('all_nonzero_support_directions_strict_payment = True')
