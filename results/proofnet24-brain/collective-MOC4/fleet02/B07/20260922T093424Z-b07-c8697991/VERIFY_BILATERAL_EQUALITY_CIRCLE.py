from fractions import Fraction as F

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def mv(A,x):
    return tuple(sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A)))

def tr(A):
    return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))

def outer(a,b):
    return tuple(tuple(x*y for y in b) for x in a)

def madd(*As):
    return tuple(tuple(sum(A[i][j] for A in As) for j in range(len(As[0][0]))) for i in range(len(As[0])))

def scale(c,A):
    return tuple(tuple(c*x for x in row) for row in A)

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

I = tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
A=B=F(1)
m=F(0)
D=A*B-m*m
rho=F(1,3)
r1=rho
s1=-rho
r2=F(1,4)
s2=F(1,5)
H=rho*rho+r2*r2+s2*s2
z=(A+B-H)/2
L=A+B-z
Z=((F(1),F(0),r1),(F(0),m,r2),(s1,s2,z))
p=(-r1,-r2,A-z)
q=(-s1,-s2,B-z)
kL=(A*r2+m*s2)/D
kR=(B*s2+m*r2)/D
wL=(F(0),F(1),-kL)
wR=(F(0),F(1),-kR)
dL=kL
dR=kR
C_L=A*(H-rho*rho)-s2*s2
E_L=A*r2+m*s2
C_R=B*(H-rho*rho)-r2*r2
E_R=B*s2+m*r2
assert D*C_L == E_L*E_L
assert D*C_R == E_R*E_R
ZZt=mm(Z,tr(Z))
ZtZ=mm(tr(Z),Z)
rhsL=madd(outer(p,p), scale(-D,outer(wL,wL)), scale(A*B,I))
rhsR=madd(outer(q,q), scale(-D,outer(wR,wR)), scale(A*B,I))
assert ZZt == rhsL
assert ZtZ == rhsR
assert tuple(L*p[i]+mv(Z,q)[i]+D*dL*wL[i] for i in range(3)) == (F(0),)*3
assert tuple(L*q[i]+mv(tr(Z),p)[i]+D*dR*wR[i] for i in range(3)) == (F(0),)*3
assert L*L-dot(q,q)-D*dL*dL == A*B
assert L*L-dot(p,p)-D*dR*dR == A*B
aL=cross(p,wL)
aR=cross(q,wR)
assert aL != (F(0),)*3 and aR != (F(0),)*3
assert mv(tr(Z),aL) == tuple(-x for x in aR)
assert mv(Z,aR) == tuple(-x for x in aL)
assert dot(aL,aL) == dot(aR,aR)
n=(F(-4,9),F(-4,9),F(-7,9))
assert dot(n,n)==1 and dot(wL,n)+dL==0
beta=L-dot(p,n)
v=tuple(q[i]+mv(tr(Z),n)[i] for i in range(3))
mvec=tuple(x/beta for x in v)
assert dot(mvec,mvec)==1 and dot(wR,mvec)+dR==0
support=dot(p,n)+dot(q,mvec)+sum(n[i]*Z[i][j]*mvec[j] for i in range(3) for j in range(3))
assert support==L
print("PASS MOC4-MSQR-BILATERAL-EQUALITY-CIRCLE-v1")
print("A=B=1, D=", D, "H=", H, "z=", z, "L=", L)
print("kL=", kL, "kR=", kR)
print("aL=", aL)
print("aR=", aR)
print("Z^T aL=", mv(tr(Z),aL))
print("Z aR=", mv(Z,aR))
print("n=", n)
print("m(n)=", mvec)
print("support=", support)
