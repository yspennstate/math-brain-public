#!/usr/bin/env python3
from collections import Counter
from itertools import product
import sympy as sp

# Exact self-checks for KRESSNER-VANDEREYCKEN-2026-LYAP6 run 3.
# This checks only finite/symbolic identities. The theorem proofs are in the report.

def tr(M):
    return sp.trace(M)

# ---------- B25: flip-moment word expansion ----------
terms = [
    (('t','a'), ()),      # A^T A \otimes I
    (('t',), ('a',)),     # A^T \otimes A
    (('a',), ('t',)),     # A \otimes A^T
    ((), ('t','a')),      # I \otimes A^T A
]

def canonical_trace(word):
    word = tuple(word)
    if not word:
        return ()
    rots = [word[i:] + word[:i] for i in range(len(word))]
    trans = tuple('t' if x == 'a' else 'a' for x in reversed(word))
    rots += [trans[i:] + trans[:i] for i in range(len(trans))]
    return min(rots)

def flip_counter(m):
    out = Counter()
    for idxs in product(range(4), repeat=m):
        B = ()
        C = ()
        for i in idxs:
            B += terms[i][0]
            C += terms[i][1]
        out[canonical_trace(B + C)] += 1
    return out

expected1 = Counter({('a','t'): 4})
expected2 = Counter({
    ('a','t','a','t'): 8,
    ('a','a','t','t'): 8,
})
expected3 = Counter({
    ('a','t','a','t','a','t'): 16,
    ('a','a','t','t','a','t'): 18,
    ('a','a','t','a','t','t'): 18,
    ('a','a','a','t','t','t'): 12,
})
assert flip_counter(1) == expected1
assert flip_counter(2) == expected2
assert flip_counter(3) == expected3

# Verify that the four third-moment trace words are norm squares.
def normword(w):
    wt = tuple('t' if x == 'a' else 'a' for x in reversed(w))
    return canonical_trace(wt + tuple(w))

third_norm_reps = {
    ('a','t','a','t','a','t'): ('t','a','t'),  # ||A^T A A^T||_F^2
    ('a','a','t','t','a','t'): ('t','a','a'),  # ||A^T A^2||_F^2
    ('a','a','t','a','t','t'): ('a','a','t'),  # ||A^2 A^T||_F^2
    ('a','a','a','t','t','t'): ('a','a','a'),  # ||A^3||_F^2
}
for k,w in third_norm_reps.items():
    assert normword(w) == k

# Source A7: exact positive first three moment differences despite the order-7 counterexample.
A7 = sp.Matrix([
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [6,-5,-13,0,0,0,0],
    [-14,-18,0,0,0,0,0],
    [12,-12,11,0,0,0,0],
    [0,0,0,-6,0,-14,0],
    [0,0,0,6,-18,0,0],
])

def trace_word(A, w):
    M = sp.eye(A.rows)
    for x in w:
        M = M * (A if x == 'a' else A.T)
    return sp.trace(M)

def flip_moment_value(A, m):
    return sum(c * trace_word(A, w) for w,c in flip_counter(m).items())

source_moments = [flip_moment_value(A7,m) for m in (1,2,3)]
assert source_moments == [7004, 7626232, 8242862096]

# ---------- B27: 2x2 Pauli/reflection identities used by the rank<=4 theorem ----------
b11,b12,b21,b22 = sp.symbols('b11 b12 b21 b22', real=True)
B = sp.Matrix([[b11,b12],[b21,b22]])
I2 = sp.eye(2)
J = sp.Matrix([[0,1],[-1,0]])
K = sp.Matrix([[1,0],[0,-1]])
L = sp.Matrix([[0,1],[1,0]])

diag_identity = sp.expand(
    tr(B*K*B*K) + tr(B*J*B*J)
    - ((b11-b22)**2 + (b12-b21)**2)
)
assert diag_identity == 0

# Pauli coordinates for arbitrary X,Y.
x0,x1,x2,x3,y0,y1,y2,y3 = sp.symbols(
    'x0 x1 x2 x3 y0 y1 y2 y3', real=True)
