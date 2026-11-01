from collections import deque, Counter
from fractions import Fraction

# Exact arithmetic in Z[a,b], a^2=2, b^2=b+1, with b=phi.
# An element is (c0,c1,c2,c3) = c0+c1*a+c2*b+c3*a*b.
def add(x,y):
    return (x[0]+y[0],x[1]+y[1],x[2]+y[2],x[3]+y[3])

def mul(x,y):
    x0,x1,x2,x3=x; y0,y1,y2,y3=y
    return (
        x0*y0 + 2*x1*y1 + x2*y2 + 2*x3*y3,
        x0*y1 + x1*y0 + x2*y3 + x3*y2,
        x0*y2 + x2*y0 + x2*y2 + 2*x1*y3 + 2*x3*y1 + 2*x3*y3,
        x0*y3 + x3*y0 + x1*y2 + x2*y1 + x2*y3 + x3*y2,
    )

Z=(0,0,0,0); ONE=(1,0,0,0); A=(0,1,0,0); B=(0,0,1,0); MONE=(-1,0,0,0)

def sring(items):
    z=Z
    for x in items: z=add(z,x)
    return z

def mm(X,Y):
    return tuple(tuple(sring(mul(X[i][k],Y[k][j]) for k in range(3)) for j in range(3)) for i in range(3))

def mv(X,v):
    return tuple(sring(mul(X[i][k],v[k]) for k in range(3)) for i in range(3))

I=tuple(tuple(ONE if i==j else Z for j in range(3)) for i in range(3))
def mpow(X,n):
    Y=I
    for _ in range(n): Y=mm(X,Y)
    return Y

# Coxeter [4,5] simple reflections in the integral Z[sqrt(2),phi] model.
S1=((MONE,A,Z),(Z,ONE,Z),(Z,Z,ONE))
S2=((ONE,Z,Z),(A,MONE,B),(Z,Z,ONE))
S3=((ONE,Z,Z),(Z,ONE,Z),(Z,B,MONE))
assert mm(S1,S1)==I and mm(S2,S2)==I and mm(S3,S3)==I
assert mpow(mm(S1,S2),4)==I
assert mpow(mm(S2,S3),5)==I
assert mpow(mm(S1,S3),2)==I

R=mm(S2,S3)
Ri=mpow(R,4)
Q=mm(mm(S1,R),S1)
Qi=mpow(Q,4)
assert mpow(R,5)==I and mpow(Q,5)==I

# Scaled midpoint of the base edge in {4,5}; S1 and S3 fix it.
MID=(A,(2,0,0,0),B)
assert mv(S1,MID)==MID and mv(S3,MID)==MID
GENS=(R,Ri,Q,Qi)
assert len({mv(g,MID) for g in GENS})==4

MAX_R=16
dist={MID:0}
q=deque([MID])
while q:
    v=q.popleft(); d=dist[v]
    if d==MAX_R: continue
    for g in GENS:
        w=mv(g,v)
        if w not in dist:
            dist[w]=d+1
            q.append(w)

count=Counter(dist.values())
shell=[count[i] for i in range(MAX_R+1)]
expected=[1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,17934,33178,61450]
assert shell==expected

# Radius-14 ball is the best ball ratio among radii 9..15 in this exact development.
ratios=[]
for r in range(9,16):
    Bsize=sum(shell[:r+1])
    boundary=shell[r+1]
    ratios.append((Fraction(boundary,Bsize),r,Bsize,boundary))
best=min(ratios)
ratio,radius,Bsize,boundary=best
assert radius==14
assert Bsize==38983 and boundary==33178
assert ratio==Fraction(33178,38983)
assert ratio < Fraction(1528,1783)
assert 33178*1783 < 1528*38983

# Finite evidence for the candidate order-six shell recurrence only.
# This is deliberately NOT promoted to an all-n theorem by the checker.
for n in range(7,17):
    rhs=(shell[n-1] + 2*shell[n-2] - 2*shell[n-3]
         + 2*shell[n-4] + shell[n-5] - shell[n-6])
    assert shell[n]==rhs

print('EXACT_COXETER_SCHREIER_PASS')
print('T_SHELLS_0_TO_16',shell)
print('T_RADIUS14_BALL',Bsize)
print('T_RADIUS14_OUTER_VERTEX_BOUNDARY',boundary)
print('T_RADIUS14_RATIO',f'{ratio.numerator}/{ratio.denominator}')
print('PREVIOUS_RADIUS9_RATIO','1528/1783')
print('STRICT_IMPROVEMENT_CROSS_PRODUCT_MARGIN',1528*38983-33178*1783)
print('FINITE_RECURRENCE_CHECK_N_7_TO_16_PASS')
print('CANDIDATE_RECURRENCE','S_n=S_(n-1)+2S_(n-2)-2S_(n-3)+2S_(n-4)+S_(n-5)-S_(n-6)')
print('ALL_EXACT_CHECKS_PASS')
