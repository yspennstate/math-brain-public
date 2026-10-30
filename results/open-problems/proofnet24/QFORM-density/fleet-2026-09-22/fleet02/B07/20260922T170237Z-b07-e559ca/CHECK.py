from fractions import Fraction
from itertools import combinations
import math


def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]


def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


n=8
seq=[3,-2,5,1,-4,2,6,-3,4,7,-5,8,-1,9,-6,10,2,-7,3,5,-8,4,11,-9,6,1,-2,7,12,-4,5,8,-3,9,-1,2]
A=[[Fraction(0) for _ in range(n)] for __ in range(n)]
k=0
for i in range(n):
    for j in range(i,n):
        A[i][j]=A[j][i]=Fraction(seq[k % len(seq)])
        k+=1

C=[0,1]
L=[2,3,4]
R=[5,6,7]
i=0
a=A[i][i]
u=[A[s][i] for s in L]
v=[A[i][t] for t in R]
B=[[A[s][t] for t in R] for s in L]
Lp=list(combinations(range(len(L)),2))
Rp=list(combinations(range(len(R)),2))

# O1 exact compound/Schur-numerator identity.
o1_direct=[]
o1_formula=[]
for Sidx in Lp:
    dr=[]; fr=[]
    r1,r2=Sidx
    s1,s2=L[r1],L[r2]
    for Tidx in Rp:
        c1,c2=Tidx
        t1,t2=R[c1],R[c2]
        M=[[A[i][i],A[i][t1],A[i][t2]],
           [A[s1][i],A[s1][t1],A[s1][t2]],
           [A[s2][i],A[s2][t1],A[s2][t2]]]
        h=det3(M)
        b11,b12=A[s1][t1],A[s1][t2]
        b21,b22=A[s2][t1],A[s2][t2]
        uu1,uu2=A[s1][i],A[s2][i]
        vv1,vv2=A[i][t1],A[i][t2]
        f=a*(b11*b22-b12*b21) - (
            vv1*(uu1*b22-uu2*b12)
            - vv2*(uu1*b21-uu2*b11)
        )
        dr.append(h); fr.append(f)
    o1_direct.append(dr); o1_formula.append(fr)
assert o1_direct == o1_formula
o1_norm=sum(x*x for row in o1_direct for x in row)

# a=0 exact hyperbolic-packet Hilbert-Schmidt identity.
U=dot(u,u); V=dot(v,v)
BF2=sum(x*x for row in B for x in row)
utB=[sum(u[r]*B[r][c] for r in range(len(L))) for c in range(len(R))]
Bv=[sum(B[r][c]*v[c] for c in range(len(R))) for r in range(len(L))]
utBv=dot(utB,v)
projection_formula=U*V*BF2 - V*dot(utB,utB) - U*dot(Bv,Bv) + utBv**2

T=[]
for r1,r2 in Lp:
    row=[]
    for c1,c2 in Rp:
        x=(v[c1]*(u[r1]*B[r2][c2]-u[r2]*B[r1][c2])
           -v[c2]*(u[r1]*B[r2][c1]-u[r2]*B[r1][c1]))
        row.append(x)
    T.append(row)
zero_pivot_norm=sum(x*x for row in T for x in row)
assert zero_pivot_norm == projection_formula

# O2 exact adjugate identity.
I=[0,1]
P=[[A[r][c] for c in I] for r in I]
detP=det2(P)
adjP=[[P[1][1],-P[0][1]],[-P[1][0],P[0][0]]]
Umat=[[A[j][c] for c in I] for j in L]
Vmat=[[A[r][kk] for kk in R] for r in I]
o2_direct=[]
o2_formula=[]
for jj,j in enumerate(L):
    dr=[]; fr=[]
    for kk,kidx in enumerate(R):
        M=[[A[I[0]][I[0]],A[I[0]][I[1]],A[I[0]][kidx]],
           [A[I[1]][I[0]],A[I[1]][I[1]],A[I[1]][kidx]],
           [A[j][I[0]],A[j][I[1]],A[j][kidx]]]
        g=det3(M)
        uv=sum(Umat[jj][r]*adjP[r][s]*Vmat[s][kk]
               for r in range(2) for s in range(2))
        f=detP*B[jj][kk]-uv
        dr.append(g); fr.append(f)
    o2_direct.append(dr); o2_formula.append(fr)
