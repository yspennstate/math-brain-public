from fractions import Fraction as F
from itertools import combinations, permutations


def z(re=0, im=0): return (F(re), F(im))
def za(x,y): return (x[0]+y[0], x[1]+y[1])
def zs(x,y): return (x[0]-y[0], x[1]-y[1])
def zm(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def zq(c,x): return (c*x[0], c*x[1])
def zp(xs):
    out=z(1)
    for x in xs: out=zm(out,x)
    return out
def supp(eta,x): return zm(eta,x)[0]
def comp(S): return tuple(i for i in range(4) if i not in set(S))
def det2(M,rs,cs):
    i,j=rs; k,l=cs
    return M[i][k]*M[j][l]-M[i][l]*M[j][k]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def det4(M):
    out=z()
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        t=z(1)
        for i,j in enumerate(p): t=zm(t,M[i][j])
        out=za(out,zq(F(-1 if inv%2 else 1),t))
    return out

# Account04/B09 exact rational orthogonal separator source, followed by a
# small exact rational TRUE-unitary (orthogonal) plane perturbation.
U0=[
 [F(492,625),F(-31,625),F(-48,125),F(12,25)],
 [F(-9,25),F(12,25),F(-4,5),F(0)],
 [F(-36,125),F(48,125),F(9,25),F(4,5)],
 [F(-256,625),F(-492,625),F(-36,125),F(9,25)]
]
t=F(1,1000)
c=(1-t*t)/(1+t*t)
s=2*t/(1+t*t)
Q=[[F(int(i==j)) for j in range(4)] for i in range(4)]
Q[0][0]=Q[1][1]=c; Q[0][1]=-s; Q[1][0]=s
U=mm(Q,U0)
I=[[F(int(i==j)) for j in range(4)] for i in range(4)]
UTU=[[sum(U[k][i]*U[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
assert UTU==I
assert all(U[i][j]!=0 for i in range(4) for j in range(4))
for rs in combinations(range(4),2):
    for cs in combinations(range(4),2):
        m00,m01=U[rs[0]][cs[0]],U[rs[0]][cs[1]]
        m10,m11=U[rs[1]][cs[0]],U[rs[1]][cs[1]]
        minor=m00*m11-m01*m10
        assert minor!=0
        tr=m00*m00+m01*m01+m10*m10+m11*m11
        assert tr*tr-4*minor*minor!=0

# Gaussian-rational spectra/support normal.  They were obtained by solving for
# a structured support coefficient block near the separating signed direction,
# then rounded and rechecked EXACTLY below.
a=[
 z(F(1592617,1000000),F(1165031,1000000)),
 z(F(-401554,1000000),F(-577389,1000000)),
 z(F(1144510,1000000),F(-779167,1000000)),
 z(F(-717378,1000000),F(-1054671,1000000))
]
b=[
 z(F(961905,1000000),F(657334,1000000)),
 z(F(652386,1000000),F(406944,1000000)),
 z(F(-796717,1000000),F(234805,1000000)),
 z(F(-730534,1000000),F(-372247,1000000))
]
eta=z(F(248743,250000),F(2003,20000))
assert len(set(a))==4 and len(set(b))==4
assert all(x!=z() for x in a+b)
assert all(za(x,y)!=z() for x in a for y in b)

orient=[(0,1),(0,2),(0,3)]
P=[[x*x for x in row] for row in U]
qq={(S,T):det2(U,S,T)**2 for S in combinations(range(4),2) for T in combinations(range(4),2)}
R=[[F(0) for _ in range(3)] for _ in range(3)]
D=[[F(0) for _ in range(3)] for _ in range(3)]
for aa,S in enumerate(orient):
    for bb,T in enumerate(orient):
        qp,qm=qq[S,T],qq[S,comp(T)]
        R[aa][bb]=qp+qm
        D[aa][bb]=qp-qm
assert all(sum(row)==1 for row in R)
assert all(sum(R[i][j] for i in range(3))==1 for j in range(3))

# Reconstruct the exact structured K from account01/B07's support coefficient
# formulas and the lead's standard-representation Hadamard block.
h=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
ac=[zp([a[k] for k in range(4) if k!=i]) for i in range(4)]
bc=[zp([b[k] for k in range(4) if k!=j]) for j in range(4)]
W=[[supp(eta,za(zm(ac[i],b[j]),zm(a[i],bc[j]))) for j in range(4)] for i in range(4)]
Am=[]; Bm=[]
for S in orient:
    Sc=comp(S)
    aS,aSc=zm(a[S[0]],a[S[1]]),zm(a[Sc[0]],a[Sc[1]])
    bS,bSc=zm(b[S[0]],b[S[1]]),zm(b[Sc[0]],b[Sc[1]])
    Am.append(zs(aSc,aS)); Bm.append(zs(bS,bSc))
Y=[[supp(eta,zm(Am[aa],Bm[bb])) for bb in range(3)] for aa in range(3)]
Z=[[sum(F(h[aa][i]*h[bb][j],8)*Y[aa][bb] for aa in range(3) for bb in range(3)) for j in range(4)] for i in range(4)]
C=[[W[i][j]+Z[i][j] for j in range(4)] for i in range(4)]
K=[[sum(F(h[aa][i]*h[bb][j],4)*C[i][j] for i in range(4) for j in range(4)) for bb in range(3)] for aa in range(3)]

perms=list(permutations(range(3)))
def mcost(p):
    vv=[K[i][p[i]] for i in range(3)]
    pr=vv[0]*vv[1]*vv[2]
    return F(0) if pr>=0 else min(abs(x) for x in vv)
m=[mcost(p) for p in perms]

# All Birkhoff decompositions of this exact R are lambda(tau)=base+tau*n.
base=[
 F(31495970140431264,390625781250390625),
 F(76729246309676961,390625781250390625),
 F(90656333152091136,390625781250390625),
 F(256768270592256,625001250000625),
 F(31264,390625),
 F(0)
]
n=[F(-1),F(1),F(1),F(-1),F(-1),F(1)]
def recon(weights):
    out=[[F(0) for _ in range(3)] for _ in range(3)]
    for w,p in zip(weights,perms):
        for i in range(3): out[i][p[i]]+=w
    return out
assert recon(base)==R
assert recon(n)==[[F(0)]*3 for _ in range(3)]
A=[]
for i in range(3):
    for j in range(3):
        A.append([F(1 if p[i]==j else 0) for p in perms])
def rank(M):
    M=[row[:] for row in M]; r=0
    for col in range(len(M[0])):
        piv=next((i for i in range(r,len(M)) if M[i][col]),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        q=M[r][col]; M[r]=[x/q for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][col]:
                q=M[i][col]; M[i]=[M[i][j]-q*M[r][j] for j in range(len(M[0]))]
        r+=1
    return r
assert rank(A)==5
# Since lambda_5=tau, nonnegativity forces tau>=0.  The exact objective
# slope is positive, so tau=0 is the minimum over ALL decompositions.
slope=sum(n[i]*m[i] for i in range(6))
assert slope>0
penalty=sum(base[i]*m[i] for i in range(6))
slack=sum(R[i][j]*abs(K[i][j])-D[i][j]*K[i][j] for i in range(3) for j in range(3))
deficit=slack-2*penalty
assert deficit < 0

# Exact generic strict-support checks for this same datum.
verts=[]
for p in permutations(range(4)):
    vv=z(1)
    for i,j in enumerate(p): vv=zm(vv,za(a[i],b[j]))
    verts.append((supp(eta,vv),p,vv))
assert len({vv for _,_,vv in verts})==24
verts.sort(key=lambda x:x[0],reverse=True)
assert verts[0][0] > verts[1][0]
support_gap=verts[0][0]-verts[1][0]

B=[[z() for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        for k in range(4): B[i][j]=za(B[i][j],zq(U[i][k]*U[j][k],b[k]))
assert all(B[i][j]!=z() for i in range(4) for j in range(i+1,4))
M=[[B[i][j] for j in range(4)] for i in range(4)]
for i in range(4): M[i][i]=za(M[i][i],a[i])
det=det4(M)
det_gap=supp(eta,det)-verts[0][0]
assert det_gap < 0

print("PASS exact true-unitary structured parity-slack refutation")
print("U true orthogonal; all 1x1/2x2 entries/minors and tested compression discriminants nonzero")
print("K_float =", [[float(x) for x in row] for row in K])
print("m_float =", [float(x) for x in m])
print("birkhoff_objective_slope =", slope)
print("min_penalty =", penalty)
print("orientation_slack =", slack)
print("PS_deficit_slack_minus_2penalty =", deficit)
print("PS_deficit_float =", float(deficit))
print("unique_support_max_perm_1based =", tuple(x+1 for x in verts[0][1]))
print("unique_vertex_support_gap =", support_gap)
print("unique_vertex_support_gap_float =", float(support_gap))
print("det_support_minus_vertex_max =", det_gap)
print("det_support_minus_vertex_max_float =", float(det_gap))
