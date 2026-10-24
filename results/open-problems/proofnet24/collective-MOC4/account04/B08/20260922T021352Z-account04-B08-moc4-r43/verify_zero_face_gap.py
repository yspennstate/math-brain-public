from fractions import Fraction as F
from itertools import permutations

PERMS=list(permutations(range(3)))
PAIRS=[(0,1),(0,2),(0,3)]
ALL4=set(range(4))
HSGN=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]

def zadd(z,w): return (z[0]+w[0], z[1]+w[1])
def zsub(z,w): return (z[0]-w[0], z[1]-w[1])
def zmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def zprod(xs):
    z=(F(1),F(0))
    for x in xs: z=zmul(z,x)
    return z
def re_eta(eta,z): return zmul(eta,z)[0]
def dot(x,y): return sum(a*b for a,b in zip(x,y))

# Exact zero-entry rational orthogonal source datum, obtained by relabelling
# the unperturbed account01/B07 source matrix so that u_00=0.
U=[
 [F(0), F(-9,25), F(12,25), F(-4,5)],
 [F(12,25), F(492,625), F(-31,625), F(-48,125)],
 [F(4,5), F(-36,125), F(48,125), F(9,25)],
 [F(9,25), F(-256,625), F(-492,625), F(-36,125)],
]
a=[(F(-7,20),F(-37,40)), (F(-9,40),F(-39,20)),
   (F(-13,10),F(13,40)), (F(1,4),F(-7,10))]
b=[(F(-59,40),F(33,40)), (F(-1,40),F(11,40)),
   (F(13,40),F(17,40)), (F(-23,40),F(-21,40))]
eta=(F(1),F(0))

assert all(dot(U[i],U[j])==F(int(i==j)) for i in range(4) for j in range(4))
assert U[0][0]==0

