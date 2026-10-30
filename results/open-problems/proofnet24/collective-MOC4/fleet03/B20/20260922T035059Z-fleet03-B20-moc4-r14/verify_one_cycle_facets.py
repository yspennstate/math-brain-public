from fractions import Fraction as Q
from itertools import permutations

def add(z,w): return (z[0]+w[0],z[1]+w[1])
def sub(z,w): return (z[0]-w[0],z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def scale(q,z): return (q*z[0],q*z[1])
def dot(n,z): return n[0]*z[0]+n[1]*z[1]

a=[(Q(10),Q(-13)),(Q(-18),Q(17)),(Q(-20),Q(5)),(Q(-20),Q(11))]
b=[(Q(17),Q(-18)),(Q(-22),Q(3)),(Q(-19),Q(-7)),(Q(2),Q(7))]
P=list(permutations(range(4)))
def name(p): return ''.join(str(j+1) for j in p)
def vertex(p):
    z=(Q(1),Q(0))
    for i,j in enumerate(p):
        z=mul(z,(a[i][0]+b[j][0],a[i][1]+b[j][1]))
    return z
V={name(p):vertex(p) for p in P}

(c1,s1)=(Q(3,5),Q(4,5))
(c2,s2)=(Q(7,25),Q(24,25))
(c3,s3)=(Q(7,25),Q(24,25))
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
assert sum(w0.values())==1 and sum(w1.values())==1
assert all(q>=0 for q in w0.values()) and all(q>=0 for q in w1.values())
def combo(w):
    z=(Q(0),Q(0))
    for k,q in w.items(): z=add(z,scale(q,V[k]))
    return z
D0=combo(w0); D1=combo(w1)
K=scale(c1*s1*s2*s3,sub(V['4123'],V['1423']))

coord={}
for k,z in V.items(): coord.setdefault(z,[]).append(k)
pts=[(x,y,tuple(sorted(ks))) for (x,y),ks in coord.items()]
pts.sort(key=lambda t:(t[0],t[1]))
def cross(o,p,q):
    return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
lo=[]
for p in pts:
    while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
    lo.append(p)
hi=[]
for p in reversed(pts):
    while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0: hi.pop()
    hi.append(p)
H=lo[:-1]+hi[:-1]
assert len(H)>=3

records=[]
for i,p in enumerate(H):
    q=H[(i+1)%len(H)]
    dx=q[0]-p[0]; dy=q[1]-p[1]
    n=(dy,-dx)
    vals={k:dot(n,z) for k,z in V.items()}
    M=max(vals.values())
    assert dot(n,(p[0],p[1]))==M==dot(n,(q[0],q[1]))
    d0=M-dot(n,D0); d1=M-dot(n,D1); C=dot(n,K)
    assert d0>=0 and d1>=0
    pay=d0*d1-C*C
    assert pay>=0
    ratio=(C*C)/(d0*d1) if d0*d1 else Q(0)
    records.append((p[2][0],q[2][0],n,d0,d1,C,pay,ratio))

worst=max(records,key=lambda r:r[7])
print('hull_vertices =',len(H))
print('hull_cycle =',[p[2][0] for p in H])
print('facet_count =',len(records))
for r in records:
    print('FACET',r[0],r[1],'ratio=',r[7],'payment=',r[6])
print('worst_facet =',worst[0],worst[1])
print('worst_normal =',worst[2])
print('worst_delta0 =',worst[3])
print('worst_delta1 =',worst[4])
print('worst_C =',worst[5])
print('worst_payment =',worst[6])
print('worst_ratio =',worst[7])
print('PASS MOC4-ONE-CYCLE-FACET-CERTIFICATE-v1')
