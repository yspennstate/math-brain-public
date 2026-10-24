from fractions import Fraction as F
from itertools import permutations

# Exact genuine SO(6) datum from account03/B09 MOC4-CYCLE-SEPARATOR-NOGO-v1.
O = [
    [F(1),0,0,0,0,0],
    [0,F(7,25),0,0,0,F(-24,25)],
    [0,0,F(1),0,0,0],
    [0,F(-504,725),0,F(20,29),0,F(-147,725)],
    [0,0,0,0,F(1),0],
    [0,F(96,145),0,F(21,29),0,F(28,145)],
]

K = [
    [F(3),0,0],
    [0,F(3),0],
    [0,0,F(-3)],
]
X = [
    [0,F(-2),F(2)],
    [F(2),0,F(-2)],
    [F(-2),F(2),0],
]

ZBASIS = {
    "I": ([[F(1),0],[0,F(1)]], F(1)),
    "J": ([[0,F(-1)],[F(1),0]], F(1)),
    "S": ([[F(1),0],[0,F(-1)]], F(-1)),
    "T": ([[0,F(1)],[F(1),0]], F(-1)),
}

def transpose(A):
    return [list(x) for x in zip(*A)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def det_perm(A):
    n=len(A)
    total=F(0)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=F(-1 if inv%2 else 1)
        for i in range(n):
            term*=A[i][p[i]]
        total+=term
    return total

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def half_norm2(A):
    return F(1,2)*sum(x*x for row in A for x in row)

def frob(A,B):
    return sum(A[i][j]*B[i][j] for i in range(2) for j in range(2))

def qdet(A,B):
    # Polarization of determinant:
    # det(A+tB)=det(A)+t*qdet(A,B)+t^2 det(B).
    return (A[0][0]*B[1][1] + A[1][1]*B[0][0]
            - A[0][1]*B[1][0] - A[1][0]*B[0][1])

def blocks_of(OO):
    return [[[[OO[2*a+i][2*b+j] for j in range(2)] for i in range(2)]
             for b in range(3)] for a in range(3)]

def channels(OO):
    B=blocks_of(OO)
    R=[[half_norm2(B[a][b]) for b in range(3)] for a in range(3)]
    D=[[det2(B[a][b]) for b in range(3)] for a in range(3)]
    return B,R,D

def support(OO):
    _,R,D=channels(OO)
    return sum(K[a][b]*D[a][b] + F(1,2)*X[a][b]*R[a][b]
               for a in range(3) for b in range(3))

def row_derivative(B,a,g,Z,eps):
    # For W(theta)O with row-plane generator
    # [[0,Z],[-Z^T,0]], this is ds/dtheta at theta=0.
    total=F(0)
    pieces=[]
    for b in range(3):
        A=B[a][b]; G=B[g][b]; ZG=mm(Z,G)
        term=((K[a][b]-eps*K[g][b])*qdet(A,ZG)
              + F(1,2)*(X[a][b]-X[g][b])*frob(A,ZG))
        pieces.append(term)
        total+=term
    return total,pieces

def gate(B,R,D,a,g):
    T=sum(K[a][b]*D[a][b] + K[g][b]*D[g][b]
          + F(1,2)*(X[a][b]-X[g][b])*(R[a][b]-R[g][b])
          for b in range(3))
    C=sum(K[a][b]*D[g][b] + K[g][b]*D[a][b] for b in range(3))
    return T,C,T-abs(C)

I6=[[F(int(i==j)) for j in range(6)] for i in range(6)]
assert mm(transpose(O),O)==I6
assert det_perm(O)==1

B,R,D=channels(O)
R_expected=[
    [F(337,625),0,F(288,625)],
    [F(127008,525625),F(1241,1682),F(21609,1051250)],
    [F(4608,21025),F(441,1682),F(21809,42050)],
]
D_expected=[
    [F(7,25),0,0],
    [0,F(20,29),0],
    [0,0,F(28,145)],
]
assert R==R_expected
assert D==D_expected
assert all(sum(row)==1 for row in R)
assert all(sum(R[a][b] for a in range(3))==1 for b in range(3))

expected_gate={
    (0,1):F(4446471,1051250),
    (0,2):F(44037,42050),
    (1,2):F(818424,525625),
}
for pair,expected in expected_gate.items():
    T,C,slack=gate(B,R,D,*pair)
    assert C==0 and slack==expected and slack>0

derivatives={}
for a in range(3):
    for g in range(a+1,3):
        for name,(Z,eps) in ZBASIS.items():
            derivatives[(a,g,name)]=row_derivative(B,a,g,Z,eps)[0]

expected_derivatives={
    (0,1,"I"):F(-27216,18125),
    (0,1,"J"):F(0),
    (0,1,"S"):F(27216,18125),
    (0,1,"T"):F(0),
    (0,2,"I"):F(-648,725),
    (0,2,"J"):F(0),
    (0,2,"S"):F(648,725),
    (0,2,"T"):F(0),
    (1,2,"I"):F(19278,105125),
    (1,2,"J"):F(0),
    (1,2,"S"):F(-19278,105125),
    (1,2,"T"):F(0),
}
assert derivatives==expected_derivatives

# Exact finite improving genuine SO(6) row-plane rotation for pair (0,1), Z=I.
# Half-angle parameter t=-1/100 gives rational c,s.
t=F(-1,100)
c=(1-t*t)/(1+t*t)
s=2*t/(1+t*t)
W=[row[:] for row in I6]
for i in range(2):
    W[i][i]=c
    W[i][2+i]=s
    W[2+i][i]=-s
    W[2+i][2+i]=c
assert mm(transpose(W),W)==I6
assert det_perm(W)==1
O1=mm(W,O)
assert mm(transpose(O1),O1)==I6
assert det_perm(O1)==1

S0=support(O)
S1=support(O1)
improvement=S1-S0
assert S0==F(1605549,525625)
assert improvement==F(59577629088,2102920521025)
assert improvement>0

print("PASS exact continuous bi-orientation stationarity / cycle-witness exclusion")
print("support_original =", S0)
print("row_discrete_gate_slacks =")
for pair in sorted(expected_gate):
    print(" ", pair, gate(B,R,D,*pair)[2])
print("row_stationarity_derivatives =")
for key in sorted(derivatives):
    print(" ", key, derivatives[key])
print("rational_improving_rotation_c =", c)
print("rational_improving_rotation_s =", s)
print("support_rotated =", S1)
print("exact_improvement =", improvement)
