from fractions import Fraction as F
from itertools import permutations, combinations

# Gaussian rationals z=(re,im), both Fractions.
def C(re=0, im=0):
    return (F(re), F(im))
def cadd(z,w): return (z[0]+w[0], z[1]+w[1])
def csub(z,w): return (z[0]-w[0], z[1]-w[1])
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cscale(q,z): return (q*z[0], q*z[1])
def cconj(z): return (z[0],-z[1])
def cprod(xs):
    z=C(1,0)
    for x in xs: z=cmul(z,x)
    return z

def matmul(A,B):
    n=len(A); m=len(B); p=len(B[0])
    out=[[F(0) for _ in range(p)] for __ in range(n)]
    for i in range(n):
        for k in range(m):
            for j in range(p):
                out[i][j]+=A[i][k]*B[k][j]
    return out
def transpose(A): return [list(x) for x in zip(*A)]

def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def sub2(U,S,T):
    return [[U[i][j] for j in T] for i in S]

def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def cdet(M):
    n=len(M)
    total=C()
    for p in permutations(range(n)):
        term=C(parity(p),0)
        for i in range(n):
            term=cmul(term,M[i][p[i]])
        total=cadd(total,term)
    return total

def cdet_directional(M,dM):
    n=len(M); total=C()
    for p in permutations(range(n)):
        s=F(parity(p))
        for k in range(n):
            term=C(s,0)
            for i in range(n):
                term=cmul(term, dM[i][p[i]] if i==k else M[i][p[i]])
            total=cadd(total,term)
    return total

def cmatmul(A,B):
    n=len(A); m=len(B); p=len(B[0])
    out=[[C() for _ in range(p)] for __ in range(n)]
    for i in range(n):
        for k in range(m):
            for j in range(p):
                out[i][j]=cadd(out[i][j],cmul(A[i][k],B[k][j]))
    return out
def ctranspose(A): return [list(x) for x in zip(*A)]

def real_eta(eta,z):
    return cmul(eta,z)[0]

# Exact rational orthogonal U = G_{24}(399/401,40/401) * U0.
U0=[
 [F(492,625),-F(31,625),-F(48,125),F(12,25)],
 [-F(9,25),F(12,25),-F(4,5),F(0)],
 [-F(36,125),F(48,125),F(9,25),F(4,5)],
 [-F(256,625),-F(492,625),-F(36,125),F(9,25)]
]
G=[[F(int(i==j)) for j in range(4)] for i in range(4)]
G[1][1]=F(399,401); G[3][3]=F(399,401)
G[1][3]=-F(40,401); G[3][1]=F(40,401)
U=matmul(G,U0)
I4=[[F(int(i==j)) for j in range(4)] for i in range(4)]
assert matmul(U,transpose(U))==I4
assert all(U[i][j] != 0 for i in range(4) for j in range(4))
for S in combinations(range(4),2):
    for T in combinations(range(4),2):
        assert det2(sub2(U,S,T)) != 0

H=[
 [F(1,2),F(1,2),F(1,2),F(1,2)],
 [F(1,2),F(1,2),-F(1,2),-F(1,2)],
 [F(1,2),-F(1,2),F(1,2),-F(1,2)],
 [F(1,2),-F(1,2),-F(1,2),F(1,2)]
]
hs=[
 [F(1),F(1),-F(1),-F(1)],
 [F(1),-F(1),F(1),-F(1)],
 [F(1),-F(1),-F(1),F(1)]
]
P=[[U[i][j]*U[i][j] for j in range(4)] for i in range(4)]
HPHt=matmul(matmul(H,P),transpose(H))
D=[row[1:] for row in HPHt[1:]]

pairs=[(0,1),(0,2),(0,3)]
def comp(S): return tuple(i for i in range(4) if i not in S)
R=[[F(0) for j in range(3)] for i in range(3)]
qplus=[[F(0) for j in range(3)] for i in range(3)]
qminus=[[F(0) for j in range(3)] for i in range(3)]
for i,S in enumerate(pairs):
    for j,T in enumerate(pairs):
        qp=det2(sub2(U,S,T))**2
        qm=det2(sub2(U,S,comp(T)))**2
        assert qp>0 and qm>0
        qplus[i][j]=qp; qminus[i][j]=qm; R[i][j]=qp+qm
        assert D[i][j]==qp-qm
