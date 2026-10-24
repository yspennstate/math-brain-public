from fractions import Fraction as F
from itertools import permutations

PERMS = list(permutations(range(3)))
PAIRS = [(0,1),(0,2),(0,3)]
ALL4 = set(range(4))
HSGN = [
    [1,1,1,1],
    [1,1,-1,-1],
    [1,-1,1,-1],
    [1,-1,-1,1],
]

def zadd(z,w): return (z[0]+w[0], z[1]+w[1])
def zsub(z,w): return (z[0]-w[0], z[1]-w[1])
def zmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def zprod(xs):
    z=(F(1),F(0))
    for x in xs: z=zmul(z,x)
    return z
def re_eta(eta,z): return zmul(eta,z)[0]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def givens(n,i,j,c,s):
    G=eye(n)
    G[i][i]=c; G[j][j]=c
    G[i][j]=s; G[j][i]=-s
    return G
def dot(x,y): return sum(a*b for a,b in zip(x,y))

# Exact rational orthogonal witness used in the earlier common-(P,R)-lift obstruction.
U0 = [
 [F(492,625), F(-31,625), F(-48,125), F(12,25)],
 [F(-9,25), F(12,25), F(-4,5), F(0)],
 [F(-36,125), F(48,125), F(9,25), F(4,5)],
 [F(-256,625), F(-492,625), F(-36,125), F(9,25)],
]

# Tiny exact right Givens perturbation on columns 1 and 4 (zero based 0,3).
t=F(1,5000)
c=(1-t*t)/(1+t*t)
s=2*t/(1+t*t)
U=mm(U0,givens(4,0,3,c,s))

# Exact simple nonzero structured spectra and eta=1.
a=[(F(-9,40),F(-39,20)), (F(-7,20),F(-37,40)),
   (F(-13,10),F(13,40)), (F(1,4),F(-7,10))]
b=[(F(-1,40),F(11,40)), (F(13,40),F(17,40)),
   (F(-23,40),F(-21,40)), (F(-59,40),F(33,40))]
eta=(F(1),F(0))

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
            Z=sum(F(HSGN[aa+1][i]*HSGN[bb+1][j],8)*Y[aa][bb]
                  for aa in range(3) for bb in range(3))
            C[i][j]=W[i][j]+Z
    K=[[sum(F(HSGN[r+1][i]*HSGN[cc+1][j],4)*C[i][j]
             for i in range(4) for j in range(4))
        for cc in range(3)] for r in range(3)]
    return K,X

K,X=structured_K_X(a,b,eta)

def det2(rows,cols):
    i,k=rows; j,l=cols
    return U[i][j]*U[k][l]-U[i][l]*U[k][j]

R=[[F(0) for _ in range(3)] for _ in range(3)]
D=[[F(0) for _ in range(3)] for _ in range(3)]
qvals=[]
for aa,S in enumerate(PAIRS):
    for bb,T in enumerate(PAIRS):
        Tc=tuple(sorted(ALL4-set(T)))
        qp=det2(S,T)**2
        qm=det2(S,Tc)**2
        qvals += [qp,qm]
        R[aa][bb]=qp+qm
        D[aa][bb]=qp-qm

def mval(p):
    vals=[K[i][p[i]] for i in range(3)]
    return F(0) if vals[0]*vals[1]*vals[2]>=0 else min(abs(x) for x in vals)
def Fphi(p):
    vals=[K[i][p[i]] for i in range(3)]
    ans=sum(abs(x) for x in vals)
    if vals[0]*vals[1]*vals[2]<0:
        ans-=2*min(abs(x) for x in vals)
    return ans
m={p:mval(p) for p in PERMS}

# Every 3x3 Birkhoff decomposition is this one-dimensional family.
r11=R[0][0]; r23=R[1][2]; r32=R[2][1]; r33=R[2][2]; r22=R[1][1]
L=max(F(0),r11-r23,r11-r32)
Uend=min(r11,r22,r33)
def lambdas(tau):
    return {
      (0,1,2):tau,
      (1,2,0):tau+r23-r11,
      (2,0,1):tau+r32-r11,
      (0,2,1):r11-tau,
      (1,0,2):r33-tau,
      (2,1,0):r22-tau,
    }
def penalty(tau):
    la=lambdas(tau)
    return sum(la[p]*m[p] for p in PERMS)
ML=penalty(L); MU=penalty(Uend)
Mmin=min(ML,MU); Mmax=max(ML,MU)
tmin=L if ML<=MU else Uend
lam=lambdas(tmin)

slack=sum(R[i][j]*abs(K[i][j])-D[i][j]*K[i][j]
          for i in range(3) for j in range(3))
gate_deficit=2*Mmin-slack

fiber={p:Fphi(p)+F(1,2)*sum(X[i][p[i]] for i in range(3)) for p in PERMS}
rhs=max(fiber.values())
lhs=sum(D[i][j]*K[i][j]+F(1,2)*R[i][j]*X[i][j]
        for i in range(3) for j in range(3))
sr_gap=rhs-lhs
g={p:rhs-fiber[p] for p in PERMS}
rescue=sum(lam[p]*g[p] for p in PERMS)

# Enumerate all 24 signed S4 endpoint images (six fibers x four even sign patterns).
signed_values=[]
for p in PERMS:
    for eps in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]:
        v=sum(F(eps[i])*K[i][p[i]] for i in range(3))
        v+=F(1,2)*sum(X[i][p[i]] for i in range(3))
        signed_values.append((v,p,eps))
max24=max(v for v,_,_ in signed_values)
maximizers=[(p,eps) for v,p,eps in signed_values if v==max24]

assert all(dot(U[i],U[j])==F(int(i==j)) for i in range(4) for j in range(4))
assert all(U[i][j]!=0 for i in range(4) for j in range(4))
assert all(q>0 for q in qvals)
assert all(sum(R[i][j] for j in range(3))==1 for i in range(3))
assert all(sum(R[i][j] for i in range(3))==1 for j in range(3))
assert all(abs(D[i][j])<R[i][j] for i in range(3) for j in range(3))
assert L<=Uend
for tau in (L,Uend,tmin):
    la=lambdas(tau)
    assert all(v>=0 for v in la.values())
    assert sum(la.values())==1
    for i in range(3):
        for j in range(3):
            assert sum(la[p] for p in PERMS if p[i]==j)==R[i][j]
assert gate_deficit>0
assert sr_gap>0
assert max24==rhs and len(maximizers)==1
assert rescue-gate_deficit==sr_gap

print('PASS exact MOC4 parity-slack counterexample / SR-rescue certificate')
print('c_small =', c)
print('s_small =', s)
print('K =')
for row in K: print(' ', [str(x) for x in row])
print('X =')
for row in X: print(' ', [str(x) for x in row])
print('L =', L)
print('U =', Uend)
print('M_min =', Mmin)
print('M_max =', Mmax)
print('orientation_slack =', slack)
print('parity_gate_deficit = 2*M_min-slack =', gate_deficit)
print('exact_SR_lhs =', lhs)
print('exact_SR_rhs =', rhs)
print('exact_SR_gap =', sr_gap)
print('support_gap_rescue_at_min_endpoint =', rescue)
print('unique_24_vertex_maximizer =', maximizers[0])
