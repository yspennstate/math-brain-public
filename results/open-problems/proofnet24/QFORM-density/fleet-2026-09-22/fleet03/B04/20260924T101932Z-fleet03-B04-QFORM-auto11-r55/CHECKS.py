from fractions import Fraction
from itertools import combinations
import math, json


def dot(x,y):
    return sum(Fraction(a)*Fraction(b) for a,b in zip(x,y))


def norm2(x):
    return dot(x,x)


def project_off(row, base):
    den=norm2(base)
    q=dot(row,base)/den
    return tuple(Fraction(row[j])-q*Fraction(base[j]) for j in range(len(base)))


def area2(x,y):
    return norm2(x)*norm2(y)-dot(x,y)**2


def det(A):
    A=[[Fraction(x) for x in row] for row in A]
    n=len(A)
    ans=Fraction(1)
    for i in range(n):
        p=next((k for k in range(i,n) if A[k][i]),None)
        if p is None:
            return Fraction(0)
        if p!=i:
            A[i],A[p]=A[p],A[i]
            ans=-ans
        piv=A[i][i]
        ans*=piv
        for j in range(i+1,n):
            A[i][j]/=piv
        for k in range(i+1,n):
            fac=A[k][i]
            for j in range(i+1,n):
                A[k][j]-=fac*A[i][j]
    return ans


# Stress cross block. The first row is the physical hub h.
m=(2,2,2)
B=[(12,-4,4),(8,8,2),(10,6,2)]
C=[project_off(b,m) for b in B]
assert C == [
    (Fraction(8),Fraction(-8),Fraction(0)),
    (Fraction(2),Fraction(2),Fraction(-4)),
    (Fraction(4),Fraction(0),Fraction(-4)),
]
pairs={(i,j):area2(C[i],C[j]) for i,j in combinations(range(3),2)}
assert pairs == {(0,1):3072,(0,2):3072,(1,2):192}
Z=sum(pairs.values())
assert Z==6336
K=[sum(v for (i,j),v in pairs.items() if i==q or j==q) for q in range(3)]
assert K==[6144,3264,3264]
assert Fraction(K[0],Z)==Fraction(32,33)
s2=norm2(m)
assert s2==12

# After promoting the heavy row i=0 to a second physical hub.
c1n=norm2(C[0])
assert c1n==128
Z1=K[0]/c1n
assert Z1==48

def dist2_from_line(x,v):
    return norm2(x)-dot(x,v)**2/norm2(v)

d2=[dist2_from_line(C[j],C[0]) for j in (1,2)]
assert d2==[24,24]
assert sum(d2)==Z1

Cdiff=3*2**(7/6)*math.exp(1/3)
generic_bound=Cdiff*float(s2*Z)**(-1/6)
Cheavy=3*2**(5/6)
heavy_bound=Cheavy*float(s2*K[0])**(-1/6)
assert Cdiff < 9.4
assert generic_bound < 1.445
assert heavy_bound < 0.826

# Rigorous target spectrum certificate.  The unscaled cross matrix M0 has
# Gram G. G-(5/8)I is positive definite by Sylvester, hence
# sigma_min(2 M0)>sqrt(5/2).
M0=[(1,1,1),(6,-2,2),(4,4,1),(5,3,1)]
G=[[sum(Fraction(row[i])*Fraction(row[j]) for row in M0)
    for j in range(3)] for i in range(3)]
assert G==[[78,20,22],[20,30,4],[22,4,7]]
lam=Fraction(5,8)
H=[[G[i][j]-(lam if i==j else 0) for j in range(3)] for i in range(3)]
leading=[det([row[:k] for row in H[:k]]) for k in range(1,4)]
assert leading==[Fraction(619,8),Fraction(119865,64),Fraction(2139,512)]
assert all(x>0 for x in leading)

# Same-bank perturbation used to make the 7x7 example fully dense.
delta=Fraction(1,2**20)
left_frob2=15*Fraction(1,10000)+delta*delta
right_frob2=9*Fraction(1,10000)
assert left_frob2 < Fraction(1,625)
assert right_frob2 < Fraction(1,625)
spectral_floor=math.sqrt(5/2)-1/25
assert spectral_floor>1.54

# All entries of the full example are nonzero.
left=[[Fraction(1,100) for _ in range(4)] for __ in range(4)]
left[0][0]=delta
right=[[Fraction(-1,100) for _ in range(3)] for __ in range(3)]
cross=[m]+B
A=[[Fraction(0) for _ in range(7)] for __ in range(7)]
for i in range(4):
    for j in range(4):
        A[i][j]=left[i][j]
for i in range(3):
    for j in range(3):
        A[4+i][4+j]=right[i][j]
for i in range(4):
    for j in range(3):
        A[i][4+j]=Fraction(cross[i][j])
        A[4+j][i]=Fraction(cross[i][j])
assert all(A[i][j]!=0 for i in range(7) for j in range(7))

partner_constant=4*75**(1/8)
assert abs(partner_constant-6.861872579851902)<1e-12

result={
  "marker":"QFORM_B04_R55_MARGINALFREE_PROJECTED_E2_CHECK_PASS",
  "squared_hub_coupling":int(s2),
  "projected_E2":int(Z),
  "currency_s2Z":int(s2*Z),
  "E2_row_marginals":[str(Fraction(x,Z)) for x in K],
  "heavy_row_marginal":str(Fraction(K[0],Z)),
  "promoted_E1":int(Z1),
  "promoted_E1_marginals":["1/2","1/2"],
  "diffuse_constant":Cdiff,
  "generic_new_theorem_bound":generic_bound,
  "actual_heavy_branch_bound":heavy_bound,
  "gram_shift_leading_minors":[str(x) for x in leading],
  "rigorous_spectral_modulus_floor":spectral_floor,
  "all_matrix_entries_nonzero":True,
  "partner_pair_E4_coefficient":partner_constant
}
print(json.dumps(result,indent=2,sort_keys=True))
