from sympy import Matrix, Rational, I, conjugate, eye, factor, simplify, symbols

ROTATIONS = [
    (0, 1, Rational(3,5), Rational(4,5)),
    (1, 2, Rational(5,13), Rational(12,13)),
    (2, 3, Rational(7,25), Rational(24,25)),
    (3, 4, Rational(20,29), Rational(21,29)),
    (4, 5, Rational(12,13), Rational(5,13)),
    (0, 5, Rational(8,17), Rational(15,17)),
    (0, 3, Rational(9,41), Rational(40,41)),
    (1, 4, Rational(11,61), Rational(60,61)),
]

def givens6(a, b, c, s):
    G = eye(6)
    G[a,a] = c
    G[a,b] = -s
    G[b,a] = s
    G[b,b] = c
    return G

O = eye(6)
for a,b,c,s in ROTATIONS:
    O = O * givens6(a,b,c,s)

assert O.T * O == eye(6)
assert simplify(O.det() - 1) == 0

M = Matrix.zeros(3)
N = Matrix.zeros(3)
for alpha in range(3):
    for beta in range(3):
        a = O[2*alpha, 2*beta]
        b = O[2*alpha, 2*beta+1]
        c = O[2*alpha+1, 2*beta]
        d = O[2*alpha+1, 2*beta+1]
        M[alpha,beta] = simplify((a+d + I*(c-b))/2)
        N[alpha,beta] = simplify((a-d + I*(c+b))/2)

assert simplify(M*M.conjugate().T + N*N.conjugate().T - eye(3)) == Matrix.zeros(3)
assert simplify(M*N.T + N*M.T) == Matrix.zeros(3)
assert N.rank() == 2
assert simplify(N.det()) == 0

H = simplify(N*N.conjugate().T)
t = symbols("t")
charpoly = factor(H.charpoly(t).as_expr())
row_sums = [simplify(sum(N[i,j]*conjugate(N[i,j]) for j in range(3))) for i in range(3)]
col_sums = [simplify(sum(N[i,j]*conjugate(N[i,j]) for i in range(3))) for j in range(3)]
lam = simplify(sum(row_sums)/2)

cofactor_checks = []
for i in range(3):
    for j in range(3):
        co = simplify(N.minor_submatrix(i,j).det())
        lhs = simplify(co*conjugate(co))
        rhs = simplify((lam-row_sums[i])*(lam-col_sums[j]))
        cofactor_checks.append(simplify(lhs-rhs) == 0)
assert all(cofactor_checks)

# Strict-cut witness for the mass/two-rook relaxation.
# S = 1/2 diag(1,1,0) + 1/2 diag(1,0,1) = diag(1,1/2,1/2).
S = Matrix.diag(Rational(1), Rational(1,2), Rational(1,2))
V1 = Matrix.diag(1,1,0)
V2 = Matrix.diag(1,0,1)
assert S == (V1+V2)/2
assert sum(S) == 2
assert all(sum(S[i,j] for j in range(3)) <= 1 for i in range(3))
assert all(sum(S[i,j] for i in range(3)) <= 1 for j in range(3))
lamS = Rational(1)
r1 = sum(S[0,j] for j in range(3))
c1 = sum(S[i,0] for i in range(3))
deficit = simplify((lamS-r1)*(lamS-c1))
lower = simplify(S[1,1]*S[2,2])  # cross-product is zero, so squared-modulus lower bound
assert deficit == 0
assert lower == Rational(1,4)
assert lower > deficit

print("MOC4-SPIN6-COFACTOR-DEFICIT-v1 exact verification")
print("O^T O = I:", O.T*O == eye(6))
print("det(O) =", factor(O.det()))
print("rank(N) =", N.rank())
print("det(N) =", simplify(N.det()))
print("charpoly(N N*) =", charpoly)
print("lambda =", lam)
print("row sums =", row_sums)
print("column sums =", col_sums)
print("all 9 cofactor-deficit identities exact:", all(cofactor_checks))
print("strict-cut witness S =", S.tolist())
print("S decomposition = 1/2 diag(1,1,0) + 1/2 diag(1,0,1):", S == (V1+V2)/2)
print("witness total mass =", sum(S))
print("witness cofactor lower bound =", lower)
print("witness deficit product =", deficit)
print("witness excluded by cofactor-deficit identity:", lower > deficit)
