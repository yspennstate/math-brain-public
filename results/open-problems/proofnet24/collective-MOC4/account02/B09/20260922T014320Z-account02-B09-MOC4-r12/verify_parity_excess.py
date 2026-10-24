#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations, combinations

# Gaussian rationals as pairs (re,im).
def zadd(x,y): return (x[0]+y[0], x[1]+y[1])
def zsub(x,y): return (x[0]-y[0], x[1]-y[1])
def zmul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def zscale(q,x): return (q*x[0],q*x[1])
def zprod(xs):
    z=(F(1),F(0))
    for x in xs: z=zmul(z,x)
    return z
def zreal(x): return x[0]
def zzero(x): return x==(F(0),F(0))
def zsum(xs):
    out=(F(0),F(0))
    for x in xs: out=zadd(out,x)
    return out

def matmul(A,B):
    m,n,p=len(A),len(B),len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]
def transpose(A): return [list(r) for r in zip(*A)]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def det2(U,rs,cs):
    i,j=rs; k,l=cs
    return U[i][k]*U[j][l]-U[i][l]*U[j][k]
def perm_sign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1
def zdet(M):
    n=len(M); out=(F(0),F(0))
    for p in permutations(range(n)):
        term=zprod([M[i][p[i]] for i in range(n)])
        out=zadd(out,zscale(F(perm_sign(p)),term))
    return out

U0=[
 [F(492,625),F(-31,625),F(-48,125),F(12,25)],
 [F(-9,25),F(12,25),F(-4,5),F(0)],
 [F(-36,125),F(48,125),F(9,25),F(4,5)],
 [F(-256,625),F(-492,625),F(-36,125),F(9,25)]]
c,s=F(99,101),F(20,101)
G=eye(4)
G[1][1]=c; G[1][3]=-s; G[3][1]=s; G[3][3]=c
U=matmul(U0,G)
assert matmul(U,transpose(U))==eye(4)
assert all(U[i][j] != 0 for i in range(4) for j in range(4))
mins=[det2(U,rs,cs) for rs in combinations(range(4),2) for cs in combinations(range(4),2)]
assert all(x != 0 for x in mins)

a=[(F(-4),F(-3)),(F(-3),F(-2)),(F(4),F(-4)),(F(0),F(2))]
b=[(F(-2),F(2)),(F(-4),F(1)),(F(-1),F(-3)),(F(-2),F(-1))]
assert len(set(a))==4 and len(set(b))==4 and all(not zzero(x) for x in a+b)

pairs=[(0,1),(0,2),(0,3)]
allset=set(range(4))
h=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]

P=[[U[i][j]*U[i][j] for j in range(4)] for i in range(4)]
D=[[sum(F(h[r][i]*h[c0][j],4)*P[i][j] for i in range(4) for j in range(4))
    for c0 in range(3)] for r in range(3)]
R=[[F(0) for _ in range(3)] for __ in range(3)]
for r,S in enumerate(pairs):
    for c0,T in enumerate(pairs):
        Tc=tuple(sorted(allset-set(T)))
        R[r][c0]=det2(U,S,T)**2+det2(U,S,Tc)**2
assert all(R[i][j] > abs(D[i][j]) for i in range(3) for j in range(3))

def pprod(v,S): return zprod([v[i] for i in S])
Aplus=[]; Aminus=[]; Bplus=[]; Bminus=[]
for S in pairs:
    Sc=tuple(sorted(allset-set(S)))
    Aplus.append(zadd(pprod(a,Sc),pprod(a,S)))
    Aminus.append(zsub(pprod(a,Sc),pprod(a,S)))
    Bplus.append(zadd(pprod(b,S),pprod(b,Sc)))
    Bminus.append(zsub(pprod(b,S),pprod(b,Sc)))
X=[[zreal(zmul(Aplus[i],Bplus[j])) for j in range(3)] for i in range(3)]
Y=[[zreal(zmul(Aminus[i],Bminus[j])) for j in range(3)] for i in range(3)]