assert o2_direct == o2_formula
o2_norm=sum(x*x for row in o2_direct for x in row)

# Exact rank-one pair-pivot singular formula.
P1=[[Fraction(2),Fraction(2)],[Fraction(2),Fraction(2)]]
adj1=[[Fraction(2),Fraction(-2)],[Fraction(-2),Fraction(2)]]
U1=[[Fraction(1),Fraction(3)],[Fraction(-2),Fraction(4)],[Fraction(5),Fraction(-1)]]
V1=[[Fraction(2),Fraction(-3),Fraction(1)],[Fraction(4),Fraction(5),Fraction(-2)]]
G1=[[-sum(U1[j][r]*adj1[r][s]*V1[s][k]
          for r in range(2) for s in range(2))
     for k in range(3)] for j in range(3)]
rank1_lhs=sum(x*x for row in G1 for x in row)
du=sum((row[0]-row[1])**2 for row in U1)
dv=sum((V1[0][k]-V1[1][k])**2 for k in range(3))
rank1_rhs=Fraction(16,4)*du*dv
assert rank1_lhs == rank1_rhs

# Ridge-calibration algebra at theta=3/2.
ks=[Fraction(3,4),Fraction(1,2),Fraction(1,4)]
assert sum(ks) == Fraction(3,2)
e2k=sum(ks[i]*ks[j] for i in range(3) for j in range(i+1,3))
ys=[x/(1-x) for x in ks]
e2y=sum(ys[i]*ys[j] for i in range(3) for j in range(i+1,3))
D=Fraction(1)
for y in ys:
    D *= (1+y)
assert e2k >= Fraction(1,2)
assert e2y >= e2k
assert D >= e2y
assert sum(1 for x in ks if x>Fraction(1,2)) <= 2

# Constant inherited from QFORM-PIVOT-RIDGE-BILINEAR-v1 at q=1, theta=3/2, r=5/3.
r=5/3
p=r/(r-1)
theta=1.5
beta=theta/2
Pr=1+(1-r/2)**(-1/r)
Cr=r**(1/(2*r))/p**(1/(2*p))
Lq=math.pi*math.e*math.sqrt(2)
Cstar=Pr*(2*math.pi)**(-0.5)*Cr**(r/2)*math.sqrt(
    2*(Lq/2)*beta*r/(beta*r-1)
)
Cpacket=Cstar*2**(1/24)
assert Cpacket < 12.232

# Target-valid near-zero scalar-pivot stress.
eps=Fraction(1,1000)
stress_minor=det3([[eps,1,0],[1,0,0],[0,0,1]])
assert stress_minor == -1
root_plus=(float(eps)+math.sqrt(float(eps)**2+8))/2
root_minus=(float(eps)-math.sqrt(float(eps)**2+8))/2
assert abs(root_plus)>1 and abs(root_minus)>1

print("O1_identity=PASS")
print("O1_fixture_norm2=", o1_norm)
print("zero_pivot_HS_identity=PASS")
print("zero_pivot_packet=", zero_pivot_norm)
print("O2_adjugate_identity=PASS")
print("O2_fixture_norm2=", o2_norm)
print("O2_rank1_singular_formula=PASS")
print("O2_rank1_packet=", rank1_lhs)
print("ridge_theta=", sum(ks))
print("ridge_e2k=", e2k)
print("ridge_e2y=", e2y)
print("ridge_D=", D)
print("pivot_ridge_packet_constant=", format(Cpacket, ".12f"))
print("near_zero_stress_minor=", stress_minor)
print("near_zero_stress_large_eigs=", format(root_plus, ".12f"), format(root_minus, ".12f"), "and +/-1")
print("STATUS=QFORM_MIXED_OVERLAP_SINGULAR_SPLIT_CHECK_PASS")
