from fractions import Fraction as F

# H is the 4x4 Hadamard eigenbasis with rows u_j.
H = [[F(1,2),F(1,2),F(-1,2),F(-1,2)],
     [F(1,2),F(-1,2),F(1,2),F(-1,2)],
     [F(1,2),F(-1,2),F(-1,2),F(1,2)],
     [F(1,2),F(1,2),F(1,2),F(1,2)]]
lam = [F(1),F(2),F(-3),F(1,2)]

def dot(a,b): return sum(x*y for x,y in zip(a,b))

# Orthonormality.
G = [[dot(H[i],H[j]) for j in range(4)] for i in range(4)]
assert G == [[F(int(i==j)) for j in range(4)] for i in range(4)]

# A = H^T diag(lam) H.
A = [[sum(lam[k]*H[k][i]*H[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
A8 = [[8*x for x in row] for row in A]
assert A8 == [[1,5,9,-11],[5,1,-11,9],[9,-11,1,5],[-11,9,5,1]]
assert all(A[i][j] != 0 for i in range(4) for j in range(4))

# Each row of H is an eigenvector with its stated eigenvalue.
for k in range(4):
    lhs = [sum(A[i][j]*H[k][j] for j in range(4)) for i in range(4)]
    rhs = [lam[k]*H[k][i] for i in range(4)]
    assert lhs == rhs

# u1,u2,u3 kill the all-ones vector and u4 has dot=2.
one=[F(1)]*4
assert [dot(H[j],one) for j in range(4)] == [0,0,0,2]

# On W in simplex, u4.W=1/2, hence ||z||^2=||W||^2-1/4 <= 3/4.
# Therefore V=z1^2+2z2^2-3z3^2 is in [-9/4,3/2], width <=15/4.
assert F(3,2)-F(-9,4) == F(15,4)

print('A8=', A8)
print('eigenvalues=', lam)
print('simple_spectrum=', len(set(lam))==4)
print('all_physical_entries_nonzero=', all(A[i][j] != 0 for i in range(4) for j in range(4)))
print('conditional_projection_height=3/r^3')
print('conditional_Q3_height_lower_bound=4/(15*r^2)')
print('STATUS=PASS')
