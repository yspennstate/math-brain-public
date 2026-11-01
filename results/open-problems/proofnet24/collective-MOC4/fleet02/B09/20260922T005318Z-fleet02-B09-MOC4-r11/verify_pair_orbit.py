from fractions import Fraction as F
from itertools import permutations

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):
    return [list(x) for x in zip(*A)]
def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def det(A):
    n=len(A); out=F(0)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        z=F(-1 if inv%2 else 1)
        for i in range(n): z*=A[i][p[i]]
        out+=z
    return out
def diag(v):
    return [[F(v[i]) if i==j else F(0) for j in range(len(v))] for i in range(len(v))]
def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def det_sum(U,a,b):
    return det(add(diag(a),mm(mm(U,diag(b)),tr(U))))
def leftrot(U,c,s):
    G=eye(4)
    G[0][0]=c; G[0][1]=-s; G[1][0]=s; G[1][1]=c
    return mm(G,U)
def permprod(a,b,p):
    z=F(1)
    for i,j in enumerate(p): z*=F(a[i]+b[j])
    return z

H=[[F(x,2) for x in row] for row in
   [[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]]
a=[-2,7,2,8]
b=[-1,5,3,1]
assert mm(H,tr(H))==eye(4)
assert len(set(a))==len(a)==4 and len(set(b))==len(b)==4
assert all(x+y != 0 for x in a for y in b)

U0=H
Us=leftrot(H,F(0),F(1))
Ur=leftrot(H,F(3,5),F(4,5))
assert mm(Ur,tr(Ur))==eye(4)

f0=det_sum(U0,a,b)
fs=det_sum(Us,a,b)
fr=det_sum(Ur,a,b)
assert (f0,fs,fr)==(F(-175),F(-391),F(1457,25))

center=(f0+fs)/2
rz=(f0-fs)/2
nx=F(-24,25); nz=F(-7,25)
rx=(fr-center-rz*nz)/nx
assert (center,rx,rz)==(F(-283),F(-387),F(108))
assert fr==center+rx*nx+rz*nz
norm2=rx*rx+rz*rz
assert norm2==F(161433)
endpoint_excess=fr-max(f0,fs)
assert endpoint_excess==F(5832,25)>0

vertices=[permprod(a,b,p) for p in permutations(range(4))]
hull_support=max(vertices)
assert hull_support==F(840)
assert norm2 < (hull_support-center)**2

print("orthogonal_Ur=True")
print("spectra_simple=True")
print("all_pair_sums_nonzero=True")
print(f"endpoint_supports={f0},{fs}")
print(f"rational_rotation_support={fr}")
print(f"endpoint_excess={endpoint_excess}")
print(f"ellipse_center={center}")
print(f"ellipse_vector=(rx={rx},ry=0,rz={rz})")
print(f"ellipse_norm_squared={norm2}")
print(f"full_hull_support={hull_support}")
print("moc4_violation=False")
