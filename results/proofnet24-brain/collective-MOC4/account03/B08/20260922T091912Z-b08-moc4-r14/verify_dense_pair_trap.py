#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations, combinations
from math import lcm

def z(re=0, im=0): return (Fraction(re), Fraction(im))
def zadd(a,b): return (a[0]+b[0], a[1]+b[1])
def zsub(a,b): return (a[0]-b[0], a[1]-b[1])
def zmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def zscale(q,a): q=Fraction(q); return (q*a[0], q*a[1])

def mat_id(n):
    return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def mat_add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), Fraction(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def mat_T(A):
    return [list(row) for row in zip(*A)]
def mat_inv(A):
    n=len(A)
    M=[list(map(Fraction,row))+[Fraction(int(i==j)) for j in range(n)]
       for i,row in enumerate(A)]
    for col in range(n):
        piv=next(i for i in range(col,n) if M[i][col])
        M[col],M[piv]=M[piv],M[col]
        q=M[col][col]
        M[col]=[x/q for x in M[col]]
        for i in range(n):
            if i==col: continue
            q=M[i][col]
            if q:
                M[i]=[M[i][j]-q*M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]

def gmat_mul(A,B):
    out=[[z() for _ in range(len(B[0]))] for __ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            s=z()
            for k in range(len(B)):
                s=zadd(s,zmul(A[i][k],B[k][j]))
            out[i][j]=s
    return out
def gmat_add(A,B):
    return [[zadd(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def gmat_T(A):
    return [list(row) for row in zip(*A)]
def real_to_g(A):
    return [[z(A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def diag_g(vals):
    n=len(vals); M=[[z() for _ in range(n)] for __ in range(n)]
    for i,v in enumerate(vals): M[i][i]=v
    return M
def gdet(A):
    n=len(A); total=z()
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=z(1)
        for i in range(n): term=zmul(term,A[i][p[i]])
        total=zsub(total,term) if inv%2 else zadd(total,term)
    return total

def solve3(M,b):
    A=[list(row)+[b[i]] for i,row in enumerate(M)]
    for col in range(3):
        piv=next((i for i in range(col,3) if A[i][col]),None)
        if piv is None: return None
        A[col],A[piv]=A[piv],A[col]
        q=A[col][col]
        A[col]=[x/q for x in A[col]]
        for i in range(3):
            if i==col: continue
            q=A[i][col]
            if q:
                A[i]=[A[i][j]-q*A[col][j] for j in range(4)]
    return [A[i][3] for i in range(3)]

a=[z(23,19), z(1,17), z(25,-26), z(-35,19)]
b=[z(-21,13), z(-1,23), z(26,-27), z(32,-21)]
p=(3,2,1,0)          # 4321
q=(2,3,0,1)          # 3412
N=1000
t=Fraction(1,10**10)
normal=(216982*N-17957, 365451*N-30244)

# Dense rational orthogonal Cayley perturbation U=Q(t)P_p.
S=[[Fraction(x) for x in row] for row in
   [[0,1,2,3],[-1,0,4,5],[-2,-4,0,6],[-3,-5,-6,0]]]
Id=mat_id(4)
tS=[[t*x for x in row] for row in S]
Q=mat_mul(mat_sub(Id,tS), mat_inv(mat_add(Id,tS)))
P=[[Fraction(1 if j==p[i] else 0) for j in range(4)] for i in range(4)]
U=mat_mul(Q,P)
assert mat_mul(U,mat_T(U))==Id
assert all(U[i][j] != 0 for i in range(4) for j in range(4))
for rs in combinations(range(4),2):
    for cs in combinations(range(4),2):
        minor=U[rs[0]][cs[0]]*U[rs[1]][cs[1]]-U[rs[0]][cs[1]]*U[rs[1]][cs[0]]
        assert minor != 0

Ug=real_to_g(U)
C=gmat_mul(gmat_mul(Ug,diag_g(b)),gmat_T(Ug))
D=gdet(gmat_add(diag_g(a),C))

def L(w):
    return normal[0]*w[0] + normal[1]*w[1]
def vertex(perm):
    out=z(1)
    for i in range(4):
        out=zmul(out,zadd(a[i],b[perm[i]]))
    return out

perms=list(permutations(range(4)))
verts=[vertex(r) for r in perms]
supports=[L(v) for v in verts]
assert len(set(supports))==24
order=sorted(range(24),key=lambda k:supports[k],reverse=True)
assert perms[order[0]]==q
assert perms[order[1]]==p
M=supports[order[0]]
m=min(supports)
gap=M-L(D)
loss=L(vertex(p))-L(D)
assert gap > 6
assert loss > 0

# Exact 3-vertex Caratheodory certificate.
cert=None
for inds in combinations(range(24),3):
    pts=[verts[k] for k in inds]
    A3=[[Fraction(1)]*3,
        [pts[j][0] for j in range(3)],
        [pts[j][1] for j in range(3)]]
    lam=solve3(A3,[Fraction(1),D[0],D[1]])
    if lam is not None and all(x>=0 for x in lam):
        cert=(inds,lam); break
assert cert is not None
assert sum(cert[1],Fraction(0))==1
assert (sum(cert[1][j]*verts[cert[0][j]][0] for j in range(3)),
        sum(cert[1][j]*verts[cert[0][j]][1] for j in range(3))) == D
assert [''.join(str(x+1) for x in perms[k]) for k in cert[0]] == ['1234','1342','4321']

# Full embedded SU(2) row-pair envelope.  Conjugating the pair of diagonal
# a-values makes the determinant affine in the Bloch vector n in S^2.
def det_bloch(r,s,nx,ny,nz):
    Ap=diag_g(a)
    avg=zscale(Fraction(1,2),zadd(a[r],a[s]))
    d=zscale(Fraction(1,2),zsub(a[r],a[s]))
    Ap[r][r]=zadd(avg,zscale(nz,d))
    Ap[s][s]=zsub(avg,zscale(nz,d))
    Ap[r][s]=zmul(d,z(nx,-ny))
    Ap[s][r]=zmul(d,z(nx, ny))
    return gdet(gmat_add(Ap,C))

pair_rows=[]
for r,s in combinations(range(4),2):
    hx=L(det_bloch(r,s, 1,0,0)); hmx=L(det_bloch(r,s,-1,0,0))
    hy=L(det_bloch(r,s, 0,1,0)); hmy=L(det_bloch(r,s, 0,-1,0))
    hz=L(det_bloch(r,s, 0,0,1)); hmz=L(det_bloch(r,s,0,0,-1))
    cx=(hx-hmx)/2; cy=(hy-hmy)/2; cz=(hz-hmz)/2
    assert hz==L(D)
    assert cz>0
    # exact upper bound:
    # sqrt(cx^2+cy^2+cz^2)-cz <= (cx^2+cy^2)/(2cz)
    ub=(cx*cx+cy*cy)/(2*cz)
    assert ub < Fraction(1,400)
    pair_rows.append(((r+1,s+1),ub,2*cz))

# Exact second-order Cayley/determinant series, all with Fraction arithmetic.
# Q(t)=I-2tS+2t^2 S^2+O(t^3).
def padd(p,q):
    return [zadd(p[i],q[i]) for i in range(3)]
def pmul(p,q):
    out=[z(),z(),z()]
    for i in range(3):
        for j in range(3-i):
            out[i+j]=zadd(out[i+j],zmul(p[i],q[j]))
    return out

S2=mat_mul(S,S)
Qpoly=[[[z(int(i==j)), z(-2*S[i][j]), z(2*S2[i][j])]
        for j in range(4)] for i in range(4)]
bp=[b[p[i]] for i in range(4)]
Cpoly=[[[z(),z(),z()] for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        out=[z(),z(),z()]
        for k in range(4):
            out=padd(out,pmul(Qpoly[i][k],
                              [zmul(bp[k],cc) for cc in Qpoly[j][k]]))
        Cpoly[i][j]=out
Mpoly=[[list(Cpoly[i][j]) for j in range(4)] for i in range(4)]
for i in range(4):
    Mpoly[i][i][0]=zadd(Mpoly[i][i][0],a[i])
detpoly=[z(),z(),z()]
for perm in permutations(range(4)):
    inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    term=[z(1),z(),z()]
    for i in range(4):
        term=pmul(term,Mpoly[i][perm[i]])
    if inv%2:
        term=[zscale(-1,c) for c in term]
    detpoly=padd(detpoly,term)
assert detpoly[0]==vertex(p)
assert detpoly[1]==z(0,0)
assert detpoly[2]==z(-99534232,-784537096)

# The second-order determinant vector points strictly inside the target
# triangle cone generated by 1234 and 1342 at 4321.
i1234=perms.index((0,1,2,3))
i1342=perms.index((0,2,3,1))
vp0=vertex(p)
d1=zsub(verts[i1234],vp0)
d2=zsub(verts[i1342],vp0)
det2cone=d1[0]*d2[1]-d2[0]*d1[1]
alpha=(detpoly[2][0]*d2[1]-d2[0]*detpoly[2][1])/det2cone
beta=(d1[0]*detpoly[2][1]-detpoly[2][0]*d1[1])/det2cone
assert alpha==Fraction(497504682718,1776074271)
assert beta==Fraction(1310894256442,5328222813)
assert alpha>0 and beta>0

den=lcm(*(x.denominator for x in cert[1]))
nums=[x.numerator*(den//x.denominator) for x in cert[1]]
print("MOC4-DENSE-PAIR-TRAP-v1 exact verification PASS")
print("direction =",normal)
print("top_two = 3412,4321 ; top gap =",supports[order[0]]-supports[order[1]])
print("candidate_common_gap =",gap,"~",float(gap))
print("candidate_loss_below_4321 =",loss,"~",float(loss))
print("support_width =",M-m)
print("normalized_gap ~",float(gap/(M-m)))
print("all_16_entries_nonzero = True")
print("all_36_two_by_two_minors_nonzero = True")
print("triangle_certificate = 1234,1342,4321")
print("triangle_common_denominator =",den)
print("triangle_numerators =",nums)
print("pair_SU2_max_improvement_upper_bounds:")
for pair,ub,endpoint in pair_rows:
    print(" ",pair,"<=",ub,"~",float(ub)," endpoint_swap_loss=",endpoint)
print("max_pair_upper <",Fraction(1,400))