W=[[F(0) for _ in range(4)] for __ in range(4)]
for i in range(4):
    ic=tuple(k for k in range(4) if k!=i)
    for j in range(4):
        jc=tuple(k for k in range(4) if k!=j)
        W[i][j]=zreal(zadd(zmul(pprod(a,ic),b[j]),zmul(a[i],pprod(b,jc))))
Z=[[sum(F(h[r][i]*h[c0][j],8)*Y[r][c0] for r in range(3) for c0 in range(3))
    for j in range(4)] for i in range(4)]
C=[[W[i][j]+Z[i][j] for j in range(4)] for i in range(4)]
K=[[sum(F(h[r][i]*h[c0][j],4)*C[i][j] for i in range(4) for j in range(4))
    for c0 in range(3)] for r in range(3)]

K_expected=[
 [F(191,2),F(-142),F(47,2)],
 [F(185,2),F(-143,2),F(-331,2)],
 [F(-315,2),F(135,2),F(273,2)]]
X_expected=[[F(145),F(88),F(-43)], [F(-126),F(-396),F(-294)], [F(-82),F(-214),F(-146)]]
assert K==K_expected and X==X_expected

Acoef=[[abs(K[i][j])+X[i][j]/2 for j in range(3)] for i in range(3)]
ps=list(permutations(range(3)))
m=[]; cvals=[]; qvals=[]
for p in ps:
    vals=[K[i][p[i]] for i in range(3)]
    prod=vals[0]*vals[1]*vals[2]
    mm=F(0) if prod>=0 else min(abs(v) for v in vals)
    cc=sum(Acoef[i][p[i]] for i in range(3))
    m.append(mm); cvals.append(cc); qvals.append(cc-2*mm)
avg=sum(R[i][j]*Acoef[i][j] for i in range(3) for j in range(3))
M=max(qvals)
E=avg-M
S=sum(R[i][j]*abs(K[i][j])-D[i][j]*K[i][j] for i in range(3) for j in range(3))
gap=S-E
assert cvals==[F(105),F(147),F(279),F(321),F(-8),F(-8)]
assert m==[F(143,2),F(135,2),F(185,2),F(142),F(0),F(0)]
assert qvals==[F(-38),F(12),F(94),F(37),F(-8),F(-8)]
assert avg==F(939823244619,3984765625)
assert E==F(565255275869,3984765625) and E>0
assert S==F(2119488205727,3984765625)
assert gap==F(1554232929858,3984765625) and gap>0
assert all(cvals[k] < avg for k in range(6) if m[k]==0)

verts=[]; supports=[]
for p in permutations(range(4)):
    v=zprod([zadd(a[i],b[p[i]]) for i in range(4)])
    verts.append(v); supports.append(v[0])
assert len(set(verts))==24
Mperm=max(supports)
assert Mperm==F(-48) and supports.count(Mperm)==1
Bmat=[[zsum(zscale(U[i][k]*U[j][k],b[k]) for k in range(4))
       for j in range(4)] for i in range(4)]
assert all(not zzero(Bmat[i][j]) for i in range(4) for j in range(i+1,4))
Fmat=[[(a[i] if i==j else (F(0),F(0))) for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        Fmat[i][j]=zadd(Fmat[i][j],Bmat[i][j])
det_support=zdet(Fmat)[0]
assert Mperm-det_support==gap

print("orthogonal=True")
print("all_16_entries_nonzero=True")
print("all_36_two_minors_nonzero=True")
print("strict_R_gt_absD=True")
print("simple_nonzero_spectra=True")
print("K=",K)
print("X=",X)
print("fiber_c=",cvals)
print("fiber_m=",m)
print("fiber_q=",qvals)
print("R_average_A=",avg)
print("parity_excess_E=",E)
print("orientation_slack_S=",S)
print("exact_SR_gap_S_minus_E=",gap)
print("all_zero_penalty_fibers_below_R_average=True")
print("24_distinct_complex_vertices=True")
print("unique_support_max=",Mperm)
print("determinant_support=",det_support)
print("target_support_gap=",Mperm-det_support)
print("irreducibility_cross_entries_nonzero=True")
