from fractions import Fraction as F
from itertools import permutations, combinations

def add(z,w): return (z[0]+w[0], z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def scale(c,z): return (c*z[0], c*z[1])
ZERO=(F(0),F(0)); ONE=(F(1),F(0))

def parity(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

def det_scalar(A):
    n=len(A); s=F(0)
    for p in permutations(range(n)):
        t=F(parity(p))
        for i in range(n): t*=A[i][p[i]]
        s+=t
    return s

def det_gauss(A):
    n=len(A); s=ZERO
    for p in permutations(range(n)):
        t=(F(parity(p)),F(0))
        for i in range(n): t=mul(t,A[i][p[i]])
        s=add(s,t)
    return s

def transpose(A): return [list(x) for x in zip(*A)]
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]

U=[
 [F(636,1105), F(-423,1105), F(-12,65), F(-772,1105)],
 [F(3576,5525), F(332,5525), F(-144,325), F(3411,5525)],
 [F(164,425), F(348,425), F(9,25), F(-96,425)],
 [F(27,85), F(-36,85), F(4,5), F(24,85)],
]
assert matmul(transpose(U),U)==eye(4)
assert det_scalar(U)==1
assert all(U[i][j] for i in range(4) for j in range(4))
assert all(U[I[0]][J[0]]*U[I[1]][J[1]]-U[I[0]][J[1]]*U[I[1]][J[0]] for I in combinations(range(4),2) for J in combinations(range(4),2))

a=[(F(-4),F(4)), (F(0),F(-1)), (F(-3),F(2)), (F(-4),F(-4))]
b=[(F(-4),F(-4)), (F(2),F(-1)), (F(2),F(-4)), (F(4),F(-1))]
assert len(set(a))==4 and len(set(b))==4
assert all(z[1] != 0 for z in a+b)

M=[[ZERO for _ in range(4)] for __ in range(4)]
for i in range(4):
    for j in range(4):
        z=ZERO
        for k in range(4): z=add(z, scale(U[i][k]*U[j][k], b[k]))
        if i==j: z=add(z,a[i])
        M[i][j]=z

detAB=det_gauss(M)
expected=(F(-82603754544,763140625), F(-3513801072,763140625))
assert detAB==expected

def vertex(p):
    z=ONE
    for i in range(4): z=mul(z, add(a[i], b[p[i]]))
    return z

P=list(permutations(range(4))); V={p:vertex(p) for p in P}
assert len(set(V.values()))==24
p1=(0,1,2,3); p2=(0,1,3,2); p3=(0,3,1,2)
assert V[p1]==(F(80),F(-240)); assert V[p2]==(F(64),F(256)); assert V[p3]==(F(-416),F(-32))
w1=F(1442439283,4637546875); w2=F(57833177464,180864328125); w3=F(66776018624,180864328125)
assert w1>0 and w2>0 and w3>0 and w1+w2+w3==1
combo=add(add(scale(w1,V[p1]),scale(w2,V[p2])),scale(w3,V[p3])); assert combo==detAB

def area2(z1,z2,z3): return (z2[0]-z1[0])*(z3[1]-z1[1])-(z2[1]-z1[1])*(z3[0]-z1[0])
assert area2(V[p1],V[p2],V[p3])==F(242688)

ordr=[(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]; sgn=[1,1,1,-1,1,1]
def q_arrays(W):
    O=[[F(0) for _ in range(6)] for __ in range(6)]
    for aa,IJ in enumerate(ordr):
        i,j=IJ
        for bb,KL in enumerate(ordr):
            k,l=KL
            O[aa][bb]=F(sgn[aa]*sgn[bb])*(W[i][k]*W[j][l]-W[i][l]*W[j][k])
    qp=[[F(0) for _ in range(3)] for __ in range(3)]; qm=[[F(0) for _ in range(3)] for __ in range(3)]
    for aa in range(3):
        for bb in range(3):
            A,B0=O[2*aa][2*bb],O[2*aa][2*bb+1]; C,D0=O[2*aa+1][2*bb],O[2*aa+1][2*bb+1]
            qp[aa][bb]=((A+D0)**2+(C-B0)**2)/4; qm[aa][bb]=((A-D0)**2+(C+B0)**2)/4
    R=[[qp[i][j]+qm[i][j] for j in range(3)] for i in range(3)]
    D=[[qp[i][j]-qm[i][j] for j in range(3)] for i in range(3)]
    return R,D

def Phi(R,D): return R[0][0]-R[0][1]+3*D[0][2]+3*D[1][0]+R[1][1]-R[1][2]-R[2][0]-3*D[2][1]+R[2][2]
R,D=q_arrays(U); phi_true=Phi(R,D)
assert phi_true==F(2403485709,763140625)
assert phi_true-F(3)==F(114063834,763140625)>0
phi={}
for p in P:
    W=[[F(0) for _ in range(4)] for __ in range(4)]
    for i in range(4): W[i][p[i]]=F(1)
    Rp,Dp=q_arrays(W); phi[p]=Phi(Rp,Dp)
assert max(phi.values())==3 and set(phi.values())=={F(-9),F(-3),F(3)}
assert phi[p1]==phi[p2]==phi[p3]==3
phi_cert=w1*phi[p1]+w2*phi[p2]+w3*phi[p3]
assert phi_cert==3 and phi_true-phi_cert==F(114063834,763140625)

print('PASS MOC4-SIMPLE-COMPLEX-EVEN-LIFT-NOGO-v1 exact certificate')
print('U^T U = I, det(U)=1; all entries and all 2x2 minors nonzero')
print('a =', a); print('b =', b); print('det(A+B) =', detAB)
print('24 target vertices distinct = PASS')
print('certificate permutations =', p1,p2,p3)
print('certificate vertices =', V[p1],V[p2],V[p3])
print('certificate weights =', w1,w2,w3)
print('triangle doubled area =', F(242688))
print('Phi(true q) =', phi_true); print('max Phi(24 q endpoints) = 3')
print('Phi gap =', phi_true-F(3)); print('certificate endpoint Phi values =', phi[p1],phi[p2],phi[p3])