X = x0*I2 + x1*J + x2*K + x3*L
Y = y0*I2 + y1*J + y2*K + y3*L
cp,spn,cq,sqn = sp.symbols('cp sp cq sq', real=True)
P = cp*K + spn*L
Q = cq*K + sqn*L

direct_ref = sp.expand(tr(X*Q*Y*P))
pred_ref = sp.expand(2*(
    cp*cq*(x0*y0+x1*y1+x2*y2-x3*y3)
    + cp*sqn*(-x0*y1+x1*y0+x2*y3+x3*y2)
    + spn*cq*(x0*y1-x1*y0+x2*y3+x3*y2)
    + spn*sqn*(x0*y0+x1*y1-x2*y2+x3*y3)
))
assert sp.expand(direct_ref - pred_ref) == 0

direct_jj = sp.expand(tr(X*J*Y*J))
pred_jj = sp.expand(-2*(x0*y0-x1*y1-x2*y2-x3*y3))
assert sp.expand(direct_jj - pred_jj) == 0

# ---------- B15: exact parity checks on representative integer complex-linear/transverse blocks ----------
J6 = sp.diag(J,J,J)

def block_matrix(coeffs, kind):
    # 3x3 blocks, each block aI+bJ (commuting) or aK+bL (anticommuting)
    out = sp.zeros(6)
    for i in range(3):
        for j in range(3):
            a,b = coeffs[i][j]
            blk = a*I2 + b*J if kind == 'comm' else a*K + b*L
            out[2*i:2*i+2, 2*j:2*j+2] = blk
    return out

comm_coeffs = [
    [(1,2),(0,1),(2,-1)],
    [(-1,1),(3,0),(1,1)],
    [(2,0),(-2,1),(0,2)],
]
anti_coeffs = [
    [(1,-1),(2,1),(0,1)],
    [(1,0),(-1,2),(2,-2)],
    [(0,2),(1,1),(3,-1)],
]
A0 = block_matrix(comm_coeffs, 'comm')
E = block_matrix(anti_coeffs, 'anti')
assert A0*J6 == J6*A0
assert E*J6 == -J6*E

def Gamma(X):
    return J6*X*J6.T

def Lop(A,X):
    return A*X + X*A.T

# representative + and - parity test matrices
Xplus = block_matrix([
    [(1,0),(2,1),(0,0)],
    [(2,-1),(0,0),(1,2)],
    [(0,0),(1,-2),(3,0)],
], 'comm')
Xminus = block_matrix([
    [(1,1),(0,2),(2,0)],
    [(0,-2),(1,0),(3,1)],
    [(2,0),(3,-1),(0,1)],
], 'anti')
assert Gamma(Xplus) == Xplus
assert Gamma(Xminus) == -Xminus
assert Gamma(Lop(A0,Xplus)) == Lop(A0,Xplus)
assert Gamma(Lop(A0,Xminus)) == -Lop(A0,Xminus)
assert Gamma(Lop(E,Xplus)) == -Lop(E,Xplus)
assert Gamma(Lop(E,Xminus)) == Lop(E,Xminus)

# delta H = L_A0^* L_E + L_E^* L_A0; L_A^*=L_{A^T}
def dH(X):
    return Lop(A0.T, Lop(E,X)) + Lop(E.T, Lop(A0,X))
assert Gamma(dH(Xplus)) == -dH(Xplus)
assert Gamma(dH(Xminus)) == dH(Xminus)
assert tr(Xplus.T*dH(Xplus)) == 0
assert tr(Xminus.T*dH(Xminus)) == 0

print("MOMENT_COUNTERS_PASS")
print("D1 = 4 ||A||_F^2")
print("D2 = 8 (||A^T A||_F^2 + ||A^2||_F^2)")
print("D3 = 16||A^T A A^T||_F^2 + 18||A^T A^2||_F^2 + 18||A^2 A^T||_F^2 + 12||A^3||_F^2")
print("SOURCE_A7_D1_D2_D3 =", *source_moments)
print("RANK4_PAULI_IDENTITIES_PASS")
print("TRANSVERSE_PARITY_IDENTITIES_PASS")
print("ALL_EXACT_CHECKS_PASS")
