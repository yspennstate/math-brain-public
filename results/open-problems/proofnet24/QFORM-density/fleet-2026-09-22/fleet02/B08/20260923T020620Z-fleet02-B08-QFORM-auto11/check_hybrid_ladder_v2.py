import math
from fractions import Fraction
from itertools import combinations

L=1.0
theta=1.0/8.0
beta=(3.0/16.0)*math.sqrt(3.0/5.0)*L
h=5.0/8.0
CD=6.0*math.sqrt(math.e)*(2.0*h)**(-0.5)/(3.0-4.0*h)
K3=5.0*math.sqrt(2.0*math.e)*(225.0/37.0)**0.1
c4=((224.0/225.0)*(223.0/225.0)*(222.0/225.0))/24.0
K4=5.0*math.sqrt(2.0*math.e)*c4**(-0.1)

C_k0=CD/beta
C_k1_d5=K3/(beta*theta**(3.0/5.0))
C_k1_d3=CD*15.0**(1.0/3.0)/(beta*theta**(1.0/3.0))
C_k2_d5=K4/(beta*theta**(4.0/5.0))
b2=theta*beta/15.0
C_k2_nested_d5=K3/b2
C_k2_nested_d3=CD*15.0**(1.0/3.0)/b2

print(f"beta={beta:.15f}")
print(f"beta_over_8={beta/8.0:.15f}")
print(f"beta_over_120={beta/120.0:.15f}")
print(f"CD_h_5_8={CD:.12f}")
print(f"K3={K3:.12f}")
print(f"c4={c4:.15f}")
print(f"K4={K4:.12f}")
print(f"C_k0={C_k0:.12f}")
print(f"C_k1_d5={C_k1_d5:.12f}")
print(f"C_k1_d3={C_k1_d3:.12f}")
print(f"C_k2_d5={C_k2_d5:.12f}")
print(f"C_k2_nested_d5={C_k2_nested_d5:.12f}")
print(f"C_k2_nested_d3={C_k2_nested_d3:.12f}")

assert C_k0 < 122.0
assert C_k1_d5 < 335.0
assert C_k1_d3 < 601.0
assert C_k2_d5 < 584.0
assert C_k2_nested_d5 < 11539.0
assert C_k2_nested_d3 < 36059.0

# Exact check of the anchored Schur E2 identity W_ij^(3)=z^2 e2(S^T S).
def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

B=[
 [Fraction(2), Fraction(1), Fraction(-1), Fraction(3)],
 [Fraction(2), Fraction(4), Fraction(0), Fraction(1)],
 [Fraction(1), Fraction(-2), Fraction(5), Fraction(2)],
 [Fraction(-2), Fraction(1), Fraction(3), Fraction(-1)],
]
z=B[0][0]
a=B[0][1:]
b=[B[i][0] for i in range(1,4)]
C=[[B[i][j] for j in range(1,4)] for i in range(1,4)]
S=[[C[i][j]-b[i]*a[j]/z for j in range(3)] for i in range(3)]
W=Fraction(0)
for rr in combinations(range(1,4),2):
    for cc in combinations(range(1,4),2):
        W += det3([[B[r][c] for c in (0,)+cc] for r in (0,)+rr])**2
E2=Fraction(0)
for rr in combinations(range(3),2):
    for cc in combinations(range(3),2):
        E2 += det2([[S[r][c] for c in cc] for r in rr])**2
print(f"schur_anchor_W={W}")
print(f"schur_anchor_z2E2={z*z*E2}")
assert W == z*z*E2

# Exact spectral formulas for the Hadamard hybrid witnesses; no matrix numerics needed.
delta=beta/16.0
for k in (1,2):
    p=[1.0-delta]*k+[1.0/5.0]*(3-k)
    plus=[1.0,1.0,1.0]
    minus=[2.0*x-1.0 for x in p]
    cross=sorted([1.0-x for x in p], reverse=True)
    child=sorted(p, reverse=True)
    target_large=sum(abs(x)>=1.0-1e-14 for x in plus+minus)
    child_gate=sum(abs(x)>=0.5*math.sqrt(3.0/5.0)-1e-14 for x in child)
    fbound=6.0*((4.0/5.0)**k*(3.0/5.0)**(3-k))**(-1.0/6.0)
    print(f"k={k} cross={cross} target_large={target_large} child_gate={child_gate} theoremF_bound={fbound:.12f}")
    assert target_large == 3
    assert child_gate == k

print("QFORM_B08_HYBRID_VOLUME_TAIL_LADDER_V2_CHECK_PASS")