for i in range(3):
    assert sum(R[i])==1
for j in range(3):
    assert sum(R[i][j] for i in range(3))==1

# Exact simple spectra and exact unit support direction.
a=[
 (F(-8,5),F(-29,5)),
 (F(-1),F(6,5)),
 (F(3,5),F(-6,5)),
 (F(-4,5),F(3))
]
b=[
 (F(0),F(-7,5)),
 (F(3,5),F(-1)),
 (F(-1,5),F(6,5)),
 (F(14,5),F(17,5))
]
eta=(F(-85,157),F(-132,157))
assert cmul(eta,cconj(eta))==C(1,0)
assert len(set(a))==4 and len(set(b))==4
assert all(cadd(a[i],b[j])!=C() for i in range(4) for j in range(4))

def cprod_idx(arr, inds): return cprod([arr[i] for i in inds])
aic=[cprod_idx(a,[j for j in range(4) if j!=i]) for i in range(4)]
bic=[cprod_idx(b,[j for j in range(4) if j!=i]) for i in range(4)]
W=[[F(0) for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        W[i][j]=real_eta(eta,cadd(cmul(aic[i],b[j]),cmul(a[i],bic[j])))

Aminus=[]; Bminus=[]; Aplus=[]; Bplus=[]
for S in pairs:
    Aminus.append(csub(cprod_idx(a,comp(S)),cprod_idx(a,S)))
    Aplus.append(cadd(cprod_idx(a,comp(S)),cprod_idx(a,S)))
for T in pairs:
    Bminus.append(csub(cprod_idx(b,T),cprod_idx(b,comp(T))))
    Bplus.append(cadd(cprod_idx(b,T),cprod_idx(b,comp(T))))
Y=[[real_eta(eta,cmul(Aminus[i],Bminus[j])) for j in range(3)] for i in range(3)]
X=[[real_eta(eta,cmul(Aplus[i],Bplus[j])) for j in range(3)] for i in range(3)]
Z=matmul(matmul(transpose(hs),Y),hs)
Z=[[x/F(8) for x in row] for row in Z]
Cmat=[[W[i][j]+Z[i][j] for j in range(4)] for i in range(4)]
HCHt=matmul(matmul(H,Cmat),transpose(H))
K=[row[1:] for row in HCHt[1:]]

K_expected=[
 [F(1285076,98125),F(4665936,98125),-F(1562076,98125)],
 [-F(6796296,98125),-F(476876,19625),F(1802184,98125)],
 [F(2093004,98125),-F(1257338,98125),F(4522321,98125)]
]
assert K==K_expected

E0=(0,1,2); E1=(1,2,0); E2=(2,0,1)
O0=(0,2,1); O1=(2,1,0); O2=(1,0,2)

def fcost(p):
    x=[K[i][p[i]] for i in range(3)]
    s=sum(abs(v) for v in x)
    if x[0]*x[1]*x[2] < 0:
        s-=2*min(abs(v) for v in x)
    return s
def mcost(p):
    x=[K[i][p[i]] for i in range(3)]
    return F(0) if x[0]*x[1]*x[2]>=0 else min(abs(v) for v in x)

L=max(F(0),R[2][2]-R[0][1],R[1][1]-R[0][2])
Uend=min(R[0][0],R[1][1],R[2][2])
assert L==F(3360256,2512515625)
assert Uend==F(31264,390625)

def weights(x):
    return {
      E0:x,
      E1:R[0][1]-R[2][2]+x,
      E2:R[0][2]-R[1][1]+x,
      O0:R[0][0]-x,
      O1:R[1][1]-x,
      O2:R[2][2]-x
    }
def reconstruct(w):
    Q=[[F(0) for _ in range(3)] for __ in range(3)]
    for p,v in w.items():
        for i in range(3): Q[i][p[i]]+=v
    return Q

endpoint=[]
for x in (L,Uend):
    w=weights(x)
    assert all(v>=0 for v in w.values()) and sum(w.values())==1
    assert reconstruct(w)==R
    M=sum(w[p]*mcost(p) for p in w)
    J=sum(w[p]*fcost(p) for p in w)
    endpoint.append((x,M,J,w))

# Exact 3x3 Birkhoff-roof theorem:
# weighted absolute assignment part is <R,|K|>, while J=<R,|K|>-2M.
RabsK=sum(R[i][j]*abs(K[i][j]) for i in range(3) for j in range(3))
for x,M,J,w in endpoint:
    assert J==RabsK-2*M
Psi=min(J for x,M,J,w in endpoint)
Mmax=max(M for x,M,J,w in endpoint)
assert Psi==RabsK-2*Mmax

DK=sum(D[i][j]*K[i][j] for i in range(3) for j in range(3))
roof_gap=DK-Psi
assert roof_gap==F(4570193437650692,6163514892578125)
assert roof_gap>0

slack=RabsK-DK
ML=[z[1] for z in endpoint if z[0]==L][0]
MU=[z[1] for z in endpoint if z[0]==Uend][0]
# This demonstrates the logical flaw in "there exists a decomposition satisfying PS":
# the U endpoint satisfies 2M<=slack, but the roof-minimizing endpoint L violates it.
assert 2*MU <= slack
assert 2*ML > slack

# Generic unique exposed permutation support.
def vsigma(p):
    return cprod([cadd(a[i],b[p[i]]) for i in range(4)])
scores=[(real_eta(eta,vsigma(p)),p) for p in permutations(range(4))]
scores.sort(reverse=True)
assert len({s for s,p in scores})==24
assert scores[0][1]==(0,2,3,1)
assert scores[0][0]==F(2973192,19625)
assert scores[0][0]-scores[1][0]==F(5578176,98125)

# Exact target support is well inside the hull in this direction.
# B = U diag(b) U^T using Gaussian-rational arithmetic.
Uc=[[C(U[i][j],0) for j in range(4)] for i in range(4)]
Bdiag=[[C() for j in range(4)] for i in range(4)]
for i in range(4): Bdiag[i][i]=b[i]
Bmat=cmatmul(cmatmul(Uc,Bdiag),ctranspose(Uc))
Xmat=[[Bmat[i][j] for j in range(4)] for i in range(4)]
for i in range(4): Xmat[i][i]=cadd(Xmat[i][i],a[i])
det_actual=cdet(Xmat)
support_actual=real_eta(eta,det_actual)
assert support_actual==F(371150847508507028,6163514892578125)
assert scores[0][0]-support_actual==F(562623072007117972,6163514892578125)>0

# Exact six-fiber SR identity also holds with large slack.
SR_lhs=DK+F(1,2)*sum(R[i][j]*X[i][j] for i in range(3) for j in range(3))
rhs=[]
for p in permutations(range(4)):
    Pp=[[F(0) for j in range(4)] for i in range(4)]
    for i in range(4): Pp[i][p[i]]=1
    Sfull=matmul(matmul(H,Pp),transpose(H))
    S=[row[1:] for row in Sfull[1:]]
    val=sum(S[i][j]*K[i][j] for i in range(3) for j in range(3))
    val+=F(1,2)*sum(abs(S[i][j])*X[i][j] for i in range(3) for j in range(3))
    rhs.append((val,p))
rhs.sort(reverse=True)
assert rhs[0][1]==(0,2,3,1)
assert rhs[0][0]-SR_lhs==scores[0][0]-support_actual

# Apply account02/B09 BIPAIR result: this witness is not pair-stationary.
# Row rotation generator J_{12}: B'=[J,B], det' is exact directional derivative.
J=[[F(0) for j in range(4)] for i in range(4)]
J[0][1]=-1; J[1][0]=1
Jc=[[C(J[i][j],0) for j in range(4)] for i in range(4)]
JB=cmatmul(Jc,Bmat); BJ=cmatmul(Bmat,Jc)
dB=[[csub(JB[i][j],BJ[i][j]) for j in range(4)] for i in range(4)]
ddet=cdet_directional(Xmat,dB)
row12_derivative=real_eta(eta,ddet)
assert row12_derivative==F(245364861810144,3074072265625)
assert row12_derivative!=0

print("PASS exact parity-roof counterexample")
print("L =", L)
print("U =", Uend)
print("M(L) =", ML)
print("M(U) =", MU)
print("slack/2 =", slack/2)
print("<D,K> - Psi =", roof_gap)
print("support actual =", support_actual)
print("support max vertex =", scores[0][0], "at", scores[0][1])
print("support slack =", scores[0][0]-support_actual)
print("row(1,2) support derivative =", row12_derivative)
