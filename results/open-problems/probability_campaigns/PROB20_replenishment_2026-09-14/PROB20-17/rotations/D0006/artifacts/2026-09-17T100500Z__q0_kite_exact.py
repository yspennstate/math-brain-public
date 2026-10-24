#!/usr/bin/env python3
from fractions import Fraction as F

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def matvec(A,v):
    return tuple(sum(A[i][k]*v[k] for k in range(len(v))) for i in range(len(A)))
def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def poly_area2(P):
    return sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P)))
def centroid(P):
    a2=poly_area2(P)
    cx=cy=F(0)
    for i in range(len(P)):
        x,y=P[i]; x2,y2=P[(i+1)%len(P)]
        c=x*y2-y*x2
        cx+=(x+x2)*c; cy+=(y+y2)*c
    return (cx/(3*a2),cy/(3*a2))

Q0=[(F(-7),F(-5)),(F(5),F(-5)),(F(11),F(1)),(F(-7),F(7))]
assert poly_area2(Q0)==F(288)
assert centroid(Q0)==(F(0),F(0))

# (x,y)=M(u,v), so (u,v)=Minv(x,y)
M=[[F(1),F(3)],[F(-1),F(1)]]
Minv=[[F(1,4),F(-3,4)],[F(1,4),F(1,4)]]
I=[[F(1),F(0)],[F(0),F(1)]]
assert matmul(M,Minv)==I and matmul(Minv,M)==I
assert det2(M)==F(4)

K=[matvec(Minv,p) for p in Q0]
assert K==[(F(2),F(-3)),(F(5),F(0)),(F(2),F(3)),(F(-7),F(0))]
assert abs(poly_area2(K))==F(72)

# Reflection v -> -v transported back to Q0.
D=[[F(1),F(0)],[F(0),F(-1)]]
T=matmul(matmul(M,D),Minv)
assert T==[[F(-1,2),F(-3,2)],[F(-1,2),F(1,2)]]
assert matmul(T,T)==I
image=[matvec(T,p) for p in Q0]
assert set(image)==set(Q0)

# Exact failure of the canonical cyclic Dirichlet scalar complete mix
# to satisfy the conditional vertical-uniform triangle criterion.
A,B,C=F(4,5),F(1,10),F(1,10)
assert A+B+C==1
U1=-7*A+5*B+2*C
U2=-7*B+5*C+2*A
U3=-7*C+5*A+2*B
assert (U1,U2,U3)==(F(-49,10),F(7,5),F(7,2))
assert U1+U2+U3==0

def h(u):
    if F(-7)<=u<=F(2):
        return (u+7)/3
    if F(2)<=u<=F(5):
        return 5-u
    raise AssertionError("outside")

H=tuple(h(u) for u in (U1,U2,U3))
assert H==(F(7,10),F(14,5),F(3,2))
assert max(H) > sum(H)-max(H)

print("Q0_area=144")
print("Q0_centroid=(0,0)")
print("kite_vertices=" + repr(K))
print("det_M=4")
print("Q0_reflection_matrix=" + repr(T))
print("reflection_involution=True")
print("dirichlet_test_U=" + repr((U1,U2,U3)))
print("dirichlet_test_widths=" + repr(H))
print("canonical_scalar_mix_width_triangle_fails=True")
print("ALL_ASSERTIONS_PASSED")