def structured_K_X(a,b,eta):
    W=[[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        ai_c=zprod([a[k] for k in range(4) if k!=i])
        for j in range(4):
            bj_c=zprod([b[k] for k in range(4) if k!=j])
            W[i][j]=re_eta(eta,zadd(zmul(ai_c,b[j]),zmul(a[i],bj_c)))
    Y=[[F(0) for _ in range(3)] for _ in range(3)]
    X=[[F(0) for _ in range(3)] for _ in range(3)]
    for aa,S in enumerate(PAIRS):
        Sc=tuple(sorted(ALL4-set(S)))
        Aminus=zsub(zprod([a[k] for k in Sc]),zprod([a[k] for k in S]))
        Aplus=zadd(zprod([a[k] for k in Sc]),zprod([a[k] for k in S]))
        for bb,T in enumerate(PAIRS):
            Tc=tuple(sorted(ALL4-set(T)))
            Bminus=zsub(zprod([b[k] for k in T]),zprod([b[k] for k in Tc]))
            Bplus=zadd(zprod([b[k] for k in T]),zprod([b[k] for k in Tc]))
            Y[aa][bb]=re_eta(eta,zmul(Aminus,Bminus))
            X[aa][bb]=re_eta(eta,zmul(Aplus,Bplus))
    C=[[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            C[i][j]=W[i][j]+sum(
                F(HSGN[aa+1][i]*HSGN[bb+1][j],8)*Y[aa][bb]
                for aa in range(3) for bb in range(3))
    K=[[sum(F(HSGN[r+1][i]*HSGN[c+1][j],4)*C[i][j]
             for i in range(4) for j in range(4))
        for c in range(3)] for r in range(3)]
    return K,X

K,X=structured_K_X(a,b,eta)

def det2(rows,cols):
    i,k=rows; j,l=cols
    return U[i][j]*U[k][l]-U[i][l]*U[k][j]

R=[[F(0) for _ in range(3)] for _ in range(3)]
D=[[F(0) for _ in range(3)] for _ in range(3)]
Q=[[F(0) for _ in range(3)] for _ in range(3)]
for aa,S in enumerate(PAIRS):
    for bb,T in enumerate(PAIRS):
        Tc=tuple(sorted(ALL4-set(T)))
        qp=det2(S,T)**2
        qm=det2(S,Tc)**2
        R[aa][bb]=qp+qm
        D[aa][bb]=qp-qm
        Q[aa][bb]=qp

x=[U[i][0]**2 for i in range(1,4)]
y=[U[0][j]**2 for j in range(1,4)]
assert sum(x)==sum(y)==1
assert all(Q[i][j]==x[i]*y[j] for i in range(3) for j in range(3))
assert all(D[i][j]==2*Q[i][j]-R[i][j] for i in range(3) for j in range(3))
assert all(sum(R[i][j] for j in range(3))==1 for i in range(3))
assert all(sum(R[i][j] for i in range(3))==1 for j in range(3))

def Fphi(p):
    vals=[K[i][p[i]] for i in range(3)]
    return max(sum(eps[i]*vals[i] for i in range(3))
               for eps in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)])

def kval(p): return sum(K[i][p[i]] for i in range(3))
def Hmark(p):
    vals=[K[i][p[i]] for i in range(3)]
    return max(kval(p), *vals)

assert all(Fphi(p)+kval(p)==2*Hmark(p) for p in PERMS)

fiber={p:Fphi(p)+F(1,2)*sum(X[i][p[i]] for i in range(3)) for p in PERMS}
M=max(fiber.values())
g={p:M-fiber[p] for p in PERMS}
lhs=sum(D[i][j]*K[i][j]+F(1,2)*R[i][j]*X[i][j]
        for i in range(3) for j in range(3))
sr_gap=M-lhs

r11=R[0][0]; r23=R[1][2]; r32=R[2][1]; r33=R[2][2]; r22=R[1][1]
L=max(F(0),r11-r23,r11-r32)
Uend=min(r11,r22,r33)
def lambdas(t):
    return {
      (0,1,2):t,
      (1,2,0):t+r23-r11,
      (2,0,1):t+r32-r11,
      (0,2,1):r11-t,
      (1,0,2):r33-t,
      (2,1,0):r22-t,
    }

QK=sum(Q[i][j]*K[i][j] for i in range(3) for j in range(3))
endpoint_rows=[]
for tag,t in [('L',L),('U',Uend)]:
    la=lambdas(t)
    assert all(v>=0 for v in la.values()) and sum(la.values())==1
    assert all(sum(la[p] for p in PERMS if p[i]==j)==R[i][j]
               for i in range(3) for j in range(3))
    EH=sum(la[p]*Hmark(p) for p in PERMS)
    G=sum(la[p]*g[p] for p in PERMS)
    marked_part=2*(EH-QK)
    assert G+marked_part==sr_gap
    endpoint_rows.append((tag,t,EH,marked_part,G))

# Recheck the older parity-slack route on this zero face as a secondary diagnostic.
def mval(p):
    vals=[K[i][p[i]] for i in range(3)]
    return F(0) if vals[0]*vals[1]*vals[2]>=0 else min(abs(v) for v in vals)
def penalty(t):
    la=lambdas(t)
    return sum(la[p]*mval(p) for p in PERMS)
S=sum(R[i][j]*abs(K[i][j])-D[i][j]*K[i][j]
      for i in range(3) for j in range(3))
pL,pU=penalty(L),penalty(Uend)
parity_best_deficit=2*min(pL,pU)-S

assert endpoint_rows[0][3] < 0
assert endpoint_rows[1][3] < 0
assert parity_best_deficit > 0
assert sr_gap > 0

print("PASS exact zero-face gap decomposition")
print("x =", [str(v) for v in x])
print("y =", [str(v) for v in y])
print("L =", L)
print("U =", Uend)
print("QK =", QK)
for tag,t,EH,marked_part,G in endpoint_rows:
    print(tag, "EH =", EH)
    print(tag, "2(EH-QK) =", marked_part)
    print(tag, "fiber_gap_rescue =", G)
    print(tag, "total_gap =", G+marked_part)
print("parity_best_deficit =", parity_best_deficit)
print("exact_SR_gap =", sr_gap)
