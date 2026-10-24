from itertools import combinations
import sympy as sp

R = sp.Matrix([
    [8,0,0],
    [0,1,0],
    [0,0,1],
    [1,0,0],
    [0,1,0],
    [0,0,1],
])
L = sp.Matrix([
    [ 2,-4,-4],
    [-4, 2,-4],
    [-4,-4, 2],
])
A = R*L*R.T
expected_A = sp.Matrix([
    [128,-32,-32,16,-32,-32],
    [-32,2,-4,-4,2,-4],
    [-32,-4,2,-4,-4,2],
    [16,-4,-4,2,-4,-4],
    [-32,2,-4,-4,2,-4],
    [-32,-4,2,-4,-4,2],
])
assert A == expected_A
assert all(A[i,j] != 0 for i in range(6) for j in range(6))
assert L.det() == -216
assert sorted(L.eigenvals().keys()) == [-6,6]
assert A.rank() == 3
assert A.eigenvals() == {sp.Integer(156):1, sp.Integer(12):1, sp.Integer(-30):1, sp.Integer(0):3}

G = R.T*R
assert G == sp.diag(65,2,2)
lev = [(R.row(i)*G.inv()*R.row(i).T)[0] for i in range(6)]
assert lev == [sp.Rational(64,65), sp.Rational(1,2), sp.Rational(1,2), sp.Rational(1,65), sp.Rational(1,2), sp.Rational(1,2)]
assert lev[0] > sp.Rational(1,2)

bases=[]
for S in combinations(range(6),3):
    d=R[list(S),:].det()
    if d != 0:
        bases.append((S,d,d*d))
assert len(bases) == 8
assert sorted([z for _,_,z in bases]) == [1,1,1,1,64,64,64,64]
counts=[0]*6
for S,_,_ in bases:
    for i in S:
        counts[i]+=1
assert counts == [4,4,4,4,4,4]
# Uniform on the eight bases: H=log 8 and average log squared determinant=log 8.
# Thus G_R=64. All six marginals are exactly 1/2.
G_currency = sp.Integer(64)
B_two_thirds = sp.Integer(2)  # [prod_i (1/2)^(-1/4)]^(2/3)
bound = sp.Rational(3)*B_two_thirds / (abs(L.det())*G_currency)**sp.Rational(1,3)
assert sp.simplify(bound - sp.Rational(1,4)) == 0

# Partner r22 arithmetic.
J=sp.Integer(158720)
partner_bound = 3*2**(sp.Rational(4,3))*J**(-sp.Rational(1,6))

print("QFORM_B04_R36_REBALANCED_BASIS_CHECK_PASS")
print("A=", A.tolist())
print("spectrum=", A.eigenvals())
print("canonical_leverages=", lev)
print("basis_squared_dets=", sorted([z for _,_,z in bases]))
print("uniform_basis_counts=", counts)
print("G_currency=", G_currency)
print("new_bound_exact=", bound)
print("partner_bound_decimal=", sp.N(partner_bound,18))
